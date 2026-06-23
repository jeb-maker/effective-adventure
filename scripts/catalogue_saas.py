#!/usr/bin/env python3
"""Outils pour le catalogue SaaS (validation, stats, export, SQLite)."""

from __future__ import annotations

import argparse
import csv
import json
import sqlite3
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "catalogue-saas"
TAXONOMY_PATH = CATALOGUE / "taxonomy.json"
VENDORS_DIR = CATALOGUE / "vendors"
COVERAGE_PATH = CATALOGUE / "coverage-matrix.json"
FROZEN_SEGMENTS_PATH = CATALOGUE / "frozen-segments.json"

META_PASS_MARKERS = ("v5e-retrospective", "v5o-coverage")
NEAR_THRESHOLD_PCT = 8.0
INVENTORY_DEPTH_MIN = 18

LISTICLE_PATTERNS = (
    "/blog/",
    "/post/",
    "best-",
    "top-",
    "alternatives",
    "pickaxe.co",
    "modulos.ai",
    "riskpublishing.com",
    "zylos.ai/research",
    "dancumberlandlabs.com/blog",
)


def load_taxonomy() -> dict:
    with TAXONOMY_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def load_vendor_files() -> list[tuple[str, dict]]:
    files: list[tuple[str, dict]] = []
    for path in sorted(VENDORS_DIR.glob("*.json")):
        with path.open(encoding="utf-8") as f:
            files.append((path.name, json.load(f)))
    return files


def iter_vendors() -> list[dict]:
    vendors: list[dict] = []
    for _, data in load_vendor_files():
        vendors.extend(data.get("vendors", []))
    return vendors


def extract_domain(url: str) -> str:
    if not url:
        return ""
    parsed = urlparse(url if "://" in url else f"https://{url}")
    host = (parsed.netloc or parsed.path.split("/")[0]).lower()
    if host.startswith("www."):
        host = host[4:]
    return host


def is_listicle_source(source_url: str, product_url: str = "") -> bool:
    """True si la source ressemble à un listicle — sauf si c'est le site officiel du produit."""
    if product_url and domains_match(product_url, source_url):
        return False
    lower = source_url.lower()
    return any(pattern in lower for pattern in LISTICLE_PATTERNS)


def domains_match(product_url: str, source_url: str) -> bool:
    product_domain = extract_domain(product_url)
    source_domain = extract_domain(source_url)
    return bool(product_domain and source_domain and product_domain == source_domain)


def load_frozen_segment_ids() -> set[str]:
    if not FROZEN_SEGMENTS_PATH.exists():
        return set()
    data = json.loads(FROZEN_SEGMENTS_PATH.read_text(encoding="utf-8"))
    return {item["segment_id"] for item in data.get("frozen", [])}


