# Passe V5r — L3 France open data thématique

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5r-france-thematic-l3` |
| Date | 2026-06-23 |
| Niveau visé | L3 (9–10 → ~18 entrées/segment) |

## Enrichissement catalogue

| Segment | Avant | Cible | Ajoutés | Exemples FR |
|---|---:|---:|---:|---|
| `electoral-data-fr` | 9 | ~18 | +9 | Ballotage, Qomon, Politiciae, Explain, DigitaleBox |
| `open-data-governance-fr` | 9 | ~18 | +9 | Huwise, Validata, OpenDataFrance, Data Publica, schema.data.gouv.fr |
| `public-health-territory-fr` | 9 | ~18 | +9 | CartoSanté, Annuaire Santé, Maiia, Rézone CPTS, HealthData.gouv.fr |
| `transport-mobility-data-fr` | 9 | ~18 | +9 | Navitia, Geovelo, Karos, SNCF Open Data, Cerema Capamob |
| `civic-tech-fr` | 10 | ~18 | +8 | Civiliz, Neocity, Démarches simplifiées, WeGov, Place |
| `geospatial-gis-fr` | 15 | ~20 | +5 | GEOCLIP, QGIS, BAN, THEIA, API Carto IGN |
| `environmental-data-fr` | 16 | ~20 | +4 | Recosanté, ICPE Géorisques, mon-eau.com, Risqeo |

**Total visé** : +53 vendeurs. Patches cross-segment : Health Data Hub, OpenHealth, Medadom, Qare, ademe-data, georisques, datagouv, registre-perma.

Focus moisson : acteurs **HQ FR** prioritaires, SaaS/commercial + portails data ouverts ; `verification_status: partial` minimum.

## Contexte idées

- [`idees/0005-sante-environnement-local/README.md`](../../idees/0005-sante-environnement-local/README.md) — Recosanté, mon-eau.com
- [`idees/0011-risques-adresse/README.md`](../../idees/0011-risques-adresse/README.md) — Géorisques, BAN, Risqeo
- [`idees/0012-acces-aux-soins/README.md`](../../idees/0012-acces-aux-soins/README.md) — CartoSanté, Rézone, CRTOSanté
- [`idees/0013-choisir-son-ecole/README.md`](../../idees/0013-choisir-son-ecole/README.md) — territorial (indirect)
- [`idees/0014-analyse-electorale-fine/README.md`](../../idees/0014-analyse-electorale-fine/README.md) — Ballotage, Qomon, Politiciae
- [`idees/0015-deserts-de-mobilite/README.md`](../../idees/0015-deserts-de-mobilite/README.md) — Navitia, Cerema Capamob
- [`idees/0018-transparence-vie-publique/README.md`](../../idees/0018-transparence-vie-publique/README.md) — civic + électoral
- [`idees/0023-conformite-open-data-collectivites/README.md`](../../idees/0023-conformite-open-data-collectivites/README.md) — ODF, Validata, Huwise
- [`idees/0026-exposition-parcelles-agricoles/README.md`](../../idees/0026-exposition-parcelles-agricoles/README.md) — GEOCLIP, API Carto

## Scripts

```bash
python3 scripts/enrich_catalogue_v5r.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation
```
