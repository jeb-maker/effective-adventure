# Revue critique (red team) — 0019 Sourcing & benchmark de prix pour acheteurs publics

- **Fiche auditée** : `idees/0019-sourcing-achat-public/README.md`
- **Score affiché par la fiche** : 53 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : le verdict **❌ Écartée est juste et très bien
> documenté** (≥ 8 concurrents, dont 3 B2G dédiés). La revue le **conforte** : le
> dernier sous-créneau résiduel envisagé — « acheteurs comparables par strate
> financière » via DECP × **OFGL** — est **déjà servi gratuitement par l'OFGL
> lui-même** (data.ofgl.fr, comparaison à un groupe de référence). C2 reste un cran
> trop haut → recalcul **50/100**, toujours ❌ Écartée.

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « marchespublics.ai : 290 / 990 / 2 490 € HT/mois » | §2/§4 | **Vérifié, sourcé** (liens /administrations, /tarifs datés). Bon. | **OK** |
| A2 | « MA.iA : 300+ organismes publics, +16 M données, via UGAP » | §2/§4 | Sourcé (ma-ia.app + fiche UGAP). Le « +16 M données » est marketing éditeur → à présenter comme tel. | **OK (nuancer le chiffre éditeur)** |
| A3 | « consentement à payer faible pour la seule couche données » | §2 | Plausible (gratuit + bundling), mais asséné sans donnée. | **À nuancer** |
| A4 | « effort technique modéré (4–8 semaines pour un MVP) » | §9 | Estimation d'effort non étayée ; sert à charge (souligne l'absence de barrière), donc peu gênant. | **Reformuler** (estimation) |

**À mettre au crédit de la fiche** : §4 est **remarquable** — 10 acteurs classés
(3 B2G dédiés : marchespublics.ai, MA.iA, Sam IA ; 3 suites MPE : Atexo, Ordiges,
achatpublic ; 3 gratuits : decp.info, data.economie, Nextend ; + ressource OECP),
tous datés 2026-06-20, avec distinction nette vs idée 0001. Le §3 (sémantique
`montant` DECP, seuils, fusion recensement/DECP) et le §6 (limite métier du
« prix ») sont rigoureux. C'est une fiche **solide** ; la revue ne corrige qu'à la
marge.

---

## 2. Sur-optimisme : notes de scoring trop généreuses

### C2 — Cible solvable (qui paie) : **3 → 2** (poids ×3)
La fiche démontre pourtant que le budget standalone est **difficile à arracher** :
(1) **gratuits** couvrant le cœur (decp.info, data.economie, Nextend), (2)
**bundling** dans les suites MPE déjà payées (Atexo, Ordiges), (3) **cycle d'achat
public** lent avec préférence pour les centrales (UGAP, CAIH). La fiche conclut
elle-même : « le budget *additionnel* pour un outil standalone DECP est difficile à
arracher face au gratuit et au bundling ». C'est l'ancrage 2 (« budget capté/
indirect, pas additionnel »), pas 3. Le 3 surévalue un budget qui existe **mais va
ailleurs** (suites MPE, centrales).

### Notes laissées inchangées (défendables)
- **C1 = 4** : estimation prix, sourcing, comparaison inter-acheteurs sont des
  douleurs **récurrentes** documentées (guide OECP, discours marketing des
  concurrents). OK — on ne descend pas, la douleur est réelle.
- **C3 = 3** : DECP ouvert/quotidien, SQL fiable sur agrégats, **mais** `montant`
  ≠ dépense réelle, pas de prix unitaires, délais de publication longs. Juste.
- **C4 = 1**, **C5 = 1** : **mérités et confortés** (voir §4 : ≥ 8 acteurs +
  OFGL sur le dernier résidu).
- **C6 = 4** : archi RAG(sens)/SQL(chiffres) saine sur agrégats ; réserve métier
  sur le « prix » affiché. OK.
- **C7 = 3** : MVP rapide techniquement mais sans créneau pour le déployer. OK.
- **C8 = 2** : concurrence/commoditisation + promesse prix fragile. OK.
- **C9 = 2** : revenu standalone faible, impact déjà capté. OK.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- **Architecture conforme** : volumes, médianes, comptages par CPV/région/acheteur,
  listes de titulaires = **requêtes SQL** (DuckDB/PostgreSQL) sur DECP + jointure
  SIRENE ; LLM borné à l'explication (CPV, procédures). Conforme.
