# Revue critique (red team) — 0021 Veille foncière & urbanisme (B2B)

- **Fiche auditée** : `idees/0021-veille-fonciere-amenageurs/README.md`
- **Score affiché par la fiche** : 50 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche est solide, bien sourcée et conclut justement
> à l'écartage. Adversarialement, elle reste **trop généreuse sur C2** : le seed
> vise un marché **déjà entièrement équipé** (Kel Foncier revendiqué « utilisé par
> tous les promoteurs »), où le budget à arracher est **additionnel**, pas neuf.
> En appliquant la règle « budget existant ≠ budget additionnel », C2 passe de 3 à 2
> et le score de **50 à 47/100** — verdict écartée **renforcé**.

---

## 1. Affirmations non sourcées (à sourcer / à corriger)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « je ne pense pas qu'il y ait un promoteur qui n'utilise pas KelFoncier » | §2/§7 | **Témoignage marketing du concurrent** repris comme constat de marché. La fiche le signale (« selon leurs témoignages ») — à conserver comme tel, **ne pas** en faire une preuve d'exhaustivité (≠ étude indépendante). | **À nuancer (déjà fait)** |
| A2 | « marge foncier typique **15–30 % du CA** programme selon Kel Foncier » | §1 | Source = page commerciale Kel Foncier. **Confirmé** par leur page Logiciel : « en moyenne 15 % … jusqu'à 25-30 % » (https://www.kelfoncier.com/logiciel/ , consulté 2026-06-23). Bien attribué, mais reste un chiffre d'éditeur, pas une statistique sectorielle indépendante. | **À sourcer mieux (ordre de grandeur OK)** |
| A3 | « Urbanease … « nerf de la guerre » » | §1 | **Vérifié** : Urbanease (PriceHubble) emploie bien cette formule et revendique « en moyenne 40 min gagnées sur chaque dossier », 84 M de parcelles (https://www.urbanease.io/ , consulté 2026-06-23). OK. | **OK** |
| A4 | Prix « Géofoncier 80–87 € », « IZIRED 84,99 € », « PermisAPI 49–199 € » | §2/§4 | Datés et plausibles. À mettre au crédit de la fiche. | **OK** |
| A5 | « MAJIC PM … fiche officielle MàJ **25 mars 2021** (fréquence non respectée) » | §3 | Honnête et utile (signale un trou de fraîcheur). Bon réflexe. | **OK** |

**À mettre au crédit de la fiche** : le §3 (sources) et le §4 (8+ concurrents,
liens datés) sont exemplaires. La distinction propre vs 0004 est claire.

---

## 2. Sur-optimisme : notes de scoring

| Critère | Note fiche | Note revue | Justification adversariale |
|---|---|---|---|
| **C1** Intensité | 4 | **4** | Douleur forte, récurrente, à fort enjeu financier (marge foncier). Défendable. |
| **C2** Cible solvable | 3 | **2** | **Trop généreux.** Le marché est **déjà équipé** par Kel Foncier (≈ universel revendiqué), Urbanease, ORUS, Géofoncier, IZIRED. La fiche le dit elle-même : « arrachera-t-on un abonnement **supplémentaire** … réponse probablement non ». Or un budget *déjà capté* par des incumbents avec coûts de bascule (CRM, données contact, préfaisabilité) n'est pas un payeur acquis pour un entrant → **2** (payeurs existent mais budget additionnel quasi inexistant), comme la revue 0001 a baissé C2 pour une dépense additionnelle. |
| **C3** Données | 3 | **3** | Open data solide mais jointures lourdes, MAJIC annuel/2021, DVF semestriel, PLU hétérogène, **propriétaires physiques hors open data**. 3 correct (pas 4 : la donnée *qui fait la valeur*, le contact, manque). |
| **C4** Espace libre | 1 | **1** | Plancher justifié : 8+ produits couvrent le seed mot pour mot. |
| **C5** Différenciation | 1 | **1** | Plancher justifié : aucun angle non déjà tenu. |
| **C6** Faisabilité | 3 | **3** | SQL OK pour chiffres marché/permis ; préfaisabilité PLU = hors SQL simple. Correct. |
| **C7** Facilité MVP | 2 | **2** | Pipeline géo national + moteur règles urbanisme = chantier lourd. Correct. |
| **C8** Risques | 2 | **2** | Concurrence dominante, RGPD/DVF, données contact hors open data. Correct. |
| **C9** Monétisation | 2 | **2** | ARPU plafonné par incumbents, CAC B2B promoteur élevé. Correct. |

**Seule correction retenue : C2 3 → 2.**

---

## 3. Risque d'hallucination / RAG(sens) / SQL(chiffres)

- **Conformité partielle, bien diagnostiquée par la fiche** : chiffres marché
  (DVF, comptage permis, SDP champs Sitadel) traçables en SQL ; mais la **promesse
  métier centrale** — la **préfaisabilité PLU** (emprise, hauteur, CES, mixité) —
  **ne peut pas** reposer sur un simple croisement open data. C'est le cœur de
  métier des incumbents (moteurs de règles + experts), pas un livrable SQL.
- **Risque sémantique réel** : « prix DVF » ≠ prix terrain nu (ventes multi-lots,
  dépendances) ; un chiffre exact peut induire une **valorisation foncière fausse**.
  Bien identifié au §6.
- **Pas de chiffre inventé** affiché dans la fiche. RAS côté hallucination LLM.

---

## 4. Angles morts

### Concurrence : déjà exhaustive — confirmations 2026-06-23
La cartographie de la fiche est complète. Vérifications complémentaires :
- **ORUS App (1Spatial)** : « identifier et analyser en quelques minutes les
  fonciers », PLU + propriétaires + DVF + permis + **SDP en 3 clics** + 3D
  (https://1spatial.com/fr/produits/orus-app/ , 2026-06-23) — recouvre le seed.
- **Urbanease (PriceHubble)** : prospection + CRM + « fonciers détenus par des
  **sociétés en difficulté** » + patrimoine propriétaires + apps mobiles
  (https://www.urbanease.io/ , 2026-06-23) — recouvre le seed, **groupe bien financé**.
- **Kel Foncier** : 35 000 communes PLU, 250 réglementations, recherche 50+
  critères, remontée auto d'opportunités, préfaisabilité (https://www.kelfoncier.com/logiciel/ , 2026-06-23).

→ Rien à ajouter : la fiche n'a pas d'angle mort concurrentiel. C4=1 incontestable.

### Risques peu traités
- **Tendance IA 2026** : les incumbents intègrent déjà l'IA générative (extraction
  de contraintes PLU, rédaction d'approche propriétaire) — un différenciateur « IA »
  d'un entrant serait **déjà commoditisé** côté leaders. Renforce C5=1.
- **Verrou données contact** : revendiqué par Kel Foncier comme avantage RGPD-compatible ;
  un entrant open-data-only ne peut pas livrer le « à qui écrire » — trou structurel
  dans le pitch, déjà noté mais central.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 4 | 12 |
| C2 | Cible solvable | ×3 | 3 | **2** | 6 |
| C3 | Données | ×3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 1 | 1 | 2 |
| C5 | Différenciation | ×2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité | ×2 | 3 | 3 | 6 |
| C7 | Facilité du MVP | ×2 | 2 | 2 | 4 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **52** | | **49 / 105** |

**Score /100** : 49 / 105 × 100 = **46,7 → 47 / 100**.

**Changement de verdict : NON** (mais score abaissé). Fiche 50 → revue 47 →
seuil < 55 → ❌ Écartée dans les deux cas. La baisse confirme que l'idée est
**nettement** sous le seuil, pas à la marge.

---

## 6. Verdict de revue

### **À CORRIGER À LA MARGE** (verdict écartée confirmé et renforcé)

La fiche est de bonne qualité : sourcing rigoureux, cartographie concurrentielle
complète, distinction nette vs 0004. Le seul correctif est **C2 = 2** (et non 3) :
sur un marché saturé où le budget est déjà capté, « des payeurs existent » ne suffit
pas — il faut un budget *additionnel*, ici introuvable. Score 47/100 : écartée
robuste, pas limite.

### 3 actions prioritaires
1. **Abaisser C2 à 2** dans le scoring de la fiche (budget additionnel ≈ nul sur
   marché équipé) et mettre le total à 49/105 → 47/100.
2. **Ne pas prototyper** : l'angle « croiser Sitadel + DVF + PLU + friches + PM »
   est le produit de Kel Foncier/Urbanease/ORUS. Aucun différenciateur défendable.
3. Si poursuite du foncier B2B, exiger **5 entretiens terrain** prouvant une
   **niche non couverte** (foncières institutionnelles/énergie/bailleurs) ou un
   pivot **API/infra** (type PermisAPI), avant toute ligne de code.

---

REVUE 0021 | à corriger (marge) | score recalculé 47/100 (vs 50) | changement de décision: non (écartée renforcée)
