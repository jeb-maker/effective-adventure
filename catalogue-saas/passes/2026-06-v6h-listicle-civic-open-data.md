# Passe V6h — civic/open-data MCP + nettoyage listicles

- **Pass ID** : `2026-06-v6h-listicle-civic-open-data`
- **Date** : 2026-06-23
- **Script** : `scripts/enrich_catalogue_v6h.py`

## Ajouts catalogue (+3)

| ID | Segment | Statut |
|---|---|---|
| `urbaa` | civic-tech-fr, territorial-analytics, open-data-governance-fr | **verified** |
| `datagouv-mcp` | open-data-governance-fr, territorial-analytics, agent-frameworks-platforms | **verified** |
| `france-data-mcp` | open-data-governance-fr, territorial-analytics | partial (OSS) |

**Liens idées** : Urbaa + MCP data.gouv cités idée 0003 ; france-data-mcp cité 0003/0006.

## Promotions verified (+25 listicle cleanup)

| Source listicle | Vendeurs |
|---|---|
| riskpublishing.com | hyperproof, onspring, navex, diligent, metricstream-reg |
| v-comply.com | secureframe, vanta, drata, scytale, vcomply |
| modulos.ai/best | servicenow-grc, ibm-openpages, collibra |
| pickaxe.co | pickaxe, sierra, 11x, decagon |
| zylos.ai | cursor, windsurf, claude-code |
| trustible.ai | trustible |
| extend.ai | sensible |
| helply.com | zendesk-ai, forethought, hubspot-breeze |

## Métriques après passe

| Métrique | Avant (V6g) | Après (V6h) |
|---|---|---|
| Vendeurs | 1 443 | **1 446** |
| Verified | 128 | **151** |
| Listicle-sourced | 27 | **4** |

## Listicles résiduels (4)

- `windsurf` — source devin.ai (blog pricing officiel Cognition)
- `modulos` — source modulos.ai (site éditeur)
- `salesforce-agentforce` — aimagicx.com
- `pickaxe` — pickaxe.co/pricing (page tarifs éditeur)

→ Passe **V6i** : aimagicx + vérifier si devin.ai/modulos/pickaxe.co restent flaggés à tort.

## Validation

```bash
python3 scripts/enrich_catalogue_v6h.py
python3 scripts/catalogue_saas.py validate          # OK — 1446 vendeurs
python3 scripts/catalogue_saas.py audit-sources     # 4 listicle
python3 scripts/check_idees.py --strict           # 29/29 revues, 0 alerte §4
```
