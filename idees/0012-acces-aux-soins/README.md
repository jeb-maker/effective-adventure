# Observatoire de l'accès aux soins (déserts médicaux)

- **ID** : 0012
- **Statut** : ❌ Écartée
- **Score** : 44 / 100
- **Dernière mise à jour** : 2026-06-20
- **Révision critique** : voir [`revue.md`](revue.md) — score abaissé de **57 à 44**
  (écartée) après audit adversarial (existant omis : Observatoire CNAM/Data ameli,
  Observatoire SKEMA-UniCA ; payeur et différenciation surévalués).
- **Pitch (1 phrase)** : Mesurer et cartographier l'accès aux soins (APL, démographie
  médicale, annuaire santé, temps d'accès) pour identifier les déserts médicaux,
  à destination des collectivités, ARS, citoyens et soignants en installation.

---

## 1. Problème / douleur
Les déserts médicaux sont une douleur réelle, aiguë et politiquement saillante :
selon l'État, « près de 87 % du territoire national est classé en situation de
fragilité médicale » et 151 intercommunalités sont classées « zones rouges »
(~2–2,5 M habitants) (source data.gouv, consultée 2026-06-20 :
https://www.data.gouv.fr/reuses/carte-des-deserts-medicaux-en-france-le-nouveau-pacte-gouvernemental ).
La DREES documente une dégradation continue de l'accessibilité aux généralistes
(APL moyen 3,3 consultations/an/habitant en 2022 contre 3,8 en 2015 — source
DREES consultée 2026-06-20 :
https://drees.solidarites-sante.gouv.fr/communique-de-presse-jeux-de-donnees/communique-de-presse/accessibilite-aux-soins-de-premier ).

**Mais attention** : la douleur « ne pas savoir où sont les déserts » est
**déjà largement traitée** (cf. §4). Le besoin résiduel n'est pas *mesurer*
l'accès (c'est fait), mais éventuellement *agir* (attirer/installer un médecin),
là où les outils existants s'arrêtent souvent au diagnostic.

## 2. Cible & qui paie
- **ARS** : produisent **elles-mêmes** l'outil de référence (CartoSanté/Atlasanté,
  cf. §4) — payeur improbable pour un doublon.
- **Collectivités** (attirer des médecins) : disposent déjà de CartoSanté et de
  l'accompagnement ARS gratuitement ; budget « attractivité médicale » réel mais
  fléché vers des aides à l'installation, pas vers un nouvel outil cartographique.
- **Citoyens** : ne paient pas.
- **Soignants en installation** : cible des outils gratuits Rézone + C@rtoSanté +
  appli Shiny DREES.

Constat sceptique : **utilisateur ≠ payeur**, et surtout les payeurs potentiels
(ARS, collectivités) ont déjà l'outil gratuit et faisant autorité. Aucun payeur
solvable nommé pour la version « observatoire/cartographie ». Un éventuel revenu
ne peut venir que d'un service *au-delà* du diagnostic (matching installation,
conseil), non démontré ici.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| APL (accessibilité potentielle localisée), DREES | https://www.data.gouv.fr/datasets/laccessibilite-potentielle-localisee-apl | Licence Ouverte 2.0 | CSV/XLSX (communal) | Annuelle (millésimes 2015→2023) ; métadonnées data.gouv signalent « fréquence de mise à jour non respectée » | 5 professions de 1er recours (MG, IDE, sages-femmes, kiné, dentistes) ; pas spécialistes ; décalage ~2 ans ; année 2020 exclue (biais Covid) |
| Code de production APL (reproductible) | https://gitlab.com/DREES_code/public/outils/production-apl | Ouvert | Code | Maj irrégulière | Recalcul exige SNIIR-AM (non public) ; on consomme donc le résultat, pas le calcul |
| Annuaire Santé (RPPS), ANS | https://annuaire.sante.fr/ — extraction https://service.annuaire.sante.fr/annuaire-sante-webservices/V300/services/extraction/PS_LibreAcces | Données publiques RPPS (arrêté 18/04/2017) | CSV (zip, UTF-8) / API FHIR | Quotidienne (API FHIR) | Données nominatives de PS → RGPD à cadrer si réexposition ; champ « libre accès » limité |
| API FHIR Annuaire Santé | https://www.data.gouv.fr/dataservices/api-fhir-annuaire-sante | Données publiques | API REST FHIR R4 (JSON) | Quotidienne | Pensée requête unitaire, pas analyse de masse |
| FINESS (établissements sanitaires/médico-sociaux) | https://www.data.gouv.fr/datasets/finess-extraction-du-fichier-des-etablissements | Licence Ouverte | CSV | Mensuelle | Refonte FINESS annoncée été 2026 (flux actuel arrêté) — **à surveiller** |
| Metric (distancier inter-communes), Insee | https://www.insee.fr/fr/information/2410173 *(à vérifier l'URL exacte de diffusion)* | Données publiques Insee | Tables temps de trajet | Périodique | Temps voiture mairie→mairie ; pas transports en commun ni temps réel ; déjà intégré dans l'APL |
| Population municipale / structure par âge, Insee | https://www.insee.fr/ (recensement) | Licence Ouverte | CSV | Annuelle | Déjà intégrée dans l'APL (pondération par âge) |

