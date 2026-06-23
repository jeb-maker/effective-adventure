# Passe V5l — sécurité, KYC/AML et infra IA

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5l-security-kyc-infra` |
| Date | 2026-06-23 |

## Enrichissement catalogue

| Segment | Cible | Ajoutés | Exemples |
|---|---|---:|---|
| `kyc-aml` | +5–8 | +8 | Ubble, Veriff, IDnow, Persona, Dotfile, Salv |
| `cybersecurity-platforms` | +5–8 | +6 | Elastic Security, Arctic Wolf, HarfangLab, Sekoia |
| `identity-access-management` | +5–8 | +6 | Auth0, Keycloak, Wallix, CyberArk, Ping Identity |
| `cloud-security-cspm` | +5–8 | +6 | Datadog CSPM, Sysdig, Netskope, Bridgecrew |
| `email-security` | +5–8 | +6 | Vade, Tessian, IRONSCALES, Cofense, Cloudflare |
| `vulnerability-management` | +5–8 | +6 | Greenbone, Intruder, runZero, Hadrian |
| `llm-api-providers` | +5–8 | +6 | Aleph Alpha, AI21, DeepSeek, Fireworks, Groq |
| `model-inference-hosting` | +5–8 | +6 | Baseten, Anyscale, RunPod, Scaleway Generative APIs |
| `vector-databases` | +5–8 | +5 | pgvector, Redis Vector, MongoDB Atlas, Turbopuffer |
| `ai-evals-testing` | +5–8 | +6 | Arize Phoenix, Helicone, DeepEval, Ragas, W&B Weave |
| `agent-frameworks-platforms` | +5–8 | +6 | Dify, Flowise, Agno, Langflow, AgentOps |

**Total visé** : +67 vendeurs. Patches cross-segment : Wiz → cyber, Mistral → inference, Dust/n8n → agents, Snyk → CSPM/vuln, Fireworks/Groq/Scaleway multi-segment.

Focus moisson : acteurs **HQ FR** (Ubble, HarfangLab, Sekoia, Wallix, Vade, Dotfile, Scaleway) avec `france_market=strong` ; lien idée **0029 RecordAI KYC lite**.

## Contexte idées

- [`idees/0029-recordai/README.md`](../../idees/0029-recordai/README.md) — parsing inbox, IDP, conformité spec, KYC lite
- [`idees/0022-due-diligence-tiers/README.md`](../../idees/0022-due-diligence-tiers/README.md) — KYC/AML tiers

## Scripts

```bash
python3 scripts/enrich_catalogue_v5l.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation
```
