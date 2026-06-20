# Rapport de revue critique — Idée 0002 Observatoire de qualité des données publiques

**Réviseur** : agent red team indépendant  
**Date de revue** : 2026-06-20  
**Fiche auditée** : `idees/0002-observatoire-qualite-donnees/README.md` (score déclaré : 71/100, statut 🔁 À retravailler)  
**Méthode** : `docs/methode-analyse.md`, prompt `docs/prompts/03-revue-critique.md`

---

## Synthèse exécutive

L’analyse identifie un vrai problème (ressources mortes, données périmées, régressions de structure) et cite correctement plusieurs briques existantes (score métadonnées data.gouv.fr, Validata, modèle transport). En revanche, elle **sous-estime fortement l’existant opérationnel côté État** (notamment `udata-hydra`, validation schéma intégrée en 2025, feuille de route 2026) et **surestime l’espace produit libre (C4)** et la disponibilité des données (C3). Le positionnement « monitoring transversal orienté producteur » n’est pas un créneau vierge : c’est une **extension logique** de ce que fait déjà l’écosystème Etalab/OpenDataFrance, avec un risque d’internalisation **imminent et documenté**, pas hypothétique.

Le cœur technique (checks HTTP, parsing, comparaison de dates) est solide et peu exposé à l’hallucination LLM, mais l’affirmation « zéro hallucination possible » masque la difficulté des checks hors schéma déclaré et l’échelle du catalogue national.

---

## 1. Affirmations non sourcées

| Affirmation (fiche) | Problème | Verdict |
|---|---|---|
| « Les réutilisateurs perdent un temps fou » (§1) | Douleur plausible, **aucun chiffre ni étude** (enquête, tickets support, logs de téléchargement) | **À sourcer** ou reformuler en hypothèse |
| « obligation légale de publier » pour collectivités (§2) | Vrai en droit (LRN 2016) mais **sans lien ni date** dans la fiche | **À sourcer** (ex. cadre légal L.1411-1 C. des relations entre le public et l’administration) |
| « cible solvable » (§2) | Assertion commerciale sans preuve de budget alloué à la qualité (vs obligation de publication) | **À sourcer** (budget open data, marchés existants) |
| « Monétisation : B2G abonnement “gardez vos jeux verts” » (§7) | Modèle inventé, **aucun concurrent/payeur identifié**, pas d’entretien cité | **À sourcer** ou marquer comme spéculation |
| « Impact : fort » (§7) | Qualitatif, non mesuré | **À sourcer** ou nuancer |
| « rien au niveau “produit transversal” » (§4, pitch) | **Contredit par l’existant** (voir §4 ci-dessous et angles morts) | **À supprimer / reformuler** : le gap est produit **commercial tiers**, pas absence de capacité |
| « créneau produit libre » (§11) | Non démontré ; roadmap 2026 Etalab vise explicitement la qualité | **À supprimer** ou fortement nuancer |
| « Zéro hallucination possible » (§6) | Vrai pour checks binaires simples ; **faux pour dérive de structure sans schéma** (heuristiques) | **À reformuler** |
| « techniquement excellente » (§11) | Jugement global sans benchmark ni POC | **À sourcer** |
| Tableau §3 — lignes `schema.data.gouv.fr` et « Modèle transport » | Colonnes Licence / Format / Fraîcheur / Limites **vides ou « — »** : non conforme à la règle §2 méthode (limites connues obligatoires) | **À compléter** |
| Source `dawap.fr` pour champ `quality` API (§4) | Blog tiers utile mais **pas source officielle** ; la doc API officielle (`guides.data.gouv.fr/api-de-data.gouv.fr`) et l’endpoint `/datasets/{dataset}/resources/{rid}/check/` ne sont pas cités | **À sourcer** via doc officielle datée |

