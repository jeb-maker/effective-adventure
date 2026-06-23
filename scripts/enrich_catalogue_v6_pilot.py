#!/usr/bin/env python3
"""Vague V6 pilote — vérification + nouveaux acteurs (0029 RecordAI, 0001 Radar).

Segments : compliance-to-spec, kyc-aml, public-procurement-intel.
Méthode : sources officielles uniquement (pas de listicle), promotion verified.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v6-pilot-compliance-procurement"


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
    hq: str = "US",
    fr: str = "partial",
    regions: list[str] | None = None,
    geo: str = "global",
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
        "operating_regions": regions or ["US", "EU"],
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
    "compliance-to-spec.json": [
        v(
            "checkfile-ai",
            "CheckFile.ai",
            "https://www.checkfile.ai/",
            ["compliance-to-spec", "kyc-aml", "document-idp"],
            "Validation documentaire IA pour KYC/AML et conformité DORA : extraction, détection fraude, audit trail 5 ans, hébergement UE.",
            [
                "document_validation",
                "kyc_aml",
                "dora_audit_trail",
                "api_webhooks",
                "fraud_detection",
            ],
            "per_document",
            "smb",
            "https://www.checkfile.ai/pricing",
            "official_site",
            verified=True,
            hq="DE",
            fr="strong",
            regions=["FR", "EU"],
            geo="europe",
            pricing_notes="Usage-based ~0,30 €/fichier ; plans Starter 100/mois, Business 500/mois, Enterprise sur devis (consulté 2026-06-23).",
            notes="Concurrent omis en revue idée 0029 — clone direct du positionnement RecordAI KYC lite DORA.",
        ),
        v(
            "verifypdf",
            "VerifyPDF",
            "https://verifypdf.com/",
            ["compliance-to-spec", "document-idp"],
            "Détection de documents PDF falsifiés ou générés par IA ; scoring risque et piste d'audit pour due diligence documentaire (DORA tiers TIC).",
            [
                "pdf_fraud_detection",
                "audit_trail",
                "api",
                "dora_third_party",
            ],
            "hybrid",
            "mid_market",
            "https://verifypdf.com/",
            "official_site",
            verified=True,
            hq="US",
            fr="partial",
            regions=["US", "EU"],
            pricing_notes="Basic 19 $/mois (150 docs), Professional 99 $/mois (1000 docs, API) ; essai 15 jours (consulté 2026-06-23).",
            notes="Angle fraude documentaire / DORA prestataires tiers — complète CheckFile sur l'intégrité PDF.",
        ),
    ],
    "kyc-aml.json": [],
    "public-procurement-intel.json": [
        v(
            "tenderbolt-ai",
            "Tenderbolt AI",
            "https://www.tenderbolt.ai/fr",
            ["public-procurement-intel"],
            "Logiciel IA français d'analyse DCE et rédaction de mémoires techniques pour marchés publics et RFP ; hébergement Europe SOC2/ISO 27001.",
            [
                "dce_analysis",
                "memoire_technique",
                "go_nogo",
                "france_public_procurement",
            ],
            "enterprise_quote",
            "mid_market",
            "https://www.tenderbolt.ai/fr/solutions/public",
            "official_site",
            verified=True,
            hq="FR",
            fr="strong",
            regions=["FR", "EU"],
            geo="france",
            notes="Citée en comparaison par Maître AO ; fondée 2024 Paris.",
        ),
        v(
            "iziao",
            "IZIAO",
            "https://www.iziao.fr/",
            ["public-procurement-intel"],
            "Plateforme hybride IA + experts pour répondre aux marchés publics : analyse GO/NO-GO gratuite, réponse clé en main, dépôt sur plateformes acheteurs.",
            [
                "dce_analysis",
                "memoire_technique",
                "admin_forms",
                "deposit_platforms",
                "hybrid_service",
            ],
            "per_outcome",
            "smb",
            "https://www.iziao.fr/repondre-aux-marches-publics-tarifs",
            "official_site",
            verified=True,
            hq="FR",
            fr="strong",
            regions=["FR"],
            geo="france",
            pricing_notes="Crédits 0,10 € HT/unité ; packs Essentiel 350 € HT (3500 cr.), Expert 600 € HT, Sérénité 800 € HT ; 0 % engagement (consulté 2026-06-23).",
        ),
        v(
            "alertoffres",
            "AlertOffres",
            "https://alertoffres.fr/",
            ["public-procurement-intel"],
            "Veille marchés publics FR avec crédits IA : recherche AO, alertes email, accès DCE, export Excel et assistants de réponse.",
            [
                "ao_monitoring",
                "ai_credits",
                "dce_access",
                "france",
            ],
            "hybrid",
            "smb",
            "https://alertoffres.fr/tarifs",
            "official_site",
            verified=True,
            hq="FR",
            fr="strong",
            regions=["FR"],
            geo="france",
            pricing_notes="Gratuit 0 € ; Pro 29,99 € HT/mois (50 crédits IA) ; Expert 44,99 € HT/mois (100 crédits) (consulté 2026-06-23).",
            notes="Concurrent veille cité en analyse idée 0001/0008.",
        ),
        v(
            "publikconnect",
            "PublikConnect",
            "https://publikconnect.fr/",
            ["public-procurement-intel"],
            "Veille et alertes appels d'offres publics pour TPE/PME françaises ; filtres métier et notifications.",
            [
                "ao_alerts",
                "france",
                "smb_veille",
            ],
            "hybrid",
            "smb",
            "https://publikconnect.fr/tarifs",
            "official_site",
            verified=False,
            hq="FR",
            fr="strong",
            regions=["FR"],
            geo="france",
            pricing_notes="À partir de 49 €/mois (citée idée 0001 ; tarifs à reconfirmer sur site).",
        ),
    ],
}

# checkfile only in compliance-to-spec ADDITIONS; duplicate id skipped for kyc-aml empty list
# Patch kyc-aml segment on checkfile via segment patch after merge

VERIFY_UPDATES: dict[str, dict] = {
    "maitre-ao": {
        "verification_status": "verified",
        "source_url": "https://www.maitre-ao.fr/fr/tarifs",
        "source_consulted_at": TODAY,
        "pricing_notes": "Découverte 0 € ; Starter 39 €/mois ; Pro 79 €/mois ; Max 199 €/mois ; intelligence DECP incluse dès Starter (consulté 2026-06-23).",
        "capabilities": [
            "ao_alerts",
            "dce_analysis",
            "decp_intelligence",
            "memoire_technique",
            "attribution_analytics",
            "france",
        ],
        "description": "Plateforme IA marchés publics FR : veille 20 plateformes, analyse DCE Go/No-Go, intelligence attribution DECP (82k+ titulaires), mémoires techniques.",
        "discovery_pass": PASS_ID,
    },
    "nextend-ai": {
        "verification_status": "verified",
        "source_url": "https://nextend.ai/pricing",
        "source_consulted_at": TODAY,
        "pricing_notes": "Gratuit ; Pro 150 €/mois (5000 crédits IA) ; Business 250 €/mois ; à la carte dès 50 € (consulté 2026-06-23).",
        "capabilities": [
            "dce_analysis",
            "go_nogo",
            "memoire_technique",
            "cotraitants",
            "attribution_observatory",
            "france",
        ],
        "description": "Suite IA réponse AO : analyse DCE <2 min, mémoire technique, gestion co-traitants ; observatoire attribution DECP (13k+ acheteurs).",
        "discovery_pass": PASS_ID,
    },
    "marchespublics-ai": {
        "verification_status": "partial",
        "source_url": "https://marchespublics.ai/",
        "source_consulted_at": TODAY,
        "pricing_notes": "Compte gratuit ; tarifs payants non affichés publiquement (consulté 2026-06-23).",
        "capabilities": [
            "ao_monitoring",
            "decp_benchmark",
            "dce_analysis",
            "ai_analysis",
            "france",
        ],
        "description": "Veille et analyse marchés publics FR/EU : BOAMP, TED, DECP 10M+ contrats, scoring IA et benchmark prix.",
        "discovery_pass": PASS_ID,
    },
    "inscribe": {
        "verification_status": "verified",
        "source_url": "https://www.inscribe.ai/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Benchmark revue 0029 — KYC document fraud US, france_market partial.",
    },
}

SEGMENT_PATCHES: dict[str, list[str]] = {
    "checkfile-ai": ["kyc-aml", "document-idp"],
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "compliance-to-spec": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 4,
            "new_added": 2,
            "pass": PASS_ID,
        },
        "geo_digest": {
            "consulted_at": TODAY,
            "candidates_found": 3,
            "new_added": 0,
            "pass": PASS_ID,
        },
    },
    "public-procurement-intel": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 8,
            "new_added": 4,
            "pass": PASS_ID,
        },
        "analyst_report": {
            "consulted_at": TODAY,
            "candidates_found": 6,
            "new_added": 0,
            "pass": PASS_ID,
        },
        "geo_digest": {
            "consulted_at": TODAY,
            "candidates_found": 5,
            "new_added": 0,
            "pass": PASS_ID,
        },
    },
    "kyc-aml": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 2,
            "new_added": 1,
            "pass": PASS_ID,
        },
    },
}

TARGET_LEVELS = {
    "public-procurement-intel": "L3",
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


def patch_segments() -> int:
    patched = 0
    for path in VENDORS_DIR.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for vendor in data.get("vendors", []):
            extra = SEGMENT_PATCHES.get(vendor["id"])
            if not extra:
                continue
            for seg in extra:
                if seg not in vendor["segments"]:
                    vendor["segments"].append(seg)
                    changed = True
                    patched += 1
        if changed:
            data["updated_at"] = TODAY
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return patched


def merge() -> None:
    all_ids: set[str] = set()
    for path in VENDORS_DIR.glob("*.json"):
        for vendor in json.loads(path.read_text(encoding="utf-8")).get("vendors", []):
            all_ids.add(vendor["id"])

    total = 0
    per_file: dict[str, int] = {}
    for fname, vendors in ADDITIONS.items():
        if not vendors:
            continue
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
        per_file[fname] = count
        print(f"updated {fname}: +{count}")

    verified = apply_verify_updates()
    print(f"verified promotions: {verified}")

    patched = patch_segments()
    if patched:
        print(f"segment patches: +{patched}")

    matrix = json.loads(COVERAGE.read_text(encoding="utf-8"))
    for seg_id, sources in COVERAGE_UPDATES.items():
        entry = matrix["segments"][seg_id]
        new_added_total = 0
        for src, upd in sources.items():
            prev = entry["sources"].get(src) or {}
            entry["sources"][src] = {
                **upd,
                "cumulative_new": prev.get("cumulative_new", prev.get("new_added", 0))
                + upd["new_added"],
            }
            new_added_total += upd["new_added"]
        entry["last_pass"] = PASS_ID
        entry["target_level"] = TARGET_LEVELS.get(seg_id, entry.get("target_level", "L2"))
        entry["vendor_count_after_pass"] = len(
            json.loads((VENDORS_DIR / f"{seg_id}.json").read_text(encoding="utf-8"))["vendors"]
        )
    matrix["updated_at"] = TODAY
    COVERAGE.write_text(json.dumps(matrix, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"done: +{total} vendors")
    for fname, n in per_file.items():
        if n:
            print(f"  {fname}: +{n}")


if __name__ == "__main__":
    merge()
