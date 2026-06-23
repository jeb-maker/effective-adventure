# Revue critique (red team) — 0029 RecordAI (email/PDF → dossier structuré validé)

- **Fiche auditée** : `idees/0029-recordai/README.md`
- **Score affiché par la fiche** : 67 / 100 — Verdict affiché : 🔁 À retravailler (présenté comme « meilleur candidat », +1 pt de validation prospect suffirait pour franchir le Go)
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche construit son passage de 66 à 67 (et son
> « +1 pt = Go ») sur un **benchmark §13 truqué par sélection** : elle ne compare
> RecordAI qu'à un triptyque KYC (Ubble / Inscribe / Klippa) choisi pour avoir
> chacun un « trou » commode, tout en **ignorant les concurrents qui occupent
> précisément le créneau revendiqué** — au premier rang desquels **CheckFile.ai**
> (FR/EU, DORA, KYC/AML, audit trail 5 ans, pricing self-service ~0,30 €/doc),
> que la fiche **cite trois fois comme *source* sans voir que c'est le produit
> RecordAI déjà construit**. Avec Rossum (inbox email native + HITL) et Parseur
> (email→JSON + validation, 39 $/mois), les trois différenciateurs revendiqués
> (C4=3, C5=4) ne tiennent pas. Réponse directe à la question posée : **non, C4=3
> et C5=4 ne sont pas justifiés.**

---

## 1. Affirmations non sourcées / contredites (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « aucun concurrent direct ne couvre le flux *email entrant → dossier KYC structuré → validation humaine → audit trail DORA* sur le segment SMB fintech FR/EU » | §11 / §13 Verdict | **Faux par omission.** Vrai uniquement sur le triptyque cherry-pické. **CheckFile.ai** (FR/DE, DORA, KYC/AML, audit trail horodaté 5 ans, self-service ~0,30 €/doc) couvre quasi tout ce flux et est déjà en prod (180 000+ docs/mois). | **À supprimer / corriger** |
| A2 | « aucun des 3 concurrents ne propose de pipeline natif *email entrant IMAP → dossier structuré* » | §13 Dim. 1 | Vrai sur les 3 *choisis*, mais **Rossum** (cité en §4 !) a une **inbox email native par file** (adresse dédiée, filtres expéditeur, rejet, HITL par défaut) ; **Parseur** est *email-first* (forward vers mailbox unique → extraction → JSON). Le « natif email » n'est pas un différenciateur. | **À corriger** |
| A3 | « Pricing transparent self-serve — inaccessible aujourd'hui via les offres enterprise existantes » | §13 Dim. 3 | **Faux.** CheckFile.ai publie un pricing par paliers (~0,30 €/doc, Starter 100 docs/mois, Business 500 + API/webhooks) ; Parseur affiche 39 $/100 pages, free tier 20 pages. Le self-serve transparent existe déjà sur le créneau. | **À supprimer** |
| A4 | « DORA art. 9-10 + AMLD6 + hébergement EU = différenciation plus durable » (justif. C5=4) | §10 / §12 | L'« ancre réglementaire » n'est pas un moat : c'est devenu **un argument marketing standard du secteur**. CheckFile.ai, VerifyPDF, et la littérature DORA 2026 vendent tous « audit trail horodaté déterministe + rétention 5 ans + hébergement EU ». Table stakes, pas avantage durable. | **À nuancer / corriger** |
| A5 | « `inscribe` = seul acteur proche » (justif. C4=3, répété 3×) | §10 / §12 / §13 | Réducteur : Inscribe fait déjà KYC/KYB onboarding (IDs, justif. domicile, registres) + audit trail horodaté + GDPR retention + routing reviewer depuis 2017. Et ce n'est pas le « seul » : CheckFile.ai, Klippa/Doxis, Rossum sont aussi proches selon l'axe retenu. | **À corriger** |
| A6 | « Aligné sur la tendance 2026 : hybride siège + usage + outcome partiel » | §7 | Plausible mais asséné sans source sur la part de marché payante de ce modèle pour ce cas d'usage. | **À sourcer** |

