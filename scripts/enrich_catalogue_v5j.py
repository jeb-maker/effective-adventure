#!/usr/bin/env python3
"""Vague 5j — automation-platforms orchestration / human-in-the-loop (RecordAI)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v5j-recordai-orchestration"


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
    "automation-platforms.json": [
        v("windmill", "Windmill", "https://www.windmill.dev/",
          ["automation-platforms"],
          "Orchestration workflows code-first ; scripts, flows planifiés et audit trail exécutions self-hosted/cloud.",
          ["workflow_orchestration", "code_scripts", "audit_trail", "self_hosted"], "hybrid", "mid_market",
          "https://www.windmill.dev/", "open_source", hq="FR", fr="strong", regions=["FR", "EU", "US"]),
        v("relay-app", "Relay.app", "https://www.relay.app/",
          ["automation-platforms"],
          "Automatisations multi-étapes avec revue humaine ; connecteurs email/docs et approbations avant action.",
          ["human_in_loop", "email_connectors", "document_triggers", "approval_steps"], "hybrid", "smb",
          "https://www.relay.app/pricing", "g2"),
        v("bardeen", "Bardeen", "https://www.bardeen.ai/",
          ["automation-platforms"],
          "Automatisation navigateur + apps ; playbooks IA, extraction web/docs et exécution assistée opérateur.",
          ["browser_automation", "ai_playbooks", "document_extraction", "human_assisted"], "hybrid", "smb",
          "https://www.bardeen.ai/pricing", "g2"),
        v("parabola", "Parabola", "https://parabola.io/",
          ["automation-platforms"],
          "Pipelines données visuels ; ingestion email/CSV/PDF, transformations et export dossier vers ERP/CRM.",
          ["visual_pipelines", "email_ingestion", "pdf_import", "erp_export"], "hybrid", "mid_market",
          "https://parabola.io/pricing", "g2"),
        v("gumloop", "Gumloop", "https://www.gumloop.com/",
          ["automation-platforms"],
          "Workflows IA no-code ; agents, connecteurs SaaS et étapes validation avant envoi document/email.",
          ["ai_workflows", "agent_nodes", "human_validation", "saas_connectors"], "hybrid", "smb",
          "https://www.gumloop.com/", "crunchbase"),
        v("stack-ai", "Stack AI", "https://www.stack-ai.com/",
          ["automation-platforms"],
          "Orchestration agents IA ; chaînage LLM, outils métier et revue humaine sur outputs dossier.",
          ["agent_orchestration", "llm_chains", "human_review", "api_export"], "hybrid", "mid_market",
          "https://www.stack-ai.com/", "crunchbase"),
        v("retool-workflows", "Retool Workflows", "https://retool.com/workflows",
          ["automation-platforms"],
          "Orchestration backend Retool ; triggers email/webhook, étapes code/SQL et logs audit exécution.",
          ["backend_workflows", "webhook_triggers", "audit_logs", "sql_steps"], "hybrid", "mid_market",
          "https://retool.com/workflows", "official_site"),
        v("budibase", "Budibase", "https://budibase.com/",
          ["automation-platforms"],
          "Low-code + automations ; apps internes, flows déclenchés par formulaire/email et journal actions.",
          ["low_code_apps", "workflow_automation", "form_triggers", "action_log"], "hybrid", "smb",
          "https://budibase.com/pricing", "open_source", hq="GB", fr="partial", regions=["GB", "EU", "US"]),
        v("celonis", "Celonis", "https://www.celonis.com/",
          ["automation-platforms"],
          "Process mining + orchestration ; détection goulots, actions automatisées et traçabilité processus.",
          ["process_mining", "orchestration", "audit_trail", "action_flows"], "enterprise_quote", "enterprise",
          "https://www.celonis.com/", "analyst_report", hq="DE", fr="partial", regions=["DE", "EU", "US"]),
        v("temporal", "Temporal", "https://temporal.io/",
          ["automation-platforms"],
          "Moteur orchestration durable ; workflows code (retry, saga) avec historique complet exécutions.",
          ["durable_workflows", "orchestration", "execution_history", "self_hosted"], "hybrid", "enterprise",
          "https://temporal.io/", "open_source"),
        v("prefect", "Prefect", "https://www.prefect.io/",
          ["automation-platforms"],
          "Orchestration data/ops ; flows Python planifiés, observabilité runs et reprise sur échec dossier.",
          ["python_flows", "scheduling", "run_observability", "retry_logic"], "hybrid", "mid_market",
          "https://www.prefect.io/pricing", "open_source"),
        v("flowable", "Flowable", "https://www.flowable.com/",
          ["automation-platforms"],
          "BPMN/CMMN européen ; moteur processus, tâches humaines, formulaires et audit trail dossier.",
          ["bpmn", "human_tasks", "case_management", "audit_trail"], "enterprise_quote", "enterprise",
          "https://www.flowable.com/", "geo_digest", hq="BE", fr="partial", regions=["BE", "EU", "US"]),
    ],
}

SEGMENT_PATCHES: dict[str, list[str]] = {
    "laiye": ["automation-platforms"],
    "camunda": ["automation-platforms"],
    "kissflow": ["automation-platforms"],
    "pipefy": ["automation-platforms"],
    "tonkean": ["automation-platforms"],
    "levity": ["automation-platforms"],
    "dext": ["automation-platforms"],
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "automation-platforms": {
        "g2": {"consulted_at": TODAY, "candidates_found": 22, "new_added": 4, "pass": PASS_ID},
        "crunchbase": {"consulted_at": TODAY, "candidates_found": 14, "new_added": 2, "pass": PASS_ID},
        "open_source": {"consulted_at": TODAY, "candidates_found": 12, "new_added": 4, "pass": PASS_ID},
        "official_site": {"consulted_at": TODAY, "candidates_found": 10, "new_added": 2, "pass": PASS_ID},
        "analyst_report": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 1, "pass": PASS_ID},
        "geo_digest": {"consulted_at": TODAY, "candidates_found": 6, "new_added": 1, "pass": PASS_ID},
        "alternatives": {"consulted_at": TODAY, "candidates_found": 8, "new_added": 0, "pass": PASS_ID},
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
