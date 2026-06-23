# Passe V5m — verticaux métiers + compliance fins

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5m-verticals-compliance` |
| Date | 2026-06-23 |

## Enrichissement catalogue

Objectif : passer les segments sous-alimentés de **~5 à ~10–11 vendeurs** (+5 à +7 chacun).

| Segment | Avant | Ajoutés | Après | Exemples FR/EU |
|---|---:|---:|---:|---|
| `regulatory-reporting-eu` | 5 | +6 | 11 | Cegid, Basware, Storecove, EDICOM |
| `accessibility-compliance` | 5 | +6 | 11 | Accessiway, Tanaguru, Asqatasun, Facil'iti |
| `esg-csrd` | 5 | +6 | 11 | Sweep, EcoVadis, Carbonfact, Carbon Maps |
| `pharma-regulatory` | 5 | +6 | 11 | EXTEDO, Dotmatics, Medidata, Certara |
| `privacy-consent` | 5 | +6 | 11 | Sirdata, tarteaucitron, iubenda, Usercentrics |
| `insurance-insurtech` | 5 | +6 | 11 | Akur8, Wakam, Alan, Luko |
| `construction-proptech` | 5 | +6 | 11 | Finalcad, Graneet, Dalux, Buildots |
| `supply-chain-logistics` | 5 | +6 | 11 | Shippeo, Transporeon, sennder, RELEX |
| `retail-ecommerce-ai` | 5 | +6 | 11 | Mirakl, Contentsquare, AB Tasty, Lengow, PrestaShop |
| `energy-cleantech` | 5 | +6 | 11 | Voltalis, Kizy, Schneider EcoStruxure, Octopus Energy |
| `healthcare-clinical-ai` | 5 | +6 | 11 | Qare, Medadom, Lifen, Owkin, Nabla (existant) |
| `health-data-analytics` | 5 | +6 | 11 | OpenHealth, Health Data Hub, Inato, Cegedim Health Data |
| `legal-contract-ai` | 5 | +6 | 11 | Doctrine, Ordalie, Jimini, Predictice |
| `payroll-hris` | 5 | +6 | 11 | Silae, Combo, Cegid HR, Deel (+ patch Lucca) |
| `learning-lxp` | 5 | +6 | 11 | Rise Up, Didask, Teach on Mars, CrossKnowledge |
| `treasury-fpa` | 5 | +6 | 11 | Kyriba, Cashforce, BlackLine, HighRadius |
| `finance-accounting-ai` | 5 | +6 | 11 | Agicap, Qonto, Indigo, Indy, Fulll |

**Total ajouté** : **+102 vendeurs** (0 doublon skip). **+1 patch** cross-segment : `lucca` → `payroll-hris` (déjà présent dans `hr-talent-ai`).

Patches cross-segment dans nouvelles entrées : Alan (insurance × clinical), Owkin (clinical × health-data), Medidata, Carbon Maps, Fulll.

## Sources consultées

| Source | Segments | Candidats | Ajoutés |
|---|---|---:|---:|
| `g2` | compliance + verticaux | ~210 | ~45 |
| `geo_digest` | segments FR | ~150 | ~35 |
| `crunchbase` | insurtech, retail, finance | ~120 | ~18 |
| `official_site` | public/regulatory FR | ~40 | ~6 |
| `open_source` | accessibilité, privacy | ~12 | ~2 |
| `analyst_report` | ESG, supply chain, retail | ~30 | ~6 |

## Saturation

Taux d'ajout moyen ~55 % sur candidats consultés ; segments encore L2 avec marge pour passes ciblées (sources `capterra`, `producthunt` non exploitées ici).

## Hors scope

Segments `kyc-aml`, `grc-security`, `cybersecurity-platforms` — traités par autre agent.

## Scripts

```bash
python3 scripts/enrich_catalogue_v5m.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation
```
