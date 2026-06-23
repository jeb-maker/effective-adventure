# Pilotage rénovation des copropriétés (RNIC × DPE × DECP)

- **ID** : 0025
- **Statut** : 🔁 À retravailler
- **Score** : 60 / 100
- **Dernière mise à jour** : 2026-06-23
- **Révision critique** : voir [`revue.md`](revue.md) — score abaissé de **64 à 60**
  après audit adversarial. Le différenciateur unique (`RNIC.siret_syndic × DECP`)
  est **conceptuellement cassé** : la DECP est la commande *publique*, or une
  copropriété privée n'est pas pouvoir adjudicateur — ses travaux n'y figurent
  jamais (le moat ne vaut que pour les bailleurs sociaux, non solvables / servis
  gratuitement par Go Rénove PRO). Concurrents omis : **Powimo (Datahub)** pilote
  déjà le parc DPE, **CoproFF (Cerema)** croise déjà RNIC × fichiers fonciers.
  Le vrai point bloquant n'est pas la complétude du SIRET syndic (il est publié).
  Les §3bis–§11 ci-dessous reflètent le passage initial et restent à corriger.
- **Pitch (1 phrase)** : Pour syndics professionnels et bailleurs : croiser le
  registre national des copropriétés (RNIC), les DPE et les marchés publics de
  rénovation (DECP) pour prioriser les copropriétés à rénover et tracer les
  interventions passées — pivot B2B de l'idée [0009](../0009-dpe-passoires-thermiques/).

---

## 1. Problème / douleur

Les syndics professionnels et bailleurs gèrent des **portefeuilles de copropriétés**
dont une part significative est en passoire thermique (F/G). La loi Climat impose
une trajectoire de rénovation ; les dispositifs MaPrimeRénov' copropriété exigent
un diagnostic et un plan de travaux.

Douleurs :
- **Priorisation** : quelles copropriétés traiter en premier (taille, classe énergétique,
  procédure en cours) ?
- **Traçabilité** : quels travaux de rénovation ont déjà été commandés (DECP, entreprises RGE) ?
- **Données éclatées** : RNIC (gouvernance), DPE (performance), DECP (marchés) ne sont
  pas croisés dans un outil unique orienté **gestion de parc**.

**Distinction vs 0009** : 0009 cible la prospection artisan (saturée, risque juridique).
0025 cible le **gestionnaire de parc** (syndic, bailleur) — usage licite, pas de démarchage.

## 2. Cible & qui paie

| Segment | Besoin | Qui paie ? |
|---|---|---|
| **Syndics professionnels** (≥ 200 lots) | Pilotage portefeuille, plans pluriannuels | Le syndic (budget outil / conseil) |
| **Bailleurs sociaux** | Parc HLM en copropriété ou ASL | Direction patrimoine |
| **Collectivités** (OPAH, ANAH) | Ciblage copropriétés fragiles | Budget politique publique — mais Go Rénove existe |

Payeur plausible : syndic pro avec portefeuille > 50 copropriétés. Budget indicatif :
outils métier syndic (copropriété) facturés 50–200 €/mois par structure — à valider
par entretiens.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| **RNIC** | https://www.data.gouv.fr/datasets/registre-national-dimmatriculation-des-coproprietes | LO 2.0 | CSV ~430 Mo/trim. | MàJ **17 juin 2026** ; quotidien depuis avr. 2026 | Pas de propriétaire ; SIRET syndic incomplet ; renommage colonnes avr. 2026 |
| **DPE logements** | https://data.ademe.fr/datasets/dpe03existant | LO 2.0 | API/PostgreSQL | ~350 k DPE/mois | Pas de lien direct RNIC ; jointure adresse |
| **DECP** (titulaires RGE / travaux) | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | LO 2.0 | Parquet | ~quotidienne | MAPA < seuil absents ; montant ≠ dépense réelle |
| **Certifications RGE** | https://www.data.gouv.fr/dataservices/api-professionnels-rge | LO 2.0 | API REST | Régulière | Périmètre rénovation énergétique |
| **BAN** (géocodage) | https://api-adresse.data.gouv.fr | LO 2.0 | REST | Continue | Qualité adresse copropriété variable |

**Vérification disponibilité** (2026-06-21) : RNIC téléchargeable (fichier T3 2025,
~453 Mo) ; DPE et DECP confirmés ouverts. Détails :
[`docs/sources-complementaires.md`](../../docs/sources-complementaires.md).

