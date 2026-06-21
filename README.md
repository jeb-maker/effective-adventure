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
- Le **catalogue des sources complémentaires vérifiées** (croisements, disponibilité)
  est dans [`docs/sources-complementaires.md`](docs/sources-complementaires.md).
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
| [0007](idees/0007-fiche-commune-intelligente/) | Fiche commune intelligente (finances locales) | 🔁 À retravailler | 59 | 2026-06-21 |
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
| [0019](idees/0019-sourcing-achat-public/) | Sourcing & benchmark prix pour acheteurs publics | ❌ Écartée | 53 | 2026-06-20 |
| [0020](idees/0020-benchmark-financier-collectivites/) | Benchmark financier inter-collectivités | ❌ Écartée | 53 | 2026-06-20 |
| [0021](idees/0021-veille-fonciere-amenageurs/) | Veille foncière & urbanisme (promoteurs) | ❌ Écartée | 50 | 2026-06-20 |
| [0022](idees/0022-due-diligence-tiers/) | Due diligence & scoring de tiers (B2B) | ❌ Écartée | 53 | 2026-06-20 |
| [0023](idees/0023-conformite-open-data-collectivites/) | Conformité publication open data (collectivités) | ❌ Écartée | 47 | 2026-06-20 |
| [0024](idees/0024-risque-climat-actifs/) | Exposition climat d'un portefeuille d'actifs (B2B) | ❌ Écartée | 54 | 2026-06-20 |
| [0025](idees/0025-coproprietes-renovation-rnic/) | Pilotage rénovation copropriétés (RNIC × DPE × DECP) | 🔁 À retravailler | 64 | 2026-06-21 |
| [0026](idees/0026-exposition-parcelles-agricoles/) | Exposition risques parcelles agricoles (RPG × Géorisques × Hub'Eau) | 💡 Capturée | — | 2026-06-21 |
| [0027](idees/0027-transparence-subventions-marches/) | Transparence subventions × marchés (DECP × SCDL × RNA) | 💡 Capturée | — | 2026-06-21 |
| [0028](idees/0028-tensions-emploi-territoire/) | Tensions emploi par territoire (France Travail × SIRENE × FiLoSoFi) | 💡 Capturée | — | 2026-06-21 |

---

## État actuel

- **28 idées** enregistrées, dont **21 analysées** avec scoring complet (dont 0007
  et 0025, juin 2026) et **3 idées capturées** restantes (0026–0028).
- **8 idées enrichies** avec croisements et sources complémentaires vérifiées
  (0003, 0006, 0007, 0009, 0018, 0019, 0021, 0024) — voir
  [`docs/sources-complementaires.md`](docs/sources-complementaires.md).
- **2 analyses complètes** ajoutées (0007 → 59/100, 0025 → 64/100).
- **6 idées passées en revue critique adversariale** (`revue.md` dans leur
  dossier). Effet **massif** : tous les scores ont baissé et **aucune idée ne
  dépasse aujourd'hui le seuil Go (≥70)**.
- **Vague B2B/B2G (0019–0024)** : 6 idées « payeur pro + donnée chiffrée »
  testées avec consigne de chasse aux concurrents → **toutes écartées (47–54)**,
  marchés déjà occupés (marchespublics.ai, OFGL, Kel Foncier, Pappers, NamR…).
- **Tête de classement** : **0001** (Radar de la commande publique) à **66/100**
  (🔁 à retravailler) — meilleure idée mais plus « validée ». La revue a trouvé
  des concurrents directs omis (Maître AO, Nextend.ai, marchespublics.ai) et un
  piège sémantique (`montant` DECP ≠ dépense réelle).
- **À retravailler** : 0001 (66), 0002 (57), 0009 (60), 0011 (60), 0013 (59),
  0003 (—).
- **Écartées** : 0004, 0005, 0006, 0008, 0010, 0012, 0014, 0015, 0016, 0017,
  0018, 0019, 0020, 0021, 0022, 0023, 0024 — conservées avec leur analyse.
- **Encore à analyser** : 0007 (💡 capturée), 0025, 0026, 0027, 0028 (💡 capturées).

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
4. **La donnée ouverte seule n'est pas un avantage compétitif** : elle est par
   définition accessible à tous. Les 24 idées confirment que la valeur défendable
   vient d'un **enrichissement propriétaire**, d'une **distribution captive**
   (partenariat, canal) ou d'une **niche réglementaire pointue** — pas du dataset.

### Piste pour la suite

Arrêter de chercher « quel dataset exploiter » (tous sont déjà exploités).
Partir plutôt d'un **payeur précis avec une douleur chère et mal servie**, puis
voir si une donnée ouverte y répond — l'inverse de la démarche menée jusqu'ici.