**Points correctement sourcés** (vérifiés 2026-06-20) :
- Score métadonnées data.gouv.fr : [guide qualité](https://guides.data.gouv.fr/guides/guide-qualite/ameliorer-la-qualite-dun-jeu-de-donnees-en-continu/ameliorer-le-score-de-qualite-des-metadonnees.md) — confirme critères métadonnées, phase expérimentale, ajout futur du schéma.
- Validata : [validata.fr](https://validata.fr/), API documentée — confirme validation à la demande, pas monitoring historisé transversal.
- Indicateurs transport : [doc transport.data.gouv.fr](https://doc.transport.data.gouv.fr/outils/outils-disponibles-sur-le-pan/indicateurs-de-qualite) — confirme disponibilité horaire, conformité/fraîcheur quotidiennes, historisation.

---

## 2. Sur-optimisme du scoring

| Critère | Note fiche | Note revue | Justification |
|---|---|---|---|
| **C1** Intensité du problème | 4 | **4** | Douleur réelle et récurrente ; pas de surenchère majeure. |
| **C2** Cible solvable (qui paie) | 2 | **2** | Déjà bas et cohérent : B2G lent, payeur non identifié, gratuité des outils publics. Pas de sur-optimisme ici. |
| **C3** Disponibilité & fiabilité des données | 5 | **4** | API catalogue et Validata existent, mais : `quality` = métadonnées ; schémas couvrent une **minorité** des jeux ; crawling massif = contraintes infra/rate limits ; **Hydra** fait déjà une partie du travail en interne ([github.com/datagouv/hydra](https://github.com/datagouv/hydra), consulté 2026-06-20). Données « prêtes » pour un MVP restreint, pas pour un observatoire national crédible. |
| **C4** Espace concurrentiel libre | 4 | **2** | **Surestimation majeure.** L’État dispose déjà de : crawler Hydra (dispo + détection de changements + analyse CSV), validation schéma intégrée sur data.gouv.fr (2025), endpoint de check ressource, roadmap 2026 « renforcer le score de qualité », modèle transport **avec notifications producteur** ([doc notifications](https://doc.transport.data.gouv.fr/administration-des-donnees/guide-de-publication/5-parametrage-du-compte-transport.data.gouv.fr), 2026-06-20). OpenDataFrance : Observatoire territoires (collecte auto mensuelle depuis 2025) + Validata en coopération Etalab. Le vide est **produit SaaS tiers payant**, pas absence de solution publique. |
| **C5** Différenciation défendable | 3 | **2** | Différenciation = « généraliser transport.data.gouv.fr » — **imitable en un sprint** par l’équipe datagouv qui possède déjà Hydra et le PAN transport comme spec. Risque d’internalisation explicitement reconnu mais sous-pondéré au scoring. |
| **C6** Faisabilité & fiabilité technique | 5 | **4** | Checks objectifs (HTTP 200, parse CSV, dates) = traçables sans LLM. Mais : dérive de colonnes **sans schéma déclaré** = heuristique fragile ; formats hétérogènes (PDF, WMS, API paginées) ; dépendance API Validata tierce ; échelle catalogue (~centaines de milliers de ressources) non chiffrée. Architecture RAG/SQL respectable si LLM limité au résumé, mais pas « 5 ». |
| **C7** Facilité du MVP | 3 | **2** | MVP décrit = crawl catalogue entier + historisation + dashboard org + Validata : **chantier lourd** pour une petite équipe. Un MVP honnête serait un **pilote thématique** (1 schéma, N orgs), non transversal jour 1. |
| **C8** Maîtrise des risques | 3 | **2** | Internalisation **probable à court terme** ([perspectives 2026 data.gouv.fr](https://www.data.gouv.fr/posts/quelles-sont-les-perspectives-de-data-gouv-fr-pour-2026-1), 2026-06-20). Coûts crawl continu, faux positifs (HEAD vs GET, cf. transport), dépendance Validata, concurrence gratuite État/OpenDataFrance — risques **non maîtrisés**. |
| **C9** Monétisation / impact | 3 | **3** | Impact écosystème réel si open source / B2G ; monétisation faible. Note médiane acceptable : fort impact **ou** revenu, pas les deux. |

---

## 3. Risque d’hallucination / RAG(sens) vs SQL(chiffres)

**Constat positif** : l’idée repose principalement sur des **faits vérifiables** (statut HTTP, timestamp, résultat Validata, comparaison date déclarée / observée). Le LLM n’est que optionnel pour prioriser/résumer — conforme au principe §3 de la méthode **si** le périmètre reste ainsi.

**Risques non traités dans la fiche** :

1. **Dérive de structure sans schéma** : comparer les colonnes d’un CSV à une version précédente est faisable en SQL/ETL, mais l’interprétation (« colonne métier disparue » vs renommage) peut nécessiter du sens — zone grise RAG/heuristique, pas « zéro hallucination ».
2. **Score agrégé « qualité organisation »** : agrégation multi-datasets = règles métier à figer ; un LLM qui « explique » les alertes doit rester sur métadonnées d’alerte (RAG sens), jamais sur les compteurs (SQL).
3. **Fraîcheur « annoncée vs réelle »** : traçable si `last_update` API + date fichier ; mais ressources moissonnées ou miroirs peuvent fausser la comparaison — besoin de traçabilité requête + date dans l’UI.
4. **Aucun chiffre dans la fiche** n’est inventé par un LLM (pas de taille de marché fabriquée) — point favorable.

**Verdict fiabilité** : architecture compatible RAG/SQL **pour le MVP décrit**, mais la note C6=5 et la phrase « zéro hallucination possible » sont **trop absolues**.

---

## 4. Angles morts (non mentionnés ou insuffisamment traités)

### Existant public / quasi-concurrent

| Acteur / outil | Ce qu’il fait déjà | Source (consulté 2026-06-20) |
|---|---|---|
| **udata-hydra** (Etalab) | Crawl async des ressources data.gouv.fr : dispo, type fichier, modifications, analyse CSV, checksum, API `/api/checks` | [github.com/datagouv/hydra](https://github.com/datagouv/hydra) |
| **data.gouv.fr 2025** | Publication + **validation automatique schéma** intégrée ; notifications améliorées | [Évolutions 2025](https://www.data.gouv.fr/posts/quelles-evolutions-de-la-plateforme-en-2025) |
| **data.gouv.fr 2026** | Renforcement explicite du score qualité, vision unifiée catalogue | [Perspectives 2026](https://www.data.gouv.fr/posts/quelles-sont-les-perspectives-de-data-gouv-fr-pour-2026-1) |
| **API check ressource** | `GET /datasets/{dataset}/resources/{rid}/check/` | [Référence API datasets](https://guides.data.gouv.fr/api-de-data.gouv.fr/reference/datasets.md) |
| **Observatoire open data des territoires (ODF)** | Indicateurs quanti/quali, collecte **automatique mensuelle** depuis 2025 sur data.gouv.fr | [opendatafrance.fr/presentation-de-lobservatoire](https://opendatafrance.fr/presentation-de-lobservatoire/) |
| **OpenDataFactory** | Suite Validata + DataClic + SCDL — même cible producteurs territoriaux | [opendatafrance.fr/projets/opendatafactory](https://opendatafrance.fr/projets/opendatafactory/) |
| **transport.data.gouv.fr** | Non seulement indicateurs, mais **notifications producteur** (expiration, validation, indispo 6h) | [Paramétrage notifications](https://doc.transport.data.gouv.fr/administration-des-donnees/guide-de-publication/5-parametrage-du-compte-transport.data.gouv.fr) |
| **Validata × transport** | API Validata en test d’intégration PAN transport | [validata.fr](https://validata.fr/) |

### Risques opérationnels / réglementaires

- **Coût infra** : crawl horaire/quotidien de tout le catalogue (bande passante, stockage historique, faux positifs) — non chiffré.
- **Limites techniques des checks** : HEAD vs GET (documenté transport), timeouts, CDN, auth — taux d’erreur non estimé.
- **Portails locaux hors data.gouv.fr** : Opendatasoft, ArcGIS Hub — une partie de l’open data territorial n’est pas dans le périmètre API catalogue.
- **Positionnement vs gratuit public** : difficile de vendre un abonnement B2G quand l’État et OpenDataFrance financent des outils similaires.
- **Dépendance Validata** : tiers coopératif mais pas SLA garanti pour un produit commercial.
- **Extensions CKAN** (`ckanext-deadoralive`, `ckanext-check-link`) : pertinent si cible = portails locaux mutualisés, non abordé.

### Concurrence implicite la plus dangereuse

**L’équipe datagouv elle-même** : elle a l’infra (Hydra), la donnée, la légitimité et une roadmap 2026 alignée. Un startup/associatif qui réplique le modèle transport sur tout le catalogue se place en **pré-produit gratuit pour l’administration**, pas en position de pricing.

---

## 5. Recalcul du score

### Tableau revue

| # | Critère | Poids | Note fiche | Pondéré fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 | 4 | 12 |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | 3 | 5 | 15 | 4 | 12 |
| C4 | Espace concurrentiel libre | 2 | 4 | 8 | 2 | 4 |
| C5 | Différenciation défendable | 2 | 3 | 6 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | 2 | 5 | 10 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 3 | 6 | 2 | 4 |
| C8 | Maîtrise des risques | 2 | 3 | 6 | 2 | 4 |
| C9 | Monétisation / impact | 2 | 3 | 6 | 3 | 6 |
| | **Total** | | | **75 / 105** | | **60 / 105** |

**Score /100 recalculé** : round(60 / 105 × 100) = **57** (vs **71** déclaré)

**Seuil méthode** : 55–69 = 🔁 À retravailler ; < 55 = ❌ Écartée

### Changement de verdict

| Élément | Fiche | Revue |
|---|---|---|
| Score /100 | 71 (zone ✅ Go) | **57** (zone 🔁 À retravailler basse) |
| Statut affiché | 🔁 À retravailler (override manuel sur C2) | 🔁 À retravailler, **tendance ❌ Écartée** si internalisation confirmée |
| Cohérence score ↔ statut | **Incohérente** (71 ≥ 70 mais statut non-Go) | **Cohérente** : score et statut convergent vers « pas prêt prototype » |

**Changement de décision : oui.** Le score ne soutient plus un Go technique ; le point bloquant « qui paie » est aggravé par un **espace produit beaucoup plus étroit** que décrit. À la marge du seuil 55, un facteur éliminatoire (internalisation probable par l’État d’ici 2026–2027) peut justifier **❌ Écartée** sans attendre un prototype.

---

## 6. Verdict de revue

**Verdict : à corriger**

L’analyse pose le bon problème et cite une partie de l’écosystème, mais elle **surestime le vide marché** et **sous-documente l’existant Etalab/Hydra**, ce qui gonfle C3, C4 et C6. La stratégie commerciale reste non validée (C2 déjà faible). L’idée a de la valeur en **contribution open source ciblée** (ex. couche d’alertes pour un schéma précis, ou extension Validata), moins en **produit transversal B2G autonome**.

### 3 actions prioritaires

1. **Cartographier l’existant avec preuves datées** : documenter Hydra, endpoints API check, roadmap 2026, ODT OpenDataFrance, et redéfinir le gap en une phrase falsifiable (« ce que datagouv ne fait *pas encore* publiquement pour les producteurs »).
2. **Trancher le positionnement avant tout code** : soit **OSS / subvention** (impact, pas revenu), soit **B2G niche** (1 verticale + 2 entretiens payeurs signés) — abandonner le scoring hybride 71/« à retravailler ».
3. **Réduire le MVP à un pilote non transversal** : 1 schéma référencé (ex. SCDL ou IRVE), ~50 organisations, checks objectifs + historique 90 jours ; mesurer faux positifs et coût crawl avant d’envisager « observatoire national ».

---

REVUE 0002 | à corriger | score recalculé 57/100 (vs 71) | changement de décision: oui
