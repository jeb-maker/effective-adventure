# Analyse électorale fine (bureau de vote)

- **ID** : 0014
- **Statut** : 🔁 À retravailler
- **Score** : 55 / 100
- **Dernière mise à jour** : 2026-06-20
- **Pitch (1 phrase)** : Exploiter les résultats électoraux au **bureau de vote**
  croisés avec la socio-démographie INSEE pour analyser participation,
  abstention, basculements et sociologie du vote — pour journalistes, partis,
  chercheurs et collectivités.

---

## 1. Problème / douleur
Comprendre **pourquoi** un territoire vote comme il vote (abstention,
basculements, corrélation au niveau de vie) suppose de descendre sous la
commune, au **bureau de vote** (≈ 70 000 en France), et de croiser ces
résultats avec des données socio-démographiques fines. Ce besoin est réel et
**récurrent à chaque scrutin** pour quatre publics : journalistes (récits du
soir électoral et analyses de fond), partis/candidats (ciblage du terrain),
chercheurs (géographie sociale du vote), collectivités (compréhension locale).

Mais c'est une **douleur analytique, pas opérationnelle critique** : il s'agit
d'éclairer/expliquer, rarement de débloquer une décision urgente. Et surtout, le
besoin est déjà **largement servi** (voir §4). La vraie douleur résiduelle est
le coût d'assemblage des jeux de données (résultats + contours BV + socio), qui
s'est **fortement réduit depuis 2023** grâce aux publications d'Etalab/INSEE.

## 2. Cible & qui paie
- **Journalistes / médias** : utilisateurs naturels, mais les grands titres ont
  déjà des cellules data (Le Monde, Le Figaro, Alternatives économiques) ; la
  presse régionale a peu de budget outil.
- **Partis / candidats** : **seuls vrais payeurs** (budgets de campagne réels),
  mais segment **déjà capté** par des éditeurs installés (Explain/ex-LMP,
  DigitaleBox, Quorum, NationBuilder) et **dépense intermittente** (cycle
  électoral).
- **Chercheurs / universités** : forte valeur d'usage, **faible solvabilité** ;
  publient eux-mêmes leurs analyses en open access.
- **Collectivités** : payeur possible mais besoin diffus, pas de ligne
  budgétaire évidente pour « comprendre le vote ».

Conclusion : utilisateur ≠ payeur dans la plupart des cas, et le seul segment
solvable est déjà occupé. C'est le point faible structurel de l'idée.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| Résultats par bureau de vote (Ministère de l'Intérieur) — ex. législatives 2024 | https://www.data.gouv.fr/datasets/elections-legislatives-des-30-juin-et-7-juillet-2024-resultats-definitifs-du-1er-tour | Licence Ouverte 2.0 | CSV / XLSX | par scrutin (def. ~J+8) | 1 fichier par scrutin, schémas non homogènes dans le temps ; sous réserve de recours/rectifications |
| Portail « Données élections » data.gouv.fr | https://www.data.gouv.fr/elections | Licence Ouverte 2.0 | pages + datasets | par scrutin | agrégateur, pas une base unifiée historique |
| Données des élections **agrégées** (data.gouv.fr/Etalab) | https://www.data.gouv.fr/datasets/donnees-des-elections-agregees | Licence Ouverte 2.0 | CSV (`general-results.csv`, `candidats-results.csv`) | MAJ 2026-04-05 | **structure modifiée en janv. 2026** ; jointures BV via `table-bv-reu.csv` ; rapprochement REU non fiable à 100 % |
| Proposition de **contours** des bureaux de vote (Etalab, à partir du REU) | https://www.data.gouv.fr/datasets/proposition-de-contours-des-bureaux-de-vote | Licence Ouverte 2.0 | GeoJSON / PMTiles | maj continue | **approximation** (diagrammes de Voronoi) ; « n'a pas vocation à faire autorité » ; imprécisions |
| Liaison **IRIS / Bureaux de vote 2024** | https://www.data.gouv.fr/datasets/liaison-iris-bureaux-de-vote-de-2024 | Licence Ouverte 2.0 | table de pondération | 2024 | estimation par carroyage ; tributaire de la numérotation BV des contours INSEE (≠ Intérieur) |
| INSEE Filosofi — **niveau de vie carroyé 200 m** | https://www.data.gouv.fr/datasets/revenus-pauvrete-et-niveau-de-vie-donnees-carroyees (aussi https://www.insee.fr/fr/statistiques/8735162) | Licence Ouverte 2.0 | Shapefile / GeoPackage / CSV | annuelle (millésime ~N-3) | seuil de confidentialité (carreaux < 11 ménages **imputés**, indicatrice `i_est_200`) |
| INSEE — Bureaux de vote et adresses de leurs électeurs (REU) | https://static.data.gouv.fr/resources/bureaux-de-vote-et-adresses-de-leurs-electeurs/20230627-150505/methodologie.pdf | Licence Ouverte 2.0 | CSV + doc | extraction REU 2022 | adresses normalisées/anonymisées ; ~3 000 BV/69 000 avec identifiants divergents Intérieur/INSEE |

Atout : **données ouvertes, propres et tabulaires**, jointures déjà outillées
(table IRIS/BV, table de conversion d'identifiants). Limite transverse :
l'**identifiant de bureau de vote** n'est pas parfaitement homogène entre
sources, et les contours/socio au BV sont **estimés** (pas mesurés).

## 4. Existant / concurrence
Tous éléments consultés le **2026-06-20**.

**a) Service public / données officielles — couverture forte.**
- Portail data.gouv.fr/elections + jeu agrégé BV + contours + table IRIS/BV :
  l'État a **déjà fait le travail d'ouverture et d'outillage du croisement**.
  https://www.data.gouv.fr/elections ,
  https://www.data.gouv.fr/datasets/donnees-des-elections-agregees ,
  https://www.data.gouv.fr/datasets/liaison-iris-bureaux-de-vote-de-2024

**b) Data journalism — saturé sur la diffusion grand public.**
- Le Monde / Les Décodeurs, cartes interactives des législatives 2024 (surtout
  niveau circonscription/commune) :
  https://www.lemonde.fr/les-decodeurs/article/2024/07/08/la-carte-des-resultats-des-legislatives-2024-au-second-tour_6247510_4355771.html
