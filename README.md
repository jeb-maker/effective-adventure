# Discovery produit — validation rigoureuse avant prototype

Ce dépôt est un **registre d'idées produit B2B/B2G** soumises à une **analyse
comparable, sourcée et adversariale**, pour décider quoi **construire**, quoi
**retravailler** ou quoi **abandonner** — avant d'écrire du code.

**Point de départ** : un **payeur** avec une **douleur chère et mal servie**, pas
un jeu de données disponible. La donnée ouverte (data.gouv.fr, INSEE, APIs
publiques…) n'est qu'un **levier possible** parmi d'autres (documents entrants,
APIs tierces, données propriétaires).

**Ce n'est pas** : un catalogue de datasets à exploiter, une base exhaustive du
marché SaaS mondial, ni un produit livré. C'est une **phase 0 de discovery**
documentée — avec pour objectif explicite de **sortir une ou deux idées en
prototype**, pas d'en accumuler indéfiniment.

## Comment ça marche

- La **méthode d'analyse** (grille, règles de preuve, barème de scoring, cycle de
  vie) est dans [`docs/methode-analyse.md`](docs/methode-analyse.md).
- Le **modèle** à copier pour une nouvelle idée est dans
  [`docs/modele-idee.md`](docs/modele-idee.md).
- Les **prompts d'analyse réutilisables** (capture, recherche existant, analyse,
  revue critique) sont dans [`docs/prompts/`](docs/prompts/).
- Le **catalogue des sources complémentaires vérifiées** (croisements, disponibilité)
  est dans [`docs/sources-complementaires.md`](docs/sources-complementaires.md).
- Le **catalogue SaaS** (veille marché RegTech, IDP, GRC, agents IA) est dans
  [`catalogue-saas/`](catalogue-saas/) — méthode dans
  [`docs/catalogue-saas-methode.md`](docs/catalogue-saas-methode.md).
- La **cartographie de l'existant** (SaaS vs public vs OSS — deux cartographies
  distinctes) est dans [`docs/cartographie-existant.md`](docs/cartographie-existant.md).
- Chaque idée vit dans `idees/<id>-<slug>/README.md`.
- Le **registre** ci-dessous est l'index unique (à tenir à jour à chaque ajout).

### Ajouter une idée

1. Partir d'une **douleur + payeur** identifiés (pas d'un dataset repéré).
2. Copier `docs/modele-idee.md` vers `idees/<id>-<slug>/README.md`.
3. Remplir au minimum les sections 1 à 2 (statut 💡 Capturée) ; section 3 si des
   données/APIs sont au cœur du produit.
4. Analyser (sections complètes + scoring), **revue critique obligatoire** (prompt
   03), fixer le statut, mettre à jour le registre.

### Statuts

💡 Capturée · 🔍 En analyse · ✅ Validée (Go) · 🔁 À retravailler · ❌ Écartée · 🚧 Prototype

### Barème (rappel)

Score /100 = `Σ(note×poids) / 105 × 100`. Seuils : **≥ 70 Go**, **55–69 à
retravailler**, **< 55 écartée**. Détail dans `docs/methode-analyse.md`.

### Contrôles automatisés

```bash
python3 scripts/catalogue_saas.py validate
python3 scripts/check_idees.py              # backlog revues manquantes
python3 scripts/catalogue_saas.py segment-readiness
```

CI : [`.github/workflows/validate.yml`](.github/workflows/validate.yml).

---

## Registre des idées

