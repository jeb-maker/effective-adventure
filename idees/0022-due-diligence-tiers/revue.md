# Revue critique (red team) — 0022 Due diligence & scoring de tiers (B2B)

- **Fiche auditée** : `idees/0022-due-diligence-tiers/README.md`
- **Score affiché par la fiche** : 53 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche conclut justement à l'écartage et identifie
> bien le « plafond de verre » (pas de données de paiement → scoring non
> compétitif). Adversarialement, elle reste **trop généreuse sur C3** : noter les
> données « 4/5 » revient à juger la disponibilité **brute** alors que les
> **inputs qui font la valeur du produit** (paiement, réseau, historique) sont
> **absents** de l'open data. C3 passe de 4 à 3 et le score de **53 à 50/100** —
> écartage confirmé et renforcé.

---

## 1. Affirmations non sourcées (à sourcer / à corriger)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « 47 000 € par incident en moyenne, source Euler Hermes 2024 » | §1 | La fiche **se prémunit déjà** (« à traiter comme argument marketing du concurrent, non comme étude indépendante vérifiée »). Bon réflexe — laisser tel quel, ne jamais l'utiliser comme preuve dans le scoring. | **OK (déjà nuancé)** |
| A2 | « Pappers … API **30 €/mois** (500 crédits) » | §2/§4 | **À actualiser** : les sources 2026 indiquent désormais l'API Pappers à **~19,90–20 €/mois pour 500 crédits**, avec **100 requêtes/mois gratuites** (https://hayot-expertise.fr/blog/pappers-outil-recherche-entreprise-avis , https://kbisenligne.com/guides/pappers-api-integration , consultés 2026-06-23). Le plancher de prix est donc **encore plus bas** que dans la fiche → aggrave C2/C9. | **À corriger (aggrave le verdict)** |
| A3 | « Annuaire des Entreprises … 50+ sources … concurrent direct gratuit » | §3/§4 | Bien sourcé (page sources datée). Cœur de l'argument C4. **OK.** | **OK** |
| A4 | « RiskSonnar 9,90 €/scan ; 19–649 €/mois » ; « Infolegale dès 1 980 €/an » | §2/§4 | Datés et plausibles. À mettre au crédit de la fiche. | **OK** |
| A5 | « 2 000–5 000 annonces BODACC/jour (RiskSonnar blog, ordre de grandeur) » | §3 | Honnêtement étiqueté « ordre de grandeur ». OK. | **OK** |

**À mettre au crédit de la fiche** : §4 exhaustif (État + freemium + premium + SRM
+ réutilisations), tableau RAG/SQL §6 très propre, et l'aveu central « score
open-data = règle métier banale » qui fonde l'écartage.

---

## 2. Sur-optimisme : notes de scoring

| Critère | Note fiche | Note revue | Justification adversariale |
|---|---|---|---|
| **C1** Intensité | 4 | **4** | Due diligence récurrente et coûteuse si manuelle. Défendable. |
| **C2** Cible solvable | 2 | **2** | Correct. Budgets ETI captés (Infolegale, Altares…) ; PME sur le gratuit (Annuaire, Pappers) ; pas de 1 (certains paient), pas de 3. La baisse de prix Pappers (A2) conforte 2. |
| **C3** Données | 4 | **3** | **Trop généreux.** Le rubric C3 = « disponibilité & fiabilité des **inputs** » *pour le produit visé*. Or le produit visé est un **scoring crédible**, dont les inputs décisifs (expérience de paiement DunTrade, réseau, scores propriétaires) **ne sont pas en open data** — la fiche le démontre elle-même (§3, §8.2 « plafond de verre »). Des briques open SQL-ables ne valent pas 4 quand la donnée *différenciante* est structurellement absente → **3**. |
| **C4** Espace libre | 1 | **1** | Plancher justifié : État + Pappers + Societe.com + RiskSonnar + 4 premium + SRM. |
| **C5** Différenciation | 1 | **1** | Plancher justifié : seed déjà implémenté par ≥3 produits. |
| **C6** Faisabilité | 4 | **4** | Agrégation SQL + règles traçables conformes RAG(sens)/SQL(chiffres). Défendable (la *valeur* prédictive est faible, mais la *fiabilité technique* du calcul est réelle). |
| **C7** Facilité MVP | 3 | **3** | ETL multi-sources (comptes INPI/INSEE, dédoublonnage SIREN/SIRET, normalisation DECP) non trivial, pour un résultat proche du gratuit. Correct. |
| **C8** Risques | 2 | **2** | Responsabilité du score, RGPD, concurrence État, plafond qualité. Correct. |
| **C9** Monétisation | 2 | **2** | ARPU comprimé (Pappers ~20 €, RiskSonnar 9,90 €/scan). Correct — A2 le renforce. |