- Le Figaro, résultats par ville/circonscription :
  https://www.lefigaro.fr/elections/legislatives/carte-les-resultats-des-elections-legislatives-2024-dans-votre-ville-et-par-circonscription-20240707
- Alternatives économiques, **vote × revenu au bureau de vote** (exactement
  l'angle « sociologie du vote ») :
  https://www.alternatives-economiques.fr/le-revenu-variable-cle-du-premier-tour-des-legislatives-2024
- Fondation Jean-Jaurès, « La France politique de 2024 : portrait géographique
  et social » (régression au BV, contrôles socio) :
  https://www.jean-jaures.org/publication/la-france-politique-de-2024-portrait-geographique-et-social/

**c) Académique / recherche — angle « sociologie fine » déjà mûr.**
- CEVIPOF / CDSP Sciences Po : enquêtes électorales (depuis 1958), séries de
  résultats, portail data.sciencespo.fr.
  https://www.sciencespo.fr/cevipof/fr/etudes-enquetes/ ,
  https://www.sciencespo.fr/cdsp/fr/donnees/la-banque-de-donnees-du-cdsp/
- Le croisement résultats BV × niveau de vie INSEE a déjà donné lieu à un
  **ouvrage de référence** (Souidi & Vonderscher, ~70 000 BV 2017-2024) :
  https://www.nonfiction.fr/article-12585-ce-que-disent-les-votes-par-bureau.htm ,
  https://cartonumerique.blogspot.com/2026/03/nouvelle-cartographie-electorale-de-la.html
- Projet « Le carré social » (graphes électoraux infra-communaux) cité par le
  jeu de données IRIS/BV de data.gouv.fr.

**d) Logiciels commerciaux de campagne — segment payeur déjà occupé.**
- **Explain** (ex-Liegey-Muller-Pons), outil « 50+1 » : agrège les résultats
  passés et les **croise avec l'open data et l'INSEE** pour **scorer les bureaux
  de vote** (couleur politique, abstention) et recommander des actions terrain ;
  ~**3 000 € et plus** pour une campagne.
  https://www.lexpress.fr/informations/explain-quorum-ces-strateges-numeriques-plebiscites-par-les-candidats-aux-municipales_2118220.html ,
  https://www.lemagit.fr/conseil/Tour-dhorizon-des-CRM-politiques-en-France
- **DigitaleBox** : CRM politique avec cartographie électeurs « par secteur et
  bureau de vote », à partir de **19 €/mois** jusqu'au conseil stratégique.
  https://digitalebox.com/fr/communication-politique/ ,
  https://www.lesechos.fr/pme-regions/ile-de-france/municipales-digitalebox-aide-les-candidats-a-organiser-leurs-campagnes-1168873
