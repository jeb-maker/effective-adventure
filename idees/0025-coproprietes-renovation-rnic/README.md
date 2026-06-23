# Pilotage rénovation des copropriétés (RNIC × DPE × DECP)

- **ID** : 0025
- **Statut** : 💡 Capturée
- **Score** : — / 100 (à analyser)
- **Dernière mise à jour** : 2026-06-21
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

## 4. Existant / concurrence (première passe)

- **Go Rénove / BDNB** (CSTB) : analyse de parc pour collectivités/bailleurs —
  service public gratuit — https://www.bdnb.io/services/gorenove/ (consulté 2026-06-21)
- **ThermoData, Thervy, ScanReno** : prospection artisans, pas pilotage syndic
- **Logiciels syndic** (EGIDE, Comptoir du Conseil, etc.) : gestion comptable,
  pas de croisement open data RNIC×DPE×DECP identifié — **à creuser en analyse**

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0025-coproprietes-renovation-rnic` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `energy-buildings-fr` — Bâtiments & énergie FR

Fichier : [`catalogue-saas/vendors/energy-buildings-fr.json`](../../catalogue-saas/vendors/energy-buildings-fr.json) (9 entrées)

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

#### Segment `real-estate-proptech` — Immobilier & proptech

Fichier : [`catalogue-saas/vendors/real-estate-proptech.json`](../../catalogue-saas/vendors/real-estate-proptech.json) (5 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `costar` | CoStar | US | partial | partial |
| `yardi` | Yardi | US | partial | partial |
| `procore` | Procore | US | partial | partial |
| `matera` | Matera | FR | strong | partial |
| `pricehubble` | PriceHubble | CH | partial | partial |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment energy-buildings-fr
```

<!-- catalogue-saas-end -->
## 6. Faisabilité & fiabilité technique

- Ingestion RNIC trimestrielle + flux DPE + DECP → DuckDB/PostgreSQL.
- Jointure principale : **adresse normalisée** (BAN) entre RNIC et DPE — point
  faible si adresse syndic ≠ adresse lots.
- Tous les chiffres (nb passoires, montants DECP) via **SQL traçable** ; LLM pour
  expliquer réglementation copropriété / aides uniquement.

## 11. Verdict & décision

💡 **Capturée** — extension naturelle de 0009 avec angle B2B syndics et sources
vérifiées (RNIC ouvert, volumétrie confirmée). À analyser : concurrence Go Rénove
côté bailleurs, willingness-to-pay des syndics, taux de complétude SIRET syndic
dans le RNIC.

**Prochaine étape** : requête SQL sur échantillon RNIC + DPE pour mesurer le taux
de jointure adresse réelle avant scoring complet.