**À mettre au crédit de la fiche** : le sourcing *unitaire* est honnête et daté
(liens 2026-06-23 vers rossum, parseur, inscribe, klippa, checkfile, prnewswire
Shift Claims, limnos, orderscan…). Le problème n'est **pas** l'absence de liens —
c'est la **construction du périmètre de comparaison** : la fiche source
abondamment, mais choisit ses concurrents pour que la conclusion « espace libre »
tienne. C'est le même biais que 0001 (échantillon de concurrents tronqué), en
plus sophistiqué.

---

## 2. Sur-optimisme : notes de scoring trop généreuses

> Rappel : la fiche est partie de C4=2 / C5=3 (segments génériques), puis les a
> **relevées** à **C4=3 / C5=4** en §12/§13 sur la base du seul vertical KYC lite
> + du benchmark triptyque. C'est précisément ce relèvement qui amène le total à
> 70/105 → 67/100 et la phrase « +1 pt = Go ». Ce relèvement est infondé.

### C4 — Espace concurrentiel libre : **3 → 2** (poids ×2)
Le créneau ciblé (« KYC/AML lite, email/PDF → dossier validé + audit trail DORA,
SMB fintech FR/EU ») **n'est pas libre, il est en cours de remplissage actif** :
- **CheckFile.ai** (consulté 2026-06-23) : « AI document validation | Compliance &
  KYC », serveurs **France + Allemagne**, GDPR natif, blog **DORA 2026** dédié,
  guide **KYC France** (ACPR/Tracfin), audit trail (horodatage, score, motifs de
  rejet, **archivage 5 ans AMLD6**), pricing self-service **~0,30 €/doc**, 6 000
  types de pièces / 200 pays, **180 000+ docs/mois** en prod, déployable 1–3 sem.
  → c'est **le produit décrit par RecordAI**, déjà vivant, FR/EU, SMB-accessible.
- **Rossum** : inbox email native, HITL par défaut, LLM « without hallucinations »,
  webhooks de validation métier — la plomberie « email → extraction → revue ».
- **Parseur** : email-first, schéma/validation par mailbox, webhooks, 39 $/mois.
- **VerifyPDF**, **CheckFile**, **fluxforce** : positionnement DORA explicite.

La fiche elle-même cite Rossum, Parseur, Inscribe en §4 ; le §13 les remplace par
un triptyque plus commode. Espace **occupé / en consolidation** = note 2, pas 3.
(Un argumentaire pour 1 est même soutenable vu CheckFile.ai ; je retiens 2.)

### C5 — Différenciation défendable : **4 → 2** (poids ×2)
Les **quatre** différenciateurs revendiqués (§5/§12) existent déjà ailleurs :
1. « email entrant IMAP = déclencheur natif » → **Rossum** (inbox par file) +
   **Parseur** (mailbox forward) le font déjà.
2. « audit trail DORA/AMLD6 natif » → **CheckFile.ai** (horodatage, motifs,
   rétention 5 ans), **Inscribe** (revision history, timestamps, GDPR retention).
3. « hébergement EU / RGPD » → **CheckFile.ai** (FR+DE), **Klippa/Doxis** (EU-hosted).
4. « pricing transparent self-serve SMB » → **CheckFile.ai** (paliers, ~0,30 €/doc),
   **Parseur** (39 $/mois, free tier).

Aucun des quatre n'est défendable isolément, et **leur *union* est déjà réalisée
par CheckFile.ai**. La justification « ancre réglementaire = durable » confond
*conformité* (que tout le monde affiche) et *moat* (qu'aucune donnée n'apporte
ici, puisqu'il n'y a pas de dataset propriétaire — §3 le dit). Différenciation
« copiable » **et déjà copiée**. Note 2.

### C9 — Monétisation / impact : **4 → 3** (poids ×2)
Conséquence directe de C4/C5 : si CheckFile.ai vend déjà l'audit trail DORA en
self-service à ~0,30 €/doc, le « pricing transparent » de RecordAI n'est pas un
levier de marge — c'est s'aligner sur un prix de marché **déjà cassé** par un
concurrent FR/EU. Pression de commoditisation immédiate. Note 3.

### Notes laissées inchangées (défendables)
- **C1 = 4** (×3) : la douleur (ressaisie manuelle de docs entrants) est réelle et
  récurrente. OK.
