# Dossier immobilier intelligent (DVF enrichi)

- **ID** : 0004
- **Statut** : ❌ Écartée
- **Score** : 53 / 100
- **Dernière mise à jour** : 2026-06-23
- **Révision critique** : voir [`revue.md`](revue.md) — écart **confirmé** et
  mieux étayé (score posé à **53/100**, < 55, + critère éliminatoire saturation).
  L'audit adversarial a trouvé un **clone quasi exact en production** : **Fonciris**
  (DVF + Géorisques + DPE + PLU + BDNB + SSMSI + ARCEP, aperçu 30 s, freemium +
  offre Pro marque blanche/API), que la §4 d'origine n'avait pas vu.
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

## 10. Scoring

> Tableau posé par la revue critique (la fiche écartait sans note). Notes adversariales.

| # | Critère | Poids | Note (1-5) | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 | Besoin réel et fréquent, mais ponctuel par acheteur. |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 | Acheteur paie une fois et au rabais ; payeur récurrent (agents) déjà capté. |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 | DVF/DPE/risques ouverts et prêts ; réserve : DVF semestriel, hors Alsace-Moselle. |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 | Saturé : Fonciris (clone exact) + Immo Data + MeilleursAgents + explorateur officiel. |
| C5 | Différenciation défendable | 2 | 1 | 2 | Données 100 % publiques aussi chez Fonciris ; aucun moat. |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 | Tabulaire → SQL traçable, LLM au résumé ; faisable. |
| C7 | Facilité du MVP | 2 | 3 | 6 | Agrégation multi-sources + géo non triviale mais balisée. |
| C8 | Maîtrise des risques | 2 | 2 | 4 | Saturation/prix non maîtrisés ; responsabilité du « verdict ». |
| C9 | Monétisation / impact | 2 | 2 | 4 | Monétisation compressée par le freemium d'un clone existant. |
| | **Total** | | | **56 / 105** | |

**Score /100** : 56 / 105 × 100 = **53**

## 11. Verdict & décision
❌ **Écartée** (pour un premier projet). La carte DVF est un commodity, **et** le
« dossier d'achat » agrégé multi-sources — le seul angle qu'on disait survivant —
est lui aussi un **produit fini et monétisé** : **Fonciris** (croise DVF +
Géorisques + DPE + PLU + BDNB + SSMSI + ARCEP, aperçu 30 s, freemium + Pro marque
blanche/API, consulté 2026-06-23). Score reconstruit **53/100** (< 55) **et**
critère éliminatoire de saturation → écart confirmé. Faible ROI face à l'effort.
À ne reconsidérer que sur une **niche verticale très précise** non couverte par
Fonciris, avec un payeur B2B clair.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0004-dossier-immobilier-intelligent` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `real-estate-proptech` — Immobilier & proptech

Fichier : [`catalogue-saas/vendors/real-estate-proptech.json`](../../catalogue-saas/vendors/real-estate-proptech.json) (20 entrées)

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
| … | _+8 autres_ | | | |

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

#### Segment `document-idp` — IDP & extraction documentaire

Fichier : [`catalogue-saas/vendors/document-idp.json`](../../catalogue-saas/vendors/document-idp.json) (60 entrées)

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
| … | _+48 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment real-estate-proptech
```

<!-- catalogue-saas-end -->