| ID | Idée | Statut | Score | Maj |
|---|---|---|---|---|
| [0001](idees/0001-radar-commande-publique/) | Radar de la commande publique (intelligence d'attribution) | 🔁 À retravailler | 66 ⤵ | 2026-06-20 |
| [0002](idees/0002-observatoire-qualite-donnees/) | Observatoire de qualité des données publiques | 🔁 À retravailler | 57 ⤵ | 2026-06-20 |
| [0003](idees/0003-copilote-territorial-rag/) | Copilote d'études territoriales (RAG) | ❌ Écartée | 46 ⤵ | 2026-06-23 |
| [0004](idees/0004-dossier-immobilier-intelligent/) | Dossier immobilier intelligent (DVF enrichi) | ❌ Écartée | 53 | 2026-06-23 |
| [0005](idees/0005-sante-environnement-local/) | Santé-environnement locale (eau / air) | ❌ Écartée | 44 | 2026-06-23 |
| [0006](idees/0006-assistant-implantation-commerciale/) | Assistant d'implantation commerciale (SIRENE) | ❌ Écartée | 47 ⤵ | 2026-06-23 |
| [0007](idees/0007-fiche-commune-intelligente/) | Fiche commune intelligente (finances locales) | ❌ Écartée | 50 | 2026-06-23 |
| [0008](idees/0008-veille-ao-boamp/) | Veille d'appels d'offres (BOAMP) | ❌ Écartée | 54 | 2026-06-23 |
| [0009](idees/0009-dpe-passoires-thermiques/) | Ciblage rénovation énergétique (passoires thermiques) | 🔁 À retravailler | 57 ⤵ | 2026-06-23 |
| [0010](idees/0010-boussole-aides-publiques/) | Boussole des aides et subventions publiques | ❌ Écartée | 42 ⤵ | 2026-06-20 |
| [0011](idees/0011-risques-adresse/) | Diagnostic des risques par adresse (Géorisques) | ❌ Écartée | 52 ⤵ | 2026-06-23 |
| [0012](idees/0012-acces-aux-soins/) | Observatoire de l'accès aux soins (déserts médicaux) | ❌ Écartée | 44 ⤵ | 2026-06-20 |
| [0013](idees/0013-choisir-son-ecole/) | Aide au choix d'établissement scolaire (IPS) | ❌ Écartée | 51 ⤵ | 2026-06-23 |
| [0014](idees/0014-analyse-electorale-fine/) | Analyse électorale fine (bureau de vote) | ❌ Écartée | 37 ⤵ | 2026-06-20 |
| [0015](idees/0015-deserts-de-mobilite/) | Observatoire des déserts de mobilité | ❌ Écartée | 50 ⤵ | 2026-06-23 |
| [0016](idees/0016-accessibilite-handicap-erp/) | Accessibilité handicap des lieux (ERP) | ❌ Écartée | 48 ⤵ | 2026-06-23 |
| [0017](idees/0017-empreinte-carbone-territoire/) | Empreinte carbone des territoires / PME | ❌ Écartée | 44 ⤵ | 2026-06-20 |
| [0018](idees/0018-transparence-vie-publique/) | Transparence de la vie publique | ❌ Écartée | 46 ⤵ | 2026-06-23 |
| [0019](idees/0019-sourcing-achat-public/) | Sourcing & benchmark prix pour acheteurs publics | ❌ Écartée | 50 ⤵ | 2026-06-23 |
| [0020](idees/0020-benchmark-financier-collectivites/) | Benchmark financier inter-collectivités | ❌ Écartée | 53 | 2026-06-23 |
| [0021](idees/0021-veille-fonciere-amenageurs/) | Veille foncière & urbanisme (promoteurs) | ❌ Écartée | 47 ⤵ | 2026-06-23 |
| [0022](idees/0022-due-diligence-tiers/) | Due diligence & scoring de tiers (B2B) | ❌ Écartée | 50 ⤵ | 2026-06-23 |
| [0023](idees/0023-conformite-open-data-collectivites/) | Conformité publication open data (collectivités) | ❌ Écartée | 44 ⤵ | 2026-06-23 |
| [0024](idees/0024-risque-climat-actifs/) | Exposition climat d'un portefeuille d'actifs (B2B) | ❌ Écartée | 51 ⤵ | 2026-06-23 |
| [0025](idees/0025-coproprietes-renovation-rnic/) | Pilotage rénovation copropriétés (RNIC × DPE × DECP) | 🔁 À retravailler | 60 ⤵ | 2026-06-23 |
| [0026](idees/0026-exposition-parcelles-agricoles/) | Exposition risques parcelles agricoles (RPG × Géorisques × Hub'Eau) | 🔁 À retravailler | 56 | 2026-06-23 |
| [0027](idees/0027-transparence-subventions-marches/) | Transparence subventions × marchés (DECP × SCDL × RNA) | ❌ Écartée | 48 ⤵ | 2026-06-23 |
| [0028](idees/0028-tensions-emploi-territoire/) | Tensions emploi par territoire (France Travail × SIRENE × FiLoSoFi) | 🔁 À retravailler | 56 ⤵ | 2026-06-23 |
| [0029](idees/0029-recordai/) | RecordAI — email/PDF → dossier structuré validé | 🔁 À retravailler | 59 ⤵ | 2026-06-23 |

---

## État actuel

> **Note historique** : les idées 0001–0028 ont été capturées sous l'ancien
> objectif (« produit fondé sur données ouvertes »). Elles restent dans le
> registre comme corpus de test de la méthode. Les **nouvelles idées** suivent
> l'objectif révisé (payeur + douleur d'abord).

- **29 idées** enregistrées, **29 analysées** avec scoring complet et **29 revues**
  adversariales (`revue.md`) — **couverture complète** du registre.
- **Aucune idée ne dépasse le seuil Go (≥ 70)** après red-team.
- **Tête de classement** : **0001** (Radar commande publique) à **66/100** (🔁).
  Ex-leader **0029 RecordAI** : **67 → 59** (benchmark §13 invalidé — CheckFile.ai,
  Rossum, Parseur omis).
- **À retravailler (7)** : 0001 (66), 0002 (57), 0009 (57), 0025 (60), 0026 (56),
  0028 (56), 0029 (59).
- **Écartées (22)** : 0003 (46, ex-🔁), 0004, 0005, 0006, **0007 (50)**, 0008, 0010,
  0011 (ex-🔁), 0012, 0013 (ex-🔁), 0014, 0015, 0016, 0017, 0018, 0019, 0020,
  0021, 0022, 0023, 0024, 0027.
- **Changements de statut post-revue** : 0003, 0011, 0013 passées 🔁 → ❌ ; **0007**
  💡 → ❌ (50/100, saturation Orama/Habity/OFGL).
- **Encore à analyser** : aucune — registre complet.

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
4. **La donnée ouverte seule n'est pas un avantage compétitif** : c'est pourquoi
   l'objectif du dépôt a été reformulé. La valeur défendable vient d'un
   **enrichissement propriétaire**, d'une **distribution captive** (partenariat,
   canal) ou d'une **niche réglementaire pointue** — pas du dataset.

### Règle de priorisation (post-discovery)

1. **Ne plus ouvrir de nouvelles idées** tant qu'aucune des 7 candidates 🔁 ne
   franchit le seuil Go (≥ 70) après pivot documenté.
2. ~~Appliquer le red-team~~ — **fait** (28/28 revues sur statuts finaux).
3. **Prototyper une seule idée** qui franchit le seuil — ou **fermer le registre**
   : après red-team complet, **aucune idée ≥ 70** ; la décision est un pivot
   explicite (0001 niche attribution ? 0029 micro-vertical ?) ou arrêt.
