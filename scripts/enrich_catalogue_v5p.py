#!/usr/bin/env python3
"""Vague 5p — L3 long tail regtech, KYC lite fintech FR/EU, document-idp HITL."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v5p-l3-regtech-kyc-idp"


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
    "kyc-aml.json": [
        v(
            "didit",
            "Didit",
            "https://didit.me/",
            ["kyc-aml"],
            "KYC API fintech EU ; vérification identité, liveness et parcours onboarding embeddable.",
            ["identity_verification", "liveness", "api", "onboarding"],
            "per_usage",
            "mid_market",
            "https://didit.me/",
            "g2",
            hq="ES",
            fr="partial",
            regions=["ES", "EU"],
            geo="europe",
        ),
        v(
            "lemonway-kyc",
            "Lemonway KYC",
            "https://www.lemonway.com/",
            ["kyc-aml"],
            "PSP FR ; module KYC/KYB intégré onboarding wallet et paiements régulés DSP2.",
            ["kyc_kyb", "wallet_onboarding", "psp", "eu_regulated"],
            "hybrid",
            "mid_market",
            "https://www.lemonway.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
            notes="KYC lite fintech FR — écosystème paiement Lemonway.",
        ),
        v(
            "treezor",
            "Treezor",
            "https://www.treezor.com/",
            ["kyc-aml"],
            "Banking-as-a-Service FR ; KYC/KYB natif pour émission cartes et comptes embedded finance.",
            ["baas", "kyc_kyb", "card_issuing", "embedded_finance"],
            "enterprise_quote",
            "mid_market",
            "https://www.treezor.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "mangopay-kyc",
            "MangoPay KYC",
            "https://mangopay.com/",
            ["kyc-aml"],
            "Marketplace payments EU ; workflows KYC vendeurs/acheteurs et conformité AML marketplace.",
            ["marketplace_kyc", "seller_onboarding", "aml", "eu_psp"],
            "hybrid",
            "mid_market",
            "https://mangopay.com/",
            "g2",
            hq="LU",
            fr="partial",
            regions=["LU", "EU", "FR"],
            geo="europe",
        ),
        v(
            "fourthline",
            "Fourthline",
            "https://fourthline.com/",
            ["kyc-aml"],
            "Identity verification EU ; onboarding bancaire, vidéo-ID et screening AML intégré.",
            ["banking_kyc", "video_identification", "aml_screening", "eu_compliance"],
            "enterprise_quote",
            "enterprise",
            "https://fourthline.com/",
            "g2",
            hq="NL",
            fr="partial",
            regions=["NL", "EU"],
            geo="europe",
        ),
        v(
            "flagright",
            "Flagright",
            "https://www.flagright.com/",
            ["kyc-aml", "regtech"],
            "AML transaction monitoring fintech ; règles temps réel, sanctions et case management API-first.",
            ["transaction_monitoring", "sanctions", "case_management", "api"],
            "hybrid",
            "mid_market",
            "https://www.flagright.com/",
            "crunchbase",
            hq="US",
            fr="partial",
        ),
        v(
            "checkin-com",
            "Checkin.com",
            "https://checkin.com/",
            ["kyc-aml"],
            "Identity verification hospitality/travel ; scan ID, face match et conformité sectorielle.",
            ["hospitality_kyc", "id_scan", "face_match", "sector_compliance"],
            "hybrid",
            "mid_market",
            "https://checkin.com/",
            "g2",
            hq="ES",
            fr="partial",
            regions=["ES", "EU"],
            geo="europe",
        ),
        v(
            "shufti-pro",
            "Shufti Pro",
            "https://shuftipro.com/",
            ["kyc-aml"],
            "KYC/KYB global ; vérification documentaire, biométrie, screening et due diligence.",
            ["kyc_kyb", "document_verification", "biometric", "screening"],
            "per_usage",
            "mid_market",
            "https://shuftipro.com/",
            "g2",
            hq="GB",
            fr="partial",
            regions=["GB", "EU", "US"],
        ),
        v(
            "ondorse",
            "Ondorse",
            "https://www.ondorse.co/",
            ["kyc-aml"],
            "KYB/KYC no-code FR ; collecte dossiers, vérifications automatisées et portail conformité PME.",
            ["kyb", "kyc", "no_code", "compliance_portal"],
            "hybrid",
            "smb",
            "https://www.ondorse.co/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
            notes="Concurrent Dotfile — niche KYC lite fintech FR.",
        ),
        v(
            "ariadnext",
            "ARIADNEXT (IDnow Group)",
            "https://www.ariadnext.com/",
            ["kyc-aml"],
            "Vérification documentaire FR ; OCR pièces d'identité, contrôle authenticité et API KYC.",
            ["document_verification", "id_ocr", "authenticity_check", "kyc_api"],
            "hybrid",
            "mid_market",
            "https://www.ariadnext.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "passfort",
            "PassFort (LexisNexis Risk)",
            "https://www.passfort.com/",
            ["kyc-aml"],
            "Orchestration KYC/KYB ; workflows conformité, screening et due diligence multi-juridictions.",
            ["kyc_orchestration", "kyb", "screening", "workflow"],
            "enterprise_quote",
            "enterprise",
            "https://www.passfort.com/",
            "g2",
            hq="GB",
            fr="partial",
            regions=["GB", "EU", "US"],
        ),
        v(
            "stripe-identity",
            "Stripe Identity",
            "https://stripe.com/identity",
            ["kyc-aml"],
            "Vérification identité API Stripe ; documents, selfie liveness et intégration paiements.",
            ["identity_api", "document_check", "selfie_liveness", "stripe_integration"],
            "per_usage",
            "mid_market",
            "https://stripe.com/identity",
            "official_site",
            hq="US",
            fr="partial",
        ),
    ],
    "regtech.json": [
        v(
            "behavox",
            "Behavox",
            "https://www.behavox.com/",
            ["regtech"],
            "Surveillance conformité communications ; NLP sur email/chat/voice pour banques et asset managers.",
            ["comms_surveillance", "nlp", "conduct_risk", "alerts"],
            "enterprise_quote",
            "enterprise",
            "https://www.behavox.com/",
            "g2",
            hq="GB",
            fr="partial",
            regions=["GB", "EU", "US"],
        ),
        v(
            "regnology",
            "Regnology",
            "https://www.regnology.net/",
            ["regtech"],
            "Reporting réglementaire EU ; collecte, validation et soumission XBRL/ISO pour banques et assureurs.",
            ["regulatory_reporting", "xbrl", "validation", "eu_supervisors"],
            "enterprise_quote",
            "enterprise",
            "https://www.regnology.net/",
            "analyst_report",
            hq="DE",
            fr="partial",
            regions=["DE", "EU"],
            geo="europe",
        ),
        v(
            "solidatus",
            "Solidatus",
            "https://www.solidatus.com/",
            ["regtech", "grc-security"],
            "Data lineage compliance ; cartographie données/règles réglementaires et traçabilité obligations.",
            ["data_lineage", "regulatory_mapping", "metadata", "impact_analysis"],
            "enterprise_quote",
            "enterprise",
            "https://www.solidatus.com/",
            "g2",
            hq="GB",
            fr="partial",
            regions=["GB", "EU", "US"],
        ),
        v(
            "lucinity",
            "Lucinity",
            "https://lucinity.com/",
            ["regtech"],
            "AML investigation IA ; copilot analystes, réduction faux positifs et workflows cas financiers.",
            ["aml_investigations", "ai_copilot", "case_management", "false_positive_reduction"],
            "enterprise_quote",
            "enterprise",
            "https://lucinity.com/",
            "crunchbase",
            hq="IS",
            fr="partial",
            regions=["IS", "EU", "US"],
        ),
        v(
            "feedzai",
            "Feedzai",
            "https://feedzai.com/",
            ["regtech"],
            "Financial crime platform ; fraude temps réel, AML et conformité paiements retail/banking.",
            ["fraud_detection", "aml", "real_time_scoring", "payments"],
            "enterprise_quote",
            "enterprise",
            "https://feedzai.com/",
            "analyst_report",
            hq="PT",
            fr="partial",
            regions=["PT", "EU", "US"],
            geo="europe",
        ),
        v(
            "eventus",
            "Eventus",
            "https://eventus.com/",
            ["regtech"],
            "Trade surveillance multi-actifs ; détection manipulation marché et conformité MiFID/Dodd-Frank.",
            ["trade_surveillance", "market_abuse", "mifid", "alerts"],
            "enterprise_quote",
            "enterprise",
            "https://eventus.com/",
            "g2",
        ),
        v(
            "regtrack",
            "RegTrack",
            "https://www.regtrack.com/",
            ["regtech"],
            "Change management réglementaire ; veille multi-juridictions, impact analysis et workflows compliance.",
            ["regulatory_change", "impact_analysis", "workflows", "multi_jurisdiction"],
            "enterprise_quote",
            "enterprise",
            "https://www.regtrack.com/",
            "analyst_report",
        ),
        v(
            "apiax",
            "Apiax",
            "https://www.apiax.com/",
            ["regtech"],
            "Règles réglementaires as code ; API compliance cross-border pour fintech et banques EU/CH.",
            ["reg_rules_api", "cross_border", "embeddable_compliance", "fintech"],
            "enterprise_quote",
            "mid_market",
            "https://www.apiax.com/",
            "geo_digest",
            hq="CH",
            fr="partial",
            regions=["CH", "EU"],
            geo="europe",
        ),
        v(
            "kharon",
            "Kharon",
            "https://www.kharon.com/",
            ["regtech"],
            "Intelligence sanctions et risque géopolitique ; données adverse media pour compliance export.",
            ["sanctions_intelligence", "geopolitical_risk", "adverse_media", "screening_data"],
            "enterprise_quote",
            "enterprise",
            "https://www.kharon.com/",
            "crunchbase",
        ),
        v(
            "napier",
            "Napier AI",
            "https://www.napier.ai/",
            ["regtech"],
            "AML platform IA ; screening, transaction monitoring et investigation cas pour banques EU.",
            ["aml_screening", "transaction_monitoring", "ai", "case_investigation"],
            "enterprise_quote",
            "enterprise",
            "https://www.napier.ai/",
            "g2",
            hq="GB",
            fr="partial",
            regions=["GB", "EU"],
        ),
        v(
            "opensee",
            "Opensee (Dauphine Software)",
            "https://opensee.io/",
            ["regtech"],
            "Analytics reporting réglementaire ; consolidation données prudential/ESG et contrôles auditables.",
            ["regulatory_reporting", "data_consolidation", "prudential", "audit_controls"],
            "enterprise_quote",
            "enterprise",
            "https://opensee.io/",
            "geo_digest",
            hq="FR",
            fr="strong",
            geo="france",
        ),
        v(
            "aveni",
            "Aveni",
            "https://www.aveni.ai/",
            ["regtech"],
            "Supervisory AI finance ; analyse conversations conseillers, détection risque conduct et conformité MiFID.",
            ["supervisory_ai", "conduct_risk", "conversation_analytics", "mifid"],
            "enterprise_quote",
            "enterprise",
            "https://www.aveni.ai/",
            "crunchbase",
            hq="GB",
            fr="partial",
            regions=["GB", "EU"],
        ),
    ],
    "document-idp.json": [
        v(
            "formx",
            "FormX.ai",
            "https://www.formx.ai/",
            ["document-idp"],
            "Extraction documentaire sans template ; OCR, classification et workflows revue humaine dossier.",
            ["no_template_extraction", "ocr", "classification", "human_review"],
            "hybrid",
            "mid_market",
            "https://www.formx.ai/",
            "g2",
            hq="HK",
            fr="partial",
            regions=["HK", "EU", "US"],
        ),
        v(
            "datasnipper",
            "DataSnipper",
            "https://www.datasnipper.com/",
            ["document-idp"],
            "Audit document intelligence ; extraction Excel/PDF, validation analyste et dossier de travail signé.",
            ["audit_extraction", "excel_integration", "human_validation", "workpaper"],
            "hybrid",
            "mid_market",
            "https://www.datasnipper.com/",
            "g2",
            hq="NL",
            fr="partial",
            regions=["NL", "EU", "US"],
        ),
        v(
            "deepopinion",
            "DeepOpinion",
            "https://www.deepopinion.ai/",
            ["document-idp"],
            "IDP européen no-code ; extraction, classification et poste validation opérateur sur files dossier.",
            ["no_code_idp", "classification", "human_validation", "workflow"],
            "hybrid",
            "mid_market",
            "https://www.deepopinion.ai/",
            "geo_digest",
            hq="DE",
            fr="partial",
            regions=["DE", "EU"],
            geo="europe",
        ),
        v(
            "stampli",
            "Stampli",
            "https://www.stampli.com/",
            ["document-idp"],
            "AP automation ; capture factures, extraction champs, approbations humaines et audit trail dossier.",
            ["invoice_capture", "field_extraction", "human_approval", "audit_trail"],
            "hybrid",
            "mid_market",
            "https://www.stampli.com/",
            "g2",
        ),
        v(
            "medius",
            "Medius",
            "https://www.medius.com/",
            ["document-idp"],
            "AP/IDP enterprise ; capture documents, matching PO et validation comptable avant export ERP.",
            ["ap_automation", "document_capture", "human_validation", "erp_export"],
            "enterprise_quote",
            "enterprise",
            "https://www.medius.com/",
            "g2",
            hq="SE",
            fr="partial",
            regions=["SE", "EU", "US"],
        ),
        v(
            "abbyy-flexicapture",
            "ABBYY FlexiCapture",
            "https://www.abbyy.com/flexicapture/",
            ["document-idp"],
            "Capture intelligente enterprise ; OCR, stations validation opérateur et export dossier validé.",
            ["intelligent_capture", "ocr", "validation_station", "export"],
            "enterprise_quote",
            "enterprise",
            "https://www.abbyy.com/flexicapture/",
            "analyst_report",
            hq="US",
            fr="partial",
            notes="Produit capture complémentaire à ABBYY Vantage déjà catalogué.",
        ),
        v(
            "amazon-a2i",
            "Amazon A2I (Augmented AI)",
            "https://aws.amazon.com/augmented-ai/",
            ["document-idp"],
            "Human-in-the-loop AWS ; revue humaine sur prédictions Textract/Rekognition et boucles qualité.",
            ["human_in_loop", "textract_review", "quality_loops", "aws_integration"],
            "per_usage",
            "enterprise",
            "https://aws.amazon.com/augmented-ai/",
            "official_site",
        ),
        v(
            "invofox",
            "Invofox",
            "https://invofox.com/",
            ["document-idp"],
            "IDP factures API ; extraction champs, scores confiance et validation humaine exceptions dossier.",
            ["invoice_idp", "field_extraction", "confidence_scoring", "human_validation"],
            "hybrid",
            "mid_market",
            "https://invofox.com/",
            "g2",
            hq="ES",
            fr="partial",
            regions=["ES", "EU"],
            geo="europe",
        ),
        v(
            "docubee",
            "Docubee",
            "https://www.docubee.com/",
            ["document-idp"],
            "Workflow documentaire ; capture, extraction champs, approbations humaines et archivage dossier validé.",
            ["document_workflow", "field_extraction", "human_approval", "archiving"],
            "hybrid",
            "mid_market",
            "https://www.docubee.com/",
            "capterra",
        ),
        v(
            "fabasoft",
            "Fabasoft",
            "https://www.fabasoft.com/",
            ["document-idp"],
            "Content services EU ; capture, IDP, validation humaine et gouvernance dossiers régulés.",
            ["content_services", "capture", "human_validation", "governance"],
            "enterprise_quote",
            "enterprise",
            "https://www.fabasoft.com/",
            "geo_digest",
            hq="AT",
            fr="partial",
            regions=["AT", "EU"],
            geo="europe",
        ),
        v(
            "pspdfkit",
            "PSPDFKit Document Engine",
            "https://pspdfkit.com/",
            ["document-idp"],
            "Moteur document SDK ; OCR, extraction formulaires et workflows annotation/revue intégrables.",
            ["document_sdk", "ocr", "form_extraction", "annotation"],
            "hybrid",
            "mid_market",
            "https://pspdfkit.com/",
            "g2",
            hq="DE",
            fr="partial",
            regions=["DE", "EU", "US"],
        ),
        v(
            "square9",
            "Square 9 Softworks",
            "https://www.square-9.com/",
            ["document-idp"],
            "Capture enterprise ; scan/OCR, files validation opérateur et export dossier conforme records.",
            ["document_capture", "ocr", "operator_validation", "records_management"],
            "enterprise_quote",
            "enterprise",
            "https://www.square-9.com/",
            "capterra",
        ),
    ],
}

SEGMENT_PATCHES: dict[str, list[str]] = {
    "fenergo": ["kyc-aml"],
    "feedzai": ["kyc-aml"],
    "lucinity": ["kyc-aml"],
    "napier": ["kyc-aml"],
    "workfusion": ["document-idp"],
    "parseur": ["document-idp"],
    "docparser": ["document-idp"],
    "airparser": ["document-idp"],
    "nanonets": ["parsing-inbox"],
    "formx": ["parsing-inbox"],
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "kyc-aml": {
        "g2": {"consulted_at": TODAY, "candidates_found": 22, "new_added": 5, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 18, "new_added": 4, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 1, "pass": PASS_ID},
    },
    "regtech": {
        "g2": {"consulted_at": TODAY, "candidates_found": 24, "new_added": 4, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 16, "new_added": 3, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
    },
    "document-idp": {
        "g2": {"consulted_at": TODAY, "candidates_found": 26, "new_added": 5, "pass": PASS_ID},
        "capterra": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 2, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 16, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 1, "pass": PASS_ID},
    },
}

TARGET_LEVELS = {
    "kyc-aml": "L3",
    "regtech": "L3",
    "document-idp": "L3",
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
