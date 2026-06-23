#!/usr/bin/env python3
"""Vague V6i — Terravisu/h-genai + listicle zero + verified idées 🔁."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v6i-terravisu-retravaille-verify"


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
    "geospatial-gis-fr.json": [
        v(
            "terravisu",
            "Terravisu (Makina Corpus)",
            "https://makina-corpus.com/sig-webmapping/application-cartographique-identification-parcelles-agricoles-assolements",
            ["geospatial-gis-fr", "environmental-data-fr"],
            "Application SIG web coopérative : croisement RPG × ICPE × Natura 2000 × Hub'Eau "
            "pour identifier parcelles agricoles exposées aux risques industriels et hydriques.",
            [
                "rpg",
                "icpe",
                "natura2000",
                "hub_eau",
                "parcelles_agricoles",
                "webmapping",
                "france",
            ],
            "enterprise_quote",
            "mid_market",
            "https://makina-corpus.com/sig-webmapping/application-cartographique-identification-parcelles-agricoles-assolements",
            "official_site",
            verified=True,
            notes="Preuve production SeineYonne ; concurrent direct idée 0026 (consulté 2026-06-23).",
        ),
    ],
    "open-data-governance-fr.json": [
        v(
            "h-genai",
            "h-genai (OSS)",
            "https://github.com/podolskyDavid/h-genai",
            ["open-data-governance-fr", "territorial-analytics", "rag-knowledge"],
            "Stack OSS FastAPI/Vue : agents LLM sur données OFGL et open data pour analyse financière "
            "des collectivités territoriales (AWS Bedrock).",
            [
                "open_source",
                "ofgl",
                "rag",
                "llm_agents",
                "municipal_finance",
                "france",
            ],
            "open_source",
            "self_serve",
            "https://github.com/podolskyDavid/h-genai",
            "open_source",
            notes="Repo actif (habib256/h-genai et huggingface/h-genai introuvables 2026-06-23) ; cité idées 0003/0006.",
        ),
    ],
}

VERIFY_UPDATES: dict[str, dict] = {
    # Listicle résiduel V6h
    "windsurf": {
        "verification_status": "verified",
        "source_url": "https://windsurf.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Free/Pro $20/Teams $40 seat/Max $200 ; page tarifs officielle (consulté 2026-06-23).",
    },
    "salesforce-agentforce": {
        "verification_status": "verified",
        "source_url": "https://www.salesforce.com/agentforce/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Flex Credits / conversations ; tarifs officiels Agentforce (consulté 2026-06-23).",
    },
    # 0001 — marchés publics
    "decp-info": {
        "verification_status": "verified",
        "source_url": "https://decp.info/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Exploration DECP tabulaire gratuite ; réutilisation data.gouv (consulté 2026-06-23).",
    },
    "openmarches": {
        "verification_status": "verified",
        "source_url": "https://www.data.gouv.fr/reuses/openmarches-visualisation-des-marches-it-publics",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "479k+ marchés IT DECP ; fiche réutilisation data.gouv (consulté 2026-06-23).",
    },
    "doaken": {
        "verification_status": "verified",
        "source_url": "https://doaken.fr/solutions",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Intelligence attribution DECP ; page solutions officielle (consulté 2026-06-23).",
    },
    # 0009 — DPE / rénovation
    "cantine-energetique": {
        "verification_status": "verified",
        "source_url": "https://www.cantine-energetique.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "SaaS efficacité énergétique bâtiments ; site éditeur (consulté 2026-06-23).",
    },
    "spigao": {
        "verification_status": "verified",
        "source_url": "https://www.spigao.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Cartographie DPE passoires ; concurrent idée 0009 (consulté 2026-06-23).",
    },
    # 0025 — copropriétés / rénovation
    "copro-solutions": {
        "verification_status": "verified",
        "source_url": "https://www.copro-solutions.fr/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Pilotage PPT/DPE copropriétés ; concurrent Hellio idée 0025 (consulté 2026-06-23).",
    },
    "matera": {
        "verification_status": "verified",
        "source_url": "https://www.matera.eu/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Syndic copropriété digital ; site officiel (consulté 2026-06-23).",
    },
    "scanreno": {
        "verification_status": "verified",
        "source_url": "https://www.scanreno.fr/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Rénovation copropriétés ; site éditeur (consulté 2026-06-23).",
    },
    # 0026 — parcelles agricoles
    "makina-corpus": {
        "verification_status": "verified",
        "source_url": "https://makina-corpus.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Intégrateur Terravisu ; site éditeur (consulté 2026-06-23).",
    },
    "geofolia": {
        "verification_status": "verified",
        "source_url": "https://www.isagri.fr/geofolia/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Gestion parcellaire agricole Isagri ; adjacent idée 0026 (consulté 2026-06-23).",
    },
    # 0028 — emploi territorial
    "eclaireur-public": {
        "verification_status": "verified",
        "source_url": "https://eclaireurpublic.fr/methodologie",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Observatoire subventions/marchés ; méthodologie publique (consulté 2026-06-23).",
    },
    # 0029 — KYC lite
    "ubble": {
        "verification_status": "verified",
        "source_url": "https://ubble.ai/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Vérification identité vidéo ; benchmark §13 idée 0029 (consulté 2026-06-23).",
    },
    "dotfile": {
        "verification_status": "verified",
        "source_url": "https://www.dotfile.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Onboarding/KYC PME ; site éditeur (consulté 2026-06-23).",
    },
    "ondorse": {
        "verification_status": "verified",
        "source_url": "https://www.ondorse.co/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "KYC/AML automatisé FR ; site éditeur (consulté 2026-06-23).",
    },
    "lemonway-kyc": {
        "verification_status": "verified",
        "source_url": "https://www.lemonway.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "KYC paiement / EMI ; acteur FR cité idée 0029 (consulté 2026-06-23).",
    },
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "geospatial-gis-fr": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 1,
            "new_added": 1,
            "pass": PASS_ID,
        },
    },
    "open-data-governance-fr": {
        "open_source": {
            "consulted_at": TODAY,
            "candidates_found": 1,
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
