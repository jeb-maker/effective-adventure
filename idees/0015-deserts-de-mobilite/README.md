# Observatoire des déserts de mobilité

- **ID** : 0015
- **Statut** : ❌ Écartée
- **Score** : 50 / 100
- **Dernière mise à jour** : 2026-06-23
- **Pitch (1 phrase)** : Croiser les horaires de transport public (GTFS via
  transport.data.gouv.fr) avec la population et les équipements (INSEE) pour
  cartographier les **déserts de mobilité** et l'accessibilité aux services, à
  destination des AOM, collectivités et bureaux d'études mobilité.

---

## 1. Problème / douleur
Les zones mal desservies par les transports en commun (« déserts de mobilité »)
sont un vrai sujet de politique publique : la Loi d'orientation des mobilités
(LOM) impose aux AOM de planifier l'offre, et les territoires peu denses
combinent dépendance à la voiture et éloignement des services. Le besoin est
**réel mais épisodique** côté payeur : un diagnostic d'accessibilité s'inscrit
dans un plan de mobilité, une révision de SRADDET ou une étude ponctuelle, pas
dans une douleur opérationnelle quotidienne. La douleur aiguë (être enclavé)
est subie par l'**habitant**, qui ne paie pas. La douleur du décideur est plus
tiède : « objectiver pour arbitrer », ce que beaucoup font déjà avec des outils
existants (voir §4). Problème légitime, intensité moyenne pour un produit
marchand.

## 2. Cible & qui paie
- **AOM / collectivités (régions, EPCI, départements)** : budget de planification
  mobilité existant (mandaté par la LOM), mais achat via **marché public**
  (cycle long) et culture du « faire faire » par bureau d'études plutôt que de
  l'abonnement SaaS.
- **Bureaux d'études mobilité / agences d'urbanisme** : ce sont autant des
  **clients potentiels que des concurrents** — ils réalisent eux-mêmes ces
  diagnostics et disposent déjà d'outils gratuits (Cerema, QGIS, OTP, r5).
- **Habitant / usager** : bénéficiaire, ne paie pas.

Le payeur existe (budgets mobilité publics) mais il n'y a **pas d'acheteur
récurrent en self-service**, et une alternative gratuite officielle (Cerema)
couvre déjà le cœur du besoin. Utilisateur ≠ payeur dans le cas grand public.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| GTFS transports publics (PAN) | https://transport.data.gouv.fr/datasets?format=GTFS&type=public-transit | Mixte : Licence Ouverte 2.0 **ou** ODbL (share-alike) selon le jeu | GTFS (+ NeTEx) | Continue (versions historisées, ex. agrégat Nouvelle-Aquitaine maj 2026-06-08) | **Couverture incomplète : ~76 % de la population, ~350 territoires sur 1 156** (transport.data.gouv.fr, 2026-06-20). Pas de GTFS national unique — données fragmentées par AOM/région. Le transport à la demande (TAD) et le rural sont mal représentés |
| API PAN (liste des jeux) | https://www.data.gouv.fr/dataservices/le-point-dacces-national-aux-donnees-de-transport | Licence Ouverte 2.0 | API JSON | Continue | Référence/expose les jeux ; ne fournit **pas** de calcul d'isochrone/routing |
| INSEE — Localisation & accès de la population aux équipements (BPE + Filosofi + Metric-OSRM) | https://www.data.gouv.fr/datasets/donnees-sur-la-localisation-et-lacces-de-la-population-aux-equipements | Licence Ouverte 2.0 | Parquet (partitionné par région) | Maj par millésime BPE (jeu maj 2025-07-16) | **Accessibilité calculée en VOITURE** (Metric-OSRM), pas en transport en commun — ne mesure pas le désert *de transport* |
| INSEE — Base permanente des équipements (BPE) | https://www.insee.fr/fr/metadonnees/source/operation/S2216/presentation | Licence Ouverte | CSV | Annuelle (BPE 2024 : 2,85 M équipements, 229 types) | Géoloc x,y de qualité variable selon le type ; champ marchand/non marchand hétérogène |
| INSEE — population carroyée (Filosofi 200 m) | https://www.insee.fr/ (carreaux 200 m) | Licence Ouverte | CSV/Parquet | Périodique | Secret statistique sur carreaux peu peuplés |

