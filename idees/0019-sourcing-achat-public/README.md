# Sourcing & benchmark de prix pour acheteurs publics (côté acheteur)

- **ID** : 0019
- **Statut** : ❌ Écartée
- **Score** : 50 / 100
- **Dernière mise à jour** : 2026-06-23
- **Pitch (1 phrase)** : Outil B2G pour les acheteurs publics (collectivités,
  hôpitaux, ministères) : à partir des DECP (marchés attribués) + recensement,
  benchmarker les prix payés par CPV, identifier des fournisseurs (sourcing),
  repérer des acheteurs comparables — **côté acheteur**, distinct de l'idée 0001
  (intelligence pour les **entreprises** répondant aux AO).

---

## 1. Problème / douleur
Avant de lancer une procédure, l'acheteur public doit **estimer le juste prix**
(éviter infructueux ou offres anormalement basses), **identifier des
fournisseurs qualifiés** (sourcing, art. R.2111-1 CCP) et parfois **se comparer**
à des acheteurs voisins (volume, procédures, ticket médian). Ces tâches sont
chronophages et souvent faites « au doigt mouillé » faute d'outils intégrés au
flux de travail. La douleur est **réelle et récurrente** — elle est d'ailleurs
le discours marketing explicite de plusieurs produits existants (voir §4) — mais
elle est **déjà adressée** par des suites MPE, des SaaS IA dédiés acheteurs et
des portails publics gratuits.

## 2. Cible & qui paie
- **Utilisateurs** : acheteurs publics (services achats, juristes marchés,
  prescripteurs techniques) dans collectivités, EPCI, hôpitaux, universités,
  services de l'État.
- **Payeurs potentiels** : la même entité publique (budget fonctionnement /
  transformation numérique / marchés subséquents UGAP).

**Payeurs identifiés avec budget constaté :**
- **marchespublics.ai — offres Acheteurs publics** : plans documentés **290 € /
  990 € / 2 490 € HT/mois** (3 480 € à 29 880 € HT/an), sous le seuil de dispense
  R.2122-8 (60 k€ HT/an services depuis 01/04/2026) — sourcing + benchmark DECP
  inclus dès le plan Solo. — https://marchespublics.ai/administrations ,
  https://marchespublics.ai/tarifs (consultés 2026-06-20)
- **MA.iA (Pyxis-Support)** : **300+ organismes publics** (UGAP, RATP,
  universités, hôpitaux cités), licence via **UGAP** (réf. 892343), CAIH, CFI,
  SICTIAM, CANUT — sourcing + benchmark sur **+16 M données** ; tarif sur devis
  (non public). — https://ma-ia.app/ , https://www.ugap.fr/informatique-et-telephonie-2/informatique-bureautique-6/logiciel-381/editeurs-de-logiciels-124456/gestion-du-sourcing-et-des-achats-publics-124547 (consultés 2026-06-20)

**Freins structurels à un SaaS autonome « benchmark DECP » :**
1. **Outils gratuits** couvrant le cœur du besoin (decp.info, data.economie,
   Observatoire Nextend.ai) → consentement à payer faible pour la seule couche
   données.
2. **Bundling** dans les suites MPE déjà payées (Atexo Local Trust, Ordiges) :
   sourcing + BI statistiques inclus dans le profil acheteur.
3. **Cycle d'achat public** : même sous dispense, validation hiérarchique et
   préférence pour les centrales (UGAP, CAIH) plutôt qu'un nouvel éditeur.

