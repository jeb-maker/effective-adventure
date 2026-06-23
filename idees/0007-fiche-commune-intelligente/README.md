# Fiche commune intelligente / copilote « ma commune en clair »

- **ID** : 0007
- **Statut** : 💡 Capturée
- **Score** : — / 100 (à analyser)
- **Dernière mise à jour** : 2026-06-21
- **Pitch (1 phrase)** : Transformer les données d'une commune en explications
  claires (« pourquoi ma taxe augmente ? », « ma commune investit-elle plus que
  des communes comparables ? »).

---

## 1. Problème / douleur
Les comptes/indicateurs communaux sont publics mais illisibles pour le citoyen.

## 2. Cible & qui paie
- **Citoyens** : utilisateurs, ne paient pas.
- **Élus / DGS / communicants** : pourraient payer un outil d'explication pédagogique
  (budget communication), mais les dashboards OFGL sont déjà gratuits.
- **Journalistes locaux** : usage ponctuel, budget faible.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| Comptes individuels DGFiP | https://www.data.gouv.fr/datasets/comptes-individuels-des-communes | LO 2.0 | CSV | Annuelle | Lisibilité faible sans agrégation |
| OFGL (comptes, REI, agrégats) | https://data.ofgl.fr/ — API Explore | LO 2.0 | API/CSV | Continue | Déjà très bien outillé côté public |
| REI (recensement équipements) | https://www.data.gouv.fr/datasets/recensement-des-equipements-des-services-aux-particuliers | LO 2.0 | CSV | Millésime REI | Complément services de proximité |
| API Melodi (catalogue INSEE) | https://www.data.gouv.fr/dataservices/api-melodi | LO (Insee) | REST JSON | Continue (vérifié 2026-06-21) | Compte portail-api.insee.fr requis |
| FiLoSoFi IRIS (revenus) | https://www.insee.fr/fr/statistiques/8229323 | LO (Insee) | CSV | Revenus 2021 | Communes ≥ 5 000 hab. pour IRIS |
| SSMSI délinquance (communal) | https://www.data.gouv.fr/datasets/bases-statistiques-communale-departementale-et-regionale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales | LO 2.0 | CSV | MàJ mars 2026 | Faits enregistrés, pas géolocalisé adresse |
| APL (accès aux soins) | https://data.drees.solidarites-sante.gouv.fr/ | LO 2.0 | CSV/API | Annuelle DREES | Indicateur agrégé, pas adresse |

> Vérification détaillée des sources complémentaires :
> [`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements envisagés

| Croisement | Question citoyenne | Clé |
|---|---|---|
| OFGL × communes comparables (Melodi) | « Ma commune dépense-t-elle plus que des communes similaires ? » | Code commune INSEE + strate démographique |
| DGFiP × REI | « Où vont les investissements vs les équipements manquants ? » | Code commune |
| FiLoSoFi × SSMSI | « Pouvoir d'achat local vs statistiques de délinquance » | Code commune INSEE |
| APL × démographie Melodi | « Désert médical + vieillissement de la population » | Code commune |
| Fiscalité locale × OFGL | « Pourquoi ma taxe augmente ? » (RAG sur définitions + SQL sur taux) | Code commune |

Architecture cible : **SQL** pour tous les chiffres (OFGL, DGFiP, SSMSI) ; **RAG** uniquement
sur les définitions comptables et fiscales (guides Etalab, glossaire OFGL).

## 4. Existant / concurrence
Dashboards déjà présents :
- Cartographie OFGL (data.ofgl.fr), Tableau de bord comptes des collectivités,
  NosFinancesLocales.fr, visualisations data.economie.gouv.fr.
  (Consultés 2026-06-20.)
La plupart restent des **dashboards bruts**, peu d'explication pédagogique.

## 11. Verdict & décision
💡 **Capturée.** Angle « explication » plausible mais marché moyen et outils
existants. Pourrait fusionner avec 0003 comme vertical « finances locales ».
Priorité < 0001.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0007-fiche-commune-intelligente` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `territorial-analytics` — Analytics territoriales

Fichier : [`catalogue-saas/vendors/territorial-analytics.json`](../../catalogue-saas/vendors/territorial-analytics.json) (18 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `datagouv` | data.gouv.fr | FR | strong | verified |
| `georisques` | Géorisques | FR | strong | verified |
| `ofgl` | OFGL Observatoire | FR | strong | verified |
| `cartes-gouv` | Géoportail / cartes.gouv.fr | FR | strong | verified |
| `data-gov-uk` | data.gov.uk | GB | absent | partial |
| `ons-uk` | Office for National Statistics (UK) | GB | absent | partial |
| `eurostat-regional` | Eurostat — Regional Statistics | EU | partial | partial |
| `carto-territorial` | CARTO | ES | partial | partial |
| `smappen` | Smappen | FR | strong | partial |
| `geomarket` | Geomarket | FR | strong | partial |
| `data-b` | Data-B | FR | strong | partial |
| `vigicite` | VigiCité | FR | strong | partial |
| … | _+6 autres_ | | | |

#### Segment `bi-analytics-platforms` — BI & analytics

Fichier : [`catalogue-saas/vendors/bi-analytics-platforms.json`](../../catalogue-saas/vendors/bi-analytics-platforms.json) (5 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `tableau` | Tableau (Salesforce) | US | partial | partial |
| `power-bi` | Microsoft Power BI | US | partial | partial |
| `looker` | Looker (Google Cloud) | US | partial | partial |
| `thoughtspot` | ThoughtSpot | US | partial | partial |
| `mode-analytics` | Mode | US | partial | partial |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment territorial-analytics
```

<!-- catalogue-saas-end -->
