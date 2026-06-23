# Revue critique (red team) — 0026 Exposition risques des parcelles agricoles (RPG × Géorisques × Hub'Eau)

- **Fiche auditée** : `idees/0026-exposition-parcelles-agricoles/README.md`
- **Score affiché par la fiche** : 56 / 100 — Verdict affiché : 🔁 À retravailler
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche s'auto-critique déjà sévèrement (payeur
> absent = « point éliminatoire potentiel », C2=2, C4=2, C5=2, C9=2) et le scoring
> est honnête. La revue **confirme** ces notes et les **renforce** avec deux
> éléments que la fiche n'avait pas pleinement exploités : (1) **MesParcelles**,
> l'outil des **Chambres d'agriculture** elles-mêmes (cible payante revendiquée),
> et (2) la confirmation que les **cartographies environnementales des DDT croisent
> déjà RPG × couches réglementaires**, gratuitement. Le score 56 est maintenu.

---

## 1. Affirmations non sourcées / à compléter

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « Il n'existe pas de produit SaaS national grand public couvrant l'ensemble […] avec une UX *fiche parcelle agricole* en libre-service » | §4 | Plausible et **honnêtement nuancé** par la fiche (« mais la demande solvable reste à démontrer »). Reste une affirmation d'absence : à confronter à l'évolution rapide des outils chambres/DDT. | **À surveiller** |
| A2 | Chambres d'agriculture listées comme **cible payante** | §2 | Angle mort : les chambres **éditent et distribuent déjà MesParcelles** (n°1 du marché, 20+ ans) — elles sont fournisseur d'outil, pas acheteur d'un SaaS tiers de cartographie. Affaiblit encore le payeur « chambre ». | **À corriger** |
| A3 | « Les DDT publient des cartographies gratuites par département » | §4 / §5 | Exact et **sous-exploité** : la carte environnementale DDTM (ex. DDTM76) est explicitement « couches réglementaires **croisées avec le RPG** » en cartographie interactive — c'est déjà le croisement RPG×risques de 0026, gratuit. | **À renforcer** |
| A4 | RPG « Métropole ; jointure PCI » comme limite | §3 | À actualiser : le **RPG millésime 2024** ajoute 4 couches (prairies permanentes, catégories, bio, ZDH) + SNA/IAE (règlement UE 2023/138 « données de forte valeur ») — la donnée publique s'enrichit, ce qui **réduit** l'avantage d'un agrégateur tiers. | **À intégrer** |

**À mettre au crédit de la fiche** : §4 déjà très complet (Géoportail, Géorisques,
DDT, GÉOPERSO, Géofoncier, **Terravisu/SeineYonne**, Geofolia, Farmstar — tous
datés juin 2026), §5 « défendabilité très faible » assumée, et §8 posant le payeur
absent en éliminatoire. C'est une fiche déjà red-teamée par son auteur ; la revue
ne fait que confirmer.

---

## 2. Sur-optimisme : notes de scoring

Aucune note n'est sur-optimiste — au contraire, la fiche est prudente. La revue
**confirme** l'ensemble et ne propose **aucun relèvement** :

- **C1 = 3** (×3) : douleur diffuse, contournée par les outils gratuits. Confirmé.
  (Un argument pour 2 existe, mais 3 reste défendable pour les coopératives/due
  diligence.)
- **C2 = 2** (×3) : payeur flou — et **renforcé à la baisse** : les chambres
  (cible) éditent déjà MesParcelles ; les coopératives commandent du sur-mesure
  (Terravisu) ; l'agriculteur ne paie pas pour de la donnée publique gratuite.
  Confirmé 2.
- **C3 = 4** (×3) : RPG (MàJ juin 2026, enrichi 2024), Géorisques, Hub'Eau (testé),
  GPU — ouverts et opérationnels. Confirmé 4.
- **C4 = 2** (×2) : GÉOPERSO, Géofoncier, Terravisu, **DDT (RPG×couches)**, +
  MesParcelles/Geofolia en adjacence. Confirmé 2.
- **C5 = 2** (×2) : données 100 % publiques, croisement reproductible. Confirmé 2.
- **C6 = 4** (×2) : PostGIS + SQL spatial traçable, LLM réglementaire. Confirmé 4.
- **C7 = 3** (×2) : MVP 2–3 sem. sur 1 département. Confirmé 3.
- **C8 = 3** (×2) : risque principal non technique (payeur) bien identifié. Confirmé 3.
- **C9 = 2** (×2) : ni revenu clair ni impact autonome. Confirmé 2.

→ Recalcul identique à la fiche : **56/100**.

---

## 3. Risque d'hallucination / RAG(sens) / SQL(chiffres)

