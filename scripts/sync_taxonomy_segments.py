#!/usr/bin/env python3
"""Synchronise taxonomy.json + fichiers vendors/ pour tous les segments."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAXONOMY_PATH = ROOT / "catalogue-saas" / "taxonomy.json"
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
TODAY = "2026-06-22"

# (id, label, description, category)
ALL_SEGMENTS: list[tuple[str, str, str, str]] = [
    # --- compliance ---
    ("regtech", "RegTech — veille & obligations", "Surveillance réglementaire, extraction d'obligations, mapping policies/contrôles.", "compliance"),
    ("regulatory-reporting-eu", "Reporting réglementaire EU", "E-invoicing, e-reporting, déclarations fiscales, PEPPOL, PDP.", "compliance"),
    ("grc-security", "GRC & conformité sécurité", "SOC2, ISO 27001, GDPR, DORA, NIS2 — contrôles, preuves, audits.", "compliance"),
    ("privacy-consent", "Privacy & consent management", "CMP, cookies, DPIA, droits des personnes, registres de traitement.", "compliance"),
    ("ai-governance", "AI Governance", "EU AI Act, ISO 42001, NIST AI RMF — inventaire IA, risques, artefacts.", "compliance"),
    ("compliance-to-spec", "Réglementation → spec produit", "Exigences traçables, policies-as-code, backlog logiciel testable.", "compliance"),
    ("accessibility-compliance", "Accessibilité numérique", "WCAG, RGAA, audits ERP/sites, conformité secteur public.", "compliance"),
    ("esg-csrd", "ESG & reporting extra-financier", "CSRD, bilan carbone, reporting durabilité, taxonomie verte.", "compliance"),
    ("kyc-aml", "KYC / AML / identity", "Vérification identité, LCB-FT, screening sanctions, onboarding client.", "compliance"),
    ("pharma-regulatory", "Pharma & life sciences regulatory", "GxP, pharmacovigilance, essais cliniques, soumissions réglementaires.", "compliance"),
    # --- security-it ---
    ("cybersecurity-platforms", "Cybersécurité (SIEM/XDR/SOAR)", "Détection menaces, réponse incident, SOC automatisé.", "security-it"),
    ("identity-access-management", "IAM & accès", "SSO, MFA, provisioning, PAM, identity governance.", "security-it"),
    ("cloud-security-cspm", "Cloud security & CSPM", "Posture cloud, misconfigurations, CNAPP, workload protection.", "security-it"),
    ("email-security", "Email security", "Anti-phishing, SEG, DMARC, protection messagerie.", "security-it"),
    ("vulnerability-management", "Vulnérabilités & exposition", "Scan assets, prioritisation CVE, surface d'attaque, pentest as a service.", "security-it"),
    # --- ai-infrastructure ---
    ("llm-api-providers", "API LLM & modèles", "Fournisseurs modèles et APIs (OpenAI, Anthropic, Mistral…).", "ai-infrastructure"),
    ("model-inference-hosting", "Inference & hosting modèles", "Serving, fine-tuning, GPU cloud, déploiement modèles.", "ai-infrastructure"),
    ("vector-databases", "Bases vectorielles", "Embeddings store, recherche sémantique, RAG infra.", "ai-infrastructure"),
    ("ai-evals-testing", "Evals & tests IA", "Évaluation modèles, régression prompts, qualité outputs LLM.", "ai-infrastructure"),
    ("agent-frameworks-platforms", "Frameworks & plateformes agents", "Orchestration agents, tool use, runtimes multi-agents.", "ai-infrastructure"),
    # --- data-documents ---
    ("document-idp", "IDP & extraction documentaire", "PDF/images → JSON structuré, OCR, schémas.", "data-documents"),
    ("parsing-inbox", "Parsing email & inbox", "Email/PDF entrants → champs structurés, webhooks.", "data-documents"),
    ("e-signature", "Signature électronique", "eIDAS, signature, parcours contractuels signés.", "data-documents"),
    ("translation-localization", "Traduction & localisation", "MT, TMS, localisation contenu et produit.", "data-documents"),
    ("data-integration-etl", "Intégration & ETL données", "Pipelines données, reverse ETL, sync warehouses.", "data-documents"),
    # --- ai-workplace ---
    ("ai-productivity", "Productivité IA métier", "Rédaction, slides, synthèse — hors développement.", "ai-workplace"),
    ("ai-copilot-dev", "Copilots IA & dev tools", "Code, agents dev, IDE IA.", "ai-workplace"),
    ("rag-knowledge", "RAG & knowledge enterprise", "Recherche interne, Q&A corpus d'entreprise.", "ai-workplace"),
    ("project-work-management", "Gestion de projet & work OS", "Tâches, roadmaps, wiki — avec couche IA.", "ai-workplace"),
    ("meeting-intelligence", "Meeting intelligence", "Notes, résumés, action items post-réunion.", "ai-workplace"),
    # --- automation ---
    ("automation-platforms", "Automatisation no-code / iPaaS", "Zapier, Make, n8n, Workato…", "automation"),
    ("rpa-enterprise", "RPA enterprise", "Robots UI, automation bureautique à grande échelle.", "automation"),
    # --- agents-outcome ---
    ("support-sales-agents", "Agents support & sales", "Résolution, qualification, SDR — pricing au résultat.", "agents-outcome"),
    ("voice-speech-ai", "Voix & speech IA", "STT, TTS, agents téléphoniques.", "agents-outcome"),
    # --- sales-marketing ---
    ("crm-platforms", "CRM", "Gestion relation client, pipeline, forecasting.", "sales-marketing"),
    ("marketing-automation", "Marketing automation", "Campagnes, nurturing, journeys multicanal.", "sales-marketing"),
    ("seo-content-ai", "SEO & contenu IA", "Rédaction SEO, optimisation, content at scale.", "sales-marketing"),
    ("revenue-intelligence", "Revenue intelligence", "Conversation intelligence, coaching sales, analytics revenus.", "sales-marketing"),
    # --- customer-experience ---
    ("helpdesk-platforms", "Helpdesk & service client", "Ticketing, omnicanal, base de connaissance.", "customer-experience"),
    ("customer-success", "Customer success", "Health scores, onboarding client, churn prevention.", "customer-experience"),
    # --- vertical-finance ---
    ("finance-accounting-ai", "Finance & compta IA", "AP/AR, factures, clôture, contrôles comptables.", "vertical-finance"),
    ("treasury-fpa", "Trésorerie & FP&A", "Cash management, budgeting, forecasting financier.", "vertical-finance"),
    ("spend-procurement", "Spend & procurement", "Achats, fournisseurs, cartes, P2P.", "vertical-finance"),
    # --- vertical-legal ---
    ("legal-contract-ai", "Legal & contract AI", "CLM, revue contrats, legal research.", "vertical-legal"),
    # --- vertical-hr ---
    ("hr-talent-ai", "RH & talent IA", "Recrutement, screening, talent intelligence.", "vertical-hr"),
    ("payroll-hris", "Paie & SIRH", "Paie, core HR, dossiers employés.", "vertical-hr"),
    ("learning-lxp", "Formation & LXP", "LMS, parcours formation, skills development.", "vertical-hr"),
    # --- vertical-health ---
    ("healthcare-clinical-ai", "Santé clinique IA", "Aide diagnostic, documentation clinique, workflows soignants.", "vertical-health"),
    ("health-data-analytics", "Analytics santé & medtech", "Données santé, registres, analytics population.", "vertical-health"),
    # --- vertical-industry ---
    ("real-estate-proptech", "Immobilier & proptech", "Gestion actifs, transactions, estimation, facility.", "vertical-industry"),
    ("insurance-insurtech", "Assurance & insurtech", "Underwriting, sinistres, distribution, actuariat.", "vertical-industry"),
    ("construction-proptech", "Construction & BIM", "Chantiers, plans, conformité construction.", "vertical-industry"),
    ("supply-chain-logistics", "Supply chain & logistique", "WMS, TMS, prévision demande, traçabilité.", "vertical-industry"),
    ("retail-ecommerce-ai", "Retail & e-commerce IA", "Merchandising, pricing, personnalisation, support retail.", "vertical-industry"),
    ("energy-cleantech", "Énergie & cleantech", "Gestion énergie, ENR, réseaux, optimisation conso.", "vertical-industry"),
    # --- data-b2b ---
    ("data-enrichment-b2b", "Enrichissement données B2B", "Firmographics, contacts, signaux d'intent.", "data-b2b"),
    # --- data-analytics ---
    ("bi-analytics-platforms", "BI & analytics", "Dashboards, self-service BI, semantic layer.", "data-analytics"),
    ("data-observability", "Data observability", "Qualité données, lineage, monitoring pipelines.", "data-analytics"),
    # --- france-public ---
    ("public-procurement-intel", "Intelligence marchés publics", "Veille AO, analyse attributions, sourcing public.", "france-public"),
    ("territorial-analytics", "Analytics territoriales", "Observatoires locaux, indicateurs territoire.", "france-public"),
    ("civic-tech-fr", "Civic tech France", "Participation citoyenne, services publics numériques.", "france-public"),
    # --- france-open-data ---
    ("geospatial-gis-fr", "Géospatial & carto FR", "IGN, cadastre, GPU, fonds de cartes.", "france-open-data"),
    ("transport-mobility-data-fr", "Transport & mobilité FR", "GTFS, SNCF, trafic, déserts de mobilité.", "france-open-data"),
    ("energy-buildings-fr", "Bâtiments & énergie FR", "DPE, ADEME, rénovation, passoires thermiques.", "france-open-data"),
    ("environmental-data-fr", "Environnement & risques FR", "Géorisques, eau, air, biodiversité.", "france-open-data"),
    ("electoral-data-fr", "Données électorales FR", "Résultats bureau de vote, analyses territoriales.", "france-open-data"),
    ("public-health-territory-fr", "Santé territoriale FR", "ARS, déserts médicaux, offre de soins.", "france-open-data"),
    ("open-data-governance-fr", "Gouvernance open data FR", "Conformité publication, qualité jeux de données collectivités.", "france-open-data"),
]

CATEGORIES: list[tuple[str, str]] = [
    ("compliance", "Compliance & réglementation"),
    ("security-it", "Sécurité informatique"),
    ("ai-infrastructure", "Infrastructure IA"),
    ("data-documents", "Documents & données"),
    ("ai-workplace", "IA au travail"),
    ("automation", "Automatisation"),
    ("agents-outcome", "Agents & résultats"),
    ("sales-marketing", "Sales & marketing"),
    ("customer-experience", "Expérience client"),
    ("vertical-finance", "Vertical — Finance"),
    ("vertical-legal", "Vertical — Legal"),
    ("vertical-hr", "Vertical — RH"),
    ("vertical-health", "Vertical — Santé"),
    ("vertical-industry", "Vertical — Industrie"),
    ("data-b2b", "Données B2B"),
    ("data-analytics", "Data & analytics"),
    ("france-public", "France — secteur public"),
    ("france-open-data", "France — open data thématique"),
]


def build_taxonomy() -> dict:
    existing = {}
    if TAXONOMY_PATH.exists():
        existing = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))

    return {
        "version": "2.0.0",
        "updated_at": TODAY,
        "segments": [
            {
                "id": seg_id,
                "label": label,
                "description": desc,
                "category": cat,
            }
            for seg_id, label, desc, cat in ALL_SEGMENTS
        ],
        "categories": [{"id": cid, "label": clabel} for cid, clabel in CATEGORIES],
        "pricing_models": existing.get(
            "pricing_models",
            [
                "per_seat",
                "per_usage",
                "per_task",
                "per_document",
                "per_outcome",
                "hybrid",
                "platform_fee",
                "enterprise_quote",
                "freemium",
                "open_source",
            ],
        ),
        "target_markets": existing.get(
            "target_markets", ["self_serve", "smb", "mid_market", "enterprise"]
        ),
        "verification_statuses": existing.get(
            "verification_statuses", ["verified", "partial", "unverified"]
        ),
    }


def sync_vendor_files(segment_ids: set[str]) -> tuple[int, int]:
    created = 0
    for seg_id in sorted(segment_ids):
        path = VENDORS_DIR / f"{seg_id}.json"
        if path.exists():
            continue
        payload = {
            "segment": seg_id,
            "updated_at": TODAY,
            "vendors": [],
        }
        path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        created += 1
    return created, len(segment_ids)


def main() -> None:
    VENDORS_DIR.mkdir(parents=True, exist_ok=True)
    taxonomy = build_taxonomy()
    TAXONOMY_PATH.write_text(
        json.dumps(taxonomy, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    segment_ids = {s["id"] for s in taxonomy["segments"]}
    created, total = sync_vendor_files(segment_ids)

    # Fichiers orphelins (segment absent de taxonomy)
    orphans = []
    for path in VENDORS_DIR.glob("*.json"):
        seg = path.stem
        if seg not in segment_ids:
            orphans.append(path.name)

    print(f"taxonomy: {len(segment_ids)} segments, {len(CATEGORIES)} categories")
    print(f"vendor files: {total} expected, {created} created")
    if orphans:
        print(f"warning: orphan vendor files (not in taxonomy): {', '.join(orphans)}")


if __name__ == "__main__":
    main()
