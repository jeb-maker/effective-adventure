# Catalogue SaaS — veille marché

Registre **curaté** de SaaS comparables, aligné sur les règles de preuve du dépôt.

| Ressource | Description |
|---|---|
| [`taxonomy.json`](taxonomy.json) | **68 segments** en **18 catégories** (source canonique) |
| [`SEGMENTS.md`](SEGMENTS.md) | Liste complète générée (`python3 scripts/catalogue_saas.py list-segments`) |
| [`vendors/`](vendors/) | Un fichier JSON par segment |
| [`docs/catalogue-saas-methode.md`](../docs/catalogue-saas-methode.md) | Méthode d'enrichissement |
| [`docs/catalogue-saas-exhaustivite.md`](../docs/catalogue-saas-exhaustivite.md) | Méthode L2/L3 et tagging géo |
| [`idees/catalogue-segments.json`](../idees/catalogue-segments.json) | Liaison idées → segments |
| [`passes/`](passes/) | Journal des passes de moisson |
| [`coverage-matrix.json`](coverage-matrix.json) | Matrice segment × sources |

## État (2026-06-23)

- **68 segments** définis (tous avec fichier `vendors/<id>.json`)
- **68 segments peuplés** — profondeur inventaire **≥ 18 entrées** par segment
- **1 425 vendeurs** recensés (vagues 5b–5u + **V6 pilote–c**)
- **Saturation marché** : **6/68 segments gelés** — voir `frozen-segments.json` et `segment-readiness`
- **Vérification** : **83 verified** / 1425 — cible : monter via `verify-eligible` + passes V6
- **29 idées** liées au catalogue (`idees/catalogue-segments.json`)
- **Surveillance** : `frozen-segments.json` + `saturation watch`

> **Ne pas confondre** profondeur inventaire (≥ 18) et saturation (< 5 %).
> Un segment « peuplé » n'est **pas** un marché clos. Voir
> [`docs/cartographie-existant.md`](../docs/cartographie-existant.md) §3.

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
python3 scripts/enrich_catalogue_v5e.py
python3 scripts/enrich_catalogue_v5f.py
python3 scripts/enrich_catalogue_v5g.py
python3 scripts/enrich_catalogue_v5h.py
python3 scripts/enrich_catalogue_v5i.py
python3 scripts/enrich_catalogue_v5j.py
python3 scripts/enrich_catalogue_v5k.py
python3 scripts/enrich_catalogue_v5l.py
python3 scripts/enrich_catalogue_v5m.py
python3 scripts/enrich_catalogue_v5n.py
python3 scripts/enrich_catalogue_v5o_coverage.py
python3 scripts/enrich_catalogue_v5p.py
python3 scripts/enrich_catalogue_v5q.py
python3 scripts/enrich_catalogue_v5r.py
python3 scripts/enrich_catalogue_v5s.py
python3 scripts/enrich_catalogue_v5t_security.py
python3 scripts/enrich_catalogue_v5t_verticals.py
python3 scripts/enrich_catalogue_v5t_workplace.py
python3 scripts/enrich_catalogue_v5u_fill_last4.py
python3 scripts/enrich_catalogue_v6_pilot.py   # V6 pilote verified + gaps revues 0001/0029
python3 scripts/enrich_catalogue_v6b.py        # V6b procurement + parsing/IDP verified
python3 scripts/enrich_catalogue_v6c.py        # V6c FR gaps + RecordAI verified + freeze
python3 scripts/sync_idees_catalogue.py

# Automation passes (manifeste JSON — voir passes/manifest.example.json)
python3 scripts/catalogue_pass.py init 2026-07-ma-passe    # manifeste + journal vides
python3 scripts/catalogue_pass.py run passes/….manifest.json  # apply + gate
python3 scripts/catalogue_pass.py weekly --limit 20 --dry-run   # promote auto 🔁
python3 scripts/catalogue_saas.py verify-promote --retravailler --limit 20
python3 scripts/catalogue_saas.py gate                         # validate + revues + listicle

# Provenance acteur (depuis quand + fiche générée IA)
python3 scripts/tag_catalogue_provenance_v1.py                   # rétro-tag
python3 scripts/catalogue_saas.py provenance-report
# Overrides founded_year : catalogue-saas/founded-years-overrides.json

# Découverte secteurs / acteurs (semi-auto — voir docs/cartographie-existant.md)
python3 scripts/catalogue_discover.py plan --retravailler
python3 scripts/catalogue_discover.py brief SEGMENT_ID
python3 scripts/catalogue_discover.py scan SEGMENT_ID --manifest

# Saturation (passes réelles vs seuil 5 %)
python3 scripts/catalogue_saas.py saturation
python3 scripts/catalogue_saas.py saturation watch   # [SATURÉ] / [PROCHE] par passe
python3 scripts/catalogue_saas.py saturation freeze  # → frozen-segments.json

# Exhaustivité
python3 scripts/catalogue_saas.py coverage
python3 scripts/catalogue_saas.py gaps --segment compliance-to-spec

# Régénérer la liste markdown
python3 scripts/catalogue_saas.py list-segments

python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py segment-readiness
python3 scripts/catalogue_saas.py audit-sources
python3 scripts/catalogue_saas.py verify-eligible
python3 scripts/catalogue_saas.py export -o catalogue-saas/exports/vendors.csv
```

## Explorer web (+ RAG)

Interface **100 % JavaScript** (filtres, stats, RAG TF-IDF dans le navigateur).

**En ligne** (après merge sur `main` + activation Pages) :
**https://jeb-maker.github.io/effective-adventure/**

```bash
# 1. Générer le bundle JSON (après enrichissement catalogue)
node explorer/build.mjs

# 2. Servir l'UI en local (fetch nécessite un serveur HTTP)
cd explorer && npm start
# → http://127.0.0.1:8765
```

Le déploiement GitHub Pages est automatisé via [`.github/workflows/pages.yml`](../.github/workflows/pages.yml)
(merge sur `main` → rebuild bundle → publication).

Fichiers : [`explorer/`](../explorer/) · `catalogue-bundle.json` (généré par `build.mjs`).

Après une vague d'enrichissement, relancer `node explorer/build.mjs` pour rafraîchir le bundle.

## Ajouter un segment

1. Éditer `scripts/sync_taxonomy_segments.py` → tuple dans `ALL_SEGMENTS`
2. `python3 scripts/sync_taxonomy_segments.py`
3. `python3 scripts/catalogue_saas.py list-segments`

## Enrichir un segment

1. Choisir un `id` dans [SEGMENTS.md](SEGMENTS.md)
2. Ajouter des entrées dans `vendors/<id>.json`
3. `source_url` + `source_consulted_at` obligatoires
4. `python3 scripts/catalogue_saas.py validate`
