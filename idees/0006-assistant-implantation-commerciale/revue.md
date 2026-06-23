# Revue critique (red team) — 0006 Assistant d'implantation commerciale

- **Fiche auditée** : `idees/0006-assistant-implantation-commerciale/README.md`
- **Score affiché par la fiche** : 50 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : c'est l'une des **fiches les plus solides du dépôt** —
> §4 exhaustif (réutilisations data.gouv, SaaS, services publics, OSS), sources
> datées, données honnêtes sur le maillon faible (flux piéton) ; la décision
> d'écart est **juste**. Le seul reproche adversarial : **C2 reste légèrement
> généreux** (3 → 2) ; recalculée, l'idée passe de 50 à ~47/100, ce qui **renforce**
> l'écart sans le changer.

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « Mygeomarket : 300–500 €/mois — à vérifier » ; « Data-B étude 259 € HT — à vérifier » | §4 Produits commerciaux | La fiche **signale elle-même** que ces prix sont des estimations tierces non confirmées. Honnête, mais ce sont des trous de preuve. | **À sourcer (ou marquer non-chiffrant)** |
| A2 | « flux piéton des SaaS concurrents reposent en partie sur données propriétaires (à vérifier par acteur) » | §3 Données | Hypothèse plausible mais **non vérifiée acteur par acteur** ; sert pourtant d'argument-clé (maillon faible). | **À sourcer** |
| A3 | « conversion estimée » et budgets « observés » dans les tableaux §2 | §2 Cible | Mélange de prix sourcés (Smappen, Geomarket.one) et d'estimations ; bien distinguer les deux. | **À nuancer** |

**À mettre au crédit de la fiche** : c'est un **modèle de §4** au sens de
`docs/cartographie-existant.md` — les cinq canaux de la checklist B sont couverts
(réutilisations data.gouv, services publics/gratuits, SaaS FR/EU, OSS/académique,
+ comparaison de prix datés). Les prix Smappen (99/199/399 € HT/mois),
Geomarket.one (42 € HT) et l'ODIL arrêté en 2021 sont correctement sourcés et
datés. Le sourcing est **au-dessus de la moyenne du dépôt**.

---

## 2. Sur-optimisme : notes de scoring trop généreuses

### C2 — Cible solvable (qui paie) : **3 → 2** (poids ×3)
C'est le point d'attention demandé par le prompt, et le seul vrai excès de la
fiche. Trois faiblesses se cumulent :
1. **Utilisateur ≠ payeur** sur le segment le plus nombreux (indépendants), qui
   est **accompagné gratuitement par les CCI** — la fiche le dit elle-même.
2. Le segment **solvable** (franchiseurs) est aussi le **mieux équipé et le plus
   exigeant** (conformité ELM/loi Doubin) → barrière de confiance forte pour un
   nouvel entrant.
3. **Prix plancher cassé** : Geomarket.one à 42 € HT l'étude (ELM inclus) et
   Smappen gratuit jusqu'à 10 zones → le consentement à payer pour un *nouvel*
   produit horizontal tend vers zéro. Un « budget existe » ≠ « notre cible
   paiera ». Note 2, pas 3.

### Notes confirmées (défendables — peu d'optimisme ailleurs)
- **C1 = 4** : douleur réelle (emplacement = décision lourde, peu réversible). OK.
- **C3 = 3** : cœur SIRENE/INSEE/BPE solide ; flux piéton sans source nationale.
  La note 3 est honnête (ni sur- ni sous-évaluée).
- **C4 = 1**, **C5 = 1** : déjà au plancher et **pleinement justifiées** (>10
  produits sur data.gouv + SaaS établis). On ne peut pas être « plus dur » : la
  fiche a déjà fait le travail.
- **C6 = 3**, **C7 = 2**, **C8 = 2**, **C9 = 2** : toutes défendables, aucune
  n'est généreuse.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- **Architecture conforme** : SQL/PostGIS pour le chiffré (comptage concurrents
  NAF, population/revenu IRIS, densité BPE), isochrone = calcul, LLM cantonné au
  sens (NAF, ELM, « pourquoi ce quartier »). Conforme au §3 de la méthode.
