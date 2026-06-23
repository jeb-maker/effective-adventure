#!/usr/bin/env python3
"""Vague 5q — L3 chaîne RecordAI (email → dossier validé → orchestration)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v5q-recordai-chain-l3"


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
    "parsing-inbox.json": [
        v(
            "hiver",
            "Hiver",
            "https://hiverhq.com/",
            ["parsing-inbox"],
            "Shared inbox Gmail/Outlook ; routage email, assignation cas et workflows collaboratifs audités.",
            ["shared_inbox", "email_routing", "case_assignment", "workflow"],
            "hybrid",
            "mid_market",
            "https://hiverhq.com/pricing",
            "g2",
        ),
        v(
            "helpscout",
            "Help Scout",
            "https://www.helpscout.com/",
            ["parsing-inbox"],
            "Support inbox partagée ; threads email→cas, notes internes, SLA et historique client traçable.",
            ["shared_inbox", "email_to_case", "sla", "audit_trail"],
            "hybrid",
            "smb",
            "https://www.helpscout.com/pricing",
            "g2",
        ),
        v(
            "dixa",
            "Dixa",
            "https://www.dixa.com/",
            ["parsing-inbox"],
            "Plateforme ops client EU ; agrégation email/chat, dossier conversation et workflows validation.",
            ["omnichannel_inbox", "email_aggregation", "case_management", "workflow"],
            "hybrid",
            "mid_market",
            "https://www.dixa.com/",
            "g2",
            hq="DK",
            fr="partial",
            regions=["DK", "EU", "US"],
            geo="europe",
        ),
        v(
            "emailtree-ai",
            "EmailTree AI",
            "https://emailtree.ai/",
            ["parsing-inbox"],
            "Automatisation email IA EU ; classification, extraction PJ et boucle validation opérateur dossier.",
            ["email_classification", "attachment_extraction", "human_validation", "ai_workflow"],
            "hybrid",
            "mid_market",
            "https://emailtree.ai/",
            "geo_digest",
            hq="LU",
            fr="partial",
            regions=["LU", "EU"],
            geo="europe",
        ),
        v(
            "docuware",
            "DocuWare",
            "https://start.docuware.com/",
            ["parsing-inbox", "document-idp"],
            "ECMS allemand ; capture email/scan, indexation, validation opérateur et archivage dossier conforme.",
            ["email_capture", "document_indexing", "operator_validation", "records_archiving"],
            "enterprise_quote",
            "enterprise",
            "https://start.docuware.com/",
            "geo_digest",
            hq="DE",
            fr="partial",
            regions=["DE", "EU", "US"],
            geo="europe",
        ),
        v(
            "m-files",
            "M-Files",
            "https://www.m-files.com/",
            ["parsing-inbox", "document-idp"],
            "Gestion documentaire metadata EU ; intake email, workflow approbation et audit trail versionné.",
            ["metadata_dms", "email_intake", "approval_workflow", "audit_trail"],
            "enterprise_quote",
            "enterprise",
            "https://www.m-files.com/",
            "g2",
            hq="FI",
            fr="partial",
            regions=["FI", "EU", "US"],
            geo="europe",
        ),
        v(
            "postscan-mail",
            "PostScan Mail",
            "https://www.postscanmail.com/",
            ["parsing-inbox"],
            "Boîte postale virtuelle ; numérisation courrier entrant, OCR et routage dossier PDF validé.",
            ["virtual_mailbox", "mail_digitization", "ocr", "document_routing"],
            "hybrid",
            "smb",
            "https://www.postscanmail.com/",
            "capterra",
        ),
        v(
            "mailbutler",
            "Mailbutler",
            "https://www.mailbutler.io/",
            ["parsing-inbox"],
            "Extension email EU ; templates, tâches, notes dossier et suivi workflow depuis la boîte entrante.",
            ["email_extension", "task_tracking", "templates", "workflow_notes"],
            "hybrid",
            "smb",
            "https://www.mailbutler.io/pricing",
            "g2",
            hq="DE",
            fr="partial",
            regions=["DE", "EU", "US"],
            geo="europe",
        ),
        v(
            "earth-class-mail",
            "Earth Class Mail",
            "https://www.earthclassmail.com/",
            ["parsing-inbox"],
            "Réception courrier physique ; scan haute qualité, classement dossier et export cloud auditables.",
            ["physical_mail_scan", "document_classification", "cloud_export", "audit_trail"],
            "hybrid",
            "smb",
            "https://www.earthclassmail.com/pricing",
            "official_site",
        ),
    ],
    "compliance-to-spec.json": [
        v(
            "certivity",
            "Certivity",
            "https://www.certivity.io/",
            ["compliance-to-spec"],
            "Conformité produits EU ; exigences réglementaires traduites en specs techniques et dossiers CE.",
            ["regulatory_to_spec", "ce_dossier", "requirement_mapping", "product_compliance"],
            "enterprise_quote",
            "mid_market",
            "https://www.certivity.io/",
            "geo_digest",
            hq="SE",
            fr="partial",
            regions=["SE", "EU", "US"],
            geo="europe",
        ),
        v(
            "qualio",
            "Qualio",
            "https://www.qualio.com/",
            ["compliance-to-spec"],
            "eQMS life sciences ; exigences ISO/FDA encodées en workflows, preuves et specs qualité validées.",
            ["eqms", "requirement_workflows", "evidence", "validated_specs"],
            "hybrid",
            "mid_market",
            "https://www.qualio.com/",
            "g2",
            hq="IE",
            fr="partial",
            regions=["IE", "EU", "US"],
        ),
        v(
            "compliancequest",
            "ComplianceQuest",
            "https://www.compliancequest.com/",
            ["compliance-to-spec"],
            "Quality/compliance Salesforce ; exigences→contrôles, CAPA et dossiers audit trail sur plateforme unifiée.",
            ["quality_management", "requirement_controls", "capa", "audit_trail"],
            "enterprise_quote",
            "enterprise",
            "https://www.compliancequest.com/",
            "analyst_report",
        ),
        v(
            "zengrc",
            "ZenGRC (Archer)",
            "https://www.zengrc.com/",
            ["compliance-to-spec"],
            "GRC cloud ; mapping cadres réglementaires vers contrôles, tâches et preuves dossier conformité.",
            ["framework_mapping", "control_tasks", "evidence", "compliance_dossier"],
            "enterprise_quote",
            "enterprise",
            "https://www.zengrc.com/",
            "g2",
        ),
        v(
            "standard-fusion",
            "StandardFusion",
            "https://www.standardfusion.com/",
            ["compliance-to-spec"],
            "GRC mid-market ; exigences SOC2/ISO traduites en politiques, contrôles et specs opérationnelles.",
            ["policy_controls", "framework_mapping", "operational_specs", "evidence"],
            "hybrid",
            "mid_market",
            "https://www.standardfusion.com/pricing",
            "g2",
        ),
        v(
            "certa",
            "Certa",
            "https://www.getcerta.com/",
            ["compliance-to-spec"],
            "Workflow compliance no-code ; questionnaires tiers, validation dossier et règles métier auditables.",
            ["third_party_workflows", "questionnaires", "case_validation", "audit_rules"],
            "hybrid",
            "mid_market",
            "https://www.getcerta.com/",
            "crunchbase",
        ),
        v(
            "complion",
            "Complion",
            "https://www.complion.com/",
            ["compliance-to-spec"],
            "Conformité essais cliniques ; exigences protocole→checklists, dossiers site et piste audit FDA.",
            ["clinical_compliance", "protocol_checklists", "site_dossiers", "audit_trail"],
            "enterprise_quote",
            "enterprise",
            "https://www.complion.com/",
            "analyst_report",
        ),
        v(
            "ideagen",
            "Ideagen",
            "https://www.ideagen.com/",
            ["compliance-to-spec", "grc-security"],
            "Suite GRC globale ; obligations réglementaires, cas conformité et preuves centralisées multi-cadres.",
            ["grc_suite", "regulatory_obligations", "case_management", "evidence"],
            "enterprise_quote",
            "enterprise",
            "https://www.ideagen.com/",
            "analyst_report",
            hq="GB",
            fr="partial",
            regions=["GB", "EU", "US", "AU"],
        ),
        v(
            "origami-risk",
            "Origami Risk",
            "https://www.origamirisk.com/",
            ["compliance-to-spec"],
            "GRC + assurance ; exigences réglementaires, workflows cas incidents et dossiers preuves traçables.",
            ["risk_grc", "incident_cases", "regulatory_requirements", "evidence_dossier"],
            "enterprise_quote",
            "enterprise",
            "https://www.origamirisk.com/",
            "g2",
        ),
    ],
    "automation-platforms.json": [
        v(
            "bonitasoft",
            "Bonitasoft",
            "https://www.bonitasoft.com/",
            ["automation-platforms", "compliance-to-spec"],
            "BPM open source FR ; processus métier, tâches humaines, formulaires et audit trail dossier EU.",
            ["bpmn", "human_tasks", "case_management", "audit_trail"],
            "hybrid",
            "mid_market",
            "https://www.bonitasoft.com/",
            "geo_digest",
            hq="FR",
            fr="strong",
            regions=["FR", "EU", "US"],
            geo="france",
        ),
        v(
            "bizagi",
            "Bizagi",
            "https://www.bizagi.com/",
            ["automation-platforms"],
            "BPM low-code ; modélisation processus, files humaines, connecteurs docs/email et journal cas.",
            ["bpmn", "human_workqueues", "document_connectors", "case_log"],
            "enterprise_quote",
            "enterprise",
            "https://www.bizagi.com/",
            "g2",
            hq="CO",
            fr="partial",
            regions=["CO", "EU", "US"],
        ),
        v(
            "bonita",
            "Bonita (Bonitasoft)",
            "https://www.bonitasoft.com/products",
            ["automation-platforms"],
            "Moteur BPMN open source ; orchestration durable, tâches opérateur et historique exécution complet.",
            ["bpmn_engine", "human_tasks", "orchestration", "execution_history"],
            "open_source",
            "mid_market",
            "https://www.bonitasoft.com/products",
            "open_source",
            hq="FR",
            fr="strong",
            regions=["FR", "EU"],
            geo="france",
            notes="Moteur OSS distinct de la plateforme Bonitasoft commercial cataloguée.",
        ),
        v(
            "inngest",
            "Inngest",
            "https://www.inngest.com/",
            ["automation-platforms"],
            "Orchestration événementielle ; workflows code, steps durables, reprise échec et logs audit exécution.",
            ["event_driven", "durable_steps", "retry_logic", "execution_logs"],
            "hybrid",
            "mid_market",
            "https://www.inngest.com/pricing",
            "open_source",
        ),
        v(
            "kestra",
            "Kestra",
            "https://kestra.io/",
            ["automation-platforms"],
            "Orchestration data/ops FR ; flows YAML, observabilité runs, reprise dossier et audit trail EU.",
            ["yaml_flows", "run_observability", "retry", "audit_trail"],
            "hybrid",
            "mid_market",
            "https://kestra.io/",
            "open_source",
            hq="FR",
            fr="strong",
            regions=["FR", "EU", "US"],
            geo="france",
        ),
        v(
            "hatchet",
            "Hatchet",
            "https://hatchet.run/",
            ["automation-platforms"],
            "Moteur workflows code ; files tâches, concurrence, reprise et historique runs auditables.",
            ["task_queues", "workflow_engine", "run_history", "retry"],
            "hybrid",
            "mid_market",
            "https://hatchet.run/",
            "open_source",
        ),
        v(
            "flokzu",
            "Flokzu",
            "https://flokzu.com/",
            ["automation-platforms"],
            "BPM cloud no-code ; formulaires entrants, approbations humaines et traçabilité processus EU.",
            ["no_code_bpm", "form_intake", "human_approvals", "process_traceability"],
            "hybrid",
            "smb",
            "https://flokzu.com/pricing",
            "capterra",
            hq="UY",
            fr="partial",
            regions=["UY", "EU", "US"],
        ),
        v(
            "process-street",
            "Process Street",
            "https://www.process.st/",
            ["automation-platforms"],
            "Checklists processus ; SOPs email/doc-triggered, assignations humaines et journal conformité.",
            ["process_checklists", "sop", "human_assignments", "compliance_log"],
            "hybrid",
            "smb",
            "https://www.process.st/pricing",
            "g2",
        ),
        v(
            "nintex",
            "Nintex",
            "https://www.nintex.com/",
            ["automation-platforms"],
            "Workflow enterprise ; orchestration SharePoint/M365, tâches humaines, docs et audit trail complet.",
            ["enterprise_workflow", "human_tasks", "document_automation", "audit_trail"],
            "enterprise_quote",
            "enterprise",
            "https://www.nintex.com/",
            "analyst_report",
            hq="US",
            fr="partial",
        ),
    ],
}

SEGMENT_PATCHES: dict[str, list[str]] = {
    "auditboard": ["compliance-to-spec"],
    "stampli": ["parsing-inbox"],
    "docubee": ["parsing-inbox"],
    "datasnipper": ["parsing-inbox"],
    "flowable": ["compliance-to-spec"],
    "temporal": ["parsing-inbox"],
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "parsing-inbox": {
        "g2": {"consulted_at": TODAY, "candidates_found": 20, "new_added": 4, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 3, "pass": PASS_ID},
        "capterra": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 1, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
    },
    "compliance-to-spec": {
        "g2": {"consulted_at": TODAY, "candidates_found": 22, "new_added": 3, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 2, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 2, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 1, "pass": PASS_ID},
    },
    "automation-platforms": {
        "g2": {"consulted_at": TODAY, "candidates_found": 18, "new_added": 2, "pass": PASS_ID},
        "open_source": {"consulted_at": TODAY, "candidates_found": 16, "new_added": 4, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 2, "pass": PASS_ID},
        "capterra": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
    },
}

TARGET_LEVELS = {
    "parsing-inbox": "L3",
    "compliance-to-spec": "L3",
    "automation-platforms": "L3",
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
