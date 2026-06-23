# Passe V5k — territoire idées 0025–0028

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5k-territoire-idees` |
| Date | 2026-06-23 |

## Enrichissement catalogue

| Segment | Cible | Ajoutés | Exemples |
|---|---|---:|---|
| `real-estate-proptech` | +8–10 | +10 | ScanReno, Powimo, BDNB, Deepki, Kel Foncier |
| `energy-buildings-fr` | +8–10 | +9 | Hello Watt, Enoptea, Cantine Énergétique, Go Rénove PRO |
| `territorial-analytics` | +8–10 | +10 | Smappen, Geomarket, Data-B, VigiCité, LocalNova |
| `public-procurement-intel` | +6–8 | +7 | decp.info, OpenBar, Nextend.ai, DoubleTrade |
| `hr-talent-ai` | +8–10 | +9 | Talentsoft, Lucca, JobTeaser, Beetween, Lightcast |
| `geospatial-gis-fr` | +6–8 | +7 | GÉOPERSO, Makina Corpus, GPU, Geofolia, RPG |
| `environmental-data-fr` | +6–8 | +7 | Sandre, DRIAS, BASOL, GASPAR, PREV'AIR |

**Total visé** : +59 vendeurs (skip doublons). Patches cross-segment : Deepki, BDNB, decp.info, France Travail/DARES, Lightcast, GÉOPERSO.

Focus moisson : acteurs **HQ FR** avec `france_market=strong` quand pertinent ; `verification_status: partial` minimum.

## Contexte idées

- [`idees/0025-coproprietes-renovation-rnic/README.md`](../../idees/0025-coproprietes-renovation-rnic/README.md) — RNIC × DPE × DECP copropriétés
- [`idees/0026-exposition-parcelles-agricoles/README.md`](../../idees/0026-exposition-parcelles-agricoles/README.md) — RPG × Géorisques × Hub'Eau
- [`idees/0027-transparence-subventions-marches/README.md`](../../idees/0027-transparence-subventions-marches/README.md) — DECP × SCDL × subventions
- [`idees/0028-tensions-emploi-territoire/README.md`](../../idees/0028-tensions-emploi-territoire/README.md) — tension emploi × territoire

## Scripts

```bash
python3 scripts/enrich_catalogue_v5k.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation
```
