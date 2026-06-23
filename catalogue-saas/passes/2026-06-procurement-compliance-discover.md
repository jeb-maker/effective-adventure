# Passe procurement + compliance-to-spec

- **Pass ID** : `2026-06-procurement-compliance-discover`
- **Date** : 2026-06-23
- **Segments** : `public-procurement-intel`, `compliance-to-spec` (+ kyc-aml)
- **Idées** : 0001, 0008, 0019, 0027, 0029

## Discover

```bash
python3 scripts/catalogue_discover.py brief public-procurement-intel
python3 scripts/catalogue_discover.py scan public-procurement-intel   # 1 local rejeté
python3 scripts/catalogue_discover.py scan compliance-to-spec         # 0 data.gouv
```

data.gouv peu productif sur ces segments → complément **revues adversariales** + promote verify-eligible.

## +6 ajouts

| ID | Segments | Statut |
|---|---|---|
| `attribution-intelligence` | public-procurement-intel | partial — revue 0001 |
| `shift-claims` | compliance-to-spec, document-idp | partial — revue 0029 |
| `korint` | compliance-to-spec, insurance | partial — revue 0029 |
| `mediar` | compliance-to-spec, rpa | partial — revue 0029 |
| `api-entreprise-gouv` | kyc-aml, compliance-to-spec | **verified** |
| `api-recherche-entreprises` | kyc-aml, data-enrichment | **verified** |

## +14 verify (manifeste) + 10 verify-promote

Procurement FR : DoubleTrade, Weproc, First AO, EXPLORE, Centrale des Marchés, Marchés Online, France Marchés, Tengo, Vecteur Plus…

Compliance : DiliTrust, Yooz, Libeo, Probo, VerifyPDF…

## Métriques

| Métrique | Avant | Après |
|---|---|---|
| Vendeurs | 1 458 | **1 464** |
| Verified | 192 | **216** |
| Listicle | 0 | **0** |

## Validation

```bash
python3 scripts/catalogue_pass.py run catalogue-saas/passes/2026-06-procurement-compliance-discover.manifest.json
python3 scripts/catalogue_saas.py verify-promote --segment public-procurement-intel --segment compliance-to-spec --limit 10
python3 scripts/sync_idees_catalogue.py
python3 scripts/catalogue_saas.py gate
```
