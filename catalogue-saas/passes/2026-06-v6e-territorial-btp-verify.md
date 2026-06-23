# Passe V6e — réutilisations territoriales + BTP + verified/listicle

- **Pass ID** : `2026-06-v6e-territorial-btp-verify`
- **Date** : 2026-06-23
- **Script** : `scripts/enrich_catalogue_v6e.py`
- **Contexte** : piste **cartographie** (A + B) — suite analyse 0007

## Ajouts réutilisations territoriales (+3)

Cartographie B pour finances locales citoyennes (idée 0007, écartée) → entrées catalogue A :

| ID | Segment | Source |
|---|---|---|
| `orama-limited` | territorial-analytics | oramalimited.com |
| `habity` | territorial-analytics, energy-buildings-fr | habity.fr/methodologie |
| `depenses-publiques` | territorial-analytics, public-procurement-intel | depensespubliques.fr |

## Ajouts BTP / veille privée (+4)

| ID | Segment | Source |
|---|---|---|
| `mpf-france` | public-procurement-intel | mpfrance.fr |
| `spigao` | construction-proptech, public-procurement-intel | spigao.com |
| `prescriptio` | construction-proptech, territorial-analytics | prescriptio.fr (**verified**) |
| `bati-pulse` | construction-proptech | bati-pulse.com |

## Promotions verified / fix listicle (+7)

| ID | Segment | Action |
|---|---|---|
| `langsmith`, `fiddler-ai`, `arize-ai` | ai-governance | listicle → verified |
| `holistic-ai`, `ibm-watsonx-governance` | ai-governance | listicle → URL officielle |
| `geofoncier`, `ign-geoservices` | geospatial-gis-fr | verified (0026) |

## Prochaine passe V6f

- Compléter §4 des **7 idées 🔁** (sous-sections services publics / data.gouv)
- `verify-eligible` : ~20 promotions segments energy-buildings-fr, geospatial-gis-fr
- Listicle restants (~30) : regtech, ai-governance

```bash
python3 scripts/enrich_catalogue_v6e.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats | grep verified
```
