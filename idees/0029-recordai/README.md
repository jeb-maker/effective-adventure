# RecordAI — email/PDF → dossier structuré validé

- **ID** : 0029
- **Statut** : 🔁 À retravailler
- **Score** : 59 / 100
- **Dernière mise à jour** : 2026-06-23
- **Révision critique** : voir [`revue.md`](revue.md) — score abaissé de **67 à 59**
  après audit adversarial. Le re-scoring §12/§13 (C4 2→3, C5 3→4) repose sur un
  **benchmark sélectif** : il exclut les concurrents qui occupent le créneau —
  surtout **CheckFile.ai** (FR/EU, DORA, KYC/AML, audit trail 5 ans, self-service
  ~0,30 €/doc, **cité comme *source* sans être vu comme concurrent**), ainsi que
  **Rossum** (inbox email native + HITL) et **Parseur** (email→JSON, 39 $/mois).
  **C4=3 et C5=4 ne sont pas justifiés (→ 2 et 2).** Les §10–§13 ci-dessous
  reflètent le passage initial et restent à corriger.
- **Pitch (1 phrase)** : Work-as-a-Service sur **un micro-process métier** : email ou PDF entrant → dossier structuré (JSON + preuves) validé par un humain, avec traçabilité audit.

---

## 1. Problème / douleur

De nombreux processus métier (compliance, assurance, immobilier, RH, achats) démarrent par un **document ou email non structuré**. Les équipes ressaisissent manuellement, perdent du temps et introduisent des erreurs. Les solutions IDP génériques extraient des champs mais ne livrent pas un **dossier métier validé** prêt à intégrer un workflow ou un système cible.

## 2. Cible & qui paie

| Acteur | Douleur | Budget |
|---|---|---|
| **PME/ETI** avec process documentaire récurrent | Saisie manuelle, délais | Abonnement + usage (30–500 €/mois selon volume) |
| **Cabinets / BPO** | Marge sur traitement unitaire | Par dossier traité |
| **Équipes compliance / ops** | Preuve et traçabilité | Budget outil métier |

Utilisateur = souvent ops ; payeur = responsable process ou DSI.

## 3. Données sources

Pas de dépendance à un dataset open data unique : les **documents entrants** (email, PDF) sont la source primaire. Enrichissement optionnel via APIs tierces (SIRENE, géocodage) selon le vertical — à cadrer par micro-process.

| Source | Rôle | Limites |
|---|---|---|
| Email entrant (IMAP/webhook) | Déclencheur + corps + PJ | Formats hétérogènes |
| PDF / images | Extraction OCR/IDP | Qualité scan variable |
| Schéma JSON métier (config) | Structure cible du dossier | Défini par template process |

## 4. Existant / concurrence

> Cartographie B (consultée 2026-06-23). Marché fragmenté entre parsing inbox,
> IDP et automation — catalogue structuré ci-dessous.

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **API Entreprise (INPI / DILA)** | https://www.data.gouv.fr/dataservices/api-entreprise | KYC lite : statuts, dirigeants, attestations — pivot possible |
| **Chorus Pro / facturation publique** | https://chorus-pro.gouv.fr/ | Dématérialisation factures secteur public (adjacent process document) |
| **MCP data.gouv.fr** | https://www.data.gouv.fr/dataservices | Catalogue datasets — contexte enrichissement, pas extraction email |

### Réutilisations data.gouv

Peu de réutilisation directe « email → dossier » sur data.gouv ; les jeux ouverts
servent surtout de **contexte métier** (SIRENE, RNA) dans un pivot KYC lite.
API Entreprise : https://www.data.gouv.fr/dataservices/api-entreprise (consulté 2026-06-23).

### Produits commerciaux (parsing / IDP / automation)

