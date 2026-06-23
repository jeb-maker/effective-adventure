# Passe V6f — cartographie §4 des idées 🔁

- **Pass ID** : `2026-06-v6f-section4-retravaille`
- **Date** : 2026-06-23
- **Type** : cartographie B (§4 fiches) — pas de moisson catalogue

## Objectif

Compléter la checklist [`docs/cartographie-existant.md`](../docs/cartographie-existant.md) §2
sur les **7 idées 🔁** : sous-sections `###` + mots-clés `services publics` et `data.gouv`.

## Fiches mises à jour

| Idée | Changements §4 |
|---|---|
| **0001** | + Services publics (BOAMP, DECP, PLACE) ; + Réutilisations data.gouv (decp.info, OpenMarchés) |
| **0002** | + Services publics (Etalab, transport.data.gouv) ; + Réutilisations data.gouv (Validata, udata-hydra) |
| **0009** | Déjà conforme (`check_idees` OK) |
| **0025** | + Services publics (Go Rénove, CoproFF) ; + Réutilisations data.gouv (RNIC, DECP, RGE) |
| **0026** | + Services publics (Géoportail, Géorisques, GPU) ; + Réutilisations data.gouv (RPG, Hub'Eau) |
| **0028** | + Services publics (Data Emploi, France Travail) ; + Réutilisations data.gouv (SIRENE, APIs FT) |
| **0029** | + Services publics (API Entreprise, Chorus) ; + Réutilisations data.gouv (contexte KYC lite) |

## Contrôle

```bash
python3 scripts/check_idees.py --strict
python3 scripts/check_idees.py 2>&1 | grep -E "0001|0002|0025|0026|0028|0029"
```

## Prochaine passe V6g

- `verify-eligible` : energy-buildings-fr, geospatial-gis-fr (~15 promotions)
- §4 soft alerts sur idées ❌ restantes (14 fiches)
- Entrées catalogue : CoproFF, Data Emploi, Terravisu (réutilisations niche)
