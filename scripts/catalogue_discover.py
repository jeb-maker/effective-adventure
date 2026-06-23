#!/usr/bin/env python3
"""Découverte semi-automatisée de secteurs et acteurs — briefs, data.gouv, priorités."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "catalogue-saas"
TAXONOMY_PATH = CATALOGUE / "taxonomy.json"
KEYWORDS_PATH = CATALOGUE / "discovery-keywords.json"
COVERAGE_PATH = CATALOGUE / "coverage-matrix.json"
FROZEN_PATH = CATALOGUE / "frozen-segments.json"
SEGMENTS_MAP = ROOT / "idees" / "catalogue-segments.json"
PASSES_DIR = CATALOGUE / "passes"

sys.path.insert(0, str(ROOT / "scripts"))
import catalogue_pass_lib as cpl  # noqa: E402
import catalogue_saas as cs  # noqa: E402

USER_AGENT = "effective-adventure-catalogue-discover/1.0"
SOURCE_TYPES = (
    "g2",
    "capterra",
    "crunchbase",
    "analyst_report",
    "alternatives",
    "open_source",
    "geo_digest",
    "official_site",
)


def slugify(text: str) -> str:
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:48] or "candidate"


def load_keywords() -> dict:
    if KEYWORDS_PATH.exists():
        return json.loads(KEYWORDS_PATH.read_text(encoding="utf-8")).get("segments", {})
    return {}


def segment_info(segment_id: str) -> dict:
    taxonomy = cs.load_taxonomy()
    for seg in taxonomy["segments"]:
        if seg["id"] == segment_id:
            return seg
    raise KeyError(f"segment inconnu : {segment_id}")


def default_queries(segment_id: str, seg: dict) -> dict[str, list[str]]:
    label = seg["label"]
    desc = seg.get("description", "")
    base = f"{label} {desc}".strip()
    words = re.findall(r"[a-zA-ZÀ-ÿ0-9]{4,}", base.lower())
    generic = [" ".join(words[:4])] if words else [segment_id.replace("-", " ")]
    return {
        "queries": generic,
        "data_gouv": [segment_id.replace("-", " "), label.split("—")[0].strip()],
    }


def queries_for_segment(segment_id: str) -> dict[str, list[str]]:
    overrides = load_keywords().get(segment_id) or {}
    seg = segment_info(segment_id)
    defaults = default_queries(segment_id, seg)
    return {
        "queries": overrides.get("queries") or defaults["queries"],
        "data_gouv": overrides.get("data_gouv") or defaults["data_gouv"],
    }


def frozen_ids() -> set[str]:
    if not FROZEN_PATH.exists():
        return set()
    data = json.loads(FROZEN_PATH.read_text(encoding="utf-8"))
    return {item["segment_id"] for item in data.get("frozen", [])}


def coverage_gap_count(segment_id: str) -> int:
    if not COVERAGE_PATH.exists():
        return 8
    matrix = json.loads(COVERAGE_PATH.read_text(encoding="utf-8"))
    entry = matrix.get("segments", {}).get(segment_id, {})
    sources = entry.get("sources", {})
    return sum(1 for st in SOURCE_TYPES if not sources.get(st))


def vendor_domains() -> set[str]:
    domains: set[str] = set()
    for v in cs.iter_vendors():
        for url in (v.get("url"), v.get("source_url")):
            d = cs.extract_domain(url or "")
            if d:
                domains.add(d)
    return domains


def vendors_in_segment(segment_id: str) -> list[dict]:
    return [v for v in cs.iter_vendors() if segment_id in v.get("segments", [])]


def known_url(url: str, domains: set[str]) -> bool:
    d = cs.extract_domain(url)
    if not d:
        return False
    if d in domains:
        return True
    for known in domains:
        if d.endswith("." + known) or known.endswith("." + d):
            return True
    return False


def api_get(path: str, params: dict) -> dict:
    qs = urllib.parse.urlencode(params)
    url = f"https://www.data.gouv.fr/api/1/{path}?{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"API data.gouv {path} → HTTP {exc.code}") from exc


def search_data_gouv(kind: str, query: str, *, page_size: int = 15) -> list[dict]:
    payload = api_get(f"{kind}/", {"q": query, "page_size": page_size})
    results: list[dict] = []
    for item in payload.get("data", []):
        page = item.get("page") or ""
        if kind == "reuses":
            url = page if page.startswith("http") else f"https://www.data.gouv.fr{page}"
        else:
            url = page or item.get("link") or ""
        results.append(
            {
                "kind": kind,
                "title": item.get("title") or "(sans titre)",
                "url": url,
                "description": (item.get("description") or "")[:280],
                "query": query,
            }
        )
    return results


def dedupe_results(items: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for item in items:
        key = cs.extract_domain(item["url"]) or item["url"]
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def prioritize_segments(*, retravailler_only: bool = False, limit: int = 20) -> list[dict]:
    retrav = cpl.retravailler_segment_ids()
    frozen = frozen_ids()
    taxonomy = cs.load_taxonomy()
    ranked: list[dict] = []

    for seg in taxonomy["segments"]:
        sid = seg["id"]
        if retravailler_only and sid not in retrav:
            continue
        score = 0
        reasons: list[str] = []
        if sid in retrav:
            score += 100
            reasons.append("idée 🔁")
        if sid in frozen:
            score -= 1000
            reasons.append("gelé")
        else:
            score += 50
        gap = coverage_gap_count(sid)
        if gap > 0:
            score += min(gap * 8, 40)
            reasons.append(f"{gap} source(s) manquante(s)")
        if sid.startswith(("territorial", "public-", "civic-", "open-data", "geospatial", "energy-", "environmental", "electoral", "public-health", "transport-")):
            score += 15
            reasons.append("segment FR")
        count = len(vendors_in_segment(sid))
        partial = sum(1 for v in vendors_in_segment(sid) if v["verification_status"] == "partial")
        if partial > 5:
            score += 10
            reasons.append(f"{partial} partial")
        ranked.append(
            {
                "segment_id": sid,
                "label": seg["label"],
                "score": score,
                "vendor_count": count,
                "reasons": reasons,
            }
        )

    ranked.sort(key=lambda x: (-x["score"], x["segment_id"]))
    return ranked[:limit]


def search_urls(queries: list[str]) -> list[dict]:
    out: list[dict] = []
    for q in queries:
        enc = urllib.parse.quote(q)
        out.append({"source": "g2", "query": q, "url": f"https://www.g2.com/search?query={enc}"})
        out.append(
            {
                "source": "capterra",
                "query": q,
                "url": f"https://www.capterra.com/search/?search={enc}",
            }
        )
        out.append(
            {
                "source": "github",
                "query": q,
                "url": f"https://github.com/search?q={enc}&type=repositories",
            }
        )
        out.append(
            {
                "source": "alternativeto",
                "query": q,
                "url": f"https://alternativeto.net/browse/search/?q={enc}",
            }
        )
    return out


def render_brief(segment_id: str) -> str:
    seg = segment_info(segment_id)
    q = queries_for_segment(segment_id)
    vendors = vendors_in_segment(segment_id)
    verified = sum(1 for v in vendors if v["verification_status"] == "verified")
    partial = len(vendors) - verified
    frozen = "oui" if segment_id in frozen_ids() else "non"
    retrav = "oui" if segment_id in cpl.retravailler_segment_ids() else "non"
    today = date.today().isoformat()

    lines = [
        f"# Brief découverte — `{segment_id}`",
        "",
        f"- **Date** : {today}",
        f"- **Label** : {seg['label']}",
        f"- **Description** : {seg.get('description', '')}",
        f"- **Catalogue** : {len(vendors)} acteurs ({verified} verified, {partial} partial)",
        f"- **Gelé** : {frozen} | **Lié idée 🔁** : {retrav}",
        f"- **Sources coverage manquantes** : {coverage_gap_count(segment_id)}/{len(SOURCE_TYPES)}",
        "",
        "## Acteurs déjà recensés (extrait)",
        "",
    ]
    for v in sorted(vendors, key=lambda x: x["id"])[:15]:
        st = v["verification_status"]
        lines.append(f"- `{v['id']}` — {v['name']} ({st})")
    if len(vendors) > 15:
        lines.append(f"- … +{len(vendors) - 15} autres")
    lines.extend(["", "## Recherches web à lancer (manuel ou agent)", ""])
    for item in search_urls(q["queries"][:3]):
        lines.append(f"- **{item['source']}** ({item['query']}) : {item['url']}")
    lines.extend(
        [
            "",
            "## Scan automatisé data.gouv",
            "",
            "```bash",
            f"python3 scripts/catalogue_discover.py scan {segment_id}",
            f"python3 scripts/catalogue_discover.py scan {segment_id} --manifest > candidates.json",
            "```",
            "",
            "## Checklist cartographie B (§4)",
            "",
            "- [ ] Réutilisations data.gouv.fr",
            "- [ ] Services publics / .gouv.fr",
            "- [ ] Produits commerciaux FR/EU",
            "- [ ] Open source / académique",
            "- [ ] Bricolage (Excel, Zapier…)",
            "",
        ]
    )
    return "\n".join(lines)


def scan_segment(
    segment_id: str,
    *,
    page_size: int = 12,
) -> tuple[list[dict], list[dict]]:
    q = queries_for_segment(segment_id)
    domains = vendor_domains()
    raw: list[dict] = []
    for query in q["data_gouv"]:
        for kind in ("reuses", "dataservices"):
            try:
                raw.extend(search_data_gouv(kind, query, page_size=page_size))
            except RuntimeError as exc:
                print(f"  avertissement : {exc}", file=sys.stderr)
    items = dedupe_results(raw)
    novel, known = [], []
    for item in items:
        bucket = known if known_url(item["url"], domains) else novel
        bucket.append(item)
    return novel, known


def candidate_to_vendor(item: dict, segment_id: str, pass_id: str) -> dict:
    vid = slugify(item["title"])
    today = date.today().isoformat()
    src_type = "official_site" if item["kind"] == "reuses" else "official_site"
    return {
        "id": vid,
        "name": item["title"],
        "url": item["url"],
        "segments": [segment_id],
        "description": item["description"] or f"Entrée découverte {item['kind']} data.gouv.",
        "capabilities": ["france", "open_data"],
        "pricing_model": "freemium",
        "target_market": "self_serve",
        "geography": "france",
        "hq_country": "FR",
        "france_market": "strong",
        "operating_regions": ["FR"],
        "discovery_source": src_type,
        "discovery_pass": pass_id,
        "source_url": item["url"],
        "source_consulted_at": today,
        "verification_status": "partial",
        "notes": f"Découvert auto data.gouv ({item['query']}) — À VALIDER avant merge.",
    }


def cmd_plan(args: argparse.Namespace) -> int:
    rows = prioritize_segments(
        retravailler_only=args.retravailler,
        limit=args.limit,
    )
    print(f"{'Score':>5}  {'Segment':32} {'Cnt':>4}  Priorité")
    print("-" * 72)
    for row in rows:
        reasons = ", ".join(row["reasons"]) or "—"
        print(
            f"{row['score']:5}  {row['segment_id']:32} {row['vendor_count']:4}  {reasons}"
        )
    return 0


def cmd_brief(args: argparse.Namespace) -> int:
    text = render_brief(args.segment)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
        print(f"Écrit : {args.output}")
    else:
        print(text)
    return 0


def cmd_scan(args: argparse.Namespace) -> int:
    novel, known = scan_segment(args.segment, page_size=args.page_size)
    print(f"Segment `{args.segment}` — data.gouv : {len(novel)} nouveau(x), {len(known)} déjà catalogue")
    print()
    if novel:
        print("## Candidats nouveaux (à valider)")
        for item in novel:
            print(f"- [{item['kind']}] {item['title']}")
            print(f"  {item['url']}")
            if item["description"]:
                print(f"  {item['description'][:120]}…")
    if args.show_known and known:
        print()
        print("## Déjà recensés")
        for item in known[:10]:
            print(f"- {item['title']} — {item['url']}")

    if args.manifest:
        pass_id = args.pass_id or f"discover-{args.segment}-{date.today().isoformat()}"
        fname = f"{args.segment}.json"
        manifest = {
            "pass_id": pass_id,
            "date": date.today().isoformat(),
            "description": f"Draft auto data.gouv — {args.segment} (NON VALIDÉ)",
            "additions": {
                fname: [candidate_to_vendor(item, args.segment, pass_id) for item in novel]
            },
            "verify_updates": {},
            "coverage_updates": {},
        }
        out = json.dumps(manifest, indent=2, ensure_ascii=False)
        if args.manifest_output:
            args.manifest_output.write_text(out + "\n", encoding="utf-8")
            print(f"\nManifeste draft : {args.manifest_output}", file=sys.stderr)
        else:
            print(out)
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    """Plan → briefs → scan pour les N segments prioritaires."""
    rows = prioritize_segments(retravailler_only=args.retravailler, limit=args.limit)
    out_dir = args.output_dir or (PASSES_DIR / f"discover-{date.today().isoformat()}")
    out_dir.mkdir(parents=True, exist_ok=True)
    summary: list[dict] = []

    for row in rows:
        sid = row["segment_id"]
        brief_path = out_dir / f"{sid}-brief.md"
        brief_path.write_text(render_brief(sid), encoding="utf-8")
        novel, _ = scan_segment(sid, page_size=args.page_size)
        summary.append({"segment_id": sid, "novel_count": len(novel), "brief": str(brief_path)})
        if novel and args.manifest:
            pass_id = f"discover-{sid}-{date.today().isoformat()}"
            manifest = {
                "pass_id": pass_id,
                "date": date.today().isoformat(),
                "description": f"Draft auto — {sid}",
                "additions": {
                    f"{sid}.json": [
                        candidate_to_vendor(item, sid, pass_id) for item in novel[: args.max_candidates]
                    ]
                },
            }
            mpath = out_dir / f"{sid}.manifest.json"
            mpath.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    index = out_dir / "INDEX.md"
    lines = [
        f"# Découverte {date.today().isoformat()}",
        "",
        "| Segment | Candidats data.gouv | Brief |",
        "|---|---|---|",
    ]
    for row in summary:
        sid = row["segment_id"]
        lines.append(f"| `{sid}` | {row['novel_count']} | [{sid}-brief.md]({sid}-brief.md) |")
    lines.extend(
        [
            "",
            "## Pipeline",
            "",
            "1. Relire chaque brief + candidats manifest",
            "2. Compléter recherches G2/Capterra (URLs dans brief)",
            "3. `python3 scripts/catalogue_pass.py run …manifest.json` après validation",
            "",
        ]
    )
    index.write_text("\n".join(lines), encoding="utf-8")
    print(f"Découverte : {len(rows)} segment(s) → {out_dir}")
    print(f"Index : {index}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Découverte semi-auto de secteurs et acteurs (briefs + data.gouv)"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_plan = sub.add_parser("plan", help="Prioriser les segments à moissonner")
    p_plan.add_argument("--limit", type=int, default=15)
    p_plan.add_argument("--retravailler", action="store_true", help="Segments idées 🔁 seulement")

    p_brief = sub.add_parser("brief", help="Générer un brief de recherche pour un segment")
    p_brief.add_argument("segment")
    p_brief.add_argument("-o", "--output", type=Path)

    p_scan = sub.add_parser("scan", help="Scanner data.gouv (réutilisations + dataservices)")
    p_scan.add_argument("segment")
    p_scan.add_argument("--page-size", type=int, default=12)
    p_scan.add_argument("--show-known", action="store_true")
    p_scan.add_argument("--manifest", action="store_true", help="Émettre un manifeste draft JSON")
    p_scan.add_argument("--manifest-output", type=Path)
    p_scan.add_argument("--pass-id")

    p_run = sub.add_parser("run", help="Plan + briefs + scan data.gouv (batch)")
    p_run.add_argument("--limit", type=int, default=5)
    p_run.add_argument("--retravailler", action="store_true")
    p_run.add_argument("--page-size", type=int, default=10)
    p_run.add_argument("--output-dir", type=Path)
    p_run.add_argument("--manifest", action="store_true")
    p_run.add_argument("--max-candidates", type=int, default=8)

    args = parser.parse_args()
    handlers = {
        "plan": cmd_plan,
        "brief": cmd_brief,
        "scan": cmd_scan,
        "run": cmd_run,
    }
    return handlers[args.command](args)


if __name__ == "__main__":
    raise SystemExit(main())
