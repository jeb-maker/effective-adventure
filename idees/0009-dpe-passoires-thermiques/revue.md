# Revue critique (red team) — 0009 Ciblage rénovation énergétique (passoires thermiques)

- **Fiche auditée** : `idees/0009-dpe-passoires-thermiques/README.md`
- **Score affiché par la fiche** : 60 / 100 — Verdict affiché : 🔁 À retravailler
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : excellente fiche (donnée propre, §4 saturé bien
> sourcé, mur juridique correctement identifié), mais **C2 est trop généreux** :
> le payeur le plus naturel (artisan/prospection) est juridiquement percuté et
> doublé par du freemium et un service public gratuit (Go Rénove). Recalculée,
> l'idée tombe de 60 à **57/100** — toujours « à retravailler », mais **à un point
> de l'écart**, et l'audit confirme la saturation (kelvin° s'ajoute à
> ThermoData/ScanReno/MenuiserieAi/Thervy).

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « > 14 millions de DPE… ~678 000 appartements F/G en copropriété » | §3bis | La fiche **signale elle-même** que ce sont des chiffres rapportés par un réutilisateur, « à re-vérifier par requête directe ». Bon réflexe, mais à ne pas afficher comme acquis. | **À sourcer (requête SQL datée)** |
| A2 | « achat de leads ~25–90 € l'unité » | §2 Cible | Sourcé (Samy Lead) — recevable, mais fourchette à dater précisément. | **OK / à dater** |
| A3 | « ~850 000 logements F/G reclassés » (ré-étiquetage 2026) | §8 Risques | Ordre de grandeur cohérent (le web parle de ~700 000–850 000 selon source) mais **non sourcé dans la fiche**. | **À sourcer** |

**À mettre au crédit de la fiche** : §4 **exemplaire** (services publics +
commercial pléthorique + DIY, liens datés 2026-06-20), §8 **rigoureux** sur le
mur juridique (loi du 30 juin 2025), §3 honnête sur les limites (ré-étiquetage,
absence de propriétaire). C'est une des fiches les mieux documentées du dépôt.

---

## 2. Sur-optimisme : notes de scoring trop généreuses

### C2 — Cible solvable (qui paie) : **3 → 2** (poids ×3)
C'est le point d'attention du prompt et le vrai excès. La fiche elle-même décrit :
1. le payeur le plus naturel (artisan prospection) est **percuté par
   l'interdiction du démarchage** en rénovation énergétique (depuis le 1er juillet
   2025, opt-in généralisé au 11 août 2026, amendes jusqu'à 375 000 €, fin de
   Bloctel — confirmé 2026-06-23) ;
2. le segment collectivités/bailleurs a une alternative **publique gratuite**
   (Go Rénove PRO) ;
3. les artisans ont déjà du **freemium** (ScanReno 5 leads/mois gratuits).
Quand le payeur principal est légalement contraint **et** doublé par le gratuit,
la note 3 (« payeurs existent ») est optimiste. Le budget existe mais la **voie
légale et solvable se rétrécit** → note 2.

### Notes confirmées (défendables)
- **C1 = 4**, **C3 = 4** : justes (douleur réelle ; donnée ouverte propre avec
  réserves). OK.
- **C4 = 1**, **C5 = 1** : **planchers pleinement justifiés** — on ne peut pas
  être plus dur, et l'audit n'a fait qu'ajouter des concurrents (kelvin°).
- **C6 = 5**, **C7 = 5** : **défendables mais à double tranchant** — la facilité
  technique et la donnée prête sont précisément ce qui **nourrit la saturation**.
  La fiche le dit. On les laisse à 5 (le critère mesure la faisabilité, pas la
  désirabilité), mais ils gonflent mécaniquement un score que C4/C5/C8 condamnent.
- **C8 = 1**, **C9 = 2** : justes (risque juridique quasi éliminatoire sur l'usage
  phare ; monétisation cannibalisée).

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- **Architecture conforme et exemplaire** : DPE tabulaire → DuckDB/SQL, chiffres
  tracés jusqu'au DPE source + date, LLM cantonné au sens (libellés, gestes,
  aides). Risque d'hallucination faible par construction. C6 = 5 mérité.
- **Réserve métier bien identifiée par la fiche** : le ré-étiquetage 2026
  (coef. électricité 2,3 → 1,9) rend toute liste « passoires » **volatile** ; à
  afficher honnêtement. C'est un risque de **donnée**, pas de modèle.
- Aucun chiffre halluciné. La seule prudence : ne pas afficher les volumes « 14 M
  DPE » sans requête directe (cf. A1).

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire non mentionnés)

### Concurrents — saturation encore confirmée (consultés 2026-06-23)

- **Public** (déjà cités, OK) : **Go Rénove** (CSTB/BDNB : recherche adresse,
  analyse territoriale collectivités, analyse de parc bailleurs, offre PRO),
  **Observatoire DPE-Audit ADEME**, **France Rénov'** (accompagnement
  particuliers), **BDNB open data**.
