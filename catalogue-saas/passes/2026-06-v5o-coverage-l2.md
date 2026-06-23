# Passe V5o — backfill coverage L2 (post V5l–V5n)

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5o-coverage-l2` |
| Date | 2026-06-23 |

## Objectif

Compléter la **matrice de couverture** pour les 46 segments passés de L1 (~5 entrées) à L2 (~11 entrées) via V5l, V5m, V5n.

Sources backfillées : `capterra`, `open_source`, `analyst_report`, `geo_digest` (là où absentes).

## État catalogue

- **914 vendeurs** uniques
- **0 segment** avec ≤ 6 entrées fichier
- Cible L2 atteinte sur l'ensemble des 68 segments

## Script

```bash
python3 scripts/enrich_catalogue_v5o_coverage.py
python3 scripts/catalogue_saas.py coverage
python3 scripts/catalogue_saas.py validate
```
