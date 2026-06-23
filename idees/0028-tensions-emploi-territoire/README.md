# Tensions emploi par territoire (France Travail × SIRENE × FiLoSoFi)

- **ID** : 0028
- **Statut** : 💡 Capturée
- **Score** : — / 100 (à analyser)
- **Dernière mise à jour** : 2026-06-21
- **Pitch (1 phrase)** : Croiser les données France Travail (demandeurs d'emploi,
  tensions par métier), la structure économique locale (SIRENE/NAF) et le pouvoir
  d'achat (FiLoSoFi) pour aider franchises et recruteurs à choisir un territoire —
  extension emploi de [0006](../0006-assistant-implantation-commerciale/).

---

## 1. Problème / douleur

Un franchiseur ou un recruteur qui ouvre un point de vente ou un site de production
doit savoir :
- s'il **trouvera des candidats** (tension par métier/territoire),
- si le **pouvoir d'achat** local soutient l'activité,
- quelle est la **densité d'établissements** concurrents (SIRENE).

Les données existent (France Travail, INSEE, SIRENE) mais ne sont pas croisées dans
un outil accessible aux **non-experts**. La douleur est réelle pour les réseaux
de franchise et les cabinets RH territoriaux — segment déjà partiellement servi
par la CCI et les outils de géomarketing (0006).

## 2. Cible & qui paie

| Segment | Besoin | Payeur |
|---|---|---|
| **Franchiseurs** (retail, services) | Où recruter + où vendre | Franchiseur (budget expansion) |
| **Cabinets de recrutement régionaux** | Cartographie tensions métiers | Abonnement B2B |
| **CCI / France Travail** | Orientation — outils publics existants | Public |
| **Indépendants** | Même besoin que 0006 | Budget faible |

Payeur plausible : **franchiseur** en phase d'expansion (déjà client Geomarket/Smappen
pour l'implantation — bundling possible).

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| **API Marché du travail** | https://www.data.gouv.fr/dataservices/api-marche-du-travail | LO 2.0 | REST JSON | Réf. déc. 2025 | Compte OAuth France Travail |
| **API Accès à l'emploi** | https://www.data.gouv.fr/dataservices/api-acces-a-lemploi-des-demandeurs-demploi | LO 2.0 | REST JSON | Réf. déc. 2025 | Par métier ROME |
| **API Informations emploi territoire** | https://www.data.gouv.fr/dataservices/api-informations-sur-lemploi-dans-un-territoire | LO 2.0 | REST JSON | Réf. déc. 2025 | Établissements, salariés |
| **SIRENE** (établissements par NAF) | https://www.data.gouv.fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret | LO 2.0 | CSV/API | Mensuelle | Géoloc via jeu statistique séparé |
| **FiLoSoFi IRIS** | https://www.insee.fr/fr/statistiques/8229323 | LO (Insee) | CSV | Revenus 2021 | Communes ≥ 5 000 hab. |
| **Nomenclature ROME / NAF** | Référentiels INSEE / FT | LO | CSV | Référentiel | Mapping métier ↔ secteur = heuristique |

**Vérification** (2026-06-21) : les 3 API France Travail sont référencées sur
data.gouv.fr (MàJ déc. 2025) ; accès nécessite inscription portail France Travail
(hors test sans credentials). SIRENE et FiLoSoFi : dumps ouverts confirmés.

[`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements

| Indicateur | Sources | Clé |
|---|---|---|
| Tension recrutement métier X en commune Y | API Marché du travail + ROME | Code commune + code ROME |
| Pouvoir d'achat vs offre commerciale | FiLoSoFi × SIRENE (NAF commerce) | IRIS / commune |
| Dynamique emploi vs créations entreprises | API emploi territoire × SIRENE créations | Commune |
| « Score territoire » franchise | Pondération SQL (tension basse + revenus + concurrence) | Composite traçable |

## 4. Existant / concurrence (première passe)

- **Smappen, Geomarket, Data-B** (0006) : démo + concurrence, pas tension emploi FT
- **France Travail / Mes Services Locaux** : consultation publique partielle
- **CCI études de marché** : prestation humaine, pas self-service
- **À creuser** : APIs France Travail déjà intégrées dans outils RH (Talentsoft, etc.)

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0028-tensions-emploi-territoire` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `territorial-analytics` — Analytics territoriales

Fichier : [`catalogue-saas/vendors/territorial-analytics.json`](../../catalogue-saas/vendors/territorial-analytics.json) (18 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `datagouv` | data.gouv.fr | FR | strong | verified |
| `georisques` | Géorisques | FR | strong | verified |
| `ofgl` | OFGL Observatoire | FR | strong | verified |
| `cartes-gouv` | Géoportail / cartes.gouv.fr | FR | strong | verified |
| `data-gov-uk` | data.gov.uk | GB | absent | partial |
| `ons-uk` | Office for National Statistics (UK) | GB | absent | partial |
| `eurostat-regional` | Eurostat — Regional Statistics | EU | partial | partial |
| `carto-territorial` | CARTO | ES | partial | partial |
| `smappen` | Smappen | FR | strong | partial |
| `geomarket` | Geomarket | FR | strong | partial |
| `data-b` | Data-B | FR | strong | partial |
| `vigicite` | VigiCité | FR | strong | partial |
| … | _+6 autres_ | | | |

#### Segment `hr-talent-ai` — RH & talent IA

Fichier : [`catalogue-saas/vendors/hr-talent-ai.json`](../../catalogue-saas/vendors/hr-talent-ai.json) (14 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `paradox-olivia` | Paradox (Olivia) | US | partial | partial |
| `eightfold` | Eightfold AI | US | partial | partial |
| `hirevue` | HireVue | US | partial | partial |
| `textio` | Textio | US | partial | partial |
| `greenhouse` | Greenhouse | US | partial | partial |
| `talentsoft` | Talentsoft (Cegid) | FR | strong | partial |
| `lucca` | Lucca | FR | strong | partial |
| `jobteaser` | JobTeaser | FR | strong | partial |
| `beetween` | Beetween | FR | strong | partial |
| `flatchr` | Flatchr | FR | strong | partial |
| `welcom-hr` | Welcome to the Jungle (ATS) | FR | strong | partial |
| `people-spheres` | PeopleSpheres | FR | strong | partial |
| … | _+2 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment territorial-analytics
```

<!-- catalogue-saas-end -->
## 6. Faisabilité & fiabilité technique

- Ingestion périodique APIs FT (après OAuth) + stock SIRENE + FiLoSoFi → DuckDB.
- Tous les indicateurs chiffrés = **SQL** avec source API + date d'appel.
- Dépendance **credentials France Travail** : risque de changement API / quotas.

## 11. Verdict & décision

💡 **Capturée** — différenciation vs 0006 par la **couche emploi** (France Travail),
mais marché géomarketing déjà saturé. Crédible comme **module** d'un outil
d'implantation existant plutôt que produit autonome.

**Prochaine étape** : obtenir accès API France Travail (sandbox) et tester 1 requête
« tension métier commerce de détail » × commune pilote.
