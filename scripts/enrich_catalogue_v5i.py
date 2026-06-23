#!/usr/bin/env python3
"""Vague 5i — document-idp human-in-the-loop / validation dossier (RecordAI)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v5i-document-idp"


def v(
    id_: str, name: str, url: str, segments: list[str], desc: str, caps: list[str],
    pricing: str, market: str, source: str, src_type: str,
    hq: str = "US", fr: str = "partial", regions: list[str] | None = None,
) -> dict:
    return {
        "id": id_, "name": name, "url": url, "segments": segments,
        "description": desc, "capabilities": caps, "pricing_model": pricing,
        "target_market": market, "geography": "global",
        "hq_country": hq, "france_market": fr,
        "operating_regions": regions or ["US", "EU"],
        "discovery_source": src_type, "discovery_pass": PASS_ID,
        "source_url": source, "source_consulted_at": TODAY,
        "verification_status": "partial",
    }


ADDITIONS: dict[str, list[dict]] = {
    "document-idp.json": [
        v("ephesoft", "Ephesoft", "https://ephesoft.com/",
          ["document-idp"],
          "Capture intelligente ; classification, extraction et postes de validation humaine avant export ERP.",
          ["document_capture", "classification", "human_validation", "erp_export"], "enterprise_quote", "enterprise",
          "https://ephesoft.com/", "analyst_report"),
        v("grooper", "Grooper", "https://grooper.com/",
          ["document-idp"],
          "Plateforme document intelligence ; OCR, extraction champs et revue opérateur avec audit trail dossier.",
          ["ocr", "field_extraction", "human_review", "audit_trail"], "enterprise_quote", "enterprise",
          "https://grooper.com/", "g2"),
        v("alkymi", "Alkymi", "https://www.alkymi.io/",
          ["document-idp"],
          "Extraction documents financiers ; workflows revue analyste et validation dossier avant intégration.",
          ["financial_documents", "field_extraction", "human_review", "workflow"], "enterprise_quote", "enterprise",
          "https://www.alkymi.io/", "g2"),
        v("super-ai", "Super.AI", "https://super.ai/",
          ["document-idp"],
          "Traitement hybride IA + opérateurs ; classification, extraction et QC humain sur dossiers complexes.",
          ["hybrid_processing", "classification", "human_qc", "complex_documents"], "hybrid", "mid_market",
          "https://super.ai/pricing", "crunchbase"),
        v("docdigitizer", "DocDigitizer", "https://docdigitizer.com/",
          ["document-idp"],
          "IDP avec validation humaine intégrée ; extraction champs et contrôle qualité dossier avant livraison.",
          ["field_extraction", "human_validation", "quality_control", "api"], "hybrid", "mid_market",
          "https://docdigitizer.com/", "geo_digest", hq="PT", fr="partial", regions=["PT", "EU"]),
        v("natif-ai", "Natif.ai", "https://natif.ai/",
          ["document-idp"],
          "IDP européen ; modèles pré-entraînés, interface revue humaine et export dossier validé.",
          ["pretrained_models", "field_extraction", "human_review", "eu_hosting"], "hybrid", "mid_market",
          "https://natif.ai/", "geo_digest", hq="DE", fr="partial", regions=["DE", "EU"]),
        v("automation-hero", "Automation Hero", "https://automationhero.com/",
          ["document-idp"],
          "IDP industriel ; extraction, règles métier et postes de validation opérateur pour dossiers.",
          ["industrial_idp", "business_rules", "human_validation", "workflow"], "enterprise_quote", "enterprise",
          "https://automationhero.com/", "g2", hq="DE", fr="partial", regions=["DE", "EU", "US"]),
        v("ibm-datacap", "IBM Datacap", "https://www.ibm.com/products/datacap",
          ["document-idp"],
          "Capture enterprise ; scan/OCR, reconnaissance champs et stations validation humaine auditables.",
          ["document_capture", "ocr", "validation_station", "audit_trail"], "enterprise_quote", "enterprise",
          "https://www.ibm.com/products/datacap", "official_site"),
        v("microsoft-syntex", "Microsoft Syntex", "https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-syntex",
          ["document-idp"],
          "Traitement docs SharePoint/M365 ; extraction, métadonnées et approbations humaines sur dossiers.",
          ["sharepoint", "metadata_extraction", "human_approval", "content_processing"], "hybrid", "enterprise",
          "https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-syntex", "official_site"),
        v("docugami", "Docugami", "https://www.docugami.com/",
          ["document-idp"],
          "Compréhension contrats/docs ; graphe sémantique, revue humaine et dossier validé exportable.",
          ["contract_understanding", "semantic_graph", "human_review", "export"], "hybrid", "mid_market",
          "https://www.docugami.com/", "g2"),
        v("parascript", "Parascript", "https://www.parascript.com/",
          ["document-idp"],
          "Reconnaissance chèques/docs ; extraction champs, scores confiance et validation opérateur.",
          ["check_recognition", "field_extraction", "confidence_scoring", "human_validation"], "enterprise_quote", "enterprise",
          "https://www.parascript.com/", "analyst_report"),
        v("antworks", "AntWorks", "https://www.ant.works/",
          ["document-idp"],
          "IDP cognitive ; classification, extraction et boucle human-in-the-loop pour exceptions dossier.",
          ["cognitive_idp", "classification", "human_in_loop", "exception_handling"], "enterprise_quote", "enterprise",
          "https://www.ant.works/", "analyst_report", hq="GB", fr="partial", regions=["GB", "EU", "US"]),
        v("iron-mountain-insight", "Iron Mountain InSight", "https://www.ironmountain.com/services/digital/insight",
          ["document-idp"],
          "Numérisation + IDP ; OCR, indexation et contrôle qualité humain sur dossiers archivés.",
          ["digitization", "ocr", "indexing", "human_qc"], "enterprise_quote", "enterprise",
          "https://www.ironmountain.com/services/digital/insight", "official_site"),
        v("laiye", "Laiye", "https://laiye.com/",
          ["document-idp"],
          "Automatisation intelligente ; IDP, règles métier et revue humaine sur files d'attente dossier.",
          ["intelligent_automation", "idp", "human_review", "work_queue"], "enterprise_quote", "enterprise",
          "https://laiye.com/", "g2", hq="CN", fr="partial", regions=["CN", "EU", "US"]),
        v("heron-data", "Heron Data", "https://www.herondata.io/",
          ["document-idp"],
          "Extraction docs financiers crédit ; scoring, revue analyste et dossier validé pour underwriting.",
          ["financial_extraction", "credit_scoring", "human_review", "underwriting"], "hybrid", "mid_market",
          "https://www.herondata.io/", "crunchbase", hq="GB", fr="partial", regions=["GB", "EU", "US"]),
        v("cascading-ai", "Cascading AI", "https://www.cascading.ai/",
          ["document-idp"],
          "IDP crédit/commercial ; collecte docs, extraction et validation humaine dossier prêt.",
          ["loan_documents", "field_extraction", "human_validation", "case_management"], "hybrid", "mid_market",
          "https://www.cascading.ai/", "crunchbase"),
    ],
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "document-idp": {
        "g2": {"consulted_at": TODAY, "candidates_found": 24, "new_added": 5, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 16, "new_added": 3, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 3, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "alternatives": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
    },
}


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
        data["updated_at"] = TODAY
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"updated {fname}: +{count}")

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
    print(f"done: +{total} vendors")


if __name__ == "__main__":
    merge()
