# Passe V6g — verified segments + §4 idées ❌ complètes

- **Pass ID** : `2026-06-v6g-verified-section4-ecartees`
- **Date** : 2026-06-23
- **Scripts** : `scripts/enrich_catalogue_v6g.py` + fiches `idees/*/README.md`

## Partie A — Catalogue (+3, verified +18)

### Ajouts

| ID | Segment |
|---|---|
| `data-emploi-francetravail` | territorial-analytics (**verified**) |
| `eclaireur-public` | territorial-analytics, public-procurement-intel |
| `coproff-cerema` | energy-buildings-fr, real-estate-proptech |

### Promotions verified

- **energy-buildings-fr** : go-renove-pro, heero, openmeti, hellowatt, enoptea, metron
- **environmental-data-fr** : atmo-france, hub-eau, georisques-api
- **geospatial-gis-fr** : geoperso, alkante
- **territorial-analytics** : vigicite
- **listicle fix** : modulos, kla-digital ; arthur-ai, modelop, atlan, onetrust (URL officielle)

## Partie B — §4 idées ❌ (14 fiches)

Toutes les idées **❌ Écartées** ont reçu :
- `### Services publics / .gouv.fr`
- `### Réutilisations data.gouv`

**Résultat** : `check_idees.py` → **0 alerte §4** sur 29/29 fiches.

## Prochaine passe V6h

- Listicle restants (~25) : grc-security, compliance-to-spec
- Entrées catalogue : Terravisu, Urbaa.app, MCP data.gouv (réutilisations 0003)

```bash
python3 scripts/enrich_catalogue_v6g.py
python3 scripts/check_idees.py --strict
python3 scripts/catalogue_saas.py stats | grep verified
```
