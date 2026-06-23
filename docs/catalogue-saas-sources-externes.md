# Sources externes — G2, Capterra, Crunchbase, etc.

Comment alimenter le catalogue depuis les agrégateurs SaaS, **sans violer les ToS**.

---

## Synthèse par source

| Source | API officielle | Données utiles | Recommandation dépôt |
|---|---|---|---|
| **G2** | Oui — [Developer Portal](https://my.g2.com/developers) (~1 000 appels/mois gratuits) | catégories, produits, reviews, vendor | **Intégrer** via `G2_API_TOKEN` |
| **Crunchbase** | Enterprise / contact sales uniquement | founded_year, funding, HQ | **Import CSV** export Pro (pas de scrape) |
| **Capterra / GetApp** | Pas d'API publique | catégories, pricing, reviews | **Import CSV** manuel ou brief URLs discover |
| **AlternativeTo** | Non | alternatives OSS/commercial | Brief discover + curation |
| **Product Hunt** | API limitée | lancements récents | Optionnel (startups récentes) |
| **GitHub** | API ouverte | OSS, stars, created_at | Déjà partiellement couvert (`open_source`) |
| **data.gouv** | API ouverte | services publics FR | **Déjà intégré** (`catalogue_discover.py`) |

**À éviter** : scrapers Apify/ScraperAPI sur G2/Capterra/Crunchbase en production CI — risque blocage + ToS.

---

## Pipeline recommandé

```text
Source légale (G2 API / CSV export / data.gouv)
        ↓
catalogue_collect.py import / g2-search
        ↓
catalogue-saas/imports/*.json  (candidats bruts)
        ↓
Revue humaine → manifeste JSON
        ↓
catalogue_pass.py run → gate
```

---

## G2 (API)

1. Créer un compte vendeur ou développeur G2
2. [Developer Portal](https://my.g2.com/developers) → Access Tokens → Generate
3. Exporter : `export G2_API_TOKEN=...`
4. Lancer :

```bash
python3 scripts/catalogue_collect.py g2-search --segment regtech --limit 20
python3 scripts/catalogue_collect.py merge-imports --dry-run
```

Champs remplis : `name`, `url`, `description`, `discovery_source=g2`, `entry_ai_generated=true`.

---

## Crunchbase (export CSV)

1. Abonnement Pro/Business avec export
2. Exporter CSV (companies) filtré par catégorie ou liste de domaines
3. Placer dans `catalogue-saas/imports/crunchbase-YYYY-MM-DD.csv`
4. Colonnes attendues (flexibles) : `name`, `website`, `founded_on` / `Founded Date`, `description`, `location`

```bash
python3 scripts/catalogue_collect.py import-csv catalogue-saas/imports/crunchbase-2026-06.csv --source crunchbase
```

Enrichit surtout **`founded_year`**, `hq_country`, `notes` sur vendeurs **déjà présents** (match par domaine).

---

## Capterra (export manuel)

Pas d'API officielle. Options :

- Extension [Capterra Reviews Exporter](https://chromewebstore.google.com/detail/capterra-reviews-exporter/ijhmkkpaeldmgphbciakkogipljnphjm) → CSV
- Copier-coller depuis brief discover (`catalogue_discover.py brief SEGMENT`)
- Apify **hors CI** — usage ponctuel, relecture obligatoire

Format CSV minimal : `name`, `url`, `category`, `description`

```bash
python3 scripts/catalogue_collect.py import-csv imports/capterra-regtech.csv --source capterra --segment regtech
```

---

## Variables d'environnement

| Variable | Usage |
|---|---|
| `G2_API_TOKEN` | Token API G2 (`Authorization: Token token=…`) |

---

## Limites

- Les imports **ne mergent pas** automatiquement dans `vendors/` — ils produisent des candidats + enrichissement `founded_year`
- Toute nouvelle entrée passe par **manifeste + gate**
- `entry_ai_generated=true` sur candidats collectés automatiquement
