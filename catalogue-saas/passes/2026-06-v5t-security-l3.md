# Passe V5t — L3 complétion segments sécurité

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5t-security-l3` |
| Date | 2026-06-23 |
| Niveau visé | L3 (sécurité cyber/IAM/CSPM/email/vuln + vector DB) |

## Enrichissement catalogue

| Segment | Avant | Cible | Ajoutés | Exemples |
|---|---:|---:|---:|---|
| `cybersecurity-platforms` | 12 | ~18 | +7 | Stormshield, TEHTRIS, CrowdSec, Gatewatcher, Darktrace |
| `identity-access-management` | 11 | ~18 | +7 | Alsid, Thales CipherTrust, Evidian, BeyondTrust, Saviynt |
| `cloud-security-cspm` | 12 | ~18 | +7 | Zscaler, Tailscale, Upwind, Defender for Cloud, Stacklet |
| `email-security` | 11 | ~18 | +7 | Mailinblack, Hornetsecurity, KnowBe4, Avanan |
| `vulnerability-management` | 12 | ~18 | +7 | YesWeHack, Yogosha, HackerOne, Outpost24, Nuclei |
| `vector-databases` | 10 | ~20 | +10 | LanceDB, Elasticsearch Vector, OpenSearch k-NN, Supabase Vector |

**Total** : +45 vendeurs (1072 → 1117 IDs uniques). Acteurs FR déjà présents conservés : HarfangLab, Sekoia, Wallix, Vade.

## Patches cross-segment

| Vendeur | Segments ajoutés |
|---|---|
| Vespa | `vector-databases` |
| Stormshield | `cloud-security-cspm` |
| CrowdSec | `vulnerability-management` |

Focus moisson : **HQ FR/EU** — Stormshield, TEHTRIS, CrowdSec, Gatewatcher, Alsid, Thales, Evidian, Mailinblack, YesWeHack, Yogosha ; compléments EU WithSecure, Hornetsecurity, Libraesva, Outpost24.

## Sources consultées

| Source | Segments | Candidats bruts | Nouveaux |
|---|---|---:|---:|
| geo_digest | cyber, IAM, email, vuln | 82 | 15 |
| g2 | cyber, IAM, CSPM, email, vuln, vector | 110 | 17 |
| analyst_report | cyber, CSPM, email, vuln | 56 | 7 |
| official_site | CSPM, email, vector | 42 | 9 |
| open_source | vuln, vector | 24 | 4 |
| crunchbase | IAM, CSPM, vector | 36 | 3 |

## Gaps HQ FR (avant → après)

| Segment | hq_FR avant | Acteurs FR ajoutés |
|---|---:|---|
| `cybersecurity-platforms` | 2 | Stormshield, TEHTRIS, CrowdSec, Gatewatcher |
| `identity-access-management` | 1 | Alsid, Thales CipherTrust, Evidian |
| `email-security` | 1 | Mailinblack |
| `vulnerability-management` | 0 | YesWeHack, Yogosha |

## Scripts

```bash
python3 scripts/enrich_catalogue_v5t_security.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation
python3 scripts/catalogue_saas.py gaps --segment cybersecurity-platforms
```