**Seule correction retenue : C3 4 → 3.**

---

## 3. Risque d'hallucination / RAG(sens) / SQL(chiffres)

- **Conformité technique : bonne.** Le tableau §6 est exemplaire : SIREN/BODACC/DECP/RGE
  en SQL traçable, LLM cantonné au commentaire. **Pas de chiffre inventé.**
- **Risque réel, bien posé par la fiche : le faux-vrai.**
  1. **DECP `montant`** = notification / max accord-cadre ≠ dépense réelle (cf. revue 0001) ;
     un « total marchés publics du fournisseur » serait exact et trompeur.
  2. **Absence de comptes** ≠ risque nul : une entreprise saine sans dépôt produit
     un trou de données qu'un score naïf interprète mal.
  3. **Homonymes SIREN/SIRET** sur BODACC → risque d'attribuer une procédure
     collective au mauvais tiers (risque réputationnel/juridique). À traiter en garde-fou.
- **Conclusion** : le danger n'est pas l'hallucination LLM mais le **score
  composite « exact et inutile »** (tout le monde « moyen ») ou **« exact et
  diffamatoire »**. Cela milite aussi pour C3=3 (input décisif manquant).

---

## 4. Angles morts

### Concurrence : cartographie complète — confirmations 2026-06-23
- **Pappers** : KYC/KYB, surveillance temps réel (webhooks), scoring, alertes
  procédure collective, API REST 99,9 % dispo, **~20 €/mois / 100 req gratuites**
  (https://kbisenligne.com/guides/pappers-api-integration , 2026-06-23). Le seed
  est livré par Pappers à un prix plancher.
- **Annuaire des Entreprises** (État) : 50+ sources agrégées, gratuit — concurrent
  structurel imbattable en exhaustivité open data.
- Rien à ajouter : la fiche n'a pas d'angle mort concurrentiel.

### Risques peu traités
- **Commoditisation IA** : Pappers annonce résumés IA, signaux faibles BODACC,
  scoring ESG (https://www.wiiz.fr/pappers-juridique/ , 2026-06-23) — la « couche
  IA d'explication » d'un entrant est déjà intégrée chez l'incumbent. Renforce C5=1.
- **Responsabilité produit** : un « vert » sur une entreprise qui défaille expose
  juridiquement ; les incumbents ont disclaimers + modèles validés statistiquement.
  La fiche le cite (§8.4) — à ériger en risque éliminatoire de fait.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 4 | 12 |
| C2 | Cible solvable | ×3 | 2 | 2 | 6 |
| C3 | Données | ×3 | 4 | **3** | 9 |
| C4 | Espace concurrentiel libre | ×2 | 1 | 1 | 2 |
| C5 | Différenciation | ×2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité | ×2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | ×2 | 3 | 3 | 6 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **56** | | **53 / 105** |

**Score /100** : 53 / 105 × 100 = **50,5 → 50 / 100**.

**Changement de verdict : NON** (score abaissé). Fiche 53 → revue 50 → seuil < 55 →
❌ Écartée dans les deux cas.

---

## 6. Verdict de revue

### **À CORRIGER À LA MARGE** (verdict écartée confirmé et renforcé)

La fiche est rigoureuse et arrive à la bonne conclusion. Le seul correctif est
**C3 = 3** : noter 4 confond « briques open disponibles » et « inputs disponibles
pour le produit visé » — or la donnée qui fait la valeur (paiement, réseau) est
**absente**, ce qui équivaut au « plafond de verre » que la fiche décrit. Avec
C3=3, l'idée tombe à 50/100, sous le seuil de façon non ambiguë. L'actualisation
du prix Pappers (~20 €/mois) ne change pas de note mais durcit C2/C9.

### 3 actions prioritaires
1. **Abaisser C3 à 3** (input différenciant absent de l'open data) → total 53/105 → 50/100.
2. **Actualiser le prix API Pappers** (~19,90–20 €/mois, 100 req gratuites ;
   liens datés 2026-06-23) — renforce l'argument de plancher de prix.
3. **Ne pas prototyper** : si exploration de la filière « tiers », viser un angle
   **non agrégatif** (audit trail conformité achats publics via API Entreprise pour
   administrations habilitées ; ou vertical sectoriel à règles opposables), jamais
   un agrégateur généraliste open data.

---

REVUE 0022 | à corriger (marge) | score recalculé 50/100 (vs 53) | changement de décision: non (écartée renforcée)
