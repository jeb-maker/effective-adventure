# Catalogue SaaS — veille marché

Registre **curaté** de SaaS comparables, aligné sur les règles de preuve du dépôt.

- **Méthode** : [`docs/catalogue-saas-methode.md`](../docs/catalogue-saas-methode.md)
- **Taxonomie** : [`taxonomy.json`](taxonomy.json)
- **Schéma** : [`schema/vendor.schema.json`](schema/vendor.schema.json)
- **Données** : [`vendors/`](vendors/) (un fichier JSON par segment)

---

## Segments (taxonomie)

Choisir un segment **avant** d'ajouter des vendeurs. Source : [`taxonomy.json`](taxonomy.json).

| # | ID | Label | Description | Fichier vendeurs |
|---|---|---|---|---|
| 1 | `regtech` | RegTech — veille & obligations | Surveillance réglementaire, extraction d'obligations, mapping policies/contrôles | [`regtech.json`](vendors/regtech.json) |
| 2 | `grc-security` | GRC & conformité sécurité | SOC2, ISO 27001, GDPR, DORA, NIS2 — contrôles, preuves, audits | [`grc-security.json`](vendors/grc-security.json) |
| 3 | `ai-governance` | AI Governance | EU AI Act, ISO 42001, NIST AI RMF — inventaire IA, risques, artefacts | [`ai-governance.json`](vendors/ai-governance.json) |
| 4 | `document-idp` | IDP & extraction documentaire | PDF/images → données structurées, OCR, schémas JSON | [`document-idp.json`](vendors/document-idp.json) |
| 5 | `parsing-inbox` | Parsing email & inbox | Email/PDF entrants → champs structurés, webhooks | [`parsing-inbox.json`](vendors/parsing-inbox.json) |
| 6 | `ai-copilot-dev` | Copilots IA & dev tools | Assistants par siège, code, productivité équipe | [`ai-copilot-dev.json`](vendors/ai-copilot-dev.json) |
| 7 | `support-sales-agents` | Agents support & sales | Résolution, qualification, SDR — souvent pricing au résultat | [`support-sales-agents.json`](vendors/support-sales-agents.json) |
| 8 | `automation-platforms` | Plateformes d'automatisation | Zapier, Make, n8n — workflows + intégrations | [`automation-platforms.json`](vendors/automation-platforms.json) |
| 9 | `compliance-to-spec` | Réglementation → spec produit | Traduction vers backlog logiciel testable — niche émergente | [`compliance-to-spec.json`](vendors/compliance-to-spec.json) |

Un vendeur peut appartenir à **plusieurs segments** (`segments: []` dans l'entrée JSON).

---

## État du remplissage (vague 1 — 2026-06-22)

| Segment | Entrées | Statut |
|---|---:|---|
| `regtech` | 13 | peuplé |
| `grc-security` | 11 | peuplé |
| `ai-governance` | 8 | peuplé |
| `document-idp` | 16 | peuplé |
| `parsing-inbox` | 5 | peuplé |
| `ai-copilot-dev` | 6 | peuplé |
| `support-sales-agents` | 6 | peuplé |
| `automation-platforms` | 3 | peuplé |
| `compliance-to-spec` | 0 | **à explorer** |

**Total recensé : 68 vendeurs** (plusieurs tags multi-segments possibles).

---

## Commandes

```bash
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py export -o catalogue-saas/exports/vendors.csv
python3 scripts/catalogue_saas.py build-db
```

## Enrichir

1. Choisir un segment dans le tableau ci-dessus.
2. Ajouter une entrée dans `vendors/<segment>.json`.
3. Renseigner `source_url` + `source_consulted_at` (obligatoire).
4. Lancer `validate` avant commit.

## Limites

- Non exhaustif : objectif veille, pas annuaire mondial.
- `partial` = profil ou pricing à reconfirmer sur le site officiel.
- Ne pas utiliser `unverified` pour scorer une fiche idée.