Conséquence clé : pour la pondération population × accessibilité **routière**, la
donnée est quasi prête (jeu INSEE par carreau). Pour l'accessibilité
**transport en commun** (le cœur de l'idée), il faut router du GTFS, et c'est là
que la couverture manque — **précisément dans les zones rurales** qu'on veut
qualifier de déserts.

## 4. Existant / concurrence
Tous liens consultés le **2026-06-20**.

**Services publics / officiels — le besoin est largement déjà outillé :**
- **Cerema — extension QGIS « Networks » (gratuite, moteur Musliw)** : analyse
  et cartographie de l'**accessibilité multimodale à partir de fichiers GTFS**,
  croisement avec données socio-économiques, cartes d'offre (nb de passages aux
  arrêts). C'est, à peu de chose près, **le produit décrit par cette idée, en
  gratuit, ciblé collectivités / bureaux d'études / agences d'urbanisme**.
  https://www.cerema.fr/fr/activites/services/formation-analyser-cartographier-offre-transport-multimodale
- **Cerema — Capamob** : méthodes et fiches pour « mesurer l'accessibilité d'un
  territoire », isochrones, accessibilité aux services, identification des
  sous-espaces faiblement accessibles.
  https://capamob.cerema.fr/territoire/mesurer-laccessibilite-territoire
- **Cerema Data — isochrones autour des gares** (15 min à pied, vélo, voiture)
  déjà calculées et diffusées (cité par Capamob, lien ci-dessus).
- **Observatoire des territoires (ANCT)** : indicateur « temps d'accès routier
  moyen à un centre d'équipements et de services » (avril 2025) et « temps
  d'accès au réseau France services » — cartographie + données ouvertes.
  https://www.observatoire-des-territoires.gouv.fr/temps-dacces-routier-moyen-un-centre-dequipements-et-de-services-en-hexagone
  et https://anct.gouv.fr/ressources/cartotheque/temps-d-acces-routier-au-reseau-france-services
- **INSEE** : jeu de données prêt « accès de la population aux équipements »
  (durée/distance par carreau au plus proche équipement). Voir §3.

**Produits commerciaux (géomarketing / isochrones) :** Isocarto, Smappen,
Maplytics, ZoneChalandise.fr — génèrent des isochrones + couches INSEE
(population, revenus) et exports PDF/Excel. Ciblent surtout commerce/immobilier,
souvent **voiture** ; certains gèrent le transport en commun (Isocarto).
- https://isocarto.fr/ · https://www.smappen.fr/carte-temps-trajet/ ·
  https://maplytics.fr/ · https://zonechalandise.fr/blog/logiciel-geomarketing-zone-de-chalandise
  (prix non détaillés ici → **à vérifier** avant toute comparaison tarifaire).

**Open source / standards :** OpenTripPlanner et r5/r5r (matrices de temps de
trajet multimodal GTFS), QGIS — briques libres matures que tout bureau d'études
peut assembler.

**Réutilisations déclarées sur le PAN** : la page Réutilisations liste des
projets d'accessibilité (ex. « Tourisme en train : accessibilité ferroviaire »)
mais aucun « observatoire des déserts de mobilité » identifié comme produit
dominant. https://transport.data.gouv.fr/reuses

