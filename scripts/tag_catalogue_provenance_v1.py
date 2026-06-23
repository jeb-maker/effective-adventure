#!/usr/bin/env python3
"""Rétro-tag founded_year + entry_ai_generated sur toutes les fiches vendeur."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
OVERRIDES_PATH = ROOT / "catalogue-saas" / "founded-years-overrides.json"
TODAY = "2026-06-23"

# Passes agent/auto → fiche considérée générée par IA/pipeline
AI_PASS_PREFIXES = (
    "discover-",
    "auto-verify-",
    "auto-weekly-",
    "2026-06-v6",
)

# Passes agent mais relues/validées humainement → entry_ai_generated false
VALIDATED_PASSES = frozenset(
    {
        "2026-06-discover-validated-retravaille",
        "2026-06-procurement-compliance-discover",
    }
)

VALIDATED_PASS_PREFIXES = (
    "2026-06-discover-validated",
    "2026-06-procurement-compliance",
)

YEAR_IN_TEXT = re.compile(
    r"(?:fondé(?:e)?|créé(?:e)?|lancé(?:e)?|since|depuis|est\.?\s*)\s*(?:en\s+)?(\d{4})",
    re.IGNORECASE,
)


def load_overrides() -> dict[str, dict]:
    if not OVERRIDES_PATH.exists():
        return {}
    return json.loads(OVERRIDES_PATH.read_text(encoding="utf-8")).get("vendors", {})


def infer_ai_generated(vendor: dict) -> bool:
    notes = vendor.get("notes") or ""
    if "Découvert auto" in notes or "À VALIDER" in notes:
        return True

    src = vendor.get("discovery_source") or ""
    if src == "retrospective_backfill":
        return False

    pass_id = vendor.get("discovery_pass") or ""
    if pass_id in VALIDATED_PASSES or any(
        pass_id.startswith(p) for p in VALIDATED_PASS_PREFIXES
    ):
        return False
    if "retrospective" in pass_id or pass_id == "2026-06-v5a":
        return False

    if any(pass_id.startswith(p) for p in AI_PASS_PREFIXES):
        return True

    if pass_id.startswith("2026-06-v5"):
        return True

    return False


def infer_year_from_text(vendor: dict) -> tuple[int | None, str | None]:
    for field in ("notes", "description", "pricing_notes"):
        text = vendor.get(field) or ""
        m = YEAR_IN_TEXT.search(text)
        if m:
            year = int(m.group(1))
            if 1970 <= year <= 2100:
                return year, f"inféré depuis {field}"
    return None, None


def resolve_founded(vendor: dict, overrides: dict[str, dict]) -> tuple[int | None, str | None]:
    vid = vendor["id"]
    if vid in overrides:
        o = overrides[vid]
        return o.get("founded_year"), o.get("founded_year_source")

    if vendor.get("founded_year") is not None:
        return vendor.get("founded_year"), vendor.get("founded_year_source")

    return infer_year_from_text(vendor)


def tag_vendor(vendor: dict, overrides: dict[str, dict]) -> bool:
    changed = False
    ai = infer_ai_generated(vendor)
    if vendor.get("entry_ai_generated") != ai:
        vendor["entry_ai_generated"] = ai
        changed = True

    year, source = resolve_founded(vendor, overrides)
    if vendor.get("founded_year") != year:
        vendor["founded_year"] = year
        changed = True
    if source and vendor.get("founded_year_source") != source:
        vendor["founded_year_source"] = source
        changed = True
    elif year is None and "founded_year_source" in vendor:
        del vendor["founded_year_source"]
        changed = True

    return changed


def run(*, dry_run: bool = False) -> dict[str, int]:
    overrides = load_overrides()
    stats = {
        "files": 0,
        "vendors": 0,
        "changed": 0,
        "ai_true": 0,
        "ai_false": 0,
        "year_known": 0,
        "year_unknown": 0,
    }

    for path in sorted(VENDORS_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        file_changed = False
        for vendor in data.get("vendors", []):
            stats["vendors"] += 1
            if tag_vendor(vendor, overrides):
                stats["changed"] += 1
                file_changed = True
            if vendor.get("entry_ai_generated"):
                stats["ai_true"] += 1
            else:
                stats["ai_false"] += 1
            if vendor.get("founded_year") is not None:
                stats["year_known"] += 1
            else:
                stats["year_unknown"] += 1

        if file_changed and not dry_run:
            data["updated_at"] = TODAY
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            stats["files"] += 1

    return stats


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    stats = run(dry_run=dry_run)
    mode = " (dry-run)" if dry_run else ""
    print(f"Tag provenance{mode} — {stats['vendors']} vendeurs")
    print(f"  modifiés     : {stats['changed']}")
    print(f"  entry_ai_generated true/false : {stats['ai_true']}/{stats['ai_false']}")
    print(f"  founded_year connu/inconnu    : {stats['year_known']}/{stats['year_unknown']}")
    if not dry_run:
        print(f"  fichiers     : {stats['files']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
