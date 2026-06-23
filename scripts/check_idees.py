#!/usr/bin/env python3
"""Contrôle des revues critiques obligatoires pour les idées en statut final."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDEES = ROOT / "idees"

STATUT_RE = re.compile(r"^-\s+\*\*Statut\*\*\s*:\s*(.+)$", re.MULTILINE)
SECTION_RE = re.compile(r"^##\s+(\d+)\.\s+(.+)$", re.MULTILINE)

FINAL_EMOJI = frozenset({"🔁", "❌", "✅", "🚧"})
SKIP_EMOJI = frozenset({"💡", "🔍"})

FINAL_TEXT_MARKERS = (
    "à retravailler",
    "retravailler",
    "écartée",
    "ecartee",
    "validée",
    "validee",
    "retenue",
    "abandonnée",
    "abandonnee",
    "en cours",
    "en construction",
)

CARTOGRAPHY_KEYWORDS = (
    "services publics",
    "data.gouv",
)


def classify_status(raw: str) -> str:
    """Retourne 'skip', 'final' ou 'other'."""
    text = raw.strip()
    if not text:
        return "other"
    first = text.split()[0] if text.split() else text
    if first in SKIP_EMOJI or any(text.startswith(e) for e in SKIP_EMOJI):
        return "skip"
    if first in FINAL_EMOJI or any(text.startswith(e) for e in FINAL_EMOJI):
        return "final"
    lower = text.lower()
    if any(marker in lower for marker in FINAL_TEXT_MARKERS):
        return "final"
    return "other"


def extract_section(content: str, section_num: int) -> str | None:
    matches = list(SECTION_RE.finditer(content))
    for i, match in enumerate(matches):
        if int(match.group(1)) != section_num:
            continue
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        return content[start:end]
    return None


def section4_cartography_warnings(section4: str | None) -> list[str]:
    if not section4:
        return ["section §4 absente"]
    warnings: list[str] = []
    lower = section4.lower()
    has_subsections = bool(re.search(r"^###\s+", section4, re.MULTILINE))
    if not has_subsections:
        warnings.append("§4 sans sous-sections (###)")
    for keyword in CARTOGRAPHY_KEYWORDS:
        if keyword not in lower:
            warnings.append(f"mot-clé cartographie manquant : « {keyword} »")
    return warnings


def scan_idea(readme_path: Path) -> dict:
    content = readme_path.read_text(encoding="utf-8")
    folder = readme_path.parent
    match = STATUT_RE.search(content)
    raw_status = match.group(1).strip() if match else "(absent)"
    status_kind = classify_status(raw_status) if match else "other"
    has_revue = (folder / "revue.md").exists()
    section4 = extract_section(content, 4)
    carto_warnings = (
        section4_cartography_warnings(section4)
        if status_kind == "final"
        else []
    )
    return {
        "folder": folder.name,
        "path": folder,
        "status": raw_status,
        "status_kind": status_kind,
        "has_revue": has_revue,
        "carto_warnings": carto_warnings,
    }


def report(strict: bool) -> int:
    if not IDEES.is_dir():
        print(f"Dossier manquant : {IDEES}", file=sys.stderr)
        return 1

    ideas = [
        scan_idea(path)
        for path in sorted(IDEES.glob("*/README.md"))
    ]

    missing = [
        idea for idea in ideas
        if idea["status_kind"] == "final" and not idea["has_revue"]
    ]
    skipped = sum(1 for idea in ideas if idea["status_kind"] == "skip")
    finals = sum(1 for idea in ideas if idea["status_kind"] == "final")

    print(f"Idées scannées : {len(ideas)}  |  statut final : {finals}  |  ignorées : {skipped}")
    print()

    if missing:
        print(f"Sans revue.md ({len(missing)}) — revue obligatoire pour 🔁 ❌ ✅ 🚧 :")
        print(f"{'Dossier':36} {'Statut':30} {'Revue'}")
        print("-" * 72)
        for idea in missing:
            print(
                f"{idea['folder']:36} {idea['status'][:30]:30} manquante"
            )
    else:
        print("OK — toutes les idées en statut final ont un revue.md")

    print()
    carto_flagged = [
        idea for idea in ideas
        if idea["status_kind"] == "final" and idea["carto_warnings"]
    ]
    if carto_flagged:
        print("Avertissements cartographie §4 (soft) :")
        for idea in carto_flagged:
            for warning in idea["carto_warnings"]:
                print(f"  {idea['folder']:36} — {warning}")
    else:
        print("Cartographie §4 : aucun avertissement soft")

    print()
    print(
        f"Résumé : {len(missing)} sans revue / {finals} finales, "
        f"{len(carto_flagged)} avec alertes §4"
    )

    if strict and missing:
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Contrôle revue.md pour idées en statut final",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Code sortie 1 si revue manquante pour statut final",
    )
    args = parser.parse_args()
    return report(strict=args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
