#!/usr/bin/env python3
"""Serveur local pour explorer le catalogue SaaS (filtres + RAG léger TF-IDF)."""

from __future__ import annotations

import json
import math
import os
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from catalogue_saas import (  # noqa: E402
    iter_vendors,
    load_frozen_segment_ids,
    load_taxonomy,
)

EXPLORER_DIR = ROOT / "explorer"
IDEAS_PATH = ROOT / "idees" / "catalogue-segments.json"
TOKEN_RE = re.compile(r"[a-z0-9àâäéèêëïîôùûüçœæ]+", re.I)


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def cosine_similarity(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in a)
    norm_a = math.sqrt(sum(v * v for v in a.values()))
    norm_b = math.sqrt(sum(v * v for v in b.values()))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


class TfIdfIndex:
    def __init__(self, documents: list[dict[str, Any]]) -> None:
        self.documents = documents
        self.doc_tokens = [tokenize(doc["text"]) for doc in documents]
        df: Counter[str] = Counter()
        for tokens in self.doc_tokens:
            for token in set(tokens):
                df[token] += 1
        n = len(documents)
        self.idf = {token: math.log((n + 1) / (freq + 1)) + 1.0 for token, freq in df.items()}

    def _vector(self, tokens: list[str]) -> dict[str, float]:
        tf = Counter(tokens)
        return {token: count * self.idf[token] for token, count in tf.items() if token in self.idf}

    def search(self, query: str, top_k: int = 8) -> list[tuple[float, int]]:
        q_vec = self._vector(tokenize(query))
        if not q_vec:
            return []
        scored: list[tuple[float, int]] = []
        for idx, tokens in enumerate(self.doc_tokens):
            score = cosine_similarity(q_vec, self._vector(tokens))
            if score > 0:
                scored.append((score, idx))
        scored.sort(key=lambda item: item[0], reverse=True)
        return scored[:top_k]


def vendor_document_text(vendor: dict[str, Any], seg_labels: dict[str, str]) -> str:
    segments = " ".join(seg_labels.get(s, s) for s in vendor.get("segments", []))
    capabilities = " ".join(vendor.get("capabilities", []))
    parts = [
        vendor.get("name", ""),
        vendor.get("description", ""),
        segments,
        capabilities,
        vendor.get("pricing_model", ""),
        vendor.get("target_market", ""),
        vendor.get("geography", ""),
        vendor.get("hq_country", ""),
        vendor.get("france_market", ""),
        vendor.get("pricing_notes", "") or "",
        vendor.get("notes", "") or "",
    ]
    return " ".join(p for p in parts if p)


def synthesize_local(query: str, hits: list[dict[str, Any]]) -> str:
    if not hits:
        return (
            f"Aucun acteur pertinent trouvé pour « {query} ». "
            "Essayez des termes plus larges (segment, capacité, pays)."
        )
    lines = [f"**{len(hits)} acteur(s)** correspondent à « {query} » :\n"]
    for hit in hits[:6]:
        seg = ", ".join(hit.get("segment_labels", []))
        lines.append(
            f"- **{hit['name']}** — {seg}. {hit['description'][:160].rstrip()}…"
        )
    if len(hits) > 6:
        lines.append(f"\n… et {len(hits) - 6} autre(s) dans les sources ci-dessous.")
    return "\n".join(lines)


def synthesize_openai(query: str, hits: list[dict[str, Any]], api_key: str) -> str:
    context_blocks = []
    for hit in hits[:8]:
        context_blocks.append(
            json.dumps(
                {
                    "name": hit["name"],
                    "url": hit["url"],
                    "segments": hit.get("segment_labels", []),
                    "description": hit["description"],
                    "pricing_model": hit.get("pricing_model"),
                    "target_market": hit.get("target_market"),
                    "hq_country": hit.get("hq_country"),
                    "france_market": hit.get("france_market"),
                    "verification_status": hit.get("verification_status"),
                },
                ensure_ascii=False,
            )
        )
    payload = {
        "model": os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
        "temperature": 0.2,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Tu es un analyste marché SaaS. Réponds en français, de façon factuelle, "
                    "en t'appuyant uniquement sur les fiches fournies. Cite les noms des produits. "
                    "Si l'information manque, dis-le."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Question : {query}\n\nFiches catalogue :\n"
                    + "\n".join(f"- {block}" for block in context_blocks)
                ),
            },
        ],
    }
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"].strip()


