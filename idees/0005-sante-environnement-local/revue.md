# Revue critique (red team) — 0005 Santé-environnement locale (eau / air)

- **Fiche auditée** : `idees/0005-sante-environnement-local/README.md`
- **Score affiché par la fiche** : — / 100 (écartée : saturation + risque sanitaire) — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : décision d'écart **correcte et désormais renforcée** —
> au-delà de Recosanté, l'État a lancé en **février 2026** une carte officielle
> grand public de la qualité de l'eau du robinet, et l'**UFC-Que Choisir** publie
> une carte interactive (50 contaminants, PFAS) ; la saturation est totale, le
> payeur inexistant et le **risque sanitaire** quasi éliminatoire. Score
> reconstruit ≈ 44/100, ❌ Écartée maintenue.

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « marché déjà couvert » (§1) | §1 Problème | Vrai, mais **sous-sourcé** : la fiche ne cite que Recosanté et quelques sites eau ; elle manque la carte officielle Ministère de la Santé (2026) et l'UFC-Que Choisir. | **À compléter** |
| A2 | « risque de positionnement sur du conseil santé » (§1) | §1 Problème | Bien vu et **décisif** (c'est le critère quasi éliminatoire), mais affirmé sans le qualifier juridiquement (responsabilité, information sanitaire). | **À étayer en §8** |
| A3 | « Données via Hub'Eau/SISE-Eaux déjà très exploitées » (§8) | §8 Risques | Plausible et correct, mais **non sourcé** (aucune réutilisation citée nommément). | **À sourcer** |

**À mettre au crédit de la fiche** : elle écarte sans complaisance et cite des
réutilisations réelles (Recosanté, mon-eau.com, Dans Mon Eau). Le diagnostic
(saturation + risque sanitaire) est le bon ; il manque surtout les **preuves
publiques les plus récentes** et un scoring traçable.

---

## 2. Sur-optimisme : notes de scoring (la fiche n'en a pas)

La fiche écarte sur deux critères éliminatoires (saturation, santé) **sans
tableau**. Reconstruction en §5. Attention C2/C4 :

- **C2 (qui paie) = 1** : produit d'**information citoyenne** → l'utilisateur
  (habitant) **ne paie pas**, et les alternatives (Recosanté, carte Ministère
  Santé, UFC-Que Choisir, mon-eau.com) sont **gratuites**. Aucun payeur B2B
  crédible n'est identifié. C2 plancher.
- **C4 (espace libre) = 1** : eau **et** air sont couverts par des services
  publics gratuits **et** une association de consommateurs **et** des
  réutilisations matures. C4 plancher.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- Les données (Hub'Eau, Atmo, SISE-Eaux) sont **tabulaires et SQL-ables** : le
  risque d'hallucination « numérique » serait faible.
- **Mais le vrai risque n'est pas l'hallucination, c'est l'interprétation
  sanitaire.** Transformer une mesure (un dépassement de norme, un paramètre
  physico-chimique) en message à l'habitant frôle l'**information/conseil de
  santé**. L'UFC-Que Choisir prend d'ailleurs soin de préciser qu'« une fréquence
  élevée de dépassement ne signifie en aucun cas que l'eau serait non potable »
  (https://www.quechoisir.org/carte-interactive-eau-n21241/) — précaution qu'un
  produit commercial devrait reproduire, sous peine de **désinformation
  anxiogène** et de responsabilité.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire non mentionnés)

### Concurrents OMIS — consultés le 2026-06-23

- **Carte officielle « Qualité de l'eau du robinet » (Ministère de la Santé)** :
  outil de recherche national par région/département/commune, **bulletin de
  conformité** par paramètre, mis en avant par Service-Public.fr le **19 février
  2026** (https://www.service-public.gouv.fr/particuliers/actualites/A18016 et
  https://www.service-public.gouv.fr/particuliers/vosdroits/R11461). L'État
  occupe directement le créneau « ma commune ».
- **UFC-Que Choisir — carte interactive de la conformité de l'eau** :
  **50 contaminants et paramètres**, code postal/commune, dossiers PFAS/TFA
  (https://www.quechoisir.org/carte-interactive-eau-n21241/ , consulté
  2026-06-23). Acteur indépendant, gratuit, à forte notoriété et caution.
- **Recosanté** (cité par la fiche) : service public air/pollens/UV/baignade,
  application mobile (https://recosante.beta.gouv.fr / fabrique sociale).
- **Atmo France / AASQA** : indices et alertes qualité de l'air officiels par
  région (segment air entièrement couvert).
- **mon-eau.com, EauPotable.net, Dans Mon Eau (Générations Futures + Data for
  Good)** (cités) : réutilisations matures côté eau.

→ Conclusion : la fiche n'a pas seulement « un » concurrent ; elle affronte
**l'État (eau + air), une association de consommateurs de référence, et des
réutilisations matures**, sur les deux volets du pitch. Espace produit = **fermé**.

### Risques / réglementaire non chiffrés

- **Risque sanitaire/juridique (quasi éliminatoire)** : interpréter des mesures
  pour des particuliers = frontière du conseil de santé ; responsabilité en cas
  de message erroné ou anxiogène.
- **PFAS/TFA — sujet sensible et mouvant** : la réglementation évolue (TFA non
  réglementé à ce jour) ; afficher un « score » sur des polluants émergents
  expose à la controverse scientifique et à la contestation.
- **Concurrence d'une caution publique/associative** : difficile de monétiser
  une information que l'État et l'UFC-Que Choisir donnent gratuitement **avec**
  une légitimité supérieure.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note revue | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | 9 | Préoccupation réelle (eau/air) mais besoin d'information, pas douleur payante. |
| C2 | Cible solvable (qui paie) | ×3 | 1 | 3 | Habitant ne paie pas ; alternatives gratuites (État, UFC-QC) ; pas de payeur B2B. |
| C3 | Disponibilité & fiabilité données | ×3 | 4 | 12 | Hub'Eau/Atmo/SISE-Eaux ouvertes, prêtes et SQL-ables. |
| C4 | Espace concurrentiel libre | ×2 | 1 | 2 | Saturé : État (eau + air) + UFC-Que Choisir + Recosanté + réutilisations. |
| C5 | Différenciation défendable | ×2 | 1 | 2 | Aucune ; mêmes données publiques, caution moindre qu'État/UFC-QC. |
| C6 | Faisabilité & fiabilité technique | ×2 | 3 | 6 | Données SQL-ables, mais interprétation sanitaire = risque (pas un simple résumé). |
| C7 | Facilité du MVP | ×2 | 4 | 8 | MVP technique simple (données prêtes) — ce qui nourrit la saturation. |
| C8 | Maîtrise des risques | ×2 | 1 | 2 | Risque sanitaire/juridique quasi éliminatoire + saturation non maîtrisés. |
| C9 | Monétisation / impact | ×2 | 1 | 2 | Pas de revenu (gratuit citoyen) ; impact déjà porté par l'État et l'UFC-QC. |
| | **Total** | | | **46 / 105** | |

**Score /100** : 46 / 105 × 100 = **44 / 100**.

**Changement de décision : NON.**
- Fiche : ❌ Écartée (saturation + risque sanitaire, sans score).
- Revue : 44/100 → < 55 → ❌ **Écartée**, renforcée par le critère éliminatoire
  sanitaire. Convergence.

---

## 6. Verdict de revue

### **À CORRIGER** (sur la preuve) → décision : ❌ Écartée (confirmée)

La décision est **juste**. La fiche est trop **minimale** : elle écarte sur une
intuition correcte (saturation + santé) sans montrer les preuves publiques les
plus fortes (carte Ministère de la Santé, février 2026 ; UFC-Que Choisir) ni
poser de score. Reconstruit à 44/100 avec un risque sanitaire quasi éliminatoire,
❌ Écartée est confirmée et mieux documentée.

### 3 actions prioritaires
1. **Compléter le §4** avec la carte officielle Ministère de la Santé (2026) et
   l'UFC-Que Choisir (liens datés), pour rendre la saturation incontestable.
2. **Acter le score 44/100** et qualifier explicitement le **risque sanitaire**
   en §8 (frontière du conseil de santé, responsabilité, PFAS/TFA).
3. **Ne pas rouvrir** sans un payeur B2B/B2G précis et un usage **non sanitaire**
   (ex. donnée d'entrée d'un autre produit), faute de quoi l'idée reste écartée.

---

REVUE 0005 | à corriger | score recalculé 44/100 (vs —) | changement de décision: non (❌ confirmée)
