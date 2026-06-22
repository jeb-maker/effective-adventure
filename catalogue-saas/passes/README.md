# Journal des passes de moisson

Chaque passe documente une session d'enrichissement **reproductible** pour un segment ou une vague.

## Template de passe

Créer `YYYY-MM-<segment>.md` avec :

1. **Segment** et niveau visé (L1 / L2 / L3)
2. **Date** et identifiant (`discovery_pass`)
3. **Sources consultées** (URL, requête, nb candidats bruts)
4. **Résultats** (nouveaux, doublons, patches cross-segments)
5. **Saturation** (taux nouveaux / candidats ; seuil 5 %)
6. **Prochaine passe** (sources manquantes)

## Fichiers liés

| Fichier | Rôle |
|---|---|
| [`coverage-matrix.json`](../coverage-matrix.json) | État machine-readable par segment × source |
| [`scripts/enrich_*`](../scripts/) | Scripts d'import idempotents |
| [`passes/`](./) | Journal humain des moissons |

## Commandes

```bash
python3 scripts/catalogue_saas.py coverage
python3 scripts/catalogue_saas.py gaps --segment compliance-to-spec
python3 scripts/catalogue_saas.py gaps --hq US --france-market absent
```
