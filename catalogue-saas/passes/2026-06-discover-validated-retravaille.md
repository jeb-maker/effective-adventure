# Passe discover — pipeline test 2026-06-23

- **Pass ID** : `2026-06-discover-validated-retravaille`
- **Date** : 2026-06-23
- **Pipeline** : `catalogue_discover run` → curation → `catalogue_pass run` → `weekly promote`

## Découverte auto (7 segments 🔁)

Dossier : `catalogue-saas/passes/discover-2026-06-23/`

| Segment | Candidats data.gouv bruts | Retenu après curation |
|---|---|---|
| territorial-analytics | 10 | 3 |
| energy-buildings-fr | 3 | 3 |
| open-data-governance-fr | 0 | 1 (Sirene) |
| geospatial-gis-fr | 2 | 0 (jeux locaux) |
| public-procurement-intel | 1 | 0 (agglo locale) |
| environmental-data-fr | 0 | 0 |
| hr-talent-ai | 0 | 0 |

**Rejetés** : jeux open data locaux (agglo Saintes, Grand Poitiers, SQY…) — hors périmètre catalogue produit.

## Ajouts validés (+10)

| ID | Segments | Statut |
|---|---|---|
| `aides-territoires` | territorial-analytics, civic-tech-fr | verified |
| `territoires-fertiles` | territorial-analytics, environmental-data-fr | partial |
| `agence-ore-consommation-commune` | territorial-analytics, energy-buildings-fr | verified |
| `api-dpe-logements-ademe` | energy-buildings-fr | verified |
| `observatoire-dpe-passoires-ademe` | energy-buildings-fr, real-estate-proptech | verified |
| `api-imope-urbs` | energy-buildings-fr, real-estate-proptech | partial |
| `api-sirene-insee` | open-data-governance-fr, data-enrichment-b2b | verified |
| `limnos` | parsing-inbox, document-idp, automation-platforms | verified |
| `orderscan` | parsing-inbox, document-idp | verified |
| `hellio-copropriete` | real-estate-proptech, energy-buildings-fr | verified |

## Promotion auto (+15 weekly)

Pass `auto-weekly-discover-2026-06-23` sur segments 🔁.

## Métriques

| Métrique | Avant | Après |
|---|---|---|
| Vendeurs | 1 448 | **1 458** |
| Verified | 168 | **192** |
| Listicle | 0 | **0** |

## Correctif discover

`catalogue_discover.py` : extraction URL dataservices (`business_documentation_url`, `base_api_url`).

## Validation

```bash
python3 scripts/catalogue_discover.py run --retravailler --limit 7 --manifest
python3 scripts/catalogue_pass.py run catalogue-saas/passes/2026-06-discover-validated-retravaille.manifest.json
python3 scripts/catalogue_pass.py weekly --limit 15
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py gate
```