def validate() -> int:
    taxonomy = load_taxonomy()
    segment_ids = {s["id"] for s in taxonomy["segments"]}
    pricing_models = set(taxonomy["pricing_models"])
    target_markets = set(taxonomy["target_markets"])
    statuses = set(taxonomy["verification_statuses"])
    france_markets = set(taxonomy.get("france_market_levels", []))
    discovery_sources = set(taxonomy.get("discovery_sources", []))

    errors: list[str] = []
    seen_ids: set[str] = set()

    required = {
        "id",
        "name",
        "url",
        "segments",
        "description",
        "capabilities",
        "pricing_model",
        "target_market",
        "source_url",
        "source_consulted_at",
        "verification_status",
    }

    for filename, data in load_vendor_files():
        stem = Path(filename).stem
        if stem not in segment_ids:
            errors.append(f"{filename}: fichier hors taxonomie (orphelin)")

        for i, vendor in enumerate(data.get("vendors", [])):
            prefix = f"{filename}[{i}] {vendor.get('id', '?')}"

            missing = required - vendor.keys()
            if missing:
                errors.append(f"{prefix}: champs manquants {sorted(missing)}")
                continue

            vid = vendor["id"]
            if vid in seen_ids:
                errors.append(f"{prefix}: id dupliqué '{vid}'")
            seen_ids.add(vid)

            for seg in vendor["segments"]:
                if seg not in segment_ids:
                    errors.append(f"{prefix}: segment inconnu '{seg}'")

            if vendor["pricing_model"] not in pricing_models:
                errors.append(
                    f"{prefix}: pricing_model inconnu '{vendor['pricing_model']}'"
                )

            if vendor["target_market"] not in target_markets:
                errors.append(
                    f"{prefix}: target_market inconnu '{vendor['target_market']}'"
                )

            if vendor["verification_status"] not in statuses:
                errors.append(
                    f"{prefix}: verification_status invalide"
                )

            if "hq_country" in vendor:
                hq = vendor["hq_country"]
                if not (hq == "unknown" or (len(hq) == 2 and hq.isalpha() and hq.isupper())):
                    errors.append(f"{prefix}: hq_country invalide '{hq}'")

            if "france_market" in vendor:
                if vendor["france_market"] not in france_markets:
                    errors.append(
                        f"{prefix}: france_market invalide '{vendor['france_market']}'"
                    )

            if "discovery_source" in vendor and discovery_sources:
                if vendor["discovery_source"] not in discovery_sources:
                    errors.append(
                        f"{prefix}: discovery_source invalide '{vendor['discovery_source']}'"
                    )

            if len(vendor["description"]) < 10:
                errors.append(f"{prefix}: description trop courte")

    for seg_id in sorted(segment_ids):
        vendor_file = VENDORS_DIR / f"{seg_id}.json"
        if not vendor_file.exists():
            errors.append(f"segment '{seg_id}': fichier manquant vendors/{seg_id}.json")

    if errors:
        print("VALIDATION ÉCHOUÉE", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK — {len(seen_ids)} vendeurs, {len(load_vendor_files())} fichiers segment")
    return 0


def stats() -> None:
    vendors = iter_vendors()
    taxonomy = load_taxonomy()
    segments = taxonomy["segments"]
    categories = {c["id"]: c["label"] for c in taxonomy.get("categories", [])}
    seg_labels = {s["id"]: s["label"] for s in segments}

    print(f"Total vendeurs : {len(vendors)}")
    print(f"Segments taxonomie : {len(segments)}")
    print()

    by_segment: Counter[str] = Counter()
    for v in vendors:
        for seg in v["segments"]:
            by_segment[seg] += 1

    by_category: Counter[str] = Counter()
    empty = 0
    for seg in segments:
        sid = seg["id"]
        count = by_segment.get(sid, 0)
        if count == 0:
            empty += 1
        by_category[seg.get("category", "?")] += 1

    print(f"Segments peuplés : {len(segments) - empty} / {len(segments)} (vides : {empty})")
    print()

    current_cat = None
    for seg in segments:
        cat = seg.get("category", "?")
        if cat != current_cat:
            current_cat = cat
            print(f"## {categories.get(cat, cat)}")
        sid = seg["id"]
        count = by_segment.get(sid, 0)
        flag = "" if count else " [vide]"
        print(f"  {sid:32} {count:3}  {seg['label']}{flag}")

    print()
    print("Par pricing_model :")
    for model, count in Counter(v["pricing_model"] for v in vendors).most_common():
        print(f"  {model:20} {count}")

    print()
    print("Par verification_status :")
    for status, count in Counter(
        v["verification_status"] for v in vendors
    ).most_common():
        print(f"  {status:12} {count}")

    listicle_count = sum(
        1 for v in vendors if is_listicle_source(v["source_url"], v["url"])
    )
    by_verification = Counter(v["verification_status"] for v in vendors)
    eligible = sum(
        1
        for v in vendors
        if v["verification_status"] == "partial"
        and domains_match(v["url"], v["source_url"])
        and not is_listicle_source(v["source_url"], v["url"])
    )

    print()
    print("Vérification / sources :")
    for status in ("verified", "partial", "unverified"):
        if by_verification.get(status):
            print(f"  {status:20} {by_verification[status]}")
    print(f"  {'listicle-sourced':20} {listicle_count}")
    print(f"  {'promotion candidates':20} {eligible}  (partial + domaine officiel)")

    print()
    if any("hq_country" in v for v in vendors):
        print("Par hq_country :")
        for hq, count in Counter(
            v.get("hq_country", "(absent)") for v in vendors
        ).most_common(10):
            print(f"  {hq:12} {count}")

    if any("france_market" in v for v in vendors):
        print()
        print("Par france_market :")
        for fm, count in Counter(
            v.get("france_market", "(absent)") for v in vendors
        ).most_common():
            print(f"  {fm:12} {count}")


def write_segments_markdown(output: Path) -> None:
    taxonomy = load_taxonomy()
    vendors = iter_vendors()
    by_segment: Counter[str] = Counter()
    for v in vendors:
        for seg in v["segments"]:
            by_segment[seg] += 1

    categories = {c["id"]: c["label"] for c in taxonomy.get("categories", [])}
    lines = [
        "# Segments du catalogue SaaS",
        "",
        f"Généré depuis `taxonomy.json` — **{len(taxonomy['segments'])} segments**.",
        "",
    ]
    current_cat = None
    for seg in taxonomy["segments"]:
        cat = seg.get("category", "?")
        if cat != current_cat:
            current_cat = cat
            lines.extend(["", f"## {categories.get(cat, cat)}", ""])
            lines.append("| ID | Label | Vendeurs |")
            lines.append("|---|---|---:|")
        sid = seg["id"]
        count = by_segment.get(sid, 0)
        lines.append(f"| `{sid}` | {seg['label']} | {count} |")
    lines.append("")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def export_csv(output: Path) -> None:
    vendors = iter_vendors()
    output.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "id",
        "name",
        "url",
        "segments",
        "description",
        "capabilities",
        "pricing_model",
        "pricing_notes",
        "target_market",
        "geography",
        "hq_country",
        "france_market",
        "operating_regions",
        "discovery_source",
        "discovery_pass",
        "verification_status",
        "source_url",
        "source_consulted_at",
        "notes",
    ]

    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for v in vendors:
            row = {k: v.get(k, "") for k in fieldnames}
            row["segments"] = "|".join(v["segments"])
            row["capabilities"] = "|".join(v["capabilities"])
            regions = v.get("operating_regions")
            row["operating_regions"] = "|".join(regions) if regions else ""
            writer.writerow(row)

    print(f"Export CSV : {output} ({len(vendors)} lignes)")


