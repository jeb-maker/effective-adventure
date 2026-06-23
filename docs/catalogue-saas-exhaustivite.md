# Méthode d'exhaustivité — catalogue SaaS

Complète [`catalogue-saas-methode.md`](catalogue-saas-methode.md) avec le processus **L2/L3** et le tagging géographique.

---

## 1. Redéfinition d'« exhaustif »

| Niveau | Définition | Critère d'arrêt |
|---|---|---|
| **L1** | Top acteurs reconnus (5–10) | Liste stable |
| **L2** | Tous les acteurs cités dans ≥ 2 sources indépendantes | Passe complète < 5 % nouveaux |
| **L3** | L2 + long tail (OSS, startups, niches régionales) | 3 passes < 5 % + revue trimestrielle |

**Saturation** : une passe qui consulte toutes les sources prévues et ajoute < **5 %** de vendeurs nouveaux → segment **gelé** jusqu'à la revue trimestrielle.

---

## 2. Entonnoir en 7 étapes

1. **Cadrer** le segment (`taxonomy.json`) + niveau L2/L3
2. **Matrice sources** — cocher ≥ 4 types dans `coverage-matrix.json`
3. **Moisson** — journal dans `catalogue-saas/passes/`
4. **Dédup** — un `id` par produit, notes M&A
5. **Fiche vendor** — T0 (inventaire) → T1 (capabilities) → T2 (scoring)
6. **Tag géo** — `hq_country`, `france_market`, `operating_regions`
7. **Saturation** — mettre à jour `coverage-matrix.json`, geler ou relancer

---

## 3. Champs géographiques

| Champ | Description | Exemple |
|---|---|---|
| `hq_country` | Siège (ISO 3166-1 alpha-2 ou `unknown`) | `FR`, `US`, `DE` |
| `france_market` | Présence / adoption marché français | `strong`, `partial`, `absent`, `unknown` |
| `operating_regions` | Zones d'opération documentées | `["FR", "EU"]` |
| `discovery_source` | Type de source de la découverte | `g2`, `crunchbase`… |
| `discovery_pass` | Identifiant de passe | `2026-06-v5b-compliance-to-spec` |

### Deux filtres indépendants

- **`hq_country != FR`** → acteur hors France
- **`france_market = absent`** → opportunité localisation / import

---

## 4. Matrice sources (obligatoire)

Types dans `taxonomy.json` → `coverage_source_types` :

| Type | Exemples |
|---|---|
| `g2` | Catégories G2, filtres région |
| `capterra` | Listes comparatives |
| `crunchbase` | Tags, HQ, funding |
| `analyst_report` | Gartner, IDC, RegTech Analyst |
| `alternatives` | « X alternatives », AlternativeTo |
| `open_source` | GitHub, awesome-lists |
| `geo_digest` | Sifted, Maddyness, EU-Startups |
| `official_site` | Pricing, docs produit |

Segment **non clos** tant que < 4 types sont renseignés dans `coverage-matrix.json`.

---

## 5. Vagues d'enrichissement

| Vague | Contenu | Statut |
|---|---|---|
| V1–V4 | 68 segments peuplés (L1) | Fait |
| **V5a** | Schéma géo + tag rétrospectif 394 entrées | Fait |
| **V5b** | Pilote L3 `compliance-to-spec` | Fait |
| **V5c** | L2 `regtech`, `document-idp`, `ai-governance` | Fait |
| **V5d** | Équivalents internationaux `france-*` (+41) | Fait |
| **V5e** | Coverage L2 rétrospectif + liaison 28 idées | Fait |
| **V5f** | L3 agents/voix, parsing inbox, GRC (+32) | Fait |
| **V5g** | 2e L3 parsing + compliance-to-spec, idée RecordAI | Fait |
| **V5h** | 3e L3 dossier validé (parsing + compliance) | Fait |
| **V5i** | L3 document-idp human-in-the-loop | Fait |
| **V5j** | automation-platforms orchestration RecordAI | Fait |
| **V5k** | Territoire idées 0025–0028 (7 segments FR) | Fait |
| **V5l** | Sécurité + KYC + infra IA (L1→L2) | Fait |
| **V5m** | Verticaux + compliance fins (L1→L2) | Fait |
| **V5n** | Workplace / data / sales (L1→L2) | Fait |
| **V5o** | Backfill coverage-matrix segments L2 | Fait |
| Maintenance | Long tail L3, revue trimestrielle | Continu |

### Surveillance saturation (maintenance)

Avant toute nouvelle vague de moisson :

```bash
python3 scripts/catalogue_saas.py saturation watch   # taux par passe réelle, flags [SATURÉ]/[PROCHE]
python3 scripts/catalogue_saas.py saturation freeze  # met à jour frozen-segments.json (< 5 %)
python3 scripts/catalogue_saas.py saturation         # rapport historique complet
```

- **Seuil gel** : < **5 %** nouveaux / candidats sur la **dernière passe réelle** (hors `v5e-retrospective`, `v5o-coverage`).
- **Alerte** : **5–8 %** → segment `[PROCHE]` ; éviter une remoisson généraliste au cycle suivant.
- **Registre gel** : `catalogue-saas/frozen-segments.json` — segments à ne pas remoissonner sans revue trimestrielle.
- **Journal** : `catalogue-saas/passes/2026-06-saturation-watch.md`.

---

## 6. Commandes

```bash
# Tag géographique rétrospectif (idempotent)
python3 scripts/tag_catalogue_geography_v5a.py

# Pilote L3 compliance-to-spec
python3 scripts/enrich_compliance_to_spec_v5b.py

# Liaison fiches idées
python3 scripts/sync_idees_catalogue.py

# Rapports
python3 scripts/catalogue_saas.py coverage
python3 scripts/catalogue_saas.py gaps
python3 scripts/catalogue_saas.py gaps --hq US --france-market absent
python3 scripts/catalogue_saas.py gaps --segment compliance-to-spec
python3 scripts/catalogue_saas.py saturation
python3 scripts/catalogue_saas.py saturation watch
python3 scripts/catalogue_saas.py saturation freeze
python3 scripts/catalogue_saas.py validate
```

---

## 7. Règles d'inclusion

**Inclure** : SaaS, API, plateforme cloud, OSS avec offre commerciale.

**Exclure** : consulting pur, feature ERP non autonome, doublons régionaux, produit sunset.

**Cas public** (`france-open-data`) : portails/APIs publiques autorisés avec note explicite ; les exporter séparément pour l'analyse concurrence SaaS pure.

---

## 8. Cibles chiffrées

| Étape | Vendeurs uniques (ordre de grandeur) |
|---|---|
| Post-V5g (juin 2026) | ~534 |
| Post-V5k + idées | ~637 |
| **Post-V5l–V5n (L2 complet)** | **~914** |
| L3 + maintenance | 1 500–2 500 |

La fiabilité prime sur la vitesse : **`unknown` est préférable à une guess non sourcée**.
