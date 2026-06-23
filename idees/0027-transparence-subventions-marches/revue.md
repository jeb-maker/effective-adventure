# Revue critique (red team) — 0027 Transparence subventions × marchés publics

- **Fiche auditée** : `idees/0027-transparence-subventions-marches/README.md`
- **Score affiché par la fiche** : 51 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche écarte justement l'idée (pas de payeur,
> risque institutionnel beta.gouv). Mais elle contient une **affirmation
> factuellement fausse** — « **Aucun outil ne propose ce triptyque requêtable** » —
> démentie par **Éclaireur Public** (Anticor + Data for Good, lancé 19 fév. 2025),
> qui croise **subventions + marchés** par collectivité avec un indice A–E grand
> public, et par **DépensesPubliques.fr** qui affiche déjà DECP **et** SCDL. C4 et
> C5 passent de 2 à 1, score de **51 à 48/100** — écartage cimenté.

---

## 1. Affirmations non sourcées ou fausses (à corriger / supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| **A1** | « **Aucun outil ne propose ce triptyque requêtable** en open data, alors que chaque brique existe séparément » | §1 | **FAUX et non sourcé.** Démenti par **Éclaireur Public** (subventions + marchés, par collectivité, comparatif, A–E, 100 % data.gouv.fr — https://eclaireurpublic.fr/methodologie , 2026-06-23) et par **DépensesPubliques.fr** qui affiche DECP **et** subventions SCDL sur la fiche commune (https://depensespubliques.fr/donnees-sources , 2026-06-23). C'est l'affirmation-pivot du « pourquoi nous » → à supprimer/corriger. | **À supprimer / corriger** |
| A2 | « VigiCité … 6 763 élus … 2,3 M marchés publics » | §4 | Bien sourcé et daté (2026-06-23). OK. | **OK** |
| A3 | « Data.Subvention (beta.gouv.fr) … accès restreint aux agents publics » | §4 | Bien sourcé. Risque institutionnel correctement identifié. OK. | **OK** |
| A4 | Footer manquant : la fiche **n'a pas** de ligne récapitulative finale « 0027 \| … \| ❌ Écartée \| 51/100 \| … » comme les autres fiches du dépôt | §11 | Incohérence de format (toutes les autres fiches du lot ont cette ligne). | **À corriger (format)** |

**À mettre au crédit de la fiche** : §3bis (croisements bien posés), §6 (RAG/SQL
strict, score de confiance fuzzy-matching), et l'identification du **risque
éliminatoire** (Data.Subvention/beta.gouv) — l'essentiel du raisonnement tient.

---

## 2. Sur-optimisme : notes de scoring

| Critère | Note fiche | Note revue | Justification adversariale |
|---|---|---|---|
| **C1** Intensité | 3 | **3** | Niche réelle mais étroite (journalistes, ONG). Correct. |
| **C2** Cible solvable | 2 | **2** | Aucun payeur B2B solide (rédactions = budget faible, ONG = dons, citoyens = gratuit attendu). Correct — on pourrait plaider 1, mais 2 reste acceptable. |
| **C3** Données | 3 | **3** | DECP ✅ + RNA ✅ consolidés ; **SCDL fragmenté** (pas de dump national). Correct. |
| **C4** Espace libre | 2 | **1** | **Trop généreux.** La fiche le note « étroit » mais Éclaireur Public fait **déjà** subventions+marchés par collectivité ; DépensesPubliques affiche les deux ; VigiCité fait DECP×RNA ; Data.Subvention consolide le SCDL. Le terrain n'est pas « résiduel », il est **occupé** → **1**. |
| **C5** Différenciation | 2 | **1** | **Trop généreux.** Le « triptyque » revendiqué est déjà livré (Éclaireur Public) ou trivialement extensible (VigiCité AGPL). La donnée ouverte n'est pas un avantage. Aucun fossé → **1**. |
| **C6** Faisabilité | 4 | **4** | SQL strict + score de confiance fuzzy : conforme RAG(sens)/SQL(chiffres). Défendable. |
| **C7** Facilité MVP | 3 | **3** | MVP 4–6 sem. sur quelques jeux SCDL ; consolidation nationale = chantier continu. Correct. |
| **C8** Risques | 2 | **2** | Risque éliminatoire institutionnel (beta.gouv) + extension VigiCité. Correct. |
| **C9** Monétisation | 2 | **2** | Impact élevé, **non monétisable** ; pas de modèle. Correct. |

**Corrections retenues : C4 2 → 1 et C5 2 → 1.**

---

## 3. Risque d'hallucination / RAG(sens) / SQL(chiffres)

