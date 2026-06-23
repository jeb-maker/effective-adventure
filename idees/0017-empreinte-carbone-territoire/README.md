# Empreinte carbone des territoires / PME

- **ID** : 0017
- **Statut** : ❌ Écartée
- **Score** : 44 / 100
- **Dernière mise à jour** : 2026-06-20
- **Révision critique** : voir [`revue.md`](revue.md) — score abaissé de **56 à 44**
  (écartée) après audit adversarial (pivot territorial déjà couvert par RARE/OREC ;
  licence ecoinvent payante pour un SaaS ; PME non solvable).
- **Pitch (1 phrase)** : Un outil qui s'appuie sur les facteurs d'émission ouverts
  de l'ADEME (Base Carbone / Base Empreinte) et sur les données locales d'énergie
  pour aider PME et collectivités à estimer et suivre leur empreinte carbone (bilan GES).

---

## 1. Problème / douleur
Mesurer son empreinte carbone est devenu un passage obligé : le **BEGES**
(bilan d'émissions de GES, art. L229-25 du Code de l'environnement) est
**obligatoire** pour les entreprises > 500 salariés (250 en outre-mer), les
collectivités > 50 000 habitants, l'État et les personnes morales publiques de
> 250 agents, avec **amende jusqu'à 50 000 € (100 000 € en récidive)** et un plan
de transition obligatoire ([mission-transition-ecologique.beta.gouv.fr, consulté
2026-06-20](https://mission-transition-ecologique.beta.gouv.fr/projets-entreprise/bilan-ges) ;
[hayot-expertise.fr, 2026-06-20](https://hayot-expertise.fr/blog/beges-entreprises-50-500-salaries-2026)).

**Nuance sceptique majeure** : la cible affichée (PME) n'est **pas** soumise à
l'obligation par son seul effectif — le seuil légal reste 500 salariés
([hayot-expertise.fr, 2026-06-20](https://hayot-expertise.fr/blog/beges-entreprises-50-500-salaries-2026)).
La douleur des PME est donc largement **induite** (pression des donneurs d'ordre,
chaîne de valeur CSRD/ESRS E1, appels d'offres), pas réglementaire directe. Et le
calcul lui-même est déjà partiellement résolu par des outils gratuits. La douleur
est réelle mais tiède pour le segment le moins solvable.

## 2. Cible & qui paie
- **Grandes entreprises / ETI assujetties au BEGES & à la CSRD** : budget réel,
  mais **segment déjà capté par des acteurs financés** (cf. §4). Payeur = utilisateur.
- **PME (cible du seed)** : payent peu, sont price-sensitive, et disposent
  d'alternatives gratuites ; budgets constatés 1 500–15 000 €/an
  ([logiciel-bilan-carbone.fr, 2026-06-20](https://www.logiciel-bilan-carbone.fr/)).
- **Collectivités > 50 000 hab.** : obligées (PCAET/BEGES), mais déjà outillées
  par les observatoires régionaux et l'ADEME (cf. §4).
- **Bureaux d'études RSE / cabinets** : payeurs possibles en marque blanche.

Le payeur existe et a un budget, mais le segment qui paie *bien* (ETI/grands
groupes) est précisément le plus concurrentiel ; le segment cité (PME) paie *peu*.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| Base Empreinte® ADEME (portail officiel) | https://base-empreinte.ademe.fr/ | Conditions d'utilisation ADEME (gratuit, compte requis) | Web / CSV / XLSX | MAJ ~annuelle (V23.6 juil. 2025, *version exacte à vérifier*) | Certaines données (issues d'**ecoinvent**) **non librement réutilisables** — l'ADEME n'en détient pas la propriété intellectuelle |
| Base Carbone® via API open data ADEME | https://data.ademe.fr/datasets/base-carbone | Licence Ouverte / Open Licence 2.0 | API data-fair/Koumoul (JSON), CSV, XLSX | MAJ périodique | Facteurs d'émission **uniquement** — ne contient aucune donnée d'activité de l'entreprise |
| Base Carbone complète (miroir data.gouv v17.0) | https://www.data.gouv.fr/datasets/base-carbone-complete-de-lademe-en-francais-v17-0 | Licence Ouverte 2.0 | CSV (UTF-8) / XLSX | Version figée (v17, ancienne) | Non maintenue, à recouper avec la version officielle |
| Consommation annuelle élec & gaz par commune/IRIS/EPCI (Agence ORE) | https://opendata.agenceore.fr/datasets/consommation-annuelle-d-electricite-et-gaz-par-iris | Licence Ouverte 2.0 | CSV / API Opendatasoft | Annuelle ; millésime 2024, MAJ 12 jan. 2026 | Cellules **masquées** (secret statistique / informations commercialement sensibles) ; maille agrégée, pas par entreprise |
| API Données locales de consommation d'énergie (SDES) | https://www.data.gouv.fr/dataservices/api-donnees-locales-de-consommation-denergie | Licence Ouverte | API | Continue | Données agrégées par territoire/secteur, pas individuelles |

**Limite structurelle de fond** : les open data ne couvrent que les **facteurs
d'émission** et des **consommations énergétiques agrégées**. Le cœur d'un bilan
GES — les **données d'activité propres à l'organisation** (factures, carburant,
déplacements, achats scope 3) — **n'est pas une donnée ouverte** : c'est de la
collecte interne, manuelle, spécifique à chaque client. L'open data ne fournit
donc que la moitié « facile » de l'équation.

## 4. Existant / concurrence

> Cartographie B (consultée 2026-06-23).

**Verdict de saturation : SATURÉ.** C'est l'un des créneaux climat-tech les plus
encombrés en France.

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **Base Empreinte® / Base Carbone® ADEME** | https://base-empreinte.ademe.fr/ | Facteurs d'émission nationaux (>3 000), API |
| **Plateforme Bilans GES ADEME** | https://bilans-ges.ademe.fr/ | Dépôt officiel bilans GES organisations |
| **Nos Gestes Climat** | https://nosgestesclimat.fr/ | Calculateur particuliers (beta.gouv, Publicodes) |
| **data.gouv.fr — inventaire GES** | https://www.data.gouv.fr/datasets/inventaire-national-des-emissions-de-polluants-atmospheriques-et-de-gaz-a-effet-de-serre | Émissions territoriales agrégées |

### Réutilisations data.gouv

| Acteur | URL | Rôle |
|---|---|---|
| **Empreinte territoriale (Territoires en Transitions)** | https://www.data.gouv.fr/reuses/empreinte-territoriale | Visualisation empreinte carbone par territoire |
| **Publicodes (beta.gouv)** | https://www.data.gouv.fr/reuses/publicodes | Langage de calcul ouvert pour modèles carbone |

### Outils publics / officiels (gratuits)

- **Base Empreinte® / Base Carbone® de l'ADEME** : la base de référence
  nationale, gratuite, > 3 000 facteurs, accessible en ligne et par API
  ([wecount.io, 2026-06-23](https://www.wecount.io/ressources-articles/base-empreinte-r-comprendre-et-utiliser-la-base-carbone-de-reference-pour-votre-entreprise) ;
  [hellocarbo.com, 2026-06-23](https://www.hellocarbo.com/blog/calculer/base-empreinte/)).
- **Méthode Bilan Carbone® V8** portée par l'**ABC** : référence francophone,
  téléchargeable après formation — mais **marque déposée** : revendiquer un
  « Bilan Carbone® » exige le respect du cahier des charges/licence ABC
  ([greenly.earth, 2026-06-23](https://greenly.earth/blog/secteurs/bilan-carbone-entreprise-logiciel)).
- **Plateforme Bilans GES ADEME** (`bilans-ges.ademe.fr`) : dépôt officiel +
  module de saisie guidée ([les-rencontres-ecologie-travail.fr, 2026-06-23](https://www.les-rencontres-ecologie-travail.fr/blog/bilan-carbone-obligatoire-entreprises-2026/)).
- **Nos Gestes Climat** (ADEME / beta.gouv, open source MIT, publicodes) :
  calculateur d'empreinte, mais **pour les particuliers**, pas les organisations
  ([github.com/incubateur-ademe/nosgestesclimat, 2026-06-23](https://github.com/incubateur-ademe/nosgestesclimat)).

### Produits commerciaux

- **Greenly** : à partir de ~1 800 €/an, automatisation via intégrations
  comptables ([logiciel-bilan-carbone.fr](https://www.logiciel-bilan-carbone.fr/)).
- **Carbo / HelloCarbo** : à partir de ~1 200 €/an
  ([logiciel-bilan-carbone.fr](https://www.logiciel-bilan-carbone.fr/)).
- **Sami** (désormais lié à SGS) : à partir de ~5 000 €/an, certifié ABC, ISO
  14064-1 ([vsmexperts.fr](https://vsmexperts.fr/blog/guide-rse/5-outils-automatiser-bilan-carbone-pme)).
- **Sweep** : ~15 000–50 000 €/an, ETI/grands groupes, fondé à Paris en 2020
  ([greenly.earth](https://greenly.earth/blog/secteurs/bilan-carbone-entreprise-logiciel)).
- **Traace, Toovalu, Plan A, Aktio (~1 990 €/an), Orki (~1 440 €/an),
  Take[air] (~150 €/mois), Climeet (~150 €/mois), Normative, Persefoni,
  Watershed, Carbometrix, Sphera…** ([logiciel-bilan-carbone.fr](https://www.logiciel-bilan-carbone.fr/) ;
  [d-carbonize.eu, 2026-06-23](https://d-carbonize.eu/fr/blog/logiciel-bilan-carbone-comparatif/)).

### Open source / bricolage

- **Nos Gestes Climat** + écosystème **Publicodes** (langage de calcul ouvert,
  modèles de bilan carbone) ([github, 2026-06-23](https://github.com/betagouv/publicodes/blob/master/README.md)) — base technique réutilisable mais orientée particuliers.

**Où est l'espace libre ?** Pas sur le bilan GES d'entreprise générique (saturé).
Créneau éventuel et étroit : **l'angle territorial pré-rempli** — utiliser les
consommations d'énergie locales ouvertes (ORE/SDES) pour produire un
**pré-diagnostic carbone automatique d'un territoire/EPCI** sans collecte
manuelle, là où les outils existants exigent une saisie lourde. Mais ce créneau
recoupe les observatoires régionaux (AASQA, observatoires énergie-climat,
*existence à vérifier au cas par cas*).

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0017-empreinte-carbone-territoire` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `esg-csrd` — ESG & reporting extra-financier

Fichier : [`catalogue-saas/vendors/esg-csrd.json`](../../catalogue-saas/vendors/esg-csrd.json) (19 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `watershed` | Watershed | US | partial | partial |
| `persefoni` | Persefoni | US | partial | partial |
| `normative` | Normative | US | partial | partial |
| `greenly` | Greenly | FR | partial | partial |
| `workiva-esg` | Workiva | US | partial | partial |
| `sweep` | Sweep | FR | strong | partial |
| `plan-a` | Plan A | DE | partial | partial |
| `ecovadis` | EcoVadis | FR | strong | partial |
| `carbonfact` | Carbonfact | FR | strong | partial |
| `carbonmaps` | Carbon Maps | FR | strong | partial |
| `ibm-envizi` | IBM Envizi | US | partial | partial |
| `apiday` | Apiday | FR | strong | partial |
| … | _+7 autres_ | | | |

#### Segment `environmental-data-fr` — Environnement & risques FR

Fichier : [`catalogue-saas/vendors/environmental-data-fr.json`](../../catalogue-saas/vendors/environmental-data-fr.json) (20 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `atmo-france` | Atmo France | FR | strong | verified |
| `hub-eau` | Hub'Eau | FR | strong | verified |
| `inpn` | INPN (OFB) | FR | strong | partial |
| `brgm-infoterre` | BRGM InfoTerre | FR | strong | partial |
| `georisques-api` | Géorisques | FR | strong | verified |
| `uk-environment-agency` | UK Environment Agency — Open Data | GB | absent | partial |
| `eea-europe` | European Environment Agency | EU | partial | partial |
| `copernicus-land` | Copernicus Land Monitoring | EU | partial | partial |
| `us-epa-envirofacts` | US EPA Envirofacts | US | absent | partial |
| `sandre` | Sandre | FR | strong | partial |
| `drias-climat` | DRIAS — Futurs climatiques | FR | strong | partial |
| `basol` | BASOL — Sites et sols pollués | FR | strong | partial |
| … | _+8 autres_ | | | |

#### Segment `energy-buildings-fr` — Bâtiments & énergie FR

Fichier : [`catalogue-saas/vendors/energy-buildings-fr.json`](../../catalogue-saas/vendors/energy-buildings-fr.json) (22 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `openmeti` | OpenMéti | FR | strong | verified |
| `ademe-data` | ADEME — data services | FR | strong | verified |
| `effy-pro` | Effy Pro | FR | strong | verified |
| `hub-anah` | Anah — Hub rénovation | FR | strong | partial |
| `heero` | Heero | FR | strong | verified |
| `uk-epc-register` | UK EPC Register | GB | absent | partial |
| `building-performance-database` | Building Performance Database (US DOE) | US | absent | partial |
| `dena-gebaeudedaten` | dena — Gebäudedaten (DE) | DE | unknown | partial |
| `gridx-energy` | gridX | DE | partial | partial |
| `hellowatt` | Hello Watt | FR | strong | verified |
| `enoptea` | Enoptea | FR | strong | verified |
| `cantine-energetique` | Cantine Énergétique | FR | strong | verified |
| … | _+10 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment esg-csrd
```

<!-- catalogue-saas-end -->
## 5. Différenciation
Faible et **peu défendable en l'état**. Le seed (facteurs ADEME ouverts +
énergie locale) est exactement ce que font déjà tous les acteurs : les facteurs
sont publics, la méthode est publique, et les concurrents sont nombreux et
financés. Un calculateur de plus n'a aucun fossé. Le seul angle potentiellement
différenciant — **le pré-remplissage automatique à partir des open data
territoriales** (zéro saisie pour un premier ordre de grandeur) — reste copiable
et marche surtout pour les collectivités, segment déjà servi. **Copiable en un
week-end** pour la partie facteurs.

## 6. Faisabilité & fiabilité technique
Bon respect du principe **RAG(sens) / SQL(chiffres)** : les facteurs d'émission
sont des données structurées → stockage tabulaire (DuckDB) et **calcul
arithmétique traçable** (activité × facteur), jamais inventé par un LLM. Le LLM ne
sert qu'à **expliquer** (choix du bon facteur, périmètre scopes 1/2/3,
vulgarisation). Risque d'hallucination faible **par construction** côté calcul.
**Réserve** : la fiabilité du résultat dépend surtout de la **qualité des données
d'activité saisies par le client** (hors open data), ce qui n'est pas maîtrisable
par l'architecture. La techno de base existe déjà en open source (Publicodes).

## 7. Monétisation / impact
- **Monétisation** : SaaS B2B, modèle prouvé (1 200–50 000 €/an selon taille),
  mais **capture de revenu difficile** vu la saturation et la présence d'acteurs
  financés + d'outils gratuits.
- **Impact** : fort sur le papier (accélérer la transition bas-carbone des PME et
  territoires), surtout via le **pré-diagnostic gratuit** abaissant le coût
  d'entrée pour les petites structures.

## 8. Risques
- **Marché saturé** d'acteurs financés (Greenly, Sami, Sweep, Traace, Plan A,
  Watershed…) → acquisition coûteuse, différenciation faible.
- **Marque « Bilan Carbone® » déposée (ABC)** : on ne peut pas s'en revendiquer
  sans licence/cahier des charges → risque juridique/branding.
- **Licence ecoinvent** : une partie des facteurs de la Base Empreinte n'est
  **pas librement réutilisable** → périmètre de données ouvertes plus étroit qu'annoncé.
- **Crédibilité / greenwashing** : un bilan « automatique » mal calibré peut
  être contesté ; les bilans réglementaires exigent rigueur méthodologique.
- **Dépendance aux données d'activité du client** : la valeur perçue tient à la
  collecte, partie la plus pénible et non automatisable par l'open data.

## 9. Effort MVP
Périmètre minimal crédible :
1. Ingestion Base Carbone (API ADEME / CSV) → DuckDB de facteurs traçables.
2. **Pré-diagnostic territorial automatique** : à partir des consommations
   élec/gaz ORE par EPCI/commune × facteurs ADEME → ordre de grandeur GES sans
   saisie (l'angle qui exploite vraiment l'open data).
3. Saisie guidée scopes 1/2 pour une organisation + export.
4. Traçabilité : chaque chiffre = donnée d'activité + facteur + version + date.

Le noyau calcul est rapide (Publicodes/DuckDB existent) ; mais atteindre un
produit **crédible et différenciant** face aux incumbents est un chantier lourd
(scope 3, import comptable, conformité, reporting).

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | 3 | 3 | 9 |
| C3 | Disponibilité & fiabilité données | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | 2 | 2 | 4 |
| C5 | Différenciation défendable | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 3 | 6 |
| C8 | Maîtrise des risques | 2 | 2 | 4 |
| C9 | Monétisation / impact | 2 | 3 | 6 |
| | **Total** | | | **59 / 105** |

**Score /100** : 59 / 105 × 100 = **56**

Justification note par note :
- **C1 = 3** : douleur réelle (obligation BEGES + amendes) mais la cible PME du
  seed n'est pas légalement obligée — demande induite et tiède pour le segment visé.
- **C2 = 3** : payeurs et budgets existent (1,5–50 k€/an sourcés), mais le segment
  qui paie bien est le plus concurrentiel et le segment PME paie peu.
- **C3 = 3** : facteurs ADEME ouverts/propres/SQL-ables, mais l'open data ne couvre
  pas les données d'activité (le cœur du bilan) et l'ecoinvent n'est pas réutilisable.
- **C4 = 2** : marché saturé d'acteurs financés + outils publics gratuits ; il ne
  reste qu'un mince créneau territorial pré-rempli.
- **C5 = 2** : facteurs et méthode publics, dizaines de concurrents → quasi aucun
  fossé, copiable.
- **C6 = 4** : séparation RAG(sens)/SQL(chiffres) nette et calcul traçable, brique
  open source dispo ; bridé par la qualité des données d'activité client.
- **C7 = 3** : noyau calcul rapide à monter, mais un MVP différenciant face aux
  incumbents reste lourd.
- **C8 = 2** : saturation, marque Bilan Carbone® déposée, licence ecoinvent,
  risque crédibilité — plusieurs risques réels non triviaux.
- **C9 = 3** : modèle de revenu prouvé et impact climat fort, mais capture de
  revenu difficile dans un marché encombré.

## 11. Verdict & décision
🔁 **À retravailler** (56/100, dans la bande 55–69). Aucun critère **éliminatoire**
ne s'applique (l'activité est légale et les données existent), donc on ne l'écarte
pas formellement — mais le score est **proche du seuil bas** et le diagnostic est
sévère : **le seed tel quel est non différenciant dans l'un des marchés
climat-tech les plus saturés** (Greenly, Sami, Sweep, Traace… + outils ADEME
gratuits). Les facteurs et la méthode étant publics, il n'y a aucun fossé.

**Condition pour la sauver (le « retravail »)** : abandonner le bilan GES
d'entreprise générique et se concentrer sur le **seul angle qui exploite vraiment
l'open data** — un **pré-diagnostic carbone territorial automatique** (à partir
des consommations énergétiques ORE/SDES par EPCI/commune × facteurs ADEME),
**sans collecte manuelle**, comme produit d'appel pour collectivités/EPCI, en se
positionnant en complément (et non en concurrent frontal) des plateformes
existantes. Sans ce recentrage, l'idée bascule de fait vers ❌ Écartée.

**Prochaine étape concrète** : faire un POC du pré-diagnostic territorial — croiser
le dataset ORE « consommation annuelle élec/gaz par EPCI » avec les facteurs Base
Carbone, sur 2–3 EPCI, pour vérifier qu'on produit un ordre de grandeur GES
crédible et traçable **sans saisie**, puis confronter ce livrable aux
observatoires régionaux existants pour mesurer le delta de valeur.

---

0017 | Empreinte carbone des territoires / PME | 🔁 À retravailler | 56/100 | Marché saturé, seed non différenciant, pivot territorial requis
