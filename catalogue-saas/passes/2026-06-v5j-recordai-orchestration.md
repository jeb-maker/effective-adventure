# Passe V5j — automation-platforms orchestration (RecordAI)

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5j-recordai-orchestration` |
| Date | 2026-06-23 |

## Enrichissement catalogue

| Segment | Ajoutés | Exemples |
|---|---:|---|
| `automation-platforms` | +12 | Windmill, Relay.app, Celonis, Flowable, Temporal, Retool Workflows |

Focus moisson : plateformes **orchestration**, **human-in-the-loop**, **audit trail** et **connecteurs email/documents** — complémentaire aux iPaaS généralistes déjà catalogués (Zapier, Make, Workato).

## Patches cross-segment

| ID | Segment ajouté | Fichier source |
|---|---|---|
| `laiye` | `automation-platforms` | document-idp |
| `camunda` | `automation-platforms` | compliance-to-spec |
| `kissflow`, `pipefy`, `tonkean`, `levity`, `dext` | `automation-platforms` | parsing-inbox |

## Contexte idée RecordAI

- [`idees/0029-recordai/README.md`](../../idees/0029-recordai/README.md) — Work-as-a-Service email/PDF → dossier validé
- Segment stratégique : `automation-platforms` (9 → 21 entrées, +7 patches cross-segment)

## Scripts

```bash
python3 scripts/enrich_catalogue_v5j.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation
```