- **Conformité : bonne.** Montants en SQL traçable (DECP `uid`/`modification_id`,
  agrégats par SIREN) ; sens juridique de la subvention en RAG ; **score de
  confiance obligatoire** sur le matching RNA↔SCDL (fuzzy sur dénomination). C'est
  exactement le bon garde-fou. **Pas de chiffre inventé.**
- **Réserve sémantique héritée** : DECP `montant` = notification / max accord-cadre
  ≠ dépense réelle (cf. revue 0001) ; agréger « part marchés vs subventions » d'un
  bénéficiaire peut être exact et trompeur. À documenter dans le produit (déjà
  esquissé §3).
- **Matching RNA/SCDL** : identifiants hétérogènes → risque de **faux positifs**
  nominatifs (associations homonymes) à fort risque réputationnel. Le score de
  confiance est nécessaire mais pas suffisant ; prévoir un seuil de non-affichage.

---

## 4. Angles morts (concurrents non mentionnés — 2026-06-23)

### Le concurrent décisif absent de la fiche : **Éclaireur Public**
- **Éclaireur Public** (Anticor + Data for Good, lancé **19 février 2025**) :
  plateforme **grand public** qui croise **subventions (SCDL) ET marchés publics
  (DECP)** par collectivité (communes, intercommunalités, départements, régions),
  produit **3 indices A–E** (subventions / marchés / agrégé) et permet la
  **comparaison entre territoires**, exclusivement à partir de data.gouv.fr
  (https://eclaireurpublic.fr/methodologie ,
  https://jss.fr/post/anticor-et-data-for-good-lancent-eclaireur-public-une-plateforme-pour-scruter-les-budgets-locaux ,
  consultés 2026-06-23). **C'est le produit décrit par le seed**, déjà en ligne,
  gratuit, porté par deux organisations établies. Il invalide A1 et fonde C4=C5=1.

### Autres recouvrements sous-pondérés
- **DépensesPubliques.fr** : affiche **DECP + subventions SCDL** sur la fiche
  commune (https://depensespubliques.fr/donnees-sources , 2026-06-23) — déjà un
  croisement marchés × subventions grand public.
- **OpenBar (Regards Citoyens)** : présent dans le catalogue du dépôt
  (`public-procurement-intel`, FR, `partial`) comme outil DECP de la communauté
  Regards Citoyens — acteur civique additionnel sur le segment marchés publics, à
  citer au §4 plutôt que de le laisser au seul catalogue.
- **decp.info** (Colin Maudry, v2.7.3 du 2026-04-20) : déjà cité — exploration DECP
  open source, brique réutilisable par tout concurrent civique.

→ Conclusion : le segment « transparence flux financiers ↔ collectivités » est
**activement occupé** par des acteurs civiques **et** un programme d'État
(Data.Subvention). L'espace n'est pas résiduel.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | 3 | 9 |
| C2 | Cible solvable | ×3 | 2 | 2 | 6 |
| C3 | Données | ×3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 2 | **1** | 2 |
| C5 | Différenciation | ×2 | 2 | **1** | 2 |
| C6 | Faisabilité & fiabilité | ×2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | ×2 | 3 | 3 | 6 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **54** | | **50 / 105** |

**Score /100** : 50 / 105 × 100 = **47,6 → 48 / 100**.

**Changement de verdict : NON** (score abaissé). Fiche 51 → revue 48 → seuil < 55 →
❌ Écartée dans les deux cas. La baisse retire toute ambiguïté : l'idée n'est pas
« limite », elle est **occupée** (Éclaireur Public) **et** sans modèle économique.

---

## 6. Verdict de revue

### **À CORRIGER** (verdict écartée confirmé et renforcé)

Le raisonnement économique de la fiche (pas de payeur, risque beta.gouv) est juste,
mais l'analyse **concurrentielle est datée** : elle a manqué **Éclaireur Public**,
qui livre exactement le triptyque revendiqué depuis février 2025. L'affirmation A1
(« aucun outil ne propose ce triptyque ») est **fausse** et doit être supprimée.
Avec C4=C5=1, le score tombe à 48/100 : écartage net, motivé autant par la
saturation civique que par l'absence de modèle économique.

### 3 actions prioritaires
1. **Supprimer/corriger A1** et **ajouter Éclaireur Public** (+ DépensesPubliques,
   OpenBar) au §4 (liens datés 2026-06-23) ; abaisser **C4 et C5 à 1**.
2. **Recalculer** : total 50/105 → **48/100** ; ajouter la **ligne récapitulative
   finale** manquante au format du dépôt.
3. **Ne pas prototyper** ; ne rouvrir que si (a) un payeur B2B concret > 10 k€/an
   est identifié **et** (b) un angle échappant à Éclaireur Public/Data.Subvention
   est démontré — sinon, contribuer à l'écosystème civique existant.

---

REVUE 0027 | à corriger | score recalculé 48/100 (vs 51) | changement de décision: non (écartée renforcée)
