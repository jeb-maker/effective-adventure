# Observatoire de qualité des données publiques

- **ID** : 0002
- **Statut** : 🔁 À retravailler
- **Score** : 57 / 100
- **Dernière mise à jour** : 2026-06-20
- **Révision critique** : voir [`revue.md`](revue.md) — score abaissé de **71 à 57**
  après audit adversarial (existant public sous-estimé : udata-hydra, Observatoire
  OpenDataFrance, validation schéma intégrée, modèle transport).
- **Pitch (1 phrase)** : Monitoring **continu et transversal** de la qualité
  réelle des jeux de données ouverts (liens morts, fichiers illisibles,
  fraîcheur, dérive de schéma), orienté **producteurs** — généraliser à tous les
  domaines ce que fait déjà transport.data.gouv.fr.

---

## 1. Problème / douleur
Les réutilisateurs perdent un temps fou sur des ressources mortes, des CSV
cassés, des données périmées ou des colonnes qui disparaissent d'une version à
l'autre. Les producteurs (collectivités, ministères) sont peu outillés pour
détecter ces régressions en continu.

## 2. Cible & qui paie
- **Réutilisateurs (devs/data)** : en profitent mais paient peu.
- **Producteurs (collectivités, ministères, éditeurs de logiciels métier)** :
  cible solvable (obligation légale de publier) **mais cycle de vente public
  lent**. → C'est LE point faible de l'idée (voir §11).

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| API catalogue data.gouv.fr (champ `quality`, `last_update`) | https://www.data.gouv.fr/api/1/ | Licence Ouverte | JSON | continue | `quality` ne couvre que les métadonnées |
| Validata (validation Table Schema) | https://validata.fr/ — API : https://api.validata.etalab.studio/apidocs | Open source | API | à la demande | Nécessite un schéma de référence |
| schema.data.gouv.fr | https://schema.data.gouv.fr/ | — | — | — | Tous les datasets n'ont pas de schéma |
| Modèle de référence (transport) | https://doc.transport.data.gouv.fr/outils/outils-disponibles-sur-le-pan/indicateurs-de-qualite | — | — | dispo/conformité/fraîcheur historisés | Limité au domaine transport |

## 4. Existant / concurrence

> Cartographie B (consultée 2026-06-23). Verdict : **fragmenté**, pas de produit
> transversal « monitoring qualité données » au niveau national.

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **Etalab / data.gouv.fr** | https://www.data.gouv.fr/ | Score qualité métadonnées natif, API catalogue |
| **schema.data.gouv.fr** | https://schema.data.gouv.fr/ | Schémas Table Schema de référence |
| **transport.data.gouv.fr** | https://doc.transport.data.gouv.fr/outils/outils-disponibles-sur-le-pan/indicateurs-de-qualite | Modèle indicateurs dispo/conformité/fraîcheur (transport) |
| **Observatoire OpenDataFrance** | https://www.opendatafrance.org/ | Veille écosystème open data FR |

### Réutilisations data.gouv

| Acteur | URL | Rôle |
|---|---|---|
| **Validata** | https://validata.fr/ | Validation fichier vs schéma (à la demande, pas monitoring continu) |
| **udata-hydra** (Etalab) | https://github.com/opendatateam/udata-hydra | Crawling URLs ressources — infra qualité liens |
| **Guides qualité Etalab** | https://guides.data.gouv.fr/guides/guide-qualite/ | Méthode amélioration score métadonnées |

Champ `quality` API data.gouv, distinction `last_update`/`last_modified` :
https://dawap.fr/actualites-developpement/integration-api-data-gouv-fr-services-publics-open-data
(Sources consultées 2026-06-20.)

### Produits commerciaux

Opendatasoft/Huwise, Toucan Toco, Fairness, Sifflet (data observability) —
segments `open-data-governance-fr` et `data-observability` du catalogue (voir ci-dessous).

### Bricolage

