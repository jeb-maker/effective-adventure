# Revue critique (red team) — 0007 Fiche commune intelligente

- **Fiche auditée** : `idees/0007-fiche-commune-intelligente/README.md`
- **Score affiché par la fiche** : 50 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : l'analyse est **honnête et bien sourcée** ; le verdict
> d'écartage est **confirmé**. Orama et Habity couvrent le pitch citoyen gratuitement ;
> le B2G chevauche 0020 (déjà écartée). C2 de la fiche (note 1) est le point
> décisif — le citoyen ne paiera pas.

---

## 1. Affirmations non sourcées

| # | Affirmation | Problème | Verdict |
|---|---|---|---|
| A1 | « douleur tiède et épisodique » (§1) | Plausible, non mesurée — mais cohérent avec l'absence de payeur B2C | **Acceptable** |
| A2 | « 4–6 semaines » effort MVP (§9) | Estimation non sourcée | **À nuancer** — ordre de grandeur plausible |
| A3 | « chat IA conversationnel sans acteur dominant » (§5) | **Non sourcé** comme gap de marché ; FMPC et Orama couvrent les cas structurés | **À nuancer** |

**À mettre au crédit de la fiche** : §4 complet avec checklist cartographie (public,
réutilisations, commercial, OSS, bricolage) ; liens datés 2026-06-23 ; Orama et
Habity correctement identifiés comme concurrents **directs** du pitch ; pas de
sur-estimation du catalogue SaaS seul (OFGL, Orama cités en priorité).

---

## 2. Sur-optimisme : notes de scoring

| Critère | Note fiche | Note revue | Commentaire |
|---|---|---|---|
| C1 | 3 | **3** | Problème réel mais tiède — OK |
| C2 | 1 | **1** | Citoyen = 0 € ; B2G = 0020 saturé — note maximale de prudence justifiée |
| C3 | 5 | **5** | OFGL/DGFiP excellents — OK |
| C4 | 1 | **1** | Orama + Habity + OFGL = saturation frontale |
| C5 | 1 | **1** | Orama gratuit = clone du pitch |
| C6 | 4 | **4** | SQL/RAG conforme si vertical finances strict |
| C7 | 4 | **3** | MVP facile mais **parité Orama/Habity** = mois, pas semaines, pour différenciation visible | 
| C8 | 2 | **2** | Risques commoditisation non maîtrisables — OK |
| C9 | 1 | **1** | Monétisation B2C nulle — OK |

Aucune note **sur-optimiste** détectée. C7 pourrait être abaissée à 3 (parité
feature avec Orama/Habity non triviale) mais n'change pas le verdict.

---

## 3. Risque d'hallucination / RAG(sens) / SQL(chiffres)

- Architecture §6 **conforme** : SQL pour chiffres, RAG pour définitions M57/fiscalité.
- Risque principal : **interprétation politique** (« mauvaise gestion ») injectée
  dans la narration LLM — la fiche le signale en §8.
- Pas de chiffre inventé dans la fiche ; croisements SSMSI/APL mentionnés mais
  **hors MVP finances** — cohérent avec l'avertissement sur le généralisme (0003).

---

## 4. Angles morts

### Concurrents vérifiés le 2026-06-23 (complément §4 fiche)

| Acteur | URL | Impact |
|---|---|---|
| **Orama** | https://oramalimited.com/comment-ca-marche/ | **Clone exact** du pitch : gratuit, API OFGL, comparables, synthèses |
| **Habity** | https://habity.fr/a-propos/methodologie | Libellé « fiche commune intelligente », 107 indicateurs, finances OFGL |
| **Collectiv'Finances** | https://www.banquedesterritoires.fr/produits-services/services-digitaux/collectivfinances-outils-analyse-financiere-collectivite | Gratuit DGS — élimine payeur B2G « expliquer le budget » |
| **NosFinancesLocales fermé** | https://www.nosfinanceslocales.fr | Preuve d'échec pérennisation civic tech pure finances |

### Non mentionnés mais marginaux

- **Territoires.XYZ** (Toucan + namR, Troyes) — portail territorial multi-thèmes ;
  adjacent, pas finances-only citoyen.
- **Fairness** — **non vérifié** comme produit FR finances locales (probable confusion).

La fiche couvre l'essentiel. Aucun concurrent omis ne remettrait en cause l'écartage.

---

## 5. Recalcul du score

| # | Critère | Poids | Note revue | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 9 |
| C2 | Cible solvable | 3 | 1 | 3 |
| C3 | Données / inputs | 3 | 5 | 15 |
| C4 | Espace concurrentiel | 2 | 1 | 2 |
| C5 | Différenciation | 2 | 1 | 2 |
| C6 | Faisabilité technique | 2 | 4 | 8 |
| C7 | Facilité MVP | 2 | 4 | 8 |
| C8 | Maîtrise risques | 2 | 2 | 4 |
| C9 | Monétisation / impact | 2 | 1 | 2 |
| | **Total** | | | **53 / 105** |

**Score /100** : 53 / 105 × 100 = **50** (arrondi)

**Verdict** : ❌ **Écartée** (< 55) — **inchangé**.

Critère éliminatoire **saturation** applicable comme pour 0008/0020 : gratuits
citoyens + officiel OFGL.

---

## 6. Verdict de revue

### **ANALYSE FIABLE** (écartage confirmé)

La fiche 0007 est l'une des analyses les plus complètes du registre sur la
cartographie §4 citoyenne. Le scoring est **prudent** (C2=1, C4=1, C5=1). L'écartage
est justifié : Orama et Habity rendent un produit standalone citoyen **non défendable**.

### 3 actions prioritaires

1. **Ne pas prototyper** 0007 en l'état — fermer le dossier.
2. **Mettre à jour le registre README** : 29/29 analysées, 0007 ❌ 50/100.
3. Si exploration finances locales ultérieure : partir de **0027** (subventions × marchés)
   ou d'un **canal B2B2G** — pas d'un 12ᵉ comparateur citoyen sur OFGL.

---

REVUE 0007 | analyse fiable | score recalculé 50/100 (inchangé) | changement de décision: non