Les indicateurs clés (APL, comptes de PS, temps d'accès) sont **structurés,
communaux et traçables** → exploitables en SQL. C'est le point fort de l'idée.

## 4. Existant / concurrence
**Verdict de saturation : SATURÉ** (par des acteurs publics gratuits faisant
autorité), avec un mince créneau libre sur le passage du *diagnostic* à *l'action*.

Services publics / officiels :
- **C@rtoSanté / CartoSanté (réseau des ARS, Atlasanté, techno Géoclip)** — outil
  cartographique de référence, **300+ indicateurs**, 8 professions libérales,
  échelles commune→région, portraits de territoire et études de marché pour
  l'installation. C'est exactement le périmètre du seed.
  https://www.data.gouv.fr/fr/datasets/cartosante/ et https://cartosante.atlasante.fr/
  (consultés 2026-06-20). Cibles explicites : candidats à l'installation **et élus
  locaux** (https://www.ars.sante.fr/crtosante-ou-sinstaller-en-liberal-en-un-clic ).
- **Rézone (Assurance Maladie)** — cartographie nationale (toutes régions),
  démographie médicale + zonages + **simulateur d'éligibilité aux aides**
  (CAIM, Coscom, Cotram, CSTM), sans création de compte.
  https://datalogue.iledefrance.ars.sante.fr/catalogue/rezone et
  https://www.cmvmediforce.fr/publications/par-themes/gestion-developpement-activite/medecins-un-nouvel-outil-daide-a-linstallation/
  (consultés 2026-06-20). Couvre la cible « soignant en installation » + aides.
- **Appli Shiny APL + jeux de données DREES** — visualisation et téléchargement
  officiels de l'APL. https://drees.shinyapps.io/carto-apl/ et
  https://data.drees.solidarites-sante.gouv.fr/explore/dataset/530_l-accessibilite-potentielle-localisee-apl/
  (consultés 2026-06-20).
- **Carte « zones rouges » de l'État (pacte déserts médicaux 2025)** — cartographie
  officielle des 151 intercommunalités prioritaires.
  https://www.data.gouv.fr/reuses/carte-des-deserts-medicaux-en-france-le-nouveau-pacte-gouvernemental
  (consulté 2026-06-20).

Réutilisations data.gouv.fr (le créneau « observatoire » est déjà tenté) :
- **Santé & Territoires — diagnostic interactif d'accès aux MG** : croise APL MG ×
  vieillissement (% 65+) sur ~35 000 communes, alertes + leviers d'action
  (renforts mobiles, incitations, transport à la demande). Très proche du seed.
  https://www.data.gouv.fr/reuses/sante-territoires-diagnostic-interactif-de-lacces-aux-medecins-generalistes
  (consulté 2026-06-20).
- **Santé et territoire** (projet étudiant BUT MMI) : carte interactive accès aux
  soins × pauvreté × vulnérabilité.
  https://www.data.gouv.fr/reuses/sante-et-territoire (consulté 2026-06-20).

Produits commerciaux / open source : pas de produit commercial dominant identifié
sur ce créneau précis (le champ est occupé par des outils publics gratuits) —
*(constat de l'analyste, recherche non exhaustive, à approfondir)*. Le code APL
de la DREES est lui-même open source (GitLab ci-dessus).

**Où est l'espace libre ?** Pas dans la mesure/carto (saturée). Éventuellement
dans : (a) l'**agrégation multi-sources orientée action** (matching « commune en
tension ↔ médecin en recherche », suivi d'un plan d'attractivité), (b) les
**spécialistes** et délais réels (les outils publics couvrent surtout le 1er
recours), (c) une **API/data-product** propre et requêtable par les éditeurs.
Tous restent à valider commercialement.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0012-acces-aux-soins` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-22 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `public-health-territory-fr` — Santé territoriale FR

Fichier : [`catalogue-saas/vendors/public-health-territory-fr.json`](../../catalogue-saas/vendors/public-health-territory-fr.json) (9 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `ameli-open-data` | Assurance Maladie — open data | FR | strong | partial |
| `santepubliquefrance` | Santé publique France — data | FR | strong | partial |
| `keldoc` | KelDoc | FR | strong | partial |
| `doctolib` | Doctolib | FR | strong | partial |
| `drees` | DREES | FR | strong | partial |
| `nhs-digital-open-data` | NHS Digital — Open Data | GB | absent | partial |
| `cdc-places` | CDC PLACES | US | absent | partial |
| `who-health-observatory` | WHO Global Health Observatory | CH | unknown | partial |
| `healthdata-gov` | HealthData.gov (US) | US | absent | partial |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment public-health-territory-fr
```

<!-- catalogue-saas-end -->
## 5. Différenciation
Faible et peu défendable face au seed. CartoSanté agrège déjà 300+ indicateurs et
Rézone fait déjà la jonction démographie ↔ aides à l'installation, gratuitement et
avec l'autorité de l'institution. Reproduire « une carte des déserts » est
**copiable en un week-end** et déjà copié (cf. réutilisations §4). Un angle
défendable n'apparaît qu'en sortant du diagnostic (action/matching/API), non
prouvé et hors du périmètre du seed tel que formulé.

## 6. Faisabilité & fiabilité technique
Techniquement sain : APL, comptes de PS (RPPS), FINESS et temps d'accès (Metric)
sont des données **structurées et communales** → entrepôt SQL (ex. DuckDB),
agrégations et classements 100 % traçables (dataset + millésime + requête).
Respect du principe **RAG(sens)/SQL(chiffres)** : le LLM ne sert qu'à expliquer
les définitions (qu'est-ce que l'APL, méthodologie, zonages), **jamais** à
produire un chiffre. Risque d'hallucination faible par construction. Réserves :
RGPD sur la réexposition des données nominatives RPPS, et refonte FINESS été 2026.

## 7. Monétisation / impact
- **Revenu** : faible/incertain. Les payeurs naturels (ARS, collectivités) ont
  déjà l'outil gratuit ; vendre un doublon est très difficile. Un SaaS ne tient
  que sur un service au-delà du diagnostic (non démontré).
- **Impact** : potentiellement fort (sujet majeur), mais l'impact « rendre visible
  le désert » est déjà capté par les outils publics ; l'impact différentiel d'un
  nouvel observatoire est marginal.

## 8. Risques
- **Saturation par le gratuit faisant autorité** (risque principal, quasi
  rédhibitoire pour la monétisation).
- **RGPD / sensibilité** : réexposer des données nominatives de professionnels et
  qualifier des territoires de « déserts » (effet réputationnel sur une commune).
- **Mésinterprétation** : un classement « accès aux soins » mal cadré peut induire
  des décisions publiques erronées — d'où l'exigence de traçabilité.
- **Dépendance** : refonte FINESS 2026, fréquence APL irrégulière.
- Pas de risque sanitaire direct (données agrégées/publiques) → **pas de critère
  éliminatoire sanitaire** ici.

## 9. Effort MVP
Faible côté technique (données prêtes) mais **inutile en l'état** car il
reproduirait CartoSanté. MVP crédible seulement s'il vise un créneau non couvert :
1. Entrepôt SQL APL + RPPS + FINESS + Metric (commune/EPCI), traçabilité par
   millésime.
2. UN angle non couvert : p.ex. **matching installation** (communes en tension ↔
   profil soignant + aides éligibles agrégées) ou **API data-product** pour
   éditeurs.
3. Validation payeur AVANT de coder (entretiens ARS/collectivités/URPS).

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 |
| C5 | Différenciation défendable | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 3 | 6 |
| C8 | Maîtrise des risques | 2 | 3 | 6 |
| C9 | Monétisation / impact | 2 | 2 | 4 |
| | **Total** | | | **60 / 105** |

**Score /100** : 60 / 105 × 100 = **57**

Justification des notes (1 phrase chacune) :
- **C1 = 4** : douleur réelle, récurrente et politiquement majeure, mais le besoin
  *de mesure* est déjà comblé (donc pas 5).
- **C2 = 2** : les payeurs plausibles (ARS, collectivités) ont déjà l'outil gratuit
  et faisant autorité, aucun payeur net identifié pour le diagnostic.
- **C3 = 4** : données ouvertes, communales, traçables et SQL-compatibles, mais
  fréquence APL irrégulière et refonte FINESS 2026 (donc pas 5).
- **C4 = 1** : créneau saturé par CartoSanté, Rézone, l'appli DREES et plusieurs
  réutilisations data.gouv.
- **C5 = 2** : une carte des déserts est copiable en un week-end et déjà copiée ;
  pas 1 car un pivot « action/API » reste théoriquement défendable.
- **C6 = 4** : architecture SQL traçable conforme à RAG(sens)/SQL(chiffres), moins
  5 à cause des contraintes RGPD/FINESS.
- **C7 = 3** : MVP techniquement rapide (données prêtes) mais sans valeur tant
  qu'il duplique l'existant.
- **C8 = 3** : pas de risque sanitaire direct, mais RGPD (RPPS) et risque de
  mésinterprétation/réputation territoriale à maîtriser.
- **C9 = 2** : impact réel possible mais déjà capté par le public, et revenu très
  incertain face au gratuit.

## 11. Verdict & décision
🔁 **À retravailler (57/100).** Le score se situe juste dans la fourchette
55–69, mais il faut être lucide : **le seed tel que formulé (mesurer/cartographier
les déserts médicaux) est de fait écarté** — il est saturé par des acteurs publics
gratuits et faisant autorité (CartoSanté/Atlasanté, Rézone de l'Assurance Maladie,
appli Shiny + données APL de la DREES, carte « zones rouges » de l'État) et déjà
dupliqué par des réutilisations data.gouv. La donnée est excellente, mais
excellente donnée ≠ produit : il n'y a ni espace concurrentiel ni payeur pour un
énième observatoire. Aucun critère **éliminatoire** strict (pas de risque
sanitaire, données disponibles), donc on ne tombe pas en « Écartée », mais le seuil
n'est franchi que grâce à la qualité des données et à l'intensité du problème.

**Ce qui pourrait sauver l'idée** : pivoter du *diagnostic* vers *l'action* —
matching « territoire en tension ↔ soignant en installation + aides agrégées »,
couverture des **spécialistes/délais réels** (peu traités par le public), ou un
**data-product/API** propre pour éditeurs. Aucun n'est validé.

**Prochaine étape concrète** : 5–8 entretiens (ARS, collectivité avec budget
attractivité médicale, URPS, soignant en cours d'installation) pour vérifier
qu'un besoin **payant** existe *au-delà* de CartoSanté/Rézone. Sans payeur nommé
à l'issue, repasser l'idée en ❌ Écartée.

---

0012 | Observatoire de l'accès aux soins (déserts médicaux) | 🔁 À retravailler | 57/100 | Saturé par outils publics gratuits, pivoter vers l'action