### 3bis. Croisements & requêtes SQL traçables

| Indicateur | Jointure | SQL ? |
|---|---|---|
| Nb lots F/G par copropriété | RNIC.num_lots × DPE (adresse) | ✅ avec réserves qualité adresse |
| Syndic (SIRET) × marchés DECP rénovation | RNIC.siret_syndic × DECP.titulaire_id | ✅ si SIRET renseigné |
| Copropriétés en procédure (art. 29-1) × passoires | RNIC.procédure × DPE classe | ✅ |
| Historique marchés travaux sur la commune | DECP.codeCPV (45xx) × RNIC.code_commune | ✅ agrégat |

## 4. Existant / concurrence

> Cartographie B (consultée 2026-06-23). Voir aussi [`revue.md`](revue.md).

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **Go Rénove PRO (CSTB / BDNB)** | https://www.bdnb.io/services/gorenove/ | Analyse de parc copropriétés/bailleurs — **gratuit** |
| **ANAH / Hub rénovation** | https://www.anah.fr/ | Dispositifs MaPrimeRénov' copropriété |
| **CoproFF (Cerema)** | https://www.cerema.fr/fr/actualites/coproff-outil-de-visualisation-des-coproprietes | Visualisation copropriétés (RNIC × foncier) — service public |

### Réutilisations data.gouv

| Jeu / service | URL | Rôle |
|---|---|---|
| **RNIC** | https://www.data.gouv.fr/datasets/registre-national-dimmatriculation-des-coproprietes | Registre copropriétés (socle idée) |
| **DECP consolidée** | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | Marchés publics (limite : copropriété ≠ acheteur public) |
| **API RGE** | https://www.data.gouv.fr/dataservices/api-professionnels-rge | Entreprises certifiées rénovation |

### Concurrents directs — syndic + DPE + rénovation

| Concurrent | Positionnement | URL | Consulté |
|---|---|---|---|
| **ScanReno** | SaaS syndics pros : PPT 10 ans, DPE collectif 2026, aides ANAH intégrées, 490–790 €/mois HT jusqu'à 50 copros | https://www.scanreno.fr/ | juin 2026 |
| **CoproSolutions (Hellio)** | Suivi PPT, DPE collectif, pilotage travaux copropriétés — tableau de bord multi-portefeuille | https://copropriete.hellio.com/blog/renovation-energetique/logiciel-suivi-travaux | juin 2026 |
| **Matera** | Syndic digital FR — gestion copropriété, AG, comptabilité ; pas de croisement RNIC×DECP identifié | https://www.matera.eu/ | juin 2026 |
| **ICS / Seiitra** | Logiciels métier syndics professionnels (gestion lourde) | https://logicielsyndic.fr/comparatif-logiciel-syndic | juin 2026 |

### Concurrents sur la niche bailleurs / collectivités

| Concurrent | Positionnement | URL | Consulté |
|---|---|---|---|
| **Go Rénove PRO (CSTB / BDNB)** | Service public gratuit : analyse de parc, tableaux de bord pilotage rénovation, export données — cible bailleurs sociaux + collectivités | https://www.bdnb.io/services/gorenove/ | juin 2026 |
| **Effy Pro** | Rénovation énergétique B2B, accompagnement et données DPE | https://www.effy.fr/pro | juin 2026 |
| **OpenMéti** | Plateforme open data énergie bâtiments, DPE et rénovation | https://www.openmeti.fr/ | juin 2026 |

### Analyse des lacunes

