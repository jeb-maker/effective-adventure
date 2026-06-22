#!/usr/bin/env python3
"""Outils pour le catalogue SaaS (validation, stats, export, SQLite)."""

from __future__ import annotations

import argparse
import csv
import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "catalogue-saas"
TAXONOMY_PATH = CATALOGUE / "taxonomy.json"
VENDORS_DIR = CATALOGUE / "vendors"


def load_taxonomy() -> dict:
    with TAXONOMY_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def load_vendor_files() -> list[tuple[str, dict]]:
    files: list[tuple[str, dict]] = []
    for path in sorted(VENDORS_DIR.glob("*.json")):
        with path.open(encoding="utf-8") as f:
            files.append((path.name, json.load(f)))
    return files


def iter_vendors() -> list[dict]:
    vendors: list[dict] = []
    for _, data in load_vendor_files():
        vendors.extend(data.get("vendors", []))
    return vendors


def validate() -> int:
    taxonomy = load_taxonomy()
    segment_ids = {s["id"] for s in taxonomy["segments"]}
    pricing_models = set(taxonomy["pricing_models"])
    target_markets = set(taxonomy["target_markets"])
    statuses = set(taxonomy["verification_statuses"])

    errors: list[str] = []
    seen_ids: set[str] = set()

    required = {
        "id",
        "name",
        "url",
        "segments",
        "description",
        "capabilities",
        "pricing_model",
        "target_market",
        "source_url",
        "source_consulted_at",
        "verification_status",
    }

    for filename, data in load_vendor_files():
        for i, vendor in enumerate(data.get("vendors", [])):
            prefix = f"{filename}[{i}] {vendor.get('id', '?')}"

            missing = required - vendor.keys()
            if missing:
                errors.append(f"{prefix}: champs manquants {sorted(missing)}")
                continue

            vid = vendor["id"]
            if vid in seen_ids:
                errors.append(f"{prefix}: id dupliqué '{vid}'")
            seen_ids.add(vid)

            for seg in vendor["segments"]:
                if seg not in segment_ids:
                    errors.append(f"{prefix}: segment inconnu '{seg}'")

            if vendor["pricing_model"] not in pricing_models:
                errors.append(
                    f"{prefix}: pricing_model inconnu '{vendor['pricing_model']}'"
                )

            if vendor["target_market"] not in target_markets:
                errors.append(
                    f"{prefix}: target_market inconnu '{vendor['target_market']}'"
                )

            if vendor["verification_status"] not in statuses:
                errors.append(
                    f"{prefix}: verification_status invalide"
                )

            if len(vendor["description"]) < 10:
                errors.append(f"{prefix}: description trop courte")

    if errors:
        print("VALIDATION ÉCHOUÉE", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK — {len(seen_ids)} vendeurs, {len(load_vendor_files())} fichiers segment")
    return 0


def stats() -> None:
    vendors = iter_vendors()
    taxonomy = load_taxonomy()
    seg_labels = {s["id"]: s["label"] for s in taxonomy["segments"]}

    print(f"Total vendeurs : {len(vendors)}")
    print()

    by_segment: Counter[str] = Counter()
    for v in vendors:
        for seg in v["segments"]:
            by_segment[seg] += 1

    print("Par segment :")
    for seg_id, count in by_segment.most_common():
        label = seg_labels.get(seg_id, seg_id)
        print(f"  {seg_id:24} {count:3}  {label}")

    print()
    print("Par pricing_model :")
    for model, count in Counter(v["pricing_model"] for v in vendors).most_common():
        print(f"  {model:20} {count}")

    print()
    print("Par verification_status :")
    for status, count in Counter(
        v["verification_status"] for v in vendors
    ).most_common():
        print(f"  {status:12} {count}")


def export_csv(output: Path) -> None:
    vendors = iter_vendors()
    output.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "id",
        "name",
        "url",
        "segments",
        "description",
        "capabilities",
        "pricing_model",
        "pricing_notes",
        "target_market",
        "geography",
        "verification_status",
        "source_url",
        "source_consulted_at",
        "notes",
    ]

    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for v in vendors:
            row = {k: v.get(k, "") for k in fieldnames}
            row["segments"] = "|".join(v["segments"])
            row["capabilities"] = "|".join(v["capabilities"])
            writer.writerow(row)

    print(f"Export CSV : {output} ({len(vendors)} lignes)")


def build_db(db_path: Path) -> None:
    vendors = iter_vendors()
    db_path.parent.mkdir(parents=True, exist_ok=True)

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE vendors (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            url TEXT NOT NULL,
            segments TEXT NOT NULL,
            description TEXT NOT NULL,
            capabilities TEXT NOT NULL,
            pricing_model TEXT NOT NULL,
            pricing_notes TEXT,
            target_market TEXT NOT NULL,
            geography TEXT,
            verification_status TEXT NOT NULL,
            source_url TEXT NOT NULL,
            source_consulted_at TEXT NOT NULL,
            notes TEXT
        )
        """
    )

    for v in vendors:
        cur.execute(
            """
            INSERT INTO vendors VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                v["id"],
                v["name"],
                v["url"],
                json.dumps(v["segments"]),
                v["description"],
                json.dumps(v["capabilities"]),
                v["pricing_model"],
                v.get("pricing_notes"),
                v["target_market"],
                v.get("geography"),
                v["verification_status"],
                v["source_url"],
                v["source_consulted_at"],
                v.get("notes"),
            ),
        )

    conn.commit()
    conn.close()
    print(f"SQLite : {db_path} ({len(vendors)} lignes)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Catalogue SaaS — outils")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="Valider JSON et références taxonomy")
    sub.add_parser("stats", help="Statistiques par segment")

    p_export = sub.add_parser("export", help="Exporter en CSV")
    p_export.add_argument("--format", choices=["csv"], default="csv")
    p_export.add_argument(
        "-o",
        "--output",
        type=Path,
        default=CATALOGUE / "exports" / "vendors.csv",
    )

    p_db = sub.add_parser("build-db", help="Générer SQLite")
    p_db.add_argument(
        "--db",
        type=Path,
        default=CATALOGUE / "catalogue.db",
    )

    args = parser.parse_args()

    if args.command == "validate":
        return validate()
    if args.command == "stats":
        stats()
        return 0
    if args.command == "export":
        export_csv(args.output)
        return 0
    if args.command == "build-db":
        build_db(args.db)
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
