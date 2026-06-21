# Ciblage de la rénovation énergétique (passoires thermiques)

- **ID** : 0009
- **Statut** : 🔁 À retravailler
- **Score** : 60 / 100
- **Dernière mise à jour** : 2026-06-21
- **Pitch (1 phrase)** : Exploiter la base nationale des DPE (ADEME) pour
  identifier et cibler les logements classés **F/G** ("passoires thermiques") à
  rénover — pour les artisans RGE, les collectivités et les bailleurs.

---

## 1. Problème / douleur
La rénovation des passoires thermiques est un enjeu réel et politiquement chaud :
la location des logements F/G est progressivement interdite et l'État pousse la
rénovation (MaPrimeRénov', CEE, éco-PTZ). Deux douleurs distinctes :

- **Côté artisans RGE** : trouver des chantiers est vital et coûteux. Cibler
  finement les logements F/G (plutôt que le flyer au hasard) augmente le taux de
  conversion. C'est une douleur forte et récurrente — mais **déjà largement
  servie** (voir §4).
- **Côté collectivités / bailleurs** : piloter une politique locale de
  rénovation suppose de connaître son parc (où sont les passoires, quel
  gisement). Douleur réelle, mais **déjà adressée par un service public**
  (Go Rénove territorial / BDNB, voir §4).

Le problème de fond existe ; ce qui manque n'est pas la donnée mais un angle
**non saturé et légal** pour l'exploiter.

## 2. Cible & qui paie
- **Artisans RGE / installateurs / chauffagistes / menuisiers** : paient déjà
  pour des leads (achat de leads ~25–90 € l'unité, ou SaaS de prospection — voir
  §4). Payeur le plus naturel… mais c'est précisément l'usage **percuté par la
  loi** (interdiction du démarchage non sollicité en rénovation énergétique,
  voir §8).
- **Collectivités / EPCI / bailleurs sociaux** : budgets existants, mais
  l'outil de référence (Go Rénove) est **public et gratuit/PRO** pour eux.
- **Agents immobiliers / réseaux de mandataires** : intérêt « valeur verte » et
  détection de biens à vendre — segment déjà outillé (Cadastre.com, DPE Scanner).
- **Particuliers** : ne paient pas ; déjà servis par l'observatoire DPE et
  Go Rénove gratuits.

Utilisateur = payeur dans le cas artisan, ce qui est sain ; mais la valeur de
notre brique (une liste d'adresses F/G) est à la fois **donnée gratuitement** en
freemium et **juridiquement contrainte** pour son usage phare.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| DPE Logements existants (depuis juillet 2021) | https://data.ademe.fr/datasets/dpe03existant | Licence Ouverte / Etalab 2.0 | API JSON, vue tabulaire, dump PostgreSQL | continue (~350 000 DPE/mois ajoutés) | Pas de nom de propriétaire ; qualité hétérogène ; pré-2021 dans jeux séparés ; ré-étiquetage massif au 01/01/2026 (coef. électricité 2,3→1,9) |
| API DPE logements (data.gouv.fr) | https://www.data.gouv.fr/dataservices/api-dpe-logements | Licence Ouverte / Etalab | API JSON | régulière | Données « simplifiées » ; base complète = data.ademe.fr ; 10 appels/s/IP |
| DPE Logements neufs (depuis juillet 2021) | https://www.data.gouv.fr/datasets/dpe-logements-neufs-depuis-juillet-2021 | Licence Ouverte / Etalab | API/CSV | continue | Peu pertinent pour les passoires (neuf = bien classé) |
| Base Adresse Nationale (BAN) | https://www.data.gouv.fr/datasets/base-adresse-nationale | Licence Ouverte | API/CSV | continue | Géocodage des adresses DPE (fiabiliser les positions) |
| BDNB – Base de Données Nationale des Bâtiments (CSTB) | https://www.data.gouv.fr/datasets/base-de-donnees-nationale-des-batiments | Licence Ouverte 2.0 | GeoPackage / PostgreSQL, API | millésimée (ex. 2025-07) | ~32 M bâtiments, >170 champs open data ; intègre déjà les DPE — donc l'enrichissement « maison » est déjà fait par le CSTB |
| Cadastre / DVF (compléments) | https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres | Licence Ouverte | CSV | semestrielle (DGFiP) | Croisement prix/ventes pour scorer un bien |
| **RNIC** (copropriétés) | https://www.data.gouv.fr/datasets/registre-national-dimmatriculation-des-coproprietes | LO 2.0 | CSV ~430 Mo/trim. | MàJ **17 juin 2026** ; quotidien depuis avr. 2026 (vérifié 2026-06-21) | Pas de propriétaire ; SIRET syndic parfois absent ; colonnes renommées avr. 2026 |
| **RPLS** (logement social) | Ex. https://www.data.gouv.fr/datasets/repertoire-des-logements-locatifs-des-bailleurs-sociaux-rpls-2021 | LO 2.0 | CSV | **Fragmenté** — pas de national consolidé (Ithéa 2021, MàJ 2023) | Couverture partielle ; millésimes locaux sur data.gouv |
| **Cartes de bruit** (4e échéance) | https://www.data.gouv.fr/datasets/zones-de-bruit-des-cartes-de-bruit-strategiques-4eme-echeance-1 | LO 2.0 | Shapefile | Variable par agglomération | Couverture nationale **inégale** ; couches éclatées |

> [`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements envisagés

| Croisement | Cas d'usage | Faisabilité |
|---|---|---|
| **DPE × RNIC** | Prioriser les copropriétés avec le plus de lots F/G | Jointure adresse (BAN) — **moyenne** |
| **RNIC × DECP** (titulaires RGE) | Quels syndics / entreprises ont déjà des marchés rénovation sur des copropriétés du portefeuille ? | SIRET — **bonne** |
| **RPLS × DPE** | Performance énergétique du parc HLM (bailleurs) | Adresse — **moyenne** ; données RPLS fragmentées |
| **DPE × cartes bruit** | Double pénalité énergie + nuisance sonore | Spatial — **moyenne** (couverture bruit) |
| **BDNB × RNIC** | Enrichissement bâti déjà fait par CSTB — RNIC apporte la **gouvernance** copropriété (syndic, procédures) | Adresse / commune |

**Piste pivot** (cf. prochaine étape §11) : outil B2B **syndics professionnels /
bailleurs** — ordonnancement des travaux sur portefeuille de copropriétés, pas
prospection artisan. Voir idée dédiée [0025](../0025-coproprietes-renovation-rnic/).

**Volume (à citer, non halluciné)** : > 14 millions de DPE enregistrés entre
juillet 2021 et février 2026 selon une extraction de la base ADEME
(répartition ~68 % appartements, ~29 % maisons), dont ~678 000 appartements en
copropriété classés F/G — chiffres rapportés par un réutilisateur, à
re-vérifier par requête directe (https://www.plan-pluriannuel-de-travaux-3pt.fr/2026/02/20/statistiques-dpe-coproprietes-france/,
consulté 2026-06-20). Un guide diagnostiqueurs évoque « plus de 12 millions »
(https://diagfrance.com/outils-materiel-diagnostiqueur-guide/apis-open-data-diagnostic/api-ademe-dpe,
consulté 2026-06-20). → ordre de grandeur « plusieurs millions » **confirmé** ;
le chiffre exact doit venir d'une requête SQL/API datée (principe §6).

## 4. Existant / concurrence
> Règle : chaque affirmation = un lien + date de consultation (toutes 2026-06-20).

**Services publics / officiels (segment collectivités, bailleurs, particuliers)**
- **Go Rénove (CSTB, alimenté par la BDNB)** : 3 services — recherche à
  l'adresse (particuliers), **analyse territoriale (collectivités)**, **analyse
  de parc (bailleurs/gestionnaires)**, avec filtrage cartographique des bâtiments
  à fort potentiel de rénovation, DPE simulé, téléchargement des données et offre
  PRO. C'est **exactement** le ciblage visé pour collectivités/bailleurs, mais en
  service public. https://www.bdnb.io/services/gorenove/ et
  https://programmeprofeel.fr/projets/go-renove/
- **Observatoire DPE-Audit de l'ADEME** : consultation/recherche des DPE et
  statistiques officielles. https://observatoire-dpe-audit.ademe.fr/accueil
- **France Rénov'** : service public d'accompagnement des particuliers (conseil,
  aides). https://france-renov.gouv.fr (cf.
  https://www.ecologie.gouv.fr/politiques-publiques/diagnostic-performance-energetique-dpe)
- **BDNB open data (CSTB)** : ~32 M bâtiments, >170 champs ouverts (dont DPE
  rattaché au bâti), Licence Ouverte 2.0 — le socle est déjà ouvert et
  téléchargeable. https://www.data.gouv.fr/datasets/base-de-donnees-nationale-des-batiments

**Produits commerciaux (segment prospection artisans RGE) — marché saturé**
- **ThermoData** : plans de prospection porte-à-porte ciblés F/G, adresses BAN,
  score commercial 0–100 (6 critères DPE), export Excel, « livré en moins de
  30 s », données ADEME (Etalab) × BAN. https://thermodata.fr/
- **ScanReno** : SaaS DPE/rénovation, carte de prospection ADEME, widget de
  génération de leads, calcul 3CL + aides 2026 ; **freemium 5 leads/mois
  gratuit**, plans payants (50/200 leads, white-label, API).
  https://www.scanreno.fr/
- **MenuiserieAi** : « carte des passoires thermiques » F/G, estimation
  MaPrimeRénov'/CEE, export CSV publipostage. https://menuiserieai.fr/prospection-dpe
- **Thervy** : « radar à prospects » croisant **6 bases publiques** (ADEME, BDNB,
  DVF, Cadastre, Géorisques, IGN), scoring 0–100, fiche bien 360, pipeline,
  PDF. https://www.thervy.com/pour/entreprises-travaux
- **Achat de leads** (Samy Lead / S Lead Digital, etc.) : leads isolation/PAC
  qualifiés 25–90 €/lead, livrés en CRM. https://samy-lead.com/leads-energie/
- **Côté immobilier** : outils de veille DPE pour agents (ex. Cadastre.com avec
  filtrage DPE, « DPE Scanner ») cités par la profession.
  https://www.quotidiag.fr/demarchage-indesirable-apres-dpe/

**Tutoriels / open data « fais-le toi-même »**
- Articles expliquant comment cibler les F/G gratuitement avec les bases ADEME
  (DPE) + SIRENE + DVF, sans plateforme payante.
  https://webtensor.fr/blog/trouver-chantiers-donnees-publiques-sirene-dpe-dvf

**Verdict de saturation : SATURÉ.** Le ciblage des passoires thermiques est
couvert sur **tous** les segments : public (Go Rénove/BDNB) pour
collectivités/bailleurs/particuliers ; commercial pléthorique (et freemium) pour
les artisans ; tutoriels gratuits pour le bricolage. L'espace produit libre est
**marginal**, et l'usage phare (prospection) est par ailleurs juridiquement
contraint (§8).

## 5. Différenciation
Très faible et **peu défendable**. La donnée est la même pour tous (open data
ADEME/BDNB sous Etalab), le geste technique (filtrer F/G + cartographier +
scorer) est **copiable en un week-end** — ThermoData annonce d'ailleurs charger
« le fichier ADEME officiel automatiquement », et Thervy croise déjà 6 bases
publiques. Aucun avantage durable :
- pas de donnée propriétaire (le nom du propriétaire manque à tout le monde) ;
- pas d'effet réseau ;
- le meilleur enrichissement (DPE × bâti) est **déjà fait et ouvert** par le CSTB
  (BDNB), donc non différenciant.

Le seul angle théoriquement défendable serait un **usage strictement légal et de
niche** (ex. priorisation de parc pour bailleurs/collectivités avec valeur
ajoutée méthodologique) — mais il affronte un service public gratuit.

## 6. Faisabilité & fiabilité technique
Techniquement **simple et robuste** : données tabulaires propres → ingestion
DuckDB/PostgreSQL → requêtes structurées (filtre classe F/G, code postal,
surface, énergie de chauffage), géocodage BAN, cartographie. **Tous les chiffres
affichés (nombre de passoires, surfaces, répartitions, estimations d'aides selon
barèmes) viennent de SQL traçable** jusqu'au DPE source + date d'extraction.
Le LLM ne sert qu'à **expliquer le sens** (libellés DPE, gestes de travaux,
conditions d'aides) — conforme au principe RAG(sens)/SQL(chiffres), **risque
d'hallucination faible par construction**. Réserve : la fiabilité métier dépend
de la qualité du DPE lui-même (ré-étiquetage 2026, DPE anciens), à afficher
honnêtement.

## 7. Monétisation / impact
- **SaaS prospection artisans** (modèle dominant du marché) : possible mais
  cannibalisé par le **freemium** (ScanReno 5 leads/mois gratuits) et l'**open
  data DIY**, et fragilisé par l'interdiction de démarchage (§8).
- **Abonnement collectivités/bailleurs** : se heurte au service public **gratuit**
  Go Rénove.
- **Impact** : réel (accélérer la rénovation), mais déjà porté par les
  dispositifs publics existants → contribution marginale.

Conclusion : ni revenu défendable, ni impact additionnel clair par rapport à
l'existant.

## 8. Risques
- **Risque juridique majeur (proche de l'éliminatoire sur l'usage phare)** :
  depuis le **1er juillet 2025** (loi du 30 juin 2025 contre les fraudes aux
  finances publiques), le **démarchage non sollicité par téléphone, SMS, email
  ou réseaux sociaux est interdit en rénovation énergétique** ; extension à
  **tous secteurs au 11 août 2026**, sauf consentement préalable explicite.
  https://www.economie.gouv.fr/particuliers/numerique-et-cybersecurite/comment-se-proteger-du-demarchage-abusif
  et https://www.dtl40.fr/dpe-diffusion-donnees-personnelles-a2.html
- **Risque RGPD** : la base DPE est diffusée à des fins de transparence
  environnementale ; l'exploiter pour de la prospection commerciale pose un
  problème de **détournement de finalité** et de **ré-identification** (adresse
  complète + caractéristiques permettent d'identifier le logement/occupant) — la
  CNIL exige le consentement pour la prospection. Sujet déjà soulevé
  publiquement (questions parlementaires, plaintes).
  https://www.quotidiag.fr/demarchage-indesirable-apres-dpe/ et
  https://www.dtl40.fr/dpe-diffusion-donnees-personnelles-a2.html
- **Risque réputationnel** : se positionner comme « machine à démarcher les
  passoires » est mal vu et associé aux arnaques MaPrimeRénov'.
- **Risque marché** : saturation + freemium + service public → faible
  willingness-to-pay.
- **Risque donnée** : ré-étiquetage 2026 (~850 000 logements F/G reclassés) rend
  toute liste « passoires » volatile.

Note : ces risques ne rendent pas l'outil **per se** illégal (l'open data reste
réutilisable, le boîtage géographique anonyme et les usages collectivités/bailleurs
restent licites), mais ils **détruisent l'usage commercial le plus rémunérateur**.

## 9. Effort MVP
Faible — c'est justement le problème (barrière à l'entrée nulle) :
1. Ingestion API/dump DPE ADEME → DuckDB ; filtre F/G + géocodage BAN.
2. Carte + filtres (classe, type, énergie, rayon) + score de priorité (SQL).
3. Export CSV / fiche bien (avec estimation d'aides via barèmes officiels).
4. Traçabilité : chaque chiffre → DPE source + date d'extraction + avertissement
   qualité/ré-étiquetage.

Mais un MVP de qualité comparable existe déjà chez plusieurs concurrents « en
30 secondes » → l'effort n'est pas le facteur limitant, la **différenciation et
la légalité** le sont.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 |
| C2 | Cible solvable (qui paie) | 3 | 3 | 9 |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 |
| C5 | Différenciation défendable | 2 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | 2 | 5 | 10 |
| C7 | Facilité du MVP | 2 | 5 | 10 |
| C8 | Maîtrise des risques | 2 | 1 | 2 |
| C9 | Monétisation / impact | 2 | 2 | 4 |
| | **Total** | | | **63 / 105** |

**Score /100** : 63 / 105 × 100 = **60**

Justification (une phrase par critère) :
- **C1 = 4** : douleur réelle et récurrente (trouver des chantiers, piloter une
  politique), mais pas un 5 car déjà largement adressée.
- **C2 = 3** : des payeurs existent (artisans, collectivités) mais le plus
  naturel est miné par la loi et par le freemium, donc pas 4.
- **C3 = 4** : données ouvertes, propres, API + dump, traçables ; pas 5 à cause
  de l'absence du propriétaire, du ré-étiquetage 2026 et de la qualité variable.
- **C4 = 1** : segment saturé sur tous les fronts (public + ≥5 produits
  commerciaux dont freemium + tutoriels DIY).
- **C5 = 1** : copiable en un week-end, donnée commune, enrichissement clé déjà
  ouvert par le CSTB (BDNB), aucun moat.
- **C6 = 5** : tabulaire → SQL, chiffres traçables, LLM cantonné au sens, faible
  risque d'hallucination.
- **C7 = 5** : MVP trivial (filtrer F/G + carte), donnée prête — mais cette
  facilité même nourrit la saturation.
- **C8 = 1** : risques juridiques (démarchage interdit), RGPD (détournement de
  finalité) et réputationnels majeurs et mal maîtrisables sur l'usage phare.
- **C9 = 2** : monétisation cannibalisée par le gratuit/public et impact
  additionnel marginal.

## 11. Verdict & décision
🔁 **À retravailler** (score 60/100, dans la bande 55–69).

L'idée part d'une **donnée excellente** (DPE ouvert, BDNB) et d'un **problème
réel**, mais le **seed est bancal sur deux points décisifs** :
1. **Saturation** : le ciblage des passoires est déjà fait — Go Rénove/BDNB
   (public) pour collectivités/bailleurs/particuliers, et au moins cinq produits
   commerciaux (dont du freemium) pour les artisans.
2. **Mur juridique** sur l'usage le plus rémunérateur : le démarchage non
   sollicité en rénovation énergétique est interdit depuis le 1er juillet 2025
   (extension à tous secteurs au 11 août 2026), et l'usage prospection des DPE
   pose un problème RGPD de détournement de finalité.

Ce n'est **pas une élimination stricte** (la donnée existe et l'outil n'est pas
illégal en soi : open data réutilisable, boîtage anonyme et usages
collectivités/bailleurs licites), d'où le statut « à retravailler » plutôt
qu'« écartée ». Mais la barre est haute : il faut trouver un angle **à la fois
légal, défendable et non couvert par le service public gratuit** — ce qui est
étroit.

**Prochaine étape concrète** : avant tout développement, valider (ou invalider)
un pivot précis : par exemple un outil B2B de **priorisation de parc pour
bailleurs sociaux / syndics** apportant une valeur méthodologique que Go Rénove
ne fournit pas (ex. ordonnancement des travaux, simulation budgétaire
multi-aides traçable), en confirmant qu'il existe un payeur prêt à signer
**malgré** l'alternative publique gratuite. Si ce payeur n'est pas trouvé après
quelques entretiens, **basculer en ❌ Écartée**.