class CatalogueStore:
    def __init__(self) -> None:
        self.taxonomy = load_taxonomy()
        self.vendors = iter_vendors()
        self.seg_labels = {s["id"]: s["label"] for s in self.taxonomy["segments"]}
        self.seg_categories = {s["id"]: s.get("category", "") for s in self.taxonomy["segments"]}
        self.cat_labels = {
            c["id"]: c["label"] for c in self.taxonomy.get("categories", [])
        }
        self.frozen_ids = load_frozen_segment_ids()
        self.ideas = self._load_ideas()
        self.rag_index = self._build_rag_index()

    def _load_ideas(self) -> dict[str, list[str]]:
        if not IDEAS_PATH.exists():
            return {}
        data = json.loads(IDEAS_PATH.read_text(encoding="utf-8"))
        return data.get("ideas", {})

    def _build_rag_index(self) -> TfIdfIndex:
        documents = [
            {
                "vendor_id": vendor["id"],
                "text": vendor_document_text(vendor, self.seg_labels),
            }
            for vendor in self.vendors
        ]
        return TfIdfIndex(documents)

    def enrich_vendor(self, vendor: dict[str, Any]) -> dict[str, Any]:
        segments = vendor.get("segments", [])
        return {
            **vendor,
            "segment_labels": [self.seg_labels.get(s, s) for s in segments],
            "categories": sorted(
                {self.cat_labels.get(self.seg_categories.get(s, ""), "") for s in segments}
                - {""}
            ),
            "frozen_segment": any(s in self.frozen_ids for s in segments),
        }

    def segment_stats(self) -> list[dict[str, Any]]:
        counts: Counter[str] = Counter()
        for vendor in self.vendors:
            for seg in vendor.get("segments", []):
                counts[seg] += 1
        rows = []
        for seg in self.taxonomy["segments"]:
            sid = seg["id"]
            rows.append(
                {
                    "id": sid,
                    "label": seg["label"],
                    "category": seg.get("category", ""),
                    "category_label": self.cat_labels.get(seg.get("category", ""), ""),
                    "count": counts.get(sid, 0),
                    "frozen": sid in self.frozen_ids,
                    "description": seg.get("description", ""),
                }
            )
        return rows

    def meta(self) -> dict[str, Any]:
        by_pricing = Counter(v["pricing_model"] for v in self.vendors)
        by_verification = Counter(v["verification_status"] for v in self.vendors)
        by_france = Counter(v.get("france_market", "unknown") for v in self.vendors)
        return {
            "vendor_count": len(self.vendors),
            "segment_count": len(self.taxonomy["segments"]),
            "category_count": len(self.taxonomy.get("categories", [])),
            "frozen_segment_count": len(self.frozen_ids),
            "idea_count": len(self.ideas),
            "pricing_models": self.taxonomy.get("pricing_models", []),
            "target_markets": self.taxonomy.get("target_markets", []),
            "verification_statuses": self.taxonomy.get("verification_statuses", []),
            "france_market_levels": self.taxonomy.get("france_market_levels", []),
            "categories": [
                {"id": c["id"], "label": c["label"]}
                for c in self.taxonomy.get("categories", [])
            ],
            "aggregates": {
                "pricing_model": dict(by_pricing),
                "verification_status": dict(by_verification),
                "france_market": dict(by_france),
            },
            "ideas": self.ideas,
            "llm_available": bool(os.environ.get("OPENAI_API_KEY")),
        }

    def filter_vendors(
        self,
        *,
        q: str = "",
        segment: str | None = None,
        category: str | None = None,
        pricing_model: str | None = None,
        target_market: str | None = None,
        verification_status: str | None = None,
        france_market: str | None = None,
        hq_country: str | None = None,
        limit: int = 200,
        offset: int = 0,
    ) -> dict[str, Any]:
        results = [self.enrich_vendor(v) for v in self.vendors]

        if segment:
            results = [v for v in results if segment in v.get("segments", [])]
        if category:
            results = [
                v
                for v in results
                if category in {self.seg_categories.get(s, "") for s in v.get("segments", [])}
            ]
        if pricing_model:
            results = [v for v in results if v.get("pricing_model") == pricing_model]
        if target_market:
            results = [v for v in results if v.get("target_market") == target_market]
        if verification_status:
            results = [
                v for v in results if v.get("verification_status") == verification_status
            ]
        if france_market:
            results = [v for v in results if v.get("france_market") == france_market]
        if hq_country:
            results = [v for v in results if v.get("hq_country") == hq_country]

        if q.strip():
            q_lower = q.lower()
            scored: list[tuple[float, dict[str, Any]]] = []
            for vendor in results:
                haystack = " ".join(
                    [
                        vendor.get("name", ""),
                        vendor.get("description", ""),
                        " ".join(vendor.get("capabilities", [])),
                        " ".join(vendor.get("segment_labels", [])),
                    ]
                ).lower()
                if q_lower in haystack:
                    scored.append((1.0, vendor))
                    continue
                for rag_score, idx in self.rag_index.search(q, top_k=len(self.vendors)):
                    if self.rag_index.documents[idx]["vendor_id"] == vendor["id"]:
                        scored.append((rag_score, vendor))
                        break
            scored.sort(key=lambda item: item[0], reverse=True)
            results = [vendor for _, vendor in scored]

        total = len(results)
        page = results[offset : offset + limit]
        return {"total": total, "offset": offset, "limit": limit, "vendors": page}

    def ask(self, query: str, top_k: int = 8) -> dict[str, Any]:
        query_tokens = set(tokenize(query))
        scored = self.rag_index.search(query, top_k=top_k * 4)
        vendor_by_id = {v["id"]: self.enrich_vendor(v) for v in self.vendors}
        hits = []
        seen: set[str] = set()
        for score, idx in scored:
            vendor_id = self.rag_index.documents[idx]["vendor_id"]
            if vendor_id in seen:
                continue
            vendor = vendor_by_id[vendor_id]
            boost = 0.0
            for seg in vendor.get("segments", []):
                label_tokens = set(tokenize(self.seg_labels.get(seg, "")))
                if query_tokens & label_tokens:
                    boost += 0.25
                if seg.replace("-", " ") in query.lower() or seg in query.lower():
                    boost += 0.35
            name_tokens = set(tokenize(vendor.get("name", "")))
            if query_tokens & name_tokens:
                boost += 0.2
            final_score = score + boost
            if final_score <= 0:
                continue
            hits.append({**vendor, "relevance": round(final_score, 4)})
            seen.add(vendor_id)
        hits.sort(key=lambda item: item["relevance"], reverse=True)
        hits = hits[:top_k]

        api_key = os.environ.get("OPENAI_API_KEY")
        mode = "openai" if api_key else "local"
        try:
            if api_key:
                answer = synthesize_openai(query, hits, api_key)
            else:
                answer = synthesize_local(query, hits)
        except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError) as exc:
            answer = synthesize_local(query, hits)
            mode = f"local-fallback ({exc.__class__.__name__})"

        return {
            "query": query,
            "answer": answer,
            "mode": mode,
            "sources": hits,
        }


