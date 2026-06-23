# Revue critique (red team) — 0018 Transparence de la vie publique

- **Fiche auditée** : `idees/0018-transparence-vie-publique/README.md`
- **Score affiché par la fiche** : 50 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : le verdict **❌ Écartée est solide** (risque pénal sur
> le patrimoine + saturation + pas de payeur). La revue le **conforte et le durcit**
> sur l'espace concurrentiel : **VigiCité** s'est encore étoffé (6 763 élus,
> 2,29 M relations, MàJ 11/06/2026, **AGPL open source**, et il intègre **déjà
> l'OFGL**), ce qui rend les notes C4=2 et C5=2 trop hautes. Recalcul : **46/100**.

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « VigiCité : 6 763 élus, score /100, ~2,29 M de relations » | §4 | **Vérifié et exact** (voir §4 ci-dessous). Bon réflexe. RAS. | **OK** |
| A2 | « les vrais payeurs solvables (affaires publiques) veulent un autre produit » | §2 | Plausible et cohérent avec les exemples (Contexte/Legiwatch/Dixit sourcés), mais asséné comme certitude. | **À nuancer** (suffisant pour conclure, pas absolu) |
| A3 | « la structure XML des déclarations est documentée (opendata-structure.xlsx) — à vérifier que le lien est encore actif » | §3 | Auto-incertitude honnête, mais un input central laissé non vérifié. | **À sourcer / vérifier** |
| A4 | « patrimoine des parlementaires non diffusable, consultable seulement en préfecture » | §3/§8 | **Affirmation décisive** (fonde le risque éliminatoire). Correctement sourcée (Sénat, Légifrance LO 135-2 / 226-1). | **OK — à conserver** |

**À mettre au crédit de la fiche** : §3 (sources HATVP/CNCCFP/RNE/RNA/DECP/SCDL
avec licences, fraîcheur, limites, et **croisements + risques** détaillés en 3bis),
§4 (VigiCité, Integrity Watch, Poligraph, Regards Citoyens, HATVP — datés
2026-06-20) et §8 (risque pénal patrimoine **chiffré et sourcé**) sont **de très
bonne facture**. La fiche est rigoureuse ; la revue ne corrige que C4/C5.

---

## 2. Sur-optimisme : notes de scoring trop généreuses

### C4 — Espace concurrentiel libre : **2 → 1** (poids ×2)
La fiche note 2 (« occupé, en cours de consolidation ») mais décrit en réalité un
créneau **entièrement servi par plusieurs acteurs gratuits et légitimes** :
VigiCité (croise HATVP × marchés × lobbys, score /100, droit de réponse — « quasi
exactement le produit du seed »), Integrity Watch (Transparency France), Poligraph
(parsing HATVP), Regards Citoyens (historique, AGPL + API). Quand le produit décrit
**existe déjà à l'identique, gratuitement et en open source**, c'est l'ancrage 1
(« saturé public + commercial »), pas 2. Le « résidu » (API requêtable car HATVP
n'a pas d'API) est une **optimisation marginale**, pas un espace.

### C5 — Différenciation défendable : **2 → 1** (poids ×2)
La fiche dit elle-même : « tout ce que propose le seed est **déjà livré
gratuitement** par VigiCité, Integrity Watch et Poligraph, à partir des mêmes
sources ; aucune barrière ; reproductible en quelques semaines ». C'est la
définition de l'ancrage 1 (« copiable en un week-end »). Pire : VigiCité est
**AGPL** — le code est public et **réutilisable**, ce qui annule tout avantage
technique. Note 1.

### Notes laissées inchangées (défendables)
- **C1 = 3** : besoin de recoupement réel mais **tiède** et porté par une niche
  militante/éditoriale. OK.
- **C2 = 2** : utilisateurs (journalistes/ONG/citoyens) ne paient pas ; payeurs
  solvables (affaires publiques) veulent un autre produit. OK.
- **C3 = 3** : ouvert, structuré, frais (MàJ nocturne AGORA) **mais** déclaratif,
  sans API officielle, et un pan (patrimoine) **juridiquement hors-jeu**. Juste.
- **C6 = 3** : archi SQL/RAG saine, mais **matching nominatif bruité** =
  faiblesse intrinsèque (un faux positif devient une accusation). OK.
- **C7 = 3** : ingestion faisable mais alourdie par la **revue juridique** et
  l'anti-faux-positifs indispensables. OK.
- **C8 = 2** : risques diffamation/RGPD + **pénal sur le patrimoine** seulement
  partiellement maîtrisables. OK (et c'est le point éliminatoire).
- **C9 = 2** : revenu faible, impact déjà capté par des ONG plus légitimes. OK.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- **Architecture conforme si bien conçue** : montants (comptes de partis,
  financements), volumes et croisements doivent venir de requêtes structurées
  (XML/CSV → SQL) ; LLM borné au sens (libellés, notions juridiques). Le LLM ne
  doit jamais produire un chiffre.
- **Le vrai risque n'est pas l'hallucination, c'est le matching** : relier un élu à
  une entreprise/un marché/un lobby repose sur du rapprochement nominatif/SIREN
  **bruité**. Un faux positif n'est pas une erreur anodine : il devient une
  **accusation potentiellement diffamatoire**. VigiCité le reconnaît
  implicitement (droit de réponse, filtrage du bruit, « scores de cohérence, pas
  des jugements », intervalle de confiance par score — vérifié 2026-06-23). C'est
  une faiblesse structurelle, pas architecturale → pèse sur C6 (déjà 3) et C8.
- **Données déclaratives saisies à la main** : la fiabilité « chiffre traçable »
  est plafonnée par la qualité à la source, pas par l'archi.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire)

### Le concurrent direct **s'est renforcé** (justifie C4=1, C5=1)
VigiCité, consulté 2026-06-23 (https://vigicite.org/, /a-propos, /methodologie,
/dashboard) — chiffres **supérieurs** à ceux de la fiche :
- **6 763 élus** référencés, **182 093 marchés publics**, **2 292 713 relations
  détectées**, MàJ tableau de bord **11/06/2026** ;
- **5 dimensions de score** (cohérence, concentration marchés, réseau,
  transparence, composite), **intervalle de confiance** par score, **droit de
  réponse** (loi 1881 art. 13), pipeline reproductible, **exports CSV/JSON** ;
- **sources** : HATVP, DECP, SIRENE, Journal Officiel, registre des lobbys, RNA,
  CNCCFP **et OFGL** — c'est-à-dire **plus** de sources que le seed (qui n'évoque
  pas l'OFGL) ;
- **open source AGPL-3.0** : le code est public, donc le « différenciateur
  technique » du seed est **déjà donné** ;
- conformité affichée (RGPD art. 86 « accès du public aux documents officiels »,
  données exclusivement publiques) — il a **déjà résolu** les garde-fous que le
  seed devrait encore construire.

→ Non seulement le créneau est saturé, mais le concurrent gratuit a **déjà traité
les angles les plus durs** (matching qualifié, droit de réponse, conformité,
open source). Le seed n'apporte **rien de défendable**. C4=1, C5=1.

### Risques non (assez) soulignés
- **Risque pénal patrimoine** (déjà §8, éliminatoire) : republier la situation
  patrimoniale = infraction (45 000 €). Confirmé.
- **Open source du concurrent** : impossible de bâtir un moat technique quand
  l'acteur dominant publie son code sous AGPL (toute amélioration doit elle-même
  être ouverte).
- **Légitimité** : ONG reconnues (Transparency, Regards Citoyens) financées par
  dons/subventions — un entrant privé est moins crédible **et** doit en plus
  trouver un revenu.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | ×3 | 2 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | ×3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 2 | **1** | 2 |
| C5 | Différenciation défendable | ×2 | 2 | **1** | 2 |
| C6 | Faisabilité & fiabilité technique | ×2 | 3 | 3 | 6 |
| C7 | Facilité du MVP | ×2 | 3 | 3 | 6 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **52** | | **48 / 105** |

**Score /100** : 48 / 105 × 100 = **46 / 100**.

**Changement de verdict : NON** (reste ❌ Écartée ; marge sous le seuil de 55
élargie de 50 → 46). Le point **éliminatoire** (risque pénal patrimoine) reste
prioritaire sur le score : même un score plus haut ne sauverait pas l'idée tant que
le seed cite explicitement les déclarations de **patrimoine**.

---

## 6. Verdict de revue

### **ANALYSE FIABLE** (C4/C5 un cran trop hauts, sans effet sur la décision)

La fiche est **rigoureuse** : elle identifie le risque pénal patrimoine (chiffré et
sourcé), la saturation par des ONG gratuites et l'absence de payeur. La revue
n'inverse rien ; elle **durcit** C4 et C5 (le créneau n'est pas « en consolidation »
mais **entièrement servi**, par un concurrent qui a même **publié son code en
AGPL** et **intègre déjà l'OFGL**), et confirme le verdict ❌ Écartée à **46/100**.

### 3 actions prioritaires
1. **Maintenir ❌ Écartée** ; conserver le risque pénal patrimoine comme **motif
   éliminatoire** prioritaire, indépendamment du score.
2. **Acter la saturation** : VigiCité (AGPL, 2,29 M relations, OFGL inclus) +
   Integrity Watch + Poligraph + Regards Citoyens ne laissent **aucun** espace
   produit ni technique défendable.
3. **Si recyclage de la donnée HATVP**, se limiter à une **brique technique**
   (API/jeu propre, **jamais le patrimoine**) traitée comme **nouvelle fiche** —
   et seulement si un usage non couvert par VigiCité (open source) est démontré.

---

REVUE 0018 | analyse fiable | score recalculé 46/100 (vs 50) | changement de décision: non
