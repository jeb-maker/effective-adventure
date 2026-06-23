#!/usr/bin/env python3
"""Vague V6b — gaps marchés publics + vérification parsing/IDP (idées 0001 Radar, 0029 RecordAI).

Segments : public-procurement-intel, parsing-inbox, document-idp, kyc-aml.
Méthode : sources officielles uniquement (pas de listicle), promotion verified.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v6b-procurement-parsing-verify"


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


# Part 2 — Ajouts marchés publics (idée 0001 Radar). Sources officielles via web search.
# Tous partial sauf grille tarifaire publique confirmée.
ADDITIONS: dict[str, list[dict]] = {
    "public-procurement-intel.json": [
        v(
            "france-marches",
            "France Marchés",
            "https://www.francemarches.com/",
            ["public-procurement-intel"],
            "Portail veille marchés publics FR : agrégation BOAMP, JOUE et 1 000+ profils acheteurs, alertes email gratuites et avis d'attribution.",
            [
                "ao_monitoring",
                "email_alerts",
                "boamp_joue",
                "attribution_notices",
                "france",
            ],
            "freemium",
            "smb",
            "https://www.francemarches.com/offre",
            "geo_digest",
            verified=False,
            hq="FR",
            fr="strong",
            regions=["FR"],
            geo="france",
            pricing_notes="Service d'alertes gratuit ; abonnements premium non affichés publiquement (consulté 2026-06-23).",
            notes="Veille majeure FR (160k+ abonnés) ; distincte de Synapse Entreprises (dématérialisation profil acheteur).",
        ),
        v(
            "tengo",
            "Tengo",
            "https://www.tengo.cc/",
            ["public-procurement-intel"],
            "Startup IA FR détection et réponse appels d'offres : veille 50+ plateformes, analyse DCE et génération de réponses sur mesure.",
            [
                "ao_monitoring",
                "dce_analysis",
                "ai_response_generation",
                "go_nogo",
                "france",
            ],
            "enterprise_quote",
            "smb",
            "https://www.tengo.cc/",
            "geo_digest",
            verified=False,
            hq="FR",
            fr="strong",
            regions=["FR"],
            geo="france",
            notes="Concurrent IA réponse AO cité idée 0001 ; tarifs sur demande.",
        ),
        v(
            "openmarches",
            "OpenMarchés",
            "https://www.data.gouv.fr/reuses/openmarches-visualisation-des-marches-it-publics",
            ["public-procurement-intel", "territorial-analytics"],
            "Réutilisation open data DECP : analyse et visualisation de 479k+ marchés publics IT FR (2018-2026), attributaires, montants et concurrence.",
            [
                "decp",
                "attribution_analytics",
                "data_visualization",
                "open_data",
                "france",
            ],
            "freemium",
            "self_serve",
            "https://www.data.gouv.fr/reuses/openmarches-visualisation-des-marches-it-publics",
            "official_site",
            verified=False,
            hq="FR",
            fr="strong",
            regions=["FR", "EU"],
            geo="france",
            notes="Analytics attribution (différent de decp.info) ; pipeline open source DuckDB/dbt/FastAPI.",
        ),
        v(
            "doaken",
            "DOAKEN",
            "https://doaken.fr/",
            ["public-procurement-intel"],
            "Logiciel FR de réponse aux appels d'offres : analyse DCE, score Go/No-Go, chiffrage DPGF vs 367k+ marchés attribués, mémoire technique et veille BOAMP/TED.",
            [
                "dce_analysis",
                "go_nogo",
                "dpgf_pricing",
                "memoire_technique",
                "ao_monitoring",
                "france",
            ],
            "enterprise_quote",
            "smb",
            "https://doaken.fr/solutions",
            "official_site",
            verified=False,
            hq="FR",
            fr="strong",
            regions=["FR"],
            geo="france",
            pricing_notes="Profils Essentiel/Croissance/Enterprise selon volume ; tarifs sur devis (consulté 2026-06-23).",
            notes="Hébergement France ; couvre marchés publics et privés (détection Sitadel).",
        ),
        v(
            "olra",
            "Olra",
            "https://olra.fr/",
            ["public-procurement-intel"],
            "Plateforme IA marchés publics pour artisans/TPE/PME du bâtiment : veille BOAMP/JOUE/DECP, brief stratégique DCE, rédaction et audit de mémoire technique.",
            [
                "ao_monitoring",
                "dce_analysis",
                "memoire_technique",
                "memoire_audit",
                "france",
            ],
            "enterprise_quote",
            "smb",
            "https://olra.fr/fonctionnalites",
            "official_site",
            verified=False,
            hq="FR",
            fr="strong",
            regions=["FR"],
            geo="france",
            pricing_notes="Plan Essentiel et Plan Pro sur devis ; essai gratuit sans CB (consulté 2026-06-23).",
            notes="Ciblage bâtiment TPE/PME ; chaîne veille→audit→rédaction sans bibliothèque préalable.",
        ),
        v(
            "vecteur-plus",
            "Vecteur Plus",
            "https://vecteurplus.com/",
            ["public-procurement-intel"],
            "Veille opportunités commerciales FR depuis ~30 ans : appels d'offres publics et projets privés, indexation 7 000+ thématiques métier, IA + qualification humaine.",
            [
                "ao_monitoring",
                "private_projects",
                "lead_qualification",
                "email_alerts",
                "france",
            ],
            "enterprise_quote",
            "smb",
            "https://www.vecteurplus.com/commande-publique/",
            "geo_digest",
            verified=False,
            hq="FR",
            fr="strong",
            regions=["FR"],
            geo="france",
            pricing_notes="3 marchés offerts à l'inscription ; abonnement veille sur devis (consulté 2026-06-23).",
            notes="Acteur historique veille AO + projets privés ; 12 000+ sources.",
        ),
    ],
}


# Part 1 — Promotions verified (idées 0001/0029). URLs pricing/sources officielles.
VERIFY_UPDATES: dict[str, dict] = {
    # Parsing inbox — clés revue 0029
    "parseur": {
        "verification_status": "verified",
        "source_url": "https://parseur.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — grille tarifaire officielle parseur.com/pricing (revue 0029).",
    },
    "dext": {
        "verification_status": "verified",
        "source_url": "https://dext.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — page tarifs officielle dext.com/pricing.",
    },
    "mailparser": {
        "verification_status": "verified",
        "source_url": "https://mailparser.io/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — source officielle (remplace listicle).",
    },
    "parsio": {
        "verification_status": "verified",
        "source_url": "https://parsio.io/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — source officielle (remplace listicle).",
    },
    "nylas": {
        "verification_status": "verified",
        "source_url": "https://www.nylas.com/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — page tarifs officielle.",
    },
    "unipile": {
        "verification_status": "verified",
        "source_url": "https://www.unipile.com/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — éditeur FR, page tarifs officielle.",
    },
    "mailjet-parse": {
        "verification_status": "verified",
        "source_url": "https://www.mailjet.com/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — éditeur FR (Sinch), page tarifs officielle.",
    },
    "cloudmailin": {
        "verification_status": "verified",
        "source_url": "https://www.cloudmailin.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — page tarifs officielle.",
    },
    "emailengine": {
        "verification_status": "verified",
        "source_url": "https://emailengine.app/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — page tarifs officielle (licence self-hosted).",
    },
    "unstract": {
        "verification_status": "verified",
        "source_url": "https://unstract.com/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — page tarifs officielle.",
    },
    # Document IDP — clés revue 0029
    "rossum": {
        "verification_status": "verified",
        "source_url": "https://rossum.ai/pricing-plans/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Starter à partir de 18 000 $/an (publié) ; Business/Enterprise/Ultimate sur devis ; engagement minimum 1 an (consulté 2026-06-23).",
        "notes": "Source mise à jour vers page tarifs officielle rossum.ai/pricing-plans (revue 0029).",
    },
    "klippa": {
        "verification_status": "verified",
        "source_url": "https://www.klippa.com/en/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — page tarifs officielle.",
    },
    "mindee": {
        "verification_status": "verified",
        "source_url": "https://www.mindee.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — éditeur FR, page tarifs officielle.",
    },
    "veryfi": {
        "verification_status": "verified",
        "source_url": "https://www.veryfi.com/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — page tarifs officielle.",
    },
    "docsumo": {
        "verification_status": "verified",
        "source_url": "https://www.docsumo.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — page tarifs officielle (remplace comparatif).",
    },
    "affinda": {
        "verification_status": "verified",
        "source_url": "https://www.affinda.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — page tarifs officielle.",
    },
    # Compliance-to-spec — clés revue 0029 (probo FR, regulativ-ai)
    "probo": {
        "verification_status": "verified",
        "source_url": "https://www.probo.io/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — compliance open-source FR (revue 0029).",
    },
    "regulativ-ai": {
        "verification_status": "verified",
        "source_url": "https://www.regulativ.ai/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "notes": "Promotion verified V6b — site officiel (regulatory change → specs).",
    },
}

SEGMENT_PATCHES: dict[str, list[str]] = {}

# Part 3 — Couverture. Marchés publics : +6 nouveaux ; parsing/IDP/kyc : passe de
# re-vérification (sources officielles consultées, 0 nouveau vendeur).
COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "public-procurement-intel": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 7,
            "new_added": 3,
            "pass": PASS_ID,
        },
        "geo_digest": {
            "consulted_at": TODAY,
            "candidates_found": 6,
            "new_added": 3,
            "pass": PASS_ID,
        },
    },
    "parsing-inbox": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 10,
            "new_added": 0,
            "pass": PASS_ID,
        },
    },
    "document-idp": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 10,
            "new_added": 0,
            "pass": PASS_ID,
        },
    },
    "kyc-aml": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 5,
            "new_added": 0,
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
