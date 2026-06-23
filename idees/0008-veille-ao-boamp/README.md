# Veille d'appels d'offres (BOAMP) — agrégateur classique

- **ID** : 0008
- **Statut** : ❌ Écartée
- **Score** : 54 / 100
- **Dernière mise à jour** : 2026-06-23
- **Révision critique** : voir [`revue.md`](revue.md) — écart **confirmé** (score
  posé à **54/100**, < 55, + critère éliminatoire saturation). L'audit aggrave le
  constat : les acteurs « attribution » récents (Maître AO, Nextend.ai,
  marchespublics.ai) **font aussi de la veille** → segment frontal fermé ; le
  renvoi vers 0001 est à nuancer (l'attribution est elle aussi disputée).
- **Pitch (1 phrase)** : Agréger les avis de marché à venir (BOAMP/TED/profils
  acheteurs) avec alertes et scoring.

---

## 1. Problème / douleur
Réelle pour les répondants aux AO, mais déjà massivement adressée.

## 4. Existant / concurrence (très saturé)

> Cartographie B (consultée 2026-06-23). Veille AO **saturée** ; sources officielles sur data.gouv.

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **BOAMP (open data)** | https://www.boamp.fr/ , https://www.data.gouv.fr/datasets/boamp | Source officielle avis de marché |
| **API BOAMP** | https://www.data.gouv.fr/dataservices/api-bulletin-officiel-des-annonces-des-marches-publics-boamp | Flux structuré avis AO |
| **PLACE / achatpublic.com** | https://www.achatpublic.com/ | Dématérialisation côté acheteurs |
| **data.economie.gouv.fr — DECP** | https://data.economie.gouv.fr/ | Données essentielles commande publique |

### Réutilisations data.gouv

| Acteur | URL | Rôle |
|---|---|---|
| **decp.info** | https://www.data.gouv.fr/reuses/decp-info-interface-dexploration-et-de-telechargement-des-donnees-de-la-commande-publique-au-format-tabulaire | Exploration DECP (adjacent attribution) |
| **OpenMarchés** | https://www.data.gouv.fr/reuses/openmarches-visualisation-des-marches-it-publics | Analytics marchés IT publics |

### Produits commerciaux

Vecteur Plus, France Marchés, Synapse, Doaken, Olra, PublikConnect (49 € HT),
AlertOffres (29,99 €), AOS, Explore, Marchés Online, Dématis, Centrale des
Marchés — plusieurs avec IA (scoring, analyse DCE, mémoire technique).
Sources (consultées 2026-06-23) :
https://olra.fr/blog/alternatives-synapse-france-marches-comparatif ,
https://remporte.fr/blog/plateformes-appels-offres-comparatif/

## 10. Scoring

> Tableau posé par la revue critique (la fiche écartait sans note). Notes adversariales.

| # | Critère | Poids | Note (1-5) | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 | Douleur réelle et récurrente pour les répondants aux AO. |
| C2 | Cible solvable (qui paie) | 3 | 3 | 9 | Payeur réel (29,99–300 €/mois) mais budget déjà capté par les incumbents. |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 | BOAMP/TED ouverts, prêts, exploitables. |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 | Très saturé : 12+ acteurs frontaux + IA + convergence attribution→veille. |
| C5 | Différenciation défendable | 2 | 1 | 2 | Aucune en frontal ; matière première gratuite, scoring déjà fait. |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 | Agrégation/filtrage robuste ; peu d'hallucination. |
| C7 | Facilité du MVP | 2 | 4 | 8 | MVP simple (données prêtes) — ce qui nourrit la saturation. |
| C8 | Maîtrise des risques | 2 | 1 | 2 | Saturation + commoditisation + guerre des prix non maîtrisées. |
| C9 | Monétisation / impact | 2 | 1 | 2 | Marché tiré vers le bas ; pas de revenu défendable pour un entrant. |
| | **Total** | | | **57 / 105** | |

**Score /100** : 57 / 105 × 100 = **54**

## 11. Verdict & décision
❌ **Écartée** en frontal. Marché très saturé (12+ acteurs, plusieurs avec IA) et
les acteurs « attribution » récents (Maître AO, Nextend.ai, marchespublics.ai)
**font aussi de la veille** → segment fermé. Score reconstruit **54/100** (< 55)
**et** critère éliminatoire de saturation. La valeur résiduelle théorique est sur
l'**analyse d'attribution** (passé), traitée dans l'idée **0001** — mais ce refuge
est lui-même disputé (cf. [`revue.md`](revue.md) et la revue de 0001). Ne pas
attaquer ce segment directement.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0008-veille-ao-boamp` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `public-procurement-intel` — Intelligence marchés publics

Fichier : [`catalogue-saas/vendors/public-procurement-intel.json`](../../catalogue-saas/vendors/public-procurement-intel.json) (43 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `marchespublics-ai` | marchespublics.ai | FR | strong | verified |
| `maitre-ao` | Maître AO | FR | strong | verified |
| `aws-boamp` | BOAMP (open data) | FR | strong | verified |
| `achatpublic` | PLACE (achatpublic.com) | FR | strong | verified |
| `tussell` | Tussell | GB | absent | partial |
| `spend-network` | Spend Network | GB | absent | partial |
| `govwin-deltek` | GovWin (Deltek) | US | absent | partial |
| `open-contracting-partnership` | Open Contracting Partnership | GB | unknown | partial |
| `decp-info` | decp.info | FR | strong | verified |
| `data-economie-gouv` | data.economie.gouv.fr | FR | strong | partial |
| `openbar` | OpenBar (Regards Citoyens) | FR | strong | partial |
| `nextend-ai` | Nextend.ai | FR | strong | verified |
| … | _+31 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment public-procurement-intel
```

<!-- catalogue-saas-end -->