- **Commercial — la liste s'allonge** :
  - **ThermoData** (https://thermodata.fr/) : plans porte-à-porte F/G, score
    0–100, tournée GPS, « 30 s » ;
  - **ScanReno** (https://www.scanreno.fr/) : SaaS DPE, carte prospection,
    **freemium 5 leads/mois**, calcul 3CL + aides 2026 ;
  - **MenuiserieAi** (https://menuiserieai.fr/prospection-dpe) : carte F/G,
    estimation MaPrimeRénov'/CEE, export CSV ;
  - **Thervy** (https://www.thervy.com/) : croise 6 bases publiques, scoring,
    fiche bien 360 ;
  - **kelvin°** (https://www.go-kelvin.com/trouver-chantiers-prospection-terrain)
    — **nouvel entrant non cité** : ciblage terrain par adresse (DPE estimé,
    chauffage, surface, année), plateforme commerciale rénovation (qualification,
    simulation aides, rapport PDF). Renforce C4/C5 au plancher.
  - **Achat de leads** (Samy Lead, etc.) : 25–90 €/lead.
- **DIY / tutoriels** : articles « cibler les F/G gratuitement avec ADEME +
  SIRENE + DVF » (webtensor.fr).

→ La fiche avait déjà conclu « SATURÉ » ; l'audit **confirme et ajoute kelvin°**.
Aucun créneau libre côté prospection ; le seul angle théorique (priorisation de
parc bailleurs/syndics) affronte Go Rénove gratuit.

### Réglementaire — confirmé et durci

- **Interdiction du démarchage en rénovation énergétique** : loi n° 2025-594 du
  30 juin 2025 ; interdiction sectorielle (tél., SMS, e-mail, réseaux sociaux)
  **depuis le 1er/2 juillet 2025** ; **opt-in généralisé tous secteurs au
  11 août 2026** ; **suppression de Bloctel** ; amendes jusqu'à **375 000 €**
  (personnes morales) et nullité des contrats (sources consultées 2026-06-23 :
  https://www.service-public.gouv.fr/particuliers/actualites/A18384 ,
  https://www.anil.org/adil-44/... , https://cms.law/fr/fra/news-information/...).
  → Le risque juridique de la fiche (§8) est **exact** et même renforcé.
- **RGPD / détournement de finalité** des DPE pour la prospection : confirmé
  comme sujet sensible.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 4 | 12 |
| C2 | Cible solvable (qui paie) | ×3 | 3 | **2** | 6 |
| C3 | Disponibilité & fiabilité données | ×3 | 4 | 4 | 12 |
| C4 | Espace concurrentiel libre | ×2 | 1 | 1 | 2 |
| C5 | Différenciation défendable | ×2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | ×2 | 5 | 5 | 10 |
| C7 | Facilité du MVP | ×2 | 5 | 5 | 10 |
| C8 | Maîtrise des risques | ×2 | 1 | 1 | 2 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **63** | | **60 / 105** |

**Score /100** : 60 / 105 × 100 = **57 / 100**.

**Changement de décision : NON (mais fragilisé).**
- Fiche : 60/100 → bande 55–69 → 🔁 À retravailler.
- Revue : 57/100 → bande 55–69 → 🔁 **À retravailler**, mais **à 2 points de
  l'écart**. Le statut tient grâce à C6/C7 = 5 (facilité technique) ; si le pivot
  « bailleurs/syndics » ne trouve pas de payeur prêt à payer **malgré** Go Rénove
  gratuit, l'idée bascule en ❌ Écartée — comme la fiche le prévoit déjà.

---

## 6. Verdict de revue

### **À CORRIGER** → décision : 🔁 À retravailler (confirmée, mais affaiblie)

La fiche est **rigoureuse et lucide** : elle reconnaît saturation et mur
juridique. Le seul excès est **C2 (3 → 2)** : le payeur principal est légalement
contraint et doublé par le gratuit/freemium, ce qui abaisse le score de 60 à 57.
On reste dans la bande « à retravailler », mais le verdict est désormais **au bord
du seuil** : la note tient uniquement grâce à la facilité technique (C6/C7 = 5),
qui est aussi la cause de la saturation. Sans payeur B2B prouvé sur le pivot
légal, l'écart est la suite logique.

### 3 actions prioritaires
1. **Acter C2 = 2** (score 57) et faire de la validation d'un **payeur légal**
   (bailleur social / syndic prêt à payer malgré Go Rénove) le **go/no-go** : pas
   d'entretiens concluants → ❌ Écartée.
2. **Compléter le §4** avec kelvin° (lien daté) et sourcer les volumes (« 14 M
   DPE », « 850 000 reclassés ») par requête SQL directe (A1/A3).
3. **Cadrer l'usage strictement légal** (pas de prospection démarchage ; boîtage
   anonyme / priorisation de parc) et le **différencier méthodologiquement** de
   Go Rénove — sinon l'idée n'a ni payeur défendable ni moat.

---

REVUE 0009 | à corriger | score recalculé 57/100 (vs 60) | changement de décision: non (🔁 maintenue, au bord de l'écart)
