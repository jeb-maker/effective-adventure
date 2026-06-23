#!/usr/bin/env python3
"""Collecte depuis sources externes (G2 API, CSV Crunchbase/Capterra) → imports JSON."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPORTS_DIR = ROOT / "catalogue-saas" / "imports"
TAXONOMY_PATH = ROOT / "catalogue-saas" / "taxonomy.json"
SEGMENTS_MAP = ROOT / "idees" / "catalogue-segments.json"

sys.path.insert(0, str(ROOT / "scripts"))
import catalogue_saas as cs  # noqa: E402

USER_AGENT = "effective-adventure-catalogue-collect/1.0"
G2_BASE = "https://data.g2.com"


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:48] or "candidate"


def today() -> str:
    return date.today().isoformat()


def load_g2_categories_for_segment(segment_id: str) -> list[str]:
    """Mapping segment → requêtes G2 (heuristique ; affiner manuellement)."""
    mapping = {
        "regtech": ["regtech", "regulatory compliance"],
        "document-idp": ["document processing", "intelligent document processing"],
        "ai-governance": ["ai governance", "responsible ai"],
        "grc-security": ["grc", "governance risk compliance"],
        "kyc-aml": ["kyc", "aml software"],
        "public-procurement-intel": ["procurement software"],
        "compliance-to-spec": ["compliance management"],
        "parsing-inbox": ["email parsing", "document automation"],
    }
    return mapping.get(segment_id, [segment_id.replace("-", " ")])


def g2_request(path: str, token: str, params: dict | None = None) -> dict:
    qs = urllib.parse.urlencode(params or {})
    url = f"{G2_BASE}{path}" + (f"?{qs}" if qs else "")
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Token token={token}",
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode()[:200]
        raise RuntimeError(f"G2 API {path} → HTTP {exc.code}: {body}") from exc


def normalize_g2_product(item: dict, segment_id: str) -> dict:
    attrs = item.get("attributes") or item
    name = attrs.get("name") or attrs.get("product_name") or "Unknown"
    url = attrs.get("public_detail_url") or attrs.get("url") or attrs.get("g2_url") or ""
    desc = (attrs.get("description") or attrs.get("short_description") or "")[:280]
    pid = slugify(name)
    return {
        "id": pid,
        "name": name,
        "url": url,
        "segments": [segment_id],
        "description": desc or f"Produit G2 — segment {segment_id}.",
        "capabilities": ["g2_listed"],
        "pricing_model": "hybrid",
        "target_market": "mid_market",
        "source_url": url or f"https://www.g2.com/search?query={urllib.parse.quote(name)}",
        "source_consulted_at": today(),
        "discovery_source": "g2",
        "discovery_pass": f"g2-collect-{today()}",
        "verification_status": "partial",
        "entry_ai_generated": True,
        "founded_year": None,
        "notes": f"Collecté G2 API ({today()}) — À VALIDER avant merge.",
        "external_ids": {"g2": str(item.get("id") or attrs.get("id") or "")},
    }


def cmd_g2_search(args: argparse.Namespace) -> int:
    token = os.environ.get("G2_API_TOKEN")
    if not token:
        print(
            "G2_API_TOKEN manquant.\n"
            "  1. https://my.g2.com/developers → Access Tokens\n"
            "  2. export G2_API_TOKEN=…",
            file=sys.stderr,
        )
        return 1

    segment = args.segment
    queries = args.query or load_g2_categories_for_segment(segment)
    existing_domains = {cs.extract_domain(v["url"]) for v in cs.iter_vendors()}

    candidates: list[dict] = []
    seen: set[str] = set()

    for query in queries:
        print(f"G2 search: {query!r}")
        try:
            data = g2_request(
                "/api/v2/products",
                token,
                {"filter[name_cont]": query, "page[size]": str(args.limit)},
            )
        except RuntimeError as exc:
            print(f"  erreur: {exc}", file=sys.stderr)
            continue

        items = data.get("data") or []
        if isinstance(data, list):
            items = data
        for item in items:
            cand = normalize_g2_product(item, segment)
            domain = cs.extract_domain(cand["url"])
            key = domain or cand["id"]
            if key in seen or (domain and domain in existing_domains):
                continue
            seen.add(key)
            candidates.append(cand)
            if len(candidates) >= args.limit:
                break
        if len(candidates) >= args.limit:
            break

    out_path = IMPORTS_DIR / f"g2-{segment}-{today()}.json"
    IMPORTS_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": "g2",
        "segment": segment,
        "collected_at": today(),
        "query": queries,
        "count": len(candidates),
        "candidates": candidates,
    }
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Écrit {len(candidates)} candidat(s) → {out_path}")
    return 0


def read_csv_rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def pick_col(row: dict, *names: str) -> str:
    lower_map = {k.lower().strip(): v for k, v in row.items() if k}
    for name in names:
        for key, val in lower_map.items():
            if name in key and val:
                return str(val).strip()
    return ""


def parse_year(value: str) -> int | None:
    if not value:
        return None
    m = re.search(r"(19|20)\d{2}", value)
    if m:
        return int(m.group(0))
    return None


def cmd_import_csv(args: argparse.Namespace) -> int:
    path = Path(args.csv)
    if not path.exists():
        print(f"Fichier introuvable : {path}", file=sys.stderr)
        return 1

    rows = read_csv_rows(path)
    vendors_by_domain: dict[str, dict] = {}
    for v in cs.iter_vendors():
        d = cs.extract_domain(v["url"])
        if d:
            vendors_by_domain[d] = v

    enrichments: list[dict] = []
    new_candidates: list[dict] = []

    for row in rows:
        name = pick_col(row, "name", "organization", "company")
        url = pick_col(row, "website", "url", "homepage")
        if url and not url.startswith("http"):
            url = f"https://{url}"
        domain = cs.extract_domain(url)
        founded = parse_year(pick_col(row, "founded", "founded_on", "founded date"))
        desc = pick_col(row, "description", "short_description")[:280]
        location = pick_col(row, "location", "headquarters", "hq")

        if domain and domain in vendors_by_domain:
            enrichments.append(
                {
                    "id": vendors_by_domain[domain]["id"],
                    "domain": domain,
                    "founded_year": founded,
                    "founded_year_source": f"{args.source} CSV {path.name}",
                    "notes_append": f"Enrichi {args.source} CSV ({today()}).",
                }
            )
        elif name and url:
            seg = args.segment or "regtech"
            new_candidates.append(
                {
                    "id": slugify(name),
                    "name": name,
                    "url": url,
                    "segments": [seg],
                    "description": desc or f"Import {args.source} — {name}.",
                    "capabilities": ["france" if "FR" in location.upper() else "global"],
                    "pricing_model": "hybrid",
                    "target_market": "mid_market",
                    "source_url": url,
                    "source_consulted_at": today(),
                    "discovery_source": args.source,
                    "discovery_pass": f"csv-import-{today()}",
                    "verification_status": "partial",
                    "entry_ai_generated": True,
                    "founded_year": founded,
                    "founded_year_source": f"{args.source} CSV {path.name}" if founded else None,
                    "notes": f"Import CSV {args.source} ({today()}) — À VALIDER.",
                }
            )

    out_path = IMPORTS_DIR / f"{args.source}-{path.stem}-{today()}.json"
    IMPORTS_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": args.source,
        "csv": str(path),
        "collected_at": today(),
        "enrichments": enrichments,
        "new_candidates": new_candidates,
    }
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"CSV {path.name}: {len(enrichments)} enrichissement(s), "
        f"{len(new_candidates)} nouveau(x) → {out_path}"
    )
    return 0


def cmd_merge_imports(args: argparse.Namespace) -> int:
    """Applique enrichments founded_year depuis imports/*.json."""
    if not IMPORTS_DIR.exists():
        print("Aucun dossier imports/")
        return 0

    overrides_path = ROOT / "catalogue-saas" / "founded-years-overrides.json"
    overrides = json.loads(overrides_path.read_text(encoding="utf-8")) if overrides_path.exists() else {
        "version": "1.0.0",
        "vendors": {},
    }
    vendor_map = overrides.setdefault("vendors", {})
    applied = 0

    for path in sorted(IMPORTS_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for item in data.get("enrichments", []):
            vid = item.get("id")
            year = item.get("founded_year")
            if not vid or not year:
                continue
            vendor_map[vid] = {
                "founded_year": year,
                "founded_year_source": item.get("founded_year_source", str(path)),
            }
            applied += 1

    if applied and not args.dry_run:
        overrides["updated_at"] = today()
        overrides_path.write_text(
            json.dumps(overrides, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(f"Overrides founded_year: +{applied} → {overrides_path}")
        print("Relancer: python3 scripts/tag_catalogue_provenance_v1.py")
    elif args.dry_run:
        print(f"Dry-run: {applied} enrichissement(s) prêts")
    else:
        print("Aucun enrichissement à merger")

    new_total = sum(len(json.loads(p.read_text()).get("new_candidates", [])) for p in IMPORTS_DIR.glob("*.json"))
    g2_total = sum(len(json.loads(p.read_text()).get("candidates", [])) for p in IMPORTS_DIR.glob("g2-*.json"))
    print(f"Candidats nouveaux (CSV) en attente manifeste : {new_total}")
    print(f"Candidats G2 en attente manifeste : {g2_total}")
    return 0


def cmd_status(_: argparse.Namespace) -> int:
    print("Sources externes — état")
    print(f"  G2_API_TOKEN : {'défini' if os.environ.get('G2_API_TOKEN') else 'absent'}")
    if IMPORTS_DIR.exists():
        files = sorted(IMPORTS_DIR.glob("*.json"))
        print(f"  imports/     : {len(files)} fichier(s)")
        for p in files[-5:]:
            print(f"    - {p.name}")
    else:
        print("  imports/     : vide")
    print()
    print("Doc : docs/catalogue-saas-sources-externes.md")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Collecte G2 / CSV → catalogue imports")
    sub = parser.add_subparsers(dest="command", required=True)

    p_g2 = sub.add_parser("g2-search", help="Recherche produits G2 (API token requis)")
    p_g2.add_argument("--segment", required=True)
    p_g2.add_argument("--query", action="append")
    p_g2.add_argument("--limit", type=int, default=20)

    p_csv = sub.add_parser("import-csv", help="Import CSV Crunchbase/Capterra")
    p_csv.add_argument("csv", type=Path)
    p_csv.add_argument("--source", choices=["crunchbase", "capterra", "g2"], default="crunchbase")
    p_csv.add_argument("--segment", help="Segment cible pour nouveaux candidats")

    p_merge = sub.add_parser("merge-imports", help="Merger enrichments founded_year → overrides")
    p_merge.add_argument("--dry-run", action="store_true")

    sub.add_parser("status", help="État token + imports")

    args = parser.parse_args()
    handlers = {
        "g2-search": cmd_g2_search,
        "import-csv": cmd_import_csv,
        "merge-imports": cmd_merge_imports,
        "status": cmd_status,
    }
    return handlers[args.command](args)


if __name__ == "__main__":
    raise SystemExit(main())
