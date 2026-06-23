# Revue critique (red team) — 0004 Dossier immobilier intelligent (DVF enrichi)

- **Fiche auditée** : `idees/0004-dossier-immobilier-intelligent/README.md`
- **Score affiché par la fiche** : — / 100 (écartée sur critère éliminatoire) — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la décision d'écarter est **correcte et même
> sous-documentée** — la fiche a écarté l'idée *avant* d'avoir vu le pire : un
> **clone quasi exact** du « dossier d'achat multi-sources » existe déjà en
> production (**Fonciris**, DVF + Géorisques + DPE + PLU + BDNB + SSMSI + ARCEP,
> aperçu en 30 s, freemium + offre Pro marque blanche/API). Saturation confirmée,
> score reconstruit ≈ 53/100, ❌ Écartée maintenue.

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « 72 % des Français veulent connaître les prix de vente de leur quartier » | §1 Problème | Chiffre cité **sans lien ni source datée** (viole la règle de preuve §2 de la méthode). | **À sourcer ou supprimer** |
| A2 | « Le seul angle survivant serait le "dossier d'achat" agrégé multi-sources, mais déjà attaqué par des applis matures » | §11 Verdict | Affirmation **juste mais sous-étayée** : la fiche ne cite **aucun** de ces « applis matures » sur le dossier agrégé (elle ne liste que des cartes DVF). | **À corriger (compléter)** |
| A3 | « La carte DVF est un commodity » | §11 Verdict | Vrai et bien vu, mais c'est l'angle **le moins ambitieux** du pitch ; l'angle réellement défendu (dossier agrégé) n'est pas instruit. | **À compléter** |

**À mettre au crédit de la fiche** : elle écarte vite et sans complaisance, et
cite des cartes DVF réelles (explore.data.gouv, Immo Data, Carte Prix Immobilier)
avec dates. Le problème n'est pas un excès d'optimisme — c'est une **§4
incomplète** sur le segment qui compte (le dossier agrégé), ce qui aurait pu, à
tort, laisser croire à un espace libre sur cet angle précis.

---

## 2. Sur-optimisme : notes de scoring (la fiche n'en a pas)

La fiche a écarté l'idée **sans tableau de scoring**, sur le seul critère
éliminatoire « saturation ». C'est défendable (la méthode autorise un écart sur
point éliminatoire), mais cela prive la décision de traçabilité. La revue
reconstruit le scoring (§5). Points d'attention C2/C4 :

- **C2 (qui paie) = 2** : l'acheteur particulier paie **une fois** (achat ponctuel,
  pas d'abonnement récurrent) et est **très sensible au prix** ; le payeur
  récurrent (agent immobilier) est déjà servi par MeilleursAgents et Fonciris Pro.
  Willingness-to-pay pour un *nouvel* agrégateur autonome : faible.
- **C4 (espace libre) = 1** : non seulement la carte DVF est un commodity, mais le
  **dossier agrégé** lui-même est déjà un produit fini (Fonciris). C4 plancher.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- L'idée est **techniquement saine** : données tabulaires (DVF, DPE, risques) →
  SQL/agrégats traçables, LLM cantonné au résumé. Risque d'hallucination faible
  par construction (ce n'est pas le point qui tue l'idée).
- **Réserve métier** (à l'image de tout produit DVF) : DVF est **semestriel et
  rétrospectif** (dernière passe : ventes S1 2025), **absent en Alsace-Moselle et
  à Mayotte**, et un prix médian de quartier n'est pas une estimation de bien.
  Un « verdict chiffré » présenté trop vite peut être **exact mais trompeur** —
  exactement le risque que Fonciris assume déjà avec des avertissements de source.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire non mentionnés)

### Concurrent direct OMIS (le plus grave) — consultés le 2026-06-23

- **Fonciris** — https://fonciris.fr/ : **le produit exact décrit par la fiche.**
  « Analyse prix DVF, risques, DPE pour votre achat immobilier », aperçu gratuit
  **en 30 s**, croise DVF/DGFiP + Géorisques + ADEME/DPE + INSEE + Cadastre/IGN +
  BRGM + BDNB + SSMSI + ARCEP + ANFR (« +30 autres sources publiques »), score
  piéton, comparables, marge de négociation, **veille**, export PDF, et une offre
  **Pro en marque blanche (logo, CRM, API)**. Guides « check-list achat » et
  « analyser un bien » à l'appui (https://fonciris.fr/guide/checklist-achat-immobilier).
  → C'est le « dossier d'achat agrégé multi-sources » au mot près.
- **Immo Data** — https://www.immo-data.fr/dvf (consulté 2026-06-23) : carte DVF
  nationale, prix/m² par commune/quartier/adresse, MàJ semestrielle. Commodity
  DVF confirmé.
