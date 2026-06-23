# Revue critique (red team) — 0003 Copilote d'études territoriales (RAG)

- **Fiche auditée** : `idees/0003-copilote-territorial-rag/README.md`
- **Score affiché par la fiche** : — / 100 (analyse partielle) — Statut affiché : 🔁 À retravailler
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche identifie bien le bon piège (RAG vs
> chiffres) mais reste une **coquille incomplète** (pas de §2 payeur, pas de §5,
> §7, §8, §9, pas de scoring) qui sous-estime la **saturation réelle** : le
> créneau « brancher une IA sur les données publiques d'un territoire » est déjà
> occupé par l'**acteur officiel** (MCP data.gouv.fr) **et** par un produit grand
> public direct (**Urbaa.app**, 35 000 communes analysées par IA). En produit
> généraliste autonome, l'idée est **écartée**.

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « Explorer data.gouv.fr est lent pour un non-spécialiste » | §1 Problème | Plausible mais **non sourcé** et, surtout, **déjà résolu** par le MCP officiel + Urbaa.app. La douleur est asséchée par l'existant. | **À nuancer / sourcer** |
| A2 | « l'acteur officiel occupe déjà le terrain "brancher un LLM sur data.gouv.fr" » | §11 Verdict | **Vrai**, et c'est l'aveu central : la fiche reconnaît la saturation mais ne l'inscrit ni en §4 complet ni dans un score. | **À conserver, mais à scorer** |
| A3 | « La valeur n'est pas la connexion (déjà faite) mais la fiabilité vérifiable » | §11 Verdict | Affirmation **décisive et non démontrée** : aucune preuve que « fiabilité vérifiable » soit (a) un manque réel des concurrents, (b) un différenciateur défendable, (c) quelque chose qu'un payeur achèterait. | **À sourcer / prouver** |
| A4 | « risque de généraliste peu fiable » (§3, ligne multi-domaines) | §3 Données | Honnête, mais c'est un **angle mort transformé en note de bas de tableau** : ce risque devrait éliminer la version généraliste, pas la décorer. | **À ériger en risque §8** |

**À mettre au crédit de la fiche** : les sources de données §3 sont bien
renseignées (MCP data.gouv, Melodi, API tabulaire) avec licence, format,
fraîcheur et limites. Le §6 cite correctement l'avertissement officiel de
data.gouv.fr (« réponses approximatives ou erronées », « en aucun cas une source
officielle »). Le sourcing data est honnête ; ce qui manque, c'est le **sourcing
là où ça compte** : le payeur (§2 absente) et l'existant produit (§4 tronqué au
seul MCP officiel).

---

## 2. Sur-optimisme : la fiche n'a pas de notes… ce qui est en soi un sur-optimisme

La fiche ne propose **aucun tableau de scoring** (§10 absente) tout en gardant un
statut 🔁 « À retravailler » — c'est-à-dire qu'elle se maintient implicitement
au-dessus du seuil d'élimination **sans l'avoir jamais démontré**. C'est le
sur-optimisme le plus net : un statut favorable par défaut, sans preuve chiffrée.

Notes attribuées par la revue (détail en §5), avec attention C2/C4 :

- **C2 (qui paie) = 2** : **aucun payeur identifié** dans la fiche (§2 manquante).
  Le MCP officiel est **gratuit** et public ; Urbaa.app propose une consultation
  grand public **gratuite**. Pour un copilote généraliste, le consentement à
  payer tend vers zéro hors prestation de conseil — qui n'est pas le produit.
- **C4 (espace libre) = 1** : le terrain est **occupé par l'acteur officiel**
  lui-même (cf. §4 de cette revue). Quand le producteur de la donnée publie son
  propre MCP gratuit, l'espace « connecter un LLM à data.gouv » n'est pas
  « partiel », il est **fermé**.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- **Bon réflexe** : la fiche pose la règle RAG(sens)/SQL(chiffres) et cite
  l'avertissement de data.gouv.fr. C'est conforme au §3 de la méthode **en
  intention**.