- **Le vrai risque est métier, pas hallucinatoire** (et la fiche l'a très bien
  vu) : le champ `montant` DECP = montant **à la notification** / **maximum**
  d'accord-cadre, **pas la consommation réelle**. Un « benchmark prix » présenté
  comme « ce que paient les collectivités » est **exact en SQL et trompeur en
  métier**. À cela s'ajoutent l'absence de **prix unitaires** (DPGF/BPU hors DECP)
  et les **délais de publication** (mois à années). Un produit honnête doit
  afficher **taux de couverture + disclaimer sémantique** (déjà prévu §9) — bon
  réflexe, mais cela révèle aussi la faiblesse de la promesse « prix ».

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire)

### Le dernier résidu (« acheteurs comparables ») est **déjà servi, gratuitement**
La fiche envisageait, comme croisement à valeur (§3bis) et comme écran MVP (§9),
le rapprochement **DECP acheteur × OFGL** pour comparer un acheteur à ses pairs
« par strate financière ». Or l'**OFGL le fait déjà nativement**, consulté
2026-06-23 :
- **data.ofgl.fr** (portail public, gratuit, lancé 2020, **données définitives
  2024** en ligne) permet de **« comparer une collectivité à un groupe de référence
  aux caractéristiques proches (taille, géographie…) »**, créer ses
  datavisualisations, cartographier les agrégats, et **piocher dans le détail des
  comptes** (balances DGFiP). —
  https://www.collectivites-locales.gouv.fr/etudes-et-statistiques/observatoire-des-finances-et-de-la-gestion-publique-locales-ofgl
  et https://www.collectivites-locales.gouv.fr/actualites/les-donnees-financieres-2024-sont-pretes-etre-analysees-sur-dataofglfr
- Couplé à **Nextend.ai — comparateur jusqu'à 5 acheteurs** (gratuit, déjà cité §4)
  côté commande publique, le « benchmark inter-acheteurs » est **doublement
  couvert** (finances via OFGL, marchés via Nextend) — sans payer.

→ Le seul sous-créneau que la fiche laissait entrevoir comme à valeur est donc
**fermé par un outil public gratuit**. Cela conforte C4=1 et **retire tout
argument de différenciation** restant (C5=1). Le §4 mérite d'ajouter OFGL à la
liste des substituts gratuits du « comparateur d'acheteurs ».

### Risques / coûts non (assez) soulignés
- **Pas de risque éliminatoire juridique** (données DECP ouvertes + agrégats) — la
  fiche le note justement ; la vigilance porte sur la **formulation sourcing** (ne
  pas créer de liste restreinte déguisée). OK.
- **CAC B2G élevé pour ARPU modeste** (quelques k€/an), cycle long via centrales —
  bien vu §8, mais c'est ce qui rend le modèle standalone non viable.
- **Couverture incomplète** (MAPA < 40 k€ absents, accords-cadres sans
  consommation, publication tardive) → benchmark/sourcing structurellement
  incomplets sur les marchés récents.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 4 | 12 |
| C2 | Cible solvable (qui paie) | ×3 | 3 | **2** | 6 |
| C3 | Disponibilité & fiabilité données | ×3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 1 | 1 | 2 |
| C5 | Différenciation défendable | ×2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | ×2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | ×2 | 3 | 3 | 6 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **56** | | **53 / 105** |

**Score /100** : 53 / 105 × 100 = **50 / 100**.

**Changement de verdict : NON** (reste ❌ Écartée ; marge sous le seuil de 55
élargie de 53 → 50). Le créneau est **saturé côté acheteur** (≥ 8 produits) et le
dernier résidu de différenciation (« acheteurs comparables ») est **fermé par
l'OFGL gratuit**.

---

## 6. Verdict de revue

### **ANALYSE FIABLE** (C2 un cran trop haut, sans effet sur la décision)

La fiche est **exemplaire** sur l'existant et la sémantique de la donnée. La revue
ne change pas la décision ; elle corrige C2 (budget existant ≠ additionnel → 2) et
**ferme le dernier résidu** en montrant que le « comparateur d'acheteurs » envisagé
est déjà rendu gratuitement par **OFGL/data.ofgl.fr** (finances) et **Nextend**
(marchés). Score recalculé **50/100**, ❌ Écartée confirmée.

### 3 actions prioritaires
1. **Maintenir ❌ Écartée** ; ajouter **OFGL/data.ofgl.fr** au §4 comme substitut
   gratuit du benchmark inter-acheteurs (et retirer ce croisement de la liste des
   différenciateurs §3bis/§9).
2. **Ne plus créditer un budget standalone** (C2=2) : le budget existe mais part
   aux suites MPE (bundling) et aux centrales (UGAP/CAIH).
3. **Réserver toute relance à un sous-créneau réellement non couvert** (ex. prix
   **unitaires DPGF** côté acheteur à l'instruction, hors DECP agrégé) — à valider
   par une **nouvelle recherche existant** avant toute capture, pas en sauvetage.

---

REVUE 0019 | analyse fiable | score recalculé 50/100 (vs 53) | changement de décision: non
