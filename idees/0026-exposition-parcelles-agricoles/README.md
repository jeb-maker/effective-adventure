# Exposition risques des parcelles agricoles (RPG × Géorisques × Hub'Eau)

- **ID** : 0026
- **Statut** : 💡 Capturée
- **Score** : — / 100 (à analyser)
- **Dernière mise à jour** : 2026-06-21
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

## 4. Existant / concurrence (première passe)

- **Géoportail, Géorisques** : consultation unitaire, pas fiche parcelle agricole
- **Kel Foncier / Géofoncier** : foncier BTP, pas angle agricole/RPG
- **Télépac / RPG** (portail agriculteur) : déclaration PAC, pas croisement risques
- **À creuser** : outils chambres d'agriculture, SIG internes DDT

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0026-exposition-parcelles-agricoles` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-22 — ne pas utiliser les entrées `unverified` pour scorer.

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

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment geospatial-gis-fr
```

<!-- catalogue-saas-end -->
## 6. Faisabilité & fiabilité technique

- Stack : PostGIS (RPG + PCI + couches Géorisques en shapefile) + appels Hub'Eau
  pour stations à proximité.
- Chiffres (surface, nb ICPE, distance) = **SQL/spatial traçable**.
- LLM : explication réglementaire ICPE / zonage PLU uniquement.

## 11. Verdict & décision

💡 **Capturée** — croisement **techniquement solide** (sources vérifiées ouvertes),
payeur incertain. Lien avec [0021](../0021-veille-fonciere-amenageurs/) (foncier)
et [0011](../0011-risques-adresse/) (risques unitaires).

**Prochaine étape** : prototype spatial sur 1 département (ex. test RPG GeoJSON +
couche ICPE) pour mesurer temps de calcul et valeur perçue par une chambre d'agriculture.