Synthèse :
- **Parsing email dédié** : [Parseur](https://parseur.com/pricing) (à partir de 39 $/mois, consulté 2026-06-23), [Mailparser](https://mailparser.io/pricing) (49 $/mois), [Parsio](https://parsio.io/pricing) (41 $/mois) — extraction champs, peu de boucle validation métier.
- **IDP générique** : [Rossum](https://rossum.ai/pricing/) (usage-based, consulté 2026-06-23), [Extend](https://www.extend.ai/pricing) (crédits documents), [Nanonets](https://nanonets.com/pricing) — extraction performante, workflow « dossier validé » souvent absent ou add-on.
- **Workflow + revue** : Dext, Levity, Pipefy, Tonkean (V5h) — plus proches du positionnement mais généralistes ou verticaux compta/ops, pas micro-process configurable.
- **Automation** : Zapier/Make + IDP — bricolage, gouvernance et traçabilité audit faibles.
- **Niche compliance→spec** : [Probo](https://www.probo.ai/) (FR, strong), Regulativ.ai, DiliTrust, Yooz — segment moins saturé mais angle « réglementation → spec » plutôt que « email → dossier ».

→ Détail traçable : section **Catalogue SaaS** ci-dessous et [`catalogue-saas/README.md`](../../catalogue-saas/README.md).

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0029-recordai` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `parsing-inbox` — Parsing email & inbox

Fichier : [`catalogue-saas/vendors/parsing-inbox.json`](../../catalogue-saas/vendors/parsing-inbox.json) (41 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `parseur` | Parseur | unknown | unknown | verified |
| `mailparser` | Mailparser | unknown | unknown | verified |
| `docparser` | Docparser | unknown | unknown | partial |
| `parsio` | Parsio | unknown | unknown | verified |
| `airparser` | Airparser | unknown | unknown | verified |
| `mailgun-inbound` | Mailgun Inbound Routes | unknown | unknown | partial |
| `postmark-inbound` | Postmark Inbound | unknown | unknown | partial |
| `extracta-ai` | Extracta.ai | unknown | unknown | partial |
| `nylas` | Nylas | US | partial | verified |
| `sendgrid-inbound` | Twilio SendGrid Inbound Parse | US | partial | partial |
| `mailjet-parse` | Mailjet Email Parser | FR | strong | verified |
| `mailslurp` | MailSlurp | US | partial | partial |
| … | _+29 autres_ | | | |

#### Segment `document-idp` — IDP & extraction documentaire

Fichier : [`catalogue-saas/vendors/document-idp.json`](../../catalogue-saas/vendors/document-idp.json) (60 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `google-document-ai` | Google Cloud Document AI | US | partial | verified |
| `aws-textract` | AWS Textract | US | partial | partial |
| `azure-document-intelligence` | Azure AI Document Intelligence | US | partial | verified |
| `nanonets` | Nanonets | US | partial | verified |
| `extend-ai` | Extend AI | US | partial | verified |
| `docupipe` | DocuPipe | unknown | unknown | verified |
| `sensible` | Sensible | US | partial | verified |
| `docsumo` | Docsumo | US | partial | verified |
| `rossum` | Rossum | US | partial | verified |
| `snapparse` | Snapparse | unknown | unknown | verified |
| `iteration-layer` | Iteration Layer | US | partial | verified |
| `docld` | DocLD | unknown | unknown | verified |
| … | _+48 autres_ | | | |

#### Segment `compliance-to-spec` — Réglementation → spec produit

Fichier : [`catalogue-saas/vendors/compliance-to-spec.json`](../../catalogue-saas/vendors/compliance-to-spec.json) (48 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `compliance-to-architecture` | Compliance-to-Architecture (CtA) | unknown | unknown | verified |
| `aispecify` | AiSpecify | US | partial | verified |
| `open-policy-agent` | Open Policy Agent (OPA) | unknown | unknown | verified |
| `hyperproof` | Hyperproof | US | partial | verified |
| `onspring` | Onspring | US | partial | verified |
| `secureframe` | Secureframe | unknown | unknown | verified |
| `snyk` | Snyk | IE | partial | partial |
| `styra` | Styra | US | partial | partial |
| `regscale` | RegScale | US | absent | partial |
| `anecdotes` | Anecdotes | US | partial | verified |
| `scrut-automation` | Scrut Automation | IN | absent | partial |
| `thoropass` | Thoropass | US | partial | partial |
| … | _+36 autres_ | | | |

#### Segment `automation-platforms` — Automatisation no-code / iPaaS

Fichier : [`catalogue-saas/vendors/automation-platforms.json`](../../catalogue-saas/vendors/automation-platforms.json) (30 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `zapier` | Zapier | unknown | unknown | verified |
| `make` | Make | unknown | unknown | partial |
| `n8n` | n8n | unknown | unknown | partial |
| `workato` | Workato | US | partial | verified |
| `tray-io` | Tray.io | US | partial | partial |
| `pipedream` | Pipedream | unknown | unknown | verified |
| `activepieces` | Activepieces | unknown | unknown | verified |
| `microsoft-power-automate` | Microsoft Power Automate | US | partial | partial |
| `tines` | Tines | US | partial | partial |
| `windmill` | Windmill | FR | strong | verified |
| `relay-app` | Relay.app | US | partial | partial |
| `bardeen` | Bardeen | US | partial | partial |
| … | _+18 autres_ | | | |

#### Segment `kyc-aml` — KYC / AML / identity

Fichier : [`catalogue-saas/vendors/kyc-aml.json`](../../catalogue-saas/vendors/kyc-aml.json) (25 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `onfido` | Onfido | GB | partial | partial |
| `sumsub` | Sumsub | US | partial | partial |
| `jumio` | Jumio | US | partial | partial |
| `complyadvantage` | ComplyAdvantage | US | partial | partial |
| `seon` | SEON | US | partial | partial |
| `ubble` | Ubble | FR | strong | verified |
| `veriff` | Veriff | EE | partial | partial |
| `idnow` | IDnow | DE | partial | partial |
| `persona` | Persona | US | partial | partial |
| `trulioo` | Trulioo | CA | partial | partial |
| `alloy` | Alloy | US | partial | verified |
| `dotfile` | Dotfile | FR | strong | verified |
| … | _+13 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment parsing-inbox
```

<!-- catalogue-saas-end -->
## 5. Différenciation

- **Un micro-process** (pas une plateforme générique) : schéma de dossier, règles métier, validation humaine ciblée.
- **Pricing hybride A+C** : abonnement socle + **par dossier validé** (outcome partiel).
- **Traçabilité** : qui a validé quoi, version du schéma, source document — prêt audit.
- **France / EU** : hébergement et RGPD comme argument vs stack US-only.

Risque : copiable si on reste sur un seul template sans profondeur métier.

## 6. Faisabilité & fiabilité technique

- Pipeline : réception email → extraction (IDP/LLM) → **JSON structuré** → file de validation → webhook export.
- Chiffres extraits : traçabilité champ → bbox/page/source ; pas de nombre inventé par le LLM sans ancrage.
- LLM pour **classification et libellés** ; validation humaine sur champs critiques.

## 7. Monétisation / impact

| Composant | Modèle |
|---|---|
| Socle | Abonnement (sièges ops ou workspace) |
| Variable | Par dossier validé / par document |
| Option | SLA + support vertical |

Aligné sur la tendance 2026 : hybride siège + usage + outcome partiel.

## 8. Risques

- IDP génériques montent en gamme (validation, workflows).
- Coût inférence LLM sur gros volumes.
- Verticalisation nécessaire pour défendre le pricing.

## 9. Effort MVP

1 micro-process pilote (ex. déclaration sinistre lite, dossier KYC lite, ou bon de commande) :
- 1 boîte email ou upload
- 1 schéma JSON
- UI validation 10 champs
- Export webhook CSV/JSON

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré | Justification courte |
|---|---|---|---:|---:|---|
| C1 | Intensité du problème | 3 | 4 | 12 | Saisie manuelle récurrente, coût ops réel |
| C2 | Cible solvable (qui paie) | 3 | 3 | 9 | Payeurs identifiés mais budgets fragmentés (PME vs BPO) |
| C3 | Disponibilité & fiabilité données | 3 | 3 | 9 | Documents = source ; pas d'avantage open data |
| C4 | Espace concurrentiel libre | 2 | 3 | 6 | Segment KYC lite DORA fintech FR/EU : Inscribe (US) seul acteur proche, Ubble rachetée enterprise (Checkout.com), Klippa/Doxis migré ECM — espace SMB ouvert (§13) |
| C5 | Différenciation défendable | 2 | 4 | 8 | Ancre réglementaire DORA art. 9-10 + AMLD6 + hébergement EU + focus SMB : différenciation plus durable (§13) |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 | Pipeline email→JSON traçable, champs ancrés source |
| C7 | Facilité du MVP | 2 | 3 | 6 | 1 micro-process faisable mais choix vertical bloquant |
| C8 | Maîtrise des risques | 2 | 2 | 4 | IDP montent en gamme ; coût LLM ; profondeur métier requise |
| C9 | Monétisation / impact | 2 | 4 | 8 | Hybride abonnement + par dossier aligné marché 2026 |
| | **Total** | | | **70 / 105** | |

**Score /100** : 70 / 105 × 100 = **67**

## 11. Verdict & décision

🔁 **À retravailler** (score relevé 66→67 après benchmark KYC lite §13). Douleur réelle et modèle économique crédible. Le benchmark §13 confirme l'espace : aucun concurrent direct ne couvre le flux « email entrant → dossier KYC structuré → validation humaine → audit trail DORA » sur le segment SMB fintech FR/EU. C4 et C5 re-scorés sur la base du vertical KYC lite retenu en §12.

**Prochaine étape** : valider le pricing avec 3 prospects fintechs FR, puis construire le pilote MVP KYC lite (périmètre §12).

---

## 12. Micro-process pilote recommandé

### Comparatif des trois candidats

| Critère | Sinistre lite | **KYC lite** ✓ | Bon de commande |
|---|---|---|---|
| **Saturation C4** | Haute — Shift Claims (FR, lancé sept. 2025, [PR Newswire 2025-09-16](https://www.prnewswire.com/fr/communiques-de-presse/shift-claims-lia-agentique-qui-accelere-et-optimise-la-gestion-des-sinistres-302557040.html)), Korint.io, Mediar.ai couvrent la chaîne complète | **Modérée** — segment enterprise (Onfido, Jumio) hors de portée PME/fintech ; niche « lite + audit trail DORA » peu couverte dans le catalogue (`inscribe` = seul acteur, HQ US, `france_market: partial`, [inscribe.ai](https://www.inscribe.ai/), consulté 2026-06-23) | Très haute — Limnos.app (FR, lancé avr. 2026, [limnos.app](https://limnos.app/), consulté 2026-06-23), OrderScan (FR, [orderscan.ai](https://www.orderscan.ai/), consulté 2026-06-23), Yooz (`france_market: strong`) |
| **Payeur clair** | Flou : assureurs enterprise ont des outils dédiés ; courtiers SMB ont des budgets insuffisants ([Tensoria, consulté 2026-06-23](https://tensoria.fr/blog/automatiser-gestion-sinistres-courtier-ia)) | **Clair** : fintechs, EMI, néo-banques sous DORA (Art. 9-10, applicable depuis jan. 2025) ont un budget compliance réglementaire non-discrétionnaire ([CheckFile.ai, consulté 2026-06-23](https://www.checkfile.ai/fr-CH/blog/dora-2026-verification-documentaire-secteur-financier)) | Clair : équipes ADV/PME, ROI mesurable — mais concurrence directe déjà établie |
| **MVP faisable** | Moyen — domaine complexe (fraude, ACPR, flux experts) | **Fort** — schéma standard ≤15 champs (nom, prénom, DDN, nationalité, type/n° pièce, justif. domicile), documents connus (CNI/passeport + quittance/relevé), règles de validation formalisées | Fort — mais marché déjà attaqué par des acteurs FR mieux positionnés |
| **Angle FR/EU** | Moyen — réglementé ACPR mais marché occupé par des insurtechs FR | **Fort** — double contrainte DORA (UE 2022/2554) + AMLD6 : audit trail horodaté, 5 ans rétention, hébergement EU défendable face aux stacks US-only | Faible — e-facture 2026 est un vecteur, mais pas de contrainte audit trail comparable |

---

### Pilote recommandé : **KYC lite**

**Justification en 3 points** :

1. **Réglementation comme moteur de demande (payeur non-discrétionnaire)** — DORA (applicable depuis le 17 janvier 2025) et AMLD6 imposent aux entités financières un audit trail déterministe et horodaté pour toute vérification documentaire. Une traçabilité « qui a validé quoi, quelle version du document, quelle décision » n'est plus un argument commercial : c'est une obligation légale sous peine de sanction ACPR/AMF ([CheckFile.ai, consulté 2026-06-23](https://www.checkfile.ai/fr-CH/blog/dora-2026-verification-documentaire-secteur-financier) ; [VerifyPDF, consulté 2026-06-23](https://verifypdf.com/dora-compliance-document-verification-financial-services/)). RecordAI, avec son positionnement « dossier validé + audit trail natif », répond directement à cette obligation.

2. **Espace concurrentiel moins saturé sur le segment SMB/fintech lite** — Les solutions enterprise (Onfido, Jumio) exigent des volumes et des budgets d'intégration inaccessibles aux PME fintechs et EMI. Dans le catalogue, `inscribe` est le seul acteur couvrant `kyc_validation + audit_trail`, mais avec `hq_country: US` et `france_market: partial` ([inscribe.ai](https://www.inscribe.ai/), consulté 2026-06-23). Aucun acteur catalogue n'adresse le flux complet « email/PDF entrant → dossier KYC structuré → validation humaine → export audit trail » pour une fintech FR/EU de 5–50 collaborateurs.

3. **MVP le plus simple et schéma le plus stable** — Le schéma KYC de base est normalisé par la réglementation elle-même (L.561-1 CMF, AMLD6) : ≤15 champs, 2–3 types de documents (CNI, passeport, justificatif domicile), règles de validation formalisées. Contrairement au sinistre (multiplicité des types d'événement) ou au bon de commande (multiplicité des ERP et SKU catalogs), le KYC lite offre un périmètre MVP cadré et reproductible.

---

### Périmètre MVP KYC lite

- **Entrée** : email entrant (IMAP/webhook) ou upload PDF/image
- **Schéma JSON** : `nom`, `prenom`, `date_naissance`, `nationalite`, `type_piece_identite`, `numero_piece`, `date_expiration_piece`, `adresse`, `justificatif_domicile_type`, `date_justificatif`, `decision` (conforme / incomplet / à compléter)
- **UI validation** : file de 10 champs à confirmer, avec aperçu document source (bbox/page tracés)
- **Audit trail** : timestamp, identifiant validateur, version schéma, hash document source
- **Export** : webhook JSON ou CSV, conservé 5 ans (AMLD6)
- **Hébergement** : EU, RGPD natif — argument différenciant vs Inscribe (US)

---

### Note de re-scoring C4 / C5 (si pilote KYC lite retenu)

> Le choix du vertical KYC lite modifie matériellement l'espace concurrentiel analysé.
> Le scoring initial (C4 = 2, C5 = 3) portait sur les segments génériques `parsing-inbox` (30 acteurs) et `document-idp` (32 acteurs).
> Recentré sur « KYC lite fintech FR/EU + audit trail DORA », les concurrents directs se réduisent à 1–2 acteurs partiellement positionnés.

| Critère | Note actuelle | Note proposée | Justification |
|---|---:|---:|---|
| C4 — Espace concurrentiel libre | 2 | **3** | Segment « KYC lite + DORA audit trail + FR/EU » peu couvert dans le catalogue ; `inscribe` = seul acteur proche, US, `france_market: partial` (consulté 2026-06-23) |
| C5 — Différenciation défendable | 3 | **4** | Ancre réglementaire (DORA art. 9-10, AMLD6) + hébergement EU + focus SMB fintech = différenciation plus durable qu'un simple « dossier validé » générique |

**Nouveau score brut proposé** : 66 − 4 − 6 + 6 + 8 = **70 / 105** → **67 / 100** (toujours « À retravailler » mais +4 pts, seuil Go à 70/100)

> Ce re-scoring est **confirmé** par le benchmark §13 (Ubble/Checkout.com, Inscribe, Klippa/Doxis AI.dp). Étape restante : validation du pricing avec 3 prospects fintechs FR.

---

## 13. Benchmark KYC lite — concurrents directs

### Contexte

Le §12 a retenu le vertical **KYC lite fintech FR/EU** comme micro-process pilote et identifié 3 concurrents directs à benchmarker : **Ubble** (FR, acquis Checkout.com), **Inscribe** (US) et **Klippa** (NL, rebrandé Doxis AI.dp suite à l'acquisition par SER Group, mars 2025 / rebrand complet mars 2026). Ce benchmark valide ou infirme le re-scoring C4/C5 proposé.

> **Entrées catalogue utilisées** (segments `kyc-aml` et `document-idp`, aucune entrée `unverified`) : `ubble` (`france_market: strong`, `verification_status: partial`), `inscribe` (`hq_country: US`, `france_market: partial`), `klippa` (`hq_country: NL`, `france_market: partial`).

---

### Dimension 1 — Flux email/PDF → dossier structuré

| Acteur | Entrée principale | Pipeline vers dossier structuré | Connecteur email natif |
|---|---|---|---|
| **Ubble** (Checkout.com) | Flux vidéo temps réel (caméra + document tenu en main) | Résultat de vérification JSON via API ; pas de dossier multi-pièces asynchrone | Absent |
| **Inscribe** | Upload document via API (PDF/image) | Extraction champs + Trust Score fraud + routing reviewer ; pas d'intake email IMAP | Absent — API pull uniquement |
| **Klippa → Doxis AI.dp** | Upload web / app / email / API | Extraction OCR + classification + vérification ; email cité comme canal d'upload ([klippa.com/en/dochorizon/kyc-software/](https://www.klippa.com/en/dochorizon/kyc-software/), consulté 2026-06-23) | Partiel — upload email optionnel, pas déclencheur de workflow |
| **RecordAI** (cible) | Email entrant IMAP/webhook + upload PDF/image | Email → extraction → JSON structuré → validation humaine → export | **Natif** — email = déclencheur premier du workflow |

**Écart principal** : aucun des 3 concurrents ne propose de pipeline natif « email entrant IMAP → dossier KYC structuré ». Ubble est exclusivement temps réel biométrique ; Inscribe est API pull fraud-first ; Klippa/Doxis mentionne l'email comme canal d'upload mais pas comme déclencheur de workflow documentaire.

---

### Dimension 2 — Validation humaine & audit trail

| Acteur | Validation humaine | Audit trail | Conformité DORA / AMLD6 |
|---|---|---|---|
| **Ubble** (Checkout.com) | Human review pour cas complexes (SLA 5 min – 24 h selon tier) | Log vérification identité ; pas de dossier documentaire horodaté multi-étapes | Non mis en avant pour DORA art. 9-10 |
| **Inscribe** | Routing automatique vers compliance reviewer sur Trust Score bas | Trust Score (0-100) + fraud signals + revision history + résumés LLM ; SOC 2 Type II + ISO 27001 | SOC 2 / ISO 27001 ; pas de positionnement DORA EU-first explicite |
| **Klippa → Doxis AI.dp** | Human-in-the-loop disponible pour cas à risque élevé | Logs extraction + vérification d'authenticité ; audit trail partiel | EU-hosted GDPR + ISO 27001 ; DORA non mis en avant ; post-acquisition SER Group complexité croissante |
| **RecordAI** (cible) | File de validation humaine par dossier (UI 10 champs + aperçu source bbox/page) | Timestamp horodaté + identifiant validateur + version schéma + hash document — **natif DORA** | **DORA art. 9-10 + AMLD6 (rétention 5 ans)** — argument central |

**Écart** : Inscribe est le plus proche sur l'audit trail documentaire, mais son positionnement est fraude/scoring US, pas workflow DORA EU-first. Klippa/Doxis a le human-in-the-loop mais n'a pas formalisé l'audit trail pour la conformité réglementaire UE.

---

### Dimension 3 — Pricing public (juin 2026)

| Acteur | Pricing public | Lien (consulté 2026-06-23) | Modèle |
|---|:---:|---|---|
| **Ubble** (Checkout.com) | ❌ Non | [checkout.com/pricing](https://www.checkout.com/pricing) | Sur mesure selon profil ; min. ~2 000 vérif/mois mentionné |
| **Inscribe** | ❌ Non | [inscribe.ai](https://www.inscribe.ai/) | Quote-based enterprise ; contact sales uniquement |
| **Klippa → Doxis AI.dp** | ❌ Non | [klippa.com/en/dochorizon/kyc-software/](https://www.klippa.com/en/dochorizon/kyc-software/) | Annual license ou pay-per-document ; volume-based ; custom quote |
| **RecordAI** (cible) | ✅ Cible | — | Abonnement socle + par dossier validé — pricing transparent self-serve |

**Observation** : les 3 concurrents pratiquent un pricing opaque sales-led. RecordAI peut se différencier par un **pricing transparent self-serve** adapté aux PME fintechs (abonnement + usage, seuil d'entrée bas), inaccessible aujourd'hui via les offres enterprise existantes.

---

### Dimension 4 — Positionnement FR/EU vs US

| Acteur | HQ | Hébergement EU | Marché FR | Argument RGPD / DORA |
|---|---|:---:|---|---|
| **Ubble** (Checkout.com) | GB (Checkout.com) — équipes FR conservées | ✅ EU disponible | Fort (fondé FR 2018, acquis 2022) | GDPR natif ; eIDAS ; ANSSI (avant acquisition) ; souveraineté FR affaiblie post-rachat |
| **Inscribe** | US (San Francisco) | ❌ Non confirmé EU | Partiel | SOC 2 / ISO 27001 ; pas d'EU-first ; données hébergées US |
| **Klippa → Doxis AI.dp** | NL / DE (SER Group) | ✅ EU-hosted | Partiel | GDPR + ISO 27001 ; intégration dans écosystème enterprise DE (SER Group ECM/BPM) éloigne l'offre du segment SMB |
| **RecordAI** (cible) | FR (cible) | ✅ EU natif | Fort (cible) | **DORA + AMLD6 + RGPD — argument central** ; seul acteur FR SMB-first sur ce flux |

**Note** : Ubble est d'origine FR mais opère désormais sous Checkout.com (UK/global) depuis 2022 — l'argument « souveraineté FR » est affaibli. Inscribe est clairement US. Klippa/Doxis est EU mais son intégration dans SER Group (éditeur enterprise DE) le tire vers des contrats complexes, éloignant son offre du segment SMB fintech.

---

### Dimension 5 — Gap RecordAI par concurrent

| Acteur | Gap principal vs RecordAI |
|---|---|
| **Ubble** (Checkout.com) | Verticalisé vérification identité **temps réel** (selfie + vidéo, liveness) ; ne couvre pas le workflow **email entrant async → dossier multi-documents** avec validation humaine ; volume minimum enterprise (≥ 2 000 vérif/mois) inaccessible PME fintech en phase pilote |
| **Inscribe** | API pull uniquement, pas de connecteur email IMAP natif ; HQ US, hébergement non EU-first ; focus **fraude/scoring** plutôt que workflow dossier KYC complet validé ; pricing enterprise hors portée PME |
| **Klippa → Doxis AI.dp** | Racheté par SER Group (enterprise ECM/BPM) → complexité et prix croissants, roadmap post-rebrand incertaine ; pas d'argument DORA natif ; upload email en option mais pas déclencheur workflow ; éloigné du segment SMB fintech FR |

---

### Tableau synthèse benchmark

| Critère | Ubble (Checkout.com) | Inscribe | Klippa → Doxis AI.dp | RecordAI (cible) |
|---|:---:|:---:|:---:|:---:|
| Flux email entrant natif | ❌ | ❌ | ⚠️ partiel | ✅ |
| Dossier multi-documents structuré | ❌ | ⚠️ partiel | ⚠️ partiel | ✅ |
| Validation humaine dossier async | ⚠️ biométrie | ✅ fraud review | ⚠️ partiel | ✅ |
| Audit trail DORA / AMLD6 natif | ❌ | ⚠️ partiel (US) | ❌ | ✅ cible |
| Pricing transparent SMB self-serve | ❌ | ❌ | ❌ | ✅ cible |
| Hébergement EU-first | ⚠️ UK post-acq. | ❌ | ✅ NL/DE | ✅ FR cible |
| Marché FR fort | ✅ origine | ❌ | ⚠️ | ✅ cible |
| Cible SMB fintech accessible | ❌ | ❌ | ❌ | ✅ cible |

**Légende** : ✅ couvert · ⚠️ partiel · ❌ absent

---

### Verdict benchmark

Le benchmark confirme que **l'espace « KYC lite email/PDF → dossier validé + audit trail DORA, segment SMB fintech FR/EU » est effectivement peu couvert** :

- **Ubble/Checkout.com** : seul acteur à forte implantation FR, mais son acquisition par Checkout.com l'a repositionné sur le segment enterprise temps réel biométrique (vidéo, liveness), éloignant son offre du workflow documentaire asynchrone visé par RecordAI.
- **Inscribe** : concurrent le plus proche sur l'audit trail et le case management, mais positionnement US, focus fraude, pricing enterprise — hors portée des PME fintechs FR/EU.
- **Klippa/Doxis AI.dp** : IDP EU-hosted solide sur l'extraction, mais rachat par SER Group (enterprise ECM) tire l'offre vers la complexité et les grands comptes ; pas d'argument DORA natif ; segment SMB non adressé.

**Gap principal RecordAI vs Ubble** : Ubble est une solution de vérification d'identité **biométrique temps réel** (flux vidéo, selfie, liveness check), non un outil de traitement de **dossiers documentaires entrants par email** avec validation humaine asynchrone et audit trail DORA. Les deux produits opèrent sur des flux différents — RecordAI couvre le traitement documentaire asynchrone en amont de l'identification biométrique.

> **Conclusion** : le re-scoring C4 (2→3) et C5 (3→4) proposé en §12 est **confirmé** par ce benchmark. L'espace concurrentiel direct sur le vertical KYC lite fintech FR/EU email/PDF asynchrone reste ouvert. Score final : **67/100** (🔁 À retravailler — seuil Go à 70/100 ; +1 pt de validation prospect suffisant pour franchir le seuil).
