# Santé-environnement locale (eau / air)

- **ID** : 0005
- **Statut** : ❌ Écartée
- **Score** : 44 / 100
- **Dernière mise à jour** : 2026-06-23
- **Révision critique** : voir [`revue.md`](revue.md) — écart **confirmé** et
  renforcé (score posé à **44/100**, < 55, + critère éliminatoire sanitaire).
  L'audit adversarial ajoute deux concurrents majeurs : la **carte officielle du
  Ministère de la Santé** sur l'eau du robinet (mise en avant le 19/02/2026) et la
  **carte interactive UFC-Que Choisir** (50 contaminants, PFAS).
- **Pitch (1 phrase)** : Informer chaque habitant sur la qualité de son eau/air
  par commune, avec pédagogie et alertes.

---

## 1. Problème / douleur
Réelle, mais marché déjà couvert et risque de positionnement sur du conseil
santé.

## 4. Existant / concurrence (saturé)

> Cartographie B (consultée 2026-06-23). Les services publics numériques couvrent déjà air, eau et environnement local.

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **Recosanté** | https://recosante.beta.gouv.fr/ | Service public numérique air, pollens, UV, baignade, radon |
| **Hub'Eau** | https://hub-eau.fr/ | API eau potable, rivières, nappes (Sandre) |
| **Atmo France — indices qualité air** | https://www.atmo-france.org/ | Prévisions et historique par commune |
| **Géorisques — radon / ICPE** | https://www.georisques.gouv.fr/ | Risques environnementaux à l'adresse |

### Réutilisations data.gouv

| Acteur | URL | Rôle |
|---|---|---|
| **Recosanté (fiche réutilisation)** | https://www.data.gouv.fr/reuses/recosante-un-service-public-numerique-sur-la-qualite-de-lair | Agrégation open data santé-environnement |
| **Dans Mon Eau** | https://www.data.gouv.fr/reuses/dans-mon-eau | Qualité eau potable par commune (Générations Futures) |

### Produits commerciaux / bricolage

- EauPotable.net, EauduRobinet.fr, Dans Mon Eau (Générations Futures + Data for
  Good), mon-eau.com (30+ jeux, score /100, API publique).
  (Consultés 2026-06-23.)

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0005-sante-environnement-local` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `environmental-data-fr` — Environnement & risques FR

Fichier : [`catalogue-saas/vendors/environmental-data-fr.json`](../../catalogue-saas/vendors/environmental-data-fr.json) (20 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `atmo-france` | Atmo France | FR | strong | verified |
| `hub-eau` | Hub'Eau | FR | strong | verified |
| `inpn` | INPN (OFB) | FR | strong | partial |
| `brgm-infoterre` | BRGM InfoTerre | FR | strong | partial |
| `georisques-api` | Géorisques | FR | strong | verified |
| `uk-environment-agency` | UK Environment Agency — Open Data | GB | absent | partial |
| `eea-europe` | European Environment Agency | EU | partial | partial |
| `copernicus-land` | Copernicus Land Monitoring | EU | partial | partial |
| `us-epa-envirofacts` | US EPA Envirofacts | US | absent | partial |
| `sandre` | Sandre | FR | strong | partial |
| `drias-climat` | DRIAS — Futurs climatiques | FR | strong | partial |
| `basol` | BASOL — Sites et sols pollués | FR | strong | partial |
| … | _+8 autres_ | | | |

#### Segment `public-health-territory-fr` — Santé territoriale FR

Fichier : [`catalogue-saas/vendors/public-health-territory-fr.json`](../../catalogue-saas/vendors/public-health-territory-fr.json) (18 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `ameli-open-data` | Assurance Maladie — open data | FR | strong | partial |
| `santepubliquefrance` | Santé publique France — data | FR | strong | partial |
| `keldoc` | KelDoc | FR | strong | partial |
| `doctolib` | Doctolib | FR | strong | partial |
| `drees` | DREES | FR | strong | partial |
| `nhs-digital-open-data` | NHS Digital — Open Data | GB | absent | partial |
| `cdc-places` | CDC PLACES | US | absent | partial |
| `who-health-observatory` | WHO Global Health Observatory | CH | unknown | partial |
| `healthdata-gov` | HealthData.gov (US) | US | absent | partial |
| `cartosante` | CartoSanté (Atlas Santé) | FR | strong | partial |
| `annuaire-sante` | Annuaire Santé (ANS) | FR | strong | partial |
| `maiia` | Maiia | FR | strong | partial |
| … | _+6 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment environmental-data-fr
```

<!-- catalogue-saas-end -->
## 8. Risques
Saturation forte **et** risque sanitaire/juridique (interprétation de mesures de
santé). Données via Hub'Eau/SISE-Eaux déjà très exploitées.

## 10. Scoring

> Tableau posé par la revue critique (la fiche écartait sans note). Notes adversariales.

| # | Critère | Poids | Note (1-5) | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 9 | Préoccupation réelle (eau/air) mais besoin d'information, pas douleur payante. |
| C2 | Cible solvable (qui paie) | 3 | 1 | 3 | Habitant ne paie pas ; alternatives gratuites (État, UFC-QC) ; pas de payeur B2B. |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 | Hub'Eau/Atmo/SISE-Eaux ouvertes, prêtes et SQL-ables. |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 | Saturé : État (eau + air) + UFC-Que Choisir + Recosanté + réutilisations. |
| C5 | Différenciation défendable | 2 | 1 | 2 | Aucune ; mêmes données publiques, caution moindre qu'État/UFC-QC. |
| C6 | Faisabilité & fiabilité technique | 2 | 3 | 6 | Données SQL-ables, mais interprétation sanitaire = risque (pas un simple résumé). |
| C7 | Facilité du MVP | 2 | 4 | 8 | MVP technique simple (données prêtes) — ce qui nourrit la saturation. |
| C8 | Maîtrise des risques | 2 | 1 | 2 | Risque sanitaire/juridique quasi éliminatoire + saturation. |
| C9 | Monétisation / impact | 2 | 1 | 2 | Pas de revenu (gratuit citoyen) ; impact déjà porté par l'État et l'UFC-QC. |
| | **Total** | | | **46 / 105** | |

**Score /100** : 46 / 105 × 100 = **44**

## 11. Verdict & décision
❌ **Écartée.** Arrivée tardive sur un créneau dense, avec un risque éliminatoire
(santé). Le pitch (eau **et** air) affronte des services publics gratuits — la
**carte officielle du Ministère de la Santé** sur l'eau du robinet (mise en avant
le 19/02/2026), **Recosanté** (air) — **et** la **carte UFC-Que Choisir**
(50 contaminants, PFAS), tous consultés 2026-06-23. Score reconstruit **44/100**
(< 55) **et** critère éliminatoire sanitaire → écart confirmé. Pas de
différenciation crédible identifiée.
