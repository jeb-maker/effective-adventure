# Passe V6 pilote — compliance-to-spec × public-procurement-intel

- **Pass ID** : `2026-06-v6-pilot-compliance-procurement`
- **Date** : 2026-06-23
- **Script** : `scripts/enrich_catalogue_v6_pilot.py`
- **Contexte** : pilote méthode V6 (sources officielles, promotion `verified`, concurrents omis en revues 0029 et 0001)

## Objectif

1. Combler les **angles morts SaaS** identifiés par le red-team (CheckFile.ai, Tenderbolt, IZIAO, AlertOffres).
2. **Promouvoir en `verified`** les acteurs clés déjà présents mais en `partial` (Maître AO, Nextend.ai).
3. Documenter la passe dans `coverage-matrix.json` avec taux de nouveauté mesurable.

## Segments ciblés

| Segment | Avant | Après | Nouveaux | Promus verified |
|---|---|---|---|---|
| `compliance-to-spec` | 59 | **61** | +2 | CheckFile.ai, VerifyPDF |
| `public-procurement-intel` | 20 | **24** | +4 | Tenderbolt, IZIAO, AlertOffres (+ PublikConnect partial) |
| `kyc-aml` (tag) | — | +1 tag | checkfile-ai patché | — |

## Ajouts (sources officielles)

### compliance-to-spec / RecordAI (0029)

| ID | Source consultée | verified |
|---|---|---|
| `checkfile-ai` | https://www.checkfile.ai/pricing | oui |
| `verifypdf` | https://verifypdf.com/ | oui |

### public-procurement-intel / Radar (0001)

| ID | Source consultée | verified |
|---|---|---|
| `tenderbolt-ai` | https://www.tenderbolt.ai/fr/solutions/public | oui |
| `iziao` | https://www.iziao.fr/repondre-aux-marches-publics-tarifs | oui |
| `alertoffres` | https://alertoffres.fr/tarifs | oui |
| `publikconnect` | https://publikconnect.fr/tarifs | partial (tarifs à reconfirmer) |

## Promotions verified (existants)

| ID | Nouvelle source |
|---|---|
| `maitre-ao` | https://www.maitre-ao.fr/fr/tarifs |
| `nextend-ai` | https://nextend.ai/pricing |
| `marchespublics-ai` | https://marchespublics.ai/ (partial — pas de grille publique) |
| `inscribe` | https://www.inscribe.ai/ |

## Saturation (dernière passe V6)

Taux estimé sur candidats consultés officiellement :

| Segment | Candidats | Nouveaux | Taux | Statut |
|---|---|---|---|---|
| `compliance-to-spec` | 7 | 2 | **28,6 %** | Loin du gel (< 5 %) |
| `public-procurement-intel` | 19 | 4 | **21,1 %** | Loin du gel ; passé L2 → **L3** cible |

→ Le segment marchés publics **n'est pas clos** : des acteurs FR (Synapse, France Marchés, Tengo…) restent à moissonner.

## Métriques globales post-passe

- **1 416 vendeurs** (+6)
- **63 verified** (+8 vs 55)
- **52 listicle-sourced** (inchangé — prochaine passe : re-vérifier)

## Prochaine passe V6b (suggestion)

1. `public-procurement-intel` : Synapse, France Marchés, Doubletrade enrichi, OpenMarchés
2. `parsing-inbox` : promotion Parseur/Rossum en verified (revue 0029)
3. Vague `verify-eligible` : 20 entrées/semaine depuis `python3 scripts/catalogue_saas.py verify-eligible`

## Commandes

```bash
python3 scripts/enrich_catalogue_v6_pilot.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py segment-readiness
python3 scripts/catalogue_saas.py verify-eligible | head -30
```
