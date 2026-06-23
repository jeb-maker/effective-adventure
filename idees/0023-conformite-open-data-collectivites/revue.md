# Revue critique (red team) — 0023 Conformité de publication open data (B2G)

- **Fiche auditée** : `idees/0023-conformite-open-data-collectivites/README.md`
- **Score affiché par la fiche** : 47 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche est déjà très sévère et juste sur le fond
> (donnée normative absente, internalisation ODF, pas de payeur). Adversarialement,
> elle reste **trop généreuse sur C1** : sans sanction, avec la priorité
> « transparence » en recul, l'intensité du besoin *non satisfait* est tiède, pas
> forte. C1 passe de 4 à 3, score de **47 à 44/100**. La revue ajoute deux angles
> morts (**udata-hydra** et **Éclaireur Public**) qui cimentent C4=1.

---

## 1. Affirmations non sourcées (à sourcer / à corriger)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « 30 % … ont publié au moins un jeu » ; « 16 % … le font réellement » | §1 | **Bien sourcés** (Observatoire ODF ; étude Data Publica × Opendatasoft via BDT, datés). OK. | **OK** |
| A2 | « absence de sanctions prévues pour le non-respect » | §1 | **Sourcé** (Datactivist/rapport Ardèche). Point capital pour C1 (voir §2). OK. | **OK** |
| A3 | « adoption SCDL ~**1,5 %** des jeux Opendatasoft » | §3 | Sourcé (BDT avril 2024). Chiffre fort, bien utilisé. | **OK** |
| A4 | « roadmap ODF 2026 = profils + **recommandations adaptées** » | §4.1 | Sourcé (rapport ODF 2025). C'est l'argument-clé de fermeture du gap « feuille de route » — solide. | **OK** |
| A5 | Catalogue : segment `open-data-governance-fr` cité comme appui §4 | §4 | La fiche **ne s'appuie pas uniquement** sur le catalogue SaaS : elle développe 10 sous-sections publiques/associatives. Conforme à `cartographie-existant.md`. **OK.** | **OK** |

**À mettre au crédit de la fiche** : §4 (10 acteurs publics/associatifs datés) est
exhaustif ; le §6 (tableau RAG/SQL) démontre proprement que tout « % conformité
réglementaire » global serait non traçable. C'est une fiche honnête.

---

## 2. Sur-optimisme : notes de scoring

| Critère | Note fiche | Note revue | Justification adversariale |
|---|---|---|---|
| **C1** Intensité | 4 | **3** | **Trop généreux.** Le rubric : 5 = « douleur forte, récurrente », 1 = « besoin tiède ». Or la fiche établit elle-même : **aucune sanction** (LRN), priorité « transparence » en **recul** (43 % vs 59 %), achat tiède côté élu. Une obligation légale **sans levier** = besoin **tiède** → **3**, pas 4. Le « ~70 % sous le seuil minimal » mesure le non-usage, pas l'intensité de la douleur ressentie. |
| **C2** Cible solvable | 2 | **2** | Correct. Aucun payeur récurrent identifié ; budgets captés par portails (Huwise) et dispositifs publics gratuits (ODF, ODL financés DINUM/ANCT/BDT). |
| **C3** Données | 3 | **3** | Correct. Publication traçable via API data.gouv ; **inventaire des obligations par collectivité absent** (RIP non unifié). 3 défendable. |
| **C4** Espace libre | 1 | **1** | Plancher justifié — et renforcé (voir §4 : udata-hydra, Éclaireur Public). |
| **C5** Différenciation | 2 | **2** | Micro-angle SCDL×org imitable par ODF/Validata en un sprint ; on pourrait plaider 1, mais 2 reste acceptable (un module check-list a une mince valeur résiduelle). Laissé à 2. |
| **C6** Faisabilité | 2 | **2** | SQL OK pour comptages, mais conformité CRPA globale = RAG/heuristiques non traçables (anti-§3). Correct. |
| **C7** Facilité MVP | 2 | **2** | MVP honnête = check-list SCDL + statut publication ; vérificateur CRPA complet hors portée. Correct. |
| **C8** Risques | 2 | **2** | Internalisation ODF probable, donnée normative absente, priorité en recul. Correct. |
| **C9** Monétisation | 2 | **2** | Impact OSS possible, revenu B2G ≈ nul face au gratuit. Correct. |

**Seule correction retenue : C1 4 → 3.**

---

## 3. Risque d'hallucination / RAG(sens) / SQL(chiffres)

- **Point fort de la fiche** : elle **refuse** explicitement d'afficher un « %
  conformité réglementaire » global, faute de dénominateur (inventaire des
  obligations) → conforme au principe anti-hallucination §3. C'est exactement le
  bon réflexe.
