# Fiche commune intelligente / copilote « ma commune en clair »

- **ID** : 0007
- **Statut** : ❌ Écartée
- **Score** : 50 / 100
- **Dernière mise à jour** : 2026-06-23
- **Révision critique** : voir [`revue.md`](revue.md) — score confirmé **50/100** (< 55) ;
  saturation citoyenne confirmée (Orama, Habity, DépensesPubliques, OFGL).
- **Pitch (1 phrase)** : Transformer les données d'une commune en explications
  claires (« pourquoi ma taxe augmente ? », « ma commune investit-elle plus que
  des communes comparables ? »).

---

## 1. Problème / douleur

La **littératie financière locale** est faible : comptes administratifs, taux
de fiscalité et ratios OFGL existent en open data, mais restent **illisibles**
pour un citoyen sans formation comptable publique. La douleur est **réelle mais
tiède** : elle picke à la réception de l'avis d'imposition, en campagne
électorale ou lors d'un débat local — pas un besoin quotidien récurrent. De plus,
plusieurs services **gratuits** couvrent déjà les deux questions du pitch (voir §4).

## 2. Cible & qui paie

| Segment | Rôle | Paie ? |
|---|---|---|
| **Citoyens / contribuables** | Utilisateurs principaux du pitch | **Non** — habitués au gratuit (OFGL, Orama, Habity, DépensesPubliques) |
| **Élus / DGS / communicants** | Pourraient acheter un outil pédagogique | Budget com' existe, mais **Collectiv'Finances** (BdT) et **LocalOpen** (LocalNova) sont gratuits ; **Toucan Toco**, **LocalCom** et **Manty** occupent le B2G payant (cf. idée **0020**) |
| **Journalistes locaux** | Usage ponctuel | Budget outils faible ; APIs gratuites suffisent |
| **Candidats aux municipales** | Rapports comparatifs | **Décomptes-Publics.fr** : 49,90–399,90 € / rapport ponctuel |

**Problème structurel** : utilisateur (citoyen) ≠ payeur. Le segment B2G « expliquer
le budget à la population » est **saturé et partiellement gratuit** — chevauche
l'idée **0020** (benchmark DGS) sans offrir de différenciation citoyenne défendable.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| Comptes individuels DGFiP | https://www.data.gouv.fr/datasets/comptes-individuels-des-communes | LO 2.0 | CSV | Annuelle | Lisibilité faible sans agrégation ; périmètre budget principal vs consolidé |
| OFGL (comptes, REI, agrégats) | https://data.ofgl.fr/ — API Explore v2 | LO 2.0 | API/CSV | Continue (2024 à jour, consulté 2026-06-23) | Déjà très bien outillé côté public ; formules M57 à réutiliser |
| Comptes communes 2017–2024 (OFGL) | https://www.data.gouv.fr/datasets/comptes-des-communes-2017-2024 | LO 2.0 | CSV | Annuelle | 7+ réutilisations citoyennes listées sur data.gouv |
| REI (recensement équipements) | https://www.data.gouv.fr/datasets/recensement-des-equipements-des-services-aux-particuliers | LO 2.0 | CSV | Millésime REI | Complément services de proximité |
| Fiscalité locale particuliers (Géo) | https://www.data.gouv.fr/datasets/fiscalite-locale-des-particuliers-geo | LO 2.0 | CSV | Taux 2021–2024 (impots.gouv.fr) | Taux globaux, pas explication causale seule |
| API Melodi (catalogue INSEE) | https://www.data.gouv.fr/dataservices/api-melodi | LO (Insee) | REST JSON | Continue | Compte portail-api.insee.fr requis |
| FiLoSoFi IRIS (revenus) | https://www.insee.fr/fr/statistiques/8229323 | LO (Insee) | CSV | Revenus 2021 | Communes ≥ 5 000 hab. pour IRIS |
| SSMSI délinquance (communal) | https://www.data.gouv.fr/datasets/bases-statistiques-communale-departementale-et-regionale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales | LO 2.0 | CSV | MàJ mars 2026 | Faits enregistrés, pas géolocalisé adresse |
| APL (accès aux soins) | https://data.drees.solidarites-sante.gouv.fr/ | LO 2.0 | CSV/API | Annuelle DREES | Indicateur agrégé |

