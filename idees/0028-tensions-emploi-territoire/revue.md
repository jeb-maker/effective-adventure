# Revue critique (red team) — 0028 Tensions emploi par territoire (France Travail × SIRENE × FiLoSoFi)

- **Fiche auditée** : `idees/0028-tensions-emploi-territoire/README.md`
- **Score affiché par la fiche** : 58 / 100 — Verdict affiché : 🔁 À retravailler
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche est déjà lucide (Data Emploi cité comme
> couvrant « 80 % du besoin »), mais elle **sous-estime** encore l'existant : Data
> Emploi descend jusqu'à la **commune** (et pas seulement le bassin), la
> nomenclature **FAP** réconcilie déjà ROME↔PCS (la « heuristique ROME/NAF » est
> en partie un problème résolu côté public), et **BMO** donne les intentions de
> recrutement par bassin gratuitement. Le seul actif différenciant — le « score
> composite franchise » — repose donc sur **trois couches gratuites**, dont la
> couche emploi est plus complète que la fiche ne l'admet. C5 doit baisser.

---

## 1. Affirmations non sourcées / à corriger

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « France Travail / Mes Services Locaux : consultation publique partielle (bassin emploi uniquement, **pas commune**) » | §4 | **Inexact.** Data Emploi sélectionne région / département / bassin / **EPCI** / **commune** ; France Travail publie aussi « l'état de l'emploi dans votre ville » (communes > 5 000 hab). La granularité commune existe déjà, gratuitement. | **À corriger** |
| A2 | « Mapping métier ROME ↔ NAF = heuristique » présenté comme verrou différenciant | §3 / §6 / §8 | À nuancer : la **nomenclature FAP** (Familles Professionnelles, INSEE/DARES) réconcilie déjà PCS (INSEE) et ROME (France Travail) ; BMO l'utilise sur 217 métiers. Le pont métier↔emploi est en partie outillé publiquement. | **À nuancer** |
| A3 | « La différenciation = la synthèse des trois couches dans un seul score […] n'existe pas en self-service » | §5 | Affirmation centrale, mais la valeur revendiquée se réduit à un **agrégat pondéré de données gratuites**, que la fiche reconnaît elle-même « imitable par Smappen en quelques semaines ». Non sourcé qu'un acheteur paierait *pour le score* plutôt que pour les couches déjà servies. | **À nuancer / sourcer** |
| A4 | « Smappen … 3 M€ ARR, 1 230 clients dont 470 franchises » | §4 | Bien sourcé (Le Journal des Entreprises, 2026) — **à mettre au crédit**. Mais cela prouve le marché *géomarketing*, pas le besoin payant pour la *couche emploi*. | **OK (mais à recontextualiser)** |

**À mettre au crédit de la fiche** : §4 exemplaire (Data Emploi, Smappen,
hr-talent-ai, CCI tous datés 2026-06-23), millésime FiLoSoFi 2021 honnêtement
signalé comme « 5 ans de retard », et verdict déjà prudent (produit = module, pas
standalone). C'est une fiche bien faite ; la revue resserre, elle ne démolit pas.

---

## 2. Sur-optimisme : notes de scoring

### C5 — Différenciation défendable : **3 → 2** (poids ×2)
Le seul différenciateur est le score composite. Or :
1. La couche emploi (la plus « différenciante » revendiquée) est **déjà publique
   et plus granulaire que la fiche ne l'admet** : Data Emploi va jusqu'à la
   commune/EPCI, BMO donne les intentions par bassin, FAP outille le mapping.
2. Les deux autres couches (SIRENE, FiLoSoFi) sont servies par **Smappen** pour
   les franchiseurs.
3. La fiche admet « imitable par Smappen en quelques semaines (intégration API FT
   simple) ».
Un agrégat de trois sources gratuites, copiable en semaines par l'acteur qui tient
déjà le canal (Smappen) = note 2, pas 3.

### Notes laissées inchangées (défendables)
- **C1 = 3** (×3) : besoin réel mais le segment « emploi » est un *module*, pas le
  cœur de douleur. OK.
- **C2 = 3** (×3) : franchiseurs solvables (Smappen le prouve), mais ils ne
  paieront pas pour ce standalone — d'où le verdict « module/partenariat ». 3 est
  la note plafond défendable (un argument pour 2 existe, vu l'absence de payeur
  *standalone* ; je laisse 3 car la solvabilité du segment est réelle).
- **C3 = 3** (×3) : APIs FT (OAuth = barrière), FiLoSoFi 2021 (obsolète), mapping
  ROME/NAF partiellement outillé par FAP. 3 OK.
