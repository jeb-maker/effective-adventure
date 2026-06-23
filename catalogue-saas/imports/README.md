# Imports sources externes

Candidats bruts **non mergés** — revue obligatoire avant manifeste.

| Fichier | Source | Commande |
|---|---|---|
| `g2-SEGMENT-DATE.json` | G2 API | `catalogue_collect.py g2-search` |
| `crunchbase-*.json` | CSV Crunchbase | `catalogue_collect.py import-csv` |

Workflow : voir [`docs/catalogue-saas-sources-externes.md`](../../docs/catalogue-saas-sources-externes.md).
