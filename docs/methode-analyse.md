# Méthode d'analyse des idées

Ce document définit **comment** on capture une idée puis comment on la soumet à
une **analyse rigoureuse**. L'objectif est que toutes les idées soient évaluées
avec la même grille, les mêmes règles de preuve et le même barème, afin de
pouvoir les **comparer honnêtement**.

---

## 1. Cycle de vie d'une idée

Chaque idée a un **statut** unique, qui évolue dans le temps :

| Statut | Emoji | Signification |
|---|---|---|
| Capturée | 💡 | Idée notée, pas encore analysée |
| En analyse | 🔍 | Analyse rigoureuse en cours |
| Validée (Go) | ✅ | Analyse favorable, candidate à un prototype |
| À retravailler | 🔁 | Potentiel réel mais un point bloquant à lever |
| Écartée | ❌ | Analyse défavorable (saturé, risqué, peu de valeur) |
| Prototype | 🚧 | Un MVP est en cours de construction |

Règle : on **n'écarte jamais une idée sans preuve**. Une idée écartée garde son
analyse, pour ne pas la reproposer naïvement plus tard.

---

## 2. Règles de preuve (anti-bullshit)

L'analyse n'a de valeur que si elle est sourcée. Trois règles non négociables :

1. **Toute affirmation sur l'existant / la concurrence** doit être accompagnée
   d'un lien et d'une date de consultation. « C'est déjà fait » sans lien = non
   recevable.
2. **Toute donnée chiffrée** (taille de marché, prix concurrent, volume de
   dataset) doit citer sa source.
3. **Toute source de données** envisagée doit préciser : URL, licence,
   format, fraîcheur/fréquence de mise à jour, et limites connues (trous de
   couverture, qualité).

---

## 3. Principe de fiabilité (anti-hallucination)

Beaucoup de ces idées impliquent un LLM. Règle d'architecture imposée à toutes :

- **RAG** uniquement sur le **sens** (métadonnées, documentation, définitions,
  schémas).
- **SQL / requêtes structurées** uniquement sur les **chiffres**.
- Le LLM **n'invente jamais un nombre**. Tout chiffre affiché doit être traçable
  jusqu'à sa source (dataset + date + requête).
- Un « je ne sais pas » franc est préférable à une réponse plausible mais fausse.

Une idée dont les chiffres reposeraient sur du RAG pur est, par défaut, notée bas
sur le critère de fiabilité.

---

## 4. Grille d'analyse (sections obligatoires)

Chaque idée analysée doit renseigner ces sections (voir `modele-idee.md`) :

1. **Problème / douleur** — quel problème réel, pour qui, à quel point ça fait mal.
2. **Cible & qui paie** — utilisateurs vs payeurs (ce n'est pas toujours pareil).
3. **Données sources** — datasets, APIs, licence, fraîcheur, fiabilité, limites.
4. **Existant / concurrence** — ce qui existe déjà (avec liens datés).
5. **Différenciation** — pourquoi nous, et est-ce défendable / imitable.
6. **Faisabilité & fiabilité technique** — archi, et respect du principe §3.
7. **Monétisation / impact** — modèle économique ou impact visé.
8. **Risques** — ce qui peut tuer le projet.
9. **Effort MVP** — périmètre minimal crédible.
10. **Scoring** — la grille pondérée du §5.
11. **Verdict & décision** — statut + justification + prochaine étape.

---

## 5. Barème de scoring pondéré

Chaque critère est noté de **1 à 5** (1 = très défavorable, 5 = très favorable),
puis multiplié par son poids. Pour les critères « inversés » (risque, effort),
**un score haut = situation favorable** (peu de risque, faible effort).

| # | Critère | Poids | Ancrage 1 (mauvais) | Ancrage 5 (excellent) |
|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | gadget, besoin tiède | douleur forte, récurrente |
| C2 | Cible solvable (qui paie) | ×3 | personne ne paie | payeurs identifiés, budget existant |
| C3 | Disponibilité & fiabilité des données | ×3 | données absentes/sales | données prêtes, propres, traçables |
| C4 | Espace concurrentiel libre | ×2 | saturé | quasi vierge au niveau produit |
| C5 | Différenciation défendable | ×2 | copiable en un week-end | avantage durable |
| C6 | Faisabilité & fiabilité technique | ×2 | repose sur du RAG fragile | chiffres SQL/objectifs traçables |
| C7 | Facilité du MVP (effort faible) | ×2 | chantier lourd | MVP rapide, données prêtes |
| C8 | Maîtrise des risques | ×2 | risques majeurs non maîtrisés | risques faibles/maîtrisés |
| C9 | Monétisation / impact | ×2 | ni revenu ni impact | fort revenu **ou** fort impact |

**Calcul du score final :**

```
score_brut    = Σ (note_critère × poids)        # max = 105
score_sur_100 = round(score_brut / 105 × 100)
```

**Seuils de décision :**

| Score /100 | Décision |
|---|---|
| ≥ 70 | ✅ Go — candidate à prototype |
| 55 – 69 | 🔁 À retravailler — lever le point faible |
| < 55 | ❌ Écartée |

Le score n'est pas un oracle : un point critique éliminatoire (ex. illégalité,
risque sanitaire, donnée inexistante) peut écarter une idée **malgré** un bon
score. Dans ce cas, le justifier explicitement dans le verdict.

---

## 6. Workflow pratique

1. **Capturer** : copier `docs/modele-idee.md` vers
   `idees/<id>-<slug>/README.md`, remplir au minimum les sections 1 à 3.
   Statut = 💡 Capturée.
2. **Analyser** : compléter toutes les sections + le scoring. Statut = 🔍.
3. **Décider** : appliquer les seuils §5, fixer le statut final.
4. **Indexer** : ajouter/mettre à jour la ligne dans le registre du `README.md`
   racine (id, titre, statut, score, date).

> Convention d'`id` : numérotation à 4 chiffres (`0001`, `0002`, …) dans l'ordre
> de capture. Le slug est en minuscules, mots séparés par des tirets.

Pour exécuter ce workflow de façon reproductible, des **prompts prêts à l'emploi**
(un par étape) sont disponibles dans [`prompts/`](prompts/). Ils renvoient à ce
document plutôt que de redéfinir les règles.