- **Conforme** : surfaces, nb ICPE, distances (ST_DWithin) = SQL/spatial traçable ;
  LLM cantonné à l'explication réglementaire (ICPE, PLU). Bon design (C6=4).
- **Réserve** : la qualité de la **jointure RPG ↔ PCI cadastrale** est le vrai
  risque de fiabilité (la fiche le note) ; un « SQL traçable » sur une jointure
  spatiale approximative peut produire des fiches parcelle exactes-mais-fausses.

---

## 4. Angles morts (concurrents, coûts, réglementaire)

Tous consultés le 2026-06-23 :
- **MesParcelles (Chambres d'agriculture France)** —
  https://chambres-agriculture.fr/etre-accompagne/nos-solutions-numeriques/mesparcelles
  : plateforme n°1, 20+ ans, gestion parcellaire cartographiée, traçabilité
  réglementaire, indicateurs environnementaux, prép. PAC. **La cible « chambre »
  est donc un éditeur d'outil, pas un acheteur** — angle mort majeur de §2.
- **DDTM — carte environnementale agricole** (ex. DDTM76) —
  https://www.seine-maritime.gouv.fr/.../Actualisation-de-la-cartographie-environnementale-agricole
  : cartographie interactive « couches réglementaires **croisées avec le RPG** »,
  gratuite. C'est le croisement de 0026, déjà public (par département).
- **Geofolia (Isagri)** — https://www.isagri.fr/geofolia/logiciel-de-gestion-parcellaire
  : gestion parcellaire + alertes réglementaires (ZNT, IFT, PAC), 8 ans
  d'historique. Adjacent mais capte le budget logiciel agricole.
- **RPG 2024 enrichi** — https://agriculture.gouv.fr/les-nouvelles-donnees-2024-du-registre-parcellaire-graphique-rpg-sont-disponibles
  : 4 nouvelles couches + SNA/IAE (UE 2023/138) → la donnée publique se rapproche
  seule du produit, réduisant la valeur d'un agrégateur.

### Risques non mentionnés (au-delà du payeur déjà identifié)
- **La cible publique s'auto-équipe** : chambres (MesParcelles) et DDT (cartes
  RPG×risques) produisent déjà l'outil → marché des chambres ≈ fermé.
- **Enrichissement continu de la donnée publique** (RPG 2024, GPU) → fenêtre de
  différenciation qui se referme sans intervention de l'idée.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | ×3 | 2 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | ×3 | 4 | 4 | 12 |
| C4 | Espace concurrentiel libre | ×2 | 2 | 2 | 4 |
| C5 | Différenciation défendable | ×2 | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | ×2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | ×2 | 3 | 3 | 6 |
| C8 | Maîtrise des risques | ×2 | 3 | 3 | 6 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **59** | | **59 / 105** |

**Score /100** : 59 / 105 × 100 = 56,2 → **56 / 100** (inchangé).

**Changement de verdict : NON.** La fiche est déjà correctement notée et reste 🔁
à retravailler. La revue confirme le score et **durcit le diagnostic** : la cible
« chambres d'agriculture » est un faux payeur (elle édite déjà MesParcelles), ce
qui rapproche l'idée de l'écartement si aucune willingness-to-pay n'émerge des
entretiens.

---

## 6. Verdict de revue

### **ANALYSE FIABLE** (score confirmé, diagnostic durci)

Rare cas où la fiche s'est déjà auto-red-teamée correctement : scoring honnête,
sources datées, payeur posé en éliminatoire. La revue ne change pas le score (56)
mais **invalide un payeur supplémentaire** (les chambres éditent MesParcelles) et
**confirme que le croisement RPG×risques existe déjà gratuitement** (DDT). Le
verdict « valider la willingness-to-pay avant tout dev, sinon écarter » est le bon.

### 3 actions prioritaires
1. **Retirer les chambres d'agriculture de la liste des payeurs** (ce sont des
   éditeurs/distributeurs d'outils — MesParcelles) ; recentrer sur cabinets conseil
   foncier / coopératives, et **prouver** la willingness-to-pay par entretiens.
2. **Comparer frontalement à la carte environnementale DDT** (gratuite, RPG×couches)
   et à GÉOPERSO : qu'apporte 0026 qu'ils ne font pas déjà ? Si rien de payant → écarter.
3. **Acter l'enrichissement RPG 2024 / GPU** : la donnée publique comble seule une
   partie du gap → la fenêtre se referme, ne pas investir sans payeur confirmé.

---

REVUE 0026 | analyse fiable | score confirmé 56/100 (inchangé) | changement de décision: non (reste 🔁) | payeur « chambres » invalidé (éditent MesParcelles) ; croisement RPG×risques déjà gratuit (DDT)
