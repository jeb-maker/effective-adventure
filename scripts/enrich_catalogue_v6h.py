#!/usr/bin/env python3
"""Vague V6h — civic/open-data MCP additions (idée 0003) + listicle cleanup batch."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
COVERAGE = ROOT / "catalogue-saas" / "coverage-matrix.json"
TODAY = "2026-06-23"
PASS_ID = "2026-06-v6h-listicle-civic-open-data"


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
    *,
    verified: bool = False,
    hq: str = "FR",
    fr: str = "strong",
    regions: list[str] | None = None,
    geo: str = "france",
    pricing_notes: str | None = None,
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
        "operating_regions": regions or ["FR"],
        "discovery_source": src_type,
        "discovery_pass": PASS_ID,
        "source_url": source,
        "source_consulted_at": TODAY,
        "verification_status": "verified" if verified else "partial",
    }
    if pricing_notes:
        d["pricing_notes"] = pricing_notes
    if notes:
        d["notes"] = notes
    return d


ADDITIONS: dict[str, list[dict]] = {
    "civic-tech-fr.json": [
        v(
            "urbaa",
            "Urbaa.app",
            "https://urbaa.app/",
            ["civic-tech-fr", "territorial-analytics", "open-data-governance-fr"],
            "Copilote territorial open data : agrège et analyse des millions de données publiques "
            "de ~35 000 communes (immobilier, finances locales, démographie, sécurité, élections, cadre de vie) "
            "via IA conversationnelle et baromètres comparatifs.",
            [
                "commune_comparison",
                "territorial_analytics",
                "open_data",
                "ai_copilot",
                "elections",
                "local_finance",
                "france",
            ],
            "freemium",
            "self_serve",
            "https://www.data.gouv.fr/reuses/urbaa-app",
            "official_site",
            verified=True,
            notes="Concurrent direct idée 0003 ; réutilisation data.gouv + site urbaa.app (consulté 2026-06-23).",
        ),
    ],
    "open-data-governance-fr.json": [
        v(
            "datagouv-mcp",
            "data.gouv.fr MCP (officiel)",
            "https://mcp.data.gouv.fr/mcp",
            ["open-data-governance-fr", "territorial-analytics", "agent-frameworks-platforms"],
            "Serveur MCP officiel Etalab/data.gouv.fr : recherche jeux de données, métadonnées, "
            "exploration ressources et requêtes tabulaires depuis un assistant compatible MCP.",
            [
                "mcp_server",
                "dataset_search",
                "metadata",
                "tabular_query",
                "open_data",
                "france",
            ],
            "open_source",
            "self_serve",
            "https://guides.data.gouv.fr/intelligence-artificielle/le-serveur-mcp-de-data.gouv.fr",
            "official_site",
            verified=True,
            pricing_notes="Service public expérimental gratuit ; endpoint https://mcp.data.gouv.fr/mcp (consulté 2026-06-23).",
            notes="Dépôt https://github.com/datagouv/datagouv-mcp ; cité idée 0003 revue.",
        ),
        v(
            "france-data-mcp",
            "france-data-mcp (OSS)",
            "https://github.com/cturkieh/france-data-mcp",
            ["open-data-governance-fr", "territorial-analytics"],
            "Serveur MCP communautaire TypeScript croisant 13+ référentiels publics français "
            "(SIRENE, santé, démographie, géo, immobilier DVF/permis) pour agents Claude/Cursor.",
            [
                "mcp_server",
                "open_source",
                "cross_reference",
                "sirene",
                "health_data",
                "real_estate",
                "france",
            ],
            "open_source",
            "self_serve",
            "https://github.com/cturkieh/france-data-mcp",
            "open_source",
            notes="Repo actif (habib256/france-data-mcp introuvable 2026-06-23) ; cité idées 0003/0006.",
        ),
    ],
}

VERIFY_UPDATES: dict[str, dict] = {
    # riskpublishing.com (5)
    "hyperproof": {
        "verification_status": "verified",
        "source_url": "https://hyperproof.io/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace riskpublishing.com listicle (consulté 2026-06-23).",
    },
    "onspring": {
        "verification_status": "verified",
        "source_url": "https://onspring.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace riskpublishing.com listicle (consulté 2026-06-23).",
    },
    "navex": {
        "verification_status": "verified",
        "source_url": "https://www.navex.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace riskpublishing.com listicle (consulté 2026-06-23).",
    },
    "diligent": {
        "verification_status": "verified",
        "source_url": "https://www.diligent.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace riskpublishing.com listicle (consulté 2026-06-23).",
    },
    "metricstream-reg": {
        "verification_status": "verified",
        "source_url": "https://www.metricstream.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace riskpublishing.com listicle (consulté 2026-06-23).",
    },
    # v-comply.com (5)
    "secureframe": {
        "verification_status": "verified",
        "source_url": "https://secureframe.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace v-comply.com/blog/top-grc-software listicle (consulté 2026-06-23).",
    },
    "vanta": {
        "verification_status": "verified",
        "source_url": "https://www.vanta.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace v-comply.com/blog/top-grc-software listicle (consulté 2026-06-23).",
    },
    "drata": {
        "verification_status": "verified",
        "source_url": "https://drata.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace v-comply.com listicle ; pricing sur devis (consulté 2026-06-23).",
    },
    "scytale": {
        "verification_status": "verified",
        "source_url": "https://scytale.ai/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace v-comply.com/blog/top-grc-software listicle (consulté 2026-06-23).",
    },
    "vcomply": {
        "verification_status": "verified",
        "source_url": "https://www.v-comply.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace v-comply.com/blog/navex-alternatives listicle (consulté 2026-06-23).",
    },
    # modulos.ai/best-ai-governance (3 restants dans grc-security ; ibm-watsonx-governance déjà fixé v6g)
    "servicenow-grc": {
        "verification_status": "verified",
        "source_url": "https://www.servicenow.com/products/governance-risk-and-compliance.html",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace modulos.ai/best-ai-governance listicle (consulté 2026-06-23).",
    },
    "ibm-openpages": {
        "verification_status": "verified",
        "source_url": "https://www.ibm.com/products/openpages",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace modulos.ai/best-ai-governance listicle (consulté 2026-06-23).",
    },
    "collibra": {
        "verification_status": "verified",
        "source_url": "https://www.collibra.com/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace modulos.ai/best-ai-governance listicle (consulté 2026-06-23).",
    },
    # pickaxe.co (4)
    "pickaxe": {
        "verification_status": "verified",
        "source_url": "https://pickaxe.co/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace pickaxe.co/post/ai-agent-pricing-models listicle (consulté 2026-06-23).",
    },
    "sierra": {
        "verification_status": "verified",
        "source_url": "https://sierra.ai/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace pickaxe.co listicle ; pricing enterprise sur devis (consulté 2026-06-23).",
    },
    "11x": {
        "verification_status": "verified",
        "source_url": "https://www.11x.ai/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace pickaxe.co/post/ai-agent-pricing-models listicle (consulté 2026-06-23).",
    },
    "decagon": {
        "verification_status": "verified",
        "source_url": "https://decagon.ai/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace pickaxe.co/post/ai-agent-pricing-models listicle (consulté 2026-06-23).",
    },
    # zylos.ai (3) — tarifs officiels
    "cursor": {
        "verification_status": "verified",
        "source_url": "https://cursor.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Pro $20/mo, Pro+ $60/mo, Ultra $200/mo ; remplace zylos.ai listicle (consulté 2026-06-23).",
    },
    "windsurf": {
        "verification_status": "verified",
        "source_url": "https://devin.ai/blog/windsurf-pricing-plans",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Free/Pro $20/Teams $40 seat/Max $200 ; annonce officielle Cognition (consulté 2026-06-23).",
    },
    "claude-code": {
        "verification_status": "verified",
        "source_url": "https://claude.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Plans Pro/Max/Team Anthropic ; remplace zylos.ai listicle (consulté 2026-06-23).",
    },
    # trustible.ai
    "trustible": {
        "verification_status": "verified",
        "source_url": "https://trustible.ai/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace trustible.ai/post/types-of-ai-governance-platforms listicle (consulté 2026-06-23).",
    },
    # extend.ai/resources
    "sensible": {
        "verification_status": "verified",
        "source_url": "https://www.sensible.so/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace extend.ai/resources listicle (consulté 2026-06-23).",
    },
    # helply.com (3)
    "zendesk-ai": {
        "verification_status": "verified",
        "source_url": "https://www.zendesk.com/pricing/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace helply.com/blog/per-seat-saas-pricing-dying listicle (consulté 2026-06-23).",
    },
    "forethought": {
        "verification_status": "verified",
        "source_url": "https://forethought.ai/",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace helply.com listicle (consulté 2026-06-23).",
    },
    "hubspot-breeze": {
        "verification_status": "verified",
        "source_url": "https://www.hubspot.com/pricing",
        "source_consulted_at": TODAY,
        "discovery_pass": PASS_ID,
        "pricing_notes": "Remplace helply.com/blog/per-seat-saas-pricing-dying listicle (consulté 2026-06-23).",
    },
}

COVERAGE_UPDATES: dict[str, dict[str, dict]] = {
    "civic-tech-fr": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 1,
            "new_added": 1,
            "pass": PASS_ID,
        },
    },
    "open-data-governance-fr": {
        "official_site": {
            "consulted_at": TODAY,
            "candidates_found": 2,
            "new_added": 2,
            "pass": PASS_ID,
        },
    },
}


def apply_verify_updates() -> int:
    count = 0
    for path in VENDORS_DIR.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for vendor in data.get("vendors", []):
            upd = VERIFY_UPDATES.get(vendor["id"])
            if not upd:
                continue
            vendor.update(upd)
            changed = True
            count += 1
        if changed:
            data["updated_at"] = TODAY
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return count


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
        if count:
            data["updated_at"] = TODAY
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"updated {fname}: +{count}")

    verified = apply_verify_updates()
    print(f"verify updates: {verified}")

    matrix = json.loads(COVERAGE.read_text(encoding="utf-8"))
    for seg_id, sources in COVERAGE_UPDATES.items():
        entry = matrix["segments"][seg_id]
        for src, upd in sources.items():
            prev = entry["sources"].get(src) or {}
            entry["sources"][src] = {
                **upd,
                "cumulative_new": prev.get("cumulative_new", prev.get("new_added", 0))
                + upd["new_added"],
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
    print("running saturation freeze…")
    rc = subprocess.call(
        [sys.executable, str(ROOT / "scripts" / "catalogue_saas.py"), "saturation", "freeze"],
        cwd=ROOT,
    )
    sys.exit(rc)
