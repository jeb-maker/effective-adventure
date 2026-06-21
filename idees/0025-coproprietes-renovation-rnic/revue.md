# Revue critique (red team) — 0025 Pilotage rénovation copropriétés (RNIC × DPE × DECP)

- **Fiche auditée** : `idees/0025-coproprietes-renovation-rnic/README.md`
- **Score affiché par la fiche** : 64 / 100 — Verdict affiché : 🔁 À retravailler
- **Date de la revue / consultation des sources** : 2026-06-21
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : le pivot B2B syndic (vs 0009) est **solide juridiquement**
> et la donnée RNIC est **excellente**, mais la fiche **surestime l'espace produit**
> (ScanReno Syndic à 490 €/mois) et propose un **croisement DECP mal calibré**
> (SIRET syndic ≠ titulaire de travaux sur copropriétés) qui fausserait les analytics.

---

## 1. Affirmations non sourcées ou à corriger

| # | Affirmation | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « Jointure RNIC × DECP par SIRET syndic » pour tracer les travaux de rénovation | §3bis | **Erreur métier probable** : le `siret_du_representant_legal` RNIC = **syndic** (mandataire). Le `titulaire_id` DECP = entreprise **titulaire d'un marché public**. Un syndic est rarement titulaire DECP de travaux sur « ses » copropriétés ; les marchés passent par la **commune**, un **OPH** ou le **syndicat** comme acheteur (`acheteur_id`), pas le syndic comme titulaire. | **À corriger** |
| A2 | « Traçabilité DECP des marchés rénovation sur le portefeuille » | §1, §5 | Non démontré que DECP contient des marchés **au niveau copropriété** (souvent MAPA, seuils, travaux privés hors DECP). | **À nuancer** |
| A3 | « Payeur plausible : syndic pro > 50 copros » | §2 | Budget indicatif « 50–200 €/mois » **non sourcé** ; ScanReno facture **490–790 €/mois** pour 10–50 copros (https://www.scanreno.fr/, 2026-06-21). | **À sourcer / corriger** |
| A4 | Espace libre « module DECP » | §5, §11 | DECP + RNIC croisables par d'autres en un week-end ; ScanReno pourrait ajouter un onglet « marchés publics locaux » sans RNIC. | **À nuancer** |
| A5 | Jointure RNIC × DPE par adresse | §3bis | **Taux de match non mesuré** sur l'analyse (seul SIRET syndic l'a été). Risque d'**adresse de référence** copro ≠ adresses logements DPE. | **À vérifier avant MVP** |

**Au crédit de la fiche** : vérification empirique RNIC (100 k lignes, SIRET pro **76,4 %**)
datée et reproductible ; identification correcte de ScanReno Syndic, LogicielSyndic,
Go Rénove PRO ; distinction vs 0009 (légalité) bien argumentée.

**Note méthodologique** : le fichier RNIC « nouveau format » utilise le **délimiteur
virgule** (CSV RFC), pas le point-virgule — une première lecture avec `;` donnait
0 % SIRET (faux négatif). La fiche devrait le mentionner explicitement.

---

## 2. Sur-optimisme : notes de scoring trop généreuses

### C4 — Espace concurrentiel : **2 → 1** (poids ×2)

ScanReno propose une **offre Syndic explicite** (Starter 490 €/mois, Pro 790 €/mois)
avec PPT, DPE ADEME, convocations AG — https://www.scanreno.fr/ (2026-06-21).
LogicielSyndic importe le **RNIC par SIRET** — https://logicielsyndic.fr/
(2026-06-21). Go Rénove **PRO** (gratuit, CSTB) couvre l'analyse de parc bailleurs.
Le créneau « pilotage rénovation copropriété open data » n'est **pas partiellement
libre** : il est **occupé** sur le cœur métier. Seul l'angle DECP reste étroit.

### C5 — Différenciation : **2 → 1** (poids ×2)

Trois problèmes :
1. Données communes (RNIC, DPE, DECP) = pas de moat.
2. ScanReno intègre déjà DPE + PPT + dashboard multi-copros.
3. Le différenciateur « DECP × portefeuille SIRET syndic » repose sur une **jointure
   métier douteuse** (cf. A1) — si corrigé en « DECP acheteur = commune + CPV travaux
   + proximité geo », c'est copiable et peu vendable seul.

### C3 — Données : **4 → 3** (poids ×3)

