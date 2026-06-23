# Revue critique (red team) — 0024 Exposition climat/risques d'un portefeuille (B2B)

- **Fiche auditée** : `idees/0024-risque-climat-actifs/README.md`
- **Score affiché par la fiche** : 54 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche est très complète et conclut justement à
> l'écartage (C4=1, C5=1, commoditisation Apify, rachat NamR par Addactis).
> Adversarialement, **C2 est trop généreux** : un marché en **consolidation** où
> les budgets sont **déjà captés** par des suites intégrées ne laisse pas de budget
> *additionnel* à un agrégateur Géorisques. C2 passe de 3 à 2, score de **54 à
> 51/100** — écartage non ambigu.

---

## 1. Affirmations non sourcées (à sourcer / à corriger)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « 143 Md€ d'ici 2050 » (France Assureurs, **cité par Fonciris**) | §1 | Chiffre **de seconde main** (relayé par un acteur commercial). À re-sourcer sur la publication primaire France Assureurs, sinon traiter comme ordre de grandeur. | **À sourcer (primaire)** |
| A2 | « hausse 40 à 120 % vs 2019-2023 » (Odealim, via monimmeuble) | §1 | Idem : source secondaire. Ordre de grandeur acceptable mais à étiqueter. | **À nuancer** |
| A3 | « NamR revendique **35 % du marché MRH** », « tous les établissements bancaires de premier rang », « +100 000 utilisateurs » | §2 | **Auto-déclarations marketing** des concurrents. La fiche les attribue (« revendique ») — à conserver comme tel, **ne pas** en faire des faits de marché. | **À nuancer (déjà attribué)** |
| A4 | « Apify 0,005 $/adresse », « 0,02 $/1000 adresses géocodage » | §4 | Datés, liens directs. Argument fort de commoditisation. **OK.** | **OK** |
| A5 | « **B808** » (élément du seed) | §4 | La fiche **fait déjà le travail de red team** : « non identifié … à clarifier ». Bon réflexe — ne pas réintroduire « B808 » comme concurrent sans source. | **OK (à supprimer du seed)** |

**À mettre au crédit de la fiche** : §4 exceptionnel (10+ concurrents datés +
commoditisation chiffrée + élimination explicite des faux concurrents B808/Cartofriches),
§6 (limites de fiabilité honnêtes : maille 8 km DRIAS, quota 10 req/s).

---

## 2. Sur-optimisme : notes de scoring

| Critère | Note fiche | Note revue | Justification adversariale |
|---|---|---|---|
| **C1** Intensité | 4 | **4** | Douleur réelle, croissante, réglementairement poussée (CSRD ESRS E1, stress tests BCE, Cat Nat). Défendable. |
| **C2** Cible solvable | 3 | **2** | **Trop généreux.** Les payeurs existent mais leurs budgets sont **déjà captés** par des suites intégrées (NamR+Addactis, Deepki ESG, Munich Re) et le marché **se consolide** (Addactis rachète NamR assurance, mai 2025). « Budget existant ≠ budget additionnel » : un agrégateur Géorisques générique n'a pas de ligne budgétaire propre → **2** (mêmes critères que revues 0001/0021). La fiche le dit elle-même : « pas de segment sous-servi démontré ». |
| **C3** Données | 4 | **4** | Excellent pour l'exposition réglementaire actuelle (Géorisques, TRI, RGA 2026, LO 2.0). On pourrait plaider 3 (DRIAS prospectif sans API REST, maille 8 km, insuffisant pour le 2050 visé), mais l'input *brut* est réellement disponible → laissé à 4, avec réserve forte. |
| **C4** Espace libre | 1 | **1** | Plancher justifié : 10+ acteurs + commoditisation Apify. Marché en consolidation. |
| **C5** Différenciation | 1 | **1** | Plancher justifié : batch copiable en un sprint, pas de modèle de vulnérabilité. |
| **C6** Faisabilité | 4 | **4** | Spatial join + API conforme RAG(sens)/SQL(chiffres) pour l'exposition. Défendable. |
| **C7** Facilité MVP | 2 | **2** | MVP technique rapide mais **non crédible** institutionnel (modèles, audit CSRD). Correct. |
| **C8** Risques | 2 | **2** | Concurrence dominante + commoditisation + responsabilité scoring non maîtrisables. Correct. |
| **C9** Monétisation | 2 | **2** | Plancher de prix Fonciris 79 €/mo + Apify 0,005 $/adresse ; budgets captés. Correct. |

