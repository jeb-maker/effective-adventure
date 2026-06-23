#!/usr/bin/env python3
"""Vague 5r — L3 cartographie segments France open data thématique (9→~18)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v5r-france-thematic-l3"


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
    hq: str = "FR",
    fr: str = "strong",
    regions: list[str] | None = None,
    geo: str = "france",
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
        "operating_regions": regions or ["FR", "EU"],
        "discovery_source": src_type,
        "discovery_pass": PASS_ID,
        "source_url": source,
        "source_consulted_at": TODAY,
        "verification_status": "partial",
    }
    if notes:
        d["notes"] = notes
    return d


ADDITIONS: dict[str, list[dict]] = {
    "electoral-data-fr.json": [
        v(
            "ballotage-datagere",
            "Ballotage (Datagère)",
            "https://www.datagere.com/",
            ["electoral-data-fr"],
            "App analytics électoraux FR ; harmonisation BV 2002–2024, basculements et exports multi-scrutins.",
            ["bureau_vote", "harmonisation", "basculements", "exports"],
            "hybrid",
            "mid_market",
            "https://www.datagere.com/",
            "geo_digest",
            notes="Concurrent cité idée 0014.",
        ),
        v(
            "qomon",
            "Qomon",
            "https://fr.qomon.com/",
            ["electoral-data-fr"],
            "CRM campagne + carto BV×INSEE ; force électorale, évolution territoriale et exports PDF.",
            ["bv_insee", "electoral_maps", "campaign_crm", "territory"],
            "hybrid",
            "mid_market",
            "https://fr.qomon.com/",
            "geo_digest",
        ),
        v(
            "politicae",
            "Politiciae DATA",
            "https://politicae.fr/",
            ["electoral-data-fr"],
            "Cartographie électorale commune/IRIS/BV ; analytics territoriaux pour campagnes et médias.",
            ["commune", "iris", "bureau_vote", "cartography"],
            "hybrid",
            "smb",
            "https://politicae.fr/",
            "geo_digest",
            notes="Concurrent cité idée 0014.",
        ),
        v(
            "explain-lmp",
            "Explain (ex-Liegey-Muller-Pons)",
            "https://www.explain.fr/",
            ["electoral-data-fr"],
            "Scoring électoral campagnes ; agrégation BV×INSEE et ciblage terrain pour candidats.",
            ["electoral_scoring", "bv_insee", "campaign", "targeting"],
            "enterprise_quote",
            "mid_market",
            "https://www.explain.fr/",
            "geo_digest",
        ),
        v(
            "digitalebox",
            "DigitaleBox",
            "https://digitalebox.com/",
            ["electoral-data-fr"],
            "CRM politique français ; cartographie électeurs par secteur et mobilisation campagne.",
            ["political_crm", "elector_mapping", "mobilization", "campaign"],
            "hybrid",
            "smb",
            "https://digitalebox.com/",
            "geo_digest",
        ),
        v(
            "terre-de-donnees",
            "Terre de Données",
            "https://www.terre-de-donnees.fr/",
            ["electoral-data-fr"],
            "Data journalism électoral ; jeux harmonisés, cartes interactives et analyses territoriales.",
            ["election_data", "data_journalism", "maps", "open_data"],
            "freemium",
            "mid_market",
            "https://www.terre-de-donnees.fr/",
            "official_site",
        ),
        v(
            "politic-data",
            "Politic Data",
            "https://www.politicdata.io/",
            ["electoral-data-fr"],
            "Plateforme analytics électoraux ; historique scrutins, comparaisons territoriales et API.",
            ["election_analytics", "historical", "api", "territory"],
            "hybrid",
            "mid_market",
            "https://www.politicdata.io/",
            "geo_digest",
            notes="Concurrent cité idée 0014.",
        ),
        v(
            "elections-agregees-etalab",
            "Données élections agrégées (Etalab)",
            "https://www.data.gouv.fr/datasets/donnees-des-elections-agregees",
            ["electoral-data-fr"],
            "Jeu national BV harmonisé ; résultats candidats, général et tables de jointure IRIS/BV.",
            ["aggregated_results", "bureau_vote", "open_data", "etalab"],
            "freemium",
            "mid_market",
            "https://www.data.gouv.fr/datasets/donnees-des-elections-agregees",
            "official_site",
            notes="Source citée idée 0014.",
        ),
        v(
            "interieur-resultats-elections",
            "Ministère de l'Intérieur — résultats électoraux",
            "https://www.interieur.gouv.fr/Elections/Les-resultats",
            ["electoral-data-fr"],
            "Publication officielle résultats ; législatives, municipales, présidentielles par commune/BV.",
            ["official_results", "elections", "commune", "open_data"],
            "freemium",
            "mid_market",
            "https://www.interieur.gouv.fr/Elections/Les-resultats",
            "official_site",
        ),
    ],
    "open-data-governance-fr.json": [
        v(
            "huwise",
            "Huwise (ex-Opendatasoft)",
            "https://www.huwise.com/",
            ["open-data-governance-fr"],
            "Plateforme open data B2G ; portails collectivités, data marketplace et gouvernance jeux.",
            ["data_portal", "marketplace", "governance", "api"],
            "enterprise_quote",
            "mid_market",
            "https://www.huwise.com/",
            "official_site",
            notes="Rebrand Opendatasoft — complète entrée opendatasoft.",
        ),
        v(
            "validata",
            "Validata",
            "https://validata.fr/",
            ["open-data-governance-fr"],
            "Validation open data vs schémas nationaux ; API Table Schema et contrôle qualité fichiers.",
            ["schema_validation", "table_schema", "api", "quality"],
            "open_source",
            "mid_market",
            "https://validata.fr/",
            "open_source",
            notes="Concurrent cité idées 0002/0023.",
        ),
        v(
            "opendatafrance",
            "OpenDataFrance — Observatoire",
            "https://opendatafrance.fr/presentation-de-lobservatoire/",
            ["open-data-governance-fr"],
            "Observatoire open data territoires ; conformité publication, profils collectivités et base Grist.",
            ["observatory", "compliance", "collectivites", "grist"],
            "freemium",
            "mid_market",
            "https://opendatafrance.fr/presentation-de-lobservatoire/",
            "official_site",
            notes="Concurrent cité idée 0023.",
        ),
        v(
            "datactivist",
            "Datactivist",
            "https://datactivist.coop/",
            ["open-data-governance-fr"],
            "Coopérative accompagnement open data ; audits, formations et déploiement portails collectivités.",
            ["advisory", "training", "open_data", "collectivites"],
            "enterprise_quote",
            "mid_market",
            "https://datactivist.coop/",
            "geo_digest",
        ),
        v(
            "data-publica",
            "Data Publica",
            "https://www.data-publica.com/",
            ["open-data-governance-fr"],
            "Baromètre et analytics open data collectivités ; benchmarking pratiques et IA générative.",
            ["barometer", "benchmark", "collectivites", "analytics"],
            "enterprise_quote",
            "mid_market",
            "https://www.data-publica.com/",
            "geo_digest",
            notes="Concurrent cité idée 0023.",
        ),
        v(
            "numerique360",
            "Numérique360 (Banque des Territoires)",
            "https://numerique360.fr/",
            ["open-data-governance-fr"],
            "Observatoire numérique collectivités ; maturité SI, open data et comparaisons territoriales.",
            ["digital_maturity", "observatory", "collectivites", "benchmark"],
            "freemium",
            "mid_market",
            "https://numerique360.fr/",
            "official_site",
        ),
        v(
            "dkod",
            "DKOD",
            "https://www.dkod.fr/",
            ["open-data-governance-fr"],
            "Intégrateur open data FR ; déploiement portails CKAN/Opendatasoft et gouvernance données.",
            ["integration", "data_portal", "ckan", "governance"],
            "enterprise_quote",
            "mid_market",
            "https://www.dkod.fr/",
            "geo_digest",
        ),
        v(
            "schema-data-gouv",
            "schema.data.gouv.fr (Etalab)",
            "https://schema.data.gouv.fr/",
            ["open-data-governance-fr"],
            "Référentiel schémas nationaux ; SCDL, Table Schema et conformité jeux prioritaires.",
            ["national_schemas", "scdl", "table_schema", "etalab"],
            "freemium",
            "mid_market",
            "https://schema.data.gouv.fr/",
            "official_site",
            notes="Source citée idées 0023/0027.",
        ),
        v(
            "dataclic",
            "DataClic (OpenDataFactory)",
            "https://dataclic.fr/",
            ["open-data-governance-fr"],
            "Plateforme publication jeux SCDL ; workflow dépôt, validation schéma et moissonnage data.gouv.fr.",
            ["scdl", "publishing", "schema_validation", "harvesting"],
            "hybrid",
            "mid_market",
            "https://dataclic.fr/",
            "geo_digest",
            notes="Concurrent cité idée 0023.",
        ),
    ],
    "public-health-territory-fr.json": [
        v(
            "cartosante",
            "CartoSanté (Atlas Santé)",
            "https://cartosante.atlasante.fr/",
            ["public-health-territory-fr"],
            "Cartographie santé territoriale ; offre de soins, démographie médicale et indicateurs ARS.",
            ["health_mapping", "medical_demography", "territory", "open_data"],
            "freemium",
            "mid_market",
            "https://cartosante.atlasante.fr/",
            "official_site",
            notes="Source citée idée 0012.",
        ),
        v(
            "annuaire-sante",
            "Annuaire Santé (ANS)",
            "https://annuaire.sante.fr/",
            ["public-health-territory-fr"],
            "Répertoire professionnels de santé ; géolocalisation PS, spécialités et libre accès par territoire.",
            ["health_directory", "rpps", "geolocation", "api"],
            "freemium",
            "mid_market",
            "https://annuaire.sante.fr/",
            "official_site",
            notes="Source citée idée 0012.",
        ),
        v(
            "maiia",
            "Maiia",
            "https://www.maiia.com/",
            ["public-health-territory-fr"],
            "Prise de RDV santé ; disponibilité praticiens par commune et signaux déserts médicaux.",
            ["appointment_booking", "availability", "territory", "telehealth"],
            "freemium",
            "self_serve",
            "https://www.maiia.com/",
            "geo_digest",
        ),
        v(
            "ordoclic",
            "Ordoclic",
            "https://www.ordoclic.fr/",
            ["public-health-territory-fr"],
            "E-prescription et parcours santé ; données indirectes activité médicale territoriale.",
            ["e_prescription", "health_workflow", "territory_signals", "france"],
            "hybrid",
            "mid_market",
            "https://www.ordoclic.fr/",
            "geo_digest",
            hq="FR",
        ),
        v(
            "geodes-spf",
            "Géodes (Santé publique France)",
            "https://geodes.santepubliquefrance.fr/",
            ["public-health-territory-fr"],
            "Portail visualisation données santé publique ; cartes, indicateurs épidémiologie et exports.",
            ["epidemiology", "visualization", "indicators", "open_data"],
            "freemium",
            "mid_market",
            "https://geodes.santepubliquefrance.fr/",
            "official_site",
        ),
        v(
            "rezone-cpts",
            "Rézone CPTS",
            "https://www.paps.sante.fr/rezone-cpts",
            ["public-health-territory-fr"],
            "Diagnostic territorial CPTS ; cartographie offre de soins et aide à l'implantation libérale.",
            ["cpts", "territorial_diagnosis", "care_access", "mapping"],
            "freemium",
            "mid_market",
            "https://www.paps.sante.fr/rezone-cpts",
            "official_site",
            notes="Source citée idée 0012.",
        ),
        v(
            "crtosante-ars",
            "CRTOsanté (ARS)",
            "https://www.ars.sante.fr/crtosante-ou-sinstaller-en-liberal-en-un-clic",
            ["public-health-territory-fr"],
            "Outil ARS implantation libérale ; zonages, aides et cartographie tension médicale.",
            ["medical_zoning", "installation", "ars", "territory"],
            "freemium",
            "mid_market",
            "https://www.ars.sante.fr/crtosante-ou-sinstaller-en-liberal-en-un-clic",
            "official_site",
            notes="Source citée idée 0012.",
        ),
        v(
            "mon-espace-sante",
            "Mon Espace Santé (ANS)",
            "https://monservicesante.fr/",
            ["public-health-territory-fr"],
            "Dossier médical partagé national ; parcours patient et données agrégées santé numérique.",
            ["dmp", "patient_portal", "health_records", "public_service"],
            "freemium",
            "self_serve",
            "https://monservicesante.fr/",
            "official_site",
        ),
        v(
            "healthcare-gouv",
            "HealthData.gouv.fr",
            "https://healthdata.gouv.fr/",
            ["public-health-territory-fr"],
            "Portail open data santé ; jeux ARS, hôpitaux, médicaments et APIs territoriales.",
            ["health_open_data", "catalog", "api", "territory"],
            "freemium",
            "mid_market",
            "https://healthdata.gouv.fr/",
            "official_site",
        ),
    ],
    "transport-mobility-data-fr.json": [
        v(
            "navitia",
            "Navitia (Hove Group)",
            "https://navitia.io/",
            ["transport-mobility-data-fr"],
            "API mobilité multimodale ; routing GTFS, isochrones et agrégation flux transport FR/EU.",
            ["gtfs", "routing", "isochrones", "api"],
            "hybrid",
            "mid_market",
            "https://navitia.io/",
            "geo_digest",
            notes="Concurrent cité idée 0015.",
        ),
        v(
            "geovelo",
            "Geovelo",
            "https://www.geovelo.fr/",
            ["transport-mobility-data-fr"],
            "App et API vélo ; itinéraires cyclables, comptages et données mobilité douce collectivités.",
            ["cycling", "routing", "api", "collectivites"],
            "hybrid",
            "mid_market",
            "https://www.geovelo.fr/",
            "geo_digest",
        ),
        v(
            "karos",
            "Karos",
            "https://www.karos.fr/",
            ["transport-mobility-data-fr"],
            "Covoiturage court trajet ; données flux domicile-travail et complémentarité transport public.",
            ["carpooling", "commute", "territory", "mobility"],
            "freemium",
            "mid_market",
            "https://www.karos.fr/",
            "geo_digest",
        ),
        v(
            "blablacar-daily",
            "BlaBlaCar Daily",
            "https://www.blablacar.fr/",
            ["transport-mobility-data-fr"],
            "Covoiturage quotidien ; signaux mobilité pendulaire et complémentarité réseaux TP.",
            ["carpooling", "daily_commute", "territory", "france"],
            "freemium",
            "self_serve",
            "https://www.blablacar.fr/",
            "geo_digest",
        ),
        v(
            "sncf-open-data",
            "SNCF Open Data",
            "https://ressources.data.sncf.com/",
            ["transport-mobility-data-fr"],
            "Portail open data SNCF ; horaires, gares, fréquentation et GTFS national ferroviaire.",
            ["rail", "gtfs", "open_data", "national"],
            "freemium",
            "mid_market",
            "https://ressources.data.sncf.com/",
            "official_site",
        ),
        v(
            "cerema-capamob",
            "Cerema — Capamob / Networks",
            "https://capamob.cerema.fr/",
            ["transport-mobility-data-fr"],
            "Méthodes et outils accessibilité multimodale ; extension QGIS GTFS Musliw pour collectivités.",
            ["accessibility", "gtfs", "qgis", "isochrones"],
            "freemium",
            "mid_market",
            "https://capamob.cerema.fr/",
            "official_site",
            notes="Concurrent cité idée 0015.",
        ),
        v(
            "ratp-open-data",
            "RATP — Open Data",
            "https://data.ratp.fr/",
            ["transport-mobility-data-fr"],
            "Données open transport RATP ; fréquentation, lignes, accessibilité et APIs Paris/IDF.",
            ["transit", "open_data", "paris", "api"],
            "freemium",
            "mid_market",
            "https://data.ratp.fr/",
            "official_site",
        ),
        v(
            "fluctuo",
            "Fluctuo",
            "https://www.fluctuo.com/",
            ["transport-mobility-data-fr"],
            "Analytics micromobilité ; données free-floating, trottinettes et vélos partagés par ville.",
            ["micromobility", "shared_mobility", "analytics", "gbfs"],
            "enterprise_quote",
            "mid_market",
            "https://www.fluctuo.com/",
            "geo_digest",
            hq="FR",
        ),
        v(
            "mappy",
            "Mappy",
            "https://www.mappy.com/",
            ["transport-mobility-data-fr"],
            "Cartographie et routing FR ; itinéraires multimodaux, trafic et APIs mobilité.",
            ["routing", "multimodal", "traffic", "maps_api"],
            "freemium",
            "self_serve",
            "https://www.mappy.com/",
            "geo_digest",
        ),
    ],
    "civic-tech-fr.json": [
        v(
            "civiliz",
            "Civiliz",
            "https://www.civiliz.io/",
            ["civic-tech-fr"],
            "Plateforme participation citoyenne FR ; consultations, budgets participatifs et engagement.",
            ["participation", "consultations", "participatory_budget", "france"],
            "enterprise_quote",
            "mid_market",
            "https://www.civiliz.io/",
            "geo_digest",
        ),
        v(
            "neocity",
            "Neocity",
            "https://www.neocity.fr/",
            ["civic-tech-fr"],
            "Plateforme smart city française ; concertation, services citoyens et pilotage territorial.",
            ["smart_city", "consultation", "citizen_services", "france"],
            "enterprise_quote",
            "mid_market",
            "https://www.neocity.fr/",
            "geo_digest",
        ),
        v(
            "demarches-simplifiees",
            "Démarches simplifiées",
            "https://www.demarches-simplifiees.fr/",
            ["civic-tech-fr"],
            "Téléservice public ; formulaires administratifs, workflows et open source pour collectivités.",
            ["digital_forms", "workflow", "public_service", "open_source"],
            "freemium",
            "mid_market",
            "https://www.demarches-simplifiees.fr/",
            "official_site",
            notes="Concurrent cité idée 0018.",
        ),
        v(
            "consultations-publiques",
            "Consultations publiques (MTE)",
            "https://consultations-publiques.developpement-durable.gouv.fr/",
            ["civic-tech-fr"],
            "Portail national concertation environnementale ; enquêtes publiques et participation citoyenne.",
            ["public_consultation", "environment", "participation", "open_data"],
            "freemium",
            "mid_market",
            "https://consultations-publiques.developpement-durable.gouv.fr/",
            "official_site",
        ),
        v(
            "voxe",
            "Voxe.org",
            "https://www.voxe.org/",
            ["civic-tech-fr"],
            "Association civic tech ; comparateurs électoraux, pédagogie citoyenne et open data politique.",
            ["civic_education", "elections", "open_data", "nonprofit"],
            "freemium",
            "self_serve",
            "https://www.voxe.org/",
            "geo_digest",
            notes="Adjacent idée 0018.",
        ),
        v(
            "wegov",
            "WeGov",
            "https://www.wegov.fr/",
            ["civic-tech-fr"],
            "Plateforme engagement citoyen FR ; sondages, concertation et analytics participation.",
            ["engagement", "surveys", "consultation", "analytics"],
            "enterprise_quote",
            "mid_market",
            "https://www.wegov.fr/",
            "geo_digest",
        ),
        v(
            "place-decidim",
            "Place (Decidim FR)",
            "https://place.dev/",
            ["civic-tech-fr"],
            "Hébergement Decidim France ; budgets participatifs, consultations et modules civic tech.",
            ["decidim", "hosting", "participatory_budget", "france"],
            "enterprise_quote",
            "mid_market",
            "https://place.dev/",
            "geo_digest",
        ),
        v(
            "jalios-jplatform",
            "Jalios JPlatform",
            "https://www.jalios.com/",
            ["civic-tech-fr", "open-data-governance-fr"],
            "Portail intranet/extranet collectivités ; espaces citoyens, open data et gouvernance contenu.",
            ["portal", "citizen_space", "intranet", "governance"],
            "enterprise_quote",
            "enterprise",
            "https://www.jalios.com/",
            "g2",
        ),
    ],
    "geospatial-gis-fr.json": [
        v(
            "geoclip",
            "GEOCLIP",
            "https://www.geoclip.com/",
            ["geospatial-gis-fr"],
            "Suite SIG française ; cartographie, géocodage et portails géographiques collectivités.",
            ["sig", "geocoding", "mapping", "collectivites"],
            "enterprise_quote",
            "mid_market",
            "https://www.geoclip.com/",
            "geo_digest",
            notes="Concurrent cité idées 0011/0026.",
        ),
        v(
            "qgis",
            "QGIS",
            "https://qgis.org/",
            ["geospatial-gis-fr"],
            "SIG open source ; analyse spatiale, plugins et écosystème très déployé secteur public FR.",
            ["open_source", "gis", "spatial_analysis", "plugins"],
            "open_source",
            "mid_market",
            "https://qgis.org/",
            "open_source",
            fr="strong",
            geo="global",
            hq="unknown",
            regions=["global"],
        ),
        v(
            "ban-adresse",
            "Base Adresse Nationale",
            "https://adresse.data.gouv.fr/",
            ["geospatial-gis-fr"],
            "Référentiel adresses France ; géocodage, API BAN et intégration parcelles cadastre.",
            ["geocoding", "addresses", "api", "open_data"],
            "freemium",
            "mid_market",
            "https://adresse.data.gouv.fr/",
            "official_site",
            notes="Source citée idée 0011.",
        ),
        v(
            "theia-cnes",
            "THEIA (CNES/IGN)",
            "https://www.theia-land.fr/",
            ["geospatial-gis-fr"],
            "Images satellitaires et produits dérivés ; occupation sol, agriculture et observation Terre FR.",
            ["satellite", "land_cover", "agriculture", "earth_observation"],
            "freemium",
            "mid_market",
            "https://www.theia-land.fr/",
            "official_site",
        ),
        v(
            "api-carto-ign",
            "API Carto (IGN)",
            "https://apicarto.ign.fr/",
            ["geospatial-gis-fr"],
            "API géographiques officielles ; cadastre, GPU, altimétrie et services WFS/WMS IGN.",
            ["api", "cadastre", "gpu", "wfs"],
            "freemium",
            "mid_market",
            "https://apicarto.ign.fr/",
            "official_site",
            notes="Source citée idées 0011/0026.",
        ),
    ],
    "environmental-data-fr.json": [
        v(
            "recosante",
            "Recosanté",
            "https://recosante.beta.gouv.fr/",
            ["environmental-data-fr", "public-health-territory-fr"],
            "Service public numérique ; recommandations air, pollens, UV, baignade et radon par commune.",
            ["air_quality", "pollen", "uv", "radon", "health"],
            "freemium",
            "self_serve",
            "https://recosante.beta.gouv.fr/",
            "official_site",
            notes="Concurrent cité idée 0005.",
        ),
        v(
            "icpe-georisques",
            "ICPE — Géorisques",
            "https://www.georisques.gouv.fr/donnees/icpe",
            ["environmental-data-fr"],
            "Installations classées ; établissements Seveso, rejets et proximité parcelles via API.",
            ["icpe", "seveso", "industrial", "parcel_proximity"],
            "freemium",
            "mid_market",
            "https://www.georisques.gouv.fr/donnees/icpe",
            "official_site",
            notes="Source citée idée 0011.",
        ),
        v(
            "mon-eau-com",
            "mon-eau.com",
            "https://www.mon-eau.com/",
            ["environmental-data-fr"],
            "Qualité eau potable par commune ; score /100, analyses et API publique jeux ouverts.",
            ["drinking_water", "quality_score", "commune", "api"],
            "freemium",
            "self_serve",
            "https://www.mon-eau.com/",
            "geo_digest",
            notes="Concurrent cité idée 0005.",
        ),
        v(
            "risqeo",
            "Risqeo",
            "https://www.risqeo.com/",
            ["environmental-data-fr", "geospatial-gis-fr"],
            "Rapports risques adresse/parcelle ; synthèse Géorisques pour pros immobilier et notaires.",
            ["risk_report", "georisques", "parcel", "real_estate"],
            "hybrid",
            "smb",
            "https://www.risqeo.com/",
            "geo_digest",
            notes="Concurrent cité idée 0011.",
        ),
    ],
}

SEGMENT_PATCHES: dict[str, list[str]] = {
    "health-data-hub": ["public-health-territory-fr"],
    "openhealth": ["public-health-territory-fr"],
    "medadom": ["public-health-territory-fr"],
    "qare": ["public-health-territory-fr"],
    "cegedim-health-data": ["public-health-territory-fr"],
    "ademe-data": ["environmental-data-fr"],
    "georisques": ["environmental-data-fr", "geospatial-gis-fr"],
    "datagouv": ["open-data-governance-fr"],
    "registre-perma": ["civic-tech-fr"],
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "electoral-data-fr": {
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 18, "new_added": 6, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 3, "pass": PASS_ID},
        "g2": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 0, "pass": PASS_ID},
    },
    "open-data-governance-fr": {
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 16, "new_added": 4, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 4, "pass": PASS_ID},
        "open_source": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
        "g2": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "public-health-territory-fr": {
        "official_site": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 6, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 3, "pass": PASS_ID},
        "g2": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 0, "pass": PASS_ID},
    },
    "transport-mobility-data-fr": {
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 16, "new_added": 6, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 3, "pass": PASS_ID},
        "open_source": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 0, "pass": PASS_ID},
    },
    "civic-tech-fr": {
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 5, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "g2": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "geospatial-gis-fr": {
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 2, "pass": PASS_ID},
        "open_source": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
    "environmental-data-fr": {
        "official_site": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 2, "pass": PASS_ID},
    },
}

TARGET_LEVELS = {
    "electoral-data-fr": "L3",
    "open-data-governance-fr": "L3",
    "public-health-territory-fr": "L3",
    "transport-mobility-data-fr": "L3",
    "civic-tech-fr": "L3",
    "geospatial-gis-fr": "L3",
    "environmental-data-fr": "L3",
}


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

    patched = patch_segments()
    if patched:
        print(f"segment patches: +{patched}")

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
        entry["target_level"] = TARGET_LEVELS.get(seg_id, entry.get("target_level", "L2"))
        entry["vendor_count_after_pass"] = len(
            json.loads((VENDORS_DIR / f"{seg_id}.json").read_text(encoding="utf-8"))["vendors"]
        )
    matrix["updated_at"] = TODAY
    COVERAGE.write_text(json.dumps(matrix, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"done: +{total} vendors")
    for fname, n in per_file.items():
        print(f"  {fname}: +{n}")


if __name__ == "__main__":
    merge()
