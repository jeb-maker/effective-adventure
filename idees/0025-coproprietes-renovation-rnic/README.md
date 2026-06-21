# Pilotage rénovation des copropriétés (RNIC × DPE × DECP)

- **ID** : 0025
- **Statut** : 🔁 À retravailler
- **Score** : 64 / 100
- **Dernière mise à jour** : 2026-06-21
- **Pitch (1 phrase)** : Pour syndics professionnels et bailleurs : croiser le
  registre national des copropriétés (RNIC), les DPE et les marchés publics de
  rénovation (DECP) pour prioriser les copropriétés à rénover et tracer les
  interventions passées — pivot B2B de l'idée [0009](../0009-dpe-passoires-thermiques/).

---

## 1. Problème / douleur

Les syndics professionnels et bailleurs gèrent des **portefeuilles de copropriétés**
soumis à une **cadence réglementaire accélérée** :

- **DPE collectif obligatoire** : depuis le **1er janvier 2026** pour les copropriétés
  de ≤ 50 lots (après 200 lots en 2024 et 50–200 en 2025) — https://sensei-avocats.fr/flash/application-des-dpe-collectif-et-nouvelle-methode-de-calcul-ce-qui-change-au-1er-janvier-2026/
  (consulté 2026-06-21).
- **Plan pluriannuel de travaux (PPT)** : obligatoire pour toutes les copropriétés
  > 15 ans, calendrier échelonné jusqu'aux petites copropriétés (2025).
- **Interdiction progressive de location** des logements classés F/G.

Douleurs opérationnelles pour un syndic pro :
1. **Prioriser** quel immeuble traiter en premier (taille, passoires individuelles,
   procédures en cours, copropriétés aidées).
2. **Piloter la conformité** (DPE collectif, PPT, vote AG).
3. **Tracer** les travaux passés et les entreprises intervenantes — y compris via
   marchés publics lorsque la copropriété ou la commune a passé des contrats DECP.

La douleur est **réelle, récurrente et réglementairement poussée** — mais **déjà
largement adressée** par des logiciels syndic et des SaaS rénovation (§4). Le
croisement **RNIC × DPE × DECP** n'est pas un vide produit entier : c'est surtout
un **module** (traçabilité marchés publics + priorisation open data) à superposer
à des outils métier existants.

**Distinction vs 0009** : 0009 visait la prospection artisan (saturée, interdiction
démarchage depuis 01/07/2025). 0025 vise le **gestionnaire de parc** — usage licite.

---

## 2. Cible & qui paie

| Segment | Utilisateur | Payeur ? | Budget constaté |
|---|---|---|---|
| **Syndics professionnels** | Gestionnaires de portefeuille | Oui | ScanReno **490–790 €/mois HT** (Syndic Starter/Pro, 10–50 copros) — https://www.scanreno.fr/ (2026-06-21) ; Doctimmo **~1,50 €/lot/mois** — https://doctimmo.fr/syndic (2026-06-21) |
| **Bailleurs / gestionnaires de parc** | Direction patrimoine | Oui (mais…) | Go Rénove **PRO** (compte professionnel, export, analyse parc) — https://www.bdnb.io/services/gorenove/ (2026-06-21) — **gratuit/ public** |
| **Collectivités / ANAH** (OPAH) | Référents habitat | Budget public | Registre officiel + outils ANAH — https://www.anah.gouv.fr/ (2026-06-21) |
| **Artisans RGE** | — | Hors périmètre | Voir 0009 |

Utilisateur = payeur pour les syndics pro (sain). **Frein** : les syndics paient
déjà des suites métier ; un outil « open data only » doit se **bundler** (module
DECP) ou justifier un gain réglementaire non couvert.

**Verdict C2** : payeurs identifiés avec budgets réels, mais **WTP pour un
produit autonome** incertain face à ScanReno/LogicielSyndic.

---

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| **RNIC** | https://www.data.gouv.fr/datasets/registre-national-dimmatriculation-des-coproprietes | LO 2.0 | CSV ~430 Mo/trim. (délimiteur **virgule** depuis avr. 2026) | MàJ **17 juin 2026** ; quotidien depuis avr. 2026 | Pas de propriétaire ; renommage colonnes avr. 2026 ; annuaire public séparé |
| **Annuaire copropriétés** (ANAH) | https://www.registre-coproprietes.gouv.fr/ | Service public | Web | Continue | Consultation unitaire, pas batch portefeuille |
| **DPE logements** | https://data.ademe.fr/datasets/dpe03existant | LO 2.0 | API / dump PostgreSQL | ~350 k DPE/mois | Pas de lien RNIC natif ; jointure **adresse** |
| **DECP** | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | LO 2.0 | Parquet | ~quotidienne | MAPA < seuil absents ; `montant` ≠ dépense réelle |
| **Certifications RGE** | https://www.data.gouv.fr/dataservices/api-professionnels-rge | LO 2.0 | API REST | Régulière | Secteur rénovation uniquement |
| **BAN** | https://api-adresse.data.gouv.fr | LO 2.0 | REST | Continue | Normalisation adresse copropriété |

