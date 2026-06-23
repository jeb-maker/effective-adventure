# Veille d'appels d'offres (BOAMP) — agrégateur classique

- **ID** : 0008
- **Statut** : ❌ Écartée
- **Score** : — / 100 (écartée : marché saturé)
- **Dernière mise à jour** : 2026-06-20
- **Pitch (1 phrase)** : Agréger les avis de marché à venir (BOAMP/TED/profils
  acheteurs) avec alertes et scoring.

---

## 1. Problème / douleur
Réelle pour les répondants aux AO, mais déjà massivement adressée.

## 4. Existant / concurrence (très saturé)
Vecteur Plus, France Marchés, Synapse, Doaken, Olra, PublikConnect (49 € HT),
AlertOffres (29,99 €), AOS, Explore, Marchés Online, Dématis, Centrale des
Marchés — plusieurs avec IA (scoring, analyse DCE, mémoire technique).
Sources (consultées 2026-06-20) :
https://olra.fr/blog/alternatives-synapse-france-marches-comparatif ,
https://remporte.fr/blog/plateformes-appels-offres-comparatif/

## 11. Verdict & décision
❌ **Écartée** en frontal. La valeur résiduelle est sur l'**analyse
d'attribution** (passé), traitée dans l'idée **0001** — pas sur la veille
(avenir). Ne pas attaquer ce segment directement.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0008-veille-ao-boamp` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `public-procurement-intel` — Intelligence marchés publics

Fichier : [`catalogue-saas/vendors/public-procurement-intel.json`](../../catalogue-saas/vendors/public-procurement-intel.json) (20 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `marchespublics-ai` | marchespublics.ai | FR | strong | partial |
| `maitre-ao` | Maître AO | FR | strong | partial |
| `aws-boamp` | BOAMP (open data) | FR | strong | verified |
| `achatpublic` | PLACE (achatpublic.com) | FR | strong | partial |
| `tussell` | Tussell | GB | absent | partial |
| `spend-network` | Spend Network | GB | absent | partial |
| `govwin-deltek` | GovWin (Deltek) | US | absent | partial |
| `open-contracting-partnership` | Open Contracting Partnership | GB | unknown | partial |
| `decp-info` | decp.info | FR | strong | partial |
| `data-economie-gouv` | data.economie.gouv.fr | FR | strong | partial |
| `openbar` | OpenBar (Regards Citoyens) | FR | strong | partial |
| `nextend-ai` | Nextend.ai | FR | strong | partial |
| … | _+8 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment public-procurement-intel
```

<!-- catalogue-saas-end -->
