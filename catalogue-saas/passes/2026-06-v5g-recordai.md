# Passe V5g — 2e L3 parsing-inbox + compliance-to-spec + idée RecordAI

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5g-parsing-compliance` |
| Date | 2026-06-22 |

## Enrichissement catalogue

| Segment | Ajoutés | Exemples |
|---|---:|---|
| `parsing-inbox` | +8 | Unipile (FR), Unstract, CloudMailin, Gmail/Graph API |
| `compliance-to-spec` | +8 | TrustArc, Regulativ.ai, Camunda, ComplianceCow, Conformiq |

Patches : Extend, Sensible, Reducto → `parsing-inbox`

## Idée produit

- [`idees/0029-recordai/README.md`](../../idees/0029-recordai/README.md) — Work-as-a-Service email/PDF → dossier validé
- Segments catalogue liés : `parsing-inbox`, `document-idp`, `compliance-to-spec`, `automation-platforms`

## Scripts

```bash
python3 scripts/enrich_catalogue_v5g.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py saturation --segment parsing-inbox  # si implémenté
```