- **Mais le généralisme rend la règle inapplicable en pratique** : garantir que
  *chaque* chiffre, *sur tous les domaines* (finances OFGL, démographie INSEE,
  immobilier DVF, transport, etc.), soit traçable jusqu'à une requête SQL
  exacte, suppose un travail de modélisation **par vertical**. Un copilote
  « tout data.gouv » qui s'appuie sur la sélection automatique de jeux via le
  catalogue MCP est, par construction, **exposé** : sélection du mauvais jeu,
  mauvais millésime, agrégat non sommable (IRIS, secret statistique), jointures
  approximatives. Le risque n'est pas l'hallucination LLM « pure » mais
  l'**erreur de pipeline généraliste** — plus insidieuse car les chiffres
  *paraissent* sourcés.
- C'est exactement pourquoi la fiche elle-même conclut « vertical first » — ce
  qui revient à **dire que le produit généraliste ne tient pas**.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire non mentionnés)

### Concurrents directs OMIS — tous consultés le 2026-06-23

- **MCP officiel data.gouv.fr** (cité, mais sous-estimé) : instance publique
  hébergée `https://mcp.data.gouv.fr/mcp`, **sans clé, sans restriction**,
  compatible Claude / ChatGPT / Mistral, expose `search_datasets`,
  `query_resource_data`, etc. (https://github.com/datagouv/datagouv-mcp ,
  https://www.data.gouv.fr/posts/experimentation-autour-dun-serveur-mcp-pour-datagouv ,
  release v0.2.27 du 2026-06-19). **L'État livre lui-même la brique de connexion.**
- **POC Mediatech + MCP + Albert API** (DINUM / IA dans l'État) : stack
  souveraine catalogue vectorisé + MCP + LLM Albert pour interroger les données
  de l'État — https://ia.numerique.gouv.fr/actualites/les-mcp-le-standard-qui-connecte-lia-aux-donnees-vivantes-de-letat/
  (consulté 2026-06-23). L'écosystème public construit déjà la couche IA.
- **Urbaa.app** — https://urbaa.app/ (consulté 2026-06-23) : **concurrent grand
  public quasi exact du pitch**. « Analyse les données publiques de 35 000
  communes grâce à l'IA pour comprendre et **comparer les territoires** »,
  29 sources open data croisées, modules Économie & Finances (budget communal,
  fiscalité, dette), prix immobilier, délinquance, taxes foncières, qualité de
  l'eau, résultats des municipales 2026. C'est, mot pour mot, « comparer des
  communes, expliquer des finances locales ».
- **h-genai** (OSS) — https://github.com/podolskyDavid/h-genai : système
  d'analyse de communes/EPCI **OFGL API + LLM + RAG**, profils financiers,
  comparaison à des communes de référence (Vue.js + AWS Bedrock). Le « copilote
  finances locales » existe déjà en open source.
- **france-data-mcp** (OSS, déjà cité en 0006) — https://github.com/cturkieh/france-data-mcp :
  MCP qui croise 6 référentiels publics FR, pensé pour « étude de marché
  territoriale, journalisme local ». Concurrent OSS de la couche « croisement ».
- **OFGL / data.ofgl.fr** — outils intégrés de datavisualisation et de
  **comparaison d'une collectivité à un groupe de référence** (taille,
  géographie), cartographie sur mesure, accès au détail des comptes
  (https://www.collectivites-locales.gouv.fr/etudes-et-statistiques/observatoire-des-finances-et-de-la-gestion-publique-locales-ofgl ,
  consulté 2026-06-23). La comparaison de finances locales est déjà un service
  public outillé.

→ Conclusion : la fiche ne cite que le MCP officiel et un « MCP tiers ». Elle a
**manqué le concurrent grand public direct (Urbaa.app)**, les briques OSS
(h-genai, france-data-mcp) et l'outillage public de comparaison (OFGL, POC
Albert). Le §4 est **tronqué** ; conclure quoi que ce soit sur C4 sans cette
cartographie B complète viole `docs/cartographie-existant.md`.

### Risques non mentionnés

- **Disqualification par l'éditeur de la donnée** : data.gouv.fr avertit que ces
  dispositifs sont « difficiles à auditer » et « en aucun cas une source
  officielle ». Un produit commercial qui en dépend hérite du **risque
  réputationnel** d'un chiffre faux présenté comme fiable.
