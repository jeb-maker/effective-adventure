# Passe V5t-b — L3 verticaux métiers + compliance

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5t-verticals-l3` |
| Date | 2026-06-23 |
| Niveau visé | L3 (11→~18 vendeurs/segment) |

## Enrichissement catalogue

Objectif : passer **18 segments verticaux/compliance** de **11 à ~18** vendeurs (+7 à +8 chacun).

| Segment | Avant | Ajoutés | Après | Exemples FR/EU |
|---|---:|---:|---:|---|
| `accessibility-compliance` | 11 | +7 | 18 | Access 42, Qualiweb, Access for All |
| `construction-proptech` | 11 | +7 | 18 | iBAT, Helyx, Plan BIM, Inovva |
| `insurance-insurtech` | 11 | +8 | 19 | Zelros, Descartes Underwriting, Assurup, Inspeer |
| `retail-ecommerce-ai` | 11 | +8 | 19 | iAdvize, Shoppingfeed, Octopia, Akeneo, Wizville |
| `energy-cleantech` | 11 | +7 | 18 | Dreev, Watteco, Beem Energy, Ekodev |
| `esg-csrd` | 11 | +8 | 19 | Apiday, Metrio (EcoAct), Klim |
| `pharma-regulatory` | 11 | +7 | 18 | Softway Medical, Pharmagest |
| `privacy-consent` | 11 | +7 | 18 | Commanders Act, TrustCommander |
| `regulatory-reporting-eu` | 11 | +8 | 19 | Generix, Flowie |
| `healthcare-clinical-ai` | 11 | +8 | 19 | Cardiologs, Incepto, Therapixel, Withings, Medecom |
| `health-data-analytics` | 11 | +7 | 18 | Adimed, Phare Data, MedTrail, HoliHealth |
| `legal-contract-ai` | 11 | +7 | 18 | Legalstart, LegalPlace, Kleo, Dili |
| `payroll-hris` | 11 | +7 | 18 | Talentia, Kelio, HR Path |
| `learning-lxp` | 11 | +7 | 18 | Edflex, Domoscio, Tentee, Neobrain, 365Talents |
| `treasury-fpa` | 11 | +7 | 18 | Fintecture |
| `finance-accounting-ai` | 11 | +7 | 18 | Expensya, Sellsy, Tiime, Dougs, Freebe |
| `supply-chain-logistics` | 11 | +7 | 18 | Flowlity, Stockly, Bigblue, Oware |
| `translation-localization` | 11 | +7 | 18 | TextMaster |

**Total ajouté** : **+131 vendeurs** (1 skip : `talentsoft` déjà dans `hr-talent-ai` → patch cross-segment).

## Patches cross-segment

| Vendeur | Segments ajoutés |
|---|---|
| Doctolib | `healthcare-clinical-ai` |
| Procore | `construction-proptech` |
| Metron | `energy-cleantech` |
| Yooz | `regulatory-reporting-eu` |
| Spendesk | `finance-accounting-ai` |
| Agicap | `treasury-fpa` |
| Talentsoft | `learning-lxp` |

Focus moisson : **HQ FR prioritaire** — Accessiway (déjà V5m), Shift Technology (déjà), Mirakl, Doctrine, Silae, Kyriba, Pennylane (déjà), Doctolib (patch), plus Zelros, iAdvize, Cardiologs, Apiday, Generix, Flowlity, TextMaster.

## Idées liées

| Idée | Segments impactés |
|---|---|
| `0016-accessibilite-handicap-erp` | `accessibility-compliance` |
| `0017-empreinte-carbone-territoire` | `esg-csrd`, `energy-cleantech` |
| `0024-risque-climat-actifs` | `insurance-insurtech`, `energy-cleantech` |
| `0013-choisir-son-ecole` | `learning-lxp` |
| `0020-benchmark-financier-collectivites` | `treasury-fpa` |
| `0006-assistant-implantation-commerciale` | `retail-ecommerce-ai` |

## Sources consultées

| Source | Segments | Candidats bruts | Nouveaux |
|---|---|---:|---:|
| g2 | 18 segments verticaux | ~340 | ~55 |
| geo_digest | segments FR | ~260 | ~52 |
| crunchbase | insurtech, retail, finance, santé | ~120 | ~12 |
| analyst_report | pharma, health-data, treasury | ~30 | ~4 |
| official_site | energy, payroll, regulatory FR | ~28 | ~3 |
| capterra | accessibilité, privacy | ~18 | ~2 |
| alternatives | translation | ~8 | ~1 |

## Scripts

```bash
python3 scripts/enrich_catalogue_v5t_verticals.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation
```
