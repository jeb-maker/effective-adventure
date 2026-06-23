#!/usr/bin/env python3
"""Orchestrateur de passes catalogue — manifeste JSON, promotion auto, gate."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PASSES_DIR = ROOT / "catalogue-saas" / "passes"

sys.path.insert(0, str(ROOT / "scripts"))
import catalogue_pass_lib as cpl  # noqa: E402


def cmd_init(args: argparse.Namespace) -> int:
    manifest_path = PASSES_DIR / f"{args.pass_id}.manifest.json"
    md_path = PASSES_DIR / f"{args.pass_id}.md"
    if manifest_path.exists() and not args.force:
        print(f"Existe déjà : {manifest_path} (utilisez --force)", file=sys.stderr)
        return 1
    manifest = cpl.init_manifest_template(args.pass_id, args.date)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_path.write_text(cpl.init_pass_markdown(args.pass_id, args.date), encoding="utf-8")
    print(f"Créé : {manifest_path}")
    print(f"Créé : {md_path}")
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    manifest = cpl.load_manifest(args.manifest)
    result = cpl.apply_manifest(manifest, dry_run=args.dry_run)
    if args.dry_run:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    print(
        f"pass {result['pass_id']}: +{result['added_total']} ajouts, "
        f"{result['verified_count']} verify updates"
    )
    if result["added_ids"]:
        print("  ajouts:", ", ".join(result["added_ids"]))
    b, a = result["before"], result["after"]
    print(
        f"  métriques: {b['total']}→{a['total']} vendeurs, "
        f"verified {b['verified']}→{a['verified']}, "
        f"listicle {b['listicle']}→{a['listicle']}"
    )
    if not args.no_freeze:
        return cpl.run_saturation_freeze()
    return 0


def cmd_promote(args: argparse.Namespace) -> int:
    segments: set[str] | None = None
    if args.retravailler:
        segments = cpl.retravailler_segment_ids()
        print(f"Segments 🔁 : {len(segments)}")
    if args.segment:
        segments = (segments or set()) | set(args.segment)

    eligible = cpl.eligible_for_promotion(
        segments=segments,
        france_market=args.france_market,
    )
    if args.limit:
        eligible = eligible[: args.limit]

    ids = [v["id"] for v in eligible]
    if args.dry_run:
        print(f"{len(ids)} promotion(s) éligible(s)")
        for v in eligible:
            print(f"  {v['id']:32} {v['name']}")
        return 0

    if not ids:
        print("Aucun candidat verify-eligible.")
        return 0

    pass_id = args.pass_id or f"auto-verify-{cpl.today()}"
    count = cpl.promote_verified(ids, pass_id, pricing_note=args.pricing_note)
    print(f"Promu {count} vendeur(s) → verified (pass {pass_id})")
    if not args.no_freeze:
        return cpl.run_saturation_freeze()
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    """Applique le manifeste puis exécute le gate complet."""
    rc = cmd_apply(args)
    if rc != 0:
        return rc
    gate_cmd = [sys.executable, str(ROOT / "scripts" / "catalogue_saas.py"), "gate"]
    if args.no_idees:
        gate_cmd.append("--no-idees")
    return subprocess.call(gate_cmd, cwd=ROOT)


def cmd_weekly(args: argparse.Namespace) -> int:
    """Passe hebdo cartographie : promote auto + gate."""
    promote_args = argparse.Namespace(
        retravailler=True,
        segment=None,
        france_market=args.france_market,
        limit=args.limit,
        pass_id=args.pass_id or f"auto-weekly-{cpl.today()}",
        pricing_note=None,
        dry_run=args.dry_run,
        no_freeze=False,
    )
    rc = cmd_promote(promote_args)
    if rc != 0 or args.dry_run:
        return rc
    gate_cmd = [sys.executable, str(ROOT / "scripts" / "catalogue_saas.py"), "gate"]
    return subprocess.call(gate_cmd, cwd=ROOT)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Passes catalogue SaaS — manifeste JSON et automation"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="Créer manifeste + journal vides")
    p_init.add_argument("pass_id", help="ex. 2026-06-v6j-my-pass")
    p_init.add_argument("--date", help="YYYY-MM-DD (défaut: aujourd'hui)")
    p_init.add_argument("--force", action="store_true")

    p_apply = sub.add_parser("apply", help="Appliquer un manifeste JSON")
    p_apply.add_argument("manifest", type=Path)
    p_apply.add_argument("--dry-run", action="store_true")
    p_apply.add_argument("--no-freeze", action="store_true")

    p_run = sub.add_parser("run", help="apply + catalogue_saas.py gate")
    p_run.add_argument("manifest", type=Path)
    p_run.add_argument("--dry-run", action="store_true")
    p_run.add_argument("--no-freeze", action="store_true")
    p_run.add_argument("--no-idees", action="store_true")

    p_promote = sub.add_parser("promote", help="Promouvoir candidats verify-eligible")
    p_promote.add_argument("--limit", type=int, default=20)
    p_promote.add_argument("--segment", action="append", help="Filtrer segment(s)")
    p_promote.add_argument(
        "--retravailler",
        action="store_true",
        help="Limiter aux segments des idées 🔁",
    )
    p_promote.add_argument("--france-market", choices=["strong", "partial", "absent", "unknown"])
    p_promote.add_argument("--pass-id")
    p_promote.add_argument("--pricing-note")
    p_promote.add_argument("--dry-run", action="store_true")
    p_promote.add_argument("--no-freeze", action="store_true")

    p_weekly = sub.add_parser(
        "weekly",
        help="Promotion auto (🔁, limit N) + gate — passe hebdo cartographie",
    )
    p_weekly.add_argument("--limit", type=int, default=20)
    p_weekly.add_argument("--france-market", choices=["strong", "partial", "absent", "unknown"])
    p_weekly.add_argument("--pass-id")
    p_weekly.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()
    handlers = {
        "init": cmd_init,
        "apply": cmd_apply,
        "run": cmd_run,
        "promote": cmd_promote,
        "weekly": cmd_weekly,
    }
    return handlers[args.command](args)


if __name__ == "__main__":
    raise SystemExit(main())