- **Risque résiduel** : la « feuille de route » générée par LLM/heuristique est, de
  l'aveu de la fiche, **non traçable** sans inventaire interne ; à ne livrer que comme
  **template** explicitement non personnalisé (§9 le dit). Bien.
- **Pas de chiffre inventé** affiché. RAS.

---

## 4. Angles morts (concurrents non mentionnés — 2026-06-23)

### Deux acteurs absents de la fiche, qui renforcent C4=1
- **udata-hydra** (équipe data.gouv.fr / opendatateam) : crawler de métadonnées
  **officiel** de data.gouv.fr qui surveille en continu disponibilité, fraîcheur,
  type de fichier et **analyse le contenu CSV** (csv-detective), convertit en tables
  PostgreSQL/Parquet/PMTiles — v2.7.0 du 2026-03-12 (https://github.com/datagouv/hydra ,
  https://github.com/datagouv/hydra/blob/main/CHANGELOG.md , consultés 2026-06-23).
  L'État **internalise déjà** une bonne part de la surveillance technique de
  publication — angle mort partagé avec l'idée **0002**.
- **Éclaireur Public** (Anticor + Data for Good, lancé **19 février 2025**) :
  plateforme citoyenne qui **mesure la conformité de publication** des collectivités
  sur **deux familles de données obligatoires** (subventions SCDL + marchés DECP),
  avec un **indice A–E par collectivité** et **comparaison** entre territoires,
  exclusivement à partir de data.gouv.fr (https://eclaireurpublic.fr/methodologie ,
  https://www.lettreducadre.fr/article/avec-eclaireur-public-anticor-et-data-for-good-scrutent-les-budgets-locaux.55401 ,
  consultés 2026-06-23). Constat publié : **99,5 %** des communes assujetties n'ont
  publié **aucune** donnée de subventions 2024 ; 30,2 % ne publient pas les marchés.
  → C'est précisément un **scoring de conformité de publication par collectivité**,
  gratuit et grand public, sur le périmètre le plus sensible. Recoupe directement
  le seed.

→ Conclusion : non seulement l'Observatoire ODF couvre le macro, mais des outils
**par collectivité** (Éclaireur Public) et **techniques officiels** (udata-hydra)
existent déjà. C4=1 incontestable ; l'espace tiers est nul.

### Risque non chiffré
- **Cannibalisation interne 0002/0023** : les deux idées tournent sur la même API
  catalogue. Bien noté §5/§8 — à trancher (un seul « produit producteur data », mais
  marché déjà couvert).

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | **3** | 9 |
| C2 | Cible solvable | ×3 | 2 | 2 | 6 |
| C3 | Données | ×3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 1 | 1 | 2 |
| C5 | Différenciation | ×2 | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité | ×2 | 2 | 2 | 4 |
| C7 | Facilité du MVP | ×2 | 2 | 2 | 4 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **49** | | **46 / 105** |

**Score /100** : 46 / 105 × 100 = **43,8 → 44 / 100**.

**Changement de verdict : NON** (score abaissé). Fiche 47 → revue 44 → seuil < 55 →
❌ Écartée dans les deux cas. Avec critère **éliminatoire** confirmé (dénominateur
réglementaire inexistant en open data → tout « % conformité » serait inventé).

---

## 6. Verdict de revue

### **À CORRIGER À LA MARGE** (verdict écartée confirmé et renforcé)

La fiche est honnête et déjà sévère. Le seul correctif est **C1 = 3** : une
obligation légale **sans sanction**, avec priorité élu en recul, ne constitue pas
une douleur « forte » au sens du barème. Avec l'ajout d'**Éclaireur Public**
(scoring de conformité par collectivité, déjà en ligne) et **udata-hydra**
(surveillance technique officielle), l'écartage est cimenté à 44/100. Le critère
éliminatoire (donnée normative absente) reste le motif premier, indépendamment du
score.

### 3 actions prioritaires
1. **Abaisser C1 à 3** (obligation sans levier = besoin tiède) → total 46/105 → 44/100.
2. **Ajouter Éclaireur Public et udata-hydra** au §4 (liens datés 2026-06-23) :
   le premier prouve qu'un scoring de conformité **par collectivité** existe déjà ;
   le second, que l'État internalise la surveillance technique.
3. **Ne pas prototyper** ; si réouverture, uniquement comme **contribution OSS** à
   l'écosystème ODF/Etalab, jamais comme SaaS autonome à « % conformité CRPA ».

---

REVUE 0023 | à corriger (marge) | score recalculé 44/100 (vs 47) | changement de décision: non (écartée renforcée)
