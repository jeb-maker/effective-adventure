# Revue critique (red team) — 0020 Benchmark financier inter-collectivités

- **Fiche auditée** : `idees/0020-benchmark-financier-collectivites/README.md`
- **Score affiché par la fiche** : 53 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche arrive à la bonne décision (écartée) avec un
> scoring déjà sévère et bien calibré (C4=1, C5=1). La revue **confirme** le verdict
> et le **renforce** : la fiche a en réalité **sous-documenté** la concurrence
> publique gratuite (DGFiP « Tableau de bord financier » / fiches **AEFF**, et
> la fonction de comparaison à un **groupe de référence** déjà offerte par l'OFGL),
> ce qui aggrave la saturation au lieu de l'atténuer. Le score reste à 53/100.

---

## 1. Affirmations non sourcées (à sourcer / à corriger)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « **Hélios / PIGP** … Pas de benchmark inter-collectivités ; données **propres** uniquement » | §4.1 | **Partiellement faux.** La DGFiP diffuse via le PIGP un **« Tableau de bord financier »** comportant les **fiches AEFF** (Analyse des Équilibres Financiers Fondamentaux), en versions budget principal / consolidé / **agrégé**, pour communes, GFP, régions, départements et SDIS — donc avec une dimension comparative et de strate, gratuitement (https://www.collectivites-locales.gouv.fr/tableau-de-bord-de-lelu , consulté 2026-06-23 ; dépliant DGFiP https://www.impots.gouv.fr/ , consulté 2026-06-23). À corriger : ce n'est pas « données propres uniquement ». | **À corriger (aggrave la saturation)** |
| A2 | « OFGL … pas de restitution « mandat » clé en main » | §4.1 | À nuancer : la plateforme OFGL revendique désormais explicitement « comparer une collectivité à un **groupe de référence** aux caractéristiques proches (taille, géographie) », des **datastories** interactives et des cartographies sur mesure (https://www.collectivites-locales.gouv.fr/actualites/les-donnees-financieres-2024-sont-pretes-etre-analysees-sur-dataofglfr , consulté 2026-06-23). Le « cœur de l'idée » est donc encore plus couvert que ne le dit la fiche. | **À nuancer (renforce C4=1)** |
| A3 | « **floriculture** de réutilisations » (§11) | §11 | Coquille manifeste pour « floraison » / « foisonnement ». Cosmétique mais à corriger dans une fiche de décision. | **À corriger (rédaction)** |
| A4 | Tarifs « **Localrural** 500–1 100 €/an », « LocalNova > 1 000 clients », « RCF ~500 collectivités », « Manty sur mesure » | §2/§4.3 | **Bien sourcés et datés** — rien à redire. À mettre au crédit de la fiche. | **OK** |

**Sur le terme « Girafe » (mentionné dans la commande de revue)** : la recherche web
n'a **pas confirmé** l'existence d'un produit/outil de benchmark financier des
collectivités nommé « Girafe » (2026-06-23). Les références officielles vérifiées
sont **data.ofgl.fr** (OFGL) et le **Tableau de bord financier DGFiP** (PIGP/Hélios,
fiches AEFF). À défaut de source, « Girafe » ne doit **pas** être cité comme
concurrent dans la fiche ; si une source existe, elle reste à produire (lien + date).

---

## 2. Sur-optimisme : notes de scoring (analyse adversariale)

La grille de la fiche est, fait rare, **déjà à plancher** là où ça compte
(C4=1, C5=1, C8=2, C9=2, C2=2). Il y a donc peu de marge pour « durcir »
légitimement. Examen note par note :

| Critère | Note fiche | Note revue | Verdict adversarial |
|---|---|---|---|
| **C1** Intensité | 4 | **4** | Douleur réelle et récurrente (pression budgétaire, mandats). Défendable. La douleur étant **entièrement servie par le gratuit officiel**, on pourrait plaider 3, mais le rubric note l'intensité du *problème*, pas son taux de couverture → on laisse 4. |
| **C2** Cible solvable | 2 | **2** | Correct. Payeurs réels (LocalNova >1 000 clients) mais marché capté + gratuit massif + budgets 2025-2026 tendus. Pas de 1 (des gens paient), pas de 3 (budget *additionnel* introuvable). |
| **C3** Données | 4 | **4** | OFGL/DGFiP open, API documentées, formules publiques. Légitime. Réserve sémantique (consolidation, bénéficiaire fiscal, décalage) déjà signalée. |
| **C4** Espace libre | 1 | **1** | Plancher justifié — et **renforcé** par A1/A2 : 10+ acteurs **plus** DGFiP AEFF gratuit **plus** comparaison « groupe de référence » OFGL. Aucune marge. |
| **C5** Différenciation | 1 | **1** | Plancher justifié. « Couche IA + alertes mandat » copiable, déjà investie par Manty/LocalNova. |
| **C6** Faisabilité | 4 | **4** | SQL sur OFGL + LLM cantonné au sens : conforme §3. Défendable. |
| **C7** Facilité MVP | 3 | **3** | Données prêtes (MVP technique rapide) mais méthodo strates (31 groupes DGFiP) + consolidation EPCI non triviales. 3 correct. |
| **C8** Risques | 2 | **2** | Concurrence + budget + État : non maîtrisable pour un entrant. Correct. |
| **C9** Monétisation | 2 | **2** | Revenu B2G face au gratuit, impact marginal. Correct. |

**Conclusion §2** : aucune note de la fiche n'est sur-optimiste. Le scoring est
honnête et même légèrement **conservateur** sur C1. La revue ne propose **aucun
changement de note** ; les corrections A1/A2 renforcent C4 (déjà à 1) sans pouvoir
le baisser davantage.

---

## 3. Risque d'hallucination / RAG(sens) / SQL(chiffres)

- **Architecture conforme** : chiffres en SQL sur agrégats OFGL (avec réutilisation
  des formules `methodologie-ofgl-formules-des-agregats-financiers`), LLM cantonné
  à l'explication pédagogique (épargne brute, capacité de désendettement). Conforme
  au §3 de `docs/methode-analyse.md`. **Pas de chiffre non traçable affiché** dans
  la fiche.
- **Vrai risque (bien identifié par la fiche)** : la **sémantique métier**, pas
  l'hallucination LLM. Un ratio « SQL exact » peut être trompeur si le périmètre
  (budget principal vs consolidé vs FPUN) ou le bénéficiaire fiscal (CFE perçue par
  l'EPCI) est mal posé. La fiche l'anticipe (« afficher le périmètre ») — bon réflexe.
- **Réserve supplémentaire** : la comparaison par **strate** suppose le calage sur
  les **31 groupes de référence DGFiP** (≠ strate démographique). Une erreur de
  groupe produit un « écart vs pairs » faux-vrai. À traiter comme garde-fou produit.

Verdict fiabilité : **architecture saine**, risque correctement cerné. RAS.

---

## 4. Angles morts (concurrents / coûts / réglementaire)

### Concurrents publics gratuits sous-pondérés (le point le plus important)
- **DGFiP — Tableau de bord financier (PIGP/Hélios) + fiches AEFF** : gratuit,
  officiel, avec versions consolidée/agrégée et déclinaison par niveau de
  collectivité (communes, GFP, régions, départements, **SDIS**) —
  https://www.collectivites-locales.gouv.fr/tableau-de-bord-de-lelu (2026-06-23).
  La fiche le réduit à tort à « données propres ».
- **OFGL — comparaison à un groupe de référence** : explicitement mis en avant
  comme fonction de la plateforme (taille/géographie), avec datastories et
  cartographies — https://www.collectivites-locales.gouv.fr/actualites/les-donnees-financieres-2024-sont-pretes-etre-analysees-sur-dataofglfr (2026-06-23).
  C'est **exactement** le « benchmark par strate » du seed, en gratuit.

→ Ces deux éléments ne créent pas un nouveau verdict (C4 est déjà à 1), mais ils
**ferment** définitivement l'argument « l'OFGL ne fait pas de restitution / pas de
comparaison de pairs ».

### Risques / coûts non (ou peu) traités
- **Coût d'acquisition B2G** : la fiche mentionne « CAC 12–24 mois à vérifier »
  sans le chiffrer ; combiné à un ARPU 500–1 100 €/an (segment petites communes),
  les unit economics sont à démontrer — déjà fatal, mais à expliciter.
- **Risque réputationnel/politique** : publier des classements « santé financière »
  nommant des communes peut exposer (lecture politique d'un ratio dégradé). Non cité.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 4 | 12 |
| C2 | Cible solvable | ×3 | 2 | 2 | 6 |
| C3 | Données | ×3 | 4 | 4 | 12 |
| C4 | Espace concurrentiel libre | ×2 | 1 | 1 | 2 |
| C5 | Différenciation | ×2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité | ×2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | ×2 | 3 | 3 | 6 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **56** | | **56 / 105** |

**Score /100** : 56 / 105 × 100 = **53 / 100** (inchangé).

**Changement de verdict : NON.** Fiche 53 → revue 53 → seuil < 55 → ❌ Écartée
dans les deux cas. La revue confirme et **durcit qualitativement** la saturation
sans modifier le chiffre.

---

## 6. Verdict de revue

### **ANALYSE FIABLE** (verdict écartée confirmé)

La fiche 0020 est un cas de scoring **honnête et bien sourcé** : elle n'a pas
sur-noté C2/C4, elle a documenté le gratuit institutionnel et les SaaS installés,
et elle conclut justement à l'écartage. La seule faiblesse est une **sous-estimation**
de la concurrence publique gratuite (DGFiP AEFF, comparaison « groupe de référence »
OFGL), qui va dans le sens du verdict. Aucune note n'est à relever.

### 3 actions prioritaires (si la fiche est rééditée)
1. **Corriger §4.1** : reclasser le **Tableau de bord financier DGFiP / fiches AEFF**
   comme concurrent gratuit *comparatif* (pas « données propres »), et créditer
   l'OFGL de la comparaison « groupe de référence » (liens datés 2026-06-23).
2. **Retirer ou sourcer « Girafe »** : non vérifié comme produit de benchmark
   financier ; ne pas l'introduire dans la cartographie sans lien + date.
3. **Conserver l'écartage** : ne pas prototyper. Si exploration ultérieure du
   secteur, ne viser qu'un angle **non couvert par OFGL/DGFiP/LocalNova/Manty**
   (ex. croisement finances × DECP par politique publique), confronté au terrain.

---

REVUE 0020 | analyse fiable | score recalculé 53/100 (inchangé) | changement de décision: non
