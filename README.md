# Répertoire d'idées — données publiques (data.gouv.fr)

Ce dépôt collecte des **idées de produits/projets fondés sur les données
ouvertes** (principalement data.gouv.fr) et les soumet à une **analyse
rigoureuse et comparable**.

## Comment ça marche

- La **méthode d'analyse** (grille, règles de preuve, barème de scoring, cycle de
  vie) est dans [`docs/methode-analyse.md`](docs/methode-analyse.md).
- Le **modèle** à copier pour une nouvelle idée est dans
  [`docs/modele-idee.md`](docs/modele-idee.md).
- Les **prompts d'analyse réutilisables** (capture, recherche existant, analyse,
  revue critique) sont dans [`docs/prompts/`](docs/prompts/).
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
| [0001](idees/0001-radar-commande-publique/) | Radar de la commande publique (intelligence d'attribution) | 🔁 À retravailler | 66 ⤵ | 2026-06-20 |
| [0002](idees/0002-observatoire-qualite-donnees/) | Observatoire de qualité des données publiques | 🔁 À retravailler | 57 ⤵ | 2026-06-20 |
| [0003](idees/0003-copilote-territorial-rag/) | Copilote d'études territoriales (RAG) | 🔁 À retravailler | — | 2026-06-20 |
| [0004](idees/0004-dossier-immobilier-intelligent/) | Dossier immobilier intelligent (DVF enrichi) | ❌ Écartée | — | 2026-06-20 |
| [0005](idees/0005-sante-environnement-local/) | Santé-environnement locale (eau / air) | ❌ Écartée | — | 2026-06-20 |
| [0006](idees/0006-assistant-implantation-commerciale/) | Assistant d'implantation commerciale (SIRENE) | ❌ Écartée | 50 | 2026-06-20 |
| [0007](idees/0007-fiche-commune-intelligente/) | Fiche commune intelligente (finances locales) | 💡 Capturée | — | 2026-06-20 |
| [0008](idees/0008-veille-ao-boamp/) | Veille d'appels d'offres (BOAMP) | ❌ Écartée | — | 2026-06-20 |
| [0009](idees/0009-dpe-passoires-thermiques/) | Ciblage rénovation énergétique (passoires thermiques) | 🔁 À retravailler | 60 | 2026-06-20 |
| [0010](idees/0010-boussole-aides-publiques/) | Boussole des aides et subventions publiques | ❌ Écartée | 42 ⤵ | 2026-06-20 |
| [0011](idees/0011-risques-adresse/) | Diagnostic des risques par adresse (Géorisques) | 🔁 À retravailler | 60 | 2026-06-20 |
| [0012](idees/0012-acces-aux-soins/) | Observatoire de l'accès aux soins (déserts médicaux) | ❌ Écartée | 44 ⤵ | 2026-06-20 |
| [0013](idees/0013-choisir-son-ecole/) | Aide au choix d'établissement scolaire (IPS) | 🔁 À retravailler | 59 | 2026-06-20 |
| [0014](idees/0014-analyse-electorale-fine/) | Analyse électorale fine (bureau de vote) | ❌ Écartée | 37 ⤵ | 2026-06-20 |
| [0015](idees/0015-deserts-de-mobilite/) | Observatoire des déserts de mobilité | ❌ Écartée | 54 | 2026-06-20 |
| [0016](idees/0016-accessibilite-handicap-erp/) | Accessibilité handicap des lieux (ERP) | ❌ Écartée | 52 | 2026-06-20 |
| [0017](idees/0017-empreinte-carbone-territoire/) | Empreinte carbone des territoires / PME | ❌ Écartée | 44 ⤵ | 2026-06-20 |
| [0018](idees/0018-transparence-vie-publique/) | Transparence de la vie publique | ❌ Écartée | 50 | 2026-06-20 |

---

## État actuel

- **18 idées** enregistrées, dont 13 analysées avec scoring complet.
- **6 idées passées en revue critique adversariale** (`revue.md` dans leur
  dossier). Effet **massif** : tous les scores ont baissé et **aucune idée ne
  dépasse aujourd'hui le seuil Go (≥70)**.
- **Tête de classement** : **0001** (Radar de la commande publique) à **66/100**
  (🔁 à retravailler) — meilleure idée mais plus « validée ». La revue a trouvé
  des concurrents directs omis (Maître AO, Nextend.ai, marchespublics.ai) et un
  piège sémantique (`montant` DECP ≠ dépense réelle).
- **À retravailler** : 0001 (66), 0002 (57), 0009 (60), 0011 (60), 0013 (59),
  0003 (—).
- **Écartées** : 0004, 0005, 0006, 0008, 0010, 0012, 0014, 0015, 0016, 0017,
  0018 — conservées avec leur analyse.
- **Encore à analyser** : 0007 (💡 capturée).

> ⤵ dans le registre = score abaissé après revue critique.

### Enseignements transverses

1. **Le red-team est indispensable** : le 1er passage d'analyse (même soigné)
   sur-note systématiquement « espace libre » (C4) et « qui paie » (C2). Les
   revues ont trouvé des concurrents réels dans presque tous les cas.
2. La quasi-totalité des idées « grand public / cartographie » sont **déjà
   servies par un service public gratuit** (Errial, acceslibre, CartoSanté, Go
   Rénove, udata-hydra…) ou saturées côté commercial.
3. Même les idées B2B « donnée chiffrée traçable » ont déjà des concurrents :
   l'avantage doit venir d'une **niche/distribution**, pas de la donnée seule.