- **C4 = 2** (×2) : Data Emploi (gratuit, jusqu'à la commune) + Smappen + BMO
  saturent les couches séparément. Confirmé 2 (un argument pour 1 est soutenable).
- **C6 = 3** (×2) : SQL strict, mais dépendance OAuth FT + heuristique mapping. OK.
- **C7 = 3** (×2) : 6–8 sem., bloqueur OAuth FT. OK.
- **C8 = 3** (×2) : pas d'éliminatoire isolé, cumul de risques marché. OK.
- **C9 = 3** (×2) : revenu réel possible mais via module/partenariat. OK.

---

## 3. Risque d'hallucination / RAG(sens) / SQL(chiffres)

- **Conforme** : score composite = SQL pondéré traçable (source API + date) ;
  description métier = RAG. Bon design. La fiche impose même d'afficher le
  millésime FiLoSoFi et le taux de correspondance ROME/NAF. Rien à redire (C6=3).
- **Réserve métier** : un « score territoire » composite pondéré
  (0,4 / 0,3 / 0,3) est *traçable* mais **arbitraire** ; sans validation terrain
  des pondérations, il est exact-mais-subjectif. À documenter comme tel.

---

## 4. Angles morts (concurrents, coûts, réglementaire)

Tous consultés le 2026-06-23 :
- **Data Emploi (France Travail)** — https://dataemploi.francetravail.fr/emploi/accueil
  et https://dataemploi.francetravail.fr/emploi/panorama/NAT/FR : gratuit, sélection
  région/département/**bassin/EPCI/commune**, tensions par métier (5 tranches),
  demandeurs, offres, secteurs qui recrutent, métiers recherchés, comparaison
  entre territoires. **Plus complet que ce que §4 affirme** (la commune existe).
- **BMO (Besoins en Main-d'Œuvre)** — https://www.francetravail.org/opendata/enquete-besoins-en-main-doeuvre.html
  et https://statistiques.francetravail.org/bmo/static/methode_2026 : intentions
  de recrutement + difficultés, par bassin, 217 métiers FAP, gratuit, MàJ avril
  2026. Couvre la dimension « trouverai-je des candidats » que 0028 met en avant.
- **FAP (Familles Professionnelles)** : nomenclature qui réconcilie PCS (INSEE) et
  ROME (France Travail) — relativise le verrou « mapping ROME/NAF heuristique ».
- **Smappen** — https://smappen.fr/ : géomarketing franchises (déjà couvert §4).

### Risques non mentionnés
- **L'argument différenciant rétrécit** : si Data Emploi couvre la commune et BMO
  les intentions, la « couche emploi » de 0028 n'apporte qu'un *repackaging* ; le
  seul ajout est la *fusion en un score* — l'élément le plus copiable.
- **Dépendance OAuth France Travail** (déjà notée) : délai administratif + quotas +
  risque de conditions d'usage commercial.
- **Donnée propriétaire absente** : aucun actif défendable hors distribution
  (partenariat Smappen) — exactement le risque structurel récurrent du registre.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | ×3 | 3 | 3 | 9 |
| C3 | Disponibilité & fiabilité données | ×3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 2 | 2 | 4 |
| C5 | Différenciation défendable | ×2 | 3 | **2** | 4 |
| C6 | Faisabilité & fiabilité technique | ×2 | 3 | 3 | 6 |
| C7 | Facilité du MVP | ×2 | 3 | 3 | 6 |
| C8 | Maîtrise des risques | ×2 | 3 | 3 | 6 |
| C9 | Monétisation / impact | ×2 | 3 | 3 | 6 |
| | **Total** | | **61** | | **59 / 105** |

**Score /100** : 59 / 105 × 100 = 56,2 → **56 / 100**.

**Changement de verdict : NON** (reste 🔁 à retravailler, zone 55–69) — mais
l'idée se rapproche du seuil d'écartement (55). La condition de déblocage est plus
exigeante qu'affichée : sans **partenariat Smappen** (distribution), la couche
emploi seule ne justifie aucun produit autonome, car elle est déjà gratuite et
granulaire chez France Travail.

---

## 6. Verdict de revue

### **À CORRIGER** (resserrement, pas démolition)

La fiche est honnête et bien sourcée, mais elle survalorise encore le seul
différenciateur (score composite) en sous-estimant Data Emploi (granularité
commune) et la nomenclature FAP. Le produit autonome n'a pas de moat ; sa seule
voie crédible est **un module distribué par Smappen** (canal existant, 470
franchises). Sans ce canal, l'idée est sous le seuil.

### 3 actions prioritaires
1. **Corriger §4** : Data Emploi couvre la commune/EPCI ; BMO couvre les intentions ;
   FAP outille le mapping. Re-noter C5 à 2.
2. **Tester le partenariat Smappen en premier** (avant tout dev) : c'est la seule
   hypothèse qui transforme un repackaging en produit distribuable.
3. **Si pas de canal**, écarter — un agrégat de trois sources gratuites copiable
   en semaines n'est pas défendable en standalone.

---

REVUE 0028 | à corriger | score recalculé 56/100 (vs 58) | changement de décision: non (reste 🔁, proche du seuil 55) | différenciateur (score composite) sur-noté : couche emploi déjà gratuite et granulaire (Data Emploi commune, BMO, FAP)
