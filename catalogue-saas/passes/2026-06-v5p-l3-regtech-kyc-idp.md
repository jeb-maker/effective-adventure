# Passe V5p — L3 long tail regtech, KYC lite FR/EU, document-idp HITL

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5p-l3-regtech-kyc-idp` |
| Date | 2026-06-23 |
| Niveau visé | L3 (long tail) |

## Enrichissement catalogue

| Segment | Avant | Cible | Ajoutés | Exemples |
|---|---:|---:|---:|---|
| `kyc-aml` | 13 | +10–15 | +12 | Didit, Lemonway KYC, Treezor, MangoPay KYC, Fourthline, Flagright, Ondorse, ARIADNEXT |
| `regtech` | 30 | +10–15 | +12 | Behavox, Regnology, Solidatus, Feedzai, Napier, Opensee (FR), Apiax |
| `document-idp` | 48 | +10–15 | +12 | FormX, DataSnipper, DeepOpinion, Stampli, Amazon A2I, Invofox, Fabasoft |

**Total visé** : +36 vendeurs. Exclus (déjà catalogués) : Dotfile, Salv, Klippa, Veryfi, Base64.ai, Konfuzio.

## Patches cross-segment

| Vendeur | Segments ajoutés |
|---|---|
| Fenergo, Feedzai, Lucinity, Napier | `kyc-aml` |
| Workfusion, Parseur, Docparser, Airparser | `document-idp` |
| Nanonets, FormX | `parsing-inbox` |

Focus moisson : **HQ FR/EU** sur KYC lite fintech (Lemonway, Treezor, Ondorse, ARIADNEXT, Opensee) ; IDP avec **HITL / dossier validé** (FormX, DataSnipper, Amazon A2I).

## Sources consultées

| Source | Segments | Candidats bruts | Nouveaux |
|---|---|---:|---:|
| g2 | kyc-aml, regtech, document-idp | 72 | 14 |
| geo_digest | kyc-aml, regtech, document-idp | 42 | 8 |
| analyst_report | regtech, document-idp | 32 | 5 |
| crunchbase | kyc-aml, regtech | 26 | 4 |
| capterra | document-idp | 14 | 2 |
| official_site | kyc-aml, regtech, document-idp | 28 | 3 |

## Contexte idées RecordAI

- [`idees/0029-recordai/README.md`](../../idees/0029-recordai/README.md) — KYC lite, IDP, dossier validé
- [`idees/0022-due-diligence-tiers/README.md`](../../idees/0022-due-diligence-tiers/README.md) — KYC/AML tiers

## Scripts

```bash
python3 scripts/enrich_catalogue_v5p.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation
```