def build_db(db_path: Path) -> None:
    vendors = iter_vendors()
    db_path.parent.mkdir(parents=True, exist_ok=True)

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE vendors (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            url TEXT NOT NULL,
            segments TEXT NOT NULL,
            description TEXT NOT NULL,
            capabilities TEXT NOT NULL,
            pricing_model TEXT NOT NULL,
            pricing_notes TEXT,
            target_market TEXT NOT NULL,
            geography TEXT,
            verification_status TEXT NOT NULL,
            source_url TEXT NOT NULL,
            source_consulted_at TEXT NOT NULL,
            notes TEXT
        )
        """
    )

    for v in vendors:
        cur.execute(
            """
            INSERT INTO vendors VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                v["id"],
                v["name"],
                v["url"],
                json.dumps(v["segments"]),
                v["description"],
                json.dumps(v["capabilities"]),
                v["pricing_model"],
                v.get("pricing_notes"),
                v["target_market"],
                v.get("geography"),
                v["verification_status"],
                v["source_url"],
                v["source_consulted_at"],
                v.get("notes"),
            ),
        )

    conn.commit()
    conn.close()
    print(f"SQLite : {db_path} ({len(vendors)} lignes)")


def coverage_report() -> None:
    if not COVERAGE_PATH.exists():
        print(f"Fichier manquant : {COVERAGE_PATH}", file=sys.stderr)
        raise SystemExit(1)

    matrix = json.loads(COVERAGE_PATH.read_text(encoding="utf-8"))
    taxonomy = load_taxonomy()
    seg_labels = {s["id"]: s["label"] for s in taxonomy["segments"]}
    source_types = matrix.get("source_types", [])
    threshold = matrix.get("saturation_threshold_pct", 5)

    print(f"Matrice couverture — {len(matrix['segments'])} segments")
    print(f"Seuil saturation : {threshold} % de nouveaux / passe")
    print()

    incomplete_l2 = 0
    for seg in taxonomy["segments"]:
        sid = seg["id"]
        entry = matrix["segments"].get(sid, {})
        level = entry.get("target_level", "?")
        sources = entry.get("sources", {})
        done = sum(1 for st in source_types if sources.get(st))
        flag = "" if done >= 4 or level == "L1" else " [incomplet]"
        if done < 4 and level in ("L2", "L3"):
            incomplete_l2 += 1
        print(
            f"  {sid:32} {level:3}  sources {done}/{len(source_types)}{flag}"
            f"  — {seg_labels[sid]}"
        )

    print()
    print(f"Segments L2/L3 avec < 4 sources : {incomplete_l2}")


