# Passe V5t-c — L3 workplace / sales / data / infra

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5t-workplace-l3` |
| Date | 2026-06-23 |
| Niveau visé | L3 (20 segments workplace/sales/data/infra) |

## Enrichissement catalogue

| Segment | Avant | Après | Ajoutés | Exemples FR/EU |
|---|---:|---:|---:|---|
| `agent-frameworks-platforms` | 11 | 19 | +8 | Beam AI (DE) |
| `ai-evals-testing` | 11 | 18 | +7 | Langfuse (DE) |
| `ai-productivity` | 11 | 18 | +7 | — |
| `bi-analytics-platforms` | 11 | 18 | +7 | Pigment*, Toucan Toco* (FR) |
| `crm-platforms` | 11 | 19 | +8 | folk, Twenty, noCRM.io (FR) |
| `customer-success` | 11 | 19 | +8 | — |
| `data-enrichment-b2b` | 11 | 19 | +8 | Kaspr, Dropcontact, Datagma, Hunter.io (FR) |
| `data-integration-etl` | 11 | 18 | +7 | — |
| `data-observability` | 11 | 18 | +7 | Validio (SE) |
| `e-signature` | 11 | 18 | +7 | Certigna, LuxTrust (FR/LU) |
| `helpdesk-platforms` | 11 | 18 | +7 | Aircall, Ringover, Diabolocom (FR) |
| `llm-api-providers` | 11 | 18 | +7 | Mistral déjà catalogué |
| `marketing-automation` | 11 | 18 | +7 | Sarbacane, Splio, Mailjet (FR), Actito (BE) |
| `meeting-intelligence` | 11 | 18 | +7 | Jamie (DE) |
| `model-inference-hosting` | 11 | 18 | +7 | Nebius (EU), Scaleway déjà catalogué |
| `project-work-management` | 11 | 18 | +7 | — |
| `revenue-intelligence` | 11 | 18 | +7 | — |
| `rpa-enterprise` | 11 | 18 | +7 | SAP Build (DE), Laiye* |
| `seo-content-ai` | 11 | 18 | +7 | — |
| `spend-procurement` | 11 | 18 | +7 | Spendesk déjà catalogué ; Pleo, Payhawk (EU) |

\*Patch cross-segment (vendeur déjà présent). Pipedrive EU, Brevo, Spendesk, Pigment déjà en catalogue — non re-ajoutés.

**Total passe** : +144 vendeurs nouveaux. Exclus (déjà catalogués) : anecdotes, Perplexity, Ramp, Dust, n8n, deepset.

## Patches cross-segment

| Vendeur | Segments ajoutés |
|---|---|
| stack-ai | `agent-frameworks-platforms` |
| fiddler-ai, whylabs | `ai-evals-testing` / `data-observability` |
| pigment, toucan-toco | `bi-analytics-platforms` |
| prefect | `data-integration-etl` |
| atlan | `data-observability` |
| gladly, dixa | `helpdesk-platforms` |
| gong, otter-ai, chorus-ai | `meeting-intelligence` |
| microsoft-power-automate, laiye, automation-hero | `rpa-enterprise` |
| anecdotes | `data-observability` |

## Sources consultées

| Source | Segments | Candidats bruts | Nouveaux |
|---|---|---:|---:|
| g2 | 20 segments workplace/sales/data | ~520 | ~72 |
| geo_digest | CRM, helpdesk, marketing, enrichment FR | ~180 | ~28 |
| crunchbase | agents, evals, inference, CS | ~200 | ~22 |
| analyst_report | BI, RPA, CRM enterprise, e-sign EU | ~160 | ~18 |
| open_source | agents, ETL, BI | ~80 | ~4 |

## Gaps HQ FR (acteurs ajoutés)

| Segment | Acteurs FR/EU ajoutés |
|---|---|
| `crm-platforms` | folk, Twenty, noCRM.io |
| `data-enrichment-b2b` | Kaspr, Dropcontact, Datagma, Hunter.io |
| `helpdesk-platforms` | Aircall, Ringover, Diabolocom |
| `marketing-automation` | Sarbacane, Splio, Mailjet |
| `e-signature` | Certigna |
| `spend-procurement` | Pleo, Payhawk (EU) |

## Scripts

```bash
python3 scripts/enrich_catalogue_v5t_workplace.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation watch
python3 scripts/catalogue_saas.py gaps --segment crm-platforms
```