Utilisateur = payeur en théorie, mais le **budget additionnel** pour un outil
standalone DECP est difficile à arracher face au gratuit et au bundling.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| DECP consolidées (format tabulaire) | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | Licence Ouverte 2.0 | Parquet / CSV | ~quotidienne (MAJ data.gouv indiquée « today » le 2026-06-20) | Seuil déclaration **40 k€ HT** (MAPA & marchés < seuil absents) ; `montant` = montant **à la notification** / max accord-cadre ≠ dépense réelle ; **pas de prix unitaires** (DPGF/BPU) dans le schéma DECP standard |
| DECP — interface DAJ (exploration) | https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/ | Licence Ouverte (portail Etalab) | Interface web + export CSV/Parquet | Continue | Même sémantique `montant` ; exploration manuelle, pas produit métier acheteur |
| API tabulaire data.gouv (DECP) | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | Licence Ouverte 2.0 | JSON tabulaire via API | ~quotidienne | Rate limit ~100 req/s ; volumétrie importante |
| Référentiel schéma DECP v2.0 (fusion recensement) | https://www.data.gouv.fr/datasets/referentiel-de-donnees-marches-publics | — | Documentation schéma | — | Depuis **01/01/2024**, recensement économique et DECP fusionnés en une seule liste « données essentielles » (≥ 40 k€ HT) ; **plus de jeu REAP séparé** |
| Base SIRENE (enrichissement fournisseurs) | https://www.data.gouv.fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret | Licence Ouverte | CSV | Mensuelle (INSEE) | Enrichissement titulaires (NAF, effectif) ; pas de lien automatique CPV↔NAF fiable à 100 % |
| **Subventions SCDL** | Schéma https://schema.data.gouv.fr/scdl/subventions/ | LO 2.0 | CSV par collectivité | Hétérogène (vérifié 2026-06-21) | Pas de consolidation nationale ; obligation > 23 k€ |
| **RNA** (associations bénéficiaires) | https://www.data.gouv.fr/datasets/repertoire-national-des-associations | LO 2.0 | CSV | MàJ mai 2026 | Lien subvention→RNA pas toujours structuré |
| Statistiques agrégées OECP (recensement annuel) | https://www.weka.fr/actualite/commande-publique/article/recensement-des-marches-publics-les-resultats-2024-sont-connus-212163/ | — (publication presse, source OECP mars 2026) | Rapport PDF / articles | Annuelle (2024 publié mars 2026) | Agrégats nationaux, pas outil de benchmark unitaire |