- **C2 = 3** (×3) : payeur réglementaire non-discrétionnaire (fintech/EMI sous
  DORA) crédible — et **l'existence même de CheckFile.ai (180 k docs/mois payants)
  confirme la solvabilité**. Ironie : la meilleure preuve du payeur est aussi la
  preuve du concurrent. 3, pas plus (budget capté par l'incumbent).
- **C3 = 3** (×3) : pas d'avantage open-data (documents = source). OK.
- **C6 = 4** (×2) : pipeline email→JSON avec champs ancrés source, RAG(sens)/SQL
  ou extraction tracée — conforme §3 de la méthode. OK (voir §3 ci-dessous).
- **C7 = 3** (×2) : 1 micro-process KYC lite faisable ; choix du vertical reste
  bloquant. OK.
- **C8 = 2** (×2) : la fiche notait déjà bas (« IDP montent en gamme ») — confirmé,
  et même sous-estimé (les concurrents y sont *déjà*, pas « montent »). Reste 2.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- **Architecture conforme** : la fiche cantonne le LLM à la classification / aux
  libellés, ancre chaque champ extrait à sa source (bbox/page), et impose une
  validation humaine sur les champs critiques. C'est le bon design, et c'est un
  vrai point fort (C6=4 mérité). À conserver.
- **Réserve** : le risque produit n'est pas l'hallucination LLM (bien maîtrisée),
  c'est la **fiabilité de l'extraction sur scans dégradés** et la **détection de
  fraude documentaire** — terrain où les concurrents (Inscribe « Trust Score »
  0-100, CheckFile « 99 % détection fraude », Rossum « Aurora ») ont **des années
  d'avance et des certifs (SOC 2 Type II, ISO 27001)** que RecordAI n'a pas. La
  fiche ne chiffre aucune cible de précision ni de taux de fraude détectée : sur
  un vertical KYC/AML, c'est l'angle mort technique central.
- Aucun chiffre non traçable affiché dans la fiche elle-même (les chiffres cités
  sont des chiffres concurrents, correctement attribués). OK sur ce point.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire)

### Concurrents directs OMIS du benchmark §13 (le plus grave)
Tous consultés le 2026-06-23 :

- **CheckFile.ai** — https://www.checkfile.ai/en-GB et
  https://www.checkfile.ai/fr-CH/blog/dora-2026-verification-documentaire-secteur-financier
  et https://www.checkfile.ai/en-AU/guides/kyc-france : **le concurrent quasi
  identique**. AI document validation KYC/AML, **serveurs FR+DE**, DORA/AMLD6,
  audit trail horodaté + archivage 5 ans, cross-validation multi-docs, pricing
  self-service **~0,30 €/doc** (Starter/Business/Enterprise, API+webhooks),
  banques + cabinets d'avocats, 180 000+ docs/mois. **Cité 3× par la fiche comme
  *source* (preuve que « DORA crée la demande ») mais jamais identifié comme
  concurrent.** C'est l'erreur logique-clé : citer son clone comme étude de marché.
- **Rossum** — https://rossum.ai/platform/receive-documents/ et
  https://knowledge-base.rossum.ai/docs/email-inbox-in-rossum : inbox email
  native par file (adresse dédiée, allow/deny senders, rejet auto + notification),
  HITL par défaut (« brings in humans when it lacks confidence »), LLM propriétaire
  « without hallucinations », webhooks de validation. **Cité en §4 mais écarté du
  §13** alors qu'il détruit l'argument « email natif » et « HITL ».
- **Parseur** — https://parseur.com/features et https://parseur.com/pricing :
  email-first, schémas + **validation par mailbox**, post-processing Python,
  webhooks/JSON, **39 $/mois** (free tier 20 pages). Commoditise le flux générique.
- **VerifyPDF** — https://verifypdf.com/dora-compliance-document-verification-financial-services/
  : vérification documentaire positionnée **DORA**, audit trail par défaut.

→ Conclusion : comme pour 0001, la fiche n'a pas « raté un » concurrent, elle a
**construit un périmètre de comparaison qui exclut les plus dangereux**. Le bon
réflexe (citer ses sources) masque un mauvais raisonnement (choisir 3 concurrents
à trou pour conclure « libre »).

