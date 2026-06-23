# Passe V5h — 3e L3 parsing-inbox + compliance-to-spec (dossier validé)

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5h-dossier-valide` |
| Date | 2026-06-23 |

## Enrichissement catalogue

| Segment | Ajoutés | Exemples |
|---|---:|---|
| `parsing-inbox` | +8 | Dext, Levity, Indico, Pipefy, Tonkean |
| `compliance-to-spec` | +8 | DiliTrust (FR), Yooz (FR), Libeo (FR), Formalize, Inscribe |

Patches : Hyperscience, Ocrolus → `parsing-inbox`

## Contexte idée RecordAI

- [`idees/0029-recordai/README.md`](../../idees/0029-recordai/README.md) — analyse rigoureuse complétée (score 66, 🔁)
- Focus moisson : acteurs avec **boucle validation humaine** et **dossier audité**, pas seulement extraction brute.

## Scripts

```bash
python3 scripts/enrich_catalogue_v5h.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py saturation
```
