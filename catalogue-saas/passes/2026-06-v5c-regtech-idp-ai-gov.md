# Passe L2/L3 — `regtech`, `document-idp`, `ai-governance`

| Champ | Valeur |
|---|---|
| Segments | `regtech`, `document-idp`, `ai-governance` |
| Niveau visé | **L2** (saturation multi-sources) |
| `discovery_pass` | `2026-06-v5c-regtech-idp-ai-gov` |
| Date | 2026-06-22 |

## Résultats par segment

| Segment | Avant | Ajoutés | Patches | Sources renseignées |
|---|---:|---:|---:|---:|
| `regtech` | 17 | +10 | +1 (ComplyAdvantage) | 7/8 |
| `document-idp` | 22 | +10 | — | 8/8 |
| `ai-governance` | 13 | +12 | — (OneTrust, Collibra déjà tagués) | 8/8 |

## Sources consultées (commun)

| Type | Rôle |
|---|---|
| `g2` | Listes catégories RegTech, IDP, AI Governance |
| `capterra` | Comparatifs produits et alternatives |
| `crunchbase` | HQ, funding, tags marché |
| `analyst_report` | IDC/Gartner/RegTech Analyst (2025-2026) |
| `alternatives` | Pages « X alternatives » |
| `open_source` | Frameworks guardrails, libs IDP |
| `official_site` | Pricing et docs produit |
| `geo_digest` | Acteurs EU (Alyne, Konfuzio, Mindee FR…) |

## Acteurs FR notables ajoutés

- **Mindee** (`document-idp`) — HQ FR, `france_market: strong`

## Saturation estimée

| Segment | Candidats bruts | Nouveaux | Taux | Gel ? |
|---|---:|---:|---:|---|
| regtech | ~162 | 10 | ~6 % | Non |
| document-idp | ~207 | 10 | ~5 % | Limite |
| ai-governance | ~156 | 12 | ~8 % | Non |

Revue complémentaire recommandée : `geo_digest` regtech (startups EU), long tail IDP APAC.

## Script

```bash
python3 scripts/enrich_catalogue_v5c.py
python3 scripts/catalogue_saas.py gaps --segment regtech
python3 scripts/catalogue_saas.py coverage
```
