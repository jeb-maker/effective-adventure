# Passe V5s — L3 cartographie stack IA

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5s-ai-stack-l3` |
| Date | 2026-06-23 |
| Niveau visé | L3 (stack IA agents, voix, RAG, copilots) |

## Enrichissement catalogue

| Segment | Avant | Cible | Ajoutés | Exemples |
|---|---:|---:|---:|---|
| `ai-governance` | 33 | +10 | +10 | Zama, Giskard, Saidot, CalypsoAI, Deeploy, DataRobot AI Governance |
| `support-sales-agents` | 21 | +8 | +8 | Moveworks, Netomi, Boost.ai, CallDesk, Dydu, ServiceNow Now Assist |
| `voice-speech-ai` | 11 | +8 | +8 | Voxygen, Acapela, Gladia, Vocapia, Rev.ai, Murf, Resemble AI |
| `rag-knowledge` | 11 | +8 | +8 | deepset, Hebbia, Sana, Perplexity Enterprise, Kendra, Algolia NeuralSearch |
| `ai-copilot-dev` | 11 | +8 | +8 | Sourcegraph Cody, Continue, Codeium, Qodo, Augment Code, Poolside |

**Total** : +42 vendeurs. Exclus (déjà catalogués) : Holistic AI, Credo AI, Fairly, Decagon, Sierra, Ada, Forethought, Glean, Coveo, Onyx, Dust, Cursor, Tabnine.

## Patches cross-segment

| Vendeur | Segments ajoutés |
|---|---|
| Giskard | `ai-evals-testing` |
| Zama | `compliance-to-spec` |
| Moveworks | `rag-knowledge` |
| Boost.ai, CallDesk | `voice-speech-ai` |
| deepset | `agent-frameworks-platforms` |
| ServiceNow Now Assist | `helpdesk-platforms`, `automation-platforms` |
| Perplexity Enterprise | `ai-productivity` |
| Resemble AI | `support-sales-agents` |
| LangSmith, Guardrails AI | `ai-governance` (renfort) |
| Arize AI | `ai-evals-testing` |

Focus moisson : **HQ FR** sur gouvernance IA (Zama, Giskard), voix (Voxygen, Acapela, Gladia, Vocapia), agents support (CallDesk, Dydu) ; **EU AI Act** (Saidot, Deeploy, EQTY Lab).

## Sources consultées

| Source | Segments | Candidats bruts | Nouveaux |
|---|---|---:|---:|
| g2 | ai-governance, support, voix, RAG, copilots | 178 | 16 |
| geo_digest | ai-governance, support, voix, RAG | 94 | 11 |
| analyst_report | ai-governance, support, RAG, copilots | 98 | 8 |
| crunchbase | ai-governance, support, voix, RAG, copilots | 86 | 7 |
| official_site | support, voix, RAG, copilots | 60 | 4 |
| alternatives | ai-copilot-dev | 24 | 2 |
| open_source | ai-copilot-dev | 12 | 1 |

## Gaps HQ FR (avant → après)

| Segment | hq_FR avant | Acteurs FR ajoutés |
|---|---:|---|
| `ai-governance` | 0 | Zama, Giskard |
| `support-sales-agents` | 0 | CallDesk, Dydu |
| `voice-speech-ai` | 0 | Voxygen, Acapela, Gladia, Vocapia |
| `rag-knowledge` | 1 | Algolia NeuralSearch (HQ Paris) |
| `ai-copilot-dev` | 0 | — (pas de copilot dev HQ FR identifié) |

## Scripts

```bash
python3 scripts/enrich_catalogue_v5s.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation
python3 scripts/catalogue_saas.py gaps --segment ai-governance
```
