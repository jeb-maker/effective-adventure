#!/usr/bin/env python3
"""Vague 5a — tag géographique rétrospectif (hq_country, france_market, operating_regions)."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
TODAY = "2026-06-22"
PASS_ID = "2026-06-v5a"

# Overrides explicites (id → hq_country, france_market, operating_regions)
EXPLICIT: dict[str, tuple[str, str, list[str]]] = {
    "matera": ("FR", "strong", ["FR", "EU"]),
    "ennov": ("FR", "strong", ["FR", "EU"]),
    "openvox": ("FR", "strong", ["FR", "EU"]),
    "payfit": ("FR", "strong", ["FR", "EU"]),
    "axeptio": ("FR", "strong", ["FR", "EU"]),
    "shift-technology": ("FR", "partial", ["FR", "EU", "US"]),
    "nabla-copilot": ("FR", "strong", ["FR", "EU"]),
    "brevo": ("FR", "strong", ["FR", "EU"]),
    "energiency": ("FR", "strong", ["FR", "EU"]),
    "pennylane": ("FR", "strong", ["FR", "EU"]),
    "didomi": ("FR", "strong", ["FR", "EU"]),
    "chorus-pro": ("FR", "strong", ["FR"]),
    "pappers": ("FR", "strong", ["FR", "EU"]),
    "keldoc": ("FR", "strong", ["FR"]),
    "doctolib": ("FR", "strong", ["FR", "EU"]),
    "cap-collectif": ("FR", "strong", ["FR"]),
    "make-org": ("FR", "strong", ["FR"]),
    "kalipso": ("FR", "strong", ["FR", "EU"]),
    "finrege": ("FR", "strong", ["FR", "EU"]),
    "acceslibre": ("FR", "strong", ["FR"]),
    "maitre-ao": ("FR", "strong", ["FR"]),
    "marchespublics-ai": ("FR", "strong", ["FR"]),
    "achatpublic": ("FR", "strong", ["FR"]),
    "dust": ("FR", "partial", ["FR", "EU"]),
    "spendesk": ("FR", "strong", ["FR", "EU"]),
    "pigment": ("FR", "strong", ["FR", "EU"]),
    "360learning": ("FR", "strong", ["FR", "EU"]),
    "greenly": ("FR", "partial", ["FR", "EU"]),
    "heero": ("FR", "strong", ["FR"]),
    "effy-pro": ("FR", "strong", ["FR"]),
    "geofoncier": ("FR", "strong", ["FR"]),
    "alkante": ("FR", "strong", ["FR"]),
    "ign-geoservices": ("FR", "strong", ["FR", "EU"]),
    "cartelie": ("FR", "strong", ["FR"]),
    "cityway": ("FR", "strong", ["FR", "EU"]),
    "padam-mobility": ("FR", "strong", ["FR", "EU"]),
    "hove": ("FR", "strong", ["FR"]),
    "openmeti": ("FR", "strong", ["FR"]),
    "ademe-data": ("FR", "strong", ["FR"]),
    "hub-anah": ("FR", "strong", ["FR"]),
    "atmo-france": ("FR", "strong", ["FR"]),
    "hub-eau": ("FR", "strong", ["FR"]),
    "inpn": ("FR", "strong", ["FR", "EU"]),
    "brgm-infoterre": ("FR", "strong", ["FR"]),
    "georisques-api": ("FR", "strong", ["FR"]),
    "georisques": ("FR", "strong", ["FR"]),
    "datagouv": ("FR", "strong", ["FR", "EU"]),
    "ofgl": ("FR", "strong", ["FR"]),
    "cartes-gouv": ("FR", "strong", ["FR"]),
    "etalab-data-gouv": ("FR", "strong", ["FR", "EU"]),
    "fairness": ("FR", "strong", ["FR", "EU"]),
    "toucan-toco": ("FR", "partial", ["FR", "EU"]),
    "opendatasoft": ("FR", "strong", ["FR", "EU"]),
    "opendatasoft-geo": ("FR", "strong", ["FR", "EU"]),
    "contexte": ("FR", "strong", ["FR"]),
    "regardscitoyens": ("FR", "strong", ["FR"]),
    "poligma": ("FR", "strong", ["FR"]),
    "open-source-politics": ("FR", "strong", ["FR", "EU"]),
    "iv-mobilites": ("FR", "strong", ["FR"]),
    "transport-data-gouv": ("FR", "strong", ["FR", "EU"]),
    "ameli-open-data": ("FR", "strong", ["FR"]),
    "santepubliquefrance": ("FR", "strong", ["FR"]),
    "drees": ("FR", "strong", ["FR"]),
    "data-gouv-elections": ("FR", "strong", ["FR"]),
    "mistral-ai": ("FR", "partial", ["FR", "EU", "US"]),
    "personio": ("DE", "partial", ["DE", "EU"]),
    "pagero": ("SE", "partial", ["EU", "US"]),
    "pricehubble": ("CH", "partial", ["CH", "EU"]),
    "planradar": ("AT", "partial", ["EU"]),
    "decidim": ("ES", "partial", ["EU"]),
    "data-europa": ("EU", "partial", ["EU"]),
    "venvera": ("IT", "unknown", ["EU"]),
    "onfido": ("GB", "partial", ["GB", "EU", "US"]),
    "snyk": ("IE", "partial", ["EU", "US"]),
    "wiz": ("IL", "partial", ["US", "EU"]),
}

US_LIKELY_PREFIXES = (
    "salesforce", "microsoft", "google", "amazon", "aws-", "hubspot", "openai",
    "anthropic", "crowdstrike", "palo-alto", "okta", "splunk", "tenable", "qualys",
    "rapid7", "proofpoint", "mimecast", "docusign", "adobe", "tableau", "power-bi",
    "looker", "workday", "servicenow", "ibm-", "zendesk", "intercom", "freshworks",
    "atlassian", "asana", "monday", "gong", "clari", "stripe",
)


def infer_tags(vendor: dict) -> tuple[str, str, list[str]]:
    vid = vendor["id"]
    if vid in EXPLICIT:
        return EXPLICIT[vid]

    geo = vendor.get("geography", "global")
    url = vendor.get("url", "").lower()

    if geo == "france" or ".gouv.fr" in url or ".fr/" in url:
        return "FR", "strong", ["FR", "EU"]

    if geo == "us":
        return "US", "partial", ["US", "EU"]

    if geo == "europe":
        return "unknown", "partial", ["EU"]

    if geo == "eu":
        return "EU", "partial", ["EU"]

    if vendor.get("pricing_model") == "freemium" and any(
        x in url for x in ("gouv", "data.gouv", "ademe", "insee")
    ):
        return "FR", "strong", ["FR"]

    host = urlparse(url).netloc
    if host.endswith(".fr"):
        return "FR", "strong", ["FR", "EU"]

    if any(vid.startswith(p) for p in US_LIKELY_PREFIXES):
        return "US", "partial", ["US", "EU"]

    if vendor.get("pricing_model") == "open_source":
        return "unknown", "unknown", ["US", "EU"]

    if geo == "global" and vendor.get("target_market") in ("enterprise", "mid_market"):
        return "US", "partial", ["US", "EU"]

    return "unknown", "unknown", ["US", "EU"]


def tag() -> None:
    updated = 0
    for path in sorted(VENDORS_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for v in data.get("vendors", []):
            hq, fm, regions = infer_tags(v)
            patch = {
                "hq_country": hq,
                "france_market": fm,
                "operating_regions": regions,
                "discovery_source": "retrospective_backfill",
                "discovery_pass": PASS_ID,
            }
            for key, value in patch.items():
                if v.get(key) != value:
                    v[key] = value
                    changed = True
                    updated += 1
        if changed:
            data["updated_at"] = TODAY
            path.write_text(
                json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
    print(f"tagged fields updated: {updated}")


if __name__ == "__main__":
    tag()