def gaps_report(
    hq: str | None = None,
    france_market: str | None = None,
    segment: str | None = None,
) -> None:
    taxonomy = load_taxonomy()
    seg_labels = {s["id"]: s["label"] for s in taxonomy["segments"]}
    vendors = iter_vendors()

    by_segment: dict[str, list[dict]] = {s["id"]: [] for s in taxonomy["segments"]}
    for v in vendors:
        for seg in v["segments"]:
            by_segment.setdefault(seg, []).append(v)

    targets = [segment] if segment else [s["id"] for s in taxonomy["segments"]]

    print("Analyse des gaps par segment")
    if hq:
        print(f"  filtre hq_country = {hq}")
    if france_market:
        print(f"  filtre france_market = {france_market}")
    print()

    for sid in targets:
        if sid not in seg_labels:
            print(f"Segment inconnu : {sid}", file=sys.stderr)
            continue
        seg_vendors = by_segment.get(sid, [])
        filtered = seg_vendors
        if hq:
            filtered = [v for v in filtered if v.get("hq_country") == hq]
        if france_market:
            filtered = [v for v in filtered if v.get("france_market") == france_market]

        fr_count = sum(1 for v in seg_vendors if v.get("hq_country") == "FR")
        absent_count = sum(
            1 for v in seg_vendors if v.get("france_market") == "absent"
        )
        unknown_count = sum(
            1 for v in seg_vendors if v.get("france_market") == "unknown"
        )

        if segment or fr_count == 0 or absent_count >= 3:
            print(f"## {sid} — {seg_labels[sid]}")
            print(
                f"   total={len(seg_vendors)}  hq_FR={fr_count}  "
                f"france_absent={absent_count}  france_unknown={unknown_count}"
            )
            if filtered and (hq or france_market):
                print(f"   matching ({len(filtered)}):")
                for v in filtered[:8]:
                    print(
                        f"     - {v['name']} "
                        f"[hq={v.get('hq_country','?')}, "
                        f"fr={v.get('france_market','?')}]"
                    )
                if len(filtered) > 8:
                    print(f"     … +{len(filtered) - 8} autres")
            if fr_count == 0 and len(seg_vendors) > 0:
                print("   >> aucun acteur HQ France")
            print()


def load_coverage_matrix() -> dict:
    if not COVERAGE_PATH.exists():
        print(f"Fichier manquant : {COVERAGE_PATH}", file=sys.stderr)
        raise SystemExit(1)
    return json.loads(COVERAGE_PATH.read_text(encoding="utf-8"))


def is_meta_pass(pass_id: str) -> bool:
    return any(marker in pass_id for marker in META_PASS_MARKERS)


def segment_pass_metrics(
    entry: dict, pass_id: str
) -> tuple[int, int, float] | None:
    total_cand = 0
    total_new = 0
    for src_data in entry.get("sources", {}).values():
        if not src_data or not isinstance(src_data, dict):
            continue
        if src_data.get("pass") != pass_id:
            continue
        total_cand += src_data.get("candidates_found", 0)
        total_new += src_data.get("new_added", 0)
    if total_cand == 0:
        return None
    return total_new, total_cand, 100.0 * total_new / total_cand


def effective_last_pass(entry: dict) -> str | None:
    last = entry.get("last_pass")
    if last and not is_meta_pass(last):
        return last
    real_passes = [
        src_data.get("pass")
        for src_data in entry.get("sources", {}).values()
        if src_data
        and isinstance(src_data, dict)
        and src_data.get("pass")
        and not is_meta_pass(src_data["pass"])
    ]
    return max(real_passes) if real_passes else None


