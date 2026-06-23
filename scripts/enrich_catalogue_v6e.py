#!/usr/bin/env python3
"""Vague V6e — réutilisations territoriales (0007) + BTP privé + verified/listicle."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v6e-territorial-btp-verify"


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
            "orama-limited",
            "Orama Limited",
            "https://oramalimited.com/",
            ["territorial-analytics"],
            "Réutilisation data.gouv / API OFGL : fiche commune gratuite, note A–E, comparables multicritères et synthèses pédagogiques finances locales.",
            ["ofgl_api", "commune_benchmark", "fiscal_analytics", "open_data", "france"],
            "freemium",
            "self_serve",
            "https://oramalimited.com/comment-ca-marche/",
            "official_site",
            notes="Concurrent direct idée 0007 ; citoyen 0 € (consulté 2026-06-23).",
        ),
        v(
            "habity",
            "Habity",
            "https://habity.fr/",
            ["territorial-analytics", "energy-buildings-fr"],
            "Fiche commune 107 indicateurs (14 domaines) : fiscalité REI, finances OFGL consolidées, percentiles nationaux sur 34k+ communes.",
            ["commune_profile", "rei_fiscalite", "ofgl_finances", "open_data", "france"],
            "freemium",
            "self_serve",
            "https://habity.fr/a-propos/methodologie",
            "official_site",
            notes="Réutilisation data.gouv ; MAJ finances avril 2026 (consulté 2026-06-23).",
        ),
        v(
            "depenses-publiques",
            "DépensesPubliques.fr",
            "https://depensespubliques.fr/",
            ["territorial-analytics", "public-procurement-intel"],
            "Observatoire citoyen 36k+ communes : comparateur, classements, fiches traçables DGFiP + DECP + SCDL ; contenus pédagogiques.",
            ["commune_benchmark", "decp", "scdl", "open_data", "france"],
            "freemium",
            "self_serve",
            "https://depensespubliques.fr/donnees-sources",
            "official_site",
            notes="Modèle économique non public ; citoyen 0 € (consulté 2026-06-23).",
        ),
    ],
    "public-procurement-intel.json": [
        v(
            "mpf-france",
            "MPF (Marchés Publics France)",
            "https://www.mpfrance.fr/",
            ["public-procurement-intel"],
            "Veille sur-mesure Infopro Digital (28+ ans) : marchés publics et construction privée, qualification humaine 12k+ sources.",
            ["ao_monitoring", "private_construction", "human_qualification", "renewal_alerts", "france"],
            "enterprise_quote",
            "mid_market",
            "https://www.mpfrance.fr/qui-sommes-nous/foire-questions-abonnement/",
            "official_site",
            pricing_notes="Veille AO 1 200–5 000 € HT/an ; alertes renouvellement 1 450–4 000 € HT/an selon zone (consulté 2026-06-23).",
            notes="Sœur de Marchés Online (Infopro Digital).",
        ),
    ],
    "construction-proptech.json": [
        v(
            "spigao",
            "Spigao",
            "https://www.spigao.com/",
            ["construction-proptech", "public-procurement-intel"],
            "Plateforme BTP Intescia/Explore : veille AO publics/privés, BI marché, import DCE vers 50+ logiciels de chiffrage.",
            ["ao_monitoring", "private_btp_tenders", "dce_import", "business_intelligence", "france"],
            "enterprise_quote",
            "mid_market",
            "https://www.spigao.com/",
            "official_site",
            notes="Groupe Intescia ; tarifs sur devis — comparatifs tiers 200–400 €/mois (consulté 2026-06-23).",
        ),
        v(
            "prescriptio",
            "Prescriptio",
            "https://prescriptio.fr/",
            ["construction-proptech", "territorial-analytics"],
            "Data BTP : veille marchés publics, permis Sitadel, transactions DVF, entreprises RGE sur carte interactive.",
            ["ao_monitoring", "building_permits", "dvf_data", "rge_companies", "france"],
            "hybrid",
            "smb",
            "https://prescriptio.fr/prescriptio-vs-vecteur-plus",
            "official_site",
            verified=True,
            pricing_notes="39 €/mois ou 390 €/an ; essai 14 j sans engagement (consulté 2026-06-23).",
        ),
        v(
            "bati-pulse",
            "Bati-Pulse",
            "https://bati-pulse.com/",
            ["construction-proptech"],
            "Plateforme Intescia/Explore : détection anticipée chantiers BTP neufs/rénovations (publics et privés), enrichissement humain.",
            ["construction_veille", "private_btp_tenders", "project_tracking", "territorial_analytics", "france"],
            "enterprise_quote",
            "mid_market",
            "https://bati-pulse.com/",
            "official_site",
            notes="Explore Bati-Pulse ; tarifs sur devis (consulté 2026-06-23).",
        ),
    ],
}

VERIFY_UPDATES: dict[str, dict] = {
    # listicle → official (ai-governance)
    "langsmith": {
        "verification_status": "verified",
        "source_url": "https://www.langchain.com/pricing-langsmith",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Developer $0 ; Plus $39/seat/mo ; Enterprise custom ; remplace kla.digital listicle (consulté 2026-06-23).",
    },
    "fiddler-ai": {
        "verification_status": "verified",
        "source_url": "https://www.fiddler.ai/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace dancumberlandlabs.com listicle (consulté 2026-06-23).",
    },
    "arize-ai": {
        "verification_status": "verified",
        "source_url": "https://arize.com/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace dancumberlandlabs.com listicle (consulté 2026-06-23).",
    },
    "holistic-ai": {
        "source_url": "https://www.holisticai.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Source officielle ; remplace kla.digital listicle — tarifs sur devis (consulté 2026-06-23).",
    },
    "ibm-watsonx-governance": {
        "source_url": "https://www.ibm.com/products/watsonx-governance",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Source officielle IBM ; remplace modulos.ai listicle (consulté 2026-06-23).",
    },
    # géospatial 0026
    "geofoncier": {
        "verification_status": "verified",
        "source_url": "https://www.geofoncier.fr/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Portail notaires ; accès professionnel — tarifs par abonnement (consulté 2026-06-23).",
    },
    "ign-geoservices": {
        "verification_status": "verified",
        "source_url": "https://geoservices.ign.fr/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Services géographiques IGN ; open data + APIs professionnelles (consulté 2026-06-23).",
    },
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "territorial-analytics": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 5,
            "new_added": 3,
            "pass": PASS_ID,
        },
    },
    "construction-proptech": {
        "geo_digest": {
            "consulted_at": TODAY,
            "candidates_found": 4,
            "new_added": 3,
            "pass": PASS_ID,
        },
    },
    "public-procurement-intel": {
        "geo_digest": {
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
