# Surveillance saturation — juin 2026

| Champ | Valeur |
|---|---|
| Date | 2026-06-23 |
| Seuil gel | **< 5 %** nouveaux / candidats (passe réelle) |
| Seuil alerte | **5–8 %** (`[PROCHE]`) |
| Passes exclues | `v5e-retrospective`, `v5o-coverage` (backfill matrice, pas moisson) |

## Commandes

```bash
python3 scripts/catalogue_saas.py saturation watch
python3 scripts/catalogue_saas.py saturation freeze
python3 scripts/catalogue_saas.py saturation          # rapport historique par passe
```

## État actuel (post V5o)

| Indicateur | Valeur |
|---|---|
| Segments avec passe réelle mesurable | **67 / 68** |
| Segments gelés (`frozen-segments.json`) | **0** |
| Segments `[SATURÉ]` (< 5 %) | **0** |
| Segments `[PROCHE]` (5–8 %) | **0** |
| Vendeurs catalogue | **914** |
| Taux minimum observé | **13,8 %** (`support-sales-agents`, V5f) |

Aucun segment ne remplit encore le critère de gel L2/L3. La passe V5o (backfill coverage) est **exclue** du calcul : les taux affichés reflètent la **dernière passe de moisson réelle** (V5l–V5n, V5f L3, etc.).

## Top 5 à risque (taux le plus bas — gel si prochaine passe < 5 %)

| Rang | Segment | Dernière passe réelle | Taux | Écart au seuil 5 % |
|---:|---|---|---:|---:|
| 1 | `support-sales-agents` | V5f | 13,8 % | +8,8 pts |
| 2 | `data-integration-etl` | V5n | 15,0 % | +10,0 pts |
| 3 | `llm-api-providers` | V5l | 15,8 % | +10,8 pts |
| 4 | `grc-security` | V5f | 16,4 % | +11,4 pts |
| 5 | `regtech` | V5c | 16,7 % | +11,7 pts |

Ces segments restent **éloignés** du seuil de gel mais seront les **premiers candidats** si une passe de maintenance ajoute peu de nouveaux acteurs.

## Segments à éviter en remoisson (prochaine passe)

Priorité basse pour une **nouvelle vague L2** — préférer le long tail L3 ou des segments sans passe réelle récente :

1. **`support-sales-agents`**, **`grc-security`**, **`voice-speech-ai`** — V5f L3 déjà dense ; remoissonner sans angle niche (OSS, geo FR) produirait probablement < 5 %.
2. **`regtech`**, **`ai-governance`**, **`document-idp`** — V5c/V5i L2 multi-sources ; viser L3 ciblé plutôt qu'une 2e passe généraliste.
3. **Segments V5l–V5n** passés de L1→L2 (cyber, workplace, verticaux) — matrice complète post-V5o ; une remoisson immédiate dupliquerait le backfill coverage.
4. **Segments France idées (V5k)** — taux 22–58 % sur petits échantillons ; continuer le ciblage geo_digest / open data plutôt qu'une passe G2/Capterra générique.

## Recommandations maintenance

- **Relancer la surveillance** avant toute vague V6 : `saturation watch` puis `saturation freeze`.
- **Geler automatiquement** tout segment dont la prochaine passe réelle tombe < 5 % ; ne pas écraser le gel sans revue trimestrielle.
- **Prioriser** les segments sans entrée dans `coverage-matrix.json` pour une passe réelle, ou ceux encore en montée L3 (ex. `compliance-to-spec`, `parsing-inbox` — V5h ~19–22 %).
- **Ne pas remoissonner** les 46 segments dont `last_pass` = `v5o-coverage-l2` tant que leur passe d'enrichissement (V5l/V5m/V5n) reste > 5 %.
