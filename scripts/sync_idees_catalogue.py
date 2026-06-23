#!/usr/bin/env python3
"""Injecte / met à jour le bloc catalogue SaaS dans les README des idées."""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDEES = ROOT / "idees"
MAPPING_PATH = IDEES / "catalogue-segments.json"
VENDORS_DIR = ROOT / "catalogue-saas" / "vendors"
TAXONOMY_PATH = ROOT / "catalogue-saas" / "taxonomy.json"

BEGIN = "<!-- catalogue-saas-begin -->"
END = "<!-- catalogue-saas-end -->"


def load_vendors_by_segment() -> dict[str, list[dict]]:
    by_seg: dict[str, list[dict]] = {}
    for path in VENDORS_DIR.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        by_seg[path.stem] = data.get("vendors", [])
    return by_seg


def render_block(idea_slug: str, segment_ids: list[str], seg_labels: dict[str, str]) -> str:
    by_seg = load_vendors_by_segment()
    today = date.today().isoformat()
    lines = [
        BEGIN,
        "",
        "### Référence catalogue SaaS (dépôt)",
        "",
        f"**Idée** : `{idea_slug}` — segments liés pour benchmark concurrence structuré.",
        f"**Mise à jour** : {today} — ne pas utiliser les entrées `unverified` pour scorer.",
        "",
    ]

    for sid in segment_ids:
        label = seg_labels.get(sid, sid)
        vendors = by_seg.get(sid, [])
        lines.append(f"#### Segment `{sid}` — {label}")
        lines.append("")
        lines.append(
            f"Fichier : [`catalogue-saas/vendors/{sid}.json`](../../catalogue-saas/vendors/{sid}.json) "
            f"({len(vendors)} entrées)"
        )
        lines.append("")
        if not vendors:
            lines.append("_Segment vide dans le catalogue._")
            lines.append("")
            continue
        lines.append("| ID | Nom | Depuis | IA | HQ | Marché FR | Vérification |")
        lines.append("|---|---|:---:|:---:|---|---|---|")
        for v in vendors[:12]:
            hq = v.get("hq_country", "—")
            fr = v.get("france_market", "—")
            status = v.get("verification_status", "—")
            name = v["name"].replace("|", "\\|")
            since = v.get("founded_year") or "?"
            ai = "oui" if v.get("entry_ai_generated") else "non"
            lines.append(
                f"| `{v['id']}` | {name} | {since} | {ai} | {hq} | {fr} | {status} |"
            )
        if len(vendors) > 12:
            lines.append(f"| … | _+{len(vendors) - 12} autres_ | | | | | |")
        lines.append("")

    lines.extend(
        [
            "Commandes :",
            "```bash",
            "python3 scripts/catalogue_saas.py stats",
            f"python3 scripts/catalogue_saas.py gaps --segment {segment_ids[0]}",
            "```",
            "",
            END,
            "",
        ]
    )
    return "\n".join(lines)


def inject_readme(readme_path: Path, block: str) -> bool:
    text = readme_path.read_text(encoding="utf-8")
    pattern = re.compile(
        re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?",
        re.DOTALL,
    )
    if pattern.search(text):
        new_text = pattern.sub(block, text)
    elif "## 5." in text:
        idx = text.index("## 5.")
        new_text = text[:idx] + block + text[idx:]
    elif "## 4." in text:
        # Après la section 4 : chercher prochaine section ##
        m = re.search(r"^## [5-9]\.", text, re.MULTILINE)
        if m:
            new_text = text[: m.start()] + block + text[m.start() :]
        else:
            new_text = text.rstrip() + "\n\n" + block
    else:
        new_text = text.rstrip() + "\n\n" + block

    if new_text == text:
        return False
    readme_path.write_text(new_text, encoding="utf-8")
    return True


def sync(dry_run: bool = False) -> None:
    mapping = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
    taxonomy = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))
    seg_labels = {s["id"]: s["label"] for s in taxonomy["segments"]}

    updated = 0
    for idea_slug, segments in mapping["ideas"].items():
        readme = IDEES / idea_slug / "README.md"
        if not readme.exists():
            print(f"missing: {readme}")
            continue
        block = render_block(idea_slug, segments, seg_labels)
        if dry_run:
            print(f"would update: {readme}")
            continue
        if inject_readme(readme, block):
            print(f"updated: {readme.relative_to(ROOT)}")
            updated += 1
        else:
            print(f"unchanged: {readme.relative_to(ROOT)}")

    print(f"done: {updated} README(s) updated")


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    sync(dry_run=args.dry_run)
