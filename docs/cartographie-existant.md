# Cartographie de l'existant — méthode

Deux cartographies **distinctes** et **complémentaires**. Ne jamais conclure
« espace libre » (C4) à partir d'une seule.

---

## 1. Les deux cartographies

| Cartographie | Où | Couvre | Ne couvre pas |
|---|---|---|---|
| **A — Catalogue SaaS** | [`catalogue-saas/`](../catalogue-saas/) | Produits commerciaux par segment (RegTech, IDP, agents…) | Services publics gratuits, réutilisations data.gouv, OSS hobby, bricolage Zapier |
| **B — Existant par idée** | §4 de chaque fiche + [`revue.md`](../idees/) | Paysage réel du besoin : public + commercial + OSS + bricolage | Exhaustivité SaaS mondiale (→ voir A) |

**Règle** : la section §4 **Existant / concurrence** d'une fiche doit couvrir **B**
en entier. Le catalogue SaaS (A) n'est qu'une **entrée** de B, jamais un substitut.

---

## 2. Checklist §4 — cartographie existant (obligatoire)

Avant de noter C4 (espace concurrentiel), parcourir **chaque ligne** :

| # | Canal | Où chercher | Obligatoire |
|---|---|---|---|
| 1 | **Réutilisations data.gouv** | Onglet « Réutilisations » du/des jeux cités ; [data.gouv.fr/reuses](https://www.data.gouv.fr/reuses/) | Oui si open data impliqué |
| 2 | **Services publics / .gouv.fr** | Ministères, ANS, Etalab, beta.gouv, observatoires CNAM/INSEE… | Oui |
| 3 | **Produits commerciaux FR/EU** | Recherche web ciblée + segments [`catalogue-saas/`](../catalogue-saas/) | Oui |
| 4 | **Open source / académique** | GitHub, HAL, projets communautaires | Oui si pertinent |
| 5 | **Bricolage no-code** | Zapier, Make, Notion, Excel + scripts internes | Oui (souvent le vrai concurrent) |
| 6 | **Listes comparatives** | G2, Capterra, AlternativeTo, Product Hunt | Recommandé |

Pour **chaque** élément trouvé : nom, URL, date de consultation, ce que ça fait,
ce que ça ne fait **pas**.

**Verdict saturation** (fin de §4) : `vierge` / `partiel` / `saturé` — avec le
**créneau précis** non couvert, pas une affirmation globale.

---

## 3. Catalogue SaaS — ce qu'on peut (et ne peut pas) en conclure

### Métriques distinctes

| Métrique | Signification | État actuel |
|---|---|---|
| **Profondeur inventaire** | ≥ N entrées par segment (ex. 18) | Inventaire curaté, pas exhaustif |
| **Saturation marché** | Dernière passe < 5 % de nouveaux candidats | Seul critère de **gel** segment |
| **`verified`** | Site officiel consulté, pricing/capabilities confirmés | Minorité des entrées — cible à monter |
| **Gel (`frozen-segments.json`)** | Saturation atteinte, pas de moisson avant revue trim. | **6 segments gelés** (parsing-inbox, document-idp, kyc-aml, automation-platforms, voice-speech-ai, real-estate-proptech) |

Ne jamais écrire « segment L3 complet » si la saturation n'est pas atteinte.
Préférer : « inventaire ≥ 18 entrées, saturation non atteinte ».

### Commandes

```bash
python3 scripts/catalogue_saas.py segment-readiness   # profondeur vs saturation
python3 scripts/catalogue_saas.py saturation watch      # taux par passe
python3 scripts/catalogue_saas.py audit-sources         # sources listicle
python3 scripts/catalogue_saas.py verify-eligible       # candidats → verified
python3 scripts/catalogue_saas.py validate
```

### Promouvoir une entrée en `verified`

Critères cumulatifs :

1. `source_url` = site officiel du produit (même domaine que `url`)
2. Pricing ou page produit consulté (pas un blog « top 10 »)
3. Capabilities confirmées sur le site
4. `source_consulted_at` = date réelle de consultation

Les sources listicle (`audit-sources`) restent `partial` tant qu'une vérification
officielle n'a pas été faite.

---

## 4. Revue critique — garde-fou cartographie

Aucune décision finale (🔁 / ❌ / ✅ / 🚧) sans `revue.md` dans le dossier idée.

La revue vérifie explicitement :

- concurrents **omis** (surtout services publics) ;
- échantillon §4 **tronqué** ;
- C4 surévalué parce que seul le catalogue SaaS a été consulté.

Prompt : [`docs/prompts/03-revue-critique.md`](prompts/03-revue-critique.md).

Contrôle automatisé :

```bash
python3 scripts/check_idees.py          # rapport backlog revues
python3 scripts/check_idees.py --strict  # échoue si revue manquante
```

---

## 6. Piste cartographie continue (alternative au pivot produit)

Quand le registre idées ne produit **aucun Go** mais que la valeur du dépôt
est la **connaissance du marché**, on peut prioriser la cartographie sans ouvrir
de nouvelles idées :

| Priorité | Cartographie | Livrable |
|---|---|---|
| 1 | **A — Catalogue SaaS** | Passes V6* : verified ↑, segments 🔁 des idées restantes, gel saturation |
| 2 | **B — §4 fiches** | Sous-sections obligatoires (services publics, réutilisations data.gouv) sur les 7 🔁 |
| 3 | **Réutilisations data.gouv** | Entrées catalogue pour Orama, Habity, DépensesPubliques… (cartographie citoyenne) |
| 4 | **Audit listicle** | `audit-sources` → promotion `verified` par vague (~20/semaine) |

### Automation (manifeste JSON + gate)

Les passes V6* manuelles (`enrich_catalogue_v6*.py`) restent valides ; pour les
suivantes, préférer le pipeline unifié :

```bash
# 1. Créer une passe (manifeste + journal)
python3 scripts/catalogue_pass.py init 2026-07-v6j-ma-passe

# 2. Éditer catalogue-saas/passes/2026-07-v6j-ma-passe.manifest.json
#    (voir manifest.example.json)

# 3. Appliquer + contrôle qualité complet
python3 scripts/catalogue_pass.py run catalogue-saas/passes/2026-07-v6j-ma-passe.manifest.json

# Passe hebdo cartographie (sans manifeste — promote auto 🔁 + gate)
python3 scripts/catalogue_pass.py weekly --limit 20 --dry-run   # aperçu
python3 scripts/catalogue_pass.py weekly --limit 20             # exécution

# Gate seul (validate + listicle + check_idees --strict)
python3 scripts/catalogue_saas.py gate

# Promotion ciblée verify-eligible
python3 scripts/catalogue_saas.py verify-promote --retravailler --limit 20 --dry-run
python3 scripts/sync_idees_catalogue.py   # rafraîchir blocs README idées
```

**Ce qui reste manuel** : recherche des concurrents, rédaction des ajouts
(`additions` dans le manifeste), revue adversariale des idées, décision produit.

**Règle** : la cartographie **n'invalide pas** le verdict discovery (0 Go) — elle
**alimente** un futur pivot (0001, 0029, 0025) avec un §4 déjà complet.

---

## 5. Enchaînement recommandé

```text
Payeur + douleur (§1–2)
        │
        ▼
Checklist §4 (cartographie B) — prompt 01-recherche-existant
        │
        ├──► Segments catalogue SaaS (cartographie A) si pertinent
        │
        ▼
Analyse + scoring (prompt 02)
        │
        ▼
Revue critique OBLIGATOIRE (prompt 03) → revue.md
        │
        ▼
Décision finale + registre README
```
