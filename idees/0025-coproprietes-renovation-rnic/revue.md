# Revue critique (red team) — 0025 Pilotage rénovation des copropriétés (RNIC × DPE × DECP)

- **Fiche auditée** : `idees/0025-coproprietes-renovation-rnic/README.md`
- **Score affiché par la fiche** : 64 / 100 — Verdict affiché : 🔁 À retravailler
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche est déjà honnête (C4=2, C5=2, point
> éliminatoire signalé), mais elle **se trompe de point bloquant**. Le vrai
> problème n'est pas « le SIRET syndic est-il renseigné ? » (il l'est pour les
> syndics pros) — c'est que **le différenciateur unique, le croisement
> `RNIC.siret_syndic × DECP`, est conceptuellement cassé** : la DECP est la
> commande *publique*, or une copropriété privée n'est **pas** un pouvoir
> adjudicateur — ses travaux de rénovation **n'apparaissent jamais dans la DECP**.
> Le seul moat de la fiche ne fonctionne donc **pas** sur la cible solvable
> (syndics privés). Et côté concurrence, **Powimo (Datahub)** pilote déjà le parc
> DPE, **CoproFF (Cerema)** croise déjà officiellement RNIC × fichiers fonciers.

---

## 1. Affirmations non sourcées / fragiles (à sourcer / corriger)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « Syndic (SIRET) × marchés DECP rénovation » comme indicateur SQL ✅ | §3bis / §5 / §9 | **Erreur de périmètre.** `DECP.titulaire_id` = SIRET de l'**entreprise titulaire** d'un marché *public* ; un syndic privé n'est ni acheteur ni titulaire de marché public. Le croisement n'a de sens que pour les **bailleurs sociaux** (acheteurs publics) — pas pour les syndics privés, la cible « solvable » revendiquée. | **À corriger (fondamental)** |
| A2 | « seul outil à croiser RNIC × DECP pour montrer l'historique des marchés de rénovation passés par un syndic — aucun concurrent identifié » | §5 | Affirmation centrale du moat, mais **vide** : il n'y a pas de concurrent parce qu'il n'y a **pas de donnée** (les travaux de copro privée ne sont pas dans la DECP). « Personne ne le fait » ≠ « c'est un créneau » ; ici c'est « personne ne le fait car c'est impossible avec cette source ». | **À supprimer / refonder** |
| A3 | Point éliminatoire = « si taux SIRET syndic < 30 %, la jonction tombe » | §8 | Mal ciblé. Le SIRET syndic **est** publié au RNIC pour les syndics pros (raison sociale + SIREN/SIRET + code APE) ; il existe même une réutilisation **API COPRO** qui le relie à SIRENE. Le vrai éliminatoire est A1 (la DECP ne contient pas les travaux privés), pas la complétude SIRET. | **À recadrer** |
| A4 | « Matera — pas de croisement RNIC×DECP identifié » | §4 | Exact mais incomplet : Matera a un **pôle rénovation énergétique** dédié (DPE collectif, PPT, audit, MaPrimeRénov') — concurrent réel sur l'accompagnement rénovation copro, à mentionner au-delà du seul angle « croisement ». | **À compléter** |
| A5 | Powimo listé dans le seul tableau catalogue, sans analyse | §4 catalogue | Powimo (SEIITRA) a un **module Datahub** qui centralise les DPE d'un portefeuille, calcule la répartition par classe énergétique, le % de biens à risque, priorise les travaux et alerte sur les échéances — **c'est le tableau de bord « gestion de parc » de 0025**, déjà en prod. Omis de l'analyse §4. | **À intégrer en §4** |

**À mettre au crédit de la fiche** : sources de données bien renseignées (RNIC
MàJ 17 juin 2026, DPE ADEME, DECP, RGE, BAN — URL/licence/format/fraîcheur/limites),
willingness-to-pay sourcée (ScanReno 490–790 €/mois), et **lucidité réelle** :
C4=2, C5=2, risque « ScanReno copie », risque « Go Rénove PRO gratuit » et un point
éliminatoire explicitement posé. C'est une fiche déjà auto-critique — mais sur le
mauvais risque.

---

## 2. Sur-optimisme : notes de scoring

### C5 — Différenciation défendable : **2 → 1** (poids ×2)
La fiche note déjà 2 (« copiable en < 1 mois »). Mais le diagnostic est trop
clément : le différenciateur n'est pas « copiable », il est **non fonctionnel sur
la cible payante**. Pour un syndic privé, la DECP ne contient pas ses marchés de
rénovation (commande privée). Reste, au mieux, le segment bailleurs sociaux /
collectivités — mais celui-ci est (a) servi gratuitement par **Go Rénove PRO**
(BDNB/CSTB), (b) non solvable selon la fiche elle-même. Un moat qui ne marche que
sur le segment non-solvable = note 1.

### C8 — Maîtrise des risques : **3 → 2** (poids ×2)
La fiche identifie des risques réels (SIRET, jointure adresse, ScanReno, Go
Rénove) mais **passe à côté du risque éliminatoire réel** (A1 : périmètre DECP).
Une analyse de risque qui rate le point qui invalide le produit n'est pas une
maîtrise des risques. Ajouter aussi : Powimo/CoproSolutions/ScanReno couvrent déjà
le pilotage DPE de parc → la « lacune » revendiquée est plus étroite qu'affichée. 2.

### Notes laissées inchangées (défendables)
- **C1 = 4** (×3) : DPE collectif 2026 + PPT obligatoires = douleur réglementaire
  forte et datée. OK.
- **C2 = 3** (×3) : ScanReno (490–790 €/mois) prouve la willingness-to-pay des
  syndics pros. Marché déjà adressé → 3, pas plus. OK.
- **C3 = 4** (×3) : sources ouvertes et fraîches ; le SIRET syndic *existe*
  (mieux que la crainte de la fiche). La donnée est dispo — c'est son
  *exploitabilité pour le moat* qui pèche (cf. A1), pas sa disponibilité. 4 OK.
- **C4 = 2** (×2) : ScanReno + CoproSolutions + **Powimo (Datahub)** + Matera
  (pôle réno) sur la niche syndic, Go Rénove PRO gratuit côté bailleurs. Confirmé 2.
- **C6 = 4** (×2) : archi SQL/PostGIS traçable, LLM cantonné au réglementaire. OK.
- **C7 = 3** (×2) : MVP 3 sem. conditionné aux taux de jointure. OK.
- **C9 = 3** (×2) : SaaS plausible (ScanReno), mais concurrence forte. OK (déjà bas).

---

## 3. Risque d'hallucination / RAG(sens) / SQL(chiffres)

- **Conforme** : nombres (nb passoires, montants DECP, distances) via SQL/PostGIS
  traçable ; LLM réservé à l'explication réglementaire. Bon design (C6=4).
- **Réserve sémantique (héritée de 0001)** : la fiche note « montant DECP ≠
  dépense réelle » — bien. Mais elle continue d'ériger DECP en pièce maîtresse du
  moat alors que (a) le montant est celui à la notification / max accord-cadre, et
  (b) **surtout** la DECP ne couvre pas les travaux de copro privée (A1). Un
  indicateur « SQL traçable » peut donc être **exact et hors-sujet**.

---

## 4. Angles morts (concurrents, coûts, réglementaire)

Tous consultés le 2026-06-23 :
- **Powimo / SEIITRA — module Datahub** :
  https://www.seiitra.com/blog/passoire-thermique-un-pilotage-simplifie-avec-un-logiciel-adb/
  et https://www.seiitra.com/solutions/logiciel-syndic-de-copropriete/ — pilotage
  DPE de portefeuille (KPI classe énergétique, % à risque, priorisation travaux,
  alertes échéances), PPT, suivi interventions, OCR factures. Concurrent direct
  « gestion de parc » omis de l'analyse §4.
- **Matera — pôle rénovation énergétique** :
  https://matera.eu/fr/blog/renovation-energetique-interview — DPE collectif,
  audit, PPT, MaPrimeRénov'. Plus qu'un « syndic digital ».
- **CoproFF (Cerema / Datafoncier)** :
  https://doc-datafoncier.cerema.fr/doc/coproff/coproff — **table de référence
  croisant RNIC × Fichiers fonciers** (millésimes 2021–2024), avec type de syndic,
  représentant légal, procédures, géométrie. Le croisement « RNIC × données
  foncières/marchés » est donc **déjà un produit public** (et la version Anah
  complète réserve admin. provisoire / syndic provisoire aux ayants-droit RNIC).
- **API COPRO (réutilisation data.gouv)** :
  https://www.data.gouv.fr/reuses/api-copro-trouvez-les-syndic-de-copropriete-en-charge
  — relie déjà RNIC → SIRENE (raison sociale + SIREN/SIRET + APE du syndic),
  gratuitement. La brique « identifier le syndic et sa fiche entreprise » existe.

### Risques non mentionnés
- **Périmètre DECP (éliminatoire réel, A1)** : les travaux de copropriété privée
  ne sont pas de la commande publique → absents de la DECP. Le moat ne tient que
  pour bailleurs sociaux (non solvables, gratuits via Go Rénove PRO).
- **RNIC déclaratif, couverture ~2/3** : source data.gouv (post « Les données du
  RNIC », Anah) — ~541 900 copros immatriculées, **taux de couverture estimé aux
  2/3, sans contrôle a posteriori**. Trou de couverture structurel à afficher.
- **Donnée propriétaire absente** : tout est ouvert ; le seul avantage défendable
  serait une distribution captive (FNAIM/UNIS) — non acquise.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 4 | 12 |
| C2 | Cible solvable (qui paie) | ×3 | 3 | 3 | 9 |
| C3 | Disponibilité & fiabilité données | ×3 | 4 | 4 | 12 |
| C4 | Espace concurrentiel libre | ×2 | 2 | 2 | 4 |
| C5 | Différenciation défendable | ×2 | 2 | **1** | 2 |
| C6 | Faisabilité & fiabilité technique | ×2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | ×2 | 3 | 3 | 6 |
| C8 | Maîtrise des risques | ×2 | 3 | **2** | 4 |
| C9 | Monétisation / impact | ×2 | 3 | 3 | 6 |
| | **Total** | | **67** | | **63 / 105** |

**Score /100** : 63 / 105 × 100 = 60,0 → **60 / 100**.

**Changement de verdict : NON** (reste 🔁 à retravailler, zone 55–69), mais le
**point bloquant change de nature** : ce n'est plus « mesurer le taux de SIRET
syndic » (faux problème), c'est « le croisement RNIC×DECP est inopérant sur la
cible solvable ». Tant que ce pivot n'est pas remplacé, l'idée n'a **pas de
différenciateur fonctionnel** et glisse vers l'écartement.

---

## 6. Verdict de revue

### **À CORRIGER** (le pivot différenciant est à refonder)

Douleur réglementaire (C1), données disponibles (C3) et architecture (C6) sont
solides. Mais le **seul différenciateur (RNIC × DECP)** ne fonctionne pas sur la
cible payante (syndics privés ⇒ pas de commande publique ⇒ absents de la DECP),
et le terrain « pilotage DPE de parc » est déjà couvert (ScanReno, CoproSolutions,
**Powimo Datahub**, Matera) avec, en plus, un croisement RNIC officiel existant
(**CoproFF**). La fiche a correctement posé *un* éliminatoire (SIRET) mais a
manqué le *vrai* (périmètre DECP).

### 3 actions prioritaires
1. **Abandonner ou requalifier le croisement RNIC×DECP** : le réserver explicitement
   au segment **bailleurs sociaux** (acheteurs publics réels), tout en reconnaissant
   que ce segment est servi gratuitement par Go Rénove PRO → donc non monétisable.
   Pour les syndics privés, trouver une **autre source** de l'historique travaux
   (pas la DECP).
2. **Intégrer Powimo (Datahub), Matera (pôle réno) et CoproFF en §4** et re-noter
   C5 honnêtement (le « gap RNIC×DECP » n'est pas un gap).
3. **Si aucun différenciateur fonctionnel n'émerge**, écarter au profit de 0009
   amélioré — la beauté du croisement ne compense pas une source inadéquate.

---

REVUE 0025 | à corriger | score recalculé 60/100 (vs 64) | changement de décision: non (reste 🔁) | pivot RNIC×DECP non fonctionnel sur la cible solvable (DECP = commande publique, copro privée hors champ)