> [`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements envisagés

| Croisement | Valeur acheteur | Limite |
|---|---|---|
| DECP × subventions SCDL (même SIRET) | Fournisseur titulaire de marchés ET bénéficiaire de subventions publiques | Couverture SCDL incomplète |
| DECP × SIRENE (NAF) | Sourcing fournisseurs par secteur sur marchés comparables | CPV ↔ NAF = heuristique |
| DECP acheteur × OFGL | Acheteur comparable par strate financière (extension benchmark inter-collectivités) | Code commune / SIRET acheteur |

Voir idée [0027](../0027-transparence-subventions-marches/) pour l'angle transparence
(journalistes) du croisement subventions × marchés.

> **Note recensement vs DECP** : depuis le décret n°2022-767 et les arrêtés du
> 22/12/2022 (en vigueur 01/01/2024), le recensement économique (ex-REAP) et les
> données essentielles sont **un seul dispositif** publié sur data.gouv.fr. Les
> statistiques OECP en découlent ; il n'existe plus de source « recensement »
> distincte à croiser. — https://www.economie.gouv.fr/daj/publication-de-deux-arretes-relatifs-aux-donnees-essentielles-des-marches-publics-et-aux ,
> https://www.atexo.com/actualites/article-a-la-une-le-recensement-des-donnees-de-l-achat-public-65/ (consultés 2026-06-20)

Clés techniques DECP utiles : `uid` (SIRET acheteur + id marché), `acheteur_id`,
`codeCPV`, `titulaire_id`, `montant`, `dateNotification`, `donneesActuelles`
→ **agrégats SQL fiables**, mais **indicateur « prix payé » métier fragile**
(cf. §6).

## 4. Existant / concurrence

> Cartographie B (consultée 2026-06-23).

**Verdict de saturation : saturé sur le créneau « benchmark DECP + sourcing +
acheteurs comparables côté acheteur ».** Au moins **8 acteurs** couvrent
explicitement le seed ; plusieurs en produit B2G commercial self-service.

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **data.economie.gouv.fr — DECP** | https://data.economie.gouv.fr/ | Interface DAJ, visualisation DECP |
| **data.gouv.fr — DECP consolidées** | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | Dump tabulaire officiel |
| **PLACE / achatpublic.com** | https://www.achatpublic.com/ | Profils acheteurs, module Sourcing |
| **OECP — Guide prix marchés publics** | https://draaf.normandie.agriculture.gouv.fr/guide-sur-le-prix-dans-les-marches-publics-oecp-a3680.html | Méthode officielle estimation prix |

### Réutilisations data.gouv

| Acteur | URL | Rôle |
|---|---|---|
| **decp.info** | https://www.data.gouv.fr/reuses/decp-info-interface-dexploration-et-de-telechargement-des-donnees-de-la-commande-publique-au-format-tabulaire | Exploration/export DECP gratuit |
| **Nextend.ai Observatoire** | https://nextend.ai/observatoire | Comparateur acheteurs (gratuit) |

### Produits B2G dédiés acheteurs (concurrents directs)

1. **marchespublics.ai — Acheteurs publics** : sourcing fournisseurs (DECP +
   SIRENE), benchmark prix sur **10 M+ contrats**, comparables CPV/géo, aide
   estimation, évaluation offres, DCE assisté IA. Tarifs **290 / 990 / 2 490 €
   HT/mois**. — https://marchespublics.ai/administrations (consulté 2026-06-20)
   → **C'est le produit décrit par le seed**, côté acheteur.

2. **MA.iA (Pyxis-Support)** : depuis **2021**, module **Sourcing** (« études de
   marché, veille fournisseurs et benchmarks »), **+16 M données** en dataviz,
   **300+ clients** publics, référencé **UGAP / CAIH / SICTIAM**. Tarif sur
   devis. — https://ma-ia.app/ , https://www.code-commande-publique.com/testez-ma-ia-gratuitement-4-jours/ (consultés 2026-06-20)

3. **Sam IA (Dematis)** : assistant IA pour **acheteurs publics** — analyse
   technique & financière des offres, tableaux comparatifs, rapports d'analyse ;
   intégré à l'écosystème Marchés Publics Dematis (profil acheteur). —
   https://www.dematis.com/sam-ia/ (consulté 2026-06-20)

### Suites MPE / profils acheteurs (sourcing intégré, déjà payées)

4. **Atexo — Local Trust Achat public** : module **« Le sourcing fournisseurs »**
   + **« BI & Statistiques du profil acheteur »** dans une suite couvrant tout le
   processus achat ; **+50 000 acheteurs** sur la plateforme. —
   https://www.atexo.com/solutions/solutions-achats-et-marches-publics/ (consulté 2026-06-20)

5. **Ordiges — Solution Achats Publics** : sourcing fournisseurs, identification,
   négociations, devis, « du sourcing aux paiements » dans un SI achats unique.
   — https://ordiges.com/solution-achat-public/ (consulté 2026-06-20)

6. **achatpublic.com — module Sourcing** (portail national Atexo) : consultations
   préalables, études de marché, base qualifiée d'entreprises, traçabilité ;
   évolution **Scribe** (assistant IA) annoncée juin 2026. —
   https://www.achatpublic.com/achat-public/sourcing (consulté 2026-06-20)

### Outils gratuits / open data (substituts au payant)

7. **decp.info** (Colin Maudry) : exploration, filtrage, export CSV/XLSX des
   DECP ; enrichissements acheteur/titulaire (population, distance km) ; MAJ
   quotidienne ; API Datasette. Gratuit. —
   https://decp.info , https://www.data.gouv.fr/reuses/decp-info-interface-dexploration-et-de-telechargement-des-donnees-de-la-commande-publique-au-format-tabulaire (consultés 2026-06-20)

8. **data.economie.gouv.fr — interface DAJ** : visualisation interactive DECP,
   filtres acheteur / CPV / période, export CSV/Parquet sans code. —
   https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/ ,
   https://www.data.gouv.fr/reuses/consultation-des-donnees-de-la-commande-publique (consultés 2026-06-20)

9. **Nextend.ai — Observatoire** : **gratuit** — profils **14 000+ acheteurs**,
   **comparateur jusqu'à 5 acheteurs** côte à côte (volumes, concurrence, PME,
   procédures), atlas, baromètre annuel ; MAJ quotidienne, documente les délais
   de publication réels. Cible aussi les entreprises mais **l'outil
   « acheteurs comparables » est déjà là**. —
   https://nextend.ai/observatoire , https://nextend.ai/observatoire/comparateur (consultés 2026-06-20)

### Ressources institutionnelles (méthode, pas SaaS)

10. **OECP / DAJ — Guide « Le prix dans les marchés publics » (2023)** : boîte à
    outils méthodologique (~200 p.) pour acheteurs (estimation, OAB, notation
    prix) ; **pas un benchmark automatisé DECP**. —
    https://draaf.normandie.agriculture.gouv.fr/guide-sur-le-prix-dans-les-marches-publics-oecp-a3680.html (consulté 2026-06-20)

### Adjacent côté entreprise (≠ seed mais même donnée)

- **Doaken, Olra, marchespublics.ai Entreprises, Vecteur Plus** : benchmark /
  intelligence DECP pour **candidats** (réponse AO, DPGF), pas acheteurs — cf.
  idée **0001**. Vecteur Plus reste orienté **fournisseurs** (détection AO,
  études marché payantes sur devis). — https://doaken.fr/fonctionnalites/chiffrage-dpgf ,
  https://www.vecteurplus.com/maitriser-son-marche/ (consultés 2026-06-20)

**Où serait l'espace libre ?** Très étroit :
- **Prix unitaires ligne à ligne** (DPGF/BPU) : Doaken le fait côté **soumissionnaire** ;
  côté acheteur, nécessiterait des pièces dématérialisées hors DECP open data.
- **Benchmark sur dépense réelle consommée** (bons de commande) : données non
  ouvertes.
- **Intégration profonde au SI acheteur** (historique interne + DECP) : marché
  des éditeurs MPE (Atexo, Ordiges), barrière d'entrée forte.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0019-sourcing-achat-public` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `public-procurement-intel` — Intelligence marchés publics

Fichier : [`catalogue-saas/vendors/public-procurement-intel.json`](../../catalogue-saas/vendors/public-procurement-intel.json) (42 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `marchespublics-ai` | marchespublics.ai | FR | strong | verified |
| `maitre-ao` | Maître AO | FR | strong | verified |
| `aws-boamp` | BOAMP (open data) | FR | strong | verified |
| `achatpublic` | PLACE (achatpublic.com) | FR | strong | verified |
| `tussell` | Tussell | GB | absent | partial |
| `spend-network` | Spend Network | GB | absent | partial |
| `govwin-deltek` | GovWin (Deltek) | US | absent | partial |
| `open-contracting-partnership` | Open Contracting Partnership | GB | unknown | partial |
| `decp-info` | decp.info | FR | strong | verified |
| `data-economie-gouv` | data.economie.gouv.fr | FR | strong | partial |
| `openbar` | OpenBar (Regards Citoyens) | FR | strong | partial |
| `nextend-ai` | Nextend.ai | FR | strong | verified |
| … | _+30 autres_ | | | |

#### Segment `spend-procurement` — Spend & procurement

Fichier : [`catalogue-saas/vendors/spend-procurement.json`](../../catalogue-saas/vendors/spend-procurement.json) (18 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `coupa` | Coupa | US | partial | partial |
| `zip` | Zip | US | partial | partial |
| `procurify` | Procurify | US | partial | partial |
| `spendesk` | Spendesk | FR | strong | partial |
| `tipalti` | Tipalti | US | partial | partial |
| `sap-ariba` | SAP Ariba | DE | partial | partial |
| `ivalua` | Ivalua | FR | strong | partial |
| `jaggaer` | JAGGAER | US | partial | partial |
| `proactis` | Proactis | GB | partial | partial |
| `gep-smart` | GEP SMART | US | partial | partial |
| `zycus` | Zycus | US | partial | partial |
| `pleo` | Pleo | DK | partial | partial |
| … | _+6 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment public-procurement-intel
```

<!-- catalogue-saas-end -->
## 5. Différenciation
**Quasi inexistante** pour le périmètre du seed. Les trois piliers annoncés —
benchmark prix DECP par CPV, sourcing fournisseurs, acheteurs comparables — sont
**déjà livrés** par marchespublics.ai (payant, côté acheteur), MA.iA (payant via
centrales), Nextend (gratuit, comparateur acheteurs) et decp.info / data.economie
(gratuit, exploration). La donnée DECP est en **Licence Ouverte 2.0** : tout
concurrent peut reproduire l'agrégation en quelques semaines. Aucun avantage
durable identifiable sans pivot majeur (ex. prix unitaires DPGF, données privées
acheteur, verticalisation sectorielle BTP avec pièces déposées) non couvert par
le seed.

**Distinction vs idée 0001** : 0001 vise les **entreprises** (qui a gagné, parts
de marché concurrents) ; 0019 vise les **acheteurs** (estimation, sourcing amont).
En pratique, **marchespublics.ai scinde déjà les deux côtés** (plans Entreprises
149–1 290 €/mois vs Acheteurs 290–2 490 €/mois) sur la même base DECP — le
positionnement « côté acheteur » n'isole pas d'un marché vierge.

## 6. Faisabilité & fiabilité technique
- **Architecture conforme RAG(sens) / SQL(chiffres)** si bien conçue : volumes,
  médianes, comptages par CPV/région/acheteur, listes de titulaires → **requêtes
  SQL** (DuckDB/PostgreSQL) sur DECP consolidé + jointure SIRENE. Le LLM cantonné
  à l'explication (libellés CPV, procédures, formulation sourcing).
- **Limite métier majeure (pas hallucination LLM)** : le champ `montant` DECP
  reflète le montant **à la notification** et, pour les accords-cadres, le
  **maximum** — pas la consommation réelle. Un « benchmark prix » affiché comme
  « ce que les collectivités paient » peut être **exact en SQL et trompeur en
  métier** (cf. revue 0001). Idem pour les **délais de publication** (légal 2
  mois, en pratique mois à années — documenté par Nextend.ai sur le baromètre
  2025).
- **Pas de prix unitaires** dans les DECP standard → benchmark « par prestation
  fine » impossible sans autre source (DCE archivés, DPGF uploadés).
- **Sourcing** via historique DECP + SIRENE : faisable et traçable ; qualité
  dépend de la couverture CPV et des seuils de déclaration.

## 7. Monétisation / impact
- **Revenu standalone fragile** : marchespublics.ai a déjà ancré des prix publics
  (290–2 490 €/mois) ; MA.iA occupe les centrales ; le gratuit (Nextend, decp.info,
  data.economie) capte l'usage exploratoire. Un nouvel entrant devrait concurrencer
  sur le prix ou l'intégration — les deux sont défavorables.
- **Impact sociétal** (meilleure estimation, plus de concurrence) : réel en
  théorie, mais **déjà adressé** par l'open data et les outils cités ; marginal
  pour un 10ᵉ acteur.
- Modèle crédible restant : **module intégré** vendu à un éditeur MPE (Atexo,
  Ordiges, Dematis) plutôt que SaaS autonome — ce qui change fondamentalement
  l'idée « startup open data ».

## 8. Risques
- **Concurrence / commoditisation** : risque principal ; le créneau est occupé
  par des acteurs financés (MA.iA depuis 2021, marchespublics.ai produit mûr) et
  des substituts gratuits performants.
- **Promesse « benchmark prix »** : risque de décision acheteur biaisée si les
  limites sémantiques du `montant` DECP ne sont pas affichées (OAB, estimation
  MAPA).
- **Cycle de vente B2G** : long, centrales d'achat, marchés subséquents ; CAC
  élevé pour ARPU modeste (quelques k€/an).
- **Couverture incomplète** : MAPA < 40 k€ absents ; accords-cadres sans
  consommation ; publication tardive → sourcing/benchmark sur marchés récents
  structurellement incomplets.
- **Pas de risque éliminatoire juridique** (contrairement à une réutilisation
  mal cadrée de données personnelles) si on reste sur des données DECP ouvertes
  et des agrégats ; vigilance sur la formulation en sourcing (ne pas créer de
  liste restreinte déguisée).

## 9. Effort MVP
Périmètre minimal crédible (déjà réalisé par d'autres) :
1. Ingestion DECP consolidé + SIRENE → base analytique.
2. Écran **benchmark** : fourchette montants par CPV + filtres géo + taille
   acheteur, avec **taux de couverture** et disclaimer sémantique `montant`.
3. Écran **sourcing** : liste titulaires récurrents sur CPV + carte géo.
4. Écran **acheteurs comparables** : profils + comparateur 3–5 entités.
5. Traçabilité : chaque chiffre → requête SQL + date snapshot DECP.

Effort technique **modéré** (4–8 semaines pour un MVP) mais **sans justification
marché** face à l'existant. Le coût réel serait l'acquisition client B2G, pas le
code.

## 10. Scoring

> **Scoring ajusté après revue critique du 2026-06-23** (voir [`revue.md`](revue.md)).
> Note abaissée : C2 (3→2). Score 53 → **50** ; verdict inchangé (❌ Écartée, marge
> sous le seuil élargie). Notes initiales rappelées en colonne dédiée.

| # | Critère | Poids | Note initiale | Note (post-revue) | Pondéré |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 4 | 12 |
| C2 | Cible solvable (qui paie) | 3 | 3 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | 3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | 2 | 1 | 1 | 2 |
| C5 | Différenciation défendable | 2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 3 | 3 | 6 |
| C8 | Maîtrise des risques | 2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | 2 | 2 | 2 | 4 |
| | **Total** | | | | **53 / 105** |

**Score /100** : 53 / 105 × 100 = **50**

Justification des notes (post-revue) :
- **C1 = 4** : estimation prix, sourcing et comparaison inter-acheteurs sont des
  douleurs récurrentes documentées par les produits existants et le guide OECP.
- **C2 = 2** (ajusté) : payeurs et budgets existent mais **partent ailleurs** —
  gratuits (decp.info/data.economie/Nextend), bundling MPE (Atexo/Ordiges),
  centrales (UGAP/CAIH) ; le budget *additionnel* pour un SaaS standalone est quasi
  inexistant (constat de la fiche elle-même).
- **C3 = 3** : DECP ouvert et quotidien, SQL fiable sur agrégats, mais `montant`
  ≠ dépense réelle, pas de prix unitaires, délais de publication longs.
- **C4 = 1** : au moins 8 solutions (3 B2G dédiées, 3 MPE, 3 gratuites) couvrent
  exactement le seed ; le dernier résidu « acheteurs comparables » est lui-même
  fermé par **OFGL/data.ofgl.fr** (gratuit) + Nextend → marché saturé côté acheteur.
- **C5 = 1** : même proposition que marchespublics.ai Acheteurs et MA.iA Sourcing,
  sur donnée ouverte copiable.
- **C6 = 4** : archi RAG(sens)/SQL(chiffres) saine pour agrégats ; réserve sur la
  fiabilité métier du « prix » affiché.
- **C7 = 3** : MVP rapide techniquement, mais sans créneau libre pour le déployer.
- **C8 = 2** : concurrence et commoditisation mal maîtrisées ; promesse prix fragile.
- **C9 = 2** : revenu standalone faible, impact déjà capté par l'existant.

## 11. Verdict & décision
❌ **Écartée.** Score **50/100** après revue critique du 2026-06-23 (< 55 ; recalcul
C2 3→2, et fermeture du dernier résidu « acheteurs comparables » par OFGL gratuit).
Le problème est réel et les données DECP
utilisables, mais le seed décrit un produit **déjà commercialisé** (marchespublics.ai
Acheteurs, MA.iA) et **gratuitement accessible** (Nextend comparateur, decp.info,
data.economie). La distinction avec l'idée 0001 (côté entreprise) ne crée pas
d'espace : la même donnée sert les deux marchés et des acteurs couvrent déjà
explicitement le **côté acheteur**. Sans pivot (prix unitaires DPGF, données
internes acheteur, intégration MPE), il n'y a pas de différenciation défendable.

**Prochaine étape concrète** : ne pas prototyper ce positionnement. Si l'on reste
sur la commande publique open data, reprendre l'angle **0001** (intelligence
attribution côté entreprise — déjà « à retravailler ») ou chercher un sous-creneau
**non couvert** : ex. audit qualité DECP pour acheteurs (conformité déclaration),
ou analyse **ligne à ligne DPGF** côté acheteur à l'instruction des offres (hors
DECP agrégé) — à valider par une nouvelle recherche existant avant toute capture.

---

0019 | Sourcing & benchmark de prix pour acheteurs publics (côté acheteur) | ❌ Écartée | 50/100 | Saturé : marchespublics.ai, MA.iA, Nextend + OFGL gratuits ; revue 2026-06-23