### Risques non mentionnés
- **Commoditisation immédiate du pricing** : CheckFile.ai a déjà fixé un prix de
  marché self-service (~0,30 €/doc) sur le créneau exact. RecordAI arrive *après*.
- **Barrière confiance/certifs** : sur KYC/AML, l'achat se fait sur SOC 2 / ISO
  27001 / taux de détection de fraude prouvé. RecordAI part de zéro face à des
  incumbents certifiés (Inscribe, CheckFile).
- **« Audit trail DORA » n'est pas un produit, c'est une case** : un acheteur
  fintech veut un fournisseur *résilient et audité lui-même* (DORA tiers) — exige
  due diligence fournisseur, ce qui **favorise les acteurs établis**, pas un MVP.
- **Choix du vertical = pari** : la fiche admet que le choix du micro-process est
  bloquant, puis verrouille KYC lite — précisément le vertical le plus réglementé
  et le plus concurrencé (cf. ci-dessus). Auto-contradiction stratégique.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 4 | 12 |
| C2 | Cible solvable (qui paie) | ×3 | 3 | 3 | 9 |
| C3 | Disponibilité & fiabilité données | ×3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 3 | **2** | 4 |
| C5 | Différenciation défendable | ×2 | 4 | **2** | 4 |
| C6 | Faisabilité & fiabilité technique | ×2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | ×2 | 3 | 3 | 6 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 4 | **3** | 6 |
| | **Total** | | **70** | | **62 / 105** |

**Score /100** : 62 / 105 × 100 = 59,0 → **59 / 100**.

**Changement de verdict : NON sur le statut, OUI sur la trajectoire.**
- Fiche : 67/100 → 🔁 « à retravailler », présenté comme « +1 pt = Go ».
- Revue : 59/100 → toujours 🔁 « à retravailler », mais **le Go n'est plus à 1 pt :
  il est à 11 pts**, et il dépend de la *destruction* d'un concurrent FR/EU déjà
  installé. La narration « meilleur candidat, presque Go » est **infirmée**.

---

## 6. Verdict de revue

### **À CORRIGER** (le §12/§13 est à refaire)

La douleur (C1), le payeur réglementaire (C2) et l'architecture anti-hallucination
(C6) sont réels et bien traités. Mais le **cœur décisionnel de la fiche — le
re-scoring C4 2→3 et C5 3→4 en §12/§13 — repose sur un benchmark sélectif** qui
exclut les concurrents qui occupent le créneau (CheckFile.ai surtout, Rossum,
Parseur). Réponse à la question posée : **C4=3 et C5=4 ne sont pas justifiés ;
2 et 2 le sont.** RecordAI n'est pas « presque Go » : c'est une idée à 59 dont le
différenciateur revendiqué est **déjà entièrement livré par un concurrent FR/EU
self-service**.

### 3 actions prioritaires
1. **Refaire le §13 honnêtement** : intégrer CheckFile.ai (clone FR/EU le plus
   proche), Rossum (email natif + HITL), Parseur (self-serve email→JSON),
   VerifyPDF. Reconnaître que l'« espace libre » et le « pricing self-serve
   inédit » n'existent pas. Re-noter C4/C5 à 2.
2. **Cesser de citer CheckFile.ai comme preuve de demande** : c'est le concurrent.
   Si l'argument « DORA crée la demande » tient, il prouve surtout qu'un acteur
   FR/EU a déjà capté cette demande. Trouver un différenciateur **non couvert par
   CheckFile.ai** (sinon, pas de Go) — ex. un micro-process *hors KYC* moins
   réglementé/concurrencé, ou une intégration/distribution captive.
3. **Sur KYC/AML, chiffrer la barrière technique** : taux de détection de fraude
   cible, précision d'extraction sur scans dégradés, et plan de certification
   (SOC 2 / ISO 27001) — sans quoi un acheteur fintech ne substituera pas un
   incumbent certifié par un MVP.

---

REVUE 0029 | à corriger | score recalculé 59/100 (vs 67) | changement de décision: non (reste 🔁) mais « +1 pt = Go » infirmé | C4=3 et C5=4 NON justifiés (→ 2 et 2)
