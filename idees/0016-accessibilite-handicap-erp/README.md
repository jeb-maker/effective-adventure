# Accessibilité handicap des lieux (ERP)

- **ID** : 0016
- **Statut** : ❌ Écartée
- **Score** : 52 / 100
- **Dernière mise à jour** : 2026-06-20
- **Pitch (1 phrase)** : Exploiter les données d'accessibilité des ERP (acceslibre)
  pour aider les personnes handicapées à trouver des lieux accessibles et/ou
  aider commerces et collectivités à se mettre en conformité.

---

## 1. Problème / douleur
Le besoin est **réel et fort** : environ 12 millions de personnes sont concernées
par un handicap en France (~19 % de la population), et le manque d'information
fiable sur l'accessibilité d'un lieu **avant** de s'y rendre est un frein
quotidien majeur (source : Ville de Créteil / Jaccede, consulté 2026-06-20 —
https://www.ville-creteil.fr/jaccede-le-guide-de-laccessibilite). Côté offre, sur
~1,8 à 2 millions d'ERP, une large part n'est encore engagée dans aucune démarche
de mise en accessibilité (source : handicap.gouv.fr, consulté 2026-06-20 —
https://www.handicap.gouv.fr/vous-etes-dans-un-etablissement-recevant-du-public-erp-devenez-accessible).

**MAIS** : ce problème est précisément celui que l'État a choisi d'adresser via un
**service public numérique dédié** (acceslibre), lancé en 2021. La douleur est
donc forte mais **déjà prise en charge frontalement** par un acteur public
gratuit — ce qui déplace la question de « le problème existe-t-il ? » vers « reste-t-il
un créneau non couvert ? » (réponse en sections 4-5 : très peu).

## 2. Cible & qui paie
- **Utilisateurs (côté demande)** : personnes en situation de handicap, aidants,
  associations. → **Ne paient pas** : ils utilisent un service public gratuit
  (acceslibre) et des applis associatives gratuites (Jaccede). Pas de budget.
- **ERP / commerces (côté offre)** : pourraient payer pour de la mise en
  conformité, mais (a) la conformité réglementaire (registre public
  d'accessibilité, Ad'AP) **n'est pas** ce que décrivent les données acceslibre
  (déclaratif d'accessibilité ≠ diagnostic réglementaire), et (b) l'État finance
  déjà l'aide via un **Fonds territorial d'accessibilité de 300 M€ sur 5 ans**
  (source : préfecture Indre-et-Loire, dossier de presse 2024-08-28, consulté
  2026-06-20 —
  https://www.indre-et-loire.gouv.fr/contenu/telechargement/42678/299143/file/2024-08-28%20-%20DP%20-%20L'accessibilit%C3%A9%20des%20%C3%A9tablissements%20recevant%20du%20public.pdf).
- **Collectivités** : payeur plausible, mais déjà servies par des éditeurs B2B
  (Someware/Handimap, voir §4).

**Verdict cible** : utilisateur ≠ payeur, et aucun payeur n'est clairement non
servi. C'est le point faible majeur de l'idée.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| Accessibilité des ERP (acceslibre, jeu de données) | https://www.data.gouv.fr/datasets/accessibilite-des-etablissements-recevant-du-public-erp-pour-les-personnes-en-situation-de-handicap | Licence Ouverte 2.0 | CSV (2 fichiers) | Mise à jour quotidienne (dernière : 2026-06-20) | **Couverture partielle** (~30 % des ERP, voir ci-dessous) ; données **déclaratives** donc approximatives ; documentation des fichiers signalée manquante par data.gouv |
| API Accès libre | https://www.data.gouv.fr/dataservices/api-acces-libre · doc : https://acceslibre.beta.gouv.fr/api/docs/ | Licence Ouverte 2.0 | API REST/JSON (Swagger) | Continue | Pensée pour interroger / afficher, pas pour analytics massif ; endpoints `/api/erps`, `/api/accessibilite`, `/api/activites` |
| Schéma de données (standard CNIG) | https://schema.data.gouv.fr/MTES-MCT/acceslibre-schema/ · https://github.com/MTES-MCT/acceslibre-schema | Licence Ouverte | JSON/Excel (Data Package) | Versionné | Standardisé et propre → facilite la réutilisation |
| Acceslibre Mobilités (voirie/transports) | https://mtes-mct.github.io/alm-docs/ · code : https://gitlab.com/yukaimaps | Licence Ouverte | NeTEx accessibilité | — | Périmètre voirie/transport, distinct des ERP |

**Couverture / complétude (chiffré)** : la page d'accueil d'acceslibre annonce
**627 887 lieux recensés** (consulté 2026-06-20 — https://acceslibre.beta.gouv.fr/),
contre 425 000 en mars 2024 (source : handicap.fr, consulté 2026-06-20 —
https://informations.handicap.fr/a-accessibilite-pmr-425-000-lieux-recenses-sur-acceslibre-36533.php).
Rapporté aux ~1,8 M d'ERP visés, cela représente **de l'ordre de 30 %** de
couverture, et le caractère **déclaratif** (cases oui/non/inconnu, non audité)
limite la fiabilité — ce que reconnaît la presse spécialisée (handicap.fr, même
lien). → Données **ouvertes, propres et traçables, mais incomplètes**.

## 4. Existant / concurrence
> Règle : chaque affirmation = lien + date (tous consultés 2026-06-20).

**Service public officiel — le besoin central est déjà couvert.**
- **acceslibre** (beta.gouv.fr) : service public numérique de référence,
  recherche de lieux accessibles filtrée par handicap, contribution
  collaborative, gratuit, +10 000 contributeurs, 627 887 lieux —
  https://acceslibre.beta.gouv.fr/ . L'objectif affiché est de **diffuser ces
  données chez les grands sites tiers** (service-public.fr, allocine.fr…), donc
  l'État pousse activement la réutilisation sans laisser de vide produit
  rémunérateur (dossier de presse Indre-et-Loire, lien §2).

**Applis grand public concurrentes (gratuites, installées).**
- **Jaccede** (association) : guide collaboratif d'accessibilité des lieux,
  web + iOS + Android, gratuit ; « + de 100 000 lieux répertoriés » selon une
  page municipale (https://www.ville-creteil.fr/jaccede-le-guide-de-laccessibilite),
  chiffre exact **à vérifier** (une autre source coopérative évoque ~73 218 lieux
  dans le monde — https://groupe.up.coop/fr/notre-actualite/politique-rh/jaccede-le-collaboratif-au-service-du-handicap).
- **Wheelmap** : carte collaborative mondiale d'accessibilité (référence
  internationale) — cité par https://www.homeexchange.fr/blog/applis-voyage-handicap/ .
- **Google Maps** : attribut « entrée accessible en fauteuil roulant » et
  paramètres d'accessibilité intégrés (même source homeexchange).

**Acteurs B2B / collectivités (créneau payeur déjà occupé).**
- **Someware / Handimap** : calculateur d'itinéraires piétons PMR pour
  collectivités, intégré au réseau STAR (Rennes), HITinéraire (Lorient), Hérault
  Tourisme — https://www.someware.fr/nos-outils-numeriques/handimap/ . Sait déjà
  exploiter diagnostics d'accessibilité + données temps réel.
- **Acceslibre Mobilités (ALM)** : outil public State-financé pour la collecte
  voirie/transports, export NeTEx — https://mtes-mct.github.io/alm-docs/ .

**Niches mobilité spécialisées.**
- **Andilien** (Transilien) : accessibilité des gares IDF, état des ascenseurs en
  temps réel — https://www.transilien.com/fr/page-deplacements/application-andilien .
- **StreetCo / StreetNav** : GPS PMR évitant les obstacles trottoir —
  https://www.science-et-vie.com/societe/streetnav-debarque-a-paris-un-gps-revolutionnaire-pour-les-deplacements-des-personnes-a-mobilite-reduite-170780.html .
- **Very Important Parking** : places PMR (~800 000 lieux annoncés, à vérifier) —
  https://www.homeexchange.fr/blog/applis-voyage-handicap/ .

**Open source / réutilisations.**
- Client open source de l'API : **Foohx/acceslibre-client** (MIT) —
  https://github.com/Foohx/acceslibre-client/ .
- Sur data.gouv, le jeu de données affiche « Réutilisations et API : 4 », dont la
  réutilisation principale est… **acceslibre lui-même** (page dataset, consultée
  2026-06-20). Très peu de réutilisations tierces, ce qui en dit long sur
  l'appétence commerciale autour de cette donnée.

**Verdict de saturation : SATURÉ côté produit grand public** (service public
officiel + Jaccede + Wheelmap + Google Maps), **partiel à occupé côté B2B
collectivités** (Someware/Handimap). L'unique espace réellement non couvert
serait la **mise en conformité réglementaire** des ERP — mais ce créneau **n'est
pas alimenté par les données acceslibre** (déclaratif ≠ diagnostic réglementaire),
donc il ne valide pas la seed.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0016-accessibilite-handicap-erp` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-22 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `accessibility-compliance` — Accessibilité numérique

Fichier : [`catalogue-saas/vendors/accessibility-compliance.json`](../../catalogue-saas/vendors/accessibility-compliance.json) (5 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `accessibility-checker` | Accessibility Checker | unknown | unknown | partial |
| `deque-axe` | Deque axe DevTools | US | partial | partial |
| `userway` | UserWay | unknown | unknown | partial |
| `acceslibre` | Accès Libé (data.gouv.fr) | FR | strong | verified |
| `level-access` | Level Access | US | partial | partial |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment accessibility-compliance
```

<!-- catalogue-saas-end -->
## 5. Différenciation
Quasi inexistante sur la seed telle quelle. Refaire « trouver un lieu accessible »,
c'est **reconstruire le service public officiel** (acceslibre) avec une donnée
moins complète que la sienne — copiable en un week-end et déjà fait, mieux, par
l'État. La seule différenciation crédible (conformité/diagnostic ERP, ou
intelligence territoriale pour collectivités) (a) sort du périmètre des données
ouvertes acceslibre et (b) se heurte à Someware/Handimap déjà installés. Aucun
avantage défendable identifié.

## 6. Faisabilité & fiabilité technique
**Techniquement facile** : API documentée (Swagger), CSV quotidien, schéma CNIG,
client open source existant. Architecture saine possible : ingestion CSV → base
structurée (DuckDB/PostgreSQL) ; tous les **chiffres** (nombre de lieux,
critères d'accessibilité, taux de couverture par commune) viennent de **requêtes
SQL traçables** sur la donnée ; un LLM ne servirait qu'à **expliquer le sens**
(libellés de critères, synthèse d'une fiche) — conforme au principe
RAG(sens)/SQL(chiffres), risque d'hallucination faible. La faisabilité **n'est
pas** le problème de cette idée ; c'est la valeur/différenciation qui manque.

## 7. Monétisation / impact
- **Revenu** : très faible visibilité. Côté usagers, marché gratuit (service
  public + associatif). Côté ERP, la conformité n'est pas vendable à partir de
  cette donnée. Côté collectivités, concurrence installée + financement public
  qui tire les prix vers zéro.
- **Impact** : l'impact social potentiel est réel mais **déjà capté** par
  acceslibre ; un énième front-end n'apporterait qu'un impact marginal, et
  fragmenterait une donnée que l'État cherche justement à centraliser.

## 8. Risques
- **Redondance avec un service public gratuit** (acceslibre) : risque
  quasi-éliminatoire — difficile de justifier l'existence du produit.
- **Donnée incomplète et déclarative** : afficher « accessible » à tort engage la
  **responsabilité** vis-à-vis d'un public vulnérable.
- **Pas de payeur identifié** : risque économique structurel.
- **Concurrents installés** (Jaccede, Someware, Google Maps) sur les rares
  segments à valeur.

## 9. Effort MVP
Faible techniquement (la donnée et l'API sont prêtes), mais **l'effort n'est pas
le verrou** : même un MVP parfait se heurterait à l'absence de créneau et de
payeur. Un MVP honnête ne ferait que dupliquer acceslibre — donc inutile en
l'état. Un éventuel pivot (audit de couverture territoriale pour collectivités,
tableau de bord de complétude par commune) demanderait à requalifier entièrement
l'idée et à croiser d'autres sources (BPE/SIRENE pour le dénominateur ERP).

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 |
| C5 | Différenciation défendable | 2 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 4 | 8 |
| C8 | Maîtrise des risques | 2 | 2 | 4 |
| C9 | Monétisation / impact | 2 | 2 | 4 |
| | **Total** | | | **55 / 105** |

**Score /100** : 55 / 105 × 100 = **52**

Justification des notes (une phrase chacune) :
- **C1 = 4** : douleur réelle et large (12 M de personnes), mais déjà adressée par un service public, donc pas 5.
- **C2 = 2** : les usagers ne paient pas et aucun payeur (ERP/collectivité) n'est laissé non servi par l'offre publique/B2B existante.
- **C3 = 3** : données ouvertes, propres, quotidiennes et au standard CNIG, mais couverture ~30 % et nature déclarative qui plafonnent la fiabilité.
- **C4 = 1** : segment grand public saturé par le service officiel + Jaccede + Wheelmap + Google Maps.
- **C5 = 1** : refaire acceslibre est copiable et déjà fait par l'État ; aucune différenciation défendable trouvée.
- **C6 = 4** : API/CSV prêts et chiffres SQL-traçables (RAG limité au sens), mais pas 5 car la donnée elle-même est incomplète.
- **C7 = 4** : MVP techniquement rapide grâce à l'API et au client open source, mais sans intérêt produit.
- **C8 = 2** : redondance avec un service public gratuit + responsabilité sur donnée déclarative = risques élevés.
- **C9 = 2** : ni revenu crédible ni impact additionnel par rapport à l'existant public.

## 11. Verdict & décision
❌ **Écartée.** Score 52/100 (< 55), et surtout **critère quasi-éliminatoire de
redondance** : la seed reproduit le service public officiel **acceslibre**
(beta.gouv.fr), qui couvre déjà la recherche de lieux accessibles, est gratuit,
mieux doté en données que ne le serait un réutilisateur, et pousse activement la
diffusion de sa donnée chez les tiers. Le segment grand public est saturé
(acceslibre + Jaccede + Wheelmap + Google Maps) et le segment B2B est occupé
(Someware/Handimap), tandis que le seul créneau réellement libre — la **mise en
conformité réglementaire des ERP** — n'est **pas alimenté** par les données
ouvertes acceslibre (déclaratif ≠ diagnostic). Aucun payeur non servi n'est
identifié.

**Prochaine étape concrète** : ne pas prototyper en l'état. Si l'on veut conserver
le thème handicap, requalifier vers un angle **non couvert et chiffrable** —
p. ex. un **observatoire de la couverture/complétude d'acceslibre par commune**
(dénominateur ERP via BPE/SIRENE, numérateur via acceslibre) à destination des
collectivités et de la Délégation ministérielle à l'accessibilité — et le traiter
comme une **nouvelle idée distincte**, avec vérification d'un payeur public réel
avant toute analyse approfondie.

---

0016 | Accessibilité handicap des lieux (ERP) | ❌ Écartée | 52/100 | Redondant avec service public acceslibre, sans payeur