**Verdict de saturation : partiel → saturé sur le cœur.** L'accessibilité aux
services **en voiture** est saturée (INSEE, ANCT, géomarketing). L'accessibilité
**en transport en commun via GTFS** est couverte par un **outil officiel gratuit
(Cerema Networks)** et par des briques libres. L'espace réellement libre se
réduit à un **packaging** (observatoire national clé en main, mise à jour
automatique, vocabulaire « désert de mobilité », pré-calcul national) — créneau
étroit et imitable.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0015-deserts-de-mobilite` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `transport-mobility-data-fr` — Transport & mobilité FR

Fichier : [`catalogue-saas/vendors/transport-mobility-data-fr.json`](../../catalogue-saas/vendors/transport-mobility-data-fr.json) (18 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `iv-mobilites` | Île-de-France Mobilités — open data | FR | strong | partial |
| `cityway` | Cityway | FR | strong | partial |
| `transport-data-gouv` | transport.data.gouv.fr | FR | strong | partial |
| `padam-mobility` | Padam Mobility | FR | strong | partial |
| `hove` | Hove (ex-Deliveroo data ref mobility analytics) | FR | strong | partial |
| `tfl-open-data` | Transport for London — Open Data | GB | absent | partial |
| `mobilitydata-org` | MobilityData | US | unknown | partial |
| `transit-land` | Transitland | US | absent | partial |
| `itoworld` | ITO World | GB | absent | partial |
| `navitia` | Navitia (Hove Group) | FR | strong | partial |
| `geovelo` | Geovelo | FR | strong | partial |
| `karos` | Karos | FR | strong | partial |
| … | _+6 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment transport-mobility-data-fr
```

<!-- catalogue-saas-end -->
## 5. Différenciation
Faible et peu défendable. La méthodologie (GTFS + population + isochrones) est
publique, le moteur de référence (Cerema Networks/Musliw) est **donné
gratuitement**, et les briques (OTP, r5) sont open source. Un avantage possible
— observatoire **national pré-calculé**, rafraîchi automatiquement, comparaisons
inter-territoires, narration « désert de mobilité » — est un avantage de
**produit/UX**, pas de donnée : copiable, et concurrencé par un acteur public
gratuit qui a déjà la légitimité institutionnelle auprès de la cible.

