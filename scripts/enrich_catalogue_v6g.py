#!/usr/bin/env python3
"""Vague V6g — verified energy/geo/env + réutilisations publiques + fix listicle."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v6g-verified-section4-ecartees"


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
    "territorial-analytics.json": [
        v(
            "data-emploi-francetravail",
            "Data Emploi (France Travail)",
            "https://dataemploi.francetravail.fr/",
            ["territorial-analytics"],
            "Plateforme officielle gratuite : tensions emploi par métier ROME × territoire (région, EPCI, commune), dynamisme, salaires.",
            ["employment_tensions", "rome", "territorial_analytics", "france"],
            "freemium",
            "self_serve",
            "https://dataemploi.francetravail.fr/",
            "official_site",
            verified=True,
            notes="Concurrent direct idée 0028 — couvre ~80 % du besoin sans développement (consulté 2026-06-23).",
        ),
        v(
            "eclaireur-public",
            "Éclaireur Public (Anticor / Data for Good)",
            "https://eclaireurpublic.fr/",
            ["territorial-analytics", "public-procurement-intel"],
            "Indice A–E transparence subventions + marchés publics ; comparateur collectivités (data.gouv DECP/SCDL).",
            ["subventions", "decp", "transparency", "open_data", "france"],
            "freemium",
            "self_serve",
            "https://eclaireurpublic.fr/methodologie",
            "official_site",
            notes="Adjacent idées 0027/0018 ; gratuit (consulté 2026-06-23).",
        ),
    ],
    "energy-buildings-fr.json": [
        v(
            "coproff-cerema",
            "CoproFF (Cerema)",
            "https://www.cerema.fr/",
            ["energy-buildings-fr", "real-estate-proptech"],
            "Outil public de visualisation des copropriétés : croisement RNIC × fichiers fonciers pour collectivités et acteurs locaux.",
            ["rnic", "coproprietes", "foncier", "open_data", "france"],
            "freemium",
            "mid_market",
            "https://www.cerema.fr/fr/actualites/coproff-outil-de-visualisation-des-coproprietes",
            "official_site",
            notes="Service public Cerema ; cité idée 0025 (consulté 2026-06-23).",
        ),
    ],
}

VERIFY_UPDATES: dict[str, dict] = {
    # energy-buildings-fr (0009, 0025)
    "go-renove-pro": {
        "verification_status": "verified",
        "source_url": "https://www.bdnb.io/services/gorenove/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Service public CSTB gratuit pour bailleurs/collectivités (consulté 2026-06-23).",
    },
    "heero": {
        "verification_status": "verified",
        "source_url": "https://www.heero.fr/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    "openmeti": {
        "verification_status": "verified",
        "source_url": "https://www.openmeti.fr/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    "hellowatt": {
        "verification_status": "verified",
        "source_url": "https://www.hellowatt.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    "enoptea": {
        "verification_status": "verified",
        "source_url": "https://www.enoptea.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    "metron": {
        "verification_status": "verified",
        "source_url": "https://www.metron.io/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    # environmental-data-fr (0026, 0005)
    "atmo-france": {
        "verification_status": "verified",
        "source_url": "https://www.atmo-france.org/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    "hub-eau": {
        "verification_status": "verified",
        "source_url": "https://hub-eau.fr/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "APIs REST open data eau ; référencé data.gouv (consulté 2026-06-23).",
    },
    "georisques-api": {
        "verification_status": "verified",
        "source_url": "https://www.georisques.gouv.fr/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    # geospatial-gis-fr (0026)
    "geoperso": {
        "verification_status": "verified",
        "source_url": "https://www.geoperso.fr/logiciel-valorisation-fonciere-agricole/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    "alkante": {
        "verification_status": "verified",
        "source_url": "https://www.alkante.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    # territorial
    "vigicite": {
        "verification_status": "verified",
        "source_url": "https://www.vigicite.fr/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
    },
    # listicle → official (ai-governance / grc)
    "modulos": {
        "verification_status": "verified",
        "source_url": "https://www.modulos.ai/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace modulos.ai/best-ai-governance listicle (consulté 2026-06-23).",
    },
    "kla-digital": {
        "verification_status": "verified",
        "source_url": "https://www.kla.digital/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace kla.digital/blog listicle (consulté 2026-06-23).",
    },
    "arthur-ai": {
        "source_url": "https://www.arthur.ai/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Source officielle ; remplace dancumberlandlabs listicle (consulté 2026-06-23).",
    },
    "modelop": {
        "source_url": "https://www.modelop.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Source officielle ; remplace dancumberlandlabs listicle (consulté 2026-06-23).",
    },
    "atlan": {
        "source_url": "https://atlan.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Source officielle ; remplace dancumberlandlabs listicle (consulté 2026-06-23).",
    },
    "onetrust": {
        "source_url": "https://www.onetrust.com/platform/privacy-compliance/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Source officielle ; remplace dancumberlandlabs listicle (consulté 2026-06-23).",
    },
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "territorial-analytics": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 4,
            "new_added": 2,
            "pass": PASS_ID,
        },
    },
    "energy-buildings-fr": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 2,
            "new_added": 1,
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
