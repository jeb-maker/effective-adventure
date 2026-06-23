# Exposition risques des parcelles agricoles (RPG × Géorisques × Hub'Eau)

- **ID** : 0026
- **Statut** : 🔁 À retravailler
- **Score** : 56 / 100
- **Dernière mise à jour** : 2026-06-23
- **Pitch (1 phrase)** : Cartographier l'exposition des parcelles agricoles aux
  risques industriels (ICPE), hydriques et réglementaires (PLU) en croisant le
  Registre parcellaire graphique, Géorisques et Hub'Eau — pour agriculteurs,
  coopératives, aménageurs ruraux et collectivités.

---

## 1. Problème / douleur

Un agriculteur ou un aménageur qui étudie une parcelle doit croiser manuellement :
- le **RPG** (culture, surface, îlots),
- les **installations classées** (Géorisques / ICPE),
- la **qualité de l'eau** (nappes, rivières — Hub'Eau),
- le **zonage PLU** (pression urbanisation).

Ces données sont ouvertes mais **jamais présentées en fiche parcelle agricole**
unifiée. La douleur est réelle pour :
- choix de cultures / conformité environnementale,
- négociation foncière (extension 0021, angle agricole),
- politiques territoriales (chambres d'agriculture, EPCI ruraux).

## 2. Cible & qui paie

| Segment | Besoin | Payeur ? |
|---|---|---|
| **Agriculteurs / CUMA** | Savoir si parcelle exposée ICPE / restriction eau | Faible (sensible au prix) |
| **Coopératives / négoce agricole** | Due diligence foncier agricole | Possible (B2B) |
| **Aménageurs / promoteurs** (foncier agricole) | Pression PLU + contraintes env. | Déjà clients Kel Foncier — concurrence |
| **Chambres d'agriculture / collectivités** | Diagnostic territorial | Budget public / subvention |

Payeur le plus plausible : **cabinet conseil agricole / foncier** ou **collectivité**
dans le cadre d'un diagnostic territorial — pas l'agriculteur individuel.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| **RPG** | https://www.data.gouv.fr/datasets/registre-parcellaire-graphique-agricole | LO 2.0 | CSV/GeoJSON/ZIP | MàJ **20 juin 2026** | Métropole ; jointure PCI |
| **API Géorisques** (ICPE, BASIAS, etc.) | https://www.data.gouv.fr/dataservices/api-georisques | LO 2.0 | REST JSON | Continue | 10 req/s ; requête par coordonnée |
| **Hub'Eau** (hydrométrie, qualité eau) | https://hubeau.eaufrance.fr/ — ex. hydrométrie v2 | LO 2.0 | REST JSON | API v2.0.1 opérationnelle (test 21/06/2026) | Endpoints multiples ; pas un seul dump |
| **GPU / PLU** | https://www.geoportail-urbanisme.gouv.fr/ | LO 2.0 | WFS/WMS | Continue | Qualité variable |
| **PCI / cadastre** | https://www.data.gouv.fr/datasets/cadastre | LO 2.0 | GeoJSON | Continue | Lien RPG ↔ parcelle cadastrale |

**Vérification** (2026-06-21) :
- RPG : 4 ressources (CSV, GeoJSON, ZIP) sur data.gouv, licence fr-lo.
- Hub'Eau : `GET /api/v2/hydrometrie/referentiel/stations` → 6 433 stations, JSON valide.
- Géorisques : API référencée, quota documenté.

[`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements

| Croisement | Output | Technique |
|---|---|---|
| RPG × ICPE (spatial) | Parcelles à < 500 m d'une ICPE seuil | PostGIS ST_DWithin |
| RPG × Hub'Eau (bassin) | Stations qualité eau dans le bassin versant de l'îlot | Jointure spatiale + code station |
| RPG × GPU | Parcelles agricoles en zone constructible | Zonage PLU |
| RPG × Géorisques (RGA, inondation) | Aléas naturels sur foncier agricole | Spatial join |

## 4. Existant / concurrence

### Outils publics gratuits — barrière d'entrée basse

| Concurrent | Positionnement | URL | Consulté |
|---|---|---|---|
| **Géoportail (IGN)** | Consultation unitaire couches ICPE, RPG, Natura 2000 — service public, gratuit | https://www.geoportail.gouv.fr/ | juin 2026 |
| **Géorisques (BRGM/MTES)** | Rapport risques par adresse (ICPE, aléas naturels, BASIAS) — gratuit | https://www.georisques.gouv.fr/ | juin 2026 |
| **Cartes DDT/DDTM** | Cartographies environnementales agricoles RPG × couches réglementaires, gratuites mais départementales (ex. DDTM76 Seine-Maritime) | https://www.seine-maritime.gouv.fr/Actions-de-l-Etat/Agriculture-Foret/Enjeux-environnementaux-Eau-Erosion-Ruissellement/ | juin 2026 |

### Outils SaaS/SIG professionnels — concurrence directe

| Concurrent | Positionnement | URL | Consulté |
|---|---|---|---|
| **GÉOPERSO** | SIG métier foncier agricole — RPG, AOC, zones humides, Natura 2000, PLU, contraintes env. Cible chambres d'agriculture, SAFER, bureaux d'études | https://www.geoperso.fr/logiciel-valorisation-fonciere-agricole/ | juin 2026 |
| **Géofoncier** | 250+ couches (cadastre, PLU, servitudes, risques naturels/techno), fiche parcelle PDF exportable. Cible notaires et experts fonciers — couvre partiellement le foncier agricole | https://www.geofoncier.fr/identifier-risques-et-contraintes/ | juin 2026 |
| **Terravisu / SeineYonne (Makina Corpus)** | Application coopérative RPG × ICPE × Natura 2000 × Hub'Eau déployée pour SeineYonne. Preuve que ce croisement existe déjà en production chez une coopérative | https://makina-corpus.com/sig-webmapping/application-cartographique-identification-parcelles-agricoles-assolements | juin 2026 |

### Outils adjacents (gestion parcellaire, pas risques)

| Concurrent | Positionnement | URL | Consulté |
|---|---|---|---|
| **Geofolia (Isagri)** | Logiciel gestion parcellaire agricole avec alertes réglementaires phyto (ZNT, IFT) — pas risques industriels/ICPE | https://www.isagri.fr/geofolia/ | juin 2026 |
| **Farmstar (Airbus / Arvalis)** | Télédétection satellite, pilotage fertilisation — 14 000 agriculteurs. Pas risques environnementaux | https://www.myfarmstar.com/ | juin 2026 |

### Analyse des lacunes

**Verdict concurrence** : le croisement RPG × risques environnementaux est déjà en production
dans plusieurs outils (GÉOPERSO, Géofoncier, Terravisu/coopératives). Les DDT offrent des
cartes gratuites départementales. Il n'existe pas de produit SaaS national grand public
couvrant l'ensemble (ICPE + eau + PLU + aléas) avec une UX orientée « fiche parcelle
agricole » en libre-service — mais la demande solvable pour ce produit reste à démontrer.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0026-exposition-parcelles-agricoles` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `geospatial-gis-fr` — Géospatial & carto FR

Fichier : [`catalogue-saas/vendors/geospatial-gis-fr.json`](../../catalogue-saas/vendors/geospatial-gis-fr.json) (21 entrées)

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
| `geoperso` | GÉOPERSO | FR | strong | partial |
| `makina-corpus` | Makina Corpus | FR | strong | partial |
| `geoportail-urbanisme` | Géoportail de l'urbanisme (GPU) | FR | strong | partial |
| … | _+9 autres_ | | | |

#### Segment `environmental-data-fr` — Environnement & risques FR

Fichier : [`catalogue-saas/vendors/environmental-data-fr.json`](../../catalogue-saas/vendors/environmental-data-fr.json) (20 entrées)

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
| `sandre` | Sandre | FR | strong | partial |
| `drias-climat` | DRIAS — Futurs climatiques | FR | strong | partial |
| `basol` | BASOL — Sites et sols pollués | FR | strong | partial |
| … | _+8 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment geospatial-gis-fr
```

<!-- catalogue-saas-end -->

## 5. Différenciation

**Potentiel de différenciation** : une fiche parcelle agricole unifiée — ICPE + eau + PLU +
aléas — accessible en libre-service national, sans installation SIG, à un tarif abordable.

**Limites sévères** :
- Toutes les données sources sont publiques et gratuites → barrière à l'entrée nulle
- GÉOPERSO fait déjà ce croisement pour les professionnels fonciers agricoles
- Terravisu/SeineYonne prouve qu'une coopérative commande du sur-mesure, pas du SaaS national
- Les DDT publient des cartographies gratuites par département
- Géofoncier couvre le segment expert avec 250+ couches déjà intégrées

**Différenciation théorique** : UX grand-public (vs SIG pro) + national (vs départemental).
**Défendabilité** : très faible — copiable par n'importe quel acteur en quelques semaines
dès lors qu'il a accès aux mêmes données publiques.

## 6. Faisabilité & fiabilité technique

- Stack : PostGIS (RPG + PCI + couches Géorisques en shapefile) + appels Hub'Eau
  pour stations à proximité.
- Chiffres (surface, nb ICPE, distance) = **SQL/spatial traçable**.
- LLM : explication réglementaire ICPE / zonage PLU uniquement.

## 7. Monétisation / impact

**Options envisagées** :

| Modèle | Cible | Réalisme |
|---|---|---|
| SaaS freemium grand public | Agriculteurs individuels | Faible — prix très sensible, outils gratuits DDT concurrents |
| Abonnement B2B | Coopératives / cabinets conseil agricole | Moyen — mais les coopératives commandent du sur-mesure |
| Prestation diagnostic territorial | Chambres d'agriculture / EPCI ruraux | Budget public incertain, marché ponctuel |
| API data | Agrégateurs (Geofolia, AgroEDI) | Possible mais niche très petite |

**Contrainte** : l'agriculteur français médian est réticent à payer pour des données
publiques qu'il peut obtenir gratuitement sur Géoportail + Géorisques. Le payeur B2B
(coopérative) commande du sur-mesure plutôt que du SaaS horizontal.

## 8. Risques

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Payeur absent / budget insuffisant | Très élevée | Éliminatoire | Entretiens de validation cible avant tout développement |
| GÉOPERSO / Géofoncier étend sa couverture agricole | Élevée | Élevé — concurrent établi | Différenciation UX ou niche sectorielle |
| DDT publie des cartes nationales unifiées (Géoportail) | Moyenne | Élevé — gratuit public direct | Surveillance réglementaire |
| Qualité jointure RPG ↔ PCI parcellaire variable | Moyenne | Moyen — données incomplètes | Test sur département pilote |
| Quotas API Géorisques (10 req/s) | Structurel | Moyen si scale | Cache local + ingestion batch ICPE shapefile |

**Point éliminatoire potentiel** : si aucune cible ne manifeste une willingness-to-pay
claire lors des entretiens utilisateurs, l'idée reste un beau projet SIG sans modèle économique.

## 9. Effort MVP

**Périmètre minimal crédible** :

1. Ingestion RPG (GeoJSON département test) + couche ICPE Géorisques (shapefile) dans PostGIS
2. Calcul ST_DWithin : parcelles RPG à < 500 m / 1 km d'une ICPE
3. Jointure Hub'Eau stations qualité eau dans le bassin versant
4. Croisement GPU/PLU WFS pour zonage constructible
5. Affichage carte leaflet + fiche parcelle (surface, cultures historiques, ICPE proches, stations eau)

**Estimation** : 2–3 semaines développement (1 département test) — données disponibles,
pas de jointure adresse complexe.

**Pré-requis bloquant** : valider qu'au moins une coopérative, chambre d'agriculture ou
SAFER accepte de tester et potentiellement payer avant de développer.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 |
| C4 | Espace concurrentiel libre | 2 | 2 | 4 |
| C5 | Différenciation défendable | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 3 | 6 |
| C8 | Maîtrise des risques | 2 | 3 | 6 |
| C9 | Monétisation / impact | 2 | 2 | 4 |
| | **Total** | | | **59 / 105** |

**Score /100** : `59 / 105 × 100` = **56**

**Justifications** :
- C1=3 : douleur diffuse — les acteurs individuels la contournent avec des outils gratuits.
  La douleur est plus forte pour les coopératives (due diligence) mais reste fragmentée.
- C2=2 : payeur flou. Agriculteurs = faible budget SaaS. Coopératives = sur-mesure.
  Chambres = budget public aléatoire. Aucun segment clairement solvable identifié.
- C3=4 : RPG (juin 2026), Géorisques, Hub'Eau, GPU tous ouverts et opérationnels.
  Jointure spatiale bien documentée.
- C4=2 : GÉOPERSO, Géofoncier, Terravisu/coopératives, DDT gratuit — marché couvert
  en plusieurs segments.
- C5=2 : données toutes publiques, croisement reproductible rapidement. Pas de moat.
- C6=4 : architecture PostGIS + SQL spatial traçable, LLM uniquement pour réglementation.
- C7=3 : MVP technique faisable en 2-3 semaines sur 1 département. Données disponibles.
- C8=3 : risque principal non technique (payeur absent) ; risques data gérables.
- C9=2 : ni revenu clair ni impact fort autonome identifié. Modèle public possible mais
  fragile ; modèle commercial bloqué par la gratuité des outils concurrents.

## 11. Verdict & décision

🔁 **À retravailler** — score **56/100**

**Atouts** : croisement techniquement solide et faisable (sources vérifiées, PostGIS),
MVP réalisable en 2–3 semaines, données fraîches (RPG juin 2026, Hub'Eau opérationnel).

**Point bloquant principal** : **payeur non identifié**. Les agriculteurs ne paient pas pour
des données publiques disponibles gratuitement (Géoportail, Géorisques, cartes DDT).
Les coopératives commandent du sur-mesure (Terravisu/SeineYonne). Les chambres d'agriculture
dépendent de budgets publics aléatoires. GÉOPERSO couvre déjà les professionnels fonciers
agricoles avec RPG × contraintes environnementales.

**Pour débloquer** :
1. Conduire 5–10 entretiens (SAFER, coopératives, chambres d'agriculture) pour identifier
   une douleur suffisamment forte et une willingness-to-pay.
2. Si une coopérative ou chambre est prête à co-financer un pilote → prototype sur
   1 département (ex. Vendée ou Gers) avec validation de valeur.
3. Si aucun payeur identifié → écarter. La beauté technique ne suffit pas.

**Lien avec d'autres idées** : [0021](../0021-veille-fonciere-amenageurs/) (foncier, écarté 50/100)
et [0011](../0011-risques-adresse/) (risques unitaires, à retravailler 60/100) confirment
que le croisement données-risques sans canal de distribution est systématiquement sous le seuil Go.
