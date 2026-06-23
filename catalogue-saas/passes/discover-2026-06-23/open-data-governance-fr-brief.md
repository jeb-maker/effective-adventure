# Brief découverte — `open-data-governance-fr`

- **Date** : 2026-06-23
- **Label** : Gouvernance open data FR
- **Description** : Conformité publication, qualité jeux de données collectivités.
- **Catalogue** : 24 acteurs (4 verified, 20 partial)
- **Gelé** : non | **Lié idée 🔁** : oui
- **Sources coverage manquantes** : 2/8

## Acteurs déjà recensés (extrait)

- `arcgis-hub` — ArcGIS Hub (partial)
- `ckan` — CKAN (partial)
- `data-europa` — data.europa.eu (partial)
- `data-gov-us` — Data.gov (US) (partial)
- `data-publica` — Data Publica (partial)
- `dataclic` — DataClic (OpenDataFactory) (partial)
- `datactivist` — Datactivist (partial)
- `datagouv` — data.gouv.fr (verified)
- `datagouv-mcp` — data.gouv.fr MCP (officiel) (verified)
- `dkod` — DKOD (partial)
- `etalab-data-gouv` — Etalab / data.gouv.fr (partial)
- `fairness` — Fairness (partial)
- `france-data-mcp` — france-data-mcp (OSS) (partial)
- `h-genai` — h-genai (OSS) (partial)
- `huwise` — Huwise (ex-Opendatasoft) (partial)
- … +9 autres

## Recherches web à lancer (manuel ou agent)

- **g2** (qualité open data France) : https://www.g2.com/search?query=qualit%C3%A9%20open%20data%20France
- **capterra** (qualité open data France) : https://www.capterra.com/search/?search=qualit%C3%A9%20open%20data%20France
- **github** (qualité open data France) : https://github.com/search?q=qualit%C3%A9%20open%20data%20France&type=repositories
- **alternativeto** (qualité open data France) : https://alternativeto.net/browse/search/?q=qualit%C3%A9%20open%20data%20France
- **g2** (validation schéma data.gouv) : https://www.g2.com/search?query=validation%20sch%C3%A9ma%20data.gouv
- **capterra** (validation schéma data.gouv) : https://www.capterra.com/search/?search=validation%20sch%C3%A9ma%20data.gouv
- **github** (validation schéma data.gouv) : https://github.com/search?q=validation%20sch%C3%A9ma%20data.gouv&type=repositories
- **alternativeto** (validation schéma data.gouv) : https://alternativeto.net/browse/search/?q=validation%20sch%C3%A9ma%20data.gouv

## Scan automatisé data.gouv

```bash
python3 scripts/catalogue_discover.py scan open-data-governance-fr
python3 scripts/catalogue_discover.py scan open-data-governance-fr --manifest > candidates.json
```

## Checklist cartographie B (§4)

- [ ] Réutilisations data.gouv.fr
- [ ] Services publics / .gouv.fr
- [ ] Produits commerciaux FR/EU
- [ ] Open source / académique
- [ ] Bricolage (Excel, Zapier…)
