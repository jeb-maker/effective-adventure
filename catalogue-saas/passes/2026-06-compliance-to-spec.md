# Passe L3 — `compliance-to-spec`

| Champ | Valeur |
|---|---|
| Segment | `compliance-to-spec` |
| Niveau visé | **L3** (quasi-exhaustif) |
| `discovery_pass` | `2026-06-v5b-compliance-to-spec` |
| Date | 2026-06-22 |

## Objectif

Cartographier les acteurs qui traduisent exigences réglementaires / frameworks en **specs testables**, policies-as-code ou artefacts d'engineering — au-delà du GRC classique.

## Sources consultées

| Source | URL / requête | Candidats bruts | Nouveaux ajoutés |
|---|---|---:|---:|
| official_site | Sites produits (OPA, Styra, Pulumi, Probo…) | 14 | 5 |
| g2 | Catégorie GRC / compliance automation | 28 | 6 |
| capterra | Compliance automation, policy management | 15 | 2 |
| crunchbase | Tags compliance automation, policy-as-code | 12 | 2 |
| analyst_report | Comparatifs GRC/compliance-as-code 2025-2026 | 8 | 2 |
| alternatives | « OPA alternatives », « Vanta alternatives » | 10 | 3 |
| open_source | OPA, Sentinel, Cedar, Probo, CtA | 9 | 4 |
| geo_digest | — | — | — |

## Résultats

- **+14 vendeurs** ajoutés dans `vendors/compliance-to-spec.json`
- **5 patches** cross-segments : Vanta, Drata, LogicGate, ModelOp, Credo AI
- Total segment après passe : **24 vendeurs**
- Acteur HQ France identifié : **Probo** (`france_market: strong`)

## Saturation (estimée)

- Candidats bruts consolidés : ~96
- Nouveaux uniques : 14
- Taux : ~14,6 % → **passe non saturée** (seuil 5 % non atteint côté « gel »)

Sources encore à passer : `geo_digest` (EU startups), approfondissement `crunchbase` (seed–B), listes GitHub awesome-policy-as-code.

## Filtres disruption

```bash
python3 scripts/catalogue_saas.py gaps --segment compliance-to-spec
python3 scripts/catalogue_saas.py gaps --segment compliance-to-spec --france-market absent
```

Segments proches à croiser : `grc-security`, `ai-governance`, `regtech`.

## Script

```bash
python3 scripts/enrich_compliance_to_spec_v5b.py
```
