# RecordAI — email/PDF → dossier structuré validé

- **ID** : 0029
- **Statut** : 🔁 À retravailler
- **Score** : 66 / 100
- **Dernière mise à jour** : 2026-06-23
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

Marché fragmenté entre **parsing inbox**, **IDP** et **automation** — voir catalogue structuré (segments liés ci-dessous).

Synthèse (consulté 2026-06-23) :
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

Fichier : [`catalogue-saas/vendors/parsing-inbox.json`](../../catalogue-saas/vendors/parsing-inbox.json) (30 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `parseur` | Parseur | unknown | unknown | partial |
| `mailparser` | Mailparser | unknown | unknown | partial |
| `docparser` | Docparser | unknown | unknown | partial |
| `parsio` | Parsio | unknown | unknown | partial |
| `airparser` | Airparser | unknown | unknown | partial |
| `mailgun-inbound` | Mailgun Inbound Routes | unknown | unknown | partial |
| `postmark-inbound` | Postmark Inbound | unknown | unknown | partial |
| `extracta-ai` | Extracta.ai | unknown | unknown | partial |
| `nylas` | Nylas | US | partial | partial |
| `sendgrid-inbound` | Twilio SendGrid Inbound Parse | US | partial | partial |
| `mailjet-parse` | Mailjet Email Parser | FR | strong | partial |
| `mailslurp` | MailSlurp | US | partial | partial |
| … | _+18 autres_ | | | |

#### Segment `document-idp` — IDP & extraction documentaire

Fichier : [`catalogue-saas/vendors/document-idp.json`](../../catalogue-saas/vendors/document-idp.json) (48 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `google-document-ai` | Google Cloud Document AI | US | partial | verified |
| `aws-textract` | AWS Textract | US | partial | partial |
| `azure-document-intelligence` | Azure AI Document Intelligence | US | partial | partial |
| `nanonets` | Nanonets | US | partial | verified |
| `extend-ai` | Extend AI | US | partial | verified |
| `docupipe` | DocuPipe | unknown | unknown | verified |
| `sensible` | Sensible | US | partial | verified |
| `docsumo` | Docsumo | US | partial | partial |
| `rossum` | Rossum | US | partial | verified |
| `snapparse` | Snapparse | unknown | unknown | verified |
| `iteration-layer` | Iteration Layer | US | partial | verified |
| `docld` | DocLD | unknown | unknown | verified |
| … | _+36 autres_ | | | |

#### Segment `compliance-to-spec` — Réglementation → spec produit

Fichier : [`catalogue-saas/vendors/compliance-to-spec.json`](../../catalogue-saas/vendors/compliance-to-spec.json) (37 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `compliance-to-architecture` | Compliance-to-Architecture (CtA) | unknown | unknown | verified |
| `aispecify` | AiSpecify | US | partial | verified |
| `open-policy-agent` | Open Policy Agent (OPA) | unknown | unknown | verified |
| `hyperproof` | Hyperproof | US | partial | partial |
| `onspring` | Onspring | US | partial | partial |
| `secureframe` | Secureframe | unknown | unknown | partial |
| `snyk` | Snyk | IE | partial | partial |
| `styra` | Styra | US | partial | partial |
| `regscale` | RegScale | US | absent | partial |
| `anecdotes` | Anecdotes | US | partial | partial |
| `scrut-automation` | Scrut Automation | IN | absent | partial |
| `thoropass` | Thoropass | US | partial | partial |
| … | _+25 autres_ | | | |

#### Segment `automation-platforms` — Automatisation no-code / iPaaS

Fichier : [`catalogue-saas/vendors/automation-platforms.json`](../../catalogue-saas/vendors/automation-platforms.json) (9 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `zapier` | Zapier | unknown | unknown | partial |
| `make` | Make | unknown | unknown | partial |
| `n8n` | n8n | unknown | unknown | partial |
| `workato` | Workato | US | partial | verified |
| `tray-io` | Tray.io | US | partial | partial |
| `pipedream` | Pipedream | unknown | unknown | verified |
| `activepieces` | Activepieces | unknown | unknown | partial |
| `microsoft-power-automate` | Microsoft Power Automate | US | partial | partial |
| `tines` | Tines | US | partial | partial |

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
| C4 | Espace concurrentiel libre | 2 | 2 | 4 | Parsing-inbox et IDP saturés (26+ / 32+ acteurs catalogue) |
| C5 | Différenciation défendable | 2 | 3 | 6 | Micro-process + validation auditée ; imitable si vertical absent |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 | Pipeline email→JSON traçable, champs ancrés source |
| C7 | Facilité du MVP | 2 | 3 | 6 | 1 micro-process faisable mais choix vertical bloquant |
| C8 | Maîtrise des risques | 2 | 2 | 4 | IDP montent en gamme ; coût LLM ; profondeur métier requise |
| C9 | Monétisation / impact | 2 | 4 | 8 | Hybride abonnement + par dossier aligné marché 2026 |
| | **Total** | | | **66 / 105** | |

**Score /100** : 66 / 105 × 100 = **66**

## 11. Verdict & décision

🔁 **À retravailler.** Douleur réelle et modèle économique crédible, mais **C4 bloquant** : les segments `parsing-inbox` et `document-idp` sont denses ; la différenciation « dossier validé » n'est défendable qu'avec un **micro-process vertical précis** (ex. sinistre lite, KYC lite, bon de commande) et une preuve que les IDP génériques ne couvrent pas ce workflow.

**Prochaine étape** : choisir 1 micro-process pilote, benchmarker 3 concurrents directs sur ce vertical (pas seulement le catalogue générique), puis re-scorer C4/C5.
