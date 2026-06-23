#!/usr/bin/env python3
"""Vague V6c — compléter marchés publics FR + verified chaîne RecordAI + gel saturation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v6c-procurement-recordai-freeze"


def v(
    id_: str,
    name: str,
    url: str,
    segments: list[str],
    desc: str,
    caps: list[str],
    pricing: str,
    market: str,
    source: str,
    src_type: str,
    *,
    verified: bool = False,
    hq: str = "FR",
    fr: str = "strong",
    regions: list[str] | None = None,
    geo: str = "france",
    pricing_notes: str | None = None,
    notes: str | None = None,
) -> dict:
    d = {
        "id": id_,
        "name": name,
        "url": url,
        "segments": segments,
        "description": desc,
        "capabilities": caps,
        "pricing_model": pricing,
        "target_market": market,
        "geography": geo,
        "hq_country": hq,
        "france_market": fr,
        "operating_regions": regions or ["FR"],
        "discovery_source": src_type,
        "discovery_pass": PASS_ID,
        "source_url": source,
        "source_consulted_at": TODAY,
        "verification_status": "verified" if verified else "partial",
    }
    if pricing_notes:
        d["pricing_notes"] = pricing_notes
    if notes:
        d["notes"] = notes
    return d


ADDITIONS: dict[str, list[dict]] = {
    "public-procurement-intel.json": [
        v(
            "synapse-entreprises",
            "Synapse Entreprises",
            "https://www.synapse-entreprises.com/",
            ["public-procurement-intel"],
            "Profil acheteur pour collectivités + service entreprises « Alerte Marchés » : veille AO multi-plateformes.",
            ["ao_alerts", "ao_monitoring", "e_procurement", "france"],
            "hybrid",
            "smb",
            "https://www.synapse-entreprises.com/espace-entreprises/alerte-marches",
            "official_site",
            notes="Double rôle acheteur/entreprise ; tarifs abonnement non publics (consulté 2026-06-23).",
        ),
        v(
            "wanao",
            "Wanao",
            "https://wanao.com/",
            ["public-procurement-intel"],
            "Veille et gestion AO depuis 20+ ans : ~10 000 sources (BOAMP, JOUE, PQR, collectivités), alertes renouvellement.",
            ["ao_monitoring", "tender_management", "dce_analysis", "france"],
            "enterprise_quote",
            "mid_market",
            "https://wanao.com/",
            "official_site",
            notes="~400 000 AO/an ; tarifs sur devis (consulté 2026-06-23).",
        ),
        v(
            "first-ao",
            "First AO",
            "https://firstao-appel-offre.fr/",
            ["public-procurement-intel"],
            "Veille avis de marché et d'attribution (Groupe First ECO) : qualification humaine, fiches attributaires.",
            ["ao_monitoring", "attribution_analytics", "france"],
            "enterprise_quote",
            "mid_market",
            "https://firstao-appel-offre.fr/",
            "official_site",
            notes="Groupe First ECO ; tarifs sur devis (consulté 2026-06-23).",
        ),
    ],
}

VERIFY_UPDATES: dict[str, dict] = {
    "olra": {
        "source_url": "https://olra.fr/tarifs",
        "source_consulted_at": TODAY,
        "pricing_notes": "Essentiel/Pro/Entreprise sur devis ; essai 14 j sans CB ; pages 500/1500/mois (consulté 2026-06-23).",
        "discovery_pass": PASS_ID,
    },
    "levity": {
        "verification_status": "verified",
        "source_url": "https://levity.ai/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    "pipefy": {
        "verification_status": "verified",
        "source_url": "https://www.pipefy.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    "tonkean": {
        "verification_status": "verified",
        "source_url": "https://www.tonkean.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    "extend-ai": {
        "verification_status": "verified",
        "source_url": "https://www.extend.ai/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    "nanonets": {
        "verification_status": "verified",
        "source_url": "https://nanonets.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "public-procurement-intel": {
        "geo_digest": {
            "consulted_at": TODAY,
            "candidates_found": 5,
            "new_added": 3,
            "pass": PASS_ID,
        },
    },
    "parsing-inbox": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 3,
            "new_added": 0,
            "pass": PASS_ID,
        },
    },
    "automation-platforms": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 2,
            "new_added": 0,
            "pass": PASS_ID,
        },
    },
}


def apply_verify_updates() -> int:
    count = 0
    for path in VENDORS_DIR.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for vendor in data.get("vendors", []):
            upd = VERIFY_UPDATES.get(vendor["id"])
            if not upd:
                continue
            vendor.update(upd)
            changed = True
            count += 1
        if changed:
            data["updated_at"] = TODAY
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return count


def merge() -> None:
    all_ids: set[str] = set()
    for path in VENDORS_DIR.glob("*.json"):
        for vendor in json.loads(path.read_text(encoding="utf-8")).get("vendors", []):
            all_ids.add(vendor["id"])

    total = 0
    for fname, vendors in ADDITIONS.items():
        path = VENDORS_DIR / fname
        data = json.loads(path.read_text(encoding="utf-8"))
        count = 0
        for vendor in vendors:
            if vendor["id"] in all_ids:
                print(f"skip duplicate: {vendor['id']}")
                continue
            data["vendors"].append(vendor)
            all_ids.add(vendor["id"])
            count += 1
            total += 1
        if count:
            data["updated_at"] = TODAY
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"updated {fname}: +{count}")

    verified = apply_verify_updates()
    print(f"verify updates: {verified}")

    matrix = json.loads(COVERAGE.read_text(encoding="utf-8"))
    for seg_id, sources in COVERAGE_UPDATES.items():
        entry = matrix["segments"][seg_id]
        for src, upd in sources.items():
            prev = entry["sources"].get(src) or {}
            entry["sources"][src] = {
                **upd,
                "cumulative_new": prev.get("cumulative_new", prev.get("new_added", 0))
                + upd["new_added"],
            }
        entry["last_pass"] = PASS_ID
        entry["vendor_count_after_pass"] = len(
            json.loads((VENDORS_DIR / f"{seg_id}.json").read_text(encoding="utf-8"))["vendors"]
        )
    matrix["updated_at"] = TODAY
    COVERAGE.write_text(json.dumps(matrix, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"done: +{total} vendors")


if __name__ == "__main__":
    merge()
    print("running saturation freeze…")
    rc = subprocess.call(
        [sys.executable, str(ROOT / "scripts" / "catalogue_saas.py"), "saturation", "freeze"],
        cwd=ROOT,
    )
    sys.exit(rc)