ScanReno et CoproSolutions couvrent déjà le pilotage syndic/DPE/PPT. Go Rénove PRO (gratuit)
couvre les bailleurs sociaux et collectivités. **Lacune réelle** : croisement RNIC × DECP pour
tracer les marchés de rénovation déjà passés par les syndics — non identifié dans les offres
concurrentes. Niche étroite.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0025-coproprietes-renovation-rnic` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `energy-buildings-fr` — Bâtiments & énergie FR

Fichier : [`catalogue-saas/vendors/energy-buildings-fr.json`](../../catalogue-saas/vendors/energy-buildings-fr.json) (18 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `openmeti` | OpenMéti | FR | strong | partial |
| `ademe-data` | ADEME — data services | FR | strong | partial |
| `effy-pro` | Effy Pro | FR | strong | partial |
| `hub-anah` | Anah — Hub rénovation | FR | strong | partial |
| `heero` | Heero | FR | strong | partial |
| `uk-epc-register` | UK EPC Register | GB | absent | partial |
| `building-performance-database` | Building Performance Database (US DOE) | US | absent | partial |
| `dena-gebaeudedaten` | dena — Gebäudedaten (DE) | DE | unknown | partial |
| `gridx-energy` | gridX | DE | partial | partial |
| `hellowatt` | Hello Watt | FR | strong | partial |
| `enoptea` | Enoptea | FR | strong | partial |
| `cantine-energetique` | Cantine Énergétique | FR | strong | partial |
| … | _+6 autres_ | | | |

#### Segment `real-estate-proptech` — Immobilier & proptech

Fichier : [`catalogue-saas/vendors/real-estate-proptech.json`](../../catalogue-saas/vendors/real-estate-proptech.json) (20 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `costar` | CoStar | US | partial | partial |
| `yardi` | Yardi | US | partial | partial |
| `procore` | Procore | US | partial | partial |
| `matera` | Matera | FR | strong | partial |
| `pricehubble` | PriceHubble | CH | partial | partial |
| `scanreno` | ScanReno | FR | strong | partial |
| `powimo` | Powimo | FR | strong | partial |
| `egide-copro` | EGIDE Copro | FR | strong | partial |
| `copro-solutions` | CoproSolutions | FR | strong | partial |
| `bdnb` | BDNB (CSTB) | FR | strong | partial |
| `kel-foncier` | Kel Foncier | FR | strong | partial |
| `deepki` | Deepki | FR | strong | partial |
| … | _+8 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment energy-buildings-fr
```

<!-- catalogue-saas-end -->

## 5. Différenciation

**Avantage potentiel** : seul outil à croiser RNIC × DECP pour montrer l'historique des
marchés de rénovation passés par un syndic — aucun concurrent identifié ne fait cette jonction.

**Limites** :
- Toutes les données sont ouvertes → copiable rapidement par ScanReno ou un autre acteur
- Taux de complétude SIRET syndic dans le RNIC est incertain (point à mesurer avant développement)
- Go Rénove PRO (gratuit) creuse l'écart : un bailleur social n'a aucune raison de payer

**Verdict différenciation** : défendable à court terme uniquement si accès à un canal de
distribution captif (partenariat fédération syndics, FNAIM, UNIS) — sans canal, le croisement
DECP est reproductible en quelques semaines par ScanReno.

## 6. Faisabilité & fiabilité technique

- Ingestion RNIC trimestrielle + flux DPE + DECP → DuckDB/PostgreSQL.
- Jointure principale : **adresse normalisée** (BAN) entre RNIC et DPE — point
  faible si adresse syndic ≠ adresse lots.
- Tous les chiffres (nb passoires, montants DECP) via **SQL traçable** ; LLM pour
  expliquer réglementation copropriété / aides uniquement.

## 7. Monétisation / impact

**Modèle envisagé** : SaaS B2B — abonnement mensuel par structure syndic.

| Tier | Prix indicatif | Périmètre |
|---|---|---|
| Starter | 99–200 €/mois | ≤ 20 copropriétés |
| Pro | 300–600 €/mois | ≤ 100 copropriétés |
| Enterprise | Sur devis | Grands groupes (Nexity, Foncia...) |