- **MeilleursAgents / SeLoger, Castorus, Efficity, PriceHubble** : estimation de
  prix, historique, alertes — segment « valeur du bien » saturé côté grand public
  et agents (PriceHubble figure d'ailleurs au catalogue SaaS `real-estate-proptech`
  du dépôt).
- **Applis cadastre/DVF/DPE/PLU** (déjà citées par la fiche) : la brique
  « risques + PLU + DPE par adresse » est aussi couverte par l'**explorateur DVF
  officiel** et **Géorisques** (gratuits, publics).

→ Conclusion : la fiche avait raison d'écarter, mais pour la **mauvaise preuve**
(elle ne montrait que des cartes DVF). Le vrai motif d'écart est qu'un **clone du
dossier agrégé existe déjà, monétisé, avec offre B2B marque blanche** : il n'y a
plus de « niche dossier d'achat » à défricher.

### Risques / coûts non mentionnés

- **Guerre des prix / freemium** : Fonciris offre l'aperçu gratuit ; tout nouvel
  entrant affronte un plancher proche de zéro côté grand public.
- **Maintenance multi-sources** : 10–30 sources publiques à ingérer et tenir à
  jour (DVF semestriel, DPE continu, risques, ARCEP/ANFR) = **OPEX permanent**,
  non chiffré.
- **Responsabilité du « verdict »** : afficher une « marge de négociation » ou un
  « coût dans le temps » engage si l'acheteur s'y fie — risque de réclamation.
- **Couverture DVF** : Alsace-Moselle/Mayotte exclues → trou produit structurel.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note revue | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 12 | Besoin réel et fréquent (achat = enjeu fort), mais ponctuel par acheteur. |
| C2 | Cible solvable (qui paie) | ×3 | 2 | 6 | Acheteur paie une fois et au rabais ; payeur récurrent (agents) déjà capté. |
| C3 | Disponibilité & fiabilité données | ×3 | 4 | 12 | DVF/DPE/risques ouverts et prêts ; réserve : DVF semestriel, hors Alsace-Moselle. |
| C4 | Espace concurrentiel libre | ×2 | 1 | 2 | **Saturé** : Fonciris (clone exact) + Immo Data + MeilleursAgents + officiel. |
| C5 | Différenciation défendable | ×2 | 1 | 2 | Données 100 % publiques aussi chez Fonciris ; aucun moat. |
| C6 | Faisabilité & fiabilité technique | ×2 | 4 | 8 | Tabulaire → SQL traçable, LLM au résumé ; faisable. |
| C7 | Facilité du MVP | ×2 | 3 | 6 | Agrégation multi-sources + géo non triviale, mais bien balisée. |
| C8 | Maîtrise des risques | ×2 | 2 | 4 | Saturation/prix non maîtrisés ; responsabilité du « verdict ». |
| C9 | Monétisation / impact | ×2 | 2 | 4 | Monétisation compressée par le freemium d'un clone existant. |
| | **Total** | | | **56 / 105** | |

**Score /100** : 56 / 105 × 100 = **53 / 100**.

**Changement de décision : NON.**
- Fiche : ❌ Écartée (critère éliminatoire saturation, sans score).
- Revue : 53/100 → < 55 → ❌ **Écartée**, et **renforcée** par le critère
  éliminatoire (clone exact en production). Les deux convergent.

---

## 6. Verdict de revue

### **À CORRIGER** (sur la preuve) → décision : ❌ Écartée (confirmée)

La **décision est juste** ; c'est la **démonstration** qui était incomplète. La
fiche écartait sur des cartes DVF (commodity) sans montrer que l'angle qu'elle
disait « survivant » — le dossier agrégé multi-sources — est lui aussi un produit
fini et monétisé (Fonciris, marque blanche/API). Avec un score reconstruit à
53/100 **et** un critère éliminatoire de saturation, ❌ Écartée est confirmée et
mieux étayée.

### 3 actions prioritaires
1. **Mettre à jour le §4** avec Fonciris (lien daté) comme concurrent direct du
   dossier agrégé, et supprimer/sourcer le « 72 % » non référencé (A1).
2. **Acter le score 53/100** dans la fiche pour rendre l'écart traçable (au lieu
   d'un écart « éliminatoire » sans note).
3. **Si l'idée revient un jour**, ne la rouvrir que sur une **niche verticale
   très étroite** non couverte par Fonciris (ex. un type de bien/usage
   réglementaire précis) avec un payeur B2B clair — sinon ne pas y revenir.

---

REVUE 0004 | à corriger | score recalculé 53/100 (vs —) | changement de décision: non (❌ confirmée)