**Seule correction retenue : C2 3 → 2.**

---

## 3. Risque d'hallucination / RAG(sens) / SQL(chiffres)

- **Conformité pour l'exposition actuelle : bonne.** Zones sismiques, classes RGA,
  niveaux TRI, compteurs CatNat → champs structurés, SQL traçable avec
  `source_id + date`. LLM cantonné au sens (PPRI, ESRS E1). Conforme §3.
- **Vrai danger (bien posé §6) : la projection.** Scorer un horizon 2050 à partir de
  **DRIAS seul (maille 8 km, pas d'API REST)** sans downscaling ni modèle de
  vulnérabilité produit des chiffres **non auditables** — pire qu'une hallucination
  car « crédibles ». Pour la cible (assureurs/CSRD), un score d'exposition ≠ risque
  financier. C'est ce qui rend le MVP rapide **invendable** (et conforte C7=2, C2=2).
- **Pas de chiffre inventé** dans le scoring de la fiche. RAS.

---

## 4. Angles morts

### Concurrence : cartographie déjà complète — confirmations 2026-06-23
La fiche couvre Callendar, NamR/Addactis, Deepki, Jupiter, Mitiga, Climate X,
Munich Re, AXA Climate, Earthian, Fonciris, Bat-ADAPT. Les acteurs cités par la
commande de revue (Errial, Deepki, Climate X) sont traités :
- **Errial** est l'outil grand public/ERP à l'adresse (traité en 0011, dont 0024
  est le repositionnement) — bien rattaché.
- **Deepki** (module Résilience Climatique) et **Climate X** (Spectra, climate-adjusted
  VaR, marché France) sont présents au §4. Rien à ajouter.

→ Aucun angle mort concurrentiel. La double peine « repositionnement 0011 lui-même
saturé » est correctement identifiée (C4=C5=1).

### Risque sous-pondéré
- **Consolidation = fenêtre qui se ferme** : le rachat de NamR assurance par Addactis
  (mai 2025) montre que même les acteurs établis se font absorber ; un entrant
  arrive après la concentration. Cela justifie autant C2=2 que C8=2.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 4 | 12 |
| C2 | Cible solvable | ×3 | 3 | **2** | 6 |
| C3 | Données | ×3 | 4 | 4 | 12 |
| C4 | Espace concurrentiel libre | ×2 | 1 | 1 | 2 |
| C5 | Différenciation | ×2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité | ×2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | ×2 | 2 | 2 | 4 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **57** | | **54 / 105** |

**Score /100** : 54 / 105 × 100 = **51,4 → 51 / 100**.

**Changement de verdict : NON** (score abaissé). Fiche 54 → revue 51 → seuil < 55 →
❌ Écartée dans les deux cas. La baisse éloigne l'idée du seuil 55 et confirme que
le couple C4=C5=1 + C2=2 n'est pas un point bloquant isolé mais une saturation de fond.

---

## 6. Verdict de revue

### **À CORRIGER À LA MARGE** (verdict écartée confirmé et renforcé)

La fiche 0024 est l'une des plus solides du lot : sourcing dense, élimination
honnête des faux concurrents (B808, Cartofriches), commoditisation chiffrée. Le
seul correctif est **C2 = 2** : sur un marché en consolidation aux budgets captés,
« des payeurs existent » ne vaut pas un budget *additionnel* accessible. Score
51/100, écartage net.

### 3 actions prioritaires
1. **Abaisser C2 à 2** (budget additionnel ≈ nul, marché en consolidation) →
   total 54/105 → 51/100.
2. **Re-sourcer les chiffres de marché** (143 Md€, 40–120 %) sur leurs publications
   **primaires** France Assureurs/Odealim, pas via relais commerciaux.
3. **Ne pas prototyper** ; si verticale explorée, partir d'un **type d'actif non
   couvert par NamR** (tertiaire non résidentiel ? foncières < 50 M€ ?) et le
   **valider par 5 entretiens** avant toute ligne de code — ne pas réinvestir une
   3ᵉ variante « risques × adresse/portefeuille ».

---

REVUE 0024 | à corriger (marge) | score recalculé 51/100 (vs 54) | changement de décision: non (écartée renforcée)
