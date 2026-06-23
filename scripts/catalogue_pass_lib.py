#!/usr/bin/env python3
"""Bibliothèque partagée — application de passes catalogue et métriques."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
PASSES_DIR = ROOT / "catalogue-saas" / "passes"
IDEES = ROOT / "idees"
SEGMENTS_MAP = IDEES / "catalogue-segments.json"

sys.path.insert(0, str(ROOT / "scripts"))
import catalogue_saas as cs  # noqa: E402


def today() -> str:
    return date.today().isoformat()


def metrics_snapshot() -> dict[str, int]:
    vendors = cs.iter_vendors()
    return {
        "total": len(vendors),
        "verified": sum(1 for v in vendors if v["verification_status"] == "verified"),
        "partial": sum(1 for v in vendors if v["verification_status"] == "partial"),
        "listicle": sum(
            1 for v in vendors if cs.is_listicle_source(v["source_url"], v["url"])
        ),
        "eligible": sum(
            1
            for v in vendors
            if v["verification_status"] == "partial"
            and cs.domains_match(v["url"], v["source_url"])
            and not cs.is_listicle_source(v["source_url"], v["url"])
        ),
    }


def load_all_vendor_ids() -> set[str]:
    ids: set[str] = set()
    for path in VENDORS_DIR.glob("*.json"):
        for vendor in json.loads(path.read_text(encoding="utf-8")).get("vendors", []):
            ids.add(vendor["id"])
    return ids


def apply_verify_updates(updates: dict[str, dict]) -> int:
    count = 0
    for path in VENDORS_DIR.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for vendor in data.get("vendors", []):
            upd = updates.get(vendor["id"])
            if not upd:
                continue
            vendor.update(upd)
            changed = True
            count += 1
        if changed:
            data["updated_at"] = today()
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return count


def apply_additions(additions: dict[str, list[dict]]) -> tuple[int, list[str]]:
    all_ids = load_all_vendor_ids()
    added: list[str] = []
    total = 0
    for fname, vendors in additions.items():
        path = VENDORS_DIR / fname
        data = json.loads(path.read_text(encoding="utf-8"))
        count = 0
        for vendor in vendors:
            if vendor["id"] in all_ids:
                continue
            data["vendors"].append(vendor)
            all_ids.add(vendor["id"])
            added.append(vendor["id"])
            count += 1
            total += 1
        if count:
            data["updated_at"] = today()
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return total, added


def apply_coverage_updates(coverage_updates: dict[str, dict[str, dict]], pass_id: str) -> None:
    if not coverage_updates:
        return
    matrix = json.loads(COVERAGE.read_text(encoding="utf-8"))
    for seg_id, sources in coverage_updates.items():
        entry = matrix["segments"][seg_id]
        for src, upd in sources.items():
            prev = entry["sources"].get(src) or {}
            entry["sources"][src] = {
                **upd,
                "cumulative_new": prev.get("cumulative_new", prev.get("new_added", 0))
                + upd.get("new_added", 0),
            }
        entry["last_pass"] = pass_id
        entry["vendor_count_after_pass"] = len(
            json.loads((VENDORS_DIR / f"{seg_id}.json").read_text(encoding="utf-8"))["vendors"]
        )
    matrix["updated_at"] = today()
    COVERAGE.write_text(json.dumps(matrix, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run_saturation_freeze() -> int:
    return subprocess.call(
        [sys.executable, str(ROOT / "scripts" / "catalogue_saas.py"), "saturation", "freeze"],
        cwd=ROOT,
    )


def load_manifest(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    for key in ("pass_id",):
        if key not in data:
            raise ValueError(f"manifeste invalide : clé « {key} » manquante dans {path}")
    return data


def apply_manifest(manifest: dict[str, Any], *, dry_run: bool = False) -> dict[str, Any]:
    pass_id = manifest["pass_id"]
    additions = manifest.get("additions") or {}
    verify_updates = manifest.get("verify_updates") or {}
    coverage_updates = manifest.get("coverage_updates") or {}

    for fname in additions:
        if not (VENDORS_DIR / fname).exists():
            raise FileNotFoundError(f"fichier segment inconnu : {fname}")

    if dry_run:
        return {
            "pass_id": pass_id,
            "dry_run": True,
            "additions_count": sum(len(v) for v in additions.values()),
            "verify_count": len(verify_updates),
            "coverage_segments": list(coverage_updates.keys()),
        }

    before = metrics_snapshot()
    added_total, added_ids = apply_additions(additions)
    verified_count = apply_verify_updates(verify_updates)
    apply_coverage_updates(coverage_updates, pass_id)
    after = metrics_snapshot()

    return {
        "pass_id": pass_id,
        "added_total": added_total,
        "added_ids": added_ids,
        "verified_count": verified_count,
        "before": before,
        "after": after,
    }


def retravailler_segment_ids() -> set[str]:
    """Segments liés aux idées 🔁 À retravailler."""
    if not SEGMENTS_MAP.exists():
        return set()
    mapping = json.loads(SEGMENTS_MAP.read_text(encoding="utf-8")).get("ideas", {})
    segments: set[str] = set()
    statut_re = re.compile(r"^-\s+\*\*Statut\*\*\s*:\s*(.+)$", re.MULTILINE)
    for folder in sorted(IDEES.iterdir()):
        readme = folder / "README.md"
        if not readme.exists():
            continue
        match = statut_re.search(readme.read_text(encoding="utf-8"))
        if not match or "🔁" not in match.group(1):
            continue
        segments.update(mapping.get(folder.name, []))
    return segments


def eligible_for_promotion(
    *,
    segments: set[str] | None = None,
    france_market: str | None = None,
) -> list[dict]:
    out: list[dict] = []
    for vendor in cs.iter_vendors():
        if vendor["verification_status"] != "partial":
            continue
        if not cs.domains_match(vendor["url"], vendor["source_url"]):
            continue
        if cs.is_listicle_source(vendor["source_url"], vendor["url"]):
            continue
        if segments and not any(s in segments for s in vendor["segments"]):
            continue
        if france_market and vendor.get("france_market") != france_market:
            continue
        out.append(vendor)
    return sorted(out, key=lambda v: v["id"])


def promote_verified(
    vendor_ids: list[str],
    pass_id: str,
    *,
    pricing_note: str | None = None,
) -> int:
    consulted = today()
    updates = {
        vid: {
            "verification_status": "verified",
            "source_consulted_at": consulted,
            "discovery_pass": pass_id,
            **(
                {"pricing_notes": pricing_note}
                if pricing_note
                else {
                    "pricing_notes": (
                        f"Promotion auto verify-eligible ; source officielle (consulté {consulted})."
                    )
                }
            ),
        }
        for vid in vendor_ids
    }
    return apply_verify_updates(updates)


def init_manifest_template(pass_id: str, pass_date: str | None = None) -> dict[str, Any]:
    d = pass_date or today()
    return {
        "pass_id": pass_id,
        "date": d,
        "description": "",
        "additions": {},
        "verify_updates": {},
        "coverage_updates": {},
    }


def init_pass_markdown(pass_id: str, pass_date: str | None = None) -> str:
    d = pass_date or today()
    return f"""# Passe {pass_id}

- **Pass ID** : `{pass_id}`
- **Date** : {d}
- **Manifeste** : `catalogue-saas/passes/{pass_id}.manifest.json`

## Ajouts catalogue

| ID | Segment | Statut |
|---|---|---|

## Promotions verified

| Cible | Notes |
|---|---|

## Métriques après passe

| Métrique | Avant | Après |
|---|---|---|
| Vendeurs | | |
| Verified | | |
| Listicle-sourced | | |

## Validation

```bash
python3 scripts/catalogue_pass.py run catalogue-saas/passes/{pass_id}.manifest.json
python3 scripts/catalogue_saas.py gate
```
"""
