# Conformité de publication open data des collectivités (B2G)

- **ID** : 0023
- **Statut** : ❌ Écartée
- **Score** : 47 / 100
- **Dernière mise à jour** : 2026-06-20
- **Pitch (1 phrase)** : Outil B2G aidant les collectivités assujetties (LRN 2016) à **vérifier et atteindre** leur conformité de **publication** open data — inventaire réglementaire vs jeux publiés, écarts, feuille de route — distinct de l'idée **0002** (qualité technique des datasets déjà publiés).

---

## 1. Problème / douleur

Les collectivités de plus de 3 500 habitants et 50 agents sont tenues depuis 2018 de diffuser en open data leurs bases de données, documents du répertoire des informations publiques (RIP) et données d'intérêt économique, social, sanitaire ou environnemental ([guide juridique data.gouv.fr](https://guides.data.gouv.fr/guides/guide-juridique/producteurs-de-donnees/quelles-sont-les-obligations), consulté 2026-06-20 ; [CNIL](https://www.cnil.fr/fr/les-collectivites-territoriales-et-lopen-data-concilier-ouverture-des-donnees-et-protection-des), consulté 2026-06-20).

**Constat chiffré** : en septembre 2025, seulement **30 %** des collectivités territoriales et EPCI assujettis ont publié **au moins un** jeu de données open data au cours de la dernière décennie ([Observatoire OpenDataFrance](https://opendatafrance.fr/presentation-de-lobservatoire/), consulté 2026-06-20). Une étude Data Publica × Opendatasoft (avril 2024) évaluait à **16 %** le taux de collectivités tenues de publier qui le font réellement ([Banque des Territoires](https://www.banquedesterritoires.fr/open-data-les-pratiques-des-collectivites-les-plus-en-pointe), consulté 2026-06-20).

La douleur est **réelle pour les référents data/DGS** (incertitude juridique, pression des intercommunalités, audits internes), mais **atténuée** par l'absence de sanctions prévues pour le non-respect ([Datactivist / rapport Ardèche](https://datactivist.coop/ardeche/rapport/partie2.html), consulté 2026-06-20) et par la baisse de la priorité « transparence » dans le baromètre Data Publica 2025 (**43 %** vs 59 % en 2024 ; [Banque des Territoires](https://www.banquedesterritoires.fr/observatoire-data-publica-lia-generative-poursuit-sa-percee-et-impacte-les-collectivites-de-toutes), consulté 2026-06-20).

**Distinction vs idée 0002** : 0002 vise la **qualité technique** des jeux déjà publiés (liens morts, fraîcheur, schéma). Ici, l'enjeu est **réglementaire** : suis-je assujetti ? Qu'ai-je l'obligation de publier ? Qu'ai-je effectivement publié ? Quel écart ? Quelle feuille de route ?

---

## 2. Cible & qui paie

| Acteur | Rôle | Capacité à payer |
|---|---|---|
| **Référent open data / DGS / DSI** des communes et EPCI (3 346 communes AMF + EPCI, régions, départements) | Utilisateur quotidien | Budget limité ; **obstacle financier** cité pour les prestataires ([note BDT 2024](https://www.banquedesterritoires.fr/sites/default/files/2024-11/Banque_des_territoires_Note-conjoncture-IA-2024-web.pdf), consulté 2026-06-20) |
| **Animateurs territoriaux des données (ATD)** via OpenDataLocale | Accompagnement de proximité des PME communes | Financé par **DINUM + ANCT** (Plan de Relance), pas par abonnement SaaS ([OpenDataLocale](https://opendatafrance.gitbook.io/opendatalocale), consulté 2026-06-20) |
| **Banque des Territoires / DINUM / ANCT** | Finance l'écosystème public (ODF, Observatoire, Numérique360) | Partenariat BDT–ODF signé **18 juin 2025** pour actualiser l'Observatoire ([BDT](https://www.banquedesterritoires.fr/la-banque-des-territoires-et-opendatafrance-sassocient-pour-soutenir-les-collectivites), consulté 2026-06-20) |
| **Éditeurs (Huwise/Opendatasoft)** | Portail de publication | Budget **licence portail** constaté (~80 % des 147 portails dédiés en 2023) ; pas de ligne budgétaire identifiée pour un outil de conformité tiers ([cinquième-pouvoir.fr](https://www.cinquieme-pouvoir.fr/2024/05/loi-pour-une-republique-numerique-peu-de-collectivites-publient-leurs-donnees/), consulté 2026-06-20) |
| **Prestataires (Datactivist, multi, cabinets)** | Missions d'accompagnement ponctuelles | Marchés publics ad hoc (ex. CD31) ; pas de produit récurrent identifié ([Datactivist CD31](https://datactivist.coop/fr/references/accompagnement-open-data-cd31/), consulté 2026-06-20) |

**Verdict C2** : la collectivité est la cible logique, mais **aucun payeur avec budget récurrent alloué à un outil de conformité** n'est identifié. L'État et la BDT financent déjà des alternatives gratuites ou mutualisées.

---

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| API catalogue data.gouv.fr (organisations, datasets, métriques) | https://www.data.gouv.fr/api/1/ — doc : https://guides.data.gouv.fr/api-de-data.gouv.fr/reference/organizations | Licence Ouverte (données catalogue) | JSON REST | Continue | Ne couvre que ce qui est **sur data.gouv.fr** ; portails Opendatasoft/CKAN locaux non moissonnés = angle mort |
| Observatoire ODT — base Grist | https://opendatafrance.getgrist.com/nVz8336s2Sh2/Observatoire/p/6 | À vérifier sur la page Grist | Tables Grist / export | **Mensuelle** (auto depuis 2025) | 1 975 orgs, 19 variables ; ~20 % MAJ manuelles ([rapport ODF 2025](https://opendatafrance.fr/wp-content/uploads/2025/08/Rapport-final-observatoire.pdf), consulté 2026-06-20) |
| Indicateurs statiques Observatoire | https://git.opendatafrance.net/observatoire/indicateurs/tree/master/static | Open source (dépôt Git) | CSV/JSON statique | Variable | Corpus partiel ; pas d'API temps réel documentée |
| Schémas SCDL / nationaux | https://schema.data.gouv.fr — SCDL : https://scdl.opendatafrance.net/docs/ | Standards référencés Etalab/ODF | JSON Table Schema | Continue (versionnés semver) | Couvre des **jeux prioritaires**, pas l'intégralité des obligations CRPA ; adoption SCDL ~**1,5 %** des jeux Opendatasoft ([BDT avril 2024](https://www.banquedesterritoires.fr/open-data-les-pratiques-des-collectivites-les-plus-en-pointe), consulté 2026-06-20) |
| Cadre juridique (CRPA, LRN) | https://guides.data.gouv.fr/guides/guide-juridique/producteurs-de-donnees/quelles-sont-les-obligations | Documentation publique | Texte structuré (GitBook) | À jour Etalab | **Sens** pour RAG, pas de liste machine-readable par collectivité |
| Seuils assujettissement (communes >3 500 hab.) | https://opendatafrance.fr/notice-methodologique/ — source AMF citée | — | Statistiques publiées | Réf. 2025 : **3 346** communes | Seuil **50 agents** non ventilé par commune (présupposé par ODF) |
| RIP (répertoire informations publiques) | Ex. DILA : https://dila.gouv.fr/services/repertoire-des-informations-publiques/qu-est-ce-que-le-rip | Variable | HTML/PDF par admin | Annuelle (obligation L.322-6 CRPA) | **Pas de base nationale unifiée** ; contenu laissé à l'appréciation de chaque collectivité ([CADA via Sénat](https://www.senat.fr/questions/base/2023/qSEQ230808134.html), consulté 2026-06-20) |
| Inventaire interne des données de la collectivité | — | — | — | — | **Inexistant en open data** : indispensable pour un vrai gap analysis, inaccessible sans mission sur site |

**Bloquant données** : on peut compter en SQL ce qui est **publié** sur data.gouv.fr ; on ne peut pas dériver en SQL ce que chaque collectivité **doit** publier (périmètre CRPA large, RIP non exhaustif, compétences variables).

---

## 4. Existant / concurrence

Le besoin n'est pas vierge : l'écosystème public et associatif couvre déjà le pilotage de conformité de publication, avec une trajectoire 2026 vers recommandations individualisées.

### 4.1. Observatoire open data des territoires (OpenDataFrance) — concurrent direct

- **URL** : https://opendatafrance.fr/presentation-de-lobservatoire/ (consulté 2026-06-20)
- **Fait** : mesure quantitative et qualitative de l'ouverture des données par collectivités ; collecte **automatique mensuelle** via data.gouv.fr depuis 2025 ; jauge d'assujettis vs publiants (30 % minimal) ; profils d'activité (très actives / actives / inactives / nouvelles) ; carte, histogrammes, base Grist.
- **Limite** : indicateur principal = **au moins un jeu publié**, pas inventaire exhaustif obligation par obligation ; ~20 % d'orgs en MAJ manuelle.
- **Roadmap 2026** : profils-types (pionnières, en transition, dormantes) et **recommandations adaptées** par catégorie ([rapport ODF 2025](https://opendatafrance.fr/wp-content/uploads/2025/08/Rapport-final-observatoire.pdf), consulté 2026-06-20) — recoupe directement la « feuille de route » du seed.

### 4.2. OpenDataLocale + kit de ressources ODF — accompagnement conformité

- **URL** : https://opendatafrance.fr/projets/opendatalocale-malette-open-data-des-territoires/ (consulté 2026-06-20)
- **Fait** : programme national d'accompagnement des collectivités à la LRN ; réseau d'ATD ; Observatoire comme **outil de mesure** du déploiement ; fiches « premières étapes », check-list prérequis (ex. OpenDataLab Occitanie).
- **Limite** : dispositif humain/territorial, pas SaaS self-service ; objectif historique 2 000 collectivités ouvertes (saison 3 depuis 2021).

### 4.3. OpenDataFactory (Validata, SCDL, DataClic) — conformité schéma, pas réglementaire globale

- **URL** : https://opendatafrance.fr/projets/opendatafactory/ (consulté 2026-06-20)
- **Fait** : SCDL = jeux prioritaires normalisés ; **Validata** = validation automatisée fichier vs schéma national ([validata.fr](https://validata.fr/), consulté 2026-06-20) ; coopération Etalab/DINUM.
- **Limite** : conformité **technique par schéma**, pas couverture de l'obligation CRPA globale ni croisement RIP ↔ catalogue.

### 4.4. Guides et services publics Etalab / data.gouv.fr

- **URL** : https://guides.data.gouv.fr/guides/guide-juridique/producteurs-de-donnees/ (consulté 2026-06-20)
- **Fait** : cadre juridique officiel (qui est concerné, quoi publier, formats, licences) ; guide publication collectivités ([data.gouv.fr](https://www.data.gouv.fr/posts/plateforme-data-gouv-fr-solutions-open-source-etc-comment-publier-ses-donnees-quand-on-est-une-collectivite-territoriale-1), consulté 2026-06-20).
- **Limite** : documentation, pas tableau de bord de conformité par organisme.

### 4.5. Observatoire Data Publica + étude Opendatasoft — baromètre et benchmark

- **URL** : https://observatoire.data-publica.eu/ (consulté 2026-06-20)
- **Fait** : enquête annuelle de référence (292 collectivités en 2025) ; étude open data × Opendatasoft (avril 2024) : 16 % de conformité, 147 portails dédiés, dominante CSV.
- **Limite** : enquête déclarative, pas outil opérationnel par collectivité.

### 4.6. Huwise (ex-Opendatasoft) — éditeur portail B2G

- **URL** : https://www.huwise.com/fr/blog/opendatasoft-franchit-une-nouvelle-etape-et-devient-huwise-leader-des-data-product-marketplaces/ (consulté 2026-06-20)
- **Fait** : SaaS portail open data pour collectivités ; répond à l'obligation de publication via mise en ligne ; >350 clients, ~3 000 portails ; investissement BDT historique ([BDT](https://www.banquedesterritoires.fr/opendatasoft-plateforme-de-gestion-et-de-valorisation-des-donnees-des-collectivites), consulté 2026-06-20).
- **Limite** : **outil de publication**, pas diagnostic d'écarts réglementaires vs inventaire interne.

### 4.7. Datactivist et prestataires territoriaux

- **URL** : https://datactivist.coop/fr/projects/collectivites/ (consulté 2026-06-20)
- **Fait** : accompagnement stratégique, formation, offres de service open data (ex. Haute-Garonne : 17 collectivités embarquées).
- **Limite** : consulting facturé au projet, non scalable produit.

### 4.8. ANCT — Démarche numérique responsable (feuille de route)

- **URL** : https://lesbases.anct.gouv.fr/ressources/demarche-numerique-responsable (consulté 2026-06-20)
- **Fait** : méthodologie en 5 étapes incluant diagnostic de maturité et **élaboration de feuille de route** numérique pour collectivités >3 500 hab. ; modèles licence Etalab 2.0.
- **Limite** : cadre général numérique responsable, pas spécialisé open data/conformité CRPA automatisée.

### 4.9. CNIL / CADA — conformité juridique RGPD + open data

- **URL** : https://www.cnil.fr/fr/les-collectivites-territoriales-et-lopen-data-concilier-ouverture-des-donnees-et-protection-des (consulté 2026-06-20)
- **Fait** : guide pratique publication et réutilisation ; arbitrage anonymisation / diffusion.
- **Limite** : guidance, pas scoring automatisé.

### 4.10. Banque des Territoires — Numérique360

- **URL** : https://opendatafrance.fr/la-banque-des-territoires-et-opendatafrance/ (consulté 2026-06-20)
- **Fait** : partenariat 2025 pour enrichir Numérique360 et actualiser l'Observatoire.
- **Limite** : orientation accompagnement public, concurrence gratuite pour un SaaS tiers.

**Verdict saturation** : **saturé** au niveau macro (Observatoire ODF, baromètres, guides Etalab) et **en cours de fermeture** au niveau micro (roadmap ODF 2026 = profils + recommandations). L'espace produit tiers se limiterait à un **tableau de bord par collectivité** croisant SCDL + RIP + catalogue — niche étroite, internalisable par ODF/Etalab.

---

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0023-conformite-open-data-collectivites` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-22 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `open-data-governance-fr` — Gouvernance open data FR

Fichier : [`catalogue-saas/vendors/open-data-governance-fr.json`](../../catalogue-saas/vendors/open-data-governance-fr.json) (9 entrées)

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

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment open-data-governance-fr
```

<!-- catalogue-saas-end -->
## 5. Différenciation

| Angle seed | Existant qui le couvre déjà | Écart résiduel |
|---|---|---|
| Vérifier l'assujettissement (>3 500 hab / 50 agents) | Notice méthodologique ODF + guide « Qui est concerné » Etalab | Calcul automatisé population (INSEE) + effectifs — **effectifs non ouverts** |
| Mesurer si la collectivité publie | Observatoire ODF (présence, volume, fraîcheur, plateforme) | Redondant |
| Écarts obligation vs publication | Partiellement via SCDL + Validata (schémas) ; pas globalement | Croisement **RIP local** ↔ jeux data.gouv — mais RIP non standardisé |
| Feuille de route | ODF 2026 (recommandations par profil) ; ANCT DNR ; kit ODF | Génération auto priorisée — **imitable** par ODF en un cycle Observatoire |

**Positionnement défendable** : faible. Le seul créneau crédible serait un **module complémentaire à 0002** (qualité) + check-list SCDL par SIRET, adossé à l'API data.gouv.fr — mais OpenDataFrance et Etalab le portent déjà via Validata et l'intégration schéma sur data.gouv.fr ([guide qualité schémas](https://guides.data.gouv.fr/guides/guide-qualite/maitriser-les-schemas-de-donnees), consulté 2026-06-20).

**Ne pas dupliquer 0002** : 0002 = qualité des ressources publiées ; 0023 = couverture réglementaire de publication. En pratique, les deux partagent l'API catalogue et les schémas ; un produit unique « producteur data » serait plus cohérent qu'une seconde idée, mais le marché public le couvre déjà.

---

## 6. Faisabilité & fiabilité technique

**Architecture envisageable**

1. **SQL** : crawl API `/organizations/` + `/organizations/{org}/datasets/` → comptages, thèmes, dates `last_modified`, tags schéma, badge `local-authority`.
2. **SQL** : croisement avec seuils AMF (3 346 communes) et données Observatoire Grist.
3. **SQL** : pour chaque schéma SCDL référencé, vérifier présence d'au moins un dataset tagué conforme (métadonnées data.gouv.fr).
4. **RAG (sens)** : interpréter le périmètre CRPA (documents RIP, bases de données, intérêt ESS) ; répondre aux questions « suis-je concerné ? », « ce type de donnée est-il communicable ? » depuis guides Etalab + CNIL.
5. **Heuristique / LLM** : proposer feuille de route — **non traçable** sans inventaire interne collectivité.

**Principe RAG(sens) / SQL(chiffres)**

| Métrique | Mode | Fiabilité |
|---|---|---|
| Nombre de jeux publiés par org | SQL | Haute |
| Dernière MAJ, profil actif/inactif | SQL | Haute |
| Taux national « ≥1 jeu publié » (30 %) | SQL (reproduction Observatoire) | Haute si même périmètre |
| % conformité réglementaire globale | RAG + hypothèses | **Basse** — dénominateur inconnu |
| Liste des jeux manquants obligatoires | RAG + SCDL partiel | **Moyenne** pour SCDL seul ; **faible** pour CRPA intégral |

**Verdict technique** : les chiffres de **publication** sont fiables en SQL ; tout score de **conformité réglementaire** global reposerait sur du RAG ou des listes inventées — contraire au principe §3 de `docs/methode-analyse.md`.

---

## 7. Monétisation / impact

- **Monétisation B2G SaaS** : peu crédible face au gratuit ODF + guides Etalab + financement BDT/DINUM. Les budgets identifiés vont aux **portails** (Opendatasoft/Huwise) et aux **missions ponctuelles** (Datactivist), pas à un abonnement conformité.
- **Impact sociétal** : élevé si l'outil était public/OSS et adopté par les ATD — mais OpenDataFrance remplit déjà cette fonction d'intérêt général.
- **Modèle réaliste** : prestation conseil (comme Datactivist) ou contribution open source à l'Observatoire, plutôt que revenu récurrent.

---

## 8. Risques

| Risque | Gravité | Commentaire |
|---|---|---|
| **Internalisation par OpenDataFrance / Etalab** | Élevée | Partenariat BDT–ODF juin 2025 ; Observatoire 2026 = recommandations par profil |
| **Donnée normative absente** (inventaire obligatoire par collectivité) | Éliminatoire | Sans RIP structuré national ni SI interne, le « gap » est partiellement indéductible |
| **Angle mort portails locaux** | Élevée | Données hors data.gouv.fr non vues par l'Observatoire auto (~20 % MAJ manuelle) |
| **Absence de sanctions LRN** | Moyenne | Faible levier d'achat côté élu |
| **Confusion avec 0002** | Moyenne | Deux produits sur la même API catalogue ; risque de cannibalisation interne au portefeuille d'idées |
| **Dépendance à Validata / schémas** | Moyenne | SCDL couvre une fraction des obligations |
| **Régression priorité open data** | Moyenne | Baromètre Data Publica 2025 : transparence en baisse comme priorité élu |

---

## 9. Effort MVP

**Périmètre minimal crédible** (6–8 semaines, équipe 2 pers.) :

1. Import API data.gouv.fr : toutes les orgs `badge=local-authority` + métriques datasets.
2. Règles SQL : assujettissement (liste AMF 3 346 communes + EPCI/régions/départements).
3. Check-list **SCDL uniquement** : pour chaque org, présence/absence des schémas prioritaires.
4. Dashboard org : publié / non publié, profil activité (calqué ODF), écarts SCDL.
5. RAG limité : FAQ juridique sourcée (guides Etalab, pas de chiffres inventés).
6. Export « prochaines actions » — **template**, pas feuille de route personnalisée fiable sans données internes.

**Hors MVP honnête** : crawl RIP de milliers de sites web ; intégration progiciels métiers ; scoring conformité CRPA intégral.

---

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 | Obligation légale réelle et ~70 % des assujettis sous le seuil minimal « ≥1 jeu », mais sans sanction ni urgence politique forte. |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 | Collectivités cibles mais budget capté par portails et dispositifs publics gratuits ; aucun payeur nommé pour un SaaS conformité. |
| C3 | Disponibilité & fiabilité données | 3 | 3 | 9 | Publication traçable via API ; inventaire des obligations par collectivité **non disponible** en open data. |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 | Observatoire ODF + ODL + Etalab + éditeurs couvrent le besoin ; roadmap 2026 ferme le gap feuille de route. |
| C5 | Différenciation défendable | 2 | 2 | 4 | Seul micro-angle SCDL×org imitable par ODF/Validata en un sprint. |
| C6 | Faisabilité & fiabilité technique | 2 | 2 | 4 | SQL OK pour comptages ; conformité réglementaire globale repose sur RAG/heuristiques non traçables. |
| C7 | Facilité du MVP | 2 | 2 | 4 | MVP honnête = check-list SCDL + statut publication, pas vérificateur CRPA complet. |
| C8 | Maîtrise des risques | 2 | 2 | 4 | Internalisation probable, données normatives absentes, priorité open data en recul. |
| C9 | Monétisation / impact | 2 | 2 | 4 | Fort impact potentiel en OSS public ; revenu B2G faible face au gratuit existant. |
| | **Total** | | | **49 / 105** | |

**Score /100** : 49 / 105 × 100 = **47**

---

## 11. Verdict & décision

**❌ Écartée** — score **47/100** (< seuil 55).

**Critère éliminatoire** : l'inventaire machine-readable de ce que chaque collectivité **doit** publier (RIP exhaustif, données internes par compétence) **n'existe pas** en open data. Un outil qui afficherait un « % de conformité réglementaire » sans cette source inventerait le dénominateur — violation du principe anti-hallucination.

**Synthèse** : le seed identifie une vraie tension (obligation LRN vs ~30 % de publiants minimaux), mais l'**Observatoire OpenDataFrance** ([présentation](https://opendatafrance.fr/presentation-de-lobservatoire/), 2026-06-20) couvre déjà le pilotage macro, évolue vers des **recommandations par profil** en 2026, et s'appuie sur une collecte auto mensuelle financée par l'État et la BDT. Les briques complémentaires (SCDL, Validata, guides Etalab, OpenDataLocale, portails Huwise) fragmentent le marché sans laisser de créneau SaaS défendable. Distinct de **0002** (qualité technique), mais les deux idées convergent sur l'API catalogue — mieux vaut, si poursuite, contribuer à l'écosystème ODF/Etalab qu'un produit autonome.

**Prochaine étape concrète** : aucun prototype recommandé. Si réouverture ultérieure : valider avec OpenDataFrance si la roadmap Observatoire 2026 laisse un module « check-list SCDL par organisme » non couvert, et n'envisager qu'un **pilote OSS** sur 1 EPCI + ~20 communes, sans score de conformité CRPA global.

---

0023 | Conformité de publication open data des collectivités (B2G) | ❌ Écartée | 47/100 | Marché saturé, données obligations absentes
