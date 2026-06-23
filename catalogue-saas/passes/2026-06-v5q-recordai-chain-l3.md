# Passe V5q — L3 chaîne RecordAI (email → dossier validé → orchestration)

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5q-recordai-chain-l3` |
| Date | 2026-06-23 |
| Niveau visé | L3 (chaîne RecordAI) |

## Enrichissement catalogue

| Segment | Avant | Cible | Ajoutés | Exemples |
|---|---:|---:|---:|---|
| `parsing-inbox` | 30 | +8–10 | +9 | Hiver, Help Scout, Dixa, EmailTree AI (LU), DocuWare (DE), M-Files (FI), Mailbutler (DE) |
| `compliance-to-spec` | 37 | +8–10 | +9 | Certivity (SE), Qualio, ComplianceQuest, ZenGRC, Certa, Ideagen, Origami Risk |
| `automation-platforms` | 21 | +8–10 | +9 | Bonitasoft (FR), Kestra (FR), Bonita, Inngest, Hatchet, Flokzu, Nintex |

**Total** : +27 vendeurs (950 → 977). Focus moisson : **workflow validé**, **case management**, **audit trail**, **connecteurs email/documents**, acteurs **EU/FR**.

## Patches cross-segment

| Vendeur | Segments ajoutés |
|---|---|
| AuditBoard | `compliance-to-spec` |
| Stampli, Docubee, DataSnipper | `parsing-inbox` |
| Flowable | `compliance-to-spec` |
| Temporal | `parsing-inbox` |

## Sources consultées

| Source | Segments | Candidats bruts | Nouveaux |
|---|---|---:|---:|
| g2 | parsing-inbox, compliance-to-spec, automation-platforms | 60 | 9 |
| geo_digest | parsing-inbox, compliance-to-spec, automation-platforms | 34 | 7 |
| open_source | automation-platforms | 16 | 4 |
| analyst_report | compliance-to-spec, automation-platforms | 20 | 3 |
| capterra | parsing-inbox, automation-platforms | 18 | 2 |
| crunchbase | compliance-to-spec | 10 | 1 |
| official_site | parsing-inbox | 8 | 1 |

## Contexte idée RecordAI

- [`idees/0029-recordai/README.md`](../../idees/0029-recordai/README.md) — chaîne email/PDF → dossier structuré validé → orchestration
- Complète V5h (dossier validé), V5j (orchestration) et V5p (IDP HITL) sur l'axe **case management + audit trail**

## Scripts

```bash
python3 scripts/enrich_catalogue_v5q.py
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py saturation watch
```
