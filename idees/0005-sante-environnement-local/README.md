# Santé-environnement locale (eau / air)

- **ID** : 0005
- **Statut** : ❌ Écartée
- **Score** : — / 100 (écartée : saturation + risque sanitaire)
- **Dernière mise à jour** : 2026-06-20
- **Pitch (1 phrase)** : Informer chaque habitant sur la qualité de son eau/air
  par commune, avec pédagogie et alertes.

---

## 1. Problème / douleur
Réelle, mais marché déjà couvert et risque de positionnement sur du conseil
santé.

## 4. Existant / concurrence (saturé)
- Recosanté (air, pollens, UV, baignade, radon) —
  https://www.data.gouv.fr/reuses/recosante-un-service-public-numerique-sur-la-qualite-de-lair
- EauPotable.net, EauduRobinet.fr, Dans Mon Eau (Générations Futures + Data for
  Good), mon-eau.com (30+ jeux, score /100, API publique).
  (Consultés 2026-06-20.)

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0005-sante-environnement-local` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `environmental-data-fr` — Environnement & risques FR

Fichier : [`catalogue-saas/vendors/environmental-data-fr.json`](../../catalogue-saas/vendors/environmental-data-fr.json) (20 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `atmo-france` | Atmo France | FR | strong | partial |
| `hub-eau` | Hub'Eau | FR | strong | partial |
| `inpn` | INPN (OFB) | FR | strong | partial |
| `brgm-infoterre` | BRGM InfoTerre | FR | strong | partial |
| `georisques-api` | Géorisques | FR | strong | partial |
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

## 11. Verdict & décision
❌ **Écartée.** Arrivée tardive sur un créneau dense, avec un risque éliminatoire
(santé). Pas de différenciation crédible identifiée.
