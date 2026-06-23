# Passe V5i — document-idp human-in-the-loop (RecordAI)

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5i-document-idp` |
| Date | 2026-06-23 |

## Enrichissement catalogue

| Segment | Ajoutés | Exemples |
|---|---:|---|
| `document-idp` | +16 | Ephesoft, Alkymi, DocDigitizer, Natif.ai, Microsoft Syntex, Cascading AI |

Focus moisson : acteurs avec **poste de validation humaine**, **QC dossier** et **audit trail** — complémentaire aux extracteurs API-first déjà catalogués (Textract, Rossum, etc.).

## Contexte idée RecordAI

- [`idees/0029-recordai/README.md`](../../idees/0029-recordai/README.md) — Work-as-a-Service email/PDF → dossier validé
- Segment stratégique : `document-idp` (32 → 48 entrées)

## Scripts

```bash
python3 scripts/enrich_catalogue_v5i.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation
```
