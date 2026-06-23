# Méthode — catalogue des SaaS (veille marché)

Ce document décrit **comment répertorier, stocker et enrichir** un catalogue de
SaaS concurrents / comparables, en cohérence avec les règles de preuve du dépôt
(voir [`methode-analyse.md`](methode-analyse.md)).

---

## 1. Objectif

Alimenter le **pipeline de discovery produit** du dépôt (voir §0 de
[`methode-analyse.md`](methode-analyse.md)) :

- cartographier l'existant par segment (RegTech, IDP, GRC, agents IA…) ;
- comparer modèles de pricing et positionnement ;
- alimenter les sections « Existant / concurrence » des fiches idées ;
- détecter les créneaux peu couverts (ex. réglementation → spec produit testable).

**Ce n'est pas** une base exhaustive du marché SaaS mondial : c'est un **registre
curaté**, enrichi par vagues thématiques, avec sources datées.

---

## 2. Où stocker ? (recommandation)

| Approche | Quand l'utiliser | Avantages | Inconvénients |
|---|---|---|---|
| **Fichiers JSON versionnés** (choix actuel) | MVP, équipe petite, Git comme source de vérité | diffable, pas d'infra, reproductible | requêtes complexes manuelles |
| **SQLite** (`catalogue-saas/catalogue.db`) | >500 entrées, exports fréquents, filtres SQL | requêtes rapides, un fichier portable | moins lisible en revue humaine |
| **PostgreSQL / Supabase** | app produit, multi-utilisateurs, API publique | temps réel, auth, recherche full-text | surdimensionné pour de la veille seule |

### Choix retenu pour ce dépôt

```
catalogue-saas/
  taxonomy.json          # segments, tags, modèles de pricing
  schema/vendor.schema.json
  vendors/
    regtech.json
    grc-security.json
    ai-governance.json
    document-idp.json
    parsing-inbox.json
    ai-copilot-dev.json
    support-sales-agents.json
    automation-platforms.json
  exports/               # CSV générés (gitignored ou commit ponctuel)
scripts/catalogue_saas.py
```

**Principe** : JSON = source de vérité ; SQLite/CSV = vues dérivées générées par script.

Pour l'exhaustivité L2/L3 et le tagging géographique, voir [`catalogue-saas-exhaustivite.md`](catalogue-saas-exhaustivite.md).

La taxonomie complète (68 segments, 18 catégories) est dans [`catalogue-saas/taxonomy.json`](../catalogue-saas/taxonomy.json). Voir [`catalogue-saas/README.md`](../catalogue-saas/README.md) pour la liste à jour.

---

## 3. Schéma d'une entrée

Chaque vendeur (`vendor`) contient au minimum :

| Champ | Obligatoire | Description |
|---|---|---|
| `id` | oui | slug stable (`intercom-fin`) |
| `name` | oui | nom commercial |
| `url` | oui | site ou page produit |
| `segments` | oui | ids de `taxonomy.json` |
| `description` | oui | 1–3 phrases factuelles |
| `capabilities` | oui | liste de capacités observées |
| `pricing_model` | oui | enum (voir taxonomy) |
| `pricing_notes` | non | détail public si connu |
| `target_market` | oui | `self_serve` \| `smb` \| `mid_market` \| `enterprise` |
| `source_url` | oui | URL de la preuve (page pricing, doc, article) |
| `source_consulted_at` | oui | date ISO (`2026-06-22`) |
| `verification_status` | oui | `verified` \| `partial` \| `unverified` |
| `hq_country` | non | ISO 3166-1 alpha-2 ou `unknown` |
| `france_market` | non | `strong` \| `partial` \| `absent` \| `unknown` |
| `operating_regions` | non | zones documentées (`FR`, `EU`, `US`…) |
| `discovery_source` | non | type de source (voir taxonomy) |
| `discovery_pass` | non | identifiant de passe (`2026-06-v5b-…`) |
| `founded_year` | oui* | année création acteur ; `null` si inconnu |
| `founded_year_source` | non | URL ou note datée justifiant `founded_year` |
| `entry_ai_generated` | oui* | `true` = fiche produite par pipeline agent/auto |

\* Obligatoire après `tag_catalogue_provenance_v1.py`. Overrides : `catalogue-saas/founded-years-overrides.json`.

Règle : **`unverified` interdit dans les exports utilisés pour scorer une idée**.

---

## 4. Workflow d'enrichissement (vagues)

1. **Définir un segment** (ex. RegTech EU, IDP API, AI governance).
2. **Recherche web** : lister candidats avec URL + date.
3. **Ajouter / mettre à jour** le fichier JSON du segment.
4. **Valider** : `python3 scripts/catalogue_saas.py validate`
5. **Exporter** : `python3 scripts/catalogue_saas.py export --format csv`
6. **Indexer** : mettre à jour `catalogue-saas/README.md` (compteurs par segment).

Fréquence suggérée : **1 vague / semaine** par segment prioritaire, pas un big-bang.

---

## 5. Sources prioritaires

- sites officiels (pricing, docs produit) ;
- rapports analystes (IDC MarketScape, comparatifs datés) ;
- pages de comparaison **avec prudence** (vérifier sur le site du vendeur) ;
- listes sectorielles (RegTech Analyst, comparatifs IDP).

Ne pas scraper agressivement : préférer l'ajout manuel curaté + date de consultation.

---

## 6. Limites connues

- Impossible de lister « tous les SaaS » : marché en mouvement, fusion/acquisitions.
- Le pricing public est souvent absent (enterprise sur devis).
- Un outil peut appartenir à **plusieurs segments** (`segments` multiple).
- La catégorie « compliance-to-product-spec » reste **peu peuplée** : signal d'opportunité, pas de vide absolu.

---

## 7. Commandes utiles

```bash
# Valider le schéma et les références taxonomy
python3 scripts/catalogue_saas.py validate

# Statistiques par segment
python3 scripts/catalogue_saas.py stats

# Export CSV consolidé
python3 scripts/catalogue_saas.py export --format csv -o catalogue-saas/exports/vendors.csv

# Générer SQLite (optionnel)
python3 scripts/catalogue_saas.py build-db
```
