#!/usr/bin/env python3
"""Vague 4 — peuplement des 47 segments vides (3–5 vendeurs/segment)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
TODAY = "2026-06-22"

ADDITIONS: dict[str, list[dict]] = {
    "esg-csrd.json": [
        {
            "id": "watershed",
            "name": "Watershed",
            "url": "https://watershed.com/",
            "segments": [
                "esg-csrd"
            ],
            "description": "Plateforme enterprise de comptabilité carbone, reporting CSRD et décarbonation supply chain.",
            "capabilities": [
                "carbon_accounting",
                "csrd_reporting",
                "scope_3",
                "scenario_planning"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://watershed.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "persefoni",
            "name": "Persefoni",
            "url": "https://www.persefoni.com/",
            "segments": [
                "esg-csrd"
            ],
            "description": "Climate management & reporting ; mesure émissions, disclosures réglementaires et finance durable.",
            "capabilities": [
                "ghg_inventory",
                "regulatory_disclosure",
                "climate_analytics"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.persefoni.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "normative",
            "name": "Normative",
            "url": "https://normative.io/",
            "segments": [
                "esg-csrd"
            ],
            "description": "Carbon accounting automatisé pour PME et mid-market ; alignement GHG Protocol et CSRD.",
            "capabilities": [
                "automated_carbon",
                "supplier_engagement",
                "csrd"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://normative.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "greenly",
            "name": "Greenly",
            "url": "https://greenly.earth/",
            "segments": [
                "esg-csrd"
            ],
            "description": "SaaS bilan carbone et trajectoire net-zero pour entreprises ; offre France/Europe.",
            "capabilities": [
                "carbon_footprint",
                "action_plans",
                "csrd_readiness"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "france",
            "source_url": "https://greenly.earth/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "workiva-esg",
            "name": "Workiva",
            "url": "https://www.workiva.com/solutions/esg-reporting",
            "segments": [
                "esg-csrd"
            ],
            "description": "Reporting extra-financier connecté ; workflows CSRD, assurance et collaboration audit.",
            "capabilities": [
                "connected_reporting",
                "esg_disclosure",
                "audit_trail"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.workiva.com/solutions/esg-reporting",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "kyc-aml.json": [
        {
            "id": "onfido",
            "name": "Onfido",
            "url": "https://onfido.com/",
            "segments": [
                "kyc-aml"
            ],
            "description": "Vérification d'identité documentaire et biométrique pour onboarding digital.",
            "capabilities": [
                "document_verification",
                "biometric_check",
                "liveness",
                "fraud_signals"
            ],
            "pricing_model": "per_usage",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://onfido.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "sumsub",
            "name": "Sumsub",
            "url": "https://sumsub.com/",
            "segments": [
                "kyc-aml"
            ],
            "description": "Plateforme KYC/KYB/AML full-stack ; screening sanctions et monitoring transactionnel.",
            "capabilities": [
                "kyc_kyb",
                "aml_screening",
                "transaction_monitoring"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://sumsub.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "jumio",
            "name": "Jumio",
            "url": "https://www.jumio.com/",
            "segments": [
                "kyc-aml"
            ],
            "description": "Identity verification et AML compliance pour secteurs régulés (fintech, gaming).",
            "capabilities": [
                "id_verification",
                "aml_compliance",
                "age_verification"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.jumio.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "complyadvantage",
            "name": "ComplyAdvantage",
            "url": "https://complyadvantage.com/",
            "segments": [
                "kyc-aml"
            ],
            "description": "Screening sanctions, PEP et adverse media avec modèles ML pour réduire faux positifs.",
            "capabilities": [
                "sanctions_screening",
                "pep",
                "adverse_media",
                "transaction_monitoring"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://complyadvantage.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "seon",
            "name": "SEON",
            "url": "https://seon.io/",
            "segments": [
                "kyc-aml"
            ],
            "description": "Fraud prevention et enrichissement digital footprint pour onboarding et paiements.",
            "capabilities": [
                "device_fingerprint",
                "email_phone_signals",
                "fraud_scoring"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://seon.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "pharma-regulatory.json": [
        {
            "id": "veeva-vault",
            "name": "Veeva Vault",
            "url": "https://www.veeva.com/products/",
            "segments": [
                "pharma-regulatory"
            ],
            "description": "Suite cloud life sciences : qualité, regulatory, clinical, safety (GxP).",
            "capabilities": [
                "regulatory_submissions",
                "quality_management",
                "pharmacovigilance",
                "gxp"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.veeva.com/products/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "mastercontrol",
            "name": "MasterControl",
            "url": "https://www.mastercontrol.com/",
            "segments": [
                "pharma-regulatory"
            ],
            "description": "QMS et document management pour pharma/medtech ; workflows validation et CAPA.",
            "capabilities": [
                "qms",
                "document_control",
                "training",
                "capa"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.mastercontrol.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "iqvia-regulatory",
            "name": "IQVIA Regulatory",
            "url": "https://www.iqvia.com/solutions/compliance-and-regulatory",
            "segments": [
                "pharma-regulatory"
            ],
            "description": "Services et technologie regulatory intelligence, submissions et conformité mondiale.",
            "capabilities": [
                "regulatory_intelligence",
                "submissions",
                "labeling"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.iqvia.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "ennov",
            "name": "Ennov",
            "url": "https://www.ennov.com/",
            "segments": [
                "pharma-regulatory"
            ],
            "description": "Suite eCTD et gestion documentaire réglementaire pharma ; éditeur français.",
            "capabilities": [
                "ectd",
                "regulatory_documents",
                "workflow"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "france",
            "source_url": "https://www.ennov.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "openvox",
            "name": "OpenVox",
            "url": "https://www.openvox.fr/",
            "segments": [
                "pharma-regulatory"
            ],
            "description": "Solutions eCTD et dossiers réglementaires pour industrie pharmaceutique.",
            "capabilities": [
                "ectd_publishing",
                "regulatory_archive",
                "france"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.openvox.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "cybersecurity-platforms.json": [
        {
            "id": "crowdstrike-falcon",
            "name": "CrowdStrike Falcon",
            "url": "https://www.crowdstrike.com/",
            "segments": [
                "cybersecurity-platforms"
            ],
            "description": "Plateforme XDR cloud-native : EDR, threat intelligence, SOAR et managed detection.",
            "capabilities": [
                "edr",
                "xdr",
                "threat_intel",
                "incident_response"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.crowdstrike.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "palo-alto-cortex",
            "name": "Palo Alto Cortex",
            "url": "https://www.paloaltonetworks.com/cortex",
            "segments": [
                "cybersecurity-platforms"
            ],
            "description": "Cortex XDR/XSIAM : détection, investigation et réponse unifiées sur endpoints et cloud.",
            "capabilities": [
                "xdr",
                "xsiam",
                "soar",
                "automation"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.paloaltonetworks.com/cortex",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "sentinelone",
            "name": "SentinelOne",
            "url": "https://www.sentinelone.com/",
            "segments": [
                "cybersecurity-platforms"
            ],
            "description": "Endpoint protection autonome avec AI ; EDR, XDR et gestion vulnérabilités.",
            "capabilities": [
                "edr",
                "xdr",
                "ransomware_protection"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.sentinelone.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "splunk-enterprise-security",
            "name": "Splunk Enterprise Security",
            "url": "https://www.splunk.com/en_us/products/enterprise-security.html",
            "segments": [
                "cybersecurity-platforms"
            ],
            "description": "SIEM/SOAR leader ; corrélation événements, UEBA et playbooks réponse incident.",
            "capabilities": [
                "siem",
                "soar",
                "ueba",
                "threat_detection"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.splunk.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "microsoft-defender-xdr",
            "name": "Microsoft Defender XDR",
            "url": "https://www.microsoft.com/en-us/security/business/siem-and-xdr",
            "segments": [
                "cybersecurity-platforms"
            ],
            "description": "Suite XDR Microsoft : Defender for Endpoint, Identity, Office 365 et Sentinel SIEM.",
            "capabilities": [
                "xdr",
                "siem",
                "identity_protection",
                "cloud_security"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.microsoft.com/en-us/security/business/siem-and-xdr",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "identity-access-management.json": [
        {
            "id": "okta",
            "name": "Okta",
            "url": "https://www.okta.com/",
            "segments": [
                "identity-access-management"
            ],
            "description": "IAM cloud : SSO, MFA, lifecycle provisioning et Customer Identity (Auth0).",
            "capabilities": [
                "sso",
                "mfa",
                "lifecycle",
                "customer_identity"
            ],
            "pricing_model": "hybrid",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.okta.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "microsoft-entra-id",
            "name": "Microsoft Entra ID",
            "url": "https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id",
            "segments": [
                "identity-access-management"
            ],
            "description": "Identité cloud Microsoft ; SSO, conditional access, B2B et governance.",
            "capabilities": [
                "sso",
                "conditional_access",
                "identity_governance"
            ],
            "pricing_model": "hybrid",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "sailpoint",
            "name": "SailPoint",
            "url": "https://www.sailpoint.com/",
            "segments": [
                "identity-access-management"
            ],
            "description": "Identity governance : accès, certifications, provisioning et compliance IAM.",
            "capabilities": [
                "iga",
                "access_certification",
                "provisioning"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.sailpoint.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "1password-business",
            "name": "1Password",
            "url": "https://1password.com/business/",
            "segments": [
                "identity-access-management"
            ],
            "description": "Gestion mots de passe et secrets ; SSO, SCIM et accès développeur.",
            "capabilities": [
                "password_management",
                "secrets",
                "sso",
                "scim"
            ],
            "pricing_model": "per_seat",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://1password.com/business/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "jumpcloud",
            "name": "JumpCloud",
            "url": "https://jumpcloud.com/",
            "segments": [
                "identity-access-management"
            ],
            "description": "Open directory platform : IAM, MDM et accès zero-trust pour PME.",
            "capabilities": [
                "directory",
                "sso",
                "mdm",
                "pam"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://jumpcloud.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "cloud-security-cspm.json": [
        {
            "id": "wiz",
            "name": "Wiz",
            "url": "https://www.wiz.io/",
            "segments": [
                "cloud-security-cspm"
            ],
            "description": "CNAPP leader : posture cloud, vulnérabilités workloads, secrets et CIEM.",
            "capabilities": [
                "cspm",
                "cnapp",
                "ciem",
                "vulnerability_management"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.wiz.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "orca-security",
            "name": "Orca Security",
            "url": "https://orca.security/",
            "segments": [
                "cloud-security-cspm"
            ],
            "description": "Agentless cloud security : CSPM, CWPP, CIEM et détection malware cloud.",
            "capabilities": [
                "cspm",
                "cwpp",
                "agentless_scanning"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://orca.security/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "prisma-cloud",
            "name": "Prisma Cloud (Palo Alto)",
            "url": "https://www.paloaltonetworks.com/prisma/cloud",
            "segments": [
                "cloud-security-cspm"
            ],
            "description": "CNAPP multi-cloud : posture, compliance, runtime protection et IaC scanning.",
            "capabilities": [
                "cspm",
                "cwpp",
                "iac_scanning",
                "compliance"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.paloaltonetworks.com/prisma/cloud",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "lacework",
            "name": "Lacework (Fortinet)",
            "url": "https://www.lacework.com/",
            "segments": [
                "cloud-security-cspm"
            ],
            "description": "Cloud security platform : behavioral anomaly detection et posture multi-cloud.",
            "capabilities": [
                "cspm",
                "anomaly_detection",
                "kubernetes_security"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.lacework.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "aqua-security",
            "name": "Aqua Security",
            "url": "https://www.aquasec.com/",
            "segments": [
                "cloud-security-cspm"
            ],
            "description": "Sécurité conteneurs/Kubernetes et supply chain ; CSPM et runtime protection.",
            "capabilities": [
                "container_security",
                "kubernetes",
                "supply_chain"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.aquasec.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "email-security.json": [
        {
            "id": "proofpoint",
            "name": "Proofpoint",
            "url": "https://www.proofpoint.com/",
            "segments": [
                "email-security"
            ],
            "description": "SEG enterprise : anti-phishing, BEC, DLP et threat intelligence email.",
            "capabilities": [
                "seg",
                "anti_phishing",
                "bec_protection",
                "dlp"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.proofpoint.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "mimecast",
            "name": "Mimecast",
            "url": "https://www.mimecast.com/",
            "segments": [
                "email-security"
            ],
            "description": "Email security cloud : protection, archiving, continuity et awareness.",
            "capabilities": [
                "email_filtering",
                "archiving",
                "continuity",
                "awareness"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.mimecast.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "abnormal-security",
            "name": "Abnormal Security",
            "url": "https://abnormalsecurity.com/",
            "segments": [
                "email-security"
            ],
            "description": "AI-native email security : détection comportementale BEC et account takeover.",
            "capabilities": [
                "ai_detection",
                "bec",
                "account_takeover"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://abnormalsecurity.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "barracuda-email",
            "name": "Barracuda Email Protection",
            "url": "https://www.barracuda.com/products/emailprotection",
            "segments": [
                "email-security"
            ],
            "description": "Protection messagerie : anti-spam, phishing, impersonation et backup.",
            "capabilities": [
                "anti_spam",
                "phishing",
                "impersonation"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.barracuda.com/products/emailprotection",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "google-email-security",
            "name": "Google Workspace Email Security",
            "url": "https://workspace.google.com/security/",
            "segments": [
                "email-security"
            ],
            "description": "Protections Gmail/Workspace intégrées : phishing, malware, SPF/DKIM/DMARC.",
            "capabilities": [
                "gmail_protection",
                "dmarc",
                "dlp"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://workspace.google.com/security/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "vulnerability-management.json": [
        {
            "id": "tenable",
            "name": "Tenable",
            "url": "https://www.tenable.com/",
            "segments": [
                "vulnerability-management"
            ],
            "description": "Exposure management : Nessus, Tenable.io et priorisation vulnérabilités attack path.",
            "capabilities": [
                "vulnerability_scanning",
                "exposure_management",
                "attack_surface"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.tenable.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "qualys",
            "name": "Qualys",
            "url": "https://www.qualys.com/",
            "segments": [
                "vulnerability-management"
            ],
            "description": "VMDR cloud : scan assets, patch management et cyber risk quantification.",
            "capabilities": [
                "vmdr",
                "asset_inventory",
                "patch_management"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.qualys.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "rapid7-insightvm",
            "name": "Rapid7 InsightVM",
            "url": "https://www.rapid7.com/products/insightvm/",
            "segments": [
                "vulnerability-management"
            ],
            "description": "Gestion vulnérabilités et remediation ; intégration SIEM/SOAR InsightIDR.",
            "capabilities": [
                "vulnerability_management",
                "remediation",
                "risk_scoring"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.rapid7.com/products/insightvm/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "bitsight",
            "name": "Bitsight",
            "url": "https://www.bitsight.com/",
            "segments": [
                "vulnerability-management"
            ],
            "description": "Security ratings et gestion surface d'attaque tierce ; monitoring continu.",
            "capabilities": [
                "security_ratings",
                "third_party_risk",
                "attack_surface"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.bitsight.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "detectify",
            "name": "Detectify",
            "url": "https://detectify.com/",
            "segments": [
                "vulnerability-management"
            ],
            "description": "Surface monitoring et DAST automatisé pour applications web et APIs.",
            "capabilities": [
                "dast",
                "surface_monitoring",
                "asset_discovery"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://detectify.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "llm-api-providers.json": [
        {
            "id": "openai-api",
            "name": "OpenAI API",
            "url": "https://platform.openai.com/",
            "segments": [
                "llm-api-providers"
            ],
            "description": "API GPT-4o/o-series, embeddings et fine-tuning ; référence marché LLM.",
            "capabilities": [
                "chat_completions",
                "embeddings",
                "fine_tuning",
                "assistants"
            ],
            "pricing_model": "per_usage",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://openai.com/api/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "anthropic-api",
            "name": "Anthropic API",
            "url": "https://www.anthropic.com/api",
            "segments": [
                "llm-api-providers"
            ],
            "description": "Claude models via API ; long context, tool use et safety-focused.",
            "capabilities": [
                "claude_models",
                "tool_use",
                "long_context"
            ],
            "pricing_model": "per_usage",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.anthropic.com/api",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "mistral-ai",
            "name": "Mistral AI",
            "url": "https://mistral.ai/",
            "segments": [
                "llm-api-providers"
            ],
            "description": "Modèles open et propriétaires européens ; API, fine-tuning et déploiement souverain.",
            "capabilities": [
                "frontier_models",
                "open_models",
                "europe_sovereignty"
            ],
            "pricing_model": "per_usage",
            "target_market": "mid_market",
            "geography": "europe",
            "source_url": "https://mistral.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "google-gemini-api",
            "name": "Google Gemini API",
            "url": "https://ai.google.dev/",
            "segments": [
                "llm-api-providers"
            ],
            "description": "Gemini multimodal via Vertex AI et AI Studio ; grounding et function calling.",
            "capabilities": [
                "multimodal",
                "grounding",
                "function_calling"
            ],
            "pricing_model": "per_usage",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://ai.google.dev/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "cohere",
            "name": "Cohere",
            "url": "https://cohere.com/",
            "segments": [
                "llm-api-providers"
            ],
            "description": "LLM enterprise : génération, embeddings, rerank et RAG toolkit.",
            "capabilities": [
                "generation",
                "embeddings",
                "rerank",
                "rag"
            ],
            "pricing_model": "per_usage",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://cohere.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "model-inference-hosting.json": [
        {
            "id": "hugging-face",
            "name": "Hugging Face",
            "url": "https://huggingface.co/",
            "segments": [
                "model-inference-hosting"
            ],
            "description": "Hub modèles open-source, Inference Endpoints, Spaces et fine-tuning.",
            "capabilities": [
                "model_hub",
                "inference_endpoints",
                "spaces",
                "fine_tuning"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://huggingface.co/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "together-ai",
            "name": "Together AI",
            "url": "https://www.together.ai/",
            "segments": [
                "model-inference-hosting"
            ],
            "description": "Inference GPU cloud pour modèles open-source ; fine-tuning et serverless.",
            "capabilities": [
                "gpu_inference",
                "fine_tuning",
                "serverless"
            ],
            "pricing_model": "per_usage",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.together.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "replicate",
            "name": "Replicate",
            "url": "https://replicate.com/",
            "segments": [
                "model-inference-hosting"
            ],
            "description": "Run ML models via API ; hosting open-source et custom containers.",
            "capabilities": [
                "model_api",
                "custom_models",
                "gpu_scaling"
            ],
            "pricing_model": "per_usage",
            "target_market": "self_serve",
            "geography": "global",
            "source_url": "https://replicate.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "modal",
            "name": "Modal",
            "url": "https://modal.com/",
            "segments": [
                "model-inference-hosting"
            ],
            "description": "Infrastructure serverless GPU pour inference, training et batch jobs Python.",
            "capabilities": [
                "serverless_gpu",
                "inference",
                "batch_jobs"
            ],
            "pricing_model": "per_usage",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://modal.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "aws-bedrock",
            "name": "Amazon Bedrock",
            "url": "https://aws.amazon.com/bedrock/",
            "segments": [
                "model-inference-hosting"
            ],
            "description": "Managed foundation models multi-fournisseurs sur AWS ; fine-tuning et agents.",
            "capabilities": [
                "managed_models",
                "fine_tuning",
                "agents",
                "vpc"
            ],
            "pricing_model": "per_usage",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://aws.amazon.com/bedrock/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "vector-databases.json": [
        {
            "id": "pinecone",
            "name": "Pinecone",
            "url": "https://www.pinecone.io/",
            "segments": [
                "vector-databases"
            ],
            "description": "Vector DB managée serverless ; indexing, metadata filtering et hybrid search.",
            "capabilities": [
                "vector_search",
                "serverless",
                "metadata_filter"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.pinecone.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "weaviate",
            "name": "Weaviate",
            "url": "https://weaviate.io/",
            "segments": [
                "vector-databases"
            ],
            "description": "Base vectorielle open-source et cloud ; modules RAG et multi-tenancy.",
            "capabilities": [
                "vector_store",
                "hybrid_search",
                "rag_modules"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://weaviate.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "qdrant",
            "name": "Qdrant",
            "url": "https://qdrant.tech/",
            "segments": [
                "vector-databases"
            ],
            "description": "Vector search engine performant ; cloud managé et self-hosted.",
            "capabilities": [
                "vector_search",
                "filtering",
                "quantization"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://qdrant.tech/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "zilliz-milvus",
            "name": "Zilliz / Milvus",
            "url": "https://zilliz.com/",
            "segments": [
                "vector-databases"
            ],
            "description": "Milvus open-source et Zilliz Cloud pour embeddings à grande échelle.",
            "capabilities": [
                "distributed_vectors",
                "gpu_index",
                "cloud_managed"
            ],
            "pricing_model": "hybrid",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://zilliz.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "chroma",
            "name": "Chroma",
            "url": "https://www.trychroma.com/",
            "segments": [
                "vector-databases"
            ],
            "description": "Embedding database open-source orientée développeurs et prototypes RAG.",
            "capabilities": [
                "embeddings_store",
                "local_dev",
                "rag"
            ],
            "pricing_model": "open_source",
            "target_market": "self_serve",
            "geography": "global",
            "source_url": "https://www.trychroma.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "ai-evals-testing.json": [
        {
            "id": "braintrust",
            "name": "Braintrust",
            "url": "https://www.braintrust.dev/",
            "segments": [
                "ai-evals-testing"
            ],
            "description": "Plateforme evals LLM : datasets, scoring, régression et CI pour prompts.",
            "capabilities": [
                "eval_datasets",
                "scoring",
                "regression_ci",
                "prompt_management"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.braintrust.dev/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "promptfoo",
            "name": "Promptfoo",
            "url": "https://www.promptfoo.dev/",
            "segments": [
                "ai-evals-testing"
            ],
            "description": "CLI open-source pour tester et comparer prompts/modèles ; red teaming.",
            "capabilities": [
                "prompt_testing",
                "model_comparison",
                "red_teaming"
            ],
            "pricing_model": "open_source",
            "target_market": "self_serve",
            "geography": "global",
            "source_url": "https://www.promptfoo.dev/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "patronus-ai",
            "name": "Patronus AI",
            "url": "https://www.patronus.ai/",
            "segments": [
                "ai-evals-testing"
            ],
            "description": "Evaluation et monitoring LLM : hallucinations, sécurité et performance.",
            "capabilities": [
                "hallucination_detection",
                "safety_evals",
                "monitoring"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.patronus.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "galileo-ai",
            "name": "Galileo",
            "url": "https://www.rungalileo.io/",
            "segments": [
                "ai-evals-testing"
            ],
            "description": "Observability et evaluation GenAI : qualité outputs, drift et guardrails.",
            "capabilities": [
                "eval_metrics",
                "guardrails",
                "drift_detection"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.rungalileo.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "maxim-ai",
            "name": "Maxim AI",
            "url": "https://www.getmaxim.ai/",
            "segments": [
                "ai-evals-testing"
            ],
            "description": "Experimentation et evaluation pour agents et workflows LLM.",
            "capabilities": [
                "agent_evals",
                "simulation",
                "experiment_tracking"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.getmaxim.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "agent-frameworks-platforms.json": [
        {
            "id": "langchain",
            "name": "LangChain / LangGraph",
            "url": "https://www.langchain.com/",
            "segments": [
                "agent-frameworks-platforms"
            ],
            "description": "Framework orchestration LLM et agents ; LangGraph pour workflows stateful.",
            "capabilities": [
                "chains",
                "agents",
                "langgraph",
                "tool_calling"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.langchain.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "crewai",
            "name": "CrewAI",
            "url": "https://www.crewai.com/",
            "segments": [
                "agent-frameworks-platforms"
            ],
            "description": "Framework multi-agents role-based pour tâches collaboratives autonomes.",
            "capabilities": [
                "multi_agent",
                "role_based",
                "task_delegation"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.crewai.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "microsoft-autogen",
            "name": "Microsoft AutoGen",
            "url": "https://microsoft.github.io/autogen/",
            "segments": [
                "agent-frameworks-platforms"
            ],
            "description": "Framework open-source multi-agents conversationnels et tool use.",
            "capabilities": [
                "multi_agent_chat",
                "tool_use",
                "code_execution"
            ],
            "pricing_model": "open_source",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://microsoft.github.io/autogen/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "llamaindex",
            "name": "LlamaIndex",
            "url": "https://www.llamaindex.ai/",
            "segments": [
                "agent-frameworks-platforms"
            ],
            "description": "Data framework pour RAG et agents ; ingestion, indexing et workflows.",
            "capabilities": [
                "rag",
                "agents",
                "data_connectors",
                "workflows"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.llamaindex.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "semantic-kernel",
            "name": "Semantic Kernel",
            "url": "https://learn.microsoft.com/en-us/semantic-kernel/",
            "segments": [
                "agent-frameworks-platforms"
            ],
            "description": "SDK Microsoft pour orchestrer plugins, planners et agents enterprise.",
            "capabilities": [
                "plugins",
                "planners",
                "enterprise_agents"
            ],
            "pricing_model": "open_source",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://learn.microsoft.com/en-us/semantic-kernel/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "e-signature.json": [
        {
            "id": "docusign",
            "name": "DocuSign",
            "url": "https://www.docusign.com/",
            "segments": [
                "e-signature"
            ],
            "description": "Leader signature électronique ; eIDAS, CLM intégré et workflows enterprise.",
            "capabilities": [
                "e_signature",
                "eidas",
                "clm",
                "api"
            ],
            "pricing_model": "hybrid",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.docusign.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "adobe-acrobat-sign",
            "name": "Adobe Acrobat Sign",
            "url": "https://www.adobe.com/sign.html",
            "segments": [
                "e-signature"
            ],
            "description": "Signature documentaire intégrée écosystème Adobe ; conformité légale multi-pays.",
            "capabilities": [
                "e_signature",
                "pdf_workflows",
                "integrations"
            ],
            "pricing_model": "hybrid",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.adobe.com/sign.html",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "yousign",
            "name": "Yousign",
            "url": "https://yousign.com/",
            "segments": [
                "e-signature"
            ],
            "description": "Signature électronique française eIDAS ; PME et API développeurs.",
            "capabilities": [
                "e_signature",
                "eidas",
                "api",
                "france"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "france",
            "source_url": "https://yousign.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "pandadoc",
            "name": "PandaDoc",
            "url": "https://www.pandadoc.com/",
            "segments": [
                "e-signature"
            ],
            "description": "Propositions, contrats et signatures ; CPQ léger pour sales.",
            "capabilities": [
                "e_signature",
                "proposals",
                "cpq"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.pandadoc.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "dropbox-sign",
            "name": "Dropbox Sign (HelloSign)",
            "url": "https://sign.dropbox.com/",
            "segments": [
                "e-signature"
            ],
            "description": "Signature simple intégrée Dropbox ; API et templates.",
            "capabilities": [
                "e_signature",
                "templates",
                "api"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://sign.dropbox.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "translation-localization.json": [
        {
            "id": "deepl",
            "name": "DeepL",
            "url": "https://www.deepl.com/",
            "segments": [
                "translation-localization"
            ],
            "description": "Traduction neuronale haute qualité ; API, glossaires et write assist.",
            "capabilities": [
                "machine_translation",
                "api",
                "glossaries"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.deepl.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "phrase",
            "name": "Phrase (Memsource)",
            "url": "https://phrase.com/",
            "segments": [
                "translation-localization"
            ],
            "description": "TMS cloud : workflows traduction, MT, QA et intégrations CI/CD.",
            "capabilities": [
                "tms",
                "translation_memory",
                "mt_post_edit"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://phrase.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "smartling",
            "name": "Smartling",
            "url": "https://www.smartling.com/",
            "segments": [
                "translation-localization"
            ],
            "description": "Localization platform : traduction continue, connectors et analytics qualité.",
            "capabilities": [
                "continuous_localization",
                "connectors",
                "quality_analytics"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.smartling.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "lokalise",
            "name": "Lokalise",
            "url": "https://lokalise.com/",
            "segments": [
                "translation-localization"
            ],
            "description": "Localization pour produits digitaux ; strings, screenshots et workflows.",
            "capabilities": [
                "string_management",
                "in_context",
                "workflows"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://lokalise.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "crowdin",
            "name": "Crowdin",
            "url": "https://crowdin.com/",
            "segments": [
                "translation-localization"
            ],
            "description": "Plateforme localization agile ; crowdsourcing et intégrations dev.",
            "capabilities": [
                "string_localization",
                "crowdsourcing",
                "dev_integrations"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://crowdin.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "data-integration-etl.json": [
        {
            "id": "fivetran",
            "name": "Fivetran",
            "url": "https://www.fivetran.com/",
            "segments": [
                "data-integration-etl"
            ],
            "description": "ELT managé : 500+ connecteurs sources vers warehouses cloud.",
            "capabilities": [
                "managed_connectors",
                "elt",
                "dbt_integration"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.fivetran.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "airbyte",
            "name": "Airbyte",
            "url": "https://airbyte.com/",
            "segments": [
                "data-integration-etl"
            ],
            "description": "Data integration open-core ; connecteurs community et cloud managé.",
            "capabilities": [
                "connectors",
                "open_source",
                "elt"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://airbyte.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "dbt-labs",
            "name": "dbt Labs",
            "url": "https://www.getdbt.com/",
            "segments": [
                "data-integration-etl"
            ],
            "description": "Transformation SQL analytics-as-code ; tests, docs et lineage.",
            "capabilities": [
                "sql_transform",
                "testing",
                "lineage",
                "docs"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.getdbt.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "stitch-data",
            "name": "Stitch (Qlik)",
            "url": "https://www.stitchdata.com/",
            "segments": [
                "data-integration-etl"
            ],
            "description": "ELT simple pour analytics teams ; connecteurs SaaS vers warehouse.",
            "capabilities": [
                "elt",
                "saas_connectors",
                "scheduling"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.stitchdata.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "hevo-data",
            "name": "Hevo Data",
            "url": "https://hevodata.com/",
            "segments": [
                "data-integration-etl"
            ],
            "description": "Pipeline no-code vers Snowflake/BigQuery ; CDC et transformations.",
            "capabilities": [
                "no_code_pipelines",
                "cdc",
                "reverse_etl"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://hevodata.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "project-work-management.json": [
        {
            "id": "asana",
            "name": "Asana",
            "url": "https://asana.com/",
            "segments": [
                "project-work-management"
            ],
            "description": "Work management : projets, portfolios, goals et couche IA (Asana Intelligence).",
            "capabilities": [
                "project_tracking",
                "portfolios",
                "ai_summaries"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://asana.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "monday-com",
            "name": "monday.com",
            "url": "https://monday.com/",
            "segments": [
                "project-work-management"
            ],
            "description": "Work OS no-code ; boards, automations et AI blocks pour équipes.",
            "capabilities": [
                "work_os",
                "automations",
                "ai_blocks"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://monday.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "linear",
            "name": "Linear",
            "url": "https://linear.app/",
            "segments": [
                "project-work-management"
            ],
            "description": "Issue tracking moderne pour équipes produit/tech ; cycles et roadmaps.",
            "capabilities": [
                "issue_tracking",
                "roadmaps",
                "cycles"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://linear.app/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "clickup",
            "name": "ClickUp",
            "url": "https://clickup.com/",
            "segments": [
                "project-work-management"
            ],
            "description": "All-in-one productivité : tâches, docs, whiteboards et AI assistant.",
            "capabilities": [
                "tasks",
                "docs",
                "ai_assistant"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://clickup.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "wrike",
            "name": "Wrike",
            "url": "https://www.wrike.com/",
            "segments": [
                "project-work-management"
            ],
            "description": "PMO et gestion projet enterprise ; ressources, Gantt et reporting.",
            "capabilities": [
                "pmo",
                "resource_management",
                "reporting"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.wrike.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "meeting-intelligence.json": [
        {
            "id": "fireflies-ai",
            "name": "Fireflies.ai",
            "url": "https://fireflies.ai/",
            "segments": [
                "meeting-intelligence"
            ],
            "description": "Transcription, résumés et recherche dans réunions ; intégrations CRM.",
            "capabilities": [
                "transcription",
                "summaries",
                "crm_sync"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://fireflies.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "grain",
            "name": "Grain",
            "url": "https://grain.com/",
            "segments": [
                "meeting-intelligence"
            ],
            "description": "Highlights vidéo réunions, clips partageables et coaching sales.",
            "capabilities": [
                "video_highlights",
                "clips",
                "coaching"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://grain.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "fathom",
            "name": "Fathom",
            "url": "https://fathom.video/",
            "segments": [
                "meeting-intelligence"
            ],
            "description": "AI notetaker gratuit pour Zoom/Meet ; résumés et action items.",
            "capabilities": [
                "ai_notes",
                "action_items",
                "crm_integration"
            ],
            "pricing_model": "freemium",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://fathom.video/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "read-ai",
            "name": "Read AI",
            "url": "https://www.read.ai/",
            "segments": [
                "meeting-intelligence"
            ],
            "description": "Meeting copilot : résumés, engagement metrics et search cross-meetings.",
            "capabilities": [
                "summaries",
                "engagement_metrics",
                "search"
            ],
            "pricing_model": "freemium",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.read.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "avoma",
            "name": "Avoma",
            "url": "https://www.avoma.com/",
            "segments": [
                "meeting-intelligence"
            ],
            "description": "Conversation intelligence pour revenue teams ; coaching et playbook.",
            "capabilities": [
                "conversation_intel",
                "coaching",
                "playbooks"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.avoma.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "rpa-enterprise.json": [
        {
            "id": "uipath",
            "name": "UiPath",
            "url": "https://www.uipath.com/",
            "segments": [
                "rpa-enterprise"
            ],
            "description": "Leader RPA enterprise : robots UI, orchestration et automation platform.",
            "capabilities": [
                "rpa",
                "orchestrator",
                "process_mining",
                "document_ai"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.uipath.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "automation-anywhere",
            "name": "Automation Anywhere",
            "url": "https://www.automationanywhere.com/",
            "segments": [
                "rpa-enterprise"
            ],
            "description": "Cloud-native RPA ; bots, IQ Bot document AI et Bot Store.",
            "capabilities": [
                "rpa",
                "document_ai",
                "cloud_native"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.automationanywhere.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "blue-prism",
            "name": "Blue Prism (SS&C)",
            "url": "https://www.blueprism.com/",
            "segments": [
                "rpa-enterprise"
            ],
            "description": "RPA enterprise sécurisé ; gouvernance forte pour secteurs régulés.",
            "capabilities": [
                "rpa",
                "governance",
                "regulated_industries"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.blueprism.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "workfusion",
            "name": "WorkFusion",
            "url": "https://www.workfusion.com/",
            "segments": [
                "rpa-enterprise"
            ],
            "description": "Intelligent automation pour banking/insurance ; RPA + ML document processing.",
            "capabilities": [
                "intelligent_automation",
                "document_processing",
                "banking"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.workfusion.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "crm-platforms.json": [
        {
            "id": "salesforce-crm",
            "name": "Salesforce Sales Cloud",
            "url": "https://www.salesforce.com/products/sales-cloud/",
            "segments": [
                "crm-platforms"
            ],
            "description": "CRM leader ; pipeline, forecasting, Einstein AI et écosystème AppExchange.",
            "capabilities": [
                "pipeline",
                "forecasting",
                "einstein_ai",
                "integrations"
            ],
            "pricing_model": "hybrid",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.salesforce.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "hubspot-crm",
            "name": "HubSpot CRM",
            "url": "https://www.hubspot.com/products/crm",
            "segments": [
                "crm-platforms"
            ],
            "description": "CRM freemium + hubs marketing/sales/service ; Breeze AI agents.",
            "capabilities": [
                "crm",
                "marketing_hub",
                "ai_agents"
            ],
            "pricing_model": "freemium",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.hubspot.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "pipedrive",
            "name": "Pipedrive",
            "url": "https://www.pipedrive.com/",
            "segments": [
                "crm-platforms"
            ],
            "description": "CRM orienté ventes PME ; pipeline visuel et automations.",
            "capabilities": [
                "sales_pipeline",
                "automations",
                "reporting"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.pipedrive.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "zoho-crm",
            "name": "Zoho CRM",
            "url": "https://www.zoho.com/crm/",
            "segments": [
                "crm-platforms"
            ],
            "description": "CRM modulaire abordable ; Zia AI et suite business intégrée.",
            "capabilities": [
                "crm",
                "zia_ai",
                "suite_integration"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.zoho.com/crm/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "attio",
            "name": "Attio",
            "url": "https://attio.com/",
            "segments": [
                "crm-platforms"
            ],
            "description": "CRM flexible data-model first pour startups ; workflows et enrichissement.",
            "capabilities": [
                "flexible_data_model",
                "workflows",
                "enrichment"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://attio.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "marketing-automation.json": [
        {
            "id": "adobe-marketo",
            "name": "Adobe Marketo Engage",
            "url": "https://business.adobe.com/products/marketo.html",
            "segments": [
                "marketing-automation"
            ],
            "description": "Marketing automation B2B enterprise ; nurturing, ABM et analytics.",
            "capabilities": [
                "lead_nurturing",
                "abm",
                "scoring",
                "analytics"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://business.adobe.com/products/marketo.html",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "mailchimp",
            "name": "Mailchimp",
            "url": "https://mailchimp.com/",
            "segments": [
                "marketing-automation"
            ],
            "description": "Email marketing et automation pour PME ; audiences et parcours.",
            "capabilities": [
                "email_campaigns",
                "automations",
                "audiences"
            ],
            "pricing_model": "freemium",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://mailchimp.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "brevo",
            "name": "Brevo (ex-Sendinblue)",
            "url": "https://www.brevo.com/",
            "segments": [
                "marketing-automation"
            ],
            "description": "Marketing suite française : email, SMS, automation et CRM lite.",
            "capabilities": [
                "email",
                "sms",
                "automation",
                "crm"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "france",
            "source_url": "https://www.brevo.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "activecampaign",
            "name": "ActiveCampaign",
            "url": "https://www.activecampaign.com/",
            "segments": [
                "marketing-automation"
            ],
            "description": "Automation marketing + CRM ; email, SMS et machine learning scoring.",
            "capabilities": [
                "email_automation",
                "crm",
                "predictive_scoring"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.activecampaign.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "customer-io",
            "name": "Customer.io",
            "url": "https://customer.io/",
            "segments": [
                "marketing-automation"
            ],
            "description": "Messaging automation data-driven ; journeys basés événements produit.",
            "capabilities": [
                "event_journeys",
                "in_app",
                "email",
                "push"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://customer.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "seo-content-ai.json": [
        {
            "id": "surfer-seo",
            "name": "Surfer SEO",
            "url": "https://surferseo.com/",
            "segments": [
                "seo-content-ai"
            ],
            "description": "Optimisation contenu SEO data-driven ; briefs, éditeur et audit SERP.",
            "capabilities": [
                "content_optimization",
                "serp_analysis",
                "briefs"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://surferseo.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "clearscope",
            "name": "Clearscope",
            "url": "https://www.clearscope.io/",
            "segments": [
                "seo-content-ai"
            ],
            "description": "Recherche mots-clés et optimisation sémantique pour rédacteurs.",
            "capabilities": [
                "keyword_research",
                "content_grading",
                "semantic_seo"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.clearscope.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "writer-com",
            "name": "Writer",
            "url": "https://writer.com/",
            "segments": [
                "seo-content-ai"
            ],
            "description": "Plateforme contenu enterprise avec LLM propriétaire et brand governance.",
            "capabilities": [
                "enterprise_content",
                "brand_voice",
                "governance"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://writer.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "copy-ai",
            "name": "Copy.ai",
            "url": "https://www.copy.ai/",
            "segments": [
                "seo-content-ai"
            ],
            "description": "Génération contenu marketing et workflows GTM avec agents.",
            "capabilities": [
                "content_generation",
                "gtm_workflows",
                "agents"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.copy.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "marketmuse",
            "name": "MarketMuse",
            "url": "https://www.marketmuse.com/",
            "segments": [
                "seo-content-ai"
            ],
            "description": "Stratégie contenu IA : topic authority, briefs et planning éditorial.",
            "capabilities": [
                "topic_authority",
                "content_planning",
                "briefs"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.marketmuse.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "revenue-intelligence.json": [
        {
            "id": "gong",
            "name": "Gong",
            "url": "https://www.gong.io/",
            "segments": [
                "revenue-intelligence"
            ],
            "description": "Conversation intelligence : analyse appels, deals et coaching revenue.",
            "capabilities": [
                "call_recording",
                "deal_intelligence",
                "coaching"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.gong.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "clari",
            "name": "Clari",
            "url": "https://www.clari.com/",
            "segments": [
                "revenue-intelligence"
            ],
            "description": "Revenue platform : forecasting, pipeline inspection et RevAI.",
            "capabilities": [
                "forecasting",
                "pipeline_analytics",
                "rev_ai"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.clari.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "chorus-ai",
            "name": "Chorus.ai (ZoomInfo)",
            "url": "https://www.chorus.ai/",
            "segments": [
                "revenue-intelligence"
            ],
            "description": "Conversation analytics pour sales ; moments clés et playbook.",
            "capabilities": [
                "conversation_analytics",
                "deal_moments",
                "playbooks"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.chorus.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "people-ai",
            "name": "People.ai",
            "url": "https://people.ai/",
            "segments": [
                "revenue-intelligence"
            ],
            "description": "Activity capture et revenue operations ; données CRM auto-remplies.",
            "capabilities": [
                "activity_capture",
                "crm_hygiene",
                "revops"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://people.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "boostup-ai",
            "name": "BoostUp.ai",
            "url": "https://www.boostup.ai/",
            "segments": [
                "revenue-intelligence"
            ],
            "description": "Forecasting et intelligence pipeline multi-sources.",
            "capabilities": [
                "forecasting",
                "pipeline_health",
                "analytics"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.boostup.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "helpdesk-platforms.json": [
        {
            "id": "freshdesk",
            "name": "Freshdesk",
            "url": "https://www.freshworks.com/freshdesk/",
            "segments": [
                "helpdesk-platforms"
            ],
            "description": "Helpdesk cloud omnicanal ; ticketing, KB et Freddy AI.",
            "capabilities": [
                "ticketing",
                "omnichannel",
                "knowledge_base",
                "ai"
            ],
            "pricing_model": "freemium",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.freshworks.com/freshdesk/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "front",
            "name": "Front",
            "url": "https://front.com/",
            "segments": [
                "helpdesk-platforms"
            ],
            "description": "Inbox collaboratif équipes support et success ; workflows partagés.",
            "capabilities": [
                "shared_inbox",
                "collaboration",
                "workflows"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://front.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "help-scout",
            "name": "Help Scout",
            "url": "https://www.helpscout.com/",
            "segments": [
                "helpdesk-platforms"
            ],
            "description": "Helpdesk humain-centré PME ; docs, beacon et satisfaction.",
            "capabilities": [
                "ticketing",
                "docs",
                "customer_satisfaction"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.helpscout.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "kustomer",
            "name": "Kustomer (Meta)",
            "url": "https://www.kustomer.com/",
            "segments": [
                "helpdesk-platforms"
            ],
            "description": "CRM service-first ; timeline client unifiée et AI agents.",
            "capabilities": [
                "crm_service",
                "unified_timeline",
                "ai_agents"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.kustomer.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "customer-success.json": [
        {
            "id": "gainsight",
            "name": "Gainsight",
            "url": "https://www.gainsight.com/",
            "segments": [
                "customer-success"
            ],
            "description": "Customer success platform leader ; health scores, playbooks et PX.",
            "capabilities": [
                "health_scores",
                "playbooks",
                "nps",
                "renewals"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.gainsight.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "totango",
            "name": "Totango",
            "url": "https://www.totango.com/",
            "segments": [
                "customer-success"
            ],
            "description": "CS platform modulaire ; journeys, segmentation et AI insights.",
            "capabilities": [
                "customer_journeys",
                "segmentation",
                "ai_insights"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.totango.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "churnzero",
            "name": "ChurnZero",
            "url": "https://churnzero.com/",
            "segments": [
                "customer-success"
            ],
            "description": "Real-time CS automation ; in-app guides et alertes churn.",
            "capabilities": [
                "real_time_alerts",
                "in_app",
                "churn_prevention"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://churnzero.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "catalyst",
            "name": "Catalyst",
            "url": "https://www.catalyst.io/",
            "segments": [
                "customer-success"
            ],
            "description": "Hub données customer success ; health, stakeholders et intégrations.",
            "capabilities": [
                "cs_data_hub",
                "health",
                "stakeholder_mapping"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.catalyst.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "planhat",
            "name": "Planhat",
            "url": "https://www.planhat.com/",
            "segments": [
                "customer-success"
            ],
            "description": "Revenue success platform ; CS, expansion et workflows no-code.",
            "capabilities": [
                "revenue_success",
                "workflows",
                "expansion"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.planhat.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "treasury-fpa.json": [
        {
            "id": "anaplan",
            "name": "Anaplan",
            "url": "https://www.anaplan.com/",
            "segments": [
                "treasury-fpa"
            ],
            "description": "Connected planning enterprise ; FP&A, supply chain et workforce.",
            "capabilities": [
                "fp_and_a",
                "scenario_planning",
                "connected_planning"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.anaplan.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "pigment",
            "name": "Pigment",
            "url": "https://www.pigment.com/",
            "segments": [
                "treasury-fpa"
            ],
            "description": "FP&A moderne ; modélisation collaborative et intégrations données.",
            "capabilities": [
                "fp_and_a",
                "modeling",
                "collaboration"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.pigment.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "drivetrain",
            "name": "Drivetrain",
            "url": "https://www.drivetrain.ai/",
            "segments": [
                "treasury-fpa"
            ],
            "description": "FP&A agentic : planification, variance analysis et reporting automatisé.",
            "capabilities": [
                "agentic_fp_and_a",
                "variance",
                "reporting"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.drivetrain.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "cube-software",
            "name": "Cube",
            "url": "https://www.cubesoftware.com/",
            "segments": [
                "treasury-fpa"
            ],
            "description": "FP&A pour finance teams ; Excel-native planning et consolidation.",
            "capabilities": [
                "excel_native",
                "planning",
                "consolidation"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.cubesoftware.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "mosaic-tech",
            "name": "Mosaic",
            "url": "https://www.mosaic.tech/",
            "segments": [
                "treasury-fpa"
            ],
            "description": "Strategic finance pour startups ; métriques SaaS et forecasting.",
            "capabilities": [
                "saas_metrics",
                "forecasting",
                "board_reporting"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.mosaic.tech/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "spend-procurement.json": [
        {
            "id": "coupa",
            "name": "Coupa",
            "url": "https://www.coupa.com/",
            "segments": [
                "spend-procurement"
            ],
            "description": "Business spend management : procurement, invoicing et supply chain.",
            "capabilities": [
                "procurement",
                "invoicing",
                "supplier_management"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.coupa.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "zip",
            "name": "Zip",
            "url": "https://ziphq.com/",
            "segments": [
                "spend-procurement"
            ],
            "description": "Intake-to-procure moderne ; workflows achats et intégrations ERP.",
            "capabilities": [
                "intake_to_procure",
                "workflows",
                "erp_integration"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://ziphq.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "procurify",
            "name": "Procurify",
            "url": "https://www.procurify.com/",
            "segments": [
                "spend-procurement"
            ],
            "description": "Spend management mid-market ; PO, approvals et budgets temps réel.",
            "capabilities": [
                "purchase_orders",
                "approvals",
                "budget_tracking"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.procurify.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "spendesk",
            "name": "Spendesk",
            "url": "https://www.spendesk.com/",
            "segments": [
                "spend-procurement"
            ],
            "description": "Spend management PME Europe ; cartes, factures et workflows.",
            "capabilities": [
                "corporate_cards",
                "invoice_management",
                "approvals"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "europe",
            "source_url": "https://www.spendesk.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "payroll-hris.json": [
        {
            "id": "workday-hcm",
            "name": "Workday HCM",
            "url": "https://www.workday.com/",
            "segments": [
                "payroll-hris"
            ],
            "description": "SIRH cloud enterprise : core HR, payroll, talent et analytics.",
            "capabilities": [
                "core_hr",
                "payroll",
                "talent",
                "analytics"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.workday.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "adp-workforce",
            "name": "ADP Workforce Now",
            "url": "https://www.adp.com/",
            "segments": [
                "payroll-hris"
            ],
            "description": "Paie et HRIS global ; compliance locale et self-service employés.",
            "capabilities": [
                "payroll",
                "hris",
                "compliance",
                "self_service"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.adp.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "rippling",
            "name": "Rippling",
            "url": "https://www.rippling.com/",
            "segments": [
                "payroll-hris"
            ],
            "description": "Workforce platform unifiée : HR, IT, payroll et apps en un système.",
            "capabilities": [
                "hris",
                "payroll",
                "it_management",
                "apps"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.rippling.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "payfit",
            "name": "PayFit",
            "url": "https://payfit.com/",
            "segments": [
                "payroll-hris"
            ],
            "description": "Paie et RH automatisées pour PME ; forte présence France/Europe.",
            "capabilities": [
                "payroll",
                "leave_management",
                "hr_admin"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "france",
            "source_url": "https://payfit.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "personio",
            "name": "Personio",
            "url": "https://www.personio.com/",
            "segments": [
                "payroll-hris"
            ],
            "description": "HR software européen PME : recrutement, onboarding, payroll partenaires.",
            "capabilities": [
                "hris",
                "recruiting",
                "onboarding"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "europe",
            "source_url": "https://www.personio.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "learning-lxp.json": [
        {
            "id": "docebo",
            "name": "Docebo",
            "url": "https://www.docebo.com/",
            "segments": [
                "learning-lxp"
            ],
            "description": "LMS/LXP AI-powered ; learning suite enterprise et marketplace contenus.",
            "capabilities": [
                "lms",
                "lxp",
                "ai_learning",
                "content_marketplace"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.docebo.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "360learning",
            "name": "360Learning",
            "url": "https://360learning.com/",
            "segments": [
                "learning-lxp"
            ],
            "description": "Collaborative learning platform ; création pair-à-pair et LXP.",
            "capabilities": [
                "collaborative_learning",
                "lxp",
                "authoring"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://360learning.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "cornerstone",
            "name": "Cornerstone OnDemand",
            "url": "https://www.cornerstoneondemand.com/",
            "segments": [
                "learning-lxp"
            ],
            "description": "Talent experience suite : learning, performance et succession.",
            "capabilities": [
                "lms",
                "performance",
                "succession"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.cornerstoneondemand.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "degreed",
            "name": "Degreed",
            "url": "https://degreed.com/",
            "segments": [
                "learning-lxp"
            ],
            "description": "Upskilling platform ; agrégation contenus et skills intelligence.",
            "capabilities": [
                "upskilling",
                "skills_intelligence",
                "content_aggregation"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://degreed.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "absorb-lms",
            "name": "Absorb LMS",
            "url": "https://www.absorblms.com/",
            "segments": [
                "learning-lxp"
            ],
            "description": "LMS cloud mid-market ; SCORM, mobile et reporting.",
            "capabilities": [
                "lms",
                "scorm",
                "mobile_learning"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.absorblms.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "healthcare-clinical-ai.json": [
        {
            "id": "nuance-dax",
            "name": "Nuance DAX Copilot",
            "url": "https://www.nuance.com/healthcare/dax-copilot.html",
            "segments": [
                "healthcare-clinical-ai"
            ],
            "description": "Documentation clinique ambient AI ; notes SOAP auto-générées depuis consultation.",
            "capabilities": [
                "ambient_documentation",
                "clinical_notes",
                "ehr_integration"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.nuance.com/healthcare/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "abridge",
            "name": "Abridge",
            "url": "https://www.abridge.com/",
            "segments": [
                "healthcare-clinical-ai"
            ],
            "description": "AI medical scribe ; transcription consultation et structuration EHR.",
            "capabilities": [
                "medical_scribe",
                "transcription",
                "ehr"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.abridge.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "ambience-healthcare",
            "name": "Ambience Healthcare",
            "url": "https://www.ambiencehealthcare.com/",
            "segments": [
                "healthcare-clinical-ai"
            ],
            "description": "AI operating system clinique ; documentation, coding et workflows.",
            "capabilities": [
                "clinical_documentation",
                "medical_coding",
                "workflows"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.ambiencehealthcare.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "suki-ai",
            "name": "Suki AI",
            "url": "https://www.suki.ai/",
            "segments": [
                "healthcare-clinical-ai"
            ],
            "description": "Voice assistant médecins ; commandes vocales et notes cliniques.",
            "capabilities": [
                "voice_assistant",
                "clinical_notes",
                "commands"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.suki.ai/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "nabla-copilot",
            "name": "Nabla Copilot",
            "url": "https://www.nabla.com/",
            "segments": [
                "healthcare-clinical-ai"
            ],
            "description": "Copilot clinique français ; génération comptes-rendus et structuration.",
            "capabilities": [
                "clinical_copilot",
                "consultation_notes",
                "france"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.nabla.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "health-data-analytics.json": [
        {
            "id": "flatiron-health",
            "name": "Flatiron Health",
            "url": "https://flatiron.com/",
            "segments": [
                "health-data-analytics"
            ],
            "description": "Oncology real-world data ; registres patients et analytics recherche.",
            "capabilities": [
                "real_world_data",
                "oncology",
                "research_analytics"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://flatiron.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "komodo-health",
            "name": "Komodo Health",
            "url": "https://www.komodohealth.com/",
            "segments": [
                "health-data-analytics"
            ],
            "description": "Healthcare Map ; analytics population et parcours patients US.",
            "capabilities": [
                "healthcare_map",
                "patient_journeys",
                "analytics"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.komodohealth.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "tempus",
            "name": "Tempus",
            "url": "https://www.tempus.com/",
            "segments": [
                "health-data-analytics"
            ],
            "description": "Precision medicine ; données moléculaires/cliniques et IA décisionnelle.",
            "capabilities": [
                "precision_medicine",
                "genomics",
                "clinical_ai"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.tempus.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "truveta",
            "name": "Truveta",
            "url": "https://www.truveta.com/",
            "segments": [
                "health-data-analytics"
            ],
            "description": "Consortium données santé dé-identifiées ; recherche et insights population.",
            "capabilities": [
                "de_identified_data",
                "research",
                "population_insights"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.truveta.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "health-catalyst",
            "name": "Health Catalyst",
            "url": "https://www.healthcatalyst.com/",
            "segments": [
                "health-data-analytics"
            ],
            "description": "Healthcare analytics et data platform ; qualité, coûts et outcomes.",
            "capabilities": [
                "healthcare_analytics",
                "quality_metrics",
                "data_platform"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.healthcatalyst.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "real-estate-proptech.json": [
        {
            "id": "costar",
            "name": "CoStar",
            "url": "https://www.costar.com/",
            "segments": [
                "real-estate-proptech"
            ],
            "description": "Données et analytics immobilier commercial ; listings et market intelligence.",
            "capabilities": [
                "commercial_data",
                "listings",
                "market_analytics"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.costar.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "yardi",
            "name": "Yardi",
            "url": "https://www.yardi.com/",
            "segments": [
                "real-estate-proptech"
            ],
            "description": "Property management software ; accounting, leasing et operations.",
            "capabilities": [
                "property_management",
                "accounting",
                "leasing"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.yardi.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "procore",
            "name": "Procore",
            "url": "https://www.procore.com/",
            "segments": [
                "real-estate-proptech"
            ],
            "description": "Construction management cloud ; projets, qualité et financials.",
            "capabilities": [
                "construction_pm",
                "quality",
                "financials"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.procore.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "matera",
            "name": "Matera",
            "url": "https://www.matera.eu/",
            "segments": [
                "real-estate-proptech"
            ],
            "description": "Gestion copropriétés et syndic digital ; France.",
            "capabilities": [
                "copropriete",
                "syndic",
                "france"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "france",
            "source_url": "https://www.matera.eu/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "pricehubble",
            "name": "PriceHubble",
            "url": "https://www.pricehubble.com/",
            "segments": [
                "real-estate-proptech"
            ],
            "description": "Analytics et estimation immobilière ; AVM et insights marché.",
            "capabilities": [
                "avm",
                "market_insights",
                "portfolio_analytics"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "europe",
            "source_url": "https://www.pricehubble.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "insurance-insurtech.json": [
        {
            "id": "guidewire",
            "name": "Guidewire",
            "url": "https://www.guidewire.com/",
            "segments": [
                "insurance-insurtech"
            ],
            "description": "Suite core insurance P&C ; policy, billing et claims cloud.",
            "capabilities": [
                "policy_admin",
                "billing",
                "claims"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.guidewire.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "duck-creek",
            "name": "Duck Creek Technologies",
            "url": "https://www.duckcreek.com/",
            "segments": [
                "insurance-insurtech"
            ],
            "description": "Insurance platform SaaS ; underwriting, policy et distribution.",
            "capabilities": [
                "underwriting",
                "policy",
                "distribution"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.duckcreek.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "lemonade",
            "name": "Lemonade",
            "url": "https://www.lemonade.com/",
            "segments": [
                "insurance-insurtech"
            ],
            "description": "Assureur digital AI-first ; souscription instantanée et sinistres automatisés.",
            "capabilities": [
                "ai_underwriting",
                "instant_quote",
                "claims_automation"
            ],
            "pricing_model": "hybrid",
            "target_market": "self_serve",
            "geography": "global",
            "source_url": "https://www.lemonade.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "coalition",
            "name": "Coalition",
            "url": "https://www.coalitioninc.com/",
            "segments": [
                "insurance-insurtech"
            ],
            "description": "Cyber insurance + security ; underwriting basé posture sécurité.",
            "capabilities": [
                "cyber_insurance",
                "security_scanning",
                "underwriting"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.coalitioninc.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "shift-technology",
            "name": "Shift Technology",
            "url": "https://www.shift-technology.com/",
            "segments": [
                "insurance-insurtech"
            ],
            "description": "AI claims automation et fraud detection pour assureurs.",
            "capabilities": [
                "claims_automation",
                "fraud_detection",
                "ai"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "france",
            "source_url": "https://www.shift-technology.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "construction-proptech.json": [
        {
            "id": "autodesk-construction-cloud",
            "name": "Autodesk Construction Cloud",
            "url": "https://construction.autodesk.com/",
            "segments": [
                "construction-proptech"
            ],
            "description": "BIM et collaboration chantier ; docs, issues et field management.",
            "capabilities": [
                "bim",
                "document_management",
                "field"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://construction.autodesk.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "fieldwire",
            "name": "Fieldwire",
            "url": "https://www.fieldwire.com/",
            "segments": [
                "construction-proptech"
            ],
            "description": "Gestion chantier mobile ; plans, tâches et rapports terrain.",
            "capabilities": [
                "field_management",
                "plans",
                "task_tracking"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.fieldwire.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "buildertrend",
            "name": "Buildertrend",
            "url": "https://buildertrend.com/",
            "segments": [
                "construction-proptech"
            ],
            "description": "Construction PM résidentiel ; CRM, scheduling et client portal.",
            "capabilities": [
                "residential_pm",
                "scheduling",
                "client_portal"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://buildertrend.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "planradar",
            "name": "PlanRadar",
            "url": "https://www.planradar.com/",
            "segments": [
                "construction-proptech"
            ],
            "description": "Documentation défauts et QA/QC chantier ; plans et rapports.",
            "capabilities": [
                "defect_tracking",
                "qa_qc",
                "reporting"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "europe",
            "source_url": "https://www.planradar.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "alice-technologies",
            "name": "ALICE Technologies",
            "url": "https://www.alicetechnologies.com/",
            "segments": [
                "construction-proptech"
            ],
            "description": "Scheduling construction AI ; simulation et optimisation planning.",
            "capabilities": [
                "ai_scheduling",
                "simulation",
                "optimization"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.alicetechnologies.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "supply-chain-logistics.json": [
        {
            "id": "flexport",
            "name": "Flexport",
            "url": "https://www.flexport.com/",
            "segments": [
                "supply-chain-logistics"
            ],
            "description": "Freight forwarding digital ; booking, customs et visibilité supply chain.",
            "capabilities": [
                "freight",
                "customs",
                "visibility"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.flexport.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "project44",
            "name": "project44",
            "url": "https://www.project44.com/",
            "segments": [
                "supply-chain-logistics"
            ],
            "description": "Supply chain visibility ; tracking temps réel multi-modal.",
            "capabilities": [
                "real_time_tracking",
                "visibility",
                "analytics"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.project44.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "fourkites",
            "name": "FourKites",
            "url": "https://www.fourkites.com/",
            "segments": [
                "supply-chain-logistics"
            ],
            "description": "Real-time transportation visibility ; ETA prediction et exceptions.",
            "capabilities": [
                "transport_visibility",
                "eta_prediction",
                "exceptions"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.fourkites.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "shipbob",
            "name": "ShipBob",
            "url": "https://www.shipbob.com/",
            "segments": [
                "supply-chain-logistics"
            ],
            "description": "3PL e-commerce fulfillment ; warehousing et shipping multi-canal.",
            "capabilities": [
                "fulfillment",
                "warehousing",
                "ecommerce"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.shipbob.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "kinaxis",
            "name": "Kinaxis",
            "url": "https://www.kinaxis.com/",
            "segments": [
                "supply-chain-logistics"
            ],
            "description": "Supply chain planning concurrent ; demand, inventory et S&OP.",
            "capabilities": [
                "demand_planning",
                "inventory",
                "s_and_op"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.kinaxis.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "retail-ecommerce-ai.json": [
        {
            "id": "shopify",
            "name": "Shopify",
            "url": "https://www.shopify.com/",
            "segments": [
                "retail-ecommerce-ai"
            ],
            "description": "Commerce platform ; storefront, payments et Shopify Magic AI.",
            "capabilities": [
                "ecommerce",
                "payments",
                "shopify_magic"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "global",
            "source_url": "https://www.shopify.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "dynamic-yield",
            "name": "Dynamic Yield (Mastercard)",
            "url": "https://www.dynamicyield.com/",
            "segments": [
                "retail-ecommerce-ai"
            ],
            "description": "Personalization platform ; recommandations, A/B et merchandising.",
            "capabilities": [
                "personalization",
                "recommendations",
                "ab_testing"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.dynamicyield.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "bloomreach",
            "name": "Bloomreach",
            "url": "https://www.bloomreach.com/",
            "segments": [
                "retail-ecommerce-ai"
            ],
            "description": "Commerce experience cloud ; search, merchandising et marketing AI.",
            "capabilities": [
                "search",
                "merchandising",
                "marketing_ai"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.bloomreach.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "nosto",
            "name": "Nosto",
            "url": "https://www.nosto.com/",
            "segments": [
                "retail-ecommerce-ai"
            ],
            "description": "Commerce experience personalization ; product recommendations et UGC.",
            "capabilities": [
                "product_recommendations",
                "ugc",
                "personalization"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.nosto.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "klevu",
            "name": "Klevu",
            "url": "https://www.klevu.com/",
            "segments": [
                "retail-ecommerce-ai"
            ],
            "description": "AI search et discovery e-commerce ; NLP et merchandising.",
            "capabilities": [
                "ai_search",
                "discovery",
                "nlp"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.klevu.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "energy-cleantech.json": [
        {
            "id": "enphase",
            "name": "Enphase Energy",
            "url": "https://enphase.com/",
            "segments": [
                "energy-cleantech"
            ],
            "description": "Microinverters et energy management résidentiel ; monitoring solaire.",
            "capabilities": [
                "solar_monitoring",
                "microinverters",
                "energy_management"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://enphase.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "arcadia",
            "name": "Arcadia",
            "url": "https://www.arcadia.com/",
            "segments": [
                "energy-cleantech"
            ],
            "description": "Energy data platform ; utility data, clean energy et API.",
            "capabilities": [
                "utility_data",
                "clean_energy",
                "api"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.arcadia.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "energiency",
            "name": "Energiency",
            "url": "https://energiency.com/",
            "segments": [
                "energy-cleantech"
            ],
            "description": "Performance énergétique industrielle ; analytics et ISO 50001.",
            "capabilities": [
                "energy_analytics",
                "iso_50001",
                "industrial"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://energiency.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "gridpoint",
            "name": "GridPoint",
            "url": "https://www.gridpoint.com/",
            "segments": [
                "energy-cleantech"
            ],
            "description": "Building energy management ; optimisation HVAC et éclairage.",
            "capabilities": [
                "building_ems",
                "hvac_optimization",
                "analytics"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.gridpoint.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "sphera",
            "name": "Sphera",
            "url": "https://sphera.com/",
            "segments": [
                "energy-cleantech"
            ],
            "description": "ESG performance et risk management ; sustainability et safety.",
            "capabilities": [
                "esg_reporting",
                "risk_management",
                "sustainability"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://sphera.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "bi-analytics-platforms.json": [
        {
            "id": "tableau",
            "name": "Tableau (Salesforce)",
            "url": "https://www.tableau.com/",
            "segments": [
                "bi-analytics-platforms"
            ],
            "description": "BI visuelle leader ; dashboards, prep et Einstein analytics.",
            "capabilities": [
                "visualization",
                "dashboards",
                "data_prep"
            ],
            "pricing_model": "hybrid",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.tableau.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "power-bi",
            "name": "Microsoft Power BI",
            "url": "https://powerbi.microsoft.com/",
            "segments": [
                "bi-analytics-platforms"
            ],
            "description": "Self-service BI Microsoft ; modélisation, DAX et Copilot.",
            "capabilities": [
                "self_service_bi",
                "modeling",
                "copilot"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://powerbi.microsoft.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "looker",
            "name": "Looker (Google Cloud)",
            "url": "https://cloud.google.com/looker",
            "segments": [
                "bi-analytics-platforms"
            ],
            "description": "Semantic layer BI ; LookML et embedded analytics.",
            "capabilities": [
                "semantic_layer",
                "lookml",
                "embedded"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://cloud.google.com/looker",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "thoughtspot",
            "name": "ThoughtSpot",
            "url": "https://www.thoughtspot.com/",
            "segments": [
                "bi-analytics-platforms"
            ],
            "description": "Search-driven analytics ; NLQ et Spotter AI analyst.",
            "capabilities": [
                "search_analytics",
                "nlq",
                "ai_analyst"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.thoughtspot.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "mode-analytics",
            "name": "Mode",
            "url": "https://mode.com/",
            "segments": [
                "bi-analytics-platforms"
            ],
            "description": "Analytics collaboratif ; SQL, Python/R notebooks et reporting.",
            "capabilities": [
                "sql",
                "notebooks",
                "reporting"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://mode.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "data-observability.json": [
        {
            "id": "monte-carlo",
            "name": "Monte Carlo",
            "url": "https://www.montecarlodata.com/",
            "segments": [
                "data-observability"
            ],
            "description": "Data observability leader ; incidents données, lineage et SLA monitoring.",
            "capabilities": [
                "data_incidents",
                "lineage",
                "sla_monitoring"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.montecarlodata.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "great-expectations",
            "name": "Great Expectations",
            "url": "https://greatexpectations.io/",
            "segments": [
                "data-observability"
            ],
            "description": "Framework open-source data quality ; tests, docs et checkpoints.",
            "capabilities": [
                "data_quality",
                "tests",
                "checkpoints"
            ],
            "pricing_model": "open_source",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://greatexpectations.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "soda",
            "name": "Soda",
            "url": "https://www.soda.io/",
            "segments": [
                "data-observability"
            ],
            "description": "Data quality monitoring ; checks collaboratifs et anomaly detection.",
            "capabilities": [
                "data_quality",
                "anomaly_detection",
                "collaboration"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.soda.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "acceldata",
            "name": "Acceldata",
            "url": "https://www.acceldata.io/",
            "segments": [
                "data-observability"
            ],
            "description": "Data observability platform ; pipeline, performance et reliability.",
            "capabilities": [
                "pipeline_monitoring",
                "performance",
                "reliability"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "enterprise",
            "geography": "global",
            "source_url": "https://www.acceldata.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "anomalo",
            "name": "Anomalo",
            "url": "https://www.anomalo.com/",
            "segments": [
                "data-observability"
            ],
            "description": "Automated data quality monitoring ; ML anomaly detection tables.",
            "capabilities": [
                "automated_monitoring",
                "ml_anomalies",
                "table_level"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "global",
            "source_url": "https://www.anomalo.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "civic-tech-fr.json": [
        {
            "id": "decidim",
            "name": "Decidim",
            "url": "https://decidim.org/",
            "segments": [
                "civic-tech-fr"
            ],
            "description": "Plateforme open-source participation citoyenne ; budgets participatifs, consultations.",
            "capabilities": [
                "participatory_budget",
                "consultations",
                "open_source"
            ],
            "pricing_model": "open_source",
            "target_market": "mid_market",
            "geography": "europe",
            "source_url": "https://decidim.org/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "cap-collectif",
            "name": "Cap Collectif",
            "url": "https://cap-collectif.com/",
            "segments": [
                "civic-tech-fr"
            ],
            "description": "Plateforme concertation citoyenne française ; consultations et cartes participatives.",
            "capabilities": [
                "consultation",
                "participatory_mapping",
                "france"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://cap-collectif.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "make-org",
            "name": "Make.org",
            "url": "https://make.org/",
            "segments": [
                "civic-tech-fr"
            ],
            "description": "Mobilisation citoyenne à grande échelle ; consultations et baromètres.",
            "capabilities": [
                "citizen_mobilization",
                "surveys",
                "france"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://make.org/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "open-source-politics",
            "name": "Open Source Politics",
            "url": "https://opensourcepolitics.eu/",
            "segments": [
                "civic-tech-fr"
            ],
            "description": "Intégrateur Decidim et civic tech ; déploiement participation numérique.",
            "capabilities": [
                "decidim_integration",
                "civic_platforms",
                "france"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://opensourcepolitics.eu/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "respublica",
            "name": "République & Canton de Genève — outils (ref civic)",
            "url": "https://www.republique-et-canton-de-geneve.ch/",
            "segments": [
                "civic-tech-fr"
            ],
            "description": "Écosystème civic tech européen ; référence méthodologique participation (comparatif FR).",
            "capabilities": [
                "participation",
                "methodology",
                "europe"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "europe",
            "source_url": "https://cap-collectif.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial",
            "notes": "Référence comparative ; acteur FR principal = Cap Collectif."
        }
    ],
    "geospatial-gis-fr.json": [
        {
            "id": "geofoncier",
            "name": "Géofoncier",
            "url": "https://www.geofoncier.fr/",
            "segments": [
                "geospatial-gis-fr"
            ],
            "description": "Portail géomatique notaires ; fonds cadastraux et documents fonciers FR.",
            "capabilities": [
                "cadastre",
                "fonds_fonciers",
                "notaires"
            ],
            "pricing_model": "hybrid",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.geofoncier.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "alkante",
            "name": "Alkante",
            "url": "https://www.alkante.com/",
            "segments": [
                "geospatial-gis-fr"
            ],
            "description": "Éditeur SIG français ; solutions territoriales et open data géographique.",
            "capabilities": [
                "sig",
                "territorial",
                "open_data_geo"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.alkante.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "ign-geoservices",
            "name": "IGN Géoservices",
            "url": "https://geoservices.ign.fr/",
            "segments": [
                "geospatial-gis-fr"
            ],
            "description": "Services géographiques officiels ; APIs carto, BD TOPO, orthophotos.",
            "capabilities": [
                "geoportail",
                "api_carto",
                "bd_topo"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://geoservices.ign.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "cartelie",
            "name": "Cartélie (IGN)",
            "url": "https://cartelie.enregistrement.developpement-durable.gouv.fr/",
            "segments": [
                "geospatial-gis-fr"
            ],
            "description": "Catalogue métadonnées géographiques administration française.",
            "capabilities": [
                "metadata_catalog",
                "gpu",
                "admin_geo"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://cartelie.enregistrement.developpement-durable.gouv.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "opendatasoft-geo",
            "name": "Opendatasoft",
            "url": "https://www.opendatasoft.com/",
            "segments": [
                "geospatial-gis-fr"
            ],
            "description": "Plateforme open data avec cartographie ; portails territoires FR.",
            "capabilities": [
                "open_data_portal",
                "mapping",
                "api"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.opendatasoft.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "transport-mobility-data-fr.json": [
        {
            "id": "iv-mobilites",
            "name": "Île-de-France Mobilités — open data",
            "url": "https://prim.iledefrance-mobilites.fr/",
            "segments": [
                "transport-mobility-data-fr"
            ],
            "description": "Portail open data transport IDF ; GTFS temps réel, horaires, perturbations.",
            "capabilities": [
                "gtfs_rt",
                "open_data",
                "idf"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://prim.iledefrance-mobilites.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "cityway",
            "name": "Cityway",
            "url": "https://www.cityway.io/",
            "segments": [
                "transport-mobility-data-fr"
            ],
            "description": "MaaS et données mobilité ; apps transport et APIs territoires.",
            "capabilities": [
                "maas",
                "mobility_data",
                "api"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.cityway.io/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "transport-data-gouv",
            "name": "transport.data.gouv.fr",
            "url": "https://transport.data.gouv.fr/",
            "segments": [
                "transport-mobility-data-fr"
            ],
            "description": "National access point données transport ; GTFS, GBFS, statistiques.",
            "capabilities": [
                "gtfs",
                "gbfs",
                "national_catalog"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://transport.data.gouv.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "padam-mobility",
            "name": "Padam Mobility",
            "url": "https://www.padam-mobility.com/",
            "segments": [
                "transport-mobility-data-fr"
            ],
            "description": "Mobilité demand-responsive ; optimisation flotte et données territoire.",
            "capabilities": [
                "drt",
                "fleet_optimization",
                "territory"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.padam-mobility.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "hove",
            "name": "Hove (ex-Deliveroo data ref mobility analytics)",
            "url": "https://www.hove.fr/",
            "segments": [
                "transport-mobility-data-fr"
            ],
            "description": "Analytics mobilité et données flux urbains pour collectivités françaises.",
            "capabilities": [
                "urban_mobility",
                "analytics",
                "collectivites"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.hove.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "energy-buildings-fr.json": [
        {
            "id": "openmeti",
            "name": "OpenMéti",
            "url": "https://www.openmeti.fr/",
            "segments": [
                "energy-buildings-fr"
            ],
            "description": "Plateforme open data énergie bâtiments ; DPE et rénovation.",
            "capabilities": [
                "dpe",
                "renovation",
                "open_data"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.openmeti.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "ademe-data",
            "name": "ADEME — data services",
            "url": "https://data.ademe.fr/",
            "segments": [
                "energy-buildings-fr"
            ],
            "description": "Portail open data transition écologique ; DPE, émissions, rénovation.",
            "capabilities": [
                "dpe_data",
                "emissions",
                "renovation"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://data.ademe.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "effy-pro",
            "name": "Effy Pro",
            "url": "https://www.effy.fr/pro",
            "segments": [
                "energy-buildings-fr"
            ],
            "description": "Solutions rénovation énergétique pro ; données DPE et accompagnement.",
            "capabilities": [
                "renovation",
                "dpe",
                "b2b"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "france",
            "source_url": "https://www.effy.fr/pro",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "hub-anah",
            "name": "Anah — Hub rénovation",
            "url": "https://www.anah.fr/",
            "segments": [
                "energy-buildings-fr"
            ],
            "description": "Agence nationale habitat ; données aides et politiques rénovation.",
            "capabilities": [
                "renovation_policy",
                "subsidies",
                "habitat"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.anah.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "heero",
            "name": "Heero",
            "url": "https://www.heero.fr/",
            "segments": [
                "energy-buildings-fr"
            ],
            "description": "Financement et données rénovation résidentielle ; lien DPE et travaux.",
            "capabilities": [
                "renovation_financing",
                "dpe",
                "travaux"
            ],
            "pricing_model": "hybrid",
            "target_market": "smb",
            "geography": "france",
            "source_url": "https://www.heero.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "environmental-data-fr.json": [
        {
            "id": "atmo-france",
            "name": "Atmo France",
            "url": "https://www.atmo-france.org/",
            "segments": [
                "environmental-data-fr"
            ],
            "description": "Réseau surveillance qualité air ; open data indices et cartes polluants.",
            "capabilities": [
                "air_quality",
                "open_data",
                "indices"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.atmo-france.org/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "hub-eau",
            "name": "Hub'Eau",
            "url": "https://hub-eau.fr/",
            "segments": [
                "environmental-data-fr"
            ],
            "description": "APIs open data eau françaises ; hydrométrie, qualité, biodiversité.",
            "capabilities": [
                "water_api",
                "hydrometry",
                "open_data"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://hub-eau.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "inpn",
            "name": "INPN (OFB)",
            "url": "https://inpn.mnhn.fr/",
            "segments": [
                "environmental-data-fr"
            ],
            "description": "Inventaire national patrimoine naturel ; espèces, habitats, données biodiversité.",
            "capabilities": [
                "biodiversity",
                "species",
                "habitats"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://inpn.mnhn.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "brgm-infoterre",
            "name": "BRGM InfoTerre",
            "url": "https://infoterre.brgm.fr/",
            "segments": [
                "environmental-data-fr"
            ],
            "description": "Données géologiques et risques ; minéraux, eaux souterraines, aléas.",
            "capabilities": [
                "geology",
                "groundwater",
                "hazards"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://infoterre.brgm.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "georisques-api",
            "name": "Géorisques",
            "url": "https://www.georisques.gouv.fr/",
            "segments": [
                "environmental-data-fr"
            ],
            "description": "Portail risques naturels et technologiques ; API et rapports par parcelle.",
            "capabilities": [
                "natural_risks",
                "technological_risks",
                "parcel_reports"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.georisques.gouv.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "electoral-data-fr.json": [
        {
            "id": "data-gouv-elections",
            "name": "data.gouv.fr — élections",
            "url": "https://www.data.gouv.fr/fr/pages/donnees-elections/",
            "segments": [
                "electoral-data-fr"
            ],
            "description": "Catalogue jeux de données électorales ; résultats, candidats, géographie.",
            "capabilities": [
                "election_results",
                "catalog",
                "open_data"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.data.gouv.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "registre-perma",
            "name": "Registre des représentants d'intérêts (ref transparence)",
            "url": "https://www.hatvp.fr/",
            "segments": [
                "electoral-data-fr"
            ],
            "description": "Données transparence vie publique ; croisement intérêts et mandats.",
            "capabilities": [
                "transparency",
                "public_life",
                "open_data"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.hatvp.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "contexte",
            "name": "Contexte",
            "url": "https://www.contexte.com/",
            "segments": [
                "electoral-data-fr"
            ],
            "description": "Intelligence politique française ; veille institutions et analyse territoriale.",
            "capabilities": [
                "political_intelligence",
                "policy_monitoring",
                "france"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.contexte.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "regards-citoyens",
            "name": "Regards Citoyens",
            "url": "https://www.regardscitoyens.org/",
            "segments": [
                "electoral-data-fr"
            ],
            "description": "Association open data parlementaire ; NosDéputés, NosSénateurs.",
            "capabilities": [
                "parliamentary_data",
                "open_data",
                "civic"
            ],
            "pricing_model": "open_source",
            "target_market": "self_serve",
            "geography": "france",
            "source_url": "https://www.regardscitoyens.org/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "poligma",
            "name": "Poligma",
            "url": "https://poligma.com/",
            "segments": [
                "electoral-data-fr"
            ],
            "description": "Cartographie et analytics électoraux pour médias et collectivités.",
            "capabilities": [
                "electoral_maps",
                "analytics",
                "territory"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://poligma.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "public-health-territory-fr.json": [
        {
            "id": "ameli-open-data",
            "name": "Assurance Maladie — open data",
            "url": "https://data.ameli.fr/",
            "segments": [
                "public-health-territory-fr"
            ],
            "description": "Données santé publique ; démographie médicale, prescriptions, parcours.",
            "capabilities": [
                "health_open_data",
                "medical_demography",
                "prescriptions"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://data.ameli.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "santepubliquefrance",
            "name": "Santé publique France — data",
            "url": "https://www.santepubliquefrance.fr/donnees",
            "segments": [
                "public-health-territory-fr"
            ],
            "description": "Données épidémiologie et prévention ; indicateurs territoriaux santé.",
            "capabilities": [
                "epidemiology",
                "prevention",
                "territorial_indicators"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.santepubliquefrance.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "keldoc",
            "name": "KelDoc",
            "url": "https://www.keldoc.com/",
            "segments": [
                "public-health-territory-fr"
            ],
            "description": "Prise de RDV santé ; données disponibilité professionnels par territoire.",
            "capabilities": [
                "appointment_booking",
                "availability",
                "territory"
            ],
            "pricing_model": "freemium",
            "target_market": "self_serve",
            "geography": "france",
            "source_url": "https://www.keldoc.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "doctolib",
            "name": "Doctolib",
            "url": "https://www.doctolib.fr/",
            "segments": [
                "public-health-territory-fr"
            ],
            "description": "Plateforme santé ; données indirectes déserts médicaux via disponibilité.",
            "capabilities": [
                "booking",
                "telehealth",
                "territory_signals"
            ],
            "pricing_model": "freemium",
            "target_market": "self_serve",
            "geography": "france",
            "source_url": "https://www.doctolib.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "drees",
            "name": "DREES",
            "url": "https://www.drees.solidarites-sante.gouv.fr/",
            "segments": [
                "public-health-territory-fr"
            ],
            "description": "Statistiques ministère Santé ; études territoires, offre de soins.",
            "capabilities": [
                "health_statistics",
                "territorial_studies",
                "open_data"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.drees.solidarites-sante.gouv.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ],
    "open-data-governance-fr.json": [
        {
            "id": "opendatasoft",
            "name": "Opendatasoft",
            "url": "https://www.opendatasoft.com/",
            "segments": [
                "open-data-governance-fr"
            ],
            "description": "Plateforme open data collectivités ; publication, qualité et API.",
            "capabilities": [
                "data_portal",
                "quality",
                "api",
                "governance"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.opendatasoft.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "etalab-data-gouv",
            "name": "Etalab / data.gouv.fr",
            "url": "https://www.data.gouv.fr/",
            "segments": [
                "open-data-governance-fr"
            ],
            "description": "Portail national open data ; schéma données, moissonnage et conformité.",
            "capabilities": [
                "national_portal",
                "harvesting",
                "schema"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.data.gouv.fr/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "fairness",
            "name": "Fairness",
            "url": "https://www.fairness.coop/",
            "segments": [
                "open-data-governance-fr"
            ],
            "description": "Coopérative open data et communs numériques ; accompagnement collectivités.",
            "capabilities": [
                "open_data_coop",
                "commons",
                "advisory"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.fairness.coop/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "toucan-toco",
            "name": "Toucan Toco",
            "url": "https://www.toucantoco.com/",
            "segments": [
                "open-data-governance-fr"
            ],
            "description": "Data storytelling pour rendre données publiques accessibles citoyens.",
            "capabilities": [
                "data_storytelling",
                "embedded_analytics",
                "citizen_facing"
            ],
            "pricing_model": "enterprise_quote",
            "target_market": "mid_market",
            "geography": "france",
            "source_url": "https://www.toucantoco.com/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        },
        {
            "id": "data-europa",
            "name": "data.europa.eu",
            "url": "https://data.europa.eu/",
            "segments": [
                "open-data-governance-fr"
            ],
            "description": "Portail européen open data ; métadonnées transfrontalières et conformité DCAT.",
            "capabilities": [
                "european_catalog",
                "dcat",
                "cross_border"
            ],
            "pricing_model": "freemium",
            "target_market": "mid_market",
            "geography": "europe",
            "source_url": "https://data.europa.eu/",
            "source_consulted_at": "2026-06-22",
            "verification_status": "partial"
        }
    ]
}

SEGMENT_PATCHES: dict[str, list[str]] = {
    "langsmith": [
        "ai-evals-testing"
    ],
    "otter-ai": [
        "meeting-intelligence"
    ],
    "notion-ai": [
        "project-work-management"
    ],
    "jasper": [
        "seo-content-ai"
    ],
    "ramp": [
        "spend-procurement"
    ],
    "microsoft-power-automate": [
        "rpa-enterprise"
    ],
    "georisques": [
        "environmental-data-fr"
    ],
    "zendesk-ai": [
        "helpdesk-platforms"
    ],
    "intercom-fin": [
        "helpdesk-platforms"
    ],
    "freshworks-freddy": [
        "helpdesk-platforms"
    ]
}


def merge() -> None:
    all_ids: set[str] = set()
    for path in sorted(VENDORS_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for v in data.get("vendors", []):
            all_ids.add(v["id"])

    added = 0
    skipped = 0
    for fname, new_vendors in ADDITIONS.items():
        path = VENDORS_DIR / fname
        data = json.loads(path.read_text(encoding="utf-8"))
        count = 0
        for v in new_vendors:
            if v["id"] in all_ids:
                print(f"skip duplicate: {v['id']}")
                skipped += 1
                continue
            data["vendors"].append(v)
            all_ids.add(v["id"])
            count += 1
            added += 1
        data["updated_at"] = TODAY
        path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"updated {fname}: +{count} vendors")

    patched = 0
    for path in sorted(VENDORS_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for v in data.get("vendors", []):
            extra = SEGMENT_PATCHES.get(v["id"], [])
            for seg in extra:
                if seg not in v["segments"]:
                    v["segments"].append(seg)
                    changed = True
                    patched += 1
        if changed:
            data["updated_at"] = TODAY
            path.write_text(
                json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            print(f"patched segments in {path.name}")

    print(f"done: +{added} vendors, {skipped} skipped, {patched} segment patches")


if __name__ == "__main__":
    merge()
