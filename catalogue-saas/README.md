# Catalogue SaaS — veille marché

Registre **curaté** de SaaS comparables, aligné sur les règles de preuve du dépôt.

- **Méthode** : [`docs/catalogue-saas-methode.md`](../docs/catalogue-saas-methode.md)
- **Taxonomie** : [`taxonomy.json`](taxonomy.json) — **21 segments** en **10 catégories**
- **Schéma** : [`schema/vendor.schema.json`](schema/vendor.schema.json)
- **Données** : [`vendors/`](vendors/) (un fichier JSON par segment)

---

## Segments par catégorie

### Compliance & réglementation

| ID | Label | Fichier |
|---|---|---|
| `regtech` | RegTech — veille & obligations | [`regtech.json`](vendors/regtech.json) |
| `regulatory-reporting-eu` | Reporting réglementaire EU (e-invoicing…) | [`regulatory-reporting-eu.json`](vendors/regulatory-reporting-eu.json) |
| `grc-security` | GRC & conformité sécurité | [`grc-security.json`](vendors/grc-security.json) |
| `privacy-consent` | Privacy & consent management | [`privacy-consent.json`](vendors/privacy-consent.json) |
| `ai-governance` | AI Governance | [`ai-governance.json`](vendors/ai-governance.json) |
| `compliance-to-spec` | Réglementation → spec produit | [`compliance-to-spec.json`](vendors/compliance-to-spec.json) |
| `accessibility-compliance` | Accessibilité numérique (WCAG/RGAA) | [`accessibility-compliance.json`](vendors/accessibility-compliance.json) |

### Documents & données non structurées

| ID | Label | Fichier |
|---|---|---|
| `document-idp` | IDP & extraction documentaire | [`document-idp.json`](vendors/document-idp.json) |
| `parsing-inbox` | Parsing email & inbox | [`parsing-inbox.json`](vendors/parsing-inbox.json) |

### IA au travail

| ID | Label | Fichier |
|---|---|---|
| `ai-productivity` | Productivité IA métier (hors dev) | [`ai-productivity.json`](vendors/ai-productivity.json) |
| `ai-copilot-dev` | Copilots IA & dev tools | [`ai-copilot-dev.json`](vendors/ai-copilot-dev.json) |
| `rag-knowledge` | RAG & knowledge enterprise | [`rag-knowledge.json`](vendors/rag-knowledge.json) |

### Automatisation & agents

| ID | Label | Fichier |
|---|---|---|
| `automation-platforms` | Plateformes d'automatisation | [`automation-platforms.json`](vendors/automation-platforms.json) |
| `support-sales-agents` | Agents support & sales | [`support-sales-agents.json`](vendors/support-sales-agents.json) |
| `voice-speech-ai` | Voix & speech IA | [`voice-speech-ai.json`](vendors/voice-speech-ai.json) |

### Verticaux métier

| ID | Label | Fichier |
|---|---|---|
| `finance-accounting-ai` | Finance & compta IA | [`finance-accounting-ai.json`](vendors/finance-accounting-ai.json) |
| `legal-contract-ai` | Legal & contract AI | [`legal-contract-ai.json`](vendors/legal-contract-ai.json) |
| `hr-talent-ai` | RH & talent IA | [`hr-talent-ai.json`](vendors/hr-talent-ai.json) |

### Données B2B

| ID | Label | Fichier |
|---|---|---|
| `data-enrichment-b2b` | Enrichissement données B2B | [`data-enrichment-b2b.json`](vendors/data-enrichment-b2b.json) |

### France / secteur public

| ID | Label | Fichier |
|---|---|---|
| `public-procurement-intel` | Intelligence marchés publics | [`public-procurement-intel.json`](vendors/public-procurement-intel.json) |
| `territorial-analytics` | Analytics territoriales & open data | [`territorial-analytics.json`](vendors/territorial-analytics.json) |

Un vendeur peut appartenir à **plusieurs segments** (`segments: []` dans l'entrée JSON).

---

## État du remplissage (vague 3 — 2026-06-22)

**162 vendeurs uniques** · **21 segments** · **12 nouveaux segments** (vague 3)

| Segment | Entrées |
|---|---:|
| `grc-security` | 28 |
| `document-idp` | 24 |
| `ai-governance` | 20 |
| `regtech` | 17 |
| `automation-platforms` | 12 |
| `support-sales-agents` | 12 |
| `ai-copilot-dev` | 11 |
| `compliance-to-spec` | 10 |
| `parsing-inbox` | 9 |
| `territorial-analytics` | 6 |
| `ai-productivity` | 5 |
| `voice-speech-ai` | 5 |
| *10 segments à 4 entrées* | 4 chacun |

---

## Commandes

```bash
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/seed_catalogue_segments_v3.py   # graines nouveaux segments
python3 scripts/catalogue_saas.py export -o catalogue-saas/exports/vendors.csv
```

## Enrichir

1. Choisir un **segment** (tableau ci-dessus).
2. Ajouter une entrée dans `vendors/<segment>.json`.
3. Renseigner `source_url` + `source_consulted_at`.
4. `python3 scripts/catalogue_saas.py validate` avant commit.

Pour proposer un **nouveau segment** : l'ajouter dans `taxonomy.json` (avec `category`) puis créer le fichier `vendors/<id>.json`.
