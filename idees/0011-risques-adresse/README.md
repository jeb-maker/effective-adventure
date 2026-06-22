# Diagnostic des risques par adresse

- **ID** : 0011
- **Statut** : 🔁 À retravailler
- **Score** : 60 / 100
- **Dernière mise à jour** : 2026-06-20
- **Pitch (1 phrase)** : Synthétiser à l'adresse/parcelle tous les risques (inondation,
  retrait‑gonflement des argiles, radon, sismicité, sites/sols pollués, ICPE…) à partir
  des données Géorisques, pour particuliers acheteurs, notaires, agents et assureurs.

---

## 1. Problème / douleur
Avant un achat immobilier, comprendre les risques d'un bien (inondation, RGA, radon,
sismicité, pollution des sols, voisinage industriel) est une vraie préoccupation, et le
phénomène monte : le retrait‑gonflement des argiles touche plus de 20 millions de
Français et a causé > 3,5 Md€ de dommages immobiliers en 2022 (chiffres du ministère,
consulté 2026-06-20 : https://www.notre-environnement.gouv.fr/actualites/breves/article/retrait-gonflement-des-argiles-une-application-pour-evaluer-les-risques).

**MAIS** la douleur « informationnelle » brute est déjà très largement adressée : l'État
propose **gratuitement** le service **Errial** qui pré‑remplit l'état des risques à partir
d'une adresse ou d'une parcelle (https://errial.georisques.gouv.fr , consulté 2026-06-20),
et c'est même devenu la **référence unique** réglementaire (annonces immobilières obligées
de renvoyer vers georisques.gouv.fr). Le besoin « synthétiser les risques d'une adresse »
est donc un besoin **réel mais déjà servi**. La douleur résiduelle est d'**interprétation**
(« qu'est-ce que ça signifie pour mon achat / mon prix / mon assurabilité ? »), pas
d'accès à la donnée.

## 2. Cible & qui paie
- **Particuliers acheteurs** : utilisateurs naturels, mais **mauvais payeurs** ici car
  l'équivalent officiel (Errial) et plusieurs services privés (risques-adresse.fr,
  scores ClimaScore) sont **gratuits**. Disposition à payer faible et déjà siphonnée.
- **Notaires / diagnostiqueurs / agents** : payeurs crédibles — ils achètent déjà des
  outils de génération de rapport Géorisques (ex. Notiplus, Risqeo à 24,90 €). Mais
  l'offre est **déjà occupée**.
- **Assureurs / banques** : vrais budgets, mais ils consomment plutôt des modèles de
  risque climatique prospectif (Callendar) ou intègrent l'API directement.

Utilisateur ≠ payeur dans le cas grand public, et le payeur pro est déjà équipé : double
handicap de monétisation.

## 3. Données sources
Toutes les sources clés sont publiques, gratuites, en **Licence Ouverte 2.0** et exposées
par **une API officielle unique** — ce qui est une force pour la faisabilité mais
**aussi ce qui sature le marché** (tout le monde a accès à la même chose).

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| API Géorisques (agrégateur + endpoints détaillés) | https://www.data.gouv.fr/dataservices/api-georisques · doc : https://www.georisques.gouv.fr/doc-api | Licence Ouverte 2.0 (CGU : https://www.georisques.gouv.fr/cgu) | API REST JSON, rapport PDF | continue (BRGM) | API v2 nécessite authentification (token Cerbère, valable 1 an) ; maille variable (commune vs parcelle) |
| Rapport de risque à l'adresse | `/api/v1/resultats_rapport_risque` (adresse ou lat/lon → rapport) | LO 2.0 | JSON/PDF | continue | statut réglementaire ponctuel, pas une analyse |
| Sismicité / Radon | `/api/v1/zonage_sismique` (zones 1‑5, décret 2010‑1255) · `/api/v1/radon` (classes 1‑3, ASNR ex‑IRSN) | LO 2.0 | JSON | réglementaire, stable | **maille communale**, pas parcellaire |
| Retrait‑gonflement argiles (RGA) | endpoint argiles de l'API Géorisques | LO 2.0 | JSON | continue (BRGM) | aléa cartographique, pas un diagnostic de sol |
| Sites/sols pollués (CASIAS ex‑BASIAS, SIS) | `/api/v1/ssp` | LO 2.0 | JSON | continue (BRGM / ministère) | buffer ~200 m, complétude hétérogène |
| ICPE / installations classées | `/api/v1/installations_classees` | LO 2.0 | JSON | mensuelle (préfectures) [indicatif] | liste nominale dans un rayon ; pertinence locale variable |
| Cavités / mouvements de terrain | `/api/v1/cavites` · `/api/v1/mvt` | LO 2.0 | JSON | continue (BRGM) | inventaire historique, non exhaustif |
| GASPAR (CatNat, PPR, PAPI, TIM, DICRIM) | `/api/v1/gaspar/*` · `/api/v1/ppr` | LO 2.0 | JSON | à chaque arrêté/approbation | maille communale (sauf zonage PPR) |
| Base Adresse Nationale (géocodage) | https://api-adresse.data.gouv.fr | LO 2.0 | API JSON | continue (IGN/DINUM) | précision d'appariement variable |

Référence d'inventaire des datasets sous‑jacents : cas d'usage ERRIAL sur data.gouv.fr
(PCI cadastre, BASIAS, sites/sols pollués, mouvements de terrain, TRI, PPRN…),
consulté 2026-06-20 : https://www.data.gouv.fr/pages/onboarding/errial

## 4. Existant / concurrence
**Verdict de saturation : SATURÉ.** L'existant couvre déjà le service public
réglementaire, le créneau grand‑public gratuit, le créneau payant enrichi, l'angle
assurance/climat **et** l'accès développeur en API. Le seed le pressentait : c'est confirmé.

**Service public / officiel (le concurrent décisif, gratuit) :**
- **Errial** (georisques.gouv.fr) — génère l'état des risques pré‑rempli par adresse/parcelle,
  PDF téléchargeable, devenu la référence réglementaire unique. Consulté 2026-06-20 :
  https://errial.georisques.gouv.fr et https://www.georisques.gouv.fr/information-des-acquereurs-et-locataires
- **API Géorisques** ouverte et gratuite (LO 2.0) — donne déjà la matière brute à l'adresse.
  Consulté 2026-06-20 : https://www.data.gouv.fr/dataservices/api-georisques

**Produits commerciaux grand public / enrichis (déjà nombreux) :**
- **Fonciris** — rapport 18 sections par adresse croisant Géorisques + DVF + ADEME + INSEE +
  cadastre ; 9,99 € le rapport, 14,99 €/mois, 79 €/mois pro (API). Consulté 2026-06-20 :
  https://fonciris.fr et https://fonciris.fr/risques-immobiliers
- **ClimaScore** — 5 notes A–F (dangers naturels, environnement, quartier, bâtiment,
  horizon 2050), gratuit + rapport 9,90 €. Consulté 2026-06-20 : https://climascore.fr
- **risques-adresse.fr** — rapport **gratuit** sur 18 risques officiels par adresse + alerte
  email, 14 endpoints Géorisques. **Porte déjà exactement le nom et le périmètre de cette
  idée.** Consulté 2026-06-20 : https://risques-adresse.fr et https://risques-adresse.fr/methodologie
- **Callendar** — risque climatique prospectif (submersion, RGA, incendie, canicule) à la
  parcelle, applications grand public gratuites + offre B2B banque/assurance/immo.
  Consulté 2026-06-20 : https://www.callendar.tech
- **Risqeo / Notiplus** — génération d'ERP/rapport Géorisques pour diagnostiqueurs et pros
  (Risqeo 24,90 € le document conforme + RCP). Consulté 2026-06-20 :
  https://risqeo.fr/diagnostic-erp-comprendre-faq.html et https://www.notiplus.com/outils/georisques

**Accès développeur / API tierces (le « back‑end » est aussi déjà packagé) :**
- **ATerraData** — API d'enrichissement avec module `risks` (Géorisques) par adresse, clé API.
  Consulté 2026-06-20 : https://aterradata.com/docs
- **Apify – Géorisques FR scraper** — un rapport risques structuré par adresse en masse à
  0,005 $/adresse. Consulté 2026-06-20 : https://apify.com/dltik/georisques-fr-scraper/api

**Où reste‑t‑il (un peu) d'espace ?** Pas sur la synthèse à l'adresse (saturée). Au mieux
sur du **B2B portefeuille** (scoring climatique prospectif à la parcelle pour assureurs/
prêteurs/bailleurs sociaux, en masse) — mais Callendar y est déjà installé. Le créneau libre
est marginal et difficile.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0011-risques-adresse` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-22 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `environmental-data-fr` — Environnement & risques FR

Fichier : [`catalogue-saas/vendors/environmental-data-fr.json`](../../catalogue-saas/vendors/environmental-data-fr.json) (9 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `atmo-france` | Atmo France | FR | strong | partial |
| `hub-eau` | Hub'Eau | FR | strong | partial |
| `inpn` | INPN (OFB) | FR | strong | partial |
| `brgm-infoterre` | BRGM InfoTerre | FR | strong | partial |
| `georisques-api` | Géorisques | FR | strong | partial |
| `uk-environment-agency` | UK Environment Agency — Open Data | GB | absent | partial |
| `eea-europe` | European Environment Agency | EU | partial | partial |
| `copernicus-land` | Copernicus Land Monitoring | EU | partial | partial |
| `us-epa-envirofacts` | US EPA Envirofacts | US | absent | partial |

#### Segment `geospatial-gis-fr` — Géospatial & carto FR

Fichier : [`catalogue-saas/vendors/geospatial-gis-fr.json`](../../catalogue-saas/vendors/geospatial-gis-fr.json) (9 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `geofoncier` | Géofoncier | FR | strong | partial |
| `alkante` | Alkante | FR | strong | partial |
| `ign-geoservices` | IGN Géoservices | FR | strong | partial |
| `cartelie` | Cartélie (IGN) | FR | strong | partial |
| `opendatasoft-geo` | Opendatasoft | FR | strong | partial |
| `ordnance-survey` | Ordnance Survey | GB | absent | partial |
| `esri-arcgis` | Esri ArcGIS | US | partial | partial |
| `mapbox` | Mapbox | US | partial | partial |
| `here-technologies` | HERE Technologies | NL | partial | partial |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment environmental-data-fr
```

<!-- catalogue-saas-end -->
## 5. Différenciation
Très faible et **non défendable**. La donnée est la même pour tous (API publique LO 2.0),
la couche d'agrégation est reproductible en un week‑end (Apify le vend à 0,005 $/adresse),
et le positionnement « synthèse des risques par adresse » est **déjà pris jusque dans le
nom** (risques-adresse.fr). Aucun avantage durable : ni donnée exclusive, ni effet réseau,
ni verrou. Toute différenciation (UX, contextualisation, croisement DVF/prix) est déjà
livrée par Fonciris/ClimaScore.

## 6. Faisabilité & fiabilité technique
Techniquement **facile et fiable** — c'est le paradoxe : ce qui rend l'idée saisissable la
rend aussi copiable. Architecture : géocodage BAN → appels API Géorisques (rapport agrégé +
endpoints détaillés) → normalisation des champs structurés → restitution.
Conforme au principe **RAG(sens)/SQL(chiffres)** : tous les **chiffres/classements**
(zone sismique 1‑5, classe radon 1‑3, nombre d'ICPE dans un rayon, arrêtés CatNat) sont des
**valeurs structurées renvoyées par l'API** — donc traçables, non hallucinées ; le LLM ne
sert qu'à **expliquer le sens** (« que signifie zone 3 ? », « pourquoi cette ICPE compte »).
Risque d'hallucination faible **par construction**. Limites : maille communale pour
plusieurs risques (radon, sismicité), buffers indicatifs, et la nécessité d'afficher
clairement « informatif, non opposable » (la valeur opposable reste l'Errial officiel).

## 7. Monétisation / impact
Faible. Le grand public ne paiera pas (Errial gratuit + risques-adresse.fr/ClimaScore
gratuits) ; le segment payant pro est déjà occupé à bas prix (9,90–24,90 €/rapport, API à
0,005 $/adresse). La pression sur les prix est forte et la matière première est gratuite,
donc peu de marge. Impact « public » réel mais déjà délivré par l'État (Errial) — un acteur
privé n'ajoute pas d'impact incrémental significatif.

## 8. Risques
- **Concurrence écrasante** (public gratuit + privés établis) : risque #1, structurel.
- **Responsabilité juridique** : si un acheteur s'appuie sur un rapport erroné/incomplet —
  d'où l'obligation d'afficher « informatif, ne remplace pas l'état des risques officiel ».
- **Dépendance à une API publique** unique (changements de schéma, authentification token,
  quotas) sur laquelle on n'a aucun contrôle.
- **Commoditisation** : la valeur captée tend vers zéro quand la donnée est ouverte et les
  agrégateurs pullulent.

## 9. Effort MVP
Faible en absolu (BAN + API Géorisques + une page de rapport ≈ buildable rapidement), mais
**c'est précisément le problème** : un MVP rapide ne crée aucun fossé face à des acteurs déjà
en production avec croisement DVF/DPE/prix. Un MVP qui aurait un sens devrait viser le seul
angle marginalement libre (B2B portefeuille / scoring climatique prospectif à la parcelle),
ce qui demande des modèles propres (type Callendar) et sort du périmètre « simple synthèse ».

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | 3 | 3 | 9 |
| C3 | Disponibilité & fiabilité données | 3 | 5 | 15 |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 |
| C5 | Différenciation défendable | 2 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 4 | 8 |
| C8 | Maîtrise des risques | 2 | 3 | 6 |
| C9 | Monétisation / impact | 2 | 2 | 4 |
| | **Total** | | | **63 / 105** |

**Score /100** : 63 / 105 × 100 = **60**

Justification note par note :
- **C1 = 3** : besoin réel et récurrent (achat immo, RGA en hausse), mais déjà servi
  gratuitement par Errial — la douleur d'accès est largement résolue.
- **C2 = 3** : des payeurs existent (notaires, diagnostiqueurs paient Notiplus/Risqeo), mais
  les particuliers ne paieront pas face au gratuit, et les pros sont déjà équipés.
- **C3 = 5** : données prêtes, propres, traçables, gratuites, LO 2.0, API officielle unique —
  c'est le point le plus fort, et il serait malhonnête de le sous‑noter.
- **C4 = 1** : saturation manuelle (Errial public + Fonciris + ClimaScore + risques-adresse.fr
  + Callendar + Risqeo + Notiplus + ATerraData + Apify) — cas d'école.
- **C5 = 1** : même donnée publique pour tous, copiable en un week‑end, positionnement déjà
  pris jusque dans le nom (risques-adresse.fr).
- **C6 = 4** : architecture simple, chiffres structurés issus de l'API (pas de RAG sur les
  nombres) → hallucination faible ; pénalisé seulement par la maille communale de certains risques.
- **C7 = 4** : MVP rapide à construire — mais cette facilité profite surtout aux concurrents.
- **C8 = 3** : risques juridiques (rapport non opposable) et de dépendance API gérables par
  des disclaimers, mais le risque concurrentiel reste majeur.
- **C9 = 2** : monétisation comprimée entre gratuit officiel et concurrents à < 25 €,
  matière première gratuite → marge faible.

## 11. Verdict & décision
🔁 **À retravailler — mais au bas de la fourchette, et de fait quasi écartée en l'état.**
Le score (60/100) place l'idée dans la bande « à retravailler », porté **uniquement** par
l'excellence des données (C3) et la faisabilité technique (C6). Mais ce sont aussi ces
atouts qui causent sa perte : la donnée est ouverte et identique pour tous, donc le produit
est **commoditisé et saturé** (C4 = C5 = 1), avec un concurrent **public et gratuit** (Errial)
qui est la référence réglementaire, et un homonyme privé gratuit (risques-adresse.fr) déjà
en ligne. Aucun critère strictement éliminatoire (la donnée existe, l'usage est légal), donc
on ne l'écarte pas d'office — mais le seul point faible « à lever » est le manque total
d'espace concurrentiel, ce qui n'est pas un détail mais le cœur du problème.

**Prochaine étape concrète** : ne PAS construire la « synthèse des risques par adresse »
(saturée). Si l'on veut sauver quelque chose, instruire **une seule hypothèse de
repositionnement B2B** : scoring climatique **prospectif** (horizon 2050) à la parcelle, en
**masse/portefeuille**, pour assureurs et prêteurs — et vérifier d'abord, par 3–5 entretiens,
si Callendar et consorts laissent un créneau réel. Sans créneau démontré, basculer en
❌ Écartée.

---

0011 | Diagnostic des risques par adresse | 🔁 À retravailler | 60/100 | Saturé par Errial public et concurrents privés
