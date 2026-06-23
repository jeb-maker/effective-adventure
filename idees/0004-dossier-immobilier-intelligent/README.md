# Dossier immobilier intelligent (DVF enrichi)

- **ID** : 0004
- **Statut** : ❌ Écartée
- **Score** : — / 100 (écartée sur critère éliminatoire : saturation)
- **Dernière mise à jour** : 2026-06-20
- **Pitch (1 phrase)** : Un « dossier d'achat » par bien (DVF + DPE + risques +
  PLU + bruit + transport + fiscalité + résumé IA).

---

## 1. Problème / douleur
Forte (72 % des Français veulent connaître les prix de vente de leur quartier),
mais largement adressée.

## 4. Existant / concurrence (saturé)
- Explorateur DVF officiel — https://explore.data.gouv.fr/fr/immobilier
- Immo Data (carte) — https://www.data.gouv.fr/reuses/immo-data-toutes-les-ventes-dvf-sur-une-carte
- Carte Prix Immobilier, applis Android cadastre/DVF/DPE/PLU,
  Baromètre Stop Loyer (prix m², loyers, PTZ). (Consultés 2026-06-20.)

## 11. Verdict & décision
❌ **Écartée** (pour un premier projet). La carte DVF est un commodity. Le seul
angle survivant serait le « dossier d'achat » agrégé multi-sources, mais déjà
attaqué par des applis matures. Faible ROI face à l'effort. À ne reconsidérer que
sur une niche très précise.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0004-dossier-immobilier-intelligent` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `real-estate-proptech` — Immobilier & proptech

Fichier : [`catalogue-saas/vendors/real-estate-proptech.json`](../../catalogue-saas/vendors/real-estate-proptech.json) (15 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `costar` | CoStar | US | partial | partial |
| `yardi` | Yardi | US | partial | partial |
| `procore` | Procore | US | partial | partial |
| `matera` | Matera | FR | strong | partial |
| `pricehubble` | PriceHubble | CH | partial | partial |
| `scanreno` | ScanReno | FR | strong | partial |
| `powimo` | Powimo | FR | strong | partial |
| `egide-copro` | EGIDE Copro | FR | strong | partial |
| `copro-solutions` | CoproSolutions | FR | strong | partial |
| `bdnb` | BDNB (CSTB) | FR | strong | partial |
| `kel-foncier` | Kel Foncier | FR | strong | partial |
| `deepki` | Deepki | FR | strong | partial |
| … | _+3 autres_ | | | |

#### Segment `geospatial-gis-fr` — Géospatial & carto FR

Fichier : [`catalogue-saas/vendors/geospatial-gis-fr.json`](../../catalogue-saas/vendors/geospatial-gis-fr.json) (16 entrées)

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
| … | _+4 autres_ | | | |

#### Segment `document-idp` — IDP & extraction documentaire

Fichier : [`catalogue-saas/vendors/document-idp.json`](../../catalogue-saas/vendors/document-idp.json) (48 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `google-document-ai` | Google Cloud Document AI | US | partial | verified |
| `aws-textract` | AWS Textract | US | partial | partial |
| `azure-document-intelligence` | Azure AI Document Intelligence | US | partial | partial |
| `nanonets` | Nanonets | US | partial | verified |
| `extend-ai` | Extend AI | US | partial | verified |
| `docupipe` | DocuPipe | unknown | unknown | verified |
| `sensible` | Sensible | US | partial | verified |
| `docsumo` | Docsumo | US | partial | partial |
| `rossum` | Rossum | US | partial | verified |
| `snapparse` | Snapparse | unknown | unknown | verified |
| `iteration-layer` | Iteration Layer | US | partial | verified |
| `docld` | DocLD | unknown | unknown | verified |
| … | _+36 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment real-estate-proptech
```

<!-- catalogue-saas-end -->
