#!/usr/bin/env python3
"""Vague V6d — compléter gaps marchés publics FR + verified idées 🔁 + fix sources listicle."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v6d-procurement-verify-listicle"


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
            "saqara",
            "Saqara (ex AOS — Appels d'Offres Simplifiés)",
            "https://saqara.com/",
            ["public-procurement-intel"],
            "Suite SaaS BTP pour piloter les AO privés (donneurs d'ordre) et détecter consultations exclusives via Chantier Privé côté entreprises.",
            ["private_btp_tenders", "ao_management", "dce_distribution", "e_signature", "france"],
            "enterprise_quote",
            "mid_market",
            "https://core.saqara.com/",
            "official_site",
            notes="Ex-AOS (go-aos.io → saqara.com) ; segment AO privés BTP, distinct de la veille BOAMP classique.",
        ),
        v(
            "explore",
            "EXPLORE",
            "https://explore.fr/",
            ["public-procurement-intel"],
            "Veille commerciale data-driven (25+ ans) : marchés publics, construction et projets privés avec qualification experte.",
            ["ao_monitoring", "private_projects", "construction_veille", "attribution_analytics", "france"],
            "enterprise_quote",
            "mid_market",
            "https://www.explore.fr/solutions/veille-marches-publics/",
            "official_site",
            notes="Groupe Intescia (Spigao, Bati-Pulse) ; abonnement annuel sur devis.",
        ),
        v(
            "dematis",
            "Dematis",
            "https://www.dematis.com/",
            ["public-procurement-intel"],
            "Éditeur FR (depuis 2003) : dématérialisation marchés publics, veille entreprises, formations et assistant IA Sam IA pour DCE et réponses.",
            ["e_procurement", "ao_monitoring", "sam_ia", "dce_analysis", "go_nogo", "memoire_technique", "france"],
            "enterprise_quote",
            "mid_market",
            "https://formation.dematis.com/sam-ia/",
            "official_site",
            pricing_notes="Sam IA : forfait Découverte 500 crédits sans engagement ; forfaits sur mesure dès 1 000 crédits (consulté 2026-06-23).",
        ),
        v(
            "centrale-des-marches",
            "Centrale des Marchés",
            "https://centraledesmarches.com/",
            ["public-procurement-intel"],
            "Portail Medialex (2021) de veille marchés publics et privés : recherche géolocalisée, alertes email et formations.",
            ["ao_monitoring", "email_alerts", "private_projects", "geo_search", "france"],
            "freemium",
            "smb",
            "https://centraledesmarches.com/",
            "official_site",
            pricing_notes="Compte et veille gratuits ; alertes premium non affichées publiquement (consulté 2026-06-23).",
        ),
        v(
            "tendly",
            "Tendly",
            "https://tendly.eu/fr/",
            ["public-procurement-intel"],
            "Plateforme IA multi-pays (FR incluse) : matching AO publics, analyse risques/concurrence et génération de documents de soumission.",
            ["ao_monitoring", "ai_matching", "dce_analysis", "document_generation", "risk_analysis", "france"],
            "hybrid",
            "smb",
            "https://tendly.eu/fr/pricing",
            "official_site",
            verified=True,
            pricing_notes="Gratuit (20 cr. uniques) ; Professionnel 29 €/mois (200 cr.) ; Entreprise 149 €/mois (400 cr.) ; packs dès 15 € (consulté 2026-06-23).",
        ),
        v(
            "remporte",
            "Remporte",
            "https://remporte.fr/",
            ["public-procurement-intel"],
            "Logiciel IA FR (Flowt, 2024) pour PME/ETI : analyse DCE, scoring Go/No-Go 13 critères et rédaction mémoires techniques hébergés en France.",
            ["dce_analysis", "go_nogo", "memoire_technique", "ai_response", "knowledge_base", "france"],
            "hybrid",
            "mid_market",
            "https://remporte.fr/tarifs/",
            "official_site",
            verified=True,
            pricing_notes="Starter 4 000 € HT/an (15 AO rédigés) ; Regular et Citadelle (on-premise OIV) sur devis (consulté 2026-06-23).",
        ),
        v(
            "tendiz",
            "Tendiz",
            "https://tendiz.ai/",
            ["public-procurement-intel"],
            "Plateforme IA FR : agrégation 30+ sources (BOAMP, TED…), scoring sémantique et génération de dossiers de candidature.",
            ["ao_monitoring", "ai_matching", "dce_analysis", "memoire_technique", "competitive_scoring", "france"],
            "enterprise_quote",
            "smb",
            "https://tendiz.ai/",
            "official_site",
            notes="Ne pas confondre avec Tendrix (tendrix.fr) ; tarifs sur devis.",
        ),
        v(
            "e-marchespublics",
            "e-marchespublics.com",
            "https://www.e-marchespublics.com/",
            ["public-procurement-intel"],
            "Portail Dematis de publication et veille AO : consultation gratuite, alertes E-MP, extensions BOAMP/JOUE/presse et dépôt électronique.",
            ["ao_monitoring", "ao_publication", "e_procurement", "dce_download", "electronic_bid", "france"],
            "freemium",
            "smb",
            "https://www.e-marchespublics.com/",
            "official_site",
            pricing_notes="Veille sur avis E-MP gratuite ; extension BOAMP/JOUE/presse (~600k AO/an) sur devis (consulté 2026-06-23).",
            notes="Produit éditorial Dematis — lier à l'entrée dematis sans fusionner.",
        ),
    ],
}

VERIFY_UPDATES: dict[str, dict] = {
    # 0001 — public-procurement-intel
    "olra": {
        "verification_status": "verified",
        "source_url": "https://olra.fr/tarifs",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Essentiel/Pro/Entreprise sur devis ; essai 14 j sans CB ; quotas 500/1500 pages/mois (consulté 2026-06-23).",
    },
    "publikconnect": {
        "verification_status": "verified",
        "source_url": "https://publikconnect.fr/tarifs",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Découverte 0 € ; Pro 49 € HT/mois ; Fondateur 39 € HT/mois à vie (consulté 2026-06-23).",
    },
    "marchespublics-ai": {
        "verification_status": "verified",
        "source_url": "https://marchespublics.ai/tarifs",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Starter 149 € HT/mo, Pro 399 €, Business 1 290 € ; plans acheteurs publics séparés (consulté 2026-06-23).",
    },
    # 0002 — open-data-governance-fr
    "validata": {
        "verification_status": "verified",
        "source_url": "https://validata.fr/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Plateforme publique de validation vs schémas schema.data.gouv.fr (consulté 2026-06-23).",
    },
    # 0009 — energy-buildings-fr
    "homeys": {
        "verification_status": "verified",
        "source_url": "https://www.homeys.fr/tarifs",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Energy Analytics 99 € HT/mois ; Energy Management 149 € HT/mois (consulté 2026-06-23).",
    },
    "effy-pro": {
        "verification_status": "verified",
        "source_url": "https://www.effy.fr/pro",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Gestion Prime CEE gratuite ; Projets Qualifiés dès 39 € HT/projet (consulté 2026-06-23).",
    },
    # 0025 — real-estate-proptech
    "cityscan": {
        "verification_status": "verified",
        "source_url": "https://www.cityscan.fr/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Avis de Valeur dès 39 € HT/mois ; Captation leads dès 30 € HT/mois (consulté 2026-06-23).",
    },
    # 0026 / 0028 — territorial + geospatial
    "smappen": {
        "verification_status": "verified",
        "source_url": "https://www.smappen.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Free / Essential / Pro / Advanced ; démographie FR/BE incluse (consulté 2026-06-23).",
    },
    "geomarket": {
        "verification_status": "verified",
        "source_url": "https://ancre.geomarket.one/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Standard 42 € HT/étude ; Pro 60 € ; Abonnement Pro 300 € HT/mois (consulté 2026-06-23).",
    },
    # 0028 — data-enrichment-b2b
    "dropcontact": {
        "verification_status": "verified",
        "source_url": "https://www.dropcontact.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Starter 79 €/mois (500 crédits) ; Growth 120 € ; Entreprise sur volume (consulté 2026-06-23).",
    },
    "hunter-io": {
        "verification_status": "verified",
        "source_url": "https://hunter.io/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Free 50 crédits/mo ; Starter $49/mo ; Growth $149 ; Scale $299 (consulté 2026-06-23).",
    },
    "datagma": {
        "verification_status": "verified",
        "source_url": "https://datagma.com/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Regular $49/mo, Popular $99, Expert $249 ; éditeur FR (consulté 2026-06-23).",
    },
    "kaspr": {
        "verification_status": "verified",
        "source_url": "https://www.kaspr.io/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Free 15 crédits ; Starter €45/mo ; Business €79/mo ; éditeur FR (consulté 2026-06-23).",
    },
    # 0029 — automation / document-idp / parsing
    "windmill": {
        "verification_status": "verified",
        "source_url": "https://www.windmill.dev/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Community $0 ; Team ~$10/seat/mo ; Enterprise sur devis (consulté 2026-06-23).",
    },
    "kestra": {
        "verification_status": "verified",
        "source_url": "https://kestra.io/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Open Source gratuit ; Enterprise sur devis ; Kestra Cloud pay-as-you-scale (consulté 2026-06-23).",
    },
    "super-ai": {
        "verification_status": "verified",
        "source_url": "https://super.ai/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Starter Free (25k crédits) ; Growth $140/mo ; Enterprise custom (consulté 2026-06-23).",
    },
    "budibase": {
        "verification_status": "verified",
        "source_url": "https://budibase.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Pro $19/mo ; Premium $49 ; Business $299 ; OSS self-host gratuit (consulté 2026-06-23).",
    },
    "inngest": {
        "verification_status": "verified",
        "source_url": "https://www.inngest.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Hobby $0 (50k exécutions) ; Pro dès $75/mo ; Enterprise custom (consulté 2026-06-23).",
    },
    "mailbutler": {
        "verification_status": "verified",
        "source_url": "https://www.mailbutler.io/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Starter ~$5/user/mo ; Professional ~$9 ; Business sur devis (consulté 2026-06-23).",
    },
    # listicle → official (verified)
    "zapier": {
        "verification_status": "verified",
        "source_url": "https://zapier.com/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace pickaxe.co ; page tarifs officielle (consulté 2026-06-23).",
    },
    "activepieces": {
        "verification_status": "verified",
        "source_url": "https://www.activepieces.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Standard gratuit puis $5/flow actif/mo ; Ultimate sur contrat annuel (consulté 2026-06-23).",
    },
    "airparser": {
        "verification_status": "verified",
        "source_url": "https://airparser.com/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Starter $33/mo, Growth $49, Premium $249 (annuel) (consulté 2026-06-23).",
    },
    "replit": {
        "verification_status": "verified",
        "source_url": "https://replit.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Starter Free ; Core $20/mo annuel ; Pro $95/mo (consulté 2026-06-23).",
    },
    "azure-document-intelligence": {
        "verification_status": "verified",
        "source_url": "https://azure.microsoft.com/en-us/pricing/details/ai-document-intelligence/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Tarification Azure pay-as-you-go ; remplace comparatif extend.ai (consulté 2026-06-23).",
    },
    # listicle → official (partial, URL nettoyée)
    "make": {
        "source_url": "https://www.make.com/en/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Source officielle ; remplace pickaxe.co (consulté 2026-06-23).",
    },
    "docparser": {
        "source_url": "https://docparser.com/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Source officielle ; remplace parsio.io listicle (consulté 2026-06-23).",
    },
    "microsoft-power-automate": {
        "source_url": "https://www.microsoft.com/en-us/power-platform/products/power-automate/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Source officielle Microsoft ; remplace blog youngju.dev (consulté 2026-06-23).",
    },
    "tines": {
        "source_url": "https://www.tines.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "URL tarifs officielle ; remplace youngju.dev (consulté 2026-06-23).",
    },
    "extracta-ai": {
        "source_url": "https://extracta.ai/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Page pricing officielle ; remplace listicle (consulté 2026-06-23).",
    },
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "public-procurement-intel": {
        "geo_digest": {
            "consulted_at": TODAY,
            "candidates_found": 10,
            "new_added": 8,
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
