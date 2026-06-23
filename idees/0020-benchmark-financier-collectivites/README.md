# Benchmark financier inter-collectivités (pour DGS/élus)

- **ID** : 0020
- **Statut** : ❌ Écartée
- **Score** : 53 / 100
- **Dernière mise à jour** : 2026-06-20
- **Pitch (1 phrase)** : Outil B2G d'aide au pilotage pour DGS et élus : comparer sa commune/EPCI à des collectivités de strate comparable (comptes DGFiP/OFGL, fiscalité, dette, épargne) avec alertes et restitution pédagogique.

---

## 1. Problème / douleur

Les DGS et élus doivent **situer la santé financière** de leur territoire à chaque mandat, avant chaque débat budgétaire et face à une **pression budgétaire structurelle** (gel DGF, hausse des charges contraintes, normes). L'AMF estime la facture des mesures nationales pour les collectivités à **au moins 8,3 Md€ en 2025** (source : https://www.amf.asso.fr/documents-analyse-financiere-du-bloc-communal--quelles-sont-les-tendances-pour-2025-2026-/42853 , consulté 2026-06-20). La Banque des Territoires documente une **dynamique d'investissement historique** du bloc communal en 2025 tout en rappelant la nécessité de maîtriser la trajectoire financière (source : https://www.banquedesterritoires.fr/sites/default/files/2026-02/Note%20Bloc%20Communal%20-%20JRC%20-%2021.02.2026.pdf , consulté 2026-06-20).

La douleur est **réelle et récurrente** : comprendre si sa dette, son épargne brute ou ses dépenses de fonctionnement par habitant sont « normales » pour sa strate, préparer un dialogue de gestion, crédibiliser un discours électoral. Les ratios obligatoires (CGCT art. R.2313-1) existent mais leur interprétation comparative reste technique pour des non-spécialistes.

**Limite** : cette douleur est déjà adressée par l'OFGL (officiel, gratuit), par plusieurs SaaS installés en DGS et par des réutilisations open data récentes — le problème n'est pas l'absence d'outil, c'est la **surcharge d'offres** et la difficulté à choisir.

## 2. Cible & qui paie

| Segment | Utilisateur | Payeur ? | Budget constaté |
|---|---|---|---|
| **Communes / EPCI** (DAF, DGS, élus) | Oui | Oui, en théorie | **Localrural** (LocalNova) : abonnement annuel **500 €** (< 500 hab.) à **1 100 €** (2 000–3 000 hab.) — https://www.localrural.fr/ , consulté 2026-06-20. **LocalNova** revendique **> 1 000 collectivités** clientes — https://www.localnova-finance.fr/editeur-logiciels-conseils-budgetaires-collectivites/recherche-developpement-fintech/ , consulté 2026-06-20. |
| **Grandes collectivités** | DAF / DGS | Oui | **Ressources Consultants Finances** : logiciels (Regards, Repères) utilisés par **~500 collectivités** — https://www.ressources-consultants-finances.fr/societe-conseil-finances-locales/ , consulté 2026-06-20. Tarifs publics : **à vérifier** (devis). |
| **Manty Décision** | DGS, directions | Oui | Tarif **sur mesure**, abonnement annuel proportionnel au budget de fonctionnement — https://www.manty.eu/finance , consulté 2026-06-20. |
| **Citoyens / journalistes / candidats** | Oui | Non | DépensesPubliques.fr, FMPC (app mobile) — usage gratuit. |

**Utilisateur = payeur** pour le B2G direct, ce qui est sain commercialement. **Mais** : (1) le segment est **déjà équipé** par des éditeurs historiques ; (2) des **alternatives gratuites institutionnelles** couvrent le cœur du besoin (OFGL, Collectiv'Finances, LocalOpen) ; (3) le contexte 2025–2026 **resserre les budgets** logiciels des petites collectivités. Un nouvel entrant doit arracher un budget déjà capté ou convaincre de payer pour ce qui est gratuit ailleurs — barrière d'achat élevée.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| Comptes individuels des collectivités (DGFiP) | https://data.economie.gouv.fr/explore/dataset/comptes-individuels-des-collectivites/ | Licence Ouverte 2.0 | CSV / API Explore v2.1 | Fichier global communes **2023–2024** publié le **1 déc. 2025** — https://www.data.gouv.fr/datasets/comptes-individuels-des-communes-fichier-global-2023-2024 , consulté 2026-06-20 | **Budget principal seul** (pas consolidé avec budgets annexes) — note méthodologique DGFiP : https://www.impots.gouv.fr/cll/application/pdf/methodo_commune.pdf , consulté 2026-06-20. Décalage ~12–18 mois vs exercice en cours. |
| Comptes des communes (agrégats OFGL) | https://www.data.gouv.fr/datasets/comptes-des-communes-2017-2024/ | Licence Ouverte 2.0 | CSV / API OFGL Explore v2 | Dernière MàJ **30 juil. 2025** (exercices 2017–2024) — même URL | Agrégats recalculés OFGL ; méthode documentée. Fréquence de MàJ non renseignée sur data.gouv.fr. |
| Comptes EPCI, départements, régions (OFGL) | https://data.ofgl.fr/explore/ + jeux sur data.gouv.fr (ex. comptes consolidés communes, régions MàJ **3 juin 2026**) — https://www.data.gouv.fr/reuses/cartographie-des-resultats-financiers-des-collectivites-locales , consulté 2026-06-20 | Licence Ouverte 2.0 | CSV / API | Variable par niveau (2024 pour communes ; régions plus récentes) | Consolidation intercommunale ≠ somme arithmétique simple des communes membres. |
| Fiscalité directe locale (REI) | https://data.ofgl.fr/explore/dataset/rei/ | Licence Ouverte 2.0 (via OFGL) | CSV / API | REI **2024–2025** — même URL, consulté 2026-06-20 | Variables territorialisées sur la commune mais **bénéficiaire fiscal** parfois l'EPCI (ex. CFE en FPUN) ; `sec_stat` à interpréter avec prudence. |
| Méthodologie agrégats OFGL | https://data.ofgl.fr/explore/dataset/methodologie-ofgl-formules-des-agregats-financiers/ | Licence Ouverte 2.0 | CSV (formules) | Alignée sur rapport annuel OFGL | Indispensable pour recalculer ou auditer les ratios ; ne pas réinventer les formules. |
| Référentiel géographique / strates | https://geo.api.gouv.fr/ | Licence Ouverte | JSON API | MàJ annuelle (population, EPCI) | Strates OFGL (31 groupes de référence DGFiP) ≠ strates démographiques simples — calage méthodologique requis. |
| Dotations (OFGL) | Jeux « critères et montants des dotations » sur data.ofgl.fr — https://www.collectivites-locales.gouv.fr/etudes-et-statistiques/observatoire-des-finances-et-de-la-gestion-publique-locales-ofgl , consulté 2026-06-20 | Licence Ouverte 2.0 | CSV / API | À vérifier par jeu | Complément utile au benchmark ressources, pas au cœur comptable. |

**Synthèse fiabilité** : données **prêtes, officielles, SQL-interrogeables** (API OFGL Explore v2, API tabulaire data.gouv.fr). Le risque n'est pas l'absence de donnée mais la **sémantique métier** (consolidation, bénéficiaire fiscal, décalage temporel) — un chiffre SQL exact peut être **trompeur** si le périmètre budgétaire est mal compris.

## 4. Existant / concurrence

> Consultation des sources : **2026-06-20**. Verdict de saturation : **saturé** — le benchmark inter-collectivités par strate est couvert par l'officiel gratuit, des SaaS établis et des réutilisations open data récentes.

### 4.1 Offre publique / institutionnelle (gratuite)

| Nom | URL | Ce qu'il fait | Limites |
|---|---|---|---|
| **OFGL — data.ofgl.fr** | https://data.ofgl.fr/pages/accueil/ | Portail officiel (DGCL/DGFiP) : **~70 agrégats et ratios**, cartographie personnalisable, comparaison par strate, montant/habitant, évolution sur 6 ans — https://www.data.gouv.fr/reuses/cartographie-des-resultats-financiers-des-collectivites-locales , consulté 2026-06-20 | UX orientée data analyst ; pas d'alertes métier DGS ; pas de restitution « mandat » clé en main. **Couvre le cœur de l'idée.** |
| **Collectiv'Finances** (Banque des Territoires) | https://www.banquedesterritoires.fr/produits-services/services-digitaux/collectivfinances-outils-analyse-financiere-collectivite | Outil **100 % gratuit** : prospective financière, modélisation de projet, PPI ; accompagnement Rural Consult pour petites collectivités — même URL, consulté 2026-06-20 | Orienté **simulation/prospective**, moins benchmark passif multi-pairs ; mais répond au même besoin de pilotage financier DGS. |
| **Hélios / PIGP** (DGFiP) | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/dematerialisation-des-comptes-locaux-et-open-data/dematerialisation-comptable-et-budgetaire/helios-lapplication-informatique-de-la-direction-generale-des-finances , consulté 2026-06-20 | Consultation **gratuite** des données budgétaires/comptables de sa propre collectivité (habilitation comptable) | Pas de benchmark inter-collectivités ; données **propres** uniquement. |
| **Territoires et Finances** (AMF / Banque Postale / BdT) | https://www.amf.asso.fr/documents-territoires-finances-principaux-ratios-financiers-communes-intercommunalites-en-2021/41444 , consulté 2026-06-20 | Publication annuelle de repères par **strate démographique** (7 fiches communes + EPCI) | Publication PDF, pas un SaaS interactif ; référence méthodologique, pas concurrent direct produit. |

### 4.2 Réutilisations open data (gratuites)

| Nom | URL | Ce qu'il fait | Limites |
|---|---|---|---|
| **DépensesPubliques.fr** | https://depensespubliques.fr/ | **36 000+ communes**, comparateur, baromètre 2024, classements dette/dépenses/épargne ; API tabulaire data.gouv.fr — https://depensespubliques.fr/donnees-sources , consulté 2026-06-20 | Focus **communes** ; pas de module DGS complet (alertes, export conseil) ; monétisation **à vérifier**. |
| **FMPC** (Financer Mes Projets Communaux) | https://www.fmpc.fr/ | **34 908 communes**, ratios, comparaison, simulateur fiscal (IA sur état 1259), app iOS — même URL, consulté 2026-06-20 | Périmètre **communal** ; tarifs B2G **non publics** ; chevauchement direct avec l'idée. |
| **NosFinancesLocales** (Regards Citoyens) | https://www.nosfinanceslocales.fr | Cartographies historiques open data | **Service fermé** (« faute de motivation bénévole ») — consulté 2026-06-20. N'est plus un concurrent actif mais prouve que le créneau a déjà été tenté en civic tech sans pérennité. |
| **Ville de rêve**, **Deniers publics (Spallian)** | Réutilisations sur jeu OFGL — https://www.data.gouv.fr/datasets/comptes-des-communes-2017-2024/reuses_and_dataservices , consulté 2026-06-20 | Comparaisons / palmarès grand public | Angle citoyen, pas B2G DGS. |

### 4.3 SaaS commerciaux B2G (payants)

| Nom | URL | Ce qu'il fait | Prix / preuve budget |
|---|---|---|---|
| **LocalNova — LocalÉvaluation / LocalBenchmark / LocalObservatoire** | https://www.localnova-finance.fr/progiciel-analyse-prevision-financiere-rh-collectivites-locales/plateforme-fonction-finance-collectivite-territoriale/evaluation-financiere-comparative/ , consulté 2026-06-20 | Rapport comparatif **90+ variables** vs collectivités de même profil ; cartographie multi-années ; **LocalBenchmark** dédié comparaison performances — https://www.localnova-finance.fr/editeur-logiciels-conseils-budgetaires-collectivites/recherche-developpement-fintech/ , consulté 2026-06-20 | Devis ; **Localrural** : 500–1 100 €/an (petites communes). **> 1 000 clients.** |
| **LocalNova — LocalOpen** (freemium) | https://www.localnova-finance.fr/progiciel-analyse-prevision-financiere-rh-collectivites-locales/localopen-donnees-financiere-des-collectivites-en-libre-acces/ , consulté 2026-06-20 | Big data financier, tableaux de bord synthétiques, études thématiques — **gratuit pour décideurs publics** (inscription) | Freemium : gratuit attire, modules payants en aval. |
| **Manty Décision** | https://www.manty.eu/finance , consulté 2026-06-20 | Pilotage financier : ratios DGFiP, **comparaison à la moyenne de strate** et collectivités sélectionnées via open data (Insee, DGFiP, data.gouv.fr) — https://www.manty.eu/post/3-manieres-de-suivre-les-indicateurs-financiers-de-votre-collectivite-avec-manty-decision , consulté 2026-06-20 | Tarif sur mesure ; connecteurs logiciels métiers. **C'est l'idée 0020, déjà produite.** |
| **Ressources Consultants — Repères** | https://www.ressources-consultants-finances.fr/logiciels/reperes/ , consulté 2026-06-20 | Module **inter-collectivité** : situer son territoire vs autres collectivités (budgétaire, dotations, fiscalité, critères physico-financiers) ; moyennes nationale/régionale/départementale/strate | ~500 collectivités ; devis. Module **quasi homonyme** de l'idée. |
| **Ressources Consultants — Regards** | https://www.ressources-consultants-finances.fr/logiciels/regards-retro-prospective/ , consulté 2026-06-20 | Rétro-prospective financière SaaS (~400 collectivités budgets principaux) | Plus orienté prospective que benchmark, mais même cible DAF. |
| **Finestia** | https://www.finestia.fr/index.php , consulté 2026-06-20 | Observatoire finances locales, **comparaison budgets/collectivités**, PPI, abonnement mensuel/annuel | Tarifs **à vérifier** ; éditeur indépendant. |
| **KPMG Secteur Public** (+ partenariat LocalNova) | https://kpmg.com/fr/fr/secteurs/secteur-public/finance.html + https://www.localnova-finance.fr/accord-cooperation-kpmg-localnova/ , consulté 2026-06-20 | Conseil finances locales adossé aux applicatifs LocalNova | Prestation cabinet, pas SaaS self-service pur. |
| **FMPC** (cf. §4.2) | https://www.fmpc.fr/ | Benchmark + simulation + mobile | Concurrent direct sur le segment élus/candidats. |

### 4.4 Verdict de saturation

| Zone | Saturation |
|---|---|
| Benchmark passif par strate (ratios, dette, épargne) | **Saturée** — OFGL cartographie + DépensesPubliques + FMPC |
| Benchmark B2G DGS avec restitution élus | **Saturée** — LocalNova, Manty, Repères, Finestia |
| Gratuit institutionnel | **Très présent** — OFGL, Collectiv'Finances, LocalOpen |
| Espace libre éventuel | **Très étroit** : alertes mandat + narration IA pédagogique pour élus non-financiers, **sans** payer ni dupliquer l'OFGL — et Manty/LocalNova y investissent déjà. |

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0020-benchmark-financier-collectivites` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `territorial-analytics` — Analytics territoriales

Fichier : [`catalogue-saas/vendors/territorial-analytics.json`](../../catalogue-saas/vendors/territorial-analytics.json) (8 entrées)

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

#### Segment `treasury-fpa` — Trésorerie & FP&A

Fichier : [`catalogue-saas/vendors/treasury-fpa.json`](../../catalogue-saas/vendors/treasury-fpa.json) (5 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `anaplan` | Anaplan | US | partial | partial |
| `pigment` | Pigment | FR | strong | partial |
| `drivetrain` | Drivetrain | US | partial | partial |
| `cube-software` | Cube | US | partial | partial |
| `mosaic-tech` | Mosaic | US | partial | partial |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment territorial-analytics
```

<!-- catalogue-saas-end -->
## 5. Différenciation

Promesses possibles de l'idée 0020 vs l'existant :

| Angle revendiqué | Déjà couvert par |
|---|---|
| Comparaison par strate (dette, épargne, fiscalité) | **OFGL** (officiel), **Manty** (open data), **LocalÉvaluation**, **Repères**, **DépensesPubliques**, **FMPC** |
| Alertes sur dégradation d'indicateurs | **Manty** (tableaux de bord), **LocalNova** (diagnostic) — seuils exacts **à vérifier** produit par produit |
| Restitution claire pour élus | **LocalNova** (rapports PDF 14–25 p.), **Collectiv'Finances** (accompagnement), **FMPC** (rapport IA) |
| Données DGFiP / OFGL traçables | **Standard du marché** — aucun verrou propriétaire sur la donnée |

**Différenciation défendable** : quasi nulle en l'état. Un positionnement « couche IA d'explication + alertes mandat » est **copiable en un week-end** par Manty ou LocalNova, et partiellement gratuite via LocalOpen + OFGL. La seule voie crédible serait un **pivot** (ex. verticalisation SDIS/EPCI complexe, intégration CFU 2026, ou canal B2B2G cabinets) — hors seed initial.

## 6. Faisabilité & fiabilité technique

**Architecture recommandée** (conforme RAG(sens) / SQL(chiffres)) :

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ Ingestion OFGL  │────▶│ Entrepôt SQL     │────▶│ API / Dashboard │
│ + DGFiP + geo   │     │ (DuckDB/Postgres)│     │ (comparaisons)  │
└─────────────────┘     └────────┬─────────┘     └────────┬────────┘
                                 │                        │
                                 ▼                        ▼
                        Requêtes SQL traçables      LLM (RAG sens)
                        (ratios, percentiles,       définitions M57,
                         écarts vs strate)          alertes textuelles
```

- **Chiffres** : calculés en SQL à partir des agrégats OFGL (réutiliser les formules du jeu `methodologie-ofgl-formules-des-agregats-financiers`) ou des comptes individuels DGFiP ; chaque indicateur affiché avec **source + exercice + requête**.
- **LLM** : cantonné à l'explication pédagogique (définition épargne brute, capacité de désendettement), génération de synthèse mandat, **jamais** au calcul numérique.
- **Strates** : joindre via code INSEE + référentiel des 31 groupes DGFiP (note méthodologique impots.gouv.fr).
- **Risque de fiabilité** : comme pour DECP (cf. revue 0001), SQL traçable ≠ indicateur métier pertinent si périmètre non consolidé ou bénéficiaire fiscal mal identifié — **afficher le périmètre** (budget principal / consolidé / FPUN).

Faisabilité technique : **élevée** (données tabulaires, APIs documentées). La difficulté est **produit et distribution**, pas l'ingénierie données.

## 7. Monétisation / impact

**Modèles envisageables :**

| Modèle | Faisabilité | Commentaire |
|---|---|---|
| SaaS B2G 500–5 000 €/an | Faible | Fourchette observée (Localrural 500 €+) mais marché capté ; gratuit OFGL/Collectiv'Finances en amont |
| Freemium (benchmark gratuit, alertes payantes) | Faible | LocalOpen et DépensesPubliques occupent le gratuit |
| Conseil + outil (type KPMG/RCF) | Moyenne | Nécessite expertise finances locales, pas un pur produit data |
| Impact citoyen / transparence | Moyen | DépensesPubliques, FMPC déjà présents ; pas de revenu |

**Impact sociétal** : améliorer la littératie financière des élus est utile, mais **l'impact marginal d'un 11ᵉ outil** est faible tant que l'OFGL et les éditeurs installés couvrent le besoin.

## 8. Risques

| Risque | Gravité | Commentaire |
|---|---|---|
| **Redondance avec OFGL** (officiel, gratuit) | Critique | L'État est le concurrent le plus dangereux ; enrichissement continu (pré-rapport 2026, cartographie) — https://www.collectivites-locales.gouv.fr/actualites/pre-rapport-de-lofgl-sur-les-finances-locales-edition-2026 , consulté 2026-06-20 |
| **Saturation SaaS** (LocalNova, Manty, RCF, Finestia) | Critique | > 5 acteurs avec modules « comparaison » explicites |
| **Pression budgétaire collectivités** | Élevée | AMF 8,3 Md€+ en 2025 ; gel DGF 2026 — difficulté à signer un nouvel abonnement |
| **Cycles d'achat publics** | Élevée | Marchés, grilles DGFIP, délais longs ; CAC 12–24 mois **à vérifier** par taille de collectivité |
| **Décalage des comptes** | Moyenne | Benchmark sur N-1/N-2 quand l'exercice en cours est en exécution (Hélios) |
| **Commoditisation IA** | Moyenne | FMPC intègre déjà IA (simulateur fiscal, rapport) — https://www.fmpc.fr/ , consulté 2026-06-20 |
| **Dépendance méthodologique OFGL** | Faible | Formules publiques ; risque si l'OFGL change les agrégats |

## 9. Effort MVP

Périmètre minimal crédible (si l'idée n'était pas saturée) :

1. **Ingestion** : jeux OFGL communes + EPCI 2017–2024 + REI + geo.api.gouv.fr → DuckDB.
2. **Moteur de comparaison** : sélection auto de panel (strate DGFiP + département), percentiles sur 5 indicateurs (épargne brute/hab, DRF/hab, encours dette/hab, taux d'endettement, fiscalité/hab).
3. **Écran DGS** : fiche collectivité + écarts vs panel + tendance 5 ans (SQL uniquement).
4. **Écran élu** : synthèse 1 page PDF (LLM sur texte, chiffres injectés depuis SQL).
5. **2 alertes** : dégradation > 1 écart-type vs strate sur 2 exercices ; ratio d'alerte réglementaire (R.2313-1).
6. **Traçabilité** : chaque chiffre → dataset + `exer` + formule OFGL.

**Effort estimé** : 4–8 semaines pour un MVP fonctionnel (données prêtes), **mais** 12–24 mois pour atteindre parité feature avec Manty/LocalNova (connecteurs, prospective, consolidation). Sans différenciation, le MVP n'a **pas de go-to-market**.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré | Justification |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 | Douleur réelle (pression budgétaire, mandats) mais déjà adressée par plusieurs couches |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 | Payeurs et budgets existent (LocalNova 500 €+, Manty) mais marché capté + gratuit massif + budgets 2025–2026 tendus |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 | DGFiP/OFGL open, APIs ; réserve sur décalage temporel et périmètre non consolidé |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 | **10+ solutions** dont l'officiel OFGL ; benchmark par strate = fonctionnalité standard |
| C5 | Différenciation défendable | 2 | 1 | 2 | Aucun verrou ; Manty et LocalÉvaluation font déjà le comparatif open data |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 | SQL sur OFGL/DGFiP + LLM cantonné au sens ; conforme RAG(sens)/SQL(chiffres) |
| C7 | Facilité du MVP | 2 | 3 | 6 | Données prêtes mais parité concurrentielle et méthodologie strates non triviales |
| C8 | Maîtrise des risques | 2 | 2 | 4 | Risque concurrentiel et budgétaire mal maîtrisable pour un nouvel entrant |
| C9 | Monétisation / impact | 2 | 2 | 4 | Revenu B2G difficile face au gratuit ; impact marginal vs outils existants |
| | **Total** | | | **56 / 105** | |

**Score /100** : 56 / 105 × 100 = **53** (arrondi)

## 11. Verdict & décision

**❌ Écartée** — score **53 / 100** (< 55).

L'idée décrite est **factuellement redondante** avec l'offre existante. Le seed alertait à juste titre sur **data.ofgl.fr** et **NosFinancesLocales** : l'OFGL propose déjà cartographie, ~70 ratios et comparaison par strate ; NosFinancesLocales est fermé mais a été remplacé par une **floriculture** de réutilisations (DépensesPubliques, FMPC) et de SaaS matures (LocalNova LocalBenchmark/LocalÉvaluation, Manty comparaison open data, RCF Repères). Construire un 11ᵉ benchmark sur les mêmes jeux DGFiP/OFGL n'apporte pas de valeur défendable ni de chemin de monétisation crédible.

**Point quasi éliminatoire** : le **product-market fit est négatif** — la cible peut obtenir gratuitement (OFGL, Collectiv'Finances, LocalOpen, DépensesPubliques) ce que l'idée vendrait, et paie déjà des éditeurs installés pour le reste (prospective, connecteurs métiers, consolidation).

**Prochaine étape** : ne pas prototyper. Si l'on souhaite creuser le secteur « finances locales », pivoter vers un angle **non couvert** (ex. croisement finances + commande publique DECP par politique publique, ou audit CFU/dette avec données non encore agrégées par l'OFGL) — hors périmètre de cette fiche.

---

0020 | Benchmark financier inter-collectivités (pour DGS/élus) | ❌ Écartée | 53/100 | Marché saturé, OFGL gratuit suffit