- Également cités : Quorum, NationBuilder, Spallian.
  → la promesse « croiser résultats BV + INSEE pour cibler » **existe déjà en
  produit payant** côté partis/candidats.

**e) Open source / outils gratuits — diffusion outillée.**
- Makina Corpus : compilation de cartes électorales, démonstrateur TerraVisu
  (présidentielles 2002-2022), `elections.js`, Suffragia.
  https://makina-corpus.com/logiciel-libre/compilation-cartes-electorales-makina-corpus
- Cartes interactives communautaires (Ian Offord) sur data.gouv.fr :
  https://www.data.gouv.fr/reuses/cartes-interactives-des-resultats-des-elections-legislatives-2024
- Appli de téléchargement des contours BV en GeoJSON :
  https://www.data.gouv.fr/reuses/decoupage-contours-des-bureaux-de-vote

**Verdict de saturation : SATURÉ.** Le service public a ouvert et pré-outillé
les données ; la presse et les chercheurs publient déjà l'analyse fine
(participation, abstention, vote × revenu) ; et le seul créneau **payant**
(ciblage partis/candidats au BV) est tenu par des acteurs installés. Espace
libre résiduel, **étroit** : un outil **self-service unifié multi-scrutins**
(historique homogénéisé 2017→, basculements automatiques, focus villes
moyennes 10k-100k hab. où la recherche dit que « les progrès les plus importants
pourront être accomplis ») destiné à la **presse régionale / collectivités**,
plutôt qu'aux partis. Mais ce créneau reste à payeur incertain.

