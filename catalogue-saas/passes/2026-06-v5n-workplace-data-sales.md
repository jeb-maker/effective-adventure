# Passe V5n — workplace / data / sales

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5n-workplace-data-sales` |
| Date | 2026-06-23 |

## Enrichissement catalogue

| Segment | Cible | Ajoutés | Exemples |
|---|---|---:|---|
| `crm-platforms` | +5–7 | +6 | Dynamics 365 Sales, Freshsales, Close, Copper, Zendesk Sell |
| `marketing-automation` | +5–7 | +6 | Klaviyo, Braze, Iterable, lemlist, Drip |
| `revenue-intelligence` | +5–7 | +6 | Revenue.io, Scratchpad, Winn.ai, Aviso, Oliv AI |
| `seo-content-ai` | +5–7 | +6 | Semrush, Ahrefs, Frase, Scalenut, Neuroflash |
| `customer-success` | +5–7 | +6 | Vitally, Custify, Rocketlane, Churnkey, Strikedeck |
| `helpdesk-platforms` | +5–7 | +6 | Zendesk, Intercom, ServiceNow CSM, Gorgias |
| `e-signature` | +5–7 | +6 | Signaturit, Universign, SignNow, GetAccept, Concord |
| `translation-localization` | +5–7 | +6 | Transifex, Weglot, Smartcat, POEditor, Gridly |
| `data-integration-etl` | +5–7 | +6 | Matillion, Talend Cloud, Dagster, Census, Portable |
| `data-enrichment-b2b` | +5–7 | +6 | 6sense, Demandbase, Cognism, RocketReach, Dealfront |
| `bi-analytics-platforms` | +5–7 | +6 | Qlik Sense, Domo, Sisense, Metabase, Hex, Sigma |
| `data-observability` | +5–7 | +6 | Bigeye, Elementary, Sifflet, Datafold, lakeFS |
| `rag-knowledge` | +5–7 | +6 | Onyx, kapa.ai, Ragie, Guru, Elastic Enterprise Search |
| `ai-productivity` | +5–7 | +6 | Motion, Reclaim.ai, Tango, Beautiful.ai, Tome, Mem |
| `project-work-management` | +5–7 | +6 | Smartsheet, Basecamp, Height, Teamwork, Airtable |
| `meeting-intelligence` | +5–7 | +6 | tl;dv, Sembly, Supernormal, MeetGeek, Krisp |
| `rpa-enterprise` | +5–7 | +6 | Kryon, Pega, Robocorp, Appian RPA, NICE RPA |
| `spend-procurement` | +5–7 | +6 | SAP Ariba, Ivalua, JAGGAER, GEP SMART, Zycus |

**Total visé** : +108 vendeurs. Skip doublons : Yousign, DocuSign, PandaDoc déjà présents (`e-signature`). Patch cross-segment : Laiye → `rpa-enterprise`.

Focus : acteurs sales/data/workplace avec couverture EU/FR quand pertinent ; `verification_status: partial` minimum.

## Scripts

```bash
python3 scripts/enrich_catalogue_v5n.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation
```