**Référence marché** : ScanReno facture 490–790 €/mois HT pour 10–50 copros
(source : https://www.scanreno.fr/, juin 2026). Plafond existant confirmé.

**Risque de tarification** : Go Rénove PRO gratuit tire le prix vers le bas pour le
segment bailleurs. Le segment syndics pro est la seule cible réellement solvable.

**Impact alternatif** : outil interne / open source pour collectivités si modèle
commercial non viable.

## 8. Risques

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| SIRET syndic manquant dans RNIC | Élevée | Élevé — casse la jointure RNIC×DECP | Mesurer le taux réel avant tout développement |
| Taux de jointure adresse RNIC×DPE faible | Moyenne | Élevé — produit sans valeur si <40% de match | Test SQL sur échantillon avant MVP |
| ScanReno copie le croisement DECP | Haute | Élevé — destruction avantage compétitif | Nécessite canal distribution avant ScanReno |
| Go Rénove PRO s'étend aux syndics | Moyenne | Élevé — concurrent public gratuit direct | Différenciation niche très étroite requise |
| Réglementation DECP : marchés < seuil absents | Structurel | Moyen — données incomplètes | Documenter le trou de couverture dans l'UI |

**Point éliminatoire potentiel** : si le taux de SIRET syndic renseigné dans le RNIC
est < 30 %, la jonction RNIC×DECP devient inexploitable et la principale différenciation tombe.

## 9. Effort MVP

**Périmètre minimal crédible** :

1. Ingestion RNIC (CSV trimestriel) + DPE ADEME (API) + DECP (Parquet mensuel) dans PostgreSQL
2. Géocodage BAN des copropriétés RNIC
3. Jointure adresse RNIC × DPE → score thermique par copropriété
4. Jointure SIRET syndic (RNIC) × titulaire DECP → marchés RGE passés
5. Tableau de bord syndic : tri par classe énergétique, filtres commune/procédure
6. Export CSV du portefeuille filtré

**Estimation** : 3 semaines de développement (ingestion + SQL + UI minimaliste) après
validation du taux de jointure adresse sur échantillon.

**Pré-requis bloquant** : mesurer taux SIRET syndic et taux jointure adresse sur
un échantillon RNIC avant tout développement UI.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 |
| C2 | Cible solvable (qui paie) | 3 | 3 | 9 |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 |
| C4 | Espace concurrentiel libre | 2 | 2 | 4 |
| C5 | Différenciation défendable | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 3 | 6 |
| C8 | Maîtrise des risques | 2 | 3 | 6 |
| C9 | Monétisation / impact | 2 | 3 | 6 |
| | **Total** | | | **67 / 105** |

**Score /100** : `67 / 105 × 100` = **64**

**Justifications** :
- C1=4 : DPE collectif obligatoire dès 2026 (jan. 2026 pour toutes les copros <50 lots),
  PPT obligatoire — douleur réglementaire forte et urgente.
- C2=3 : Syndics pro paient des outils (ScanReno 490–790€/mois prouve la willingness-to-pay),
  mais le marché est déjà adressé.
- C3=4 : RNIC (MàJ 17 juin 2026), DPE ADEME, DECP tous ouverts et opérationnels ;
  jointure adresse imparfaite mais connue.
- C4=2 : ScanReno + CoproSolutions sur la niche syndic/DPE ; Go Rénove PRO gratuit pour
  bailleurs. Peu d'espace libre.
- C5=2 : Croisement DECP×RNIC est le seul différenciateur — copiable en < 1 mois par ScanReno.
- C6=4 : Architecture SQL/traçable propre ; LLM uniquement pour réglementation.
- C7=3 : MVP faisable en 3 semaines MAIS conditionné à la validation du taux de jointure.
- C8=3 : Risque SIRET syndic non mesuré pèse lourd.
- C9=3 : Modèle SaaS plausible (confirmé par ScanReno), mais compétition forte.

## 11. Verdict & décision

🔁 **À retravailler** — score **64/100**

**Atouts** : douleur réelle et urgente (obligation DPE collectif 2026), données sources
vérifiées et disponibles, architecture SQL traçable propre, willingness-to-pay confirmée
par ScanReno (490–790 €/mois).

**Point bloquant principal** : **ScanReno occupe déjà la niche cible** (syndics pro,
PPT, DPE collectif, aides ANAH 2026) avec un produit mature et un tarif établi. La
seule différenciation identifiée — le croisement DECP × RNIC pour tracer les marchés
de rénovation passés — est copiable rapidement et dépend du taux de SIRET syndic
renseigné dans le RNIC (non mesuré).

**Pour débloquer** :
1. Mesurer le taux de SIRET syndic renseigné dans le RNIC sur un échantillon réel.
2. Mesurer le taux de jointure adresse RNIC × DPE (objectif > 60 %).
3. Identifier un canal de distribution captif (fédération syndics, FNAIM, UNIS) que
   ScanReno n'a pas.
4. Si les taux sont faibles ou le canal absent → écarter en faveur de 0009 amélioré.

**Prochaine étape** : requête SQL sur échantillon RNIC (département test) pour mesurer
les deux taux avant toute décision d'investissement.