## 5. Différenciation
Faible et peu défendable. La méthode (« approche écologique » : résultats BV ×
socio carroyée, classement par déciles/centiles de niveau de vie) est
**publiée ouvertement**, code et données à l'appui ; un titre de presse ou un
chercheur la reproduit. Côté payeur, Explain fait déjà le scoring BV + INSEE.
La seule différenciation crédible serait **l'unification historique
multi-scrutins + détection automatique de basculements + UX self-service** pour
un public non-tech (presse régionale, collectivités) — utile mais
**copiable** et sans verrou (pas d'effet réseau, pas de donnée propriétaire).

## 6. Faisabilité & fiabilité technique
Architecture saine et conforme au principe **RAG(sens)/SQL(chiffres)** :
- **SQL / requêtes structurées** sur les chiffres (résultats BV, participation,
  scores, montants socio) → DuckDB/PostgreSQL sur fichiers tabulaires ; chaque
  chiffre traçable jusqu'au CSV source + scrutin + date.
- **RAG** uniquement sur le sens (libellés nuances/blocs, définitions INSEE,
  notes méthodo). Le LLM **explique**, ne calcule jamais.

Deux réserves de fiabilité propres au sujet :
1. **Inférence écologique** : corréler le vote d'un BV au niveau de vie *moyen*
   de son périmètre n'autorise **pas** de conclusion sur les comportements
   individuels (piège classique de l'écological fallacy). Le produit doit
   afficher cette limite, sinon il « survend » des chiffres exacts mais
   interprétés abusivement.
2. **Estimation géographique** : contours BV (Voronoi) et socio par carreau sont
   **approchés** ; les identifiants BV divergent (~3 000/69 000). Les jointures
   introduisent une incertitude à documenter.

Donc : chiffres bruts très fiables (SQL), **interprétation** intrinsèquement
fragile — à border par de la pédagogie méthodologique.

## 7. Monétisation / impact
- **Monétisation** : faible. Le segment solvable (partis/candidats) est capté et
  intermittent ; presse régionale et collectivités ont peu de budget ;
  chercheurs quasi nuls. Un SaaS aurait du mal à se différencier d'Explain
  (haut de gamme) et de l'open data gratuit (bas de gamme).
- **Impact civique** : réel mais **déjà produit** par la presse et les
  chercheurs en open access ; la valeur incrémentale d'un acteur de plus est
  limitée.

## 8. Risques
- **Marché saturé** côté diffusion, **occupé** côté payant → risque commercial
  élevé et difficile à maîtriser.
- **Mésusage interprétatif** (inférence écologique) → risque de crédibilité /
  d'instrumentalisation politique.
- **Sensibilité politique** : un outil de ciblage électoral expose à des débats
  CNIL/éthiques (les éditeurs existants encadrent déjà fortement leur usage).
- **Pas de verrou** : différenciation copiable, pas de donnée propriétaire.
- Pas de risque **éliminatoire** : données publiques (Licence Ouverte), socio
  INSEE agrégée/anonymisée → **légalité OK**, pas de blocage donnée.

## 9. Effort MVP
1. Ingestion + **homogénéisation multi-scrutins** (2017→) des résultats BV
   (schémas hétérogènes) → DuckDB ; normalisation des identifiants BV via
   `table-bv-reu.csv`.
2. Jointure socio (Filosofi 200 m → IRIS/BV) avec affichage explicite de
   l'incertitude et des imputations.
3. 3 vues : fiche **bureau de vote** (résultats + profil socio estimé),
   **basculements** entre scrutins, **abstention × niveau de vie**.
4. Pédagogie méthodo intégrée (avertissement inférence écologique, taux de
   couverture, sources datées).

Données prêtes et jointures pré-outillées : MVP techniquement accessible, mais
faire **mieux** que l'existant gratuit (Makina, cartes communautaires) et que
les analyses de presse demande un vrai effort produit/UX et un angle clair.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | 3 | 5 | 15 |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 |
| C5 | Différenciation défendable | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 3 | 6 |
| C8 | Maîtrise des risques | 2 | 2 | 4 |
| C9 | Monétisation / impact | 2 | 2 | 4 |
| | **Total** | | | **58 / 105** |

Justification des notes (une phrase chacune) :
- **C1 = 3** : besoin réel et récurrent à chaque scrutin, mais douleur
  analytique modérée et déjà largement satisfaite.
- **C2 = 2** : les seuls payeurs solvables (partis/candidats) sont déjà captés
  par Explain/DigitaleBox et dépensent de façon intermittente ; les autres
  publics paient peu.
- **C3 = 5** : données officielles complètes, propres, tabulaires, sous Licence
  Ouverte, avec jointures socio déjà outillées (table IRIS/BV).
- **C4 = 1** : espace saturé (État + presse + chercheurs + logiciels de campagne
  + cartes gratuites couvrent déjà tous les angles).
- **C5 = 2** : méthode publiée ouvertement et reproductible, aucun verrou
  durable, différenciation copiable.
- **C6 = 4** : chiffres bruts SQL parfaitement traçables, mais l'interprétation
  (inférence écologique, contours estimés) reste intrinsèquement fragile.
- **C7 = 3** : données prêtes et jointures pré-faites, mais homogénéiser le
  multi-scrutins et battre l'existant gratuit demande un vrai travail produit.
- **C8 = 2** : pas de risque légal, mais risque commercial (marché saturé,
  payeurs captés) et de mésusage interprétatif difficiles à maîtriser.
- **C9 = 2** : monétisation faible face aux acteurs installés et au gratuit ;
  impact civique réel mais déjà assuré par presse et chercheurs.

**Score /100** : 58 / 105 × 100 = **55**

## 11. Verdict & décision
🔁 **À retravailler** (55/100, juste au seuil). L'idée s'appuie sur des
**données exceptionnelles** (C3 = 5) et une **archi fiable** (C6 = 4), mais elle
attaque un **terrain saturé** (C4 = 1) où l'État a ouvert et pré-outillé les
données, où la presse et les chercheurs publient déjà l'analyse fine (vote ×
revenu, abstention), et où le **seul segment payant** — le ciblage partis/
candidats au bureau de vote — est tenu par Explain (≈ 3 000 €+/campagne) et
DigitaleBox. Pas de critère éliminatoire (légalité OK), mais **différenciation
faible et payeur incertain** la tirent vers le bas ; sans pivot, elle bascule
vers ❌ Écartée.

**Point bloquant à lever** : trouver un **payeur non capté + un angle non
couvert**. Piste la plus crédible : un outil **self-service multi-scrutins
homogénéisé** (basculements automatiques, focus villes moyennes 10k-100k hab.
où la recherche situe le gisement d'analyse) pour la **presse régionale et les
collectivités**, vendu sur la simplicité (vs. monter soi-même la chaîne données)
plutôt que sur la donnée elle-même.

**Prochaine étape concrète** : valider la disposition à payer d'un panel de
2-3 rédactions régionales / collectivités pour un tel outil clé en main ; si le
signal est faible, écarter. En parallèle, maquetter une fiche « bureau de vote »
intégrant l'avertissement d'inférence écologique pour tester la valeur perçue.

---

0014 | Analyse électorale fine (bureau de vote) | 🔁 À retravailler | 55/100 | Données superbes mais marché saturé, payeur incertain