> Vérification détaillée : [`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements envisagés

| Croisement | Question citoyenne | Clé |
|---|---|---|
| OFGL × communes comparables (Melodi) | « Ma commune dépense-t-elle plus que des communes similaires ? » | Code commune INSEE + strate DGFiP |
| DGFiP × REI | « Où vont les investissements vs les équipements manquants ? » | Code commune |
| Fiscalité REI × OFGL | « Pourquoi ma taxe augmente ? » (SQL taux + RAG définitions) | Code commune |
| FiLoSoFi × SSMSI | Pouvoir d'achat local vs délinquance enregistrée | Code commune INSEE |

Architecture cible : **SQL** pour tous les chiffres (OFGL, DGFiP, REI, fiscalité) ;
**RAG** uniquement sur définitions comptables et fiscales (guides Etalab, glossaire OFGL).

## 4. Existant / concurrence

**Verdict de saturation : saturé** sur le créneau citoyen « fiche commune +
comparaison + explication ». Orama et Habity (2026) couvrent quasi mot pour mot
le pitch.

### 4.1 Services publics / .gouv.fr

| Acteur | URL | Ce qu'il fait | Consulté |
|---|---|---|---|
| **OFGL — data.ofgl.fr** | https://data.ofgl.fr/pages/accueil/ | ~70 agrégats, cartographie, **analyse comparative par groupe de référence**, datastories, API Explore v2 | 2026-06-23 |
| **Cartographie OFGL** | https://data.ofgl.fr/pages/cartographie/ | Comparaison géo et strate personnalisable | 2026-06-23 |
| **Analyse comparative OFGL** | https://data.ofgl.fr/pages/accueil-analyse/ | Fiches multi-thèmes (dette, fiscalité, synthèse) | 2026-06-23 |
| **data.economie.gouv.fr** | https://data.economie.gouv.fr/explore/dataset/comptes-individuels-des-collectivites/ | Comptes individuels DGFiP, graphiques natifs | 2026-06-23 |
| **DGFiP — statistiques collectivités** | https://www.impots.gouv.fr/statistiques-collectivites-locales | Cartes taux fiscalité 2021–2024, REI | 2026-06-23 |
| **Collectiv'Finances (Banque des Territoires)** | https://www.banquedesterritoires.fr/produits-services/services-digitaux/collectivfinances-outils-analyse-financiere-collectivite | **Gratuit** pour DGS : prospective, modélisation, PPI | 2026-06-23 |
| **Tableau de bord de l'élu (PIGP/AEFF)** | https://www.collectivites-locales.gouv.fr/tableau-de-bord-de-lelu | Fiches AEFF, 21 indicateurs — **habilitation comptable** | 2026-06-23 |

### 4.2 Réutilisations data.gouv

| Acteur | URL | Ce qu'il fait | Consulté |
|---|---|---|---|
| **Orama Limited** | https://oramalimited.com/ | App **gratuite** : API OFGL, note A–E, synthèses par thème, **3 comparables** multicritères, boutons « En savoir + » | 2026-06-23 |
| **DépensesPubliques.fr** | https://depensespubliques.fr/ | 36 000+ communes, comparateur, classements, fiches traçables ; blog pédagogique fiscalité/dette | 2026-06-23 |
| **Habity** | https://habity.fr/ — réutilisation https://www.data.gouv.fr/reuses/habity-fiscalite-locale-par-commune-basee-sur-les-donnees-rei | **Fiche commune intelligente** : 107 indicateurs, 14 domaines ; finances OFGL/REI consolidées, percentiles nationaux (MAJ avril 2026) | 2026-06-23 |
| **FMPC** | https://www.fmpc.fr/ | 34 908 communes, ratios, comparaison ; simulateur impôts (impact contribuable €) | 2026-06-23 |
| **Ville de rêve** | https://www.data.gouv.fr/reuses/ville-de-reve-le-palmares-des-meilleures-villes-selon-vos-criteres | Palmarès personnalisable sur jeux OFGL | 2026-06-23 |
| **NosFinancesLocales (Regards Citoyens)** | https://www.nosfinanceslocales.fr | Cartographies 2000–2012 | 2026-06-23 — **fermé** (« faute de motivation bénévole ») |
| **Éclaireur Public** (Anticor) | https://eclaireurpublic.fr/methodologie | Indice transparence subventions + marchés (adjacent idée 0027) | 2026-06-23 |

### 4.3 Produits commerciaux

| Acteur | URL | Ce qu'il fait | Pricing (consulté 2026-06-23) |
|---|---|---|---|
| **LocalNova — LocalCom-DOB-ROB** | https://www.localnova-finance.fr/ | Rapports pédagogiques PDF pour élus/citoyens ; > 1 000 collectivités | Devis ; Localrural **500–1 100 €/an** |
| **LocalOpen** | https://www.localnova-finance.fr/applications-web-collectivites-locales/localopen-donnees-financiere-des-collectivites-en-libre-acces/ | Freemium big data + TB pour décideurs publics | Gratuit → modules payants |
| **Manty Décision** | https://www.manty.eu/finance | Ratios DGFiP, comparaison strate, exports PDF élus | Sur devis |
| **Toucan Toco — portail public** | https://www.toucantoco.com/fr/solutions/public-portal.html | Data storytelling citoyen pour collectivités | Setup + abonnement annuel sur devis |
| **Décomptes-Publics.fr** | https://www.decomptes-publics.fr/ | Rapports PDF explicatifs 10 ans + comparaison strate (candidats/journalistes) | **49,90–399,90 €** / rapport |
| **RCF Repères / Regards** | https://www.ressources-consultants-finances.fr/logiciels/reperes/ | Benchmark inter-collectivités B2G | Devis |

### 4.4 Open source / académique / civic tech

| Acteur | URL | Statut | Consulté |
|---|---|---|---|
| **NosFinancesLocales (code)** | https://github.com/regardscitoyens/nosfinanceslocales | OSS ; service **mort** | 2026-06-23 |
| **Regards Citoyens** | https://www.regardscitoyens.org/ | NosDéputés, OpenCorporates — **pas de produit finances locales actif** | 2026-06-23 |
| **Voxe.org** | https://www.voxe.org/ | Comparateur **programmes électoraux**, pas comptes communaux | 2026-06-23 |
| **Contribuables Associés — Argus 2026** | https://contribuablesassocies.org/2026/03/11/largus-des-communes-2026-demasque-les-canards-boiteux-de-la-gestion-municipale/ | Notation 34 875 communes (angle militant) | 2026-06-23 |

### 4.5 Bricolage / alternatives

| Alternative | Coût |
|---|---|
| OFGL cartographie + analyse comparative (gratuit) | 0 € |
| Orama / Habity / DépensesPubliques (fiche + comparables) | 0 € |
| ChatGPT / Copilot + export OFGL (RAG artisanal) | Licence M365 ~30 €/user/mois |
| PDF comptes administratifs sur site mairie (L.2121-26 CGCT) | 0 € ; illisible |
| LocalCom ou Décomptes-Publics en campagne | 50–400 € ponctuel |

### 4.6 Verdict de saturation

| Zone | Saturation |
|---|---|
| Fiche commune finances + comparaison strate | **Saturée** — OFGL, Orama, Habity, DépensesPubliques, FMPC |
| Couche explication pédagogique citoyenne | **Saturée** — Orama « En savoir + », blogs DP, Habity méthodologie |
| B2G communicants / DGS | **Saturée** — cf. idée **0020** (LocalNova, Manty, Toucan, Collectiv'Finances gratuit) |
| Espace libre crédible | **Quasi nul** — chat IA conversationnel multi-sources sans acteur dominant, mais cas structurés déjà couverts |

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0007-fiche-commune-intelligente` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `partial` seules pour conclure C4.

#### Segment `territorial-analytics` — Analytics territoriales

Fichier : [`catalogue-saas/vendors/territorial-analytics.json`](../../catalogue-saas/vendors/territorial-analytics.json) (24 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `ofgl` | OFGL Observatoire | FR | strong | verified |
| `datagouv` | data.gouv.fr | FR | strong | verified |
| `localnova` | LocalNova | FR | strong | partial |
| `smappen` | Smappen | FR | strong | verified |
| `geomarket` | Geomarket | FR | strong | verified |
| `vigicite` | VigiCité | FR | strong | partial |
| … | _+18 autres_ | | | |

#### Segment `open-data-governance-fr` — Gouvernance open data FR

Fichier : [`catalogue-saas/vendors/open-data-governance-fr.json`](../../catalogue-saas/vendors/open-data-governance-fr.json) (20 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `toucan-toco` | Toucan Toco | FR | partial | partial |
| `opendatasoft` | Opendatasoft | FR | strong | partial |
| `validata` | Validata | FR | strong | verified |
| … | _+17 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment territorial-analytics
```

<!-- catalogue-saas-end -->

## 5. Différenciation

| Angle revendiqué | Déjà couvert par |
|---|---|
| « Pourquoi ma taxe augmente ? » | impots.gouv.fr REI ; Habity (taux + historique) ; FMPC simulateur ; DépensesPubliques (blog) ; Orama section fiscalité |
| « Ma commune dépense-t-elle plus que des comparables ? » | OFGL analyse comparative ; Orama (3 comparables + médiane strate) ; Habity (percentiles 34 746 communes) ; DépensesPubliques |
| Explication pédagogique (vs dashboard brut) | Orama « En savoir + » ; Habity méthodologie ; LocalCom ; Toucan ; Décomptes-Publics |
| Données OFGL/DGFiP traçables | **Standard du marché** — aucun verrou |

**Différenciation défendable** : **quasi nulle**. [Orama](https://oramalimited.com/) est une
application citoyenne gratuite alimentée par l'API OFGL avec synthèses, note A–E et
comparables — formulation **identique** au pitch. [Habity](https://habity.fr/) (avril 2026)
porte explicitement le libellé « fiche commune intelligente » sur 107 indicateurs.

Seul écart résiduel étroit : **chat IA conversationnel** multi-sources avec traçabilité
SQL — non dominant, et les cas d'usage structurés (taxe, comparaison strate) sont
déjà servis sans abonnement.

## 6. Faisabilité & fiabilité technique

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ Ingestion OFGL  │────▶│ Entrepôt SQL     │────▶│ Fiche citoyenne │
│ + DGFiP + REI   │     │ (DuckDB/Postgres)│     │ + comparables   │
└─────────────────┘     └────────┬─────────┘     └────────┬────────┘
                                 │                        │
                                 ▼                        ▼
                        Requêtes SQL traçables      LLM (RAG sens)
                        (ratios, percentiles,       définitions M57,
                         écarts vs strate)          narration pédagogique
```

- **Chiffres** : SQL sur agrégats OFGL (formules publiées) + REI fiscalité ; afficher
  **périmètre** (budget principal / consolidé) et exercice.
- **LLM** : cantonné aux définitions et à la narration ; **jamais** au calcul numérique.
- **Comparables** : strate DGFiP + critères démographiques (réutiliser logique Orama/Habity).

Faisabilité technique : **élevée** pour un MVP finances-only (4–6 semaines). La
difficulté est **produit et monétisation**, pas l'ingénierie.

## 7. Monétisation / impact

| Modèle | Faisabilité | Commentaire |
|---|---|---|
| B2C freemium (citoyen) | **Très faible** | Orama, Habity, DépensesPubliques = 0 € ; consentement à payer ~0 |
| B2G SaaS (com' mairie) | **Faible** | Toucan, LocalCom, Manty, Collectiv'Finances gratuit — cf. 0020 |
| Rapport ponctuel (campagne) | **Faible** | Décomptes-Publics 49,90–399,90 € occupe le créneau |
| Impact sociétal | **Marginal** | Littératie utile, mais **11ᵉ couche** sur données déjà expliquées |

## 8. Risques

| Risque | Gravité | Commentaire |
|---|---|---|
| **Clone gratuit Orama / Habity** | Critique | Concurrent direct, gratuit, même API OFGL |
| **OFGL officiel gratuit** | Critique | Comparaison strate intégrée ; enrichissement continu État |
| **Utilisateur ≠ payeur** | Critique | Citoyen ne paie pas ; B2G saturé (0020) |
| **Interprétation politique** | Élevée | « Mauvaise gestion » vs contexte local — risque réputationnel pour un éditeur |
| **Commoditisation IA** | Élevée | FMPC intègre déjà IA simulateur fiscal |
| **Pérennisation civic tech** | Moyenne | NosFinancesLocales **fermé** faute de modèle économique |
| **Élargissement multi-domaines** | Moyenne | Croiser SSMSI, APL, etc. = copilote généraliste (cf. idée **0003**, écartée) |

## 9. Effort MVP

Périmètre minimal crédible (si le marché n'était pas saturé) :

1. Ingestion jeux OFGL communes 2017–2024 + REI fiscalité + geo.api.gouv.fr.
2. Moteur comparables : strate DGFiP + 3 communes similaires (population, revenu, ruralité).
3. Fiche citoyenne : 5 indicateurs SQL (épargne/hab, dette/hab, fiscalité/hab, investissement/hab, DRF/hab) + tendance 5 ans.
4. Bloc « Pourquoi ma taxe ? » : SQL sur évolution taux REI + RAG glossaire fiscalité.
5. Traçabilité : chaque chiffre → dataset + exercice + formule OFGL.

**Effort** : 4–6 semaines technique — **sans go-to-market** face à Orama/Habity gratuits.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré | Justification |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 9 | Littératie réelle mais douleur **tiède** et épisodique ; gratuits disponibles |
| C2 | Cible solvable (qui paie) | 3 | 1 | 3 | Citoyen = 0 € ; B2G capté + gratuit massif (Collectiv'Finances, LocalOpen, OFGL) — utilisateur ≠ payeur |
| C3 | Disponibilité & fiabilité données | 3 | 5 | 15 | OFGL/DGFiP/APIs prêtes, formules publiques, traçables en SQL |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 | **Orama + Habity + OFGL + DépensesPubliques** — pitch quasi clone |
| C5 | Différenciation défendable | 2 | 1 | 2 | Aucun verrou ; Orama gratuit = même proposition |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 | SQL/RAG conforme si vertical finances strict |
| C7 | Facilité du MVP | 2 | 4 | 8 | Données prêtes — facilité = signe de saturation |
| C8 | Maîtrise des risques | 2 | 2 | 4 | Commoditisation et payeur non maîtrisables |
| C9 | Monétisation / impact | 2 | 1 | 2 | B2C impossible ; impact marginal vs outils existants |
| | **Total** | | | **53 / 105** | |

**Score /100** : 53 / 105 × 100 = **50** (arrondi)

> **Confirmé par revue red team (2026-06-23) : 50/100 inchangé** — C2=1 (citoyen
> ≠ payeur) décisif. Détail dans [`revue.md`](revue.md).

## 11. Verdict & décision

**❌ Écartée** — score **50 / 100** (< 55).

Le pitch « fiche commune intelligente » est **factuellement redondant** avec l'existant
gratuit. Orama et Habity (2026) couvrent les deux questions citoyennes du seed ;
l'OFGL officiel intègre déjà la comparaison par strate. Le segment B2G « expliquer
le budget » chevauche l'idée **0020** (écartée à 53/100). NosFinancesLocales
(Regards Citoyens) a **échoué à se pérenniser** — signal fort sur l'absence de
modèle économique.

**Critère quasi éliminatoire** : saturation citoyenne + **product-market fit négatif**
(citoyen obtient gratuitement ce que l'idée vendrait).

**Prochaine étape** : ne pas prototyper. Si exploration ultérieure du secteur
« territoire / finances » :

- **Ne pas** dupliquer Orama/Habity/OFGL ;
- Envisager un angle **non couvert** (ex. croisement finances × DECP/subventions,
  idée **0027**) ou un **canal B2B2G** (cabinet, presse) — hors périmètre citoyen pur ;
- Traiter 0007 comme **sous-vertical finances** de 0003 plutôt que produit standalone
  — mais 0003 est elle-même **écartée** en généraliste.

**Liens** : idée voisine [0020](../0020-benchmark-financier-collectivites/) (B2G benchmark,
❌ 53) ; [0003](../0003-copilote-territorial-rag/) (copilote RAG généraliste, ❌ 46).