def saturation_flag(rate: float, threshold: float) -> str:
    if rate < threshold:
        return " [SATURÉ]"
    if rate <= NEAR_THRESHOLD_PCT:
        return " [PROCHE]"
    return ""


def collect_saturation_rows(
    matrix: dict, taxonomy: dict, *, real_passes_only: bool
) -> list[dict]:
    seg_labels = {s["id"]: s["label"] for s in taxonomy["segments"]}
    rows: list[dict] = []
    for seg in taxonomy["segments"]:
        sid = seg["id"]
        entry = matrix["segments"].get(sid, {})
        pass_id = (
            effective_last_pass(entry)
            if real_passes_only
            else entry.get("last_pass")
        )
        if not pass_id:
            continue
        if real_passes_only and is_meta_pass(pass_id):
            continue
        metrics = segment_pass_metrics(entry, pass_id)
        if metrics is None:
            continue
        new, cand, rate = metrics
        rows.append(
            {
                "segment_id": sid,
                "label": seg_labels[sid],
                "pass_id": pass_id,
                "rate": rate,
                "new": new,
                "candidates": cand,
            }
        )
    return rows


def _print_saturation_by_pass(
    rows: list[dict], threshold: float, header: str
) -> None:
    by_pass: dict[str, list[dict]] = {}
    for row in rows:
        by_pass.setdefault(row["pass_id"], []).append(row)

    print(header)
    print(
        f"Seuils : [SATURÉ] < {threshold:g} %  |  "
        f"[PROCHE] {threshold:g}–{NEAR_THRESHOLD_PCT:g} %"
    )
    print()

    for pass_id in sorted(by_pass.keys()):
        print(f"## {pass_id}")
        for row in sorted(by_pass[pass_id], key=lambda r: r["rate"]):
            flag = saturation_flag(row["rate"], threshold)
            print(
                f"  {row['segment_id']:32} {row['rate']:5.1f}%  "
                f"(+{row['new']}/{row['candidates']}){flag}"
                f"  — {row['label']}"
            )
        print()


def saturation_report() -> None:
    matrix = load_coverage_matrix()
    taxonomy = load_taxonomy()
    threshold = matrix.get("saturation_threshold_pct", 5)
    rows = [
        row
        for row in collect_saturation_rows(matrix, taxonomy, real_passes_only=False)
        if "v5e-retrospective" not in row["pass_id"]
    ]
    _print_saturation_by_pass(
        rows,
        threshold,
        f"Saturation par passe (seuil gel : < {threshold} % nouveaux / candidats)",
    )


def saturation_watch() -> None:
    matrix = load_coverage_matrix()
    taxonomy = load_taxonomy()
    threshold = matrix.get("saturation_threshold_pct", 5)
    rows = collect_saturation_rows(matrix, taxonomy, real_passes_only=True)
    _print_saturation_by_pass(
        rows,
        threshold,
        "Surveillance saturation — dernière passe réelle par segment",
    )

    saturated = sum(1 for r in rows if r["rate"] < threshold)
    near = sum(
        1 for r in rows if threshold <= r["rate"] <= NEAR_THRESHOLD_PCT
    )
    print(f"Résumé : {saturated} saturé(s), {near} proche(s) du seuil")


def saturation_freeze() -> int:
    matrix = load_coverage_matrix()
    taxonomy = load_taxonomy()
    threshold = matrix.get("saturation_threshold_pct", 5)
    today = date.today().isoformat()
    rows = collect_saturation_rows(matrix, taxonomy, real_passes_only=True)

    frozen = [
        {
            "segment_id": row["segment_id"],
            "label": row["label"],
            "last_real_pass": row["pass_id"],
            "new_rate_pct": round(row["rate"], 2),
            "new_added": row["new"],
            "candidates_found": row["candidates"],
            "frozen_at": today,
        }
        for row in rows
        if row["rate"] < threshold
    ]
    frozen.sort(key=lambda item: (item["new_rate_pct"], item["segment_id"]))

    payload = {
        "version": "1.0.0",
        "updated_at": today,
        "saturation_threshold_pct": threshold,
        "near_threshold_pct": NEAR_THRESHOLD_PCT,
        "meta_passes_excluded": list(META_PASS_MARKERS),
        "frozen_count": len(frozen),
        "frozen": frozen,
    }
    FROZEN_SEGMENTS_PATH.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Écrit : {FROZEN_SEGMENTS_PATH} — "
        f"{len(frozen)} segment(s) gelé(s) (< {threshold} %)"
    )
    return len(frozen)