- **Dépendance plateforme** : bâtir sur le MCP officiel = dépendre d'une **API
  expérimentale** (statut affiché « expérimentation ») susceptible de changer.
- **Coûts non chiffrés** : indexation multi-domaines, maintenance des jointures
  métier par vertical, coût LLM par requête — aucun budget esquissé.
- **MCP « faux officiels »** : data.gouv.fr signale la prolifération de serveurs
  MCP se présentant comme liés sans l'être → risque de confusion de marque.

---

## 5. Recalcul du score avec mes notes

La fiche n'ayant pas de tableau, je reconstruis le scoring à partir du §5 de la
méthode (notes 1–5 × poids).

| # | Critère | Poids | Note revue | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | 9 | Douleur réelle mais **diffuse et déjà asséchée** par MCP officiel + Urbaa. |
| C2 | Cible solvable (qui paie) | ×3 | 2 | 6 | **Aucun payeur identifié** (§2 absente) ; alternatives gratuites (MCP, Urbaa). |
| C3 | Disponibilité & fiabilité données | ×3 | 3 | 9 | Inputs prêts (MCP, Melodi, OFGL) mais **fiabilité généraliste fragile**. |
| C4 | Espace concurrentiel libre | ×2 | 1 | 2 | **Occupé par l'acteur officiel** + Urbaa + OSS (h-genai, france-data-mcp). |
| C5 | Différenciation défendable | ×2 | 2 | 4 | « Fiabilité vérifiable » non prouvée, **copiable**, et déjà visée par l'État. |
| C6 | Faisabilité & fiabilité technique | ×2 | 3 | 6 | RAG/SQL en intention OK, mais **inapplicable en généraliste** sans verticaux. |
| C7 | Facilité du MVP | ×2 | 2 | 4 | Périmètre « tout data.gouv » **trop large** ; la fiche admet « vertical first ». |
| C8 | Maîtrise des risques | ×2 | 2 | 4 | Risque concurrentiel (acteur officiel) + fiabilité **non maîtrisés**. |
| C9 | Monétisation / impact | ×2 | 2 | 4 | Pas de revenu (gratuit public) ; impact déjà porté par data.gouv/Albert. |
| | **Total** | | | **48 / 105** | |

**Score /100** : 48 / 105 × 100 = **46 / 100**.

**Changement de décision : OUI.**
- Fiche : statut 🔁 À retravailler, sans score (au-dessus du seuil par défaut).
- Revue : 46/100 → seuil < 55 → ❌ **Écartée** (en produit généraliste autonome).

---

## 6. Verdict de revue

### **À CORRIGER** → décision : ❌ Écartée (produit généraliste)

L'analyse est **incomplète** (sections 2, 5, 7, 8, 9, 10 absentes) et son statut
🔁 n'est justifié par aucun score. Une fois la cartographie B complétée (Urbaa,
h-genai, france-data-mcp, OFGL, POC Albert) et le scoring posé, le **copilote
généraliste tombe sous le seuil** (46/100). Le bon réflexe de la fiche
(« vertical first », « la valeur est la fiabilité ») est précisément l'aveu que
le produit horizontal n'a pas de marché propre : c'est une **couche transverse**,
pas une idée à prototyper seule.

### 3 actions prioritaires
1. **Acter l'écart du produit généraliste** : ne pas prototyper un « copilote
   tout data.gouv ». Compléter le §4 avec Urbaa.app, h-genai, france-data-mcp,
   OFGL et le POC Albert (liens datés), puis écrire §2 (payeur) honnêtement.
2. **Reformuler en couche transverse d'un vertical existant** (ex. la fiabilité
   vérifiable au-dessus de 0001), avec un **payeur B2B/B2G précis** et un
   différenciateur prouvé face à Urbaa et au MCP officiel — sinon clore.
3. **Documenter le risque de pipeline généraliste** (sélection de jeu, millésime,
   agrégats non sommables, secret statistique) en §8 et en faire un critère
   éliminatoire explicite tant que le périmètre reste horizontal.

---

REVUE 0003 | à corriger | score recalculé 46/100 (vs —) | changement de décision: oui (🔁 → ❌)