## 6. Faisabilité & fiabilité technique
Architecture saine : GTFS + BPE + Filosofi ingérés en base structurée
(DuckDB/PostGIS), routing multimodal via OTP/r5r, calcul de matrices
temps-de-trajet et d'indicateurs d'accessibilité **par carreau/IRIS**. Tous les
**chiffres** (nb de départs/jour, temps d'accès, population desservie sous X min)
sortent de **requêtes structurées / routing déterministe traçables** ; un LLM ne
servirait qu'à **expliquer** (définitions, libellés, synthèse de zone) — conforme
au principe **RAG(sens) / SQL(chiffres)**. Risque d'hallucination faible **par
construction**. Réserve : le routing multimodal national est lourd à industrialiser
et à maintenir à jour (fragmentation GTFS, versions, calendriers).

## 7. Monétisation / impact
- **Monétisation faible** : alternative officielle gratuite (Cerema), achat
  public lent, pas d'acheteur récurrent en self-service. Modèles possibles
  (SaaS collectivités, prestations d'étude) entrent en concurrence frontale avec
  les bureaux d'études… qui sont aussi la cible.
- **Impact potentiel réel** : objectiver les déserts de mobilité pour orienter
  l'offre est utile en politique publique. Mais l'impact est déjà partiellement
  capté par les dispositifs publics existants. Critère « revenu OU impact » :
  c'est l'impact, pas le revenu, qui sauve la note.

## 8. Risques
- **Paradoxe de la donnée (quasi éliminatoire)** : les déserts de mobilité sont
  par définition là où la couverture GTFS est la plus faible (rural, TAD non
  modélisé). Le produit serait **aveugle ou faux là où il prétend être utile**,
  ce qui ruine sa crédibilité ; il faudrait afficher honnêtement « zone non
  couverte » sur une grande partie de la cible.
- **Concurrent public gratuit** : Cerema Networks/Capamob couvre le cœur, avec
  la légitimité institutionnelle.
- **Vente publique** : cycles longs, marchés, faible appétence à l'abonnement.
- **Débat méthodologique** : qu'est-ce qu'un « désert » (seuils, modes, heures
  creuses) ? Contestable, donc fragilise un produit qui en fait son nom.

## 9. Effort MVP
Lourd : (1) collecter et **dédupliquer/assembler les GTFS fragmentés** par AOM/
région, gérer versions et calendriers ; (2) router multimodal (OTP/r5r) et
produire des matrices temps-de-trajet à maille fine ; (3) croiser avec BPE +
Filosofi pour des indicateurs population-pondérés ; (4) interface carto +
traçabilité (chaque chiffre → source + date + **taux de couverture affiché**).
Ce n'est pas un MVP de week-end ; et une démo crédible suppose déjà de gérer
les trous de couverture.

## 10. Scoring

> **Scoring ajusté après revue critique du 2026-06-23** (voir [`revue.md`](revue.md)).
> Notes abaissées : C2 (3→2), C9 (3→2). Score 54 → **50** ; verdict inchangé
> (❌ Écartée, marge sous le seuil élargie). Notes initiales rappelées en colonne dédiée.

| # | Critère | Poids | Note initiale | Note (post-revue) | Pondéré |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | 3 | 3 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | 3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | 2 | 2 | 2 | 4 |
| C5 | Différenciation défendable | 2 | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 2 | 2 | 4 |
| C8 | Maîtrise des risques | 2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | 2 | 3 | 2 | 4 |
| | **Total** | | | | **52 / 105** |

**Score /100** : 52 / 105 × 100 = **50**

Justification des notes (post-revue) :
- **C1 = 3** : problème public réel mais besoin diagnostique épisodique et douleur
  surtout côté habitant non-payeur, pas une douleur marchande aiguë.
- **C2 = 2** (ajusté) : budgets mobilité publics existent (LOM), mais achat via
  marché public lent, **pas d'acheteur récurrent en self-service** et alternative
  gratuite officielle (Cerema) → ancrage 2.
- **C3 = 3** : INSEE BPE/Filosofi et GTFS sont ouverts et propres, mais la
  couverture GTFS est partielle (~76 % pop) et la plus faible exactement dans
  les zones-cibles → ni 4 ni 2.
- **C4 = 2** : cœur déjà couvert par Cerema (gratuit), ANCT, INSEE et outils de
  géomarketing ; le résidu de packaging est lui-même rogné par les **observatoires
  Cerema** (politiques locales de mobilité, plans de mobilité) — note plafonnée.
- **C5 = 2** : méthode publique et moteur officiel gratuit → différenciation de
  pur produit, copiable.
- **C6 = 4** : chiffres issus de routing/SQL traçables, RAG borné au sens ; pas 5
  car l'industrialisation multimodale nationale est lourde.
- **C7 = 2** : assemblage de GTFS fragmentés + routing national + gestion des
  trous = chantier, pas un MVP rapide.
- **C8 = 2** : paradoxe de la donnée (aveugle là où ça compte) + concurrent
  public gratuit = risques structurels mal maîtrisés.
- **C9 = 2** (ajusté) : impact public réel mais **déjà capté** par les dispositifs
  publics (observatoires Cerema, ANCT) → impact marginal d'un énième observatoire faible.

## 11. Verdict & décision
❌ **Écartée** (score **50/100** après revue critique du 2026-06-23, **sous le seuil
de 55** ; recalcul C2 3→2, C9 3→2 confortant la décision initiale), et fragilisée
par un point quasi éliminatoire : le **paradoxe de couverture** (la donnée GTFS manque
précisément dans les déserts à mesurer) couplé à un **concurrent officiel
gratuit** (Cerema « Networks »/Capamob) qui sert déjà la même cible avec
légitimité. La donnée INSEE d'accessibilité existante étant en outre **routière**
et non transport-en-commun, le différenciant « transport » repose sur la donnée
la moins disponible.

**Piste de retravail (seul angle qui pourrait la repasser au-dessus du seuil)** :
abandonner l'« observatoire généraliste » (déjà fait) et viser un **créneau que
les outils gratuits ne servent pas** — p. ex. le **suivi temporel automatisé**
des dégradations/améliorations d'offre (diff entre versions GTFS dans le temps :
lignes supprimées, fréquences en baisse, arrêts perdus) comme **système d'alerte**
pour AOM, là où Cerema/Capamob font surtout du diagnostic ponctuel. À ne
ré-ouvrir que si un payeur récurrent nommé est confirmé.

---

0015 | Observatoire des déserts de mobilité | ❌ Écartée | 50/100 | Cœur déjà fait par Cerema gratuit (+ observatoires Cerema) ; donnée manque dans déserts ; revue 2026-06-23