def audit_sources() -> None:
    vendors = iter_vendors()
    flagged = [v for v in vendors if is_listicle_source(v["source_url"], v["url"])]

    print(f"Audit sources listicle / agrégateur — {len(flagged)} / {len(vendors)} vendeurs")
    print()
    print("Par verification_status :")
    for status, count in Counter(v["verification_status"] for v in flagged).most_common():
        print(f"  {status:12} {count}")

    print()
    print("Top domaines source :")
    domain_counts = Counter(extract_domain(v["source_url"]) for v in flagged)
    for domain, count in domain_counts.most_common(15):
        print(f"  {domain:40} {count}")

    print()
    print("Exemples :")
    for v in flagged[:20]:
        print(f"  {v['id']:32} {extract_domain(v['source_url']):24}  {v['source_url'][:72]}")
    if len(flagged) > 20:
        print(f"  … +{len(flagged) - 20} autres")


def verify_eligible() -> None:
    vendors = iter_vendors()
    listicle_count = sum(
        1 for v in vendors if is_listicle_source(v["source_url"], v["url"])
    )

    eligible = [
        v
        for v in vendors
        if v["verification_status"] == "partial"
        and domains_match(v["url"], v["source_url"])
        and not is_listicle_source(v["source_url"], v["url"])
    ]
    verified = [v for v in vendors if v["verification_status"] == "verified"]

    print("Candidats promotion → verified (partial, domaine officiel, hors listicle)")
    print(f"  {len(eligible)} entrée(s)")
    print()
    for v in sorted(eligible, key=lambda item: item["id"])[:30]:
        print(f"  {v['id']:32} {extract_domain(v['url']):24}  {v['name']}")
    if len(eligible) > 30:
        print(f"  … +{len(eligible) - 30} autres")

    print()
    print(f"Déjà verified — {len(verified)} entrée(s)")
    for v in sorted(verified, key=lambda item: item["id"])[:15]:
        domain = extract_domain(v["url"])
        flag = " [listicle src]" if is_listicle_source(v["source_url"], v["url"]) else ""
        print(f"  {v['id']:32} {domain:24}  {v['name']}{flag}")
    if len(verified) > 15:
        print(f"  … +{len(verified) - 15} autres")

    print()
    print(
        f"Résumé : {len(eligible)} éligible(s) promotion, "
        f"{len(verified)} verified, {listicle_count} listicle-sourced"
    )


