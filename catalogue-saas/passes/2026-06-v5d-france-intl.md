# Passe V5d — équivalents internationaux `france-public` + `france-open-data`

| Champ | Valeur |
|---|---|
| Segments | 10 segments France (secteur public + open data) |
| Objectif | Benchmark hors France — modèles UK, EU, US, DE |
| `discovery_pass` | `2026-06-v5d-france-intl` |
| Date | 2026-06-22 |

## Principe

Les entrées ajoutées sont des **équivalents internationaux** pour comparer modèles produit, open data et gouvernance — pas des concurrents directs sur le marché français. Champ `notes` : « Équivalent international pour benchmark ».

## Résultats

| Segment | Ajoutés | Exemples |
|---|---:|---|
| `public-procurement-intel` | +4 | Tussell (UK), GovWin (US), Open Contracting |
| `territorial-analytics` | +4 | data.gov.uk, ONS, Eurostat, CARTO |
| `civic-tech-fr` | +5 | CitizenLab (BE), CONSUL (ES), Commonplace (UK) |
| `geospatial-gis-fr` | +4 | Ordnance Survey, Esri, Mapbox, HERE |
| `transport-mobility-data-fr` | +4 | TfL Open Data, MobilityData, Transitland |
| `energy-buildings-fr` | +4 | UK EPC, DOE BPD, dena (DE), gridX |
| `environmental-data-fr` | +4 | UK EA, EEA, Copernicus, US EPA |
| `electoral-data-fr` | +4 | UK Electoral Commission, MIT Election Lab |
| `public-health-territory-fr` | +4 | NHS Digital, CDC PLACES, WHO GHO |
| `open-data-governance-fr` | +4 | Socrata, CKAN, ArcGIS Hub, Data.gov US |

**Total : +41 équivalents internationaux**

## Tagging géo

- `hq_country` : GB, US, EU, DE, BE, ES, AU, CH, NL…
- `france_market` : majoritairement `absent` ou `partial` (portails EU)
- `discovery_source` : `geo_digest`, `official_site`, `g2`…

## Filtres utiles

```bash
python3 scripts/catalogue_saas.py gaps --segment civic-tech-fr
python3 scripts/catalogue_saas.py gaps --segment open-data-governance-fr --hq US
python3 scripts/catalogue_saas.py export -o catalogue-saas/exports/vendors.csv
```

## Script

```bash
python3 scripts/enrich_catalogue_v5d.py
```

## Suite (V5e)

Long tail + revue trimestrielle ; saturation L2 sur segments globaux restants.