Great Expectations, Soda, scripts cron sur API catalogue — souvent le vrai
concurrent des équipes data internes.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0002-observatoire-qualite-donnees` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `open-data-governance-fr` — Gouvernance open data FR

Fichier : [`catalogue-saas/vendors/open-data-governance-fr.json`](../../catalogue-saas/vendors/open-data-governance-fr.json) (18 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `opendatasoft` | Opendatasoft | FR | strong | partial |
| `etalab-data-gouv` | Etalab / data.gouv.fr | FR | strong | partial |
| `fairness` | Fairness | FR | strong | partial |
| `toucan-toco` | Toucan Toco | FR | partial | partial |
| `data-europa` | data.europa.eu | EU | partial | partial |
| `socrata-tyler` | Socrata (Tyler Technologies) | US | absent | partial |
| `ckan` | CKAN | GB | partial | partial |
| `arcgis-hub` | ArcGIS Hub | US | partial | partial |
| `data-gov-us` | Data.gov (US) | US | absent | partial |
| `huwise` | Huwise (ex-Opendatasoft) | FR | strong | partial |
| `validata` | Validata | FR | strong | partial |
| `opendatafrance` | OpenDataFrance — Observatoire | FR | strong | partial |
| … | _+6 autres_ | | | |

#### Segment `data-observability` — Data observability

Fichier : [`catalogue-saas/vendors/data-observability.json`](../../catalogue-saas/vendors/data-observability.json) (18 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `monte-carlo` | Monte Carlo | US | partial | partial |
| `great-expectations` | Great Expectations | unknown | unknown | partial |
| `soda` | Soda | US | partial | partial |
| `acceldata` | Acceldata | US | partial | partial |
| `anomalo` | Anomalo | US | partial | partial |
| `bigeye` | Bigeye | US | partial | partial |
| `elementary-data` | Elementary | IL | partial | partial |
| `sifflet` | Sifflet | FR | strong | partial |
| `datafold` | Datafold | US | partial | partial |
| `lightup` | Lightup | US | partial | partial |
| `lakefs` | lakeFS | IL | partial | partial |
| `metaplane` | Metaplane | US | partial | partial |
| … | _+6 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment open-data-governance-fr
```

<!-- catalogue-saas-end -->
## 5. Différenciation
Le trou n'est ni « valider un fichier » (Validata) ni « noter les métadonnées »
(data.gouv.fr), mais le **monitoring continu, transversal, orienté producteur** :
liens morts (404), parsabilité réelle, fraîcheur annoncée vs réelle, conformité
au schéma (via Validata), et **détection de dérive de structure** (colonne
disparue). Défendable, mais **risque d'internalisation par l'État**.

## 6. Faisabilité & fiabilité technique
On mesure des **faits objectifs** : un lien répond ou non, un CSV se parse ou
non, une date dépasse la fréquence annoncée ou non. **Zéro hallucination
possible.** Crawl API catalogue → checks → score historisé par dataset et par
organisation. Le LLM ne sert (optionnellement) qu'à résumer/prioriser.

## 7. Monétisation / impact
- Monétisation : **B2G** (abonnement « gardez vos jeux verts » pour
  collectivités, ou licence pour éditeurs de logiciels métier).
- Impact : fort (qualité de l'écosystème open data français).

## 8. Risques
- **Internalisation** par data.gouv.fr (ils ont déjà le score métadonnées + champ
  `quality`).
- **Monétisation lente** (secteur public).
- **Faible WOW visuel** : outil d'infrastructure.

## 9. Effort MVP
1. Crawl catalogue via API (`datasets`, `resources`, `quality`, `last_update`).
2. Checks objectifs : lien vivant, parsabilité, fraîcheur réelle, validation
   schéma via Validata.
3. Score historisé par jeu de données + par organisation, avec tendance.
4. Vue « tableau de bord producteur » : les ressources en alerte et pourquoi.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | 3 | 5 | 15 |
| C4 | Espace concurrentiel libre | 2 | 4 | 8 |
| C5 | Différenciation défendable | 2 | 3 | 6 |
| C6 | Faisabilité & fiabilité technique | 2 | 5 | 10 |
| C7 | Facilité du MVP | 2 | 3 | 6 |
| C8 | Maîtrise des risques | 2 | 3 | 6 |
| C9 | Monétisation / impact | 2 | 3 | 6 |
| | **Total** | | | **75 / 105** |

**Score /100** : 75 / 105 × 100 = **71**

## 11. Verdict & décision
🔁 **À retravailler.** Techniquement excellente et créneau produit libre, mais le
**« qui signe le chèque »** n'est pas résolu (B2G lent, risque d'internalisation).
Point bloquant à lever avant un Go : valider un payeur concret (1–2 entretiens
collectivité/éditeur) ou assumer un positionnement **impact/open source** plutôt
que revenu rapide.