def segment_readiness() -> None:
    matrix = load_coverage_matrix()
    taxonomy = load_taxonomy()
    threshold = matrix.get("saturation_threshold_pct", 5)
    frozen_ids = load_frozen_segment_ids()

    vendors = iter_vendors()
    by_segment: Counter[str] = Counter()
    for v in vendors:
        for seg in v["segments"]:
            by_segment[seg] += 1

    inventory_ready = 0
    saturated_count = 0
    l3_ready = 0
    l3_targets = 0

    print(
        f"Préparation segments — profondeur ≥ {INVENTORY_DEPTH_MIN}, "
        f"saturation < {threshold:g} % (dernière passe réelle)"
    )
    print(
        f"{'Segment':32} {'Cnt':>4} {'Lvl':>3} {'Rate':>6} {'Gelé':>5}  "
        f"{'Inventaire':12} {'Saturation':12} {'L3 ready':8}"
    )
    print("-" * 96)

    for seg in taxonomy["segments"]:
        sid = seg["id"]
        entry = matrix["segments"].get(sid, {})
        target_level = entry.get("target_level", "?")
        count = by_segment.get(sid, 0)
        frozen = sid in frozen_ids

        pass_id = effective_last_pass(entry)
        rate: float | None = None
        if pass_id:
            metrics = segment_pass_metrics(entry, pass_id)
            if metrics:
                _, _, rate = metrics

        inventory_ok = count >= INVENTORY_DEPTH_MIN
        saturation_ok = rate is not None and rate < threshold
        l3_ok = target_level == "L3" and saturation_ok

        if inventory_ok:
            inventory_ready += 1
        if saturation_ok:
            saturated_count += 1
        if target_level == "L3":
            l3_targets += 1
            if l3_ok:
                l3_ready += 1

        rate_str = f"{rate:.1f}%" if rate is not None else "  n/a"
        inv_flag = "≥18" if inventory_ok else f"<{INVENTORY_DEPTH_MIN}"
        sat_flag = "OUI" if saturation_ok else "non"
        l3_flag = "OUI" if l3_ok else ("—" if target_level != "L3" else "non")
        frozen_str = "oui" if frozen else "—"

        print(
            f"  {sid:32} {count:4} {target_level:>3} {rate_str:>6} {frozen_str:>5}  "
            f"{inv_flag:12} {sat_flag:12} {l3_flag:8}  — {seg['label'][:40]}"
        )

    total = len(taxonomy["segments"])
    print()
    print(
        f"Résumé : {inventory_ready}/{total} segments profondeur inventaire "
        f"(≥ {INVENTORY_DEPTH_MIN}), "
        f"{saturated_count}/{total} segments saturés"
    )
    print(
        f"         L3 ready (saturation, pas profondeur seule) : "
        f"{l3_ready}/{l3_targets} segments cible L3"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Catalogue SaaS — outils")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="Valider JSON et références taxonomy")
    sub.add_parser("stats", help="Statistiques par segment")
    sub.add_parser("list-segments", help="Lister tous les segments (markdown)")

    p_export = sub.add_parser("export", help="Exporter en CSV")
    p_export.add_argument("--format", choices=["csv"], default="csv")
    p_export.add_argument(
        "-o",
        "--output",
        type=Path,
        default=CATALOGUE / "exports" / "vendors.csv",
    )

    p_db = sub.add_parser("build-db", help="Générer SQLite")
    p_db.add_argument(
        "--db",
        type=Path,
        default=CATALOGUE / "catalogue.db",
    )

    sub.add_parser("coverage", help="Rapport matrice sources par segment")

    p_gaps = sub.add_parser("gaps", help="Segments sans acteur FR ou marché absent")
    p_gaps.add_argument("--hq", help="Filtrer par hq_country (ex. US, FR)")
    p_gaps.add_argument(
        "--france-market",
        dest="france_market",
        help="Filtrer par france_market (strong|partial|absent|unknown)",
    )
    p_gaps.add_argument("--segment", help="Un seul segment")

    p_sat = sub.add_parser("saturation", help="Saturation / gel segments")
    sat_sub = p_sat.add_subparsers(dest="sat_action")
    sat_sub.add_parser("watch", help="Surveiller taux par passe réelle ([SATURÉ]/[PROCHE])")
    sat_sub.add_parser(
        "freeze",
        help="Geler segments < seuil dans frozen-segments.json",
    )

    sub.add_parser("audit-sources", help="Vendeurs avec source listicle / agrégateur")
    sub.add_parser(
        "verify-eligible",
        help="Candidats verified (domaine officiel) vs listicle",
    )
    sub.add_parser(
        "segment-readiness",
        help="Profondeur inventaire vs saturation par segment",
    )

    args = parser.parse_args()

    if args.command == "validate":
        return validate()
    if args.command == "stats":
        stats()
        return 0
    if args.command == "list-segments":
        write_segments_markdown(CATALOGUE / "SEGMENTS.md")
        print(f"Écrit : {CATALOGUE / 'SEGMENTS.md'}")
        return 0
    if args.command == "export":
        export_csv(args.output)
        return 0
    if args.command == "build-db":
        build_db(args.db)
        return 0
    if args.command == "coverage":
        coverage_report()
        return 0
    if args.command == "gaps":
        gaps_report(
            hq=args.hq,
            france_market=args.france_market,
            segment=args.segment,
        )
        return 0
    if args.command == "saturation":
        if args.sat_action == "watch":
            saturation_watch()
        elif args.sat_action == "freeze":
            saturation_freeze()
        else:
            saturation_report()
        return 0
    if args.command == "audit-sources":
        audit_sources()
        return 0
    if args.command == "verify-eligible":
        verify_eligible()
        return 0
    if args.command == "segment-readiness":
        segment_readiness()
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
