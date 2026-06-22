# Catalogue SaaS — veille marché

Registre **curaté** de SaaS comparables, aligné sur les règles de preuve du dépôt.

| Ressource | Description |
|---|---|
| [`taxonomy.json`](taxonomy.json) | **68 segments** en **18 catégories** (source canonique) |
| [`SEGMENTS.md`](SEGMENTS.md) | Liste complète générée (`python3 scripts/catalogue_saas.py list-segments`) |
| [`vendors/`](vendors/) | Un fichier JSON par segment |
| [`docs/catalogue-saas-methode.md`](../docs/catalogue-saas-methode.md) | Méthode d'enrichissement |
| [`docs/catalogue-saas-exhaustivite.md`](../docs/catalogue-saas-exhaustivite.md) | Méthode L2/L3 et tagging géo |
| [`passes/`](passes/) | Journal des passes de moisson |
| [`coverage-matrix.json`](coverage-matrix.json) | Matrice segment × sources |

## État (2026-06-22)

- **68 segments** définis (tous avec fichier `vendors/<id>.json`)
- **68 segments peuplés** (vague 4)
- **481 vendeurs** recensés (vagues 5b–5d)
- **Tagging géo** : `hq_country`, `france_market`, `operating_regions` (vague 5a)

## Les 18 catégories

1. Compliance & réglementation (10)
2. Sécurité informatique (5)
3. Infrastructure IA (5)
4. Documents & données (5)
5. IA au travail (5)
6. Automatisation (2)
7. Agents & résultats (2)
8. Sales & marketing (4)
9. Expérience client (2)
10. Vertical — Finance (3)
11. Vertical — Legal (1)
12. Vertical — RH (3)
13. Vertical — Santé (2)
14. Vertical — Industrie (6)
15. Données B2B (1)
16. Data & analytics (2)
17. France — secteur public (3)
18. France — open data thématique (7)

→ Détail segment par segment : **[SEGMENTS.md](SEGMENTS.md)**

## Commandes

```bash
# Synchroniser taxonomie → fichiers vendors/ vides
python3 scripts/sync_taxonomy_segments.py

# Enrichissement par vague (idempotent)
python3 scripts/tag_catalogue_geography_v5a.py
python3 scripts/enrich_catalogue_v4.py
python3 scripts/enrich_compliance_to_spec_v5b.py
python3 scripts/enrich_catalogue_v5c.py
python3 scripts/enrich_catalogue_v5d.py

# Exhaustivité
python3 scripts/catalogue_saas.py coverage
python3 scripts/catalogue_saas.py gaps --segment compliance-to-spec

# Régénérer la liste markdown
python3 scripts/catalogue_saas.py list-segments

python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py export -o catalogue-saas/exports/vendors.csv
```

## Ajouter un segment

1. Éditer `scripts/sync_taxonomy_segments.py` → tuple dans `ALL_SEGMENTS`
2. `python3 scripts/sync_taxonomy_segments.py`
3. `python3 scripts/catalogue_saas.py list-segments`

## Enrichir un segment

1. Choisir un `id` dans [SEGMENTS.md](SEGMENTS.md)
2. Ajouter des entrées dans `vendors/<id>.json`
3. `source_url` + `source_consulted_at` obligatoires
4. `python3 scripts/catalogue_saas.py validate`