- **Honnêteté remarquable** : la fiche écrit explicitement que l'archi est
  « **non conforme** si le pitch inclut flux/CA sans source traçable nationale ».
  C'est exactement le bon réflexe anti-hallucination — elle **refuse** de
  sur-vendre un chiffre (flux piéton, prévision CA) qu'elle ne peut pas tracer.
- Aucun chiffre halluciné détecté. Le risque de fiabilité est correctement
  circonscrit au flux/CA, et la fiche propose de l'omettre ou de l'avertir.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire non mentionnés)

Très peu d'angles morts — la §4 est quasi complète. Compléments mineurs
(consultés 2026-06-23) :

- **Mytraffic** (flux piéton propriétaire) : cité indirectement (« acheter des
  données propriétaires (Mytraffic, etc.) ») mais pas listé comme concurrent
  frontal sur l'analyse de zone ; c'est le détenteur de la donnée que le pitch ne
  peut pas répliquer en open data → renforce C5=1.
- **france-data-mcp** (https://github.com/cturkieh/france-data-mcp) : MCP OSS qui
  croise SIRENE + référentiels publics pour « étude de marché territoriale » →
  brique gratuite qui grignote la valeur « croisement ».
- **Urbaa.app** (https://urbaa.app/) : analyse IA de 35 000 communes (entreprises,
  démographie, finances) — recouvre la couche « comprendre un territoire » côté
  grand public, gratuit.
- **Évolution réglementaire — interdiction du démarchage** : la loi du 30 juin
  2025 (opt-in généralisé au 11 août 2026, fin de Bloctel) durcit l'usage
  prospection B2B issu de SIRENE/BODACC. À ajouter aux risques RGPD déjà bien
  traités (https://www.service-public.gouv.fr/particuliers/actualites/A18384).

Aucun de ces compléments ne change le verdict : ils **renforcent** C4/C5 (déjà au
plancher) et le risque réglementaire (C8).

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 4 | 12 |
| C2 | Cible solvable (qui paie) | ×3 | 3 | **2** | 6 |
| C3 | Disponibilité & fiabilité données | ×3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 1 | 1 | 2 |
| C5 | Différenciation défendable | ×2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | ×2 | 3 | 3 | 6 |
| C7 | Facilité du MVP | ×2 | 2 | 2 | 4 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **52** | | **49 / 105** |

**Score /100** : 49 / 105 × 100 = **46,7 → 47 / 100**.

**Changement de décision : NON.**
- Fiche : 50/100 → < 55 → ❌ Écartée.
- Revue : 47/100 → < 55 → ❌ **Écartée** (renforcée). Même bande, même verdict.

---

## 6. Verdict de revue

### **ANALYSE FIABLE** (avec une correction mineure de C2) → ❌ Écartée confirmée

C'est une analyse **rigoureuse, bien sourcée et honnête** sur ses propres limites
(flux piéton, conformité ELM, non-conformité RAG si on sur-vend le CA). La
décision d'écart est **correcte**. Le seul ajustement adversarial est **C2 (3 →
2)** : la fiche confond « un budget existe » avec « notre cible horizontale
paiera », alors qu'un prix plancher (42 € HT) et un freemium (Smappen) cassent la
willingness-to-pay. Le score passe de 50 à 47/100 — sous le seuil dans les deux
cas. Aucune raison de réhabiliter l'idée.

### 3 actions prioritaires
1. **Acter C2 = 2** (et le score 47) pour refléter le prix plancher / freemium et
   le verrou CCI sur le segment indépendant.
2. **Sourcer ou neutraliser** les prix marqués « à vérifier » (Mygeomarket,
   Data-B) et l'hypothèse « flux propriétaires » acteur par acteur (A1/A2).
3. **Ne rouvrir que sur une niche verticale + canal captif** (CCI/banque/réseau
   de franchise) avec payeur signé — comme la fiche le recommande déjà — sinon
   prioriser des idées à concurrence plus faible.

---

REVUE 0006 | analyse fiable | score recalculé 47/100 (vs 50) | changement de décision: non (❌ confirmée)
