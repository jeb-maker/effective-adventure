# Passe V6i — Terravisu/h-genai + verified idées 🔁 + listicle zéro

- **Pass ID** : `2026-06-v6i-terravisu-retravaille-verify`
- **Date** : 2026-06-23
- **Scripts** : `scripts/enrich_catalogue_v6i.py` + `scripts/catalogue_saas.py` (audit listicle)

## Ajouts catalogue (+2)

| ID | Segment | Statut |
|---|---|---|
| `terravisu` | geospatial-gis-fr, environmental-data-fr | **verified** |
| `h-genai` | open-data-governance-fr, territorial-analytics, rag-knowledge | partial (OSS) |

## Promotions verified (+17)

### Listicle résiduel V6h (2)
- `windsurf` → windsurf.com/pricing
- `salesforce-agentforce` → salesforce.com/agentforce/pricing

### Segments idées 🔁 (15)

| Idée | Vendeurs promoted |
|---|---|
| 0001 | decp-info, openmarches, doaken |
| 0009 | cantine-energetique, spigao |
| 0025 | copro-solutions, matera, scanreno |
| 0026 | makina-corpus, geofolia |
| 0028 | eclaireur-public |
| 0029 | ubble, dotfile, ondorse, lemonway-kyc |

## Correctif audit listicle

`is_listicle_source()` ignore désormais les sources dont le domaine correspond au produit (`domains_match`) — élimine les faux positifs modulos.ai / pickaxe.co.

## Métriques après passe

| Métrique | V6h | V6i |
|---|---|---|
| Vendeurs | 1 446 | **1 448** |
| Verified | 151 | **168** |
| Listicle-sourced | 4 | **0** |

## Validation

```bash
python3 scripts/enrich_catalogue_v6i.py
python3 scripts/catalogue_saas.py validate          # OK — 1448 vendeurs
python3 scripts/catalogue_saas.py audit-sources     # 0 listicle
python3 scripts/check_idees.py --strict             # 29/29 revues, 0 alerte §4
```

## Suite V6j

- Poursuite `verify-eligible` sur segments 🔁 (94 candidats FR strong restants)
- Entrées manquantes citées revues : Limnos.app, OrderScan (0029), Hellio CoproSolutions
- Décision produit (pivot 0001/0029/0025) — hors scope cartographie
