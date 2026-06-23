#!/usr/bin/env python3
"""Vague 5m — verticaux métiers + compliance fins (5→~10 vendeurs/segment)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v5m-verticals-compliance"


def v(
    id_: str, name: str, url: str, segments: list[str], desc: str, caps: list[str],
    pricing: str, market: str, source: str, src_type: str,
    hq: str = "FR", fr: str = "strong", regions: list[str] | None = None,
    geo: str = "france", notes: str | None = None,
) -> dict:
    d = {
        "id": id_, "name": name, "url": url, "segments": segments,
        "description": desc, "capabilities": caps, "pricing_model": pricing,
        "target_market": market, "geography": geo, "hq_country": hq,
        "france_market": fr, "operating_regions": regions or ["FR", "EU"],
        "discovery_source": src_type, "discovery_pass": PASS_ID,
        "source_url": source, "source_consulted_at": TODAY,
        "verification_status": "partial",
    }
    if notes:
        d["notes"] = notes
    return d


ADDITIONS: dict[str, list[dict]] = {
    "regulatory-reporting-eu.json": [
        v("cegid", "Cegid", "https://www.cegid.com/fr/facturation-electronique/", ["regulatory-reporting-eu"],
          "Suite ERP/finance FR ; facturation électronique réforme 2026, TVA et reporting fiscal multi-entités.", ["e_invoicing", "erp", "vat", "france_reform"], "enterprise_quote", "enterprise",
          "https://www.cegid.com/", "official_site", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("basware", "Basware", "https://www.basware.com/", ["regulatory-reporting-eu"],
          "Réseau e-invoicing et AP automation ; conformité Peppol, TVA et reporting statutaire Europe.", ["peppol", "e_invoicing", "ap_automation", "vat"], "enterprise_quote", "enterprise",
          "https://www.basware.com/", "g2", hq="FI", fr="partial", regions=["US", "EU"], geo="europe"),
        v("tradeshift", "Tradeshift", "https://tradeshift.com/", ["regulatory-reporting-eu"],
          "Plateforme B2B trade ; facturation électronique, supply chain finance et conformité multi-pays EU.", ["e_invoicing", "b2b_network", "compliance", "multi_country"], "enterprise_quote", "enterprise",
          "https://tradeshift.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("storecove", "Storecove", "https://www.storecove.com/", ["regulatory-reporting-eu"],
          "Gateway Peppol et e-invoicing ; routage factures B2B/B2G et conformité directives EU.", ["peppol", "e_invoicing_gateway", "b2g", "routing"], "hybrid", "mid_market",
          "https://www.storecove.com/", "g2", hq="NL", fr="partial", regions=["US", "EU"], geo="europe"),
        v("comarch-einvoicing", "Comarch e-Invoicing", "https://www.comarch.com/finance/e-invoicing/", ["regulatory-reporting-eu"],
          "E-invoicing et reporting fiscal EU ; intégration ERP, archivage légal et TVA.", ["e_invoicing", "erp_integration", "legal_archive", "vat"], "enterprise_quote", "enterprise",
          "https://www.comarch.com/", "g2", hq="PL", fr="partial", regions=["US", "EU"], geo="europe"),
        v("edicom", "EDICOM", "https://edicomgroup.com/", ["regulatory-reporting-eu"],
          "EDI et e-invoicing global ; conformité facturation électronique et reporting réglementaire EU/LATAM.", ["edi", "e_invoicing", "compliance", "global_reporting"], "enterprise_quote", "enterprise",
          "https://edicomgroup.com/", "g2", hq="ES", fr="partial", regions=["US", "EU"], geo="global"),
    ],
    "accessibility-compliance.json": [
        v("accessiway", "Accessiway", "https://www.accessiway.com/", ["accessibility-compliance"],
          "Audit et remédiation accessibilité web ; conformité RGAA/WCAG et accompagnement éditeurs FR.", ["wcag", "rgaa", "audit", "remediation"], "hybrid", "mid_market",
          "https://www.accessiway.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("tanaguru", "Tanaguru", "https://www.tanaguru.com/", ["accessibility-compliance"],
          "Suite tests accessibilité ; moteur Tanaguru, CI/CD et conformité RGAA/WCAG pour équipes dev.", ["automated_testing", "rgaa", "wcag", "ci_cd"], "hybrid", "mid_market",
          "https://www.tanaguru.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("asqatasun", "Asqatasun", "https://asqatasun.org/", ["accessibility-compliance"],
          "Outil open source audit accessibilité ; scans RGAA/WCAG et rapports pour sites publics/privés.", ["open_source", "rgaa", "wcag", "audit_reports"], "freemium", "mid_market",
          "https://asqatasun.org/", "open_source", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("facil-iti", "Facil'iti", "https://www.facil-iti.com/", ["accessibility-compliance"],
          "Overlay accessibilité ; adaptation affichage dyslexie, malvoyance et profils cognitifs sur sites web.", ["accessibility_overlay", "cognitive", "visual", "personalization"], "hybrid", "mid_market",
          "https://www.facil-iti.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("eye-able", "Eye-Able", "https://eye-able.com/", ["accessibility-compliance"],
          "Widget et audit accessibilité EU ; conformité WCAG/EN 301 549 et rapports conformité.", ["accessibility_widget", "wcag", "en301549", "audit"], "hybrid", "smb",
          "https://eye-able.com/", "g2", hq="DE", fr="partial", regions=["US", "EU"], geo="europe"),
        v("silktide", "Silktide", "https://silktide.com/", ["accessibility-compliance"],
          "Monitoring accessibilité et qualité web ; scans WCAG, tableaux de bord et alertes régression.", ["wcag_monitoring", "quality_web", "alerts", "dashboards"], "hybrid", "mid_market",
          "https://silktide.com/", "g2", hq="GB", fr="partial", regions=["US", "EU"], geo="europe"),
    ],
    "esg-csrd.json": [
        v("sweep", "Sweep", "https://www.sweep.net/", ["esg-csrd"],
          "Carbon management FR ; inventaire GHG, trajectoire SBTi et reporting CSRD pour mid-market.", ["carbon_management", "ghg_inventory", "csrd", "sbti"], "hybrid", "mid_market",
          "https://www.sweep.net/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("plan-a", "Plan A", "https://plan-a.earth/", ["esg-csrd"],
          "Plateforme décarbonation EU ; mesure émissions, plans d'action et disclosures CSRD/ESRS.", ["decarbonization", "csrd", "esrs", "action_plans"], "enterprise_quote", "mid_market",
          "https://plan-a.earth/", "g2", hq="DE", fr="partial", regions=["US", "EU"], geo="europe"),
        v("ecovadis", "EcoVadis", "https://www.ecovadis.com/", ["esg-csrd"],
          "Ratings durabilité supply chain ; questionnaires ESG fournisseurs et benchmarks sectoriels.", ["supplier_ratings", "esg_scorecards", "supply_chain", "benchmarks"], "enterprise_quote", "enterprise",
          "https://www.ecovadis.com/", "analyst_report", hq="FR", fr="strong", regions=["FR", "EU"], geo="global"),
        v("carbonfact", "Carbonfact", "https://www.carbonfact.com/", ["esg-csrd"],
          "Carbon accounting mode/textile ; ACV produits, données matières et reporting CSRD retail.", ["product_carbon", "lca", "fashion", "csrd"], "hybrid", "mid_market",
          "https://www.carbonfact.com/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("carbonmaps", "Carbon Maps", "https://www.carbonmaps.io/", ["esg-csrd", "energy-cleantech"],
          "ACV alimentaire et agro ; données produits, scopes 3 et reporting extra-financier CSRD.", ["food_lca", "scope_3", "product_data", "csrd"], "hybrid", "mid_market",
          "https://www.carbonmaps.io/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("ibm-envizi", "IBM Envizi", "https://www.ibm.com/products/envizi", ["esg-csrd"],
          "ESG data platform ; consolidation KPIs, reporting CSRD/GRI et analytics énergie/carbone.", ["esg_data", "csrd_reporting", "kpi_consolidation", "energy_analytics"], "enterprise_quote", "enterprise",
          "https://www.ibm.com/products/envizi", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
    ],
    "pharma-regulatory.json": [
        v("extedo", "EXTEDO", "https://www.extedo.com/", ["pharma-regulatory"],
          "Suite regulatory information management ; eCTD, submissions et veille réglementaire pharma EU/US.", ["ectd", "rim", "submissions", "regulatory_intelligence"], "enterprise_quote", "enterprise",
          "https://www.extedo.com/", "g2", hq="DE", fr="partial", regions=["US", "EU"], geo="europe"),
        v("labvantage", "LabVantage", "https://www.labvantage.com/", ["pharma-regulatory"],
          "LIMS enterprise ; traçabilité échantillons, workflows GxP et dossiers qualité pharma.", ["lims", "gxp", "sample_tracking", "quality"], "enterprise_quote", "enterprise",
          "https://www.labvantage.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("dotmatics", "Dotmatics", "https://www.dotmatics.com/", ["pharma-regulatory"],
          "R&D data platform life sciences ; ELN, LIMS et regulatory data management.", ["eln", "lims", "rd_data", "regulatory_data"], "enterprise_quote", "enterprise",
          "https://www.dotmatics.com/", "g2", hq="GB", fr="partial", regions=["US", "EU"], geo="global"),
        v("medidata", "Medidata (Dassault Systèmes)", "https://www.medidata.com/", ["pharma-regulatory", "health-data-analytics"],
          "Clinical cloud ; essais cliniques, RWE et conformité réglementaire FDA/EMA.", ["clinical_trials", "rwe", "regulatory_compliance", "edc"], "enterprise_quote", "enterprise",
          "https://www.medidata.com/", "analyst_report", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("benchling", "Benchling", "https://www.benchling.com/", ["pharma-regulatory"],
          "R&D cloud biotech ; ELN, registres moléculaires et workflows qualité réglementaire.", ["eln", "molecular_registry", "biotech", "quality_workflows"], "enterprise_quote", "enterprise",
          "https://www.benchling.com/", "crunchbase", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("certara", "Certara", "https://www.certara.com/", ["pharma-regulatory"],
          "Modélisation biosimulation ; soumissions réglementaires, pharmacométrie et dossiers FDA/EMA.", ["biosimulation", "regulatory_submissions", "pharmacometrics", "fda_ema"], "enterprise_quote", "enterprise",
          "https://www.certara.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
    ],
    "privacy-consent.json": [
        v("iubenda", "iubenda", "https://www.iubenda.com/", ["privacy-consent"],
          "Générateur politiques/CMP ; consentement cookies, privacy policy et conformité GDPR multi-langues.", ["cmp", "privacy_policy", "cookie_consent", "gdpr"], "hybrid", "smb",
          "https://www.iubenda.com/", "g2", hq="IT", fr="partial", regions=["US", "EU"], geo="europe"),
        v("termly", "Termly", "https://termly.io/", ["privacy-consent"],
          "CMP et compliance hub ; bannières cookies, DSAR et assessments GDPR/CCPA.", ["cmp", "cookie_banner", "dsar", "assessments"], "hybrid", "smb",
          "https://termly.io/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("cookieyes", "CookieYes", "https://www.cookieyes.com/", ["privacy-consent"],
          "CMP cookies ; scan automatique, consentement granulaire et logs preuve GDPR.", ["cmp", "cookie_scan", "consent_logs", "gdpr"], "hybrid", "smb",
          "https://www.cookieyes.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("sirdata", "Sirdata", "https://www.sirdata.com/", ["privacy-consent"],
          "Consent management et data clean room FR ; CMP, préférences et conformité ePrivacy.", ["cmp", "consent", "data_clean_room", "eprivacy"], "hybrid", "mid_market",
          "https://www.sirdata.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("tarteaucitron", "tarteaucitron.js", "https://tarteaucitron.io/", ["privacy-consent"],
          "CMP open source FR ; gestion tags/cookies, opt-in granulaire et conformité CNIL.", ["open_source", "cmp", "cnil", "tag_management"], "freemium", "smb",
          "https://tarteaucitron.io/", "open_source", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("usercentrics", "Usercentrics", "https://usercentrics.com/", ["privacy-consent"],
          "CMP enterprise EU ; consentement multi-domaines, TCF IAB et privacy governance.", ["cmp", "tcf", "multi_domain", "privacy_governance"], "hybrid", "mid_market",
          "https://usercentrics.com/", "g2", hq="DE", fr="partial", regions=["US", "EU"], geo="europe"),
    ],
    "insurance-insurtech.json": [
        v("akur8", "Akur8", "https://www.akur8.com/", ["insurance-insurtech"],
          "Pricing et underwriting IA ; modèles transparents, tarification P&C et conformité actuarielle.", ["pricing", "underwriting", "transparent_ai", "p_and_c"], "enterprise_quote", "enterprise",
          "https://www.akur8.com/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("wakam", "Wakam", "https://www.wakam.com/", ["insurance-insurtech"],
          "Assureur digital B2B2C FR ; APIs underwriting, distribution partenaires et produits modulaires.", ["b2b2c", "api_insurance", "underwriting", "distribution"], "enterprise_quote", "enterprise",
          "https://www.wakam.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("qover", "Qover", "https://www.qover.com/", ["insurance-insurtech"],
          "Insurtech API EU ; intégration assurance embarquée e-commerce, mobility et fintech.", ["embedded_insurance", "api", "ecommerce", "partnerships"], "hybrid", "mid_market",
          "https://www.qover.com/", "crunchbase", hq="BE", fr="partial", regions=["US", "EU"], geo="europe"),
        v("luko", "Luko (Allianz Direct)", "https://www.luko.eu/", ["insurance-insurtech"],
          "Assurance habitation digitale FR ; souscription en ligne, IoT prévention sinistres et claims app.", ["home_insurance", "digital_underwriting", "iot", "claims_app"], "hybrid", "self_serve",
          "https://www.luko.eu/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("alan", "Alan", "https://alan.com/", ["insurance-insurtech", "healthcare-clinical-ai"],
          "Assurance santé digitale FR ; complémentaire, téléconsultation et parcours de soins intégrés.", ["health_insurance", "telehealth", "member_app", "france"], "hybrid", "mid_market",
          "https://alan.com/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("wefox", "wefox", "https://www.wefox.com/", ["insurance-insurtech"],
          "Insurtech européen ; distribution polices, CRM courtiers et analytics portefeuille.", ["distribution", "broker_crm", "portfolio_analytics", "europe"], "hybrid", "mid_market",
          "https://www.wefox.com/", "crunchbase", hq="DE", fr="partial", regions=["US", "EU"], geo="europe"),
    ],
    "construction-proptech.json": [
        v("finalcad", "Finalcad", "https://www.finalcad.com/", ["construction-proptech"],
          "Pilotage chantier mobile FR ; plans BIM, rapports terrain et suivi avancement pour GC.", ["field_reporting", "bim_plans", "progress_tracking", "mobile"], "hybrid", "mid_market",
          "https://www.finalcad.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("dalux", "Dalux", "https://www.dalux.com/", ["construction-proptech"],
          "BIM field management ; QA/QC, snags et collaboration maîtrise d'ouvrage/entreprises EU.", ["bim", "qa_qc", "snagging", "collaboration"], "hybrid", "mid_market",
          "https://www.dalux.com/", "g2", hq="DK", fr="partial", regions=["US", "EU"], geo="europe"),
        v("buildots", "Buildots", "https://buildots.com/", ["construction-proptech"],
          "Progress tracking IA ; computer vision chantier, comparaison BIM/as-built et retards.", ["computer_vision", "bim_comparison", "progress_ai", "delays"], "enterprise_quote", "enterprise",
          "https://buildots.com/", "crunchbase", hq="IL", fr="partial", regions=["US", "EU"], geo="global"),
        v("openspace", "OpenSpace", "https://www.openspace.ai/", ["construction-proptech"],
          "Capture 360° chantier ; timeline visuelle, documentation as-built et intégration BIM.", ["360_capture", "visual_timeline", "as_built", "bim_integration"], "hybrid", "mid_market",
          "https://www.openspace.ai/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("catenda", "Catenda", "https://catenda.com/", ["construction-proptech"],
          "Collaboration BIM cloud ; maquettes 3D, BCF issues et workflows openBIM Europe.", ["openbim", "bcf", "3d_models", "cloud_collaboration"], "hybrid", "mid_market",
          "https://catenda.com/", "g2", hq="NO", fr="partial", regions=["US", "EU"], geo="europe"),
        v("graneet", "Graneet", "https://www.graneet.com/", ["construction-proptech"],
          "ERP finance BTP FR ; devis, situations travaux, trésorerie chantier et marge temps réel.", ["construction_erp", "billing", "cashflow", "margin_tracking"], "hybrid", "smb",
          "https://www.graneet.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
    ],
    "supply-chain-logistics.json": [
        v("shippeo", "Shippeo", "https://www.shippeo.com/", ["supply-chain-logistics"],
          "ETA tracking temps réel FR ; visibilité transport multimodal et alertes exceptions.", ["eta_tracking", "multimodal", "exceptions", "real_time"], "enterprise_quote", "enterprise",
          "https://www.shippeo.com/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("transporeon", "Transporeon", "https://www.transporeon.com/", ["supply-chain-logistics"],
          "Transport management EU ; e-tendering, slot booking et visibilité exécution transport.", ["transport_management", "slot_booking", "e_tendering", "visibility"], "enterprise_quote", "enterprise",
          "https://www.transporeon.com/", "g2", hq="DE", fr="partial", regions=["US", "EU"], geo="europe"),
        v("o9-solutions", "o9 Solutions", "https://o9solutions.com/", ["supply-chain-logistics"],
          "Planning supply chain IA ; demand, inventory, S&OP et digital twin supply chain.", ["demand_planning", "s_and_op", "inventory", "digital_twin"], "enterprise_quote", "enterprise",
          "https://o9solutions.com/", "analyst_report", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("blue-yonder", "Blue Yonder", "https://blueyonder.com/", ["supply-chain-logistics"],
          "Supply chain suite ; WMS, TMS, forecasting et orchestration retail/industrie.", ["wms", "tms", "forecasting", "orchestration"], "enterprise_quote", "enterprise",
          "https://blueyonder.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("relex", "RELEX Solutions", "https://www.relexsolutions.com/", ["supply-chain-logistics"],
          "Retail supply chain planning ; prévisions demande, assortiment et replenishment EU.", ["demand_forecasting", "assortment", "replenishment", "retail"], "enterprise_quote", "enterprise",
          "https://www.relexsolutions.com/", "g2", hq="FI", fr="partial", regions=["US", "EU"], geo="europe"),
        v("sennder", "sennder", "https://www.sennder.com/", ["supply-chain-logistics"],
          "Fret digital EU ; marketplace transport routier, pricing dynamique et tracking.", ["digital_freight", "road_transport", "marketplace", "tracking"], "hybrid", "mid_market",
          "https://www.sennder.com/", "crunchbase", hq="DE", fr="partial", regions=["US", "EU"], geo="europe"),
    ],
    "retail-ecommerce-ai.json": [
        v("mirakl", "Mirakl", "https://www.mirakl.com/", ["retail-ecommerce-ai"],
          "Marketplace platform FR ; catalogues sellers, pricing IA et orchestration commandes omnicanal.", ["marketplace", "seller_management", "ai_pricing", "omnichannel"], "enterprise_quote", "enterprise",
          "https://www.mirakl.com/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="global"),
        v("contentsquare", "Contentsquare", "https://contentsquare.com/", ["retail-ecommerce-ai"],
          "Analytics expérience digitale FR ; heatmaps, journey AI et optimisation conversion e-commerce.", ["digital_analytics", "journey_ai", "conversion", "heatmaps"], "enterprise_quote", "enterprise",
          "https://contentsquare.com/", "analyst_report", hq="FR", fr="strong", regions=["FR", "EU"], geo="global"),
        v("ab-tasty", "AB Tasty", "https://www.abtasty.com/", ["retail-ecommerce-ai"],
          "Experimentation et personalization FR ; A/B testing, recommandations IA et feature flags.", ["ab_testing", "personalization", "feature_flags", "recommendations"], "hybrid", "mid_market",
          "https://www.abtasty.com/", "g2", hq="FR", fr="strong", regions=["FR", "EU"], geo="global"),
        v("lengow", "Lengow", "https://www.lengow.com/", ["retail-ecommerce-ai"],
          "Feed management e-commerce FR ; diffusion marketplaces, pricing et analytics multicanal.", ["feed_management", "marketplaces", "multichannel", "pricing"], "hybrid", "mid_market",
          "https://www.lengow.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="europe"),
        v("ankorstore", "Ankorstore", "https://www.ankorstore.com/", ["retail-ecommerce-ai"],
          "Marketplace B2B retail FR ; découverte marques, commandes grossistes et IA assortiment.", ["b2b_marketplace", "wholesale", "brand_discovery", "assortment_ai"], "hybrid", "smb",
          "https://www.ankorstore.com/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="europe"),
        v("prestashop", "PrestaShop", "https://www.prestashop.com/", ["retail-ecommerce-ai"],
          "Plateforme e-commerce open source FR ; storefront, modules IA et écosystème agences.", ["ecommerce_platform", "open_source", "modules", "storefront"], "hybrid", "smb",
          "https://www.prestashop.com/", "official_site", hq="FR", fr="strong", regions=["FR", "EU"], geo="global"),
    ],
    "energy-cleantech.json": [
        v("octopus-energy", "Octopus Energy", "https://octopusenergy.com/", ["energy-cleantech"],
          "Retail énergie et tech cleantech ; tariffs dynamiques, Kraken platform et flexibilité réseau.", ["retail_energy", "dynamic_tariffs", "kraken_platform", "flexibility"], "hybrid", "mid_market",
          "https://octopusenergy.com/", "analyst_report", hq="GB", fr="partial", regions=["US", "EU"], geo="europe"),
        v("tiko", "Tiko", "https://tiko.energy/", ["energy-cleantech"],
          "Flexibilité énergétique résidentielle ; agrégation DER, demand response et services utilities EU.", ["demand_response", "der_aggregation", "residential", "utilities"], "enterprise_quote", "enterprise",
          "https://tiko.energy/", "crunchbase", hq="CH", fr="partial", regions=["US", "EU"], geo="europe"),
        v("voltalis", "Voltalis", "https://www.voltalis.com/", ["energy-cleantech"],
          "Effacement demande B2B FR ; pilotage charges électriques, RTE/CBP et rémunération flexibilité.", ["demand_response", "load_control", "rte", "b2b_flexibility"], "enterprise_quote", "enterprise",
          "https://www.voltalis.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("schneider-ecostruxure", "Schneider EcoStruxure", "https://www.se.com/ww/en/work/solutions/system/s1/ecostruxure/", ["energy-cleantech"],
          "IoT énergie bâtiments/industrie FR ; monitoring, EMS et décarbonation portefeuilles.", ["ems", "iot_energy", "building_management", "decarbonation"], "enterprise_quote", "enterprise",
          "https://www.se.com/", "official_site", hq="FR", fr="strong", regions=["FR", "EU"], geo="global"),
        v("kizy", "Kizy", "https://www.kizy.io/", ["energy-cleantech"],
          "Collecte données énergie tertiaire FR ; capteurs IoT, analytics conso et reporting décret tertiaire.", ["iot_sensors", "energy_analytics", "tertiary", "reporting"], "hybrid", "mid_market",
          "https://www.kizy.io/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("totalenergies-digital", "TotalEnergies Digital Services", "https://totalenergies.com/", ["energy-cleantech"],
          "Services digitaux énergie ; pilotage conso B2B, PPAs et solutions décarbonation corporate.", ["b2b_energy", "ppa", "corporate_decarbonation", "energy_services"], "enterprise_quote", "enterprise",
          "https://totalenergies.com/", "official_site", hq="FR", fr="strong", regions=["FR", "EU"], geo="global"),
    ],
    "healthcare-clinical-ai.json": [
        v("qare", "Qare", "https://www.qare.fr/", ["healthcare-clinical-ai"],
          "Téléconsultation FR ; médecins généralistes/spécialistes, ordonnances et intégration mutuelles.", ["teleconsultation", "prescriptions", "france", "mutuelle_integration"], "hybrid", "self_serve",
          "https://www.qare.fr/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("medadom", "Medadom", "https://www.medadom.com/", ["healthcare-clinical-ai"],
          "Téléconsultation et visite domicile FR ; triage, médecins et infirmiers on-demand.", ["teleconsultation", "home_visit", "triage", "france"], "hybrid", "self_serve",
          "https://www.medadom.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("lifen", "Lifen", "https://www.lifen.fr/", ["healthcare-clinical-ai"],
          "Messagerie médicale sécurisée FR ; échange DMP/documents et workflows hospitaliers/clinique.", ["medical_messaging", "dmp", "hospital_workflows", "hds"], "enterprise_quote", "enterprise",
          "https://www.lifen.fr/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("owkin", "Owkin", "https://owkin.com/", ["healthcare-clinical-ai", "health-data-analytics"],
          "IA federated learning santé FR ; recherche clinique, biomarqueurs et analytics multi-sites.", ["federated_learning", "clinical_research", "biomarkers", "health_ai"], "enterprise_quote", "enterprise",
          "https://owkin.com/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="global"),
        v("infermedica", "Infermedica", "https://infermedica.com/", ["healthcare-clinical-ai"],
          "Triage symptômes IA ; API diagnostic différentiel, parcours patient et intégration EHR.", ["symptom_checker", "triage_ai", "api", "ehr_integration"], "hybrid", "mid_market",
          "https://infermedica.com/", "g2", hq="PL", fr="partial", regions=["US", "EU"], geo="europe"),
        v("caresyntax", "Caresyntax", "https://www.caresyntax.com/", ["healthcare-clinical-ai"],
          "Analytics bloc opératoire ; IA perf chirurgicale, checklists et qualité/soins peri-op.", ["surgical_analytics", "or_ai", "quality_metrics", "perioperative"], "enterprise_quote", "enterprise",
          "https://www.caresyntax.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
    ],
    "health-data-analytics.json": [
        v("openhealth", "OpenHealth", "https://www.openhealth.fr/", ["health-data-analytics"],
          "Plateforme données santé FR ; agrégation claims, analytics population et études épidémiologiques.", ["health_data", "claims_analytics", "population_studies", "france"], "enterprise_quote", "enterprise",
          "https://www.openhealth.fr/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("health-data-hub", "Health Data Hub", "https://www.health-data-hub.fr/", ["health-data-analytics"],
          "Infrastructure nationale données santé FR ; accès SNDS, hébergement études et gouvernance.", ["snds", "national_health_data", "research_access", "governance"], "freemium", "enterprise",
          "https://www.health-data-hub.fr/", "official_site", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("inato", "Inato", "https://www.inato.com/", ["health-data-analytics"],
          "Matching essais cliniques FR ; recrutement patients/sites, analytics faisabilité et diversité.", ["clinical_trials", "site_matching", "patient_recruitment", "feasibility"], "hybrid", "mid_market",
          "https://www.inato.com/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="global"),
        v("cegedim-health-data", "Cegedim Health Data", "https://www.cegedim-health-data.com/", ["health-data-analytics"],
          "Real-world data FR ; bases THIN/EPRD, analytics médico-économiques et recherche pharmaceutique.", ["rwd", "medico_economic", "pharma_research", "france"], "enterprise_quote", "enterprise",
          "https://www.cegedim-health-data.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("datavant", "Datavant", "https://www.datavant.com/", ["health-data-analytics"],
          "Tokenisation données santé ; linkage privacy-preserving, RWD et analytics recherche.", ["tokenization", "privacy_preserving", "rwd", "linkage"], "enterprise_quote", "enterprise",
          "https://www.datavant.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("aetion", "Aetion", "https://aetion.com/", ["health-data-analytics"],
          "RWE analytics ; causal inference, études réglementaires et comparateurs effectiveness.", ["rwe", "causal_inference", "regulatory_studies", "effectiveness"], "enterprise_quote", "enterprise",
          "https://aetion.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
    ],
    "legal-contract-ai.json": [
        v("doctrine", "Doctrine", "https://www.doctrine.fr/", ["legal-contract-ai"],
          "Recherche juridique IA FR ; jurisprudence, codes et veille réglementaire pour cabinets/ directions juridiques.", ["legal_research", "jurisprudence", "regulatory_monitoring", "france"], "hybrid", "mid_market",
          "https://www.doctrine.fr/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("ordalie", "Ordalie", "https://www.ordalie.ai/", ["legal-contract-ai"],
          "Assistant juridique IA FR ; analyse contrats, rédaction actes et Q&R droit des affaires.", ["contract_analysis", "legal_drafting", "qa", "corporate_law"], "hybrid", "smb",
          "https://www.ordalie.ai/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("jimini", "Jimini", "https://www.jimini.ai/", ["legal-contract-ai"],
          "Copilot avocats FR ; recherche, synthèse dossiers et génération conclusions/ contrats.", ["legal_copilot", "summarization", "drafting", "france"], "hybrid", "mid_market",
          "https://www.jimini.ai/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("predictice", "Predictice", "https://www.predictice.com/", ["legal-contract-ai"],
          "Analytics jurisprudence FR ; prédiction issues litiges, statistiques tribunaux et stratégie contentieux.", ["litigation_analytics", "outcome_prediction", "court_stats", "france"], "hybrid", "mid_market",
          "https://www.predictice.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("henchman", "Henchman", "https://www.henchman.io/", ["legal-contract-ai"],
          "Knowledge management contrats EU ; recherche clauses, playbooks et réutilisation precedents.", ["clause_search", "playbooks", "precedents", "knowledge_management"], "hybrid", "mid_market",
          "https://www.henchman.io/", "g2", hq="BE", fr="partial", regions=["US", "EU"], geo="europe"),
        v("legalfly", "LegalFly", "https://www.legalfly.com/", ["legal-contract-ai"],
          "Legal workflow AI EU ; revue contrats, due diligence et collaboration legal/business.", ["contract_review", "due_diligence", "workflow", "collaboration"], "hybrid", "mid_market",
          "https://www.legalfly.com/", "crunchbase", hq="BE", fr="partial", regions=["US", "EU"], geo="europe"),
    ],
    "payroll-hris.json": [
        v("silae", "Silae", "https://www.silae.fr/", ["payroll-hris"],
          "Logiciel paie expert-comptable FR ; DSN, bulletins, gestion sociale et multi-conventions.", ["payroll", "dsn", "accountant_portal", "social_management"], "enterprise_quote", "mid_market",
          "https://www.silae.fr/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("combo", "Combo (Snapshift)", "https://www.combo.co/", ["payroll-hris"],
          "Planning RH restauration/retail FR ; paie, pointage, absences et conformité droit du travail.", ["scheduling", "payroll", "time_tracking", "hospitality"], "hybrid", "smb",
          "https://www.combo.co/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("factorial", "Factorial", "https://factorialhr.com/", ["payroll-hris"],
          "HRIS PME EU ; absences, onboarding, paie partenaires et analytics RH.", ["hris", "absences", "onboarding", "hr_analytics"], "hybrid", "smb",
          "https://factorialhr.com/", "g2", hq="ES", fr="partial", regions=["US", "EU"], geo="europe"),
        v("cegid-hr", "Cegid HR & Payroll", "https://www.cegid.com/fr/rh-paie/", ["payroll-hris"],
          "SIRH/paie Cegid FR ; core HR, paie, talent et conformité sociale multi-pays.", ["hris", "payroll", "talent", "social_compliance"], "enterprise_quote", "enterprise",
          "https://www.cegid.com/", "official_site", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("deel", "Deel", "https://www.deel.com/", ["payroll-hris"],
          "Global payroll/EOR ; contrats internationaux, compliance locale et paiements multi-devises.", ["global_payroll", "eor", "compliance", "multi_currency"], "hybrid", "mid_market",
          "https://www.deel.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("sd-worx", "SD Worx", "https://www.sdworx.com/", ["payroll-hris"],
          "Paie et HR services EU ; payroll outsourcing, SIRH et conformité sociale 15+ pays.", ["payroll_outsourcing", "hr_services", "multi_country", "compliance"], "enterprise_quote", "enterprise",
          "https://www.sdworx.com/", "g2", hq="BE", fr="partial", regions=["US", "EU"], geo="europe"),
    ],
    "learning-lxp.json": [
        v("rise-up", "Rise Up", "https://www.riseup.ai/", ["learning-lxp"],
          "LMS/LXP FR ; parcours blended, mobile learning et analytics compétences entreprise.", ["lms", "lxp", "mobile_learning", "skills_analytics"], "hybrid", "mid_market",
          "https://www.riseup.ai/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("didask", "Didask", "https://www.didask.com/", ["learning-lxp"],
          "LXP adaptive learning FR ; microlearning, IA pédagogique et auteur no-code.", ["adaptive_learning", "microlearning", "authoring", "ai_pedagogy"], "hybrid", "mid_market",
          "https://www.didask.com/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("teach-on-mars", "Teach on Mars", "https://www.teachonmars.com/", ["learning-lxp"],
          "Mobile learning enterprise FR ; parcours gamifiés, offline et analytics engagement.", ["mobile_learning", "gamification", "offline", "engagement_analytics"], "enterprise_quote", "mid_market",
          "https://www.teachonmars.com/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("crossknowledge", "CrossKnowledge (Wiley)", "https://www.crossknowledge.com/", ["learning-lxp"],
          "LXP contenus leadership FR ; catalogue soft skills, coaching digital et analytics.", ["leadership", "content_catalog", "coaching", "analytics"], "enterprise_quote", "enterprise",
          "https://www.crossknowledge.com/", "g2", hq="FR", fr="strong", regions=["FR", "EU"], geo="global"),
        v("learnworlds", "LearnWorlds", "https://www.learnworlds.com/", ["learning-lxp"],
          "LMS créateurs/entreprises EU ; cours interactifs, vidéo AI et monétisation formations.", ["course_authoring", "interactive_video", "monetization", "lms"], "hybrid", "smb",
          "https://www.learnworlds.com/", "g2", hq="CY", fr="partial", regions=["US", "EU"], geo="europe"),
        v("talentlms", "TalentLMS", "https://www.talentlms.com/", ["learning-lxp"],
          "LMS cloud PME ; SCORM, mobile et reporting simple pour formation continue.", ["lms", "scorm", "mobile", "reporting"], "hybrid", "smb",
          "https://www.talentlms.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
    ],
    "treasury-fpa.json": [
        v("kyriba", "Kyriba", "https://www.kyriba.com/", ["treasury-fpa"],
          "TMS cloud ; trésorerie, cash forecasting, FX/risk et connectivité bancaire multi-pays.", ["tms", "cash_forecasting", "fx_risk", "bank_connectivity"], "enterprise_quote", "enterprise",
          "https://www.kyriba.com/", "g2", hq="FR", fr="strong", regions=["FR", "EU"], geo="global"),
        v("gtreasury", "GTreasury", "https://www.gtreasury.com/", ["treasury-fpa"],
          "Treasury management ; cash, debt, in-house banking et reporting trésorerie.", ["treasury", "cash_management", "in_house_banking", "reporting"], "enterprise_quote", "enterprise",
          "https://www.gtreasury.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("cashforce", "Cashforce", "https://www.cashforce.com/", ["treasury-fpa"],
          "Cash forecasting EU ; ML prévisions flux, rapprochement et dashboards trésorerie.", ["cash_forecasting", "ml", "reconciliation", "dashboards"], "hybrid", "mid_market",
          "https://www.cashforce.com/", "g2", hq="BE", fr="partial", regions=["US", "EU"], geo="europe"),
        v("trovata", "Trovata", "https://trovata.io/", ["treasury-fpa"],
          "Cash management API ; agrégation comptes bancaires, tags flux et analytics trésorerie.", ["bank_aggregation", "cash_tags", "api", "analytics"], "hybrid", "mid_market",
          "https://trovata.io/", "crunchbase", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("highradius", "HighRadius", "https://www.highradius.com/", ["treasury-fpa"],
          "Autonomous finance ; O2C, trésorerie, cash application IA et collections.", ["order_to_cash", "treasury", "cash_application", "collections"], "enterprise_quote", "enterprise",
          "https://www.highradius.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
        v("blackline", "BlackLine", "https://www.blackline.com/", ["treasury-fpa"],
          "Financial close & accounting ; réconciliations, contrôles et reporting consolidé.", ["reconciliation", "financial_close", "controls", "consolidation"], "enterprise_quote", "enterprise",
          "https://www.blackline.com/", "g2", hq="US", fr="partial", regions=["US", "EU"], geo="global"),
    ],
    "finance-accounting-ai.json": [
        v("agicap", "Agicap", "https://agicap.com/", ["finance-accounting-ai"],
          "Trésorerie PME FR ; cashflow forecasting, scenarios et connexion bancaire/compta.", ["cashflow", "forecasting", "scenarios", "bank_sync"], "hybrid", "smb",
          "https://agicap.com/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("qonto", "Qonto", "https://qonto.com/", ["finance-accounting-ai"],
          "Néobanque pro FR ; comptes, cartes, facturation et automatisation comptable PME.", ["business_banking", "invoicing", "accounting_automation", "cards"], "hybrid", "smb",
          "https://qonto.com/", "crunchbase", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("indigo", "Indigo (ex-Georges)", "https://www.indigo.fr/", ["finance-accounting-ai"],
          "Compta auto-entrepreneurs/PME FR ; TVA, liasse fiscale et assistant IA fiscal.", ["accounting", "vat", "tax_filing", "ai_assist"], "hybrid", "smb",
          "https://www.indigo.fr/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("sage", "Sage", "https://www.sage.com/fr-fr/", ["finance-accounting-ai"],
          "ERP/compta PME FR ; facturation, immobilisations, paie adjacente et reporting fiscal.", ["accounting", "erp", "invoicing", "tax_reporting"], "hybrid", "smb",
          "https://www.sage.com/fr-fr/", "g2", hq="GB", fr="strong", regions=["US", "EU"], geo="france"),
        v("indy", "Indy", "https://www.indy.fr/", ["finance-accounting-ai"],
          "Comptabilité online FR ; OCR factures, TVA, liasse et télétransmission expert-comptable.", ["ocr_invoices", "vat", "tax_filing", "accountant_portal"], "hybrid", "smb",
          "https://www.indy.fr/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
        v("fulll", "Fulll", "https://www.fulll.io/", ["finance-accounting-ai", "payroll-hris"],
          "Suite cabinets/experts-comptables FR ; production comptable, paie Silae et portail clients.", ["accounting_production", "payroll", "client_portal", "france"], "hybrid", "mid_market",
          "https://www.fulll.io/", "geo_digest", hq="FR", fr="strong", regions=["FR", "EU"], geo="france"),
    ],
}

SEGMENT_PATCHES: dict[str, list[str]] = {
    "lucca": ["payroll-hris"],
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "regulatory-reporting-eu": {
        "g2": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 4, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 1, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
    },
    "accessibility-compliance": {
        "g2": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 3, "pass": PASS_ID},
        "open_source": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "esg-csrd": {
        "g2": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 3, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
    },
    "pharma-regulatory": {
        "g2": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 4, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "privacy-consent": {
        "g2": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 3, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 2, "pass": PASS_ID},
        "open_source": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "insurance-insurtech": {
        "g2": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 2, "pass": PASS_ID},
    },
    "construction-proptech": {
        "g2": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 2, "pass": PASS_ID},
    },
    "supply-chain-logistics": {
        "g2": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 3, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "retail-ecommerce-ai": {
        "g2": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 2, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 2, "pass": PASS_ID},
    },
    "energy-cleantech": {
        "g2": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 2, "pass": PASS_ID},
    },
    "healthcare-clinical-ai": {
        "g2": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 3, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
    },
    "health-data-analytics": {
        "g2": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 3, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "legal-contract-ai": {
        "g2": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 3, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "payroll-hris": {
        "g2": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 3, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "learning-lxp": {
        "g2": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 3, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "treasury-fpa": {
        "g2": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 4, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "finance-accounting-ai": {
        "g2": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 3, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
    },
}


def merge() -> None:
    all_ids: set[str] = set()
    for path in VENDORS_DIR.glob("*.json"):
        for vendor in json.loads(path.read_text(encoding="utf-8")).get("vendors", []):
            all_ids.add(vendor["id"])

    total = 0
    per_file: dict[str, int] = {}
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
        data["updated_at"] = TODAY
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        per_file[fname] = count
        print(f"updated {fname}: +{count}")

    patched = 0
    for vpath in sorted(VENDORS_DIR.glob("*.json")):
        vdata = json.loads(vpath.read_text(encoding="utf-8"))
        changed = False
        for vendor in vdata.get("vendors", []):
            for seg in SEGMENT_PATCHES.get(vendor["id"], []):
                if seg not in vendor["segments"]:
                    vendor["segments"].append(seg)
                    changed = True
                    patched += 1
        if changed:
            vdata["updated_at"] = TODAY
            vpath.write_text(json.dumps(vdata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"patched {vpath.name}")

    matrix = json.loads(COVERAGE.read_text(encoding="utf-8"))
    for seg_id, sources in COVERAGE_UPDATES.items():
        entry = matrix["segments"][seg_id]
        for src, upd in sources.items():
            prev = entry["sources"].get(src) or {}
            entry["sources"][src] = {
                **upd,
                "cumulative_new": prev.get("cumulative_new", prev.get("new_added", 0)) + upd["new_added"],
            }
        entry["last_pass"] = PASS_ID
        entry["vendor_count_after_pass"] = len(
            json.loads((VENDORS_DIR / f"{seg_id}.json").read_text(encoding="utf-8"))["vendors"]
        )
    matrix["updated_at"] = TODAY
    COVERAGE.write_text(json.dumps(matrix, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"done: +{total} vendors, {patched} segment patches")
    for fname, n in per_file.items():
        print(f"  {fname}: +{n}")


if __name__ == "__main__":
    merge()
