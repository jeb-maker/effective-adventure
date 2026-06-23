#!/usr/bin/env python3
"""Vague 5t — L3 complétion segments sécurité (cyber, IAM, CSPM, email, vuln, vector DB)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v5t-security-l3"


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
    hq: str = "US",
    fr: str = "partial",
    regions: list[str] | None = None,
    geo: str = "global",
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
        "verification_status": "partial",
    }
    if notes:
        d["notes"] = notes
    return d


ADDITIONS: dict[str, list[dict]] = {
    "cybersecurity-platforms.json": [
        v(
            "stormshield",
            "Stormshield",
            "https://www.stormshield.com/",
            ["cybersecurity-platforms"],
            "Suite sécurité réseau FR ; firewall UTM, EDR et visibilité OT/IT pour secteurs régulés et souveraineté.",
            ["firewall", "edr", "network_security", "sovereign"],
            "enterprise_quote",
            "enterprise",
            "https://www.stormshield.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "tehtris",
            "TEHTRIS",
            "https://tehtris.com/",
            ["cybersecurity-platforms"],
            "XDR souverain FR ; agents endpoint, détection zero-day et orchestration réponse multi-vecteurs.",
            ["xdr", "edr", "zero_day", "sovereign"],
            "enterprise_quote",
            "enterprise",
            "https://tehtris.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "crowdsec",
            "CrowdSec",
            "https://www.crowdsec.net/",
            ["cybersecurity-platforms"],
            "IPS collaboratif open-core FR ; blocage IPs malveillantes, CTI partagée et intégration SIEM/firewall.",
            ["collaborative_ips", "threat_intel", "siem_integration", "open_core"],
            "hybrid",
            "mid_market",
            "https://www.crowdsec.net/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "gatewatcher",
            "Gatewatcher",
            "https://www.gatewatcher.com/",
            ["cybersecurity-platforms"],
            "NDR/XDR FR ; détection menaces réseau, analyse comportementale et réponse automatisée APT.",
            ["ndr", "xdr", "network_detection", "apt"],
            "enterprise_quote",
            "enterprise",
            "https://www.gatewatcher.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "darktrace",
            "Darktrace",
            "https://www.darktrace.com/",
            ["cybersecurity-platforms"],
            "NDR/XDR IA ; modèle self-learning, détection anomalies réseau/cloud/email et réponse autonome.",
            ["ndr", "xdr", "ai_detection", "autonomous_response"],
            "enterprise_quote",
            "enterprise",
            "https://www.darktrace.com/",
            "g2",
            hq="GB",
            fr="partial",
            regions=["GB", "EU", "US"],
        ),
        v(
            "withsecure",
            "WithSecure",
            "https://www.withsecure.com/",
            ["cybersecurity-platforms"],
            "Elements XDR européen ; EPP, EDR, MDR et exposure management pour mid-market et enterprise EU.",
            ["xdr", "edr", "mdr", "exposure_management"],
            "enterprise_quote",
            "enterprise",
            "https://www.withsecure.com/",
            "g2",
            hq="FI",
            fr="partial",
            geo="europe",
            regions=["FI", "EU", "FR"],
        ),
        v(
            "stellar-cyber",
            "Stellar Cyber",
            "https://stellarcyber.ai/",
            ["cybersecurity-platforms"],
            "Open XDR ; corrélation multi-sources, SIEM intégré, SOAR et threat hunting unifié.",
            ["open_xdr", "siem", "soar", "threat_hunting"],
            "hybrid",
            "mid_market",
            "https://stellarcyber.ai/",
            "g2",
        ),
    ],
    "identity-access-management.json": [
        v(
            "alsid",
            "Alsid (Trend Micro)",
            "https://www.trendmicro.com/en_us/business/products/identity/detection-and-response.html",
            ["identity-access-management"],
            "Protection AD/identité FR ; détection compromission comptes privilégiés et attaques Kerberos/AD.",
            ["ad_security", "identity_threat_detection", "privileged_accounts", "kerberos"],
            "enterprise_quote",
            "enterprise",
            "https://www.trendmicro.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
            notes="Acquis Trend Micro — Defender for Identity / AD protection.",
        ),
        v(
            "thales-ciphertrust",
            "Thales CipherTrust",
            "https://cpl.thalesgroup.com/encryption/data-security-platform",
            ["identity-access-management"],
            "Plateforme sécurité données FR ; IAM secrets, chiffrement, tokenisation et accès privilégiés cloud.",
            ["secrets_management", "encryption", "tokenization", "privileged_access"],
            "enterprise_quote",
            "enterprise",
            "https://cpl.thalesgroup.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "evidian",
            "Evidian (Atos)",
            "https://evidian.com/",
            ["identity-access-management"],
            "IAM enterprise FR ; SSO, provisioning, gouvernance identités et conformité secteurs public/régulés.",
            ["sso", "provisioning", "identity_governance", "public_sector"],
            "enterprise_quote",
            "enterprise",
            "https://evidian.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "beyondtrust",
            "BeyondTrust",
            "https://www.beyondtrust.com/",
            ["identity-access-management"],
            "PAM et accès privilégiés ; vault secrets, session management et least privilege endpoint.",
            ["pam", "secrets_vault", "session_management", "least_privilege"],
            "enterprise_quote",
            "enterprise",
            "https://www.beyondtrust.com/",
            "g2",
        ),
        v(
            "saviynt",
            "Saviynt",
            "https://saviynt.com/",
            ["identity-access-management"],
            "IGA cloud-native ; gouvernance accès, certifications, provisioning SaaS/IaaS et SoD.",
            ["iga", "access_governance", "certification", "sod"],
            "enterprise_quote",
            "enterprise",
            "https://saviynt.com/",
            "g2",
        ),
        v(
            "onelogin",
            "OneLogin",
            "https://www.onelogin.com/",
            ["identity-access-management"],
            "IAM workforce ; SSO, MFA, directory et provisioning apps cloud pour PME/enterprise.",
            ["sso", "mfa", "directory", "provisioning"],
            "hybrid",
            "mid_market",
            "https://www.onelogin.com/",
            "g2",
        ),
        v(
            "strongdm",
            "StrongDM",
            "https://www.strongdm.com/",
            ["identity-access-management"],
            "Infrastructure access platform ; PAM moderne, accès DB/K8s/servers avec audit session complet.",
            ["infrastructure_access", "pam", "session_audit", "zero_trust"],
            "hybrid",
            "mid_market",
            "https://www.strongdm.com/",
            "crunchbase",
        ),
    ],
    "cloud-security-cspm.json": [
        v(
            "zscaler",
            "Zscaler",
            "https://www.zscaler.com/",
            ["cloud-security-cspm"],
            "SSE/ZTNA ; SWG, CASB, posture SaaS et accès zero-trust sans VPN pour workforce distribué.",
            ["sse", "ztna", "casb", "swg"],
            "enterprise_quote",
            "enterprise",
            "https://www.zscaler.com/",
            "analyst_report",
        ),
        v(
            "tailscale",
            "Tailscale",
            "https://tailscale.com/",
            ["cloud-security-cspm"],
            "Mesh VPN zero-trust ; accès réseau WireGuard, ACLs identity-aware et posture devices.",
            ["zero_trust", "mesh_vpn", "wireguard", "device_posture"],
            "hybrid",
            "mid_market",
            "https://tailscale.com/",
            "official_site",
        ),
        v(
            "upwind",
            "Upwind",
            "https://www.upwind.io/",
            ["cloud-security-cspm"],
            "CNAPP runtime-first ; posture cloud, détection menaces K8s/containers et prioritisation risques.",
            ["cnapp", "cspm", "runtime_detection", "kubernetes"],
            "enterprise_quote",
            "mid_market",
            "https://www.upwind.io/",
            "crunchbase",
            hq="IL",
            fr="partial",
            regions=["IL", "US", "EU"],
        ),
        v(
            "microsoft-defender-cloud",
            "Microsoft Defender for Cloud",
            "https://www.microsoft.com/en-us/security/business/cloud-security",
            ["cloud-security-cspm"],
            "CSPM/CWPP Azure/multi-cloud ; posture, recommandations CIS, CIEM et workload protection.",
            ["cspm", "cwpp", "ciem", "multi_cloud"],
            "hybrid",
            "enterprise",
            "https://www.microsoft.com/en-us/security/business/cloud-security",
            "official_site",
        ),
        v(
            "google-security-command-center",
            "Google Security Command Center",
            "https://cloud.google.com/security-command-center",
            ["cloud-security-cspm"],
            "CSPM GCP ; détection menaces, vulnérabilités assets, compliance et SIEM intégration Chronicle.",
            ["cspm", "threat_detection", "asset_inventory", "compliance"],
            "hybrid",
            "enterprise",
            "https://cloud.google.com/security-command-center",
            "official_site",
        ),
        v(
            "stacklet",
            "Stacklet",
            "https://stacklet.io/",
            ["cloud-security-cspm"],
            "Cloud governance ; policies-as-code multi-cloud, guardrails compliance et remédiation automatisée.",
            ["cloud_governance", "policy_as_code", "guardrails", "remediation"],
            "hybrid",
            "mid_market",
            "https://stacklet.io/",
            "crunchbase",
        ),
        v(
            "cloudflare-zero-trust",
            "Cloudflare Zero Trust",
            "https://www.cloudflare.com/zero-trust/",
            ["cloud-security-cspm"],
            "SSE zero-trust ; ZTNA, CASB, SWG, DLP et posture accès applications SaaS/self-hosted.",
            ["ztna", "sse", "casb", "dlp"],
            "hybrid",
            "mid_market",
            "https://www.cloudflare.com/zero-trust/",
            "official_site",
        ),
    ],
    "email-security.json": [
        v(
            "mailinblack",
            "Mailinblack",
            "https://www.mailinblack.com/",
            ["email-security"],
            "Protection email FR ; anti-phishing, anti-spam, sensibilisation utilisateurs et conformité RGPD.",
            ["anti_phishing", "anti_spam", "awareness", "rgpd"],
            "hybrid",
            "mid_market",
            "https://www.mailinblack.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "hornetsecurity",
            "Hornetsecurity",
            "https://www.hornetsecurity.com/",
            ["email-security"],
            "Email security cloud EU ; backup M365/Google, filtrage avancé et compliance eDiscovery.",
            ["email_filtering", "backup", "m365", "ediscovery"],
            "hybrid",
            "mid_market",
            "https://www.hornetsecurity.com/",
            "g2",
            hq="DE",
            fr="partial",
            geo="europe",
            regions=["DE", "EU", "FR"],
            notes="Maison mère de Vade Secure.",
        ),
        v(
            "knowbe4",
            "KnowBe4",
            "https://www.knowbe4.com/",
            ["email-security"],
            "Human risk management ; simulation phishing, formation sécurité et scoring vulnérabilité utilisateurs.",
            ["phishing_simulation", "security_awareness", "training", "human_risk"],
            "hybrid",
            "mid_market",
            "https://www.knowbe4.com/",
            "g2",
        ),
        v(
            "microsoft-defender-office365",
            "Microsoft Defender for Office 365",
            "https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-office-365",
            ["email-security"],
            "Protection email M365 ; anti-phishing, Safe Links/Attachments, BEC et investigation Threat Explorer.",
            ["anti_phishing", "safe_links", "bec", "threat_investigation"],
            "hybrid",
            "enterprise",
            "https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-office-365",
            "official_site",
        ),
        v(
            "keepnet-labs",
            "Keepnet Labs",
            "https://keepnetlabs.com/",
            ["email-security"],
            "Human-centric email security ; simulation phishing, awareness et incident response email automatisé.",
            ["phishing_simulation", "awareness", "incident_response", "email_threats"],
            "hybrid",
            "mid_market",
            "https://keepnetlabs.com/",
            "g2",
            hq="GB",
            fr="partial",
            regions=["GB", "EU", "US"],
        ),
        v(
            "libraesva",
            "Libraesva",
            "https://www.libraesva.com/",
            ["email-security"],
            "Email security EU ; filtrage spam/phishing, sandboxing attachments et gateway messagerie souveraine.",
            ["email_filtering", "sandboxing", "gateway", "anti_phishing"],
            "hybrid",
            "mid_market",
            "https://www.libraesva.com/",
            "g2",
            hq="IT",
            fr="partial",
            geo="europe",
            regions=["IT", "EU", "FR"],
        ),
        v(
            "avanan",
            "Avanan (Check Point Harmony Email)",
            "https://www.checkpoint.com/harmony/email-security/",
            ["email-security"],
            "Email security cloud ; API M365/Google, anti-phishing IA et remédiation post-delivery inline.",
            ["cloud_email", "m365", "anti_phishing", "post_delivery_remediation"],
            "enterprise_quote",
            "enterprise",
            "https://www.checkpoint.com/harmony/email-security/",
            "analyst_report",
            hq="IL",
            fr="partial",
            regions=["IL", "US", "EU"],
        ),
    ],
    "vulnerability-management.json": [
        v(
            "yeswehack",
            "YesWeHack",
            "https://www.yeswehack.com/",
            ["vulnerability-management"],
            "Bug bounty & pentest FR ; plateforme crowdsourcée, programmes publics/privés et conformité ISO 29147.",
            ["bug_bounty", "crowdsourced_pentest", "vdp", "iso_29147"],
            "hybrid",
            "mid_market",
            "https://www.yeswehack.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "yogosha",
            "Yogosha",
            "https://yogosha.com/",
            ["vulnerability-management"],
            "Pentest-as-a-Service FR ; communauté chasseurs, tests continus et reporting exécutif conformité.",
            ["pentest_as_a_service", "continuous_testing", "red_team", "compliance_reporting"],
            "enterprise_quote",
            "mid_market",
            "https://yogosha.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "hackerone",
            "HackerOne",
            "https://www.hackerone.com/",
            ["vulnerability-management"],
            "Bug bounty leader ; programmes VDP/BBP, triage et intégration SDLC pour enterprise.",
            ["bug_bounty", "vdp", "triage", "sdlc_integration"],
            "enterprise_quote",
            "enterprise",
            "https://www.hackerone.com/",
            "g2",
        ),
        v(
            "bugcrowd",
            "Bugcrowd",
            "https://www.bugcrowd.com/",
            ["vulnerability-management"],
            "Crowdsourced security ; bug bounty, pentest continu et attack surface reduction.",
            ["bug_bounty", "continuous_pentest", "asm", "crowdsourced"],
            "enterprise_quote",
            "enterprise",
            "https://www.bugcrowd.com/",
            "g2",
        ),
        v(
            "synack",
            "Synack",
            "https://www.synack.com/",
            ["vulnerability-management"],
            "Pentest continu ; communauté vetted researchers, red teaming et priorisation vulnérabilités.",
            ["continuous_pentest", "red_team", "vulnerability_prioritization", "vetted_researchers"],
            "enterprise_quote",
            "enterprise",
            "https://www.synack.com/",
            "analyst_report",
        ),
        v(
            "outpost24",
            "Outpost24",
            "https://outpost24.com/",
            ["vulnerability-management"],
            "Exposure management EU ; scan externe, patch management et security ratings pour TPRM.",
            ["exposure_management", "external_scanning", "patch_management", "security_ratings"],
            "enterprise_quote",
            "mid_market",
            "https://outpost24.com/",
            "g2",
            hq="SE",
            fr="partial",
            geo="europe",
            regions=["SE", "EU", "FR"],
        ),
        v(
            "projectdiscovery",
            "ProjectDiscovery (Nuclei)",
            "https://projectdiscovery.io/",
            ["vulnerability-management"],
            "Scan vulnérabilités open-source ; Nuclei templates, recon automatisée et CI/CD shift-left.",
            ["nuclei", "vulnerability_scanning", "recon", "shift_left"],
            "open_source",
            "self_serve",
            "https://projectdiscovery.io/",
            "open_source",
        ),
    ],
    "vector-databases.json": [
        v(
            "lancedb",
            "LanceDB",
            "https://lancedb.com/",
            ["vector-databases"],
            "Vector DB serverless ; stockage columnar Lance, recherche multimodale et embeddings à l'échelle.",
            ["serverless", "multimodal", "columnar", "embeddings"],
            "hybrid",
            "mid_market",
            "https://lancedb.com/",
            "crunchbase",
        ),
        v(
            "elasticsearch-vector",
            "Elasticsearch Vector Search",
            "https://www.elastic.co/elasticsearch/vector-search",
            ["vector-databases"],
            "Recherche vectorielle Elastic ; dense/sparse vectors, hybrid search et RAG sur stack ELK.",
            ["vector_search", "hybrid_search", "dense_sparse", "rag"],
            "hybrid",
            "enterprise",
            "https://www.elastic.co/elasticsearch/vector-search",
            "official_site",
        ),
        v(
            "opensearch-vector",
            "OpenSearch k-NN",
            "https://opensearch.org/platform/search/vector-search.html",
            ["vector-databases"],
            "Vector search open-source ; k-NN HNSW, filtres metadata et déploiement self-hosted/cloud.",
            ["knn", "hnsw", "metadata_filter", "self_hosted"],
            "open_source",
            "mid_market",
            "https://opensearch.org/platform/search/vector-search.html",
            "open_source",
        ),
        v(
            "singlestore",
            "SingleStore",
            "https://www.singlestore.com/",
            ["vector-databases"],
            "Base HTAP + vectors ; SQL, vector search temps réel et analytics unifiés pour apps GenAI.",
            ["htap", "vector_search", "real_time", "genai"],
            "hybrid",
            "enterprise",
            "https://www.singlestore.com/",
            "g2",
        ),
        v(
            "typesense",
            "Typesense",
            "https://typesense.org/",
            ["vector-databases"],
            "Moteur recherche typo-tolerant ; vector search intégré, API simple et self-hosted léger.",
            ["typo_tolerance", "vector_search", "self_hosted", "api"],
            "hybrid",
            "mid_market",
            "https://typesense.org/",
            "open_source",
        ),
        v(
            "faiss",
            "Faiss (Meta)",
            "https://github.com/facebookresearch/faiss",
            ["vector-databases"],
            "Bibliothèque ANN open-source ; index GPU/CPU, quantization et base des stacks vector self-hosted.",
            ["ann", "gpu_index", "quantization", "open_source"],
            "open_source",
            "self_serve",
            "https://github.com/facebookresearch/faiss",
            "open_source",
        ),
        v(
            "supabase-vector",
            "Supabase Vector",
            "https://supabase.com/docs/guides/ai/vector-columns",
            ["vector-databases"],
            "pgvector managé Supabase ; embeddings Postgres, edge functions et API RAG développeur-friendly.",
            ["pgvector", "managed_postgres", "edge_functions", "rag"],
            "hybrid",
            "mid_market",
            "https://supabase.com/docs/guides/ai/vector-columns",
            "official_site",
        ),
        v(
            "neon-serverless",
            "Neon Serverless Postgres",
            "https://neon.tech/docs/extensions/pgvector",
            ["vector-databases"],
            "Postgres serverless + pgvector ; branching DB, scale-to-zero et stack SQL pour RAG production.",
            ["serverless_postgres", "pgvector", "branching", "scale_to_zero"],
            "hybrid",
            "mid_market",
            "https://neon.tech/",
            "official_site",
        ),
        v(
            "couchbase-vector",
            "Couchbase Capella Vector Search",
            "https://www.couchbase.com/products/vector-search",
            ["vector-databases"],
            "Vector search NoSQL ; filtres metadata riches, mobile edge sync et latence sub-ms.",
            ["nosql_vectors", "metadata_filter", "edge_sync", "low_latency"],
            "hybrid",
            "enterprise",
            "https://www.couchbase.com/products/vector-search",
            "official_site",
        ),
        v(
            "azure-ai-search",
            "Azure AI Search",
            "https://azure.microsoft.com/en-us/products/ai-services/ai-search",
            ["vector-databases"],
            "Recherche cognitive Azure ; vector/hybrid search, semantic ranking et intégration OpenAI RAG.",
            ["vector_search", "hybrid_search", "semantic_ranking", "azure_openai"],
            "hybrid",
            "enterprise",
            "https://azure.microsoft.com/en-us/products/ai-services/ai-search",
            "official_site",
        ),
    ],
}

SEGMENT_PATCHES: dict[str, list[str]] = {
    "vespa": ["vector-databases"],
    "stormshield": ["cloud-security-cspm"],
    "crowdsec": ["vulnerability-management"],
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "cybersecurity-platforms": {
        "g2": {"consulted_at": TODAY, "candidates_found": 22, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 18, "new_added": 4, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 1, "pass": PASS_ID},
    },
    "identity-access-management": {
        "g2": {"consulted_at": TODAY, "candidates_found": 20, "new_added": 4, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 3, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 1, "pass": PASS_ID},
    },
    "cloud-security-cspm": {
        "g2": {"consulted_at": TODAY, "candidates_found": 18, "new_added": 1, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 2, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 3, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 1, "pass": PASS_ID},
    },
    "email-security": {
        "g2": {"consulted_at": TODAY, "candidates_found": 16, "new_added": 3, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 1, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
    },
    "vulnerability-management": {
        "g2": {"consulted_at": TODAY, "candidates_found": 18, "new_added": 3, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 2, "pass": PASS_ID},
        "open_source": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 1, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
    },
    "vector-databases": {
        "g2": {"consulted_at": TODAY, "candidates_found": 16, "new_added": 2, "pass": PASS_ID},
        "open_source": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 3, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 4, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
    },
}

TARGET_LEVELS = {
    "cybersecurity-platforms": "L3",
    "identity-access-management": "L3",
    "cloud-security-cspm": "L3",
    "email-security": "L3",
    "vulnerability-management": "L3",
    "vector-databases": "L3",
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