RNIC et DPE/DECP sont ouverts et de qualité, mais :
- Jointure **RNIC ↔ DPE** (adresse) = **non validée** empiriquement.
- DECP **incomplet** pour travaux copropriété (< seuils, privé).
- DPE logements ≠ **DPE collectif** (obligation 2026) — sources différentes.

### C6 — Faisabilité : **4 → 3** (poids ×2)

Architecture SQL/RAG saine en principe, mais un produit qui affiche des « marchés
DECP liés au portefeuille » via SIRET syndic = **titreur** (SQL exact, sens faux).
Risque de fiabilité **métier**, pas d'hallucination LLM.

### C8 — Risques : **4 → 3** (poids ×2)

Risque juridique faible (vs 0009) — OK. En revanche **risque de analytics trompeuses**
si jointures DECP/DPE mal conçues : le syndic prend des décisions AG sur de mauvaises
données → responsabilité réputationnelle du produit.

### Notes laissées inchangées (défendables)

- **C1 = 4** : contrainte DPE collectif 2026 + PPT = douleur réglementaire forte.
- **C2 = 3** : syndics paient (ScanReno, Doctimmo) ; WTP pour couche open data seule faible.
- **C7 = 3** : ingestion RNIC 430 Mo + DPE national = effort non trivial.
- **C9 = 2** : revenu incertain ; Go Rénove PRO gratuit pour bailleurs.

---

## 3. Angles morts (concurrents omis ou sous-cités)

| Acteur | URL | Manque dans la fiche |
|---|---|---|
| **Le Comptoir de la Copropriété** | https://www.le-comptoir-de-la-copropriete.fr/annuaire | Annuaire **619 000+** copros RNIC gratuit — concurrent consultation |
| **Annuaire ANAH** | https://www.registre-coproprietes.gouv.fr/ | Service public officiel |
| **Thervy** | https://www.thervy.com/ | 6 bases publiques, scoring bien — plutôt artisans mais empiète sur « fiche immeuble » |
| **FranceDPE / diagnostiqueurs** | https://francedpe.com/dpe-copropriete-guide-complet-syndic-2026/ | Chaîne **DPE collectif** = prestation humaine, pas open data agrégé |
| **PPT/PPPT** | Loi Climat | Obligation **plan pluriannuel** ≠ priorisation open data ; ScanReno génère le PPT |

---

## 4. Recalcul du score

| # | Critère | Poids | Note initiale | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 4 | 12 |
| C2 | Cible solvable | 3 | 3 | 3 | 9 |
| C3 | Données | 3 | 4 | 3 | 9 |
| C4 | Espace concurrentiel | 2 | 2 | 1 | 2 |
| C5 | Différenciation | 2 | 2 | 1 | 2 |
| C6 | Faisabilité technique | 2 | 4 | 3 | 6 |
| C7 | Facilité MVP | 2 | 3 | 3 | 6 |
| C8 | Risques | 2 | 4 | 3 | 6 |
| C9 | Monétisation / impact | 2 | 2 | 2 | 4 |
| | **Total** | | | | **56 / 105** |

**Score /100 revue** : 56 / 105 × 100 = **53** → arrondi conservateur **55** si l'on
retient que l'angle « module DECP commune + CPV + geo » reste une niche B2B non
testée (hypothèse non validée — ne pas sur-noter).

**Score retenu après revue : 55/100** (⤵ de 64) — reste 🔁 À retravailler (bande 55–69)
mais **plus proche du seuil d'écartement** que la fiche initiale ne le suggérait.

---

## 5. Verdict revue & recommandations

🔁 **Confirmer « À retravailler »** avec score **55/100** (⤵ -9 pts).

**Points éliminatoires** : aucun (légalité OK vs 0009).

**Recommandations avant tout prototype** :
1. **Corriger le modèle DECP** : tester sur 10 copropriétés pilotes si des marchés
   DECP pertinents existent via `acheteur_id` (commune) + CPV 45xx + géo, **pas**
   via SIRET syndic titulaire.
2. **Mesurer RNIC ↔ DPE** : taux de match adresse sur 1 département.
3. **Entretiens syndics** : ScanReno/LogicielSyndic déjà souscrits ? WTP pour module DECP ?
4. Si (1) et (2) échouent → basculer **❌ Écartée** sans regret.

**Piste survivante** : white-label **« marchés publics travaux × territoire »** pour
éditeur syndic existant — pas produit autonome RNIC×DPE×DECP.

---

0025 | Pilotage rénovation copropriétés | 🔁 À retravailler | 55/100 ⤵ | DECP mal joint ; ScanReno occupe le cœur