**Vérification quantifiée RNIC** (échantillon **100 001** lignes, fichier « nouveau
format colonnes », téléchargé 2026-06-21) :

| Indicateur | Résultat |
|---|---|
| Syndic **professionnel** | 76,4 % |
| **SIRET** syndic renseigné (14 car.) | 76,4 % (aligné sur pro) |
| Copropriétés **≥ 50 lots** | 48,5 % |
| Copropriétés **≥ 200 lots** | 11,5 % |

→ La jointure **RNIC × DECP par SIRET syndic** est **crédible** pour ~3/4 du parc.
La jointure **RNIC × DPE par adresse** reste le maillon faible (adresse de référence
≠ logements individuels).

[`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements & requêtes SQL traçables

| Indicateur | Jointure | SQL ? |
|---|---|---|
| Portefeuille par SIRET syndic | RNIC.siret_du_representant_legal | ✅ |
| Copropriétés ≥ N lots en procédure | RNIC.nombre_total_de_lots + champs procédure | ✅ |
| Lots F/G agrégés par adresse copro | RNIC.adresse × DPE (BAN) | ⚠️ moyen |
| Marchés rénovation liés au syndic | RNIC.siret × DECP.titulaire_id (CPV 45xx) | ✅ si syndic = titulaire ; sinon acheteur = commune |
| Titulaire RGE sur marché | DECP × API RGE | ✅ |

---

## 4. Existant / concurrence

**Verdict saturation : SATURÉ** sur le cœur « pilotage rénovation copropriété » ;
**espace étroit** sur le seul angle **DECP × portefeuille RNIC**.

### Produits ciblant explicitement les syndics (concurrents directs)

| Produit | URL | Recoupement seed | Prix (2026-06-21) |
|---|---|---|---|
| **ScanReno — offre Syndic** | https://www.scanreno.fr/ | Tableau de bord multi-copros, **PPT 10 ans**, DPE ADEME, convocations AG, aides MPR copropriété | **490 €/mois** (10 copros) ; **790 €/mois** (50 copros) |
| **LogicielSyndic** | https://logicielsyndic.fr/logiciel-syndic-professionnel | **Import RNIC par SIRET**, comptabilité, AG, travaux, benchmark charges | Sur devis ; essai gratuit |
| **Doctimmo Syndic** | https://doctimmo.fr/syndic | Conformité ELAN/Climat, DPE collectif, carnet entretien, pipeline travaux | **~1,50 €/lot/mois** |
| **Go Rénove PRO** | https://www.bdnb.io/services/gorenove/ | Analyse **parc de bâtiments**, DPE simulé, export, tableaux de bord | Compte PRO (service public CSTB) |

### Annuaires / consultation (gratuit, partiel)

| Produit | URL | Ce qu'il fait |
|---|---|---|
| **Annuaire copropriétés ANAH** | https://www.registre-coproprietes.gouv.fr/ | Recherche unitaire copropriété |
| **Le Comptoir de la Copropriété** | https://www.le-comptoir-de-la-copropriete.fr/annuaire | **619 000+** copros RNIC, recherche geo, gratuit |
| **Go Rénove particuliers** | https://www.bdnb.io/services/gorenove/ | Fiche bâtiment à l'adresse |

### Segment artisan (hors cible mais même données)

ThermoData, Thervy, MenuiserieAi — prospection F/G (cf. 0009, saturé).

**Ce que personne ne met en avant clairement** : croisement systématique **DECP**
(marchés travaux publics passés sur le territoire / par entreprise RGE) × **portefeuille
RNIC** pour audit de traçabilité. C'est un **module étroit**, pas un produit autonome
défendable — et peu de syndics achètent pour ce seul besoin.

---

## 5. Différenciation

**Faible.** ScanReno couvre déjà le triptyque réglementaire syndic (DPE + PPT + AG)
avec données ADEME. LogicielSyndic importe le RNIC par SIRET. Go Rénove PRO couvre
l'analyse de parc pour bailleurs.

Le seul angle résiduel :
- **Traçabilité DECP** : quels marchés de rénovation publics ont concerné des entreprises
  intervenant sur le territoire des copropriétés du portefeuille.
- **Priorisation open data** sans payer ScanReno — mais le coût ScanReno (490 €/mois
  pour 10 copros) ancre le marché bas.

Reproductible en **quelques semaines** par un éditeur syndic existant ou par un
intégrateur DECP (decp.info, marchespublics.ai).

---

## 6. Faisabilité & fiabilité technique

- **Architecture** : RNIC (CSV trimestriel, DuckDB) + DPE (API/dump) + DECP (Parquet)
  + géocodage BAN.
- **Conforme RAG(sens)/SQL(chiffres)** : nb lots, classes DPE agrégées, montants
  DECP = requêtes SQL traçables ; LLM limité aux explications réglementaires (PPT,
  DPE collectif, barèmes ANAH).
- **Point faible** : jointure RNIC ↔ DPE par adresse ( une copropriété = N logements
  avec DPE distincts). Approche honnête : agrégats par immeuble + fourchette, pas
  fiche logement individuelle sans consentement.
- **Point fort** : jointure RNIC ↔ DECP par **SIRET syndic** validée à **76,4 %**
  sur échantillon 100 k (2026-06-21).

---

## 7. Monétisation / impact

- **SaaS syndic autonome** : difficile (ScanReno + LogicielSyndic + Go Rénove).
- **Module B2B** vendu à un éditeur syndic ou à un cabinet conseil copropriété :
  plausible mais **petit TAM**.
- **Impact** : accélérer la rénovation copropriété — réel, mais les leviers
  réglementaires (DPE collectif 2026) créent déjà la demande ; l'open data seul
  n'accélère pas sans workflow métier (AG, PPT, compta).

---

## 8. Risques

- **Concurrence** : ScanReno a une offre Syndic explicite à 490 €/mois — barrière basse.
- **Internalisation** : ANAH/CSTB peuvent enrichir registre-coproprietes.gouv.fr ou
  Go Rénove (déjà BDNB + DPE).
- **Qualité jointure DPE** : sur-promesse sur le « nb passoires par copro » si adresses
  bruitées → risque réputationnel vis-à-vis du syndic.
- **DECP** : sémantique `montant` (cf. revue 0001) — ne pas présenter comme « dépense
  rénovation copro » sans disclaimer.
- **RGPD** : moindre que 0009 (pas de prospection occupants) ; usage gestionnaire
  licite.

Pas de point éliminatoire juridique (contrairement à 0009).

---

## 9. Effort MVP

Modéré :
1. Ingestion RNIC + index SIRET syndic + filtres (lots, procédure, commune).
2. Jointure DPE agrégée par adresse BAN (échantillon département pilote).
3. Jointure DECP titulaires CPV 45xx / 71xx sur communes du portefeuille.
4. Dashboard portefeuille : copros triées par « pression réglementaire » (SQL) +
   liste marchés DECP liés.
5. Traçabilité affichée sur chaque chiffre.

**Prérequis validation** : mesurer taux de jointure RNIC↔DPE sur 1 département
 avant scaling national.

---

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
| C8 | Maîtrise des risques | 2 | 4 | 8 |
| C9 | Monétisation / impact | 2 | 2 | 4 |
| | **Total** | | | **67 / 105** |

**Score /100** : 67 / 105 × 100 = **64**

Justification :
- **C1 = 4** : contrainte réglementaire DPE collectif 2026 + PPT = douleur forte ;
  pas 5 car workflows syndic déjà outillés.
- **C2 = 3** : syndics paient (ScanReno, Doctimmo) ; pas 4 car WTP pour couche
  open data seule faible.
- **C3 = 4** : RNIC riche, SIRET 76 % pro, DPE/DECP ouverts ; pas 5 car jointure
  adresse DPE fragile.
- **C4 = 2** : ScanReno Syndic + LogicielSyndic + Go Rénove PRO occupent le cœur ;
  seul l'angle DECP reste partiellement libre.
- **C5 = 2** : module DECP copiable ; données communes Etalab.
- **C6 = 4** : SQL traçable ; jointure adresse = réserve.
- **C7 = 3** : ingestion lourde (430 Mo RNIC + DPE national).
- **C8 = 4** : pas de risque démarchage ; risques concurrence/modeste.
- **C9 = 2** : revenu incertain ; impact indirect.

---

## 11. Verdict & décision

🔁 **À retravailler** (score **64/100**).

L'idée corrige deux faiblesses de **0009** (légalité, cible B2B syndic) et s'appuie
sur des **données vérifiées** (RNIC ouvert, SIRET syndic ~76 % sur pro). Mais le
**cœur métier** (DPE + PPT + pilotage portefeuille copropriété) est **déjà vendu**
par ScanReno (490 €/mois), LogicielSyndic (import RNIC) et Go Rénove PRO.

Le seul créneau crédible : **module DECP** de traçabilité des marchés travaux ×
portefeuille RNIC — à vendre en **white-label** à un éditeur syndic, pas en SaaS
autonome.

**Prochaine étape concrète** :
1. Mesurer jointure RNIC↔DPE sur 1 département (taux de match adresse).
2. Si > 60 % : prototyper le **seul** écran différenciant (DECP × portefeuille SIRET).
3. Sinon : ❌ Écartée ou fusionner comme annexe technique de 0001 (DECP).
