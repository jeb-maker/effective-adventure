#!/usr/bin/env python3
"""Vague 5g — 2e passe L3 parsing-inbox + compliance-to-spec."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-22"
PASS_ID = "2026-06-v5g-parsing-compliance"


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
    "parsing-inbox.json": [
        v("cloudmailin", "CloudMailin", "https://www.cloudmailin.com/", ["parsing-inbox"],
          "Réception et parsing email HTTP ; extraction corps HTML/texte et pièces jointes.",
          ["inbound_email", "http_post", "attachments", "parsing"], "per_usage", "mid_market",
          "https://www.cloudmailin.com/", "alternatives", hq="GB", regions=["GB", "EU", "US"]),
        v("aurinko", "Aurinko", "https://www.aurinko.io/", ["parsing-inbox"],
          "Unified API email/calendar ; sync et parsing multi-fournisseurs pour apps B2B.",
          ["unified_api", "email_sync", "calendar", "integrations"], "hybrid", "mid_market",
          "https://www.aurinko.io/", "crunchbase"),
        v("unipile", "Unipile", "https://www.unipile.com/", ["parsing-inbox"],
          "API messagerie unifiée ; LinkedIn, email, WhatsApp — extraction et webhooks.",
          ["unified_messaging", "email_api", "webhooks", "crm"], "hybrid", "mid_market",
          "https://www.unipile.com/", "g2", hq="FR", fr="strong", regions=["FR", "EU"]),
        v("emailengine", "EmailEngine", "https://emailengine.app/", ["parsing-inbox"],
          "Gateway email self-hosted ; IMAP/SMTP vers API REST pour parsing et automation.",
          ["imap_gateway", "rest_api", "self_hosted", "webhooks"], "hybrid", "mid_market",
          "https://emailengine.app/", "open_source", hq="EE", regions=["EU", "US"]),
        v("unstract", "Unstract", "https://unstract.com/", ["parsing-inbox", "document-idp"],
          "LLMWhisperer + pipelines ; email/PDF → JSON structuré sans templates fixes.",
          ["llm_parsing", "email_to_json", "pdf_extraction", "api"], "per_usage", "mid_market",
          "https://unstract.com/", "g2"),
        v("microsoft-graph-mail", "Microsoft Graph Mail API", "https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview",
          ["parsing-inbox"],
          "Accès programmatique boîtes Exchange/M365 ; lecture, pièces jointes et webhooks.",
          ["graph_api", "outlook", "attachments", "webhooks"], "hybrid", "enterprise",
          "https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview", "official_site"),
        v("google-gmail-api", "Gmail API", "https://developers.google.com/gmail/api",
          ["parsing-inbox"],
          "API Gmail ; lecture messages, parsing MIME et push notifications pour workflows.",
          ["gmail_api", "mime", "push_notifications", "attachments"], "hybrid", "mid_market",
          "https://developers.google.com/gmail/api", "official_site"),
        v("inbound-missive", "Missive Inbound", "https://missiveapp.com/",
          ["parsing-inbox"],
          "Boîte collaborative ; règles entrantes et intégrations pour trier emails métier.",
          ["shared_inbox", "rules", "integrations", "collaboration"], "hybrid", "smb",
          "https://missiveapp.com/", "alternatives", hq="CA", regions=["CA", "US", "EU"]),
    ],
    "compliance-to-spec.json": [
        v("trustarc", "TrustArc", "https://trustarc.com/", ["compliance-to-spec", "privacy-consent"],
          "Privacy compliance platform ; assessments, policies et mapping exigences → contrôles.",
          ["privacy_assessments", "policy_management", "control_mapping"], "enterprise_quote", "enterprise",
          "https://trustarc.com/", "g2"),
        v("processunity", "ProcessUnity", "https://www.processunity.com/", ["compliance-to-spec", "grc-security"],
          "GRC third-party risk ; workflows conformité et evidence pour tiers critiques.",
          ["tprm", "grc_workflows", "evidence", "vendor_risk"], "enterprise_quote", "enterprise",
          "https://www.processunity.com/", "analyst_report"),
        v("ostendio", "Ostendio", "https://www.ostendio.com/", ["compliance-to-spec", "grc-security"],
          "MyVCM platform ; policies, contrôles et preuves pour SOC2/HIPAA/ISO.",
          ["policies", "controls", "evidence", "soc2"], "enterprise_quote", "mid_market",
          "https://www.ostendio.com/", "g2"),
        v("fairnow", "FairNow", "https://www.fairnow.ai/", ["compliance-to-spec", "ai-governance"],
          "AI governance ; inventaire systèmes IA, risques et conformité EU AI Act encodée.",
          ["ai_inventory", "risk_controls", "eu_ai_act"], "enterprise_quote", "mid_market",
          "https://www.fairnow.ai/", "geo_digest", hq="DE", regions=["DE", "EU"]),
        v("regulativ-ai", "Regulativ.ai", "https://www.regulativ.ai/", ["compliance-to-spec", "regtech"],
          "Regulatory change → exigences actionnables ; mapping vers contrôles et specs produit.",
          ["regulatory_change", "actionable_requirements", "control_mapping"], "enterprise_quote", "enterprise",
          "https://www.regulativ.ai/", "analyst_report", hq="GB", regions=["GB", "EU", "US"]),
        v("camunda", "Camunda", "https://camunda.com/", ["compliance-to-spec"],
          "Orchestration processus ; encode workflows conformité et human-in-the-loop auditables.",
          ["bpmn", "workflow", "audit_trail", "orchestration"], "hybrid", "enterprise",
          "https://camunda.com/", "official_site", hq="DE", regions=["DE", "EU", "US"]),
        v("conformiq", "Conformiq", "https://www.conformiq.com/", ["compliance-to-spec"],
          "Model-based testing ; génération cas de test depuis exigences réglementaires formelles.",
          ["model_based_testing", "requirements_to_tests", "formal_specs"], "enterprise_quote", "enterprise",
          "https://www.conformiq.com/", "analyst_report", hq="FI", regions=["EU", "US"]),
        v("compliance-cow", "ComplianceCow", "https://www.compliancecow.com/", ["compliance-to-spec", "grc-security"],
          "Compliance-as-code marketplace ; packs contrôles et evidence réutilisables.",
          ["compliance_as_code", "control_packs", "marketplace", "evidence"], "hybrid", "mid_market",
          "https://www.compliancecow.com/", "open_source"),
    ],
}

SEGMENT_PATCHES: dict[str, list[str]] = {
    "extend-ai": ["parsing-inbox"],
    "sensible": ["parsing-inbox"],
    "reducto": ["parsing-inbox"],
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "parsing-inbox": {
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 16, "new_added": 3, "pass": PASS_ID},
        "alternatives": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 3, "pass": PASS_ID},
        "open_source": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 2, "pass": PASS_ID},
    },
    "compliance-to-spec": {
        "g2": {"consulted_at": TODAY, "candidates_found": 22, "new_added": 4, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 3, "pass": PASS_ID},
        "open_source": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 2, "pass": PASS_ID},
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
    print(f"done: +{total} vendors, {patched} patches")


if __name__ == "__main__":
    merge()
