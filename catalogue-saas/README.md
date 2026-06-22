# Catalogue SaaS — veille marché

Registre **curaté** de SaaS comparables (RegTech, IDP, GRC, agents IA…), aligné sur
les règles de preuve du dépôt.

- **Méthode** : [`docs/catalogue-saas-methode.md`](../docs/catalogue-saas-methode.md)
- **Taxonomie** : [`taxonomy.json`](taxonomy.json)
- **Schéma** : [`schema/vendor.schema.json`](schema/vendor.schema.json)
- **Données** : [`vendors/`](vendors/) (un fichier JSON par segment)

## État (vague 1 — 2026-06-22)

| Segment | Fichier | Entrées |
|---|---|---:|
| RegTech | `vendors/regtech.json` | 13 |
| GRC & sécurité | `vendors/grc-security.json` | 11 |
| AI Governance | `vendors/ai-governance.json` | 8 |
| IDP & extraction | `vendors/document-idp.json` | 16 |
| Parsing inbox | `vendors/parsing-inbox.json` | 5 |
| Copilots & dev | `vendors/ai-copilot-dev.json` | 6 |
| Support & sales agents | `vendors/support-sales-agents.json` | 6 |
| Automatisation | `vendors/automation-platforms.json` | 3 |

**Total : 68 vendeurs** (vague initiale issue des échanges IA SaaS / RegTech / IDP).

> Segment `compliance-to-spec` (réglementation → spec produit testable) : **aucun
> acteur dédié recensé** pour l'instant — créneau identifié comme émergent.

## Commandes

```bash
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py export -o catalogue-saas/exports/vendors.csv
python3 scripts/catalogue_saas.py build-db
```

## Enrichir

1. Choisir un segment dans `taxonomy.json`.
2. Ajouter une entrée dans le fichier `vendors/<segment>.json`.
3. Renseigner `source_url` + `source_consulted_at` (obligatoire).
4. Lancer `validate` avant commit.

## Limites

- Non exhaustif : objectif veille, pas annuaire mondial.
- `partial` = profil ou pricing à reconfirmer sur le site officiel.
- Ne pas utiliser `unverified` pour scorer une fiche idée.
