# Répertoire d'idées — données publiques (data.gouv.fr)

Ce dépôt collecte des **idées de produits/projets fondés sur les données
ouvertes** (principalement data.gouv.fr) et les soumet à une **analyse
rigoureuse et comparable**.

## Comment ça marche

- La **méthode d'analyse** (grille, règles de preuve, barème de scoring, cycle de
  vie) est dans [`docs/methode-analyse.md`](docs/methode-analyse.md).
- Le **modèle** à copier pour une nouvelle idée est dans
  [`docs/modele-idee.md`](docs/modele-idee.md).
- Chaque idée vit dans `idees/<id>-<slug>/README.md`.
- Le **registre** ci-dessous est l'index unique (à tenir à jour à chaque ajout).

### Ajouter une idée

1. Copier `docs/modele-idee.md` vers `idees/<id>-<slug>/README.md`.
2. Remplir au minimum les sections 1 à 3 (statut 💡 Capturée).
3. Quand on l'analyse : compléter toutes les sections + le scoring, fixer le
   statut, puis mettre à jour le registre.

### Statuts

💡 Capturée · 🔍 En analyse · ✅ Validée (Go) · 🔁 À retravailler · ❌ Écartée · 🚧 Prototype

### Barème (rappel)

Score /100 = `Σ(note×poids) / 105 × 100`. Seuils : **≥ 70 Go**, **55–69 à
retravailler**, **< 55 écartée**. Détail dans `docs/methode-analyse.md`.

---

## Registre des idées

| ID | Idée | Statut | Score | Maj |
|---|---|---|---|---|
| [0001](idees/0001-radar-commande-publique/) | Radar de la commande publique (intelligence d'attribution) | ✅ Validée | **76** | 2026-06-20 |
| [0002](idees/0002-observatoire-qualite-donnees/) | Observatoire de qualité des données publiques | 🔁 À retravailler | 71 | 2026-06-20 |
| [0003](idees/0003-copilote-territorial-rag/) | Copilote d'études territoriales (RAG) | 🔁 À retravailler | — | 2026-06-20 |
| [0004](idees/0004-dossier-immobilier-intelligent/) | Dossier immobilier intelligent (DVF enrichi) | ❌ Écartée | — | 2026-06-20 |
| [0005](idees/0005-sante-environnement-local/) | Santé-environnement locale (eau / air) | ❌ Écartée | — | 2026-06-20 |
| [0006](idees/0006-assistant-implantation-commerciale/) | Assistant d'implantation commerciale (SIRENE) | 💡 Capturée | — | 2026-06-20 |
| [0007](idees/0007-fiche-commune-intelligente/) | Fiche commune intelligente (finances locales) | 💡 Capturée | — | 2026-06-20 |
| [0008](idees/0008-veille-ao-boamp/) | Veille d'appels d'offres (BOAMP) | ❌ Écartée | — | 2026-06-20 |

---

## État actuel

- **Candidate prioritaire** : 0001 (Radar de la commande publique).
- **Pari à fort sens / à retravailler** : 0002 (qui paie ?), 0003 (recentrer).
- Idées écartées conservées avec leur analyse pour ne pas les reproposer.