STORE = CatalogueStore()


class ExplorerHandler(BaseHTTPRequestHandler):
    server_version = "CatalogueSaaSExplorer/1.0"

    def log_message(self, fmt: str, *args: Any) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _send_json(self, payload: Any, status: int = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_bytes(self, data: bytes, content_type: str) -> None:
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _read_json_body(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b"{}"
        return json.loads(raw.decode("utf-8"))

    def _serve_static(self, rel_path: str) -> None:
        if rel_path in ("", "/"):
            rel_path = "index.html"
        safe = Path(rel_path).name if "/" not in rel_path else rel_path.lstrip("/")
        file_path = (EXPLORER_DIR / safe).resolve()
        if not str(file_path).startswith(str(EXPLORER_DIR.resolve())):
            self.send_error(HTTPStatus.FORBIDDEN)
            return
        if not file_path.exists() or not file_path.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        content_types = {
            ".html": "text/html; charset=utf-8",
            ".css": "text/css; charset=utf-8",
            ".js": "application/javascript; charset=utf-8",
            ".svg": "image/svg+xml",
        }
        self._send_bytes(file_path.read_bytes(), content_types.get(file_path.suffix, "application/octet-stream"))

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/"):
            params = parse_qs(parsed.query)
            single = {k: v[0] for k, v in params.items()}

            if parsed.path == "/api/meta":
                self._send_json(STORE.meta())
                return
            if parsed.path == "/api/segments":
                self._send_json({"segments": STORE.segment_stats()})
                return
            if parsed.path == "/api/vendors":
                limit = int(single.get("limit", "100"))
                offset = int(single.get("offset", "0"))
                self._send_json(
                    STORE.filter_vendors(
                        q=single.get("q", ""),
                        segment=single.get("segment"),
                        category=single.get("category"),
                        pricing_model=single.get("pricing_model"),
                        target_market=single.get("target_market"),
                        verification_status=single.get("verification_status"),
                        france_market=single.get("france_market"),
                        hq_country=single.get("hq_country"),
                        limit=min(limit, 500),
                        offset=max(offset, 0),
                    )
                )
                return
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        self._serve_static(parsed.path.lstrip("/"))

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/api/ask":
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        body = self._read_json_body()
        query = str(body.get("query", "")).strip()
        if not query:
            self._send_json({"error": "query requis"}, status=HTTPStatus.BAD_REQUEST)
            return
        top_k = int(body.get("top_k", 8))
        self._send_json(STORE.ask(query, top_k=min(max(top_k, 1), 20)))


def main() -> int:
    port = int(os.environ.get("EXPLORER_PORT", "8765"))
    host = os.environ.get("EXPLORER_HOST", "127.0.0.1")
    if not EXPLORER_DIR.exists():
        print(f"Dossier manquant : {EXPLORER_DIR}", file=sys.stderr)
        return 1
    httpd = ThreadingHTTPServer((host, port), ExplorerHandler)
    print(f"Catalogue SaaS Explorer — http://{host}:{port}")
    print(f"  {len(STORE.vendors)} vendeurs · {len(STORE.taxonomy['segments'])} segments")
    if os.environ.get("OPENAI_API_KEY"):
        print("  RAG : synthèse OpenAI activée (OPENAI_API_KEY)")
    else:
        print("  RAG : synthèse locale (définir OPENAI_API_KEY pour LLM)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
