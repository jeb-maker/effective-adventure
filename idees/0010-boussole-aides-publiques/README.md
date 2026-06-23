# Boussole des aides et subventions publiques

- **ID** : 0010
- **Statut** : ❌ Écartée
- **Score** : 42 / 100
- **Dernière mise à jour** : 2026-06-20
- **Révision critique** : voir [`revue.md`](revue.md) — score abaissé de **55 à 42**
  (écartée) après audit adversarial (concurrents omis : Éclaireur Public,
  subvention360, simulateur DGE… ; pivot non vierge, recoupe 0001).
- **Pitch (1 phrase)** : Un assistant qui agrège les aides/subventions publiques (entreprises,
  associations, collectivités, particuliers) à partir des données ouvertes et répond
  « à quelles aides ai-je droit / qu'existe-t-il sur mon territoire ? ».

---

## 1. Problème / douleur
Le « maquis » des aides est un problème réel et reconnu : on recense des milliers de
dispositifs à des niveaux européen, national, régional, départemental et communal, sous
des formes variées (subvention, prêt, garantie, avance récupérable, exonération, crédit
d'impôt, accompagnement). Le service public Aides-territoires décrit lui-même ce besoin
comme « un véritable casse-tête » pour ~35 000 communes et ~1 260 EPCI
(https://beta.gouv.fr/startups/aides-territoires.html, consulté 2026-06-20). Conséquences :
non-recours, temps perdu, dépendance à des cabinets coûteux. La douleur est forte et
récurrente — **mais elle est déjà largement adressée** (voir §4), ce qui change la nature
du problème : ce n'est plus « personne ne le fait » mais « tout le monde le fait déjà ».

## 2. Cible & qui paie
Quatre publics aux logiques très différentes, ce qui dilue le positionnement :
- **Entreprises (TPE/PME)** : seul segment où le payeur est clairement identifié — un
  marché commercial existe (abonnements 49–199 €/an, voir §4). Utilisateur = payeur.
- **Associations** : budgets serrés ; outillées gratuitement par des services publics
  (Data.Subvention, Le Compte Asso). Faible propension à payer.
- **Collectivités** : ont un outil public dédié et gratuit (Aides-territoires). Payeur
  potentiel via ingénierie, mais l'offre gratuite est installée.
- **Particuliers** : ne paient pas ; servis par des simulateurs publics gratuits
  (mesdroitssociaux, 1jeune1solution).

→ Le seul segment solvable (entreprises) est aussi le plus saturé et partiellement
servi **gratuitement** par les banques (ex. MAPi distribué par LCL, §4).

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| API Aides-territoires (dispositifs collectivités) | https://www.data.gouv.fr/dataservices/api-aides-territoires | « Accès ouvert » indiqué ; licence précise **à vérifier** (vraisemblablement Licence Ouverte) | API REST | MàJ data.gouv 2024-11-07 ; alimentée par les porteurs | ~3 000 dispositifs, ~600 porteurs ; **recentrée sur les collectivités depuis mars 2026** ; saisie déclarative (trous de couverture) |
| Aides-entreprises.fr (DGE/ISM/CMA) | https://data.aides-entreprises.fr/documentation | « Accès libre et sans contrainte » annoncé ; libellé exact **à vérifier** | CSV / JSON / XML + API REST + webhooks | MàJ régulière déclarée | > 2 000 dispositifs ; périmètre **entreprises uniquement** ; contenu surtout textuel (objet, montants, bénéficiaires) |
| les-aides.fr (CCI, base Sémaphore) | https://les-aides.fr/api | CGU propres : **usage lucratif et démarchage interdits**, aspiration robot interdite, plafond ~720 req/jour | API | Veille CCI continue | ~6 000 aides ; **licence incompatible avec un produit commercial** (point bloquant) |
| Data.Subvention (DJEPVA / beta.gouv) | https://www.data.gouv.fr/dataservices/api-data-subvention | API **réservée aux agents publics** (État, collectivités, opérateurs) | API REST | MàJ quasi temps réel via API amont | Couvre 1,5 M assos (demandes + versements) mais **non ouverte au grand public ni au privé** |
| SCDL « Subventions » (conventions des collectivités) | https://schema.data.gouv.fr/scdl/subventions/2.1.1/ | Licence Ouverte 2.0 | CSV (schéma normé) | Dépôt sous 3 mois après convention (décret 2017-779) | Obligatoire seulement > 23 000 € et collectivités > 3 500 hab / 50 agents ; **conformité réelle faible et qualité hétérogène** |
| mesdroitssociaux.gouv.fr / OpenFisca | https://mes-aides.gouv.fr/ ; https://beta.gouv.fr/startups/mes-aides.html | Code AGPL-3.0 (OpenFisca) | Moteur de règles | Maintenu | Particuliers ; ~60 prestations (PNDS) ; **mes-aides.gouv.fr est fermé et redirige** vers PNDS et 1jeune1solution |

**Constat clé** : les données « dispositifs » sont essentiellement du **texte descriptif**
(objet, critères d'éligibilité rédigés) — donc du terrain RAG, peu propice au calcul fiable
de droits. Les rares données réellement chiffrées et structurées sont les **subventions
versées** (SCDL, Chorus via Data.Subvention), mais avec couverture/accès restreints.

## 4. Existant / concurrence
**Verdict de saturation : SATURÉ.** Chaque public visé a déjà au moins un service
officiel gratuit, et le segment payant (entreprises) compte plusieurs produits IA.

Services publics / officiels (gratuits) :
- **Aides-territoires** (collectivités) : guichet unique ~3 000 dispositifs, recherche
  territorialisée + alertes ; recentré sur les collectivités depuis mars 2026 —
  https://aides-territoires.beta.gouv.fr/ et https://beta.gouv.fr/startups/aides-territoires.html
  (consultés 2026-06-20).
- **aides-entreprises.fr** (DGE/ISM/CMA) : base de référence > 2 000 dispositifs,
  géolocalisée, + open data — https://entreprendre.service-public.gouv.fr/vosdroits/R18133
  et https://data.aides-entreprises.fr/documentation (consultés 2026-06-20).
- **les-aides.fr** (CCI/Sémaphore) : ~6 000 aides aux entreprises —
  https://les-aides.fr/api (consulté 2026-06-20).
- **mesdroitssociaux.gouv.fr** (~60 prestations) et **1jeune1solution.gouv.fr**
  (> 1 000 aides, < 30 ans) ; **mes-aides.gouv.fr** est fermé et redirige —
  https://mes-aides.gouv.fr/ (consulté 2026-06-20).
- **Data.Subvention** (assos, subventions versées, réservé agents) —
  https://datasubvention.beta.gouv.fr/ (consulté 2026-06-20).

Produits commerciaux (le créneau « assistant IA aides entreprises » est déjà occupé) :
- **MaSubventionPro** — analyse SIRET + site web, « > 10 000 dispositifs » ; 49 €HT ou
  189 €HT/an — https://masubventionpro.com/ (consulté 2026-06-20).
- **URBANCash** — détection IA (embeddings) « 400+ dispositifs FR & UE », rédaction de
  dossiers ; 199 €/an — https://urbancash.app/ (consulté 2026-06-20).
- **Reki** — copilot financement non-dilutif startups/PME tech, via MCP Claude ; 49 €/mois
  — https://www.reki.eu/mcp (consulté 2026-06-20).
- **MAPi** — > 11 000 aides, distribué via une banque (LCL) ; 6,75 €HT/mois ou commission
  au succès — https://www.entrepreneur.lcl.fr/services/mapi (consulté 2026-06-20).
- **Gus** — « > 6 000 aides », pré-diagnostic gratuit puis montage —
  https://gus.fr/ (consulté 2026-06-20).

Les chiffres de marché (« 2,3 Md€ d'aides non réclamées ») cités par ces acteurs sont
**à vérifier** (marketing).

**Espace libre éventuel** : pas du côté de « l'assistant qui répond à quelles aides ai-je
droit » (occupé sur les 4 publics). Le seul créneau moins mûr est l'**analyse de
transparence des subventions *versées*** (qui touche combien, à qui, où) à partir du SCDL
et de Chorus — angle « radar » chiffré et factuel, analogue à l'idée 0001 (commande
publique), plutôt qu'un énième agrégateur d'éligibilité.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0010-boussole-aides-publiques` — segments liés pour benchmark concurrence structuré.
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

#### Segment `civic-tech-fr` — Civic tech France

Fichier : [`catalogue-saas/vendors/civic-tech-fr.json`](../../catalogue-saas/vendors/civic-tech-fr.json) (10 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `decidim` | Decidim | ES | partial | partial |
| `cap-collectif` | Cap Collectif | FR | strong | partial |
| `make-org` | Make.org | FR | strong | partial |
| `open-source-politics` | Open Source Politics | FR | strong | partial |
| `respublica` | République & Canton de Genève — outils (ref civic) | unknown | partial | partial |
| `citizenlab` | CitizenLab | BE | partial | partial |
| `consul-project` | CONSUL Democracy | ES | partial | partial |
| `bang-the-table` | Bang the Table (EngagementHQ) | AU | absent | partial |
| `commonplace-uk` | Commonplace | GB | absent | partial |
| `polis-co` | Polis | US | absent | partial |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment territorial-analytics
```

<!-- catalogue-saas-end -->
## 5. Différenciation
Faible et peu défendable **dans la forme du seed**. Tous les acteurs puisent dans les
mêmes données ouvertes ; le « matching IA SIRET → dispositifs » est déjà banalisé
(embeddings, voire MCP Claude chez Reki/URBANCash). Aucun avantage durable : copiable en
quelques semaines, et les services publics gratuits plafonnent le consentement à payer. Une
différenciation crédible n'existe que si l'on **change d'objet** (transparence/analytics sur
subventions versées) plutôt que d'ajouter un agrégateur d'éligibilité de plus.

## 6. Faisabilité & fiabilité technique
Point critique. La promesse « à quelles aides ai-je droit » suppose d'évaluer des
**critères d'éligibilité rédigés en texte libre** : c'est intrinsèquement du RAG sur le
**sens**, donc à fort risque d'hallucination quand on l'utilise pour affirmer un droit ou
un montant. Or le principe imposé est : RAG pour le sens, **SQL/règles pour les chiffres**.
Côté particuliers, seul OpenFisca fournit un vrai moteur de règles fiable ; côté entreprises,
il n'existe pas d'équivalent — l'éligibilité resterait approximative. Les montants affichés
ne sont pas des nombres propres par bénéficiaire (sauf SCDL/Chorus, accès limité). →
**Fiabilité notée bas** : un assistant généraliste d'éligibilité reposerait majoritairement
sur du RAG, contraire au §3 de la méthode. Le seul socle réellement « SQL-fiable » est celui
des subventions versées (SCDL), qui sert un autre produit (transparence), pas l'assistant.

## 7. Monétisation / impact
- **Revenu** : segment entreprises seul solvable, mais saturé et tiré vers le bas
  (49–199 €/an, voire gratuit via banques). Marge et acquisition difficiles face à des
  acteurs installés et au gratuit public.
- **Impact** : réduire le non-recours est un impact réel, mais déjà porté par des services
  publics financés (ex. coût cumulé de Mes Aides ~1,25 M€ sur sa durée de vie —
  https://beta.gouv.fr/startups/mes-aides.html, consulté 2026-06-20). Difficile de faire
  mieux que l'État sur son propre terrain.

## 8. Risques
- **Saturation** (concurrence officielle + commerciale sur les 4 publics) — quasi certain.
- **Responsabilité** : annoncer une éligibilité/un montant erroné expose juridiquement et
  détruit la confiance (risque aggravé par la fiabilité RAG).
- **Licences** : les-aides.fr **interdit l'usage lucratif** ; Data.Subvention est réservé
  aux agents — deux des sources les plus riches sont inexploitables pour un produit
  commercial grand public.
- **Dépendance** : recentrage d'Aides-territoires sur les collectivités (mars 2026) montre
  que le périmètre des sources bouge sous nos pieds.

## 9. Effort MVP
Un agrégateur basique est rapide à partir de l'open data aides-entreprises.fr (CSV/JSON +
API). Mais atteindre une **fiabilité d'éligibilité** suffisante pour se différencier est un
chantier lourd et risqué (règles métier, maintenance, responsabilité). Un MVP « transparence
subventions versées » (ingestion SCDL → DuckDB → fiches bénéficiaire/financeur/territoire,
sur le modèle de 0001) serait à la fois plus crédible techniquement et moins encombré.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 |
| C2 | Cible solvable (qui paie) | 3 | 3 | 9 |
| C3 | Disponibilité & fiabilité données | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | 2 | 2 | 4 |
| C5 | Différenciation défendable | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | 2 | 2 | 4 |
| C7 | Facilité du MVP | 2 | 3 | 6 |
| C8 | Maîtrise des risques | 2 | 2 | 4 |
| C9 | Monétisation / impact | 2 | 3 | 6 |
| | **Total** | | | **58 / 105** |

**Score /100** : 58 / 105 × 100 = **55**

Justification des notes (une phrase chacune) :
- **C1 = 4** : douleur réelle, forte et récurrente (« maquis », non-recours), reconnue par
  les pouvoirs publics eux-mêmes.
- **C2 = 3** : un payeur existe (entreprises, marché à 49–199 €/an), mais les trois autres
  publics ne paient pas et le segment payant est partiellement servi gratuitement.
- **C3 = 3** : open data exploitable côté entreprises, mais sources clés bridées
  (les-aides interdit le commercial, Data.Subvention réservé aux agents) et dispositifs
  surtout textuels.
- **C4 = 2** : marché saturé (un service public par public + ≥ 5 produits IA commerciaux) ;
  pas 1 car le sous-angle « transparence des subventions versées » reste peu mûr.
- **C5 = 2** : mêmes données pour tous et matching IA déjà banalisé, donc copiable et sans
  moat dans la forme proposée.
- **C6 = 2** : l'éligibilité repose sur du RAG textuel à fort risque d'hallucination,
  contraire au principe SQL-pour-les-chiffres (sauf OpenFisca, limité aux particuliers).
- **C7 = 3** : un agrégateur minimal est rapide, mais la version réellement fiable et
  différenciante est un chantier lourd.
- **C8 = 2** : cumul saturation + responsabilité sur l'éligibilité + verrous de licence,
  risques sérieux et en partie non maîtrisables.
- **C9 = 3** : revenu possible mais marché encombré et concurrencé par le gratuit (public
  et bancaire), impact déjà capté par l'État.

## 11. Verdict & décision
🔁 **À retravailler** (score 55/100, à la limite basse de la fourchette 55–69). Le seed —
un assistant généraliste « à quelles aides ai-je droit » pour les 4 publics — est, en
l'état, **à écarter** : l'espace est saturé (Aides-territoires, aides-entreprises.fr,
les-aides.fr, mesdroitssociaux/1jeune1solution, Data.Subvention) et doublé d'au moins cinq
produits IA commerciaux ; surtout, sa promesse repose sur du RAG d'éligibilité peu fiable,
ce qui contrevient au principe anti-hallucination et crée un risque de responsabilité. Ce
**point de fiabilité est quasi éliminatoire** pour la version « calcule mes droits ».

L'idée n'est pas jetée pour autant : le **pivot défendable** est d'abandonner l'agrégateur
d'éligibilité au profit d'un **« radar des subventions versées »** — analytics de
transparence (qui reçoit quoi, où, de quel financeur) bâti sur des données *chiffrées et
structurées* (SCDL conventions de subvention, Chorus), sur le modèle validé de l'idée 0001.
On y retrouve un socle SQL-fiable, un créneau moins saturé et un angle transparence
crédible.

**Prochaine étape concrète** : qualifier la couverture/qualité réelle du SCDL « subventions »
sur data.gouv.fr (taux de conformité des collectivités, volumétrie, fraîcheur) pour décider
si un « radar des subventions versées » tient — et requalifier alors l'idée sous ce nouvel
angle plutôt que de prototyper l'assistant généraliste.

---

0010 | Boussole des aides et subventions publiques | 🔁 À retravailler | 55/100 | Assistant saturé ; pivoter vers radar subventions versées
