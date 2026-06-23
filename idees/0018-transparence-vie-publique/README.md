# Transparence de la vie publique

- **ID** : 0018
- **Statut** : ❌ Écartée
- **Score** : 46 / 100
- **Dernière mise à jour** : 2026-06-23
- **Pitch (1 phrase)** : Croiser les données ouvertes de la HATVP (déclarations
  d'intérêts, répertoire des représentants d'intérêts) et le financement de la
  vie politique pour montrer « qui influence quoi » et signaler les conflits
  d'intérêts potentiels, à destination des journalistes, ONG, chercheurs et
  citoyens.

---

## 1. Problème / douleur
Comprendre les liens d'intérêts des responsables publics et l'influence du
lobbying est laborieux : l'information existe (HATVP, CNCCFP) mais éclatée entre
plusieurs portails, dans des formats hétérogènes, sans croisement automatique
avec les entreprises, les marchés publics ou le financement des partis. Le
besoin de recoupement est réel pour une cible étroite (journalistes
d'investigation, ONG anti-corruption, chercheurs). Mais c'est un besoin
**récurrent et tiède plutôt qu'une douleur aiguë** : la cible principale est
militante/éditoriale, pas en souffrance opérationnelle quotidienne, et plusieurs
outils gratuits répondent déjà au gros du besoin (voir §4).

## 2. Cible & qui paie
- **Journalistes / data-journalistes** : usage réel, mais budget outils faible
  et fort réflexe « build maison » ou outils gratuits.
- **ONG / collectifs transparence** (Transparency International, Regards
  Citoyens) : ce sont des **producteurs** d'outils concurrents, pas des clients.
- **Chercheurs (sciences politiques)** : budget quasi nul, usage ponctuel.
- **Citoyens** : ne paient pas.
- **Vrais payeurs du secteur = affaires publiques / lobbying** (entreprises,
  cabinets), mais ils achètent de la **veille législative** (Contexte, Legiwatch,
  Dixit), produit différent de la transparence-redevabilité visée ici.

Problème structurel : **utilisateur ≠ payeur**, et les payeurs solvables veulent
un autre produit (veille d'influence offensive) que celui décrit par le seed
(redevabilité citoyenne). Mélanger les deux est inconfortable éthiquement.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| Contenu des déclarations (intérêts + patrimoine publiables) | https://www.data.gouv.fr/datasets/contenu-des-declarations-de-situation-patrimoniale-et-dinterets-publiees-des-responsables-publics | Licence Ouverte / Etalab | XML + liste CSV | Au fil de l'eau ; MAJ data.gouv 2026-06-03 | Saisie déclarative manuelle (qualité hétérogène) ; **patrimoine des parlementaires NON diffusable** (consultable seulement en préfecture, cf. §8) ; pas d'API officielle |
| Répertoire des représentants d'intérêts (AGORA) | https://www.hatvp.fr/open-data-repertoire/ | Licence Ouverte / Etalab | JSON (par lobby + global) + tables CSV | Mise à jour **chaque nuit** | Déclaratif ; seules l'année en cours + 5 années précédentes publiques ; périmètre du lobbying déclaré incomplet |
| Répertoire — fichiers en vues séparées (data.gouv) | https://www.data.gouv.fr/datasets/repertoire-des-representants-dinterets-fichiers-en-vues-separees | Licence Ouverte / Open Licence | CSV (8 fichiers) | MAJ data.gouv 2026-06-13 | Archives ; mêmes données en vues multiples |
| Comptes des partis et groupements politiques (CNCCFP) | https://www.data.gouv.fr/datasets/comptes-des-partis-et-groupements-politiques | Licence Ouverte (fr-lo) | CSV | Annuelle | Postes comptables agrégés ; certains comptes en francs CFP ; pas de détail donateurs |
| Comptes de campagne (CNCCFP) | https://www.data.gouv.fr/organizations/commission-nationale-des-comptes-de-campagne-et-des-financements-politiques-cnccfp/datasets | Licence Ouverte | CSV | Par scrutin | Granularité variable ; pas d'identité des donateurs |
| Code source répertoire (AGORA) | https://gitlab.com/hatvp-open/agora | (dépôt public) | Code | — | Outil de gestion, pas un produit d'analyse |
| **RNE** (répertoire national des élus) | https://www.data.gouv.fr/datasets/repertoire-national-des-elus-1 | LO 2.0 | CSV (12 mandats) | MàJ **9 juin 2026** (vérifié 2026-06-21) | Trimestriel ; matching nominatif avec HATVP = risque faux positifs |
| **RNA** (associations) | https://www.data.gouv.fr/datasets/repertoire-national-des-associations | LO 2.0 | CSV départementaux | MàJ **31 mai 2026** | Alsace-Moselle exclue ; RNA ≠ SIREN systématique |
| **DECP** (marchés attribués) | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | LO 2.0 | Parquet/CSV | ~quotidienne | Déjà croisé par VigiCité ; montant ≠ dépense réelle |
| **Subventions SCDL** | Schéma https://schema.data.gouv.fr/scdl/subventions/ | LO 2.0 | CSV par collectivité | Hétérogène (jeux MàJ juin 2026 sur certains dépts.) | **Pas de consolidation nationale** ; obligation > 23 k€ |

> [`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements envisagés

| Croisement | Question | Risque / limite |
|---|---|---|
| HATVP × RNE × DECP | Élu déclarant un intérêt × marchés sur son territoire | **Diffamation** si matching automatique non qualifié ; VigiCité le fait déjà |
| RNA × subventions SCDL | Association bénéficiaire × subventions versées | SQL traçable si SIRET/RNA présent ; couverture SCDL faible |
| DECP × subventions × SIRENE | Entreprise titulaire de marchés ET bénéficiaire de subventions | Transparence « qui touche quoi » — voir [0027](../0027-transparence-subventions-marches/) |
| Lobbying AGORA × DECP (CPV) | Secteurs lobbyés vs marchés attribués | Interprétation déclarative ; pas de lien causal |

**Recyclage possible** (cf. §11) : brique **API requêtable** DECP × subventions × RNA,
strictement limitée aux champs diffusables — pas un nouveau portail citoyen.

> Toutes URL consultées le 2026-06-20 sauf sources complémentaires (2026-06-21).
> La structure XML des déclarations est documentée par la HATVP
> (`opendata-structure.xlsx`, cité dans la notice open data — à vérifier que le
> lien historique est encore actif).

## 4. Existant / concurrence

> Cartographie B (consultée 2026-06-23).

**Verdict de saturation : saturé sur le créneau citoyen/transparence.** Les
outils gratuits portés par les ONG couvrent déjà précisément le seed.

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **HATVP — open data** | https://www.hatvp.fr/open-data/ | Déclarations d'intérêts, répertoire lobbyistes |
| **data.gouv.fr — HATVP** | https://www.data.gouv.fr/datasets/haute-autorite-pour-la-transparence-de-la-vie-publique | Jeux déclarations et répertoire |
| **Registre des représentants d'intérêts** | https://www.hatvp.fr/le-registre-des-representants-dinterets/ | Lobbying réglementé |
| **data.economie.gouv.fr — DECP** | https://data.economie.gouv.fr/ | Marchés publics (croisement adjacent) |

### Réutilisations data.gouv

| Acteur | URL | Rôle |
|---|---|---|
| **VigiCité** | https://www.data.gouv.fr/reuses/vigicite | Croisement HATVP + marchés + élus |
| **Poligraph** | https://www.data.gouv.fr/reuses/poligraph | Parse HATVP CSV/XML, déclarations lisibles |
| **NosDéputés.fr** | https://www.data.gouv.fr/reuses/nosdeputes-fr | Activité parlementaire open data |

### Produits civiques / ONG

- **Integrity Watch France — Transparency International France** (datavisualisation
  des relations responsables publics / secteur privé, à partir des déclarations
  d'intérêts HATVP + affiliations politiques + déclarations des lobbyistes du
  répertoire ; filtres par parti, déclarations rectificatives). Fait l'essentiel
  du « qui influence quoi » visé. — https://transparency-france.org/2023/05/16/public-prive-integrity-watch-loutil-de-datavisualisation-des-relations-des-responsables-publics-avec-le-secteur-prive-vient-detre-mis-a-jour/ (consulté 2026-06-23)
- **VigiCité** : croise **HATVP + marchés publics + registre des lobbys** pour
  6 763 élus, score de transparence /100, ~2,29 M de relations détectées,
  croisements « élu dirigeant d'entité privée avec marchés dans son territoire »,
  droit de réponse intégré. **C'est quasi exactement le produit du seed, déjà
  en ligne et gratuit.** — https://vigicite.org/ (consulté 2026-06-23)
- **Poligraph** : parse les fichiers open data HATVP (CSV/XML) pour rendre les
  déclarations lisibles/comparables (4 181 déclarations, 1 318 élus,
  portefeuilles, participations, transparence par parti, sync quotidienne).
  — https://poligraph.fr/declarations-et-patrimoine (consulté 2026-06-23)
- **Regards Citoyens / NosDéputés.fr & NosSénateurs.fr** : observatoire de
  l'activité parlementaire, code AGPL, données ODbL + API (XML/JSON/CSV). Acteur
  historique de la transparence parlementaire (site en refonte post-2024).
  — https://www.nosdeputes.fr/ , https://github.com/regardscitoyens/nosdeputes.fr/ (consulté 2026-06-23)

### Marché payant adjacent (veille affaires publiques)

- **Contexte** (sur devis) — https://about.contexte.com/offres ;
  **Legiwatch** (Solo ~450 €/mois, Équipe ~380 €/siège/mois, Illimité ~1 480 €/mois
  avec API) — https://www.legiwatch.fr/tarifs/ ; **Dixit** —
  https://www.dixitplatform.com/fr (tous consultés 2026-06-23). Ils couvrent la
  veille législative/influence, pas la redevabilité citoyenne.

**Où serait l'espace libre ?** Très étroit : éventuellement une couche
d'**API/jeu de données propre et requêtable** (puisque la HATVP n'expose pas
d'API officielle) ou un croisement systématique HATVP × financement CNCCFP ×
marchés publics mieux qualifié que VigiCité. Mais c'est une optimisation de
l'existant, pas un créneau vierge.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0018-transparence-vie-publique` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `electoral-data-fr` — Données électorales FR

Fichier : [`catalogue-saas/vendors/electoral-data-fr.json`](../../catalogue-saas/vendors/electoral-data-fr.json) (18 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `data-gouv-elections` | data.gouv.fr — élections | FR | strong | partial |
| `registre-perma` | Registre des représentants d'intérêts (ref transparence) | FR | strong | partial |
| `contexte` | Contexte | FR | strong | partial |
| `regards-citoyens` | Regards Citoyens | FR | strong | partial |
| `poligma` | Poligma | FR | strong | partial |
| `uk-electoral-commission` | UK Electoral Commission — Open Data | GB | absent | partial |
| `mit-election-lab` | MIT Election Data and Science Lab | US | absent | partial |
| `elections-europe` | European Parliament — Elections data | EU | partial | partial |
| `ballotpedia-data` | Ballotpedia | US | absent | partial |
| `ballotage-datagere` | Ballotage (Datagère) | FR | strong | partial |
| `qomon` | Qomon | FR | strong | partial |
| `politicae` | Politiciae DATA | FR | strong | partial |
| … | _+6 autres_ | | | |

#### Segment `civic-tech-fr` — Civic tech France

Fichier : [`catalogue-saas/vendors/civic-tech-fr.json`](../../catalogue-saas/vendors/civic-tech-fr.json) (19 entrées)

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
| `civiliz` | Civiliz | FR | strong | partial |
| `neocity` | Neocity | FR | strong | partial |
| … | _+7 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment electoral-data-fr
```

<!-- catalogue-saas-end -->
## 5. Différenciation
Faible et peu défendable. Tout ce que propose le seed (croisement intérêts ×
lobbying × marchés, score d'élu, « qui influence quoi ») est **déjà livré
gratuitement** par VigiCité, Integrity Watch et Poligraph, à partir des mêmes
sources open data. Aucune barrière : la donnée est publique et la valeur ajoutée
(parsing + matching) est reproductible en quelques semaines. Un différenciateur
crédible (API requêtable, qualité de matching supérieure) serait imitable et ne
suffit pas à fonder un avantage durable.

## 6. Faisabilité & fiabilité technique
- **Conforme au principe RAG(sens)/SQL(chiffres) si bien conçu** : montants
  (patrimoine publiable, comptes de partis, financements), volumes et
  croisements doivent venir de requêtes structurées (XML/CSV → base tabulaire →
  SQL). Le LLM ne sert qu'à expliquer le sens (libellés de déclaration, notions
  juridiques), jamais à produire un chiffre.
- **Risque technique réel = le matching**, pas le calcul. Relier un élu à une
  entreprise, à un marché public ou à un lobby repose sur du rapprochement
  nominatif/SIREN bruité. Un faux positif n'est pas une erreur anodine ici :
  il devient une **accusation potentiellement diffamatoire** (cf. §8). VigiCité
  l'admet implicitement avec son « droit de réponse » et son filtrage du bruit.
- Données déclaratives et saisies à la main : la fiabilité « chiffre traçable »
  est limitée par la qualité à la source, pas par l'architecture.

## 7. Monétisation / impact
- **Revenu : faible.** La cible qui utilise (journalistes, ONG, citoyens) ne paie
  pas ou peu ; la cible qui paie (affaires publiques) veut un autre produit.
- **Impact : réel mais déjà capté** par des acteurs institutionnels/associatifs
  (Transparency, Regards Citoyens) mieux légitimes et financés par dons/subventions.
  Un nouvel entrant apporterait un impact marginal.
- Pas de modèle économique soutenable identifié sans pivoter vers la veille
  d'influence payante — ce qui dénature l'idée.

## 8. Risques
- **🔴 Risque juridique éliminatoire (patrimoine).** Publier/divulguer tout ou
  partie des déclarations de **situation patrimoniale** hors cas légaux est une
  **infraction pénale** (art. 226-1 code pénal via art. 26 loi 2013-907 ;
  art. LO 135-2 code électoral : **45 000 € d'amende**) ; le patrimoine des
  parlementaires n'est consultable qu'en préfecture, jamais en ligne. — https://www.senat.fr/questions/base/2013/qSEQ131109158.html , https://www.legifrance.gouv.fr/loda/id/JORFTEXT000028056315 (consultés 2026-06-20). Le seed cite explicitement « déclarations de patrimoine » : c'est un piège.
- **🔴 Diffamation.** Présenter des « conflits d'intérêts potentiels » ou un score
  accusatoire sans qualification rigoureuse expose à des poursuites ; les
  croisements automatiques produisent des faux positifs.
- **🟠 RGPD.** Croiser et profiler des personnes nommées (données d'intérêts =
  données personnelles, parfois sensibles : appartenance politique) impose une
  base légale, une minimisation et un encadrement strict, malgré la licence
  ouverte. La réutilisation des déclarations d'intérêts est elle-même encadrée
  par les conditions du CRPA (art. L.321-1 et s.), pas en open bar.
- **🟠 Concurrence gratuite et légitime** : difficile d'exister face à des ONG
  reconnues offrant le même service sans contrainte de revenu.

## 9. Effort MVP
Modéré côté technique mais lourd côté conformité : (1) ingestion XML/CSV/JSON
HATVP + CSV CNCCFP → base tabulaire ; (2) matching élu↔entreprise↔marché (SIREN)
avec garde-fous anti-faux-positifs ; (3) **revue juridique obligatoire** (exclure
le patrimoine, cadrer la formulation « conflit potentiel », droit de réponse,
analyse RGPD/DPIA). Le coût n'est pas le code : c'est le risque juridique et le
fait d'arriver après des outils gratuits déjà établis.

## 10. Scoring

> **Scoring ajusté après revue critique du 2026-06-23** (voir [`revue.md`](revue.md)).
> Notes abaissées : C4 (2→1), C5 (2→1). Score 50 → **46** ; verdict inchangé
> (❌ Écartée, point éliminatoire patrimoine maintenu). Notes initiales en colonne dédiée.

| # | Critère | Poids | Note initiale | Note (post-revue) | Pondéré |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | 3 | 2 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | 3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | 2 | 2 | 1 | 2 |
| C5 | Différenciation défendable | 2 | 2 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | 2 | 3 | 3 | 6 |
| C7 | Facilité du MVP | 2 | 3 | 3 | 6 |
| C8 | Maîtrise des risques | 2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | 2 | 2 | 2 | 4 |
| | **Total** | | | | **48 / 105** |

**Score /100** : 48 / 105 × 100 = **46**

Justification des notes (post-revue) :
- **C1 = 3** : besoin réel de recoupement mais tiède et porté par une niche
  militante/éditoriale, pas une douleur opérationnelle aiguë.
- **C2 = 2** : les utilisateurs ne paient pas et les seuls payeurs solvables
  (affaires publiques) veulent un produit différent.
- **C3 = 3** : données ouvertes, structurées et fraîches (MAJ nocturne/au fil de
  l'eau) mais déclaratives, sans API officielle et avec un pan (patrimoine)
  juridiquement hors-jeu.
- **C4 = 1** (ajusté) : le produit décrit **existe déjà à l'identique, gratuitement
  et en open source** (VigiCité AGPL — 6 763 élus, 2,29 M relations, OFGL inclus —
  + Integrity Watch + Poligraph + Regards Citoyens) → saturé, pas « en consolidation ».
- **C5 = 1** (ajusté) : aucune barrière ; croisement open data reproductible en
  semaines, et le code du concurrent dominant est **public (AGPL)** → moat nul.
- **C6 = 3** : architecture SQL/RAG saine pour les chiffres, mais le matching
  nominatif bruité est un point faible intrinsèque.
- **C7 = 3** : ingestion faisable, mais alourdie par la revue juridique et
  l'anti-faux-positifs indispensables.
- **C8 = 2** : risques diffamation/RGPD élevés et risque pénal sur le patrimoine,
  seulement partiellement maîtrisables.
- **C9 = 2** : revenu faible et impact déjà capté par des ONG plus légitimes.

## 11. Verdict & décision
❌ **Écartée.** Score de **46/100** après revue critique du 2026-06-23 (< 55 ;
recalcul C4 2→1, C5 2→1 — créneau entièrement servi par VigiCité **AGPL** et
consorts), confirmé par un **point éliminatoire** : le seed inclut explicitement
les déclarations de **patrimoine**,
dont la republication est une **infraction pénale** (45 000 € — art. LO 135-2 /
226-1), et l'angle « conflits d'intérêts potentiels » porte un risque de
diffamation et RGPD difficile à maîtriser. À cela s'ajoute un créneau
**saturé** par des outils gratuits et légitimes (VigiCité fait quasi exactement
le produit décrit, plus Integrity Watch et Poligraph) et une **absence de
payeur** : la cible utilisatrice ne paie pas, et les payeurs solvables relèvent
de la veille d'affaires publiques (Contexte, Legiwatch, Dixit), un autre métier.

**Prochaine étape concrète** : ne pas prototyper en l'état. Si l'on veut
recycler la donnée HATVP, pivoter vers un angle **non saturé et sans payeur
absent** — p. ex. une **brique « données HATVP/CNCCFP propres + API requêtable »
réutilisable** (puisque la HATVP n'expose pas d'API), strictement limitée aux
champs légalement diffusables (intérêts + répertoire lobbying, jamais le
patrimoine), à offrir comme socle technique plutôt que comme énième portail de
redevabilité citoyenne.

---

0018 | Transparence de la vie publique | ❌ Écartée | 46/100 | Saturé par ONG gratuites (VigiCité AGPL), payeur absent, risque pénal patrimoine ; revue 2026-06-23
