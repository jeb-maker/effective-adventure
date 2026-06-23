# Exposition climat/risques d'un portefeuille d'actifs (B2B assurance/immo)

- **ID** : 0024
- **Statut** : ❌ Écartée
- **Score** : 54 / 100
- **Dernière mise à jour** : 2026-06-21
- **Pitch (1 phrase)** : Outil B2B pour scorer en masse l'exposition d'un portefeuille de biens (batch d'adresses) aux risques naturels et climatiques (inondation, RGA, submersion, sécheresse, sismique) via Géorisques + données climat, pour tarification, provisionnement et reporting TCFD/CSRD — distinct du diagnostic unitaire grand public (0011).

---

## 1. Problème / douleur

Les assureurs, foncières, gestionnaires d'actifs et banques doivent **quantifier l'exposition climatique de centaines à millions de biens** pour trois besoins convergents :

1. **Pilotage de portefeuille** — identifier les actifs les plus exposés aux aléas physiques (inondation, retrait-gonflement des argiles, submersion, sécheresse, sismique) afin de prioriser prévention, CapEx et arbitrages d'investissement.
2. **Tarification / provisionnement** — la sinistralité Cat Nat augmente structurellement : France Assureurs estime le coût cumulé des sinistres climatiques à **143 Md€ d'ici 2050** contre 69 Md€ sur 1989–2019 (source citée par Fonciris, consulté 2026-06-20 : https://fonciris.fr/guide/changement-climatique-immobilier-risques). Odealim projette une hausse du coût du sinistre climatique de **40 à 120 %** vs 2019–2023 (consulté 2026-06-20 : https://monimmeuble.com/actualite/assurance-catastrophe-naturelle-ce-qui-change-avec-le-climat).
3. **Reporting réglementaire** — CSRD (norme ESRS E1), stress tests BCE, TCFD et taxonomie UE imposent une analyse de **double matérialité** incluant les risques physiques à granularité actif, avec scénarios multi-horizons (2030, 2050).

**La douleur est réelle, récurrente et réglementairement poussée** — mais elle est déjà adressée par une filière B2B mature (voir §4). Le seed suppose un « vide » sur le batch portefeuille ; la recherche montre que ce vide **n'existe pas** en France en 2026.

**Distinction vs 0011** : 0011 cible la synthèse **unitaire** grand public / notaires / ERP à l'adresse (saturée par Errial gratuit + risques-adresse.fr). 0024 cible le **batch portefeuille** B2B institutionnel — créneau que 0011 identifiait comme seul repositionnement possible, mais qui est lui aussi déjà occupé.

---

## 2. Cible & qui paie

| Segment | Utilisateur | Payeur ? | Budget constaté |
|---|---|---|---|
| **Assureurs IARD / MRH** | Actuariat, souscription, prévention | Oui | **Addactis Property Risk Intelligence** (ex-NamR) déployé chez **Suravenir Assurances** et **Thélem** ; NamR revendique **35 % du marché MRH français** via le partenariat Addactis (consulté 2026-06-20 : https://www.addactis.com/fr/blog/thelem-deploie-insurance-smart-home-pricing , https://www.addactis.com/fr/blog/addactis-acquiert-assurance-namr/) |
| **Banques / crédit immo** | Risque, ESG, retail | Oui | NamR : simulateurs adoptés par **« tous les établissements bancaires de premier rang »**, **+100 000 utilisateurs** (consulté 2026-06-20 : https://namr.com/fr/donnees-risques-climatiques/) |
| **Foncières / asset managers** | Asset management, due diligence | Oui | Deepki, Jupiter, Munich Re, Climate X vendent explicitement l'évaluation portefeuille (§4) ; AXA IM analyse systématiquement les risques physiques en due diligence (consulté 2026-06-20 : https://www.adaptation-changement-climatique.gouv.fr/s-inspirer/projetotheque/axa-experimente-une-analyse-systematique-des-actifs-immobiliers-aux) |
| **Consultants ESG / CSRD** | Analystes durabilité | Oui (refacturation) | Jupiter + Axionable en France ; Mitiga Disclose pour ESRS E1 |

**Utilisateur ≠ payeur** dans les cas où l'outil est intégré en white-label par un intégrateur (Callendar CED, Addactis). Les budgets existent et sont **déjà captés** par des acteurs installés — pas par un agrégateur Géorisques générique.

---

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| API Géorisques (agrégateur + endpoints) | https://www.data.gouv.fr/dataservices/api-georisques · doc : https://www.georisques.gouv.fr/doc-api · CGU : https://www.georisques.gouv.fr/cgu | Licence Ouverte 2.0 | REST JSON ; rapport PDF via `/api/v1/resultats_rapport_risque` | Continue (BRGM) | **Pas d'endpoint batch** : 1 requête/adresse ; quota documenté **10 req/s/IP** (consulté 2026-06-20 : https://diagfrance.com/outils-materiel-diagnostiqueur-guide/apis-open-data-diagnostic) ; maille variable (commune vs adresse selon risque) ; auth token Cerbère pour v2 |
| Retrait-gonflement argiles (RGA) — carte exposition 2026 | https://www.georisques.gouv.fr/donnees/bases-de-donnees/retrait-gonflement-des-argiles-version-2026 · data.gouv : https://www.data.gouv.fr/datasets/carte-des-risques-retrait-gonflement-des-argiles-2026 | LO 2.0 | Shapefile (RGF93) / PMTiles | Millésime **2026** (arrêté 9 janv. 2026, applicable ventes terrains à compter 01/07/2026) | **Aléa cartographique**, pas diagnostic de sol ; hors Paris intra-muros ; pas de projection climatique intégrée |
| TRI inondation (Directive Inondation v2, millésime 2020) | https://www.georisques.gouv.fr/donnees/bases-de-donnees/zonages-inondation-rapportage-2020 · API : `/api/v1/tri_zonage` · WMS : https://georisques.gouv.fr/services/di_fxx_2020 | LO 2.0 | Shapefile par département ; API JSON par territoire | Rapportage **2020** ; réévaluation tous les **6 ans** | Couverture incomplète du ruissellement pluvial ; zones hors TRI = trou d'information |
| DRIAS — projections climatiques | https://www.data.gouv.fr/datasets/drias-projections-climatiques-pour-ladaptation-de-nos-societes · portail : https://www.drias-climat.fr | LO (Météo-France) | NetCDF / CSV ; grille ~8 km (SAFRAN) | DRIAS-2020 : scénarios RCP 2.6/4.5/8.5 ; TRACC intégrée | **Compte personnel requis** pour téléchargement ; **pas d'API REST documentée** ; maille 8–12 km ≠ parcelle ; usage prospectif exige expertise climatologique |
| Base Adresse Nationale (géocodage batch) | https://api-adresse.data.gouv.fr | LO 2.0 | REST JSON | Continue (IGN/DINUM) | Précision d'appariement variable ; 50 req/s/IP documenté |
| GASPAR / CatNat / PPR | Endpoints `/api/v1/gaspar/*`, `/api/v1/ppr`, `/api/v1/catnat` | LO 2.0 | JSON | À chaque arrêté | Maille souvent communale ; historique ≠ projection |
| Zonage sismique | `/api/v1/zonage_sismique` | LO 2.0 | JSON | Réglementaire (décret 2010-1255) | Zones 1–5, maille communale |
| **Cartes de bruit** (exposition nuisance) | https://www.data.gouv.fr/datasets/zones-de-bruit-des-cartes-de-bruit-strategiques-4eme-echeance-1 | LO 2.0 | Shapefile | Variable (vérifié 2026-06-21) | Couverture inégale ; complément « qualité de vie » du risque physique |
| **Copernicus Land** (occupation sols, végétation) | https://land.copernicus.eu/ | UE gratuit | Raster/API | Continu | Résolution ~10–100 m ; expertise SIG ; complément DRIAS |

> [`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements envisagés

| Croisement | Apport vs Géorisques seul | Limite |
|---|---|---|
| Géorisques × DRIAS × Copernicus | Scénario climat + aléa actuel + évolution occupation sols | DRIAS sans API REST ; maille 8 km |
| Géorisques × cartes bruit | Nuisance sonore comme risque « qualitatif » du portefeuille | Couverture bruit partielle |
| Batch BAN × endpoints Géorisques | Pipeline technique identique — la valeur est le **modèle de vulnérabilité**, pas le croisement brut | Quota 10 req/s |

**Synthèse données** : excellent pour l'**exposition réglementaire actuelle** (Géorisques + TRI + RGA en spatial join local). **Insuffisant seul** pour un scoring prospectif crédible horizon 2050 (TCFD/CSRD) : il faut croiser DRIAS + modèles de vulnérabilité bâti — ce que font déjà Callendar, NamR, Deepki, etc.

---

## 4. Existant / concurrence

**Verdict de saturation : SATURÉ** sur le créneau « scoring portefeuille B2B risques physiques/climat France ». L'espace libre se limite à des niches verticales très étroites (ex. un seul aléa, un seul type d'actif non résidentiel) — non démontrées.

### Concurrents directs B2B portefeuille / batch (≥5, tous vérifiés 2026-06-20)

| Acteur | URL | Ce qu'il fait | Ce qu'il ne fait pas / limites |
|---|---|---|---|
| **Callendar** | https://www.callendar.tech/en/clients | CED white-label + **API** pour banques/assurance/immo ; projections locales alignées **TRACC** ; apps grand public + offre B2B institutionnelle | Positionné ingénierie/adaptation plus que reporting financier pur (consulté 2026-06-20 : https://www.callendar.tech/en/post/compare-climate-data-providers-risk-assessment-services-adaptation) |
| **NamR** (+ **Addactis** depuis mai 2025) | https://namr.com/fr/donnees-risques-climatiques/ · https://www.addactis.com/fr/voir-nos-solutions/property-risk-intelligence/ | Base climatique **géolocalisée à l'adresse**, **100 % logements résidentiels** ; scoring inondation/RGA/chaleur ; simulateurs banques ; **reporting CSRD/ESRS E1** ; portefeuille MRH via Addactis (36 M bâtiments) | Focus résidentiel ; modèles propriétaires opaques ; rachat NamR assurance par Addactis renforce le verrou |
| **Deepki** | https://www.deepki.com/fr/solutions/finance/ · https://www.deepki.com/fr/blog/nouveautes-produit-deepki-printemps-2024/ | Module **Résilience Climatique** : exposition + vulnérabilité portefeuille, projections intégrées, reporting Taxonomie/TCFD | SaaS ESG global (énergie + climat) ; prix enterprise non public |
| **Jupiter Intelligence** (ClimateScore Global) | https://www.jupiterintel.com/solutions/portfolio-asset-management · partenariat France : https://www.jupiterintel.com/blog/press-release-jupiter-partners-with-axionable-in-france-to-provide-customers-with-leading-climate-data-and-analytics | Analyse physique **portefeuille entier**, Compliance Hub **CSRD ESRS E1**, REST API, résolution 90 m | Modèles propriétaires mondiaux ; dépendance licence enterprise |
| **Mitiga Solutions** (EarthScan / Disclose) | https://www.mitigasolutions.com/solutions/portfolio-assessment · https://www.mitigasolutions.com/disclose | Upload CSV portefeuille → rapport **ESRS E1 / IFRS S2** automatisé ; milliers d'actifs ; API | Modèles globaux ; moins ancré données réglementaires françaises brutes |
| **Climate X** (Spectra) | https://www.climate-x.com/spectra · marché France : https://www.climate-x.com/articles/industry/navigating-the-real-estate-crisis-in-france | Upload portefeuille par code postal ; **climate-adjusted VaR** ; TCFD, EU Taxonomy, CRREM | UK-based ; données France via modèles globaux |
| **Munich Re** (Location Risk Intelligence) | https://www.munichre.com/rmp/en/products/location-risk-intelligence.item-bf839e268fa0a1f926452c1e1097410b.html · Reporting Edition : https://www.munichre.com/rmp/en/products/location-risk-intelligence/reporting-edition.html | Upload portefeuille ; scoring multi-aléa ; **Reporting Edition CSRD/TCFD/ISSB** ; REST API (plan Enterprise) | Licence SaaS coûteuse ; modèle réassureur |
| **AXA Climate** | https://www.axa.com/fr/engagements/axa-climate | Outils d'identification risques climat/nature **à 250 m** pour tout actif mondial ; conseil + data pour finance | Intégré écosystème AXA ; commercial B2B conseil |
| **Earthian AI** | https://www.earthianai.com/fr/solutions/real-estate | Scoring climatique **portefeuille** (Lucid Climate-0) ; intégration ARGUS/Yardi/eFront | Modèles IA propriétaires ; positionnement global |
| **Fonciris API** | https://fonciris.fr/fonctionnalites · https://www.clarimmo.eu/api-docs | API REST risques (inondation, argile, sismique, CatNat) par adresse ; plan Pro **79 €/mois** avec API | Plutôt PME pro / investisseurs ; pas institutionnel pur mais **déjà batchable via API** |

### Acteurs CSRD / immobilier institutionnel (complémentaires mais couvrant le besoin reporting)

| Acteur | URL | Rôle |
|---|---|---|
| **Bat-ADAPT / R4RE** (OID) | https://o-immobilierdurable.fr/lobservatoire-de-limmobilier-durable-vous-presente-ses-outils-bat-adapt/ · référentiel : https://resources.r4re.resilience-for-real-estate.com/documentation/batadapt_referentiel.pdf | Diagnostic résilience bâtiment ; cartographie risques physiques portefeuille ; compatible Taxonomie/TCFD |
| **ThinkCities** | https://urbanthink.eu/gestionnaires-actifs-immobiliers | Cartographie risques + reporting CSRD pour gestionnaires d'actifs publics/privés |
| **Cushman & Wakefield** | https://www.cushmanwakefield.com/fr-fr/france/insights/anticiper-les-risques-climatiques | Audit vulnérabilité portefeuille multi-actifs (conseil, pas SaaS self-service) |

### Commoditisation technique (barrière d'entrée quasi nulle)

- **Apify Géorisques scraper** : rapport structuré par adresse en masse à **0,005 $/adresse** (consulté 2026-06-20 : https://apify.com/dltik/georisques-fr-scraper/api) — le « batch Géorisques » est un produit à la carte.
- **Apify géocodage BAN bulk** : **0,02 $/1000 adresses** (consulté 2026-06-20 : https://apify.com/nlp_data_lni/fr-ign-geocodage).

### Éléments du seed non confirmés comme concurrents

| Élément seed | Statut recherche 2026-06-20 |
|---|---|
| **B808** | **Non identifié** — aucun acteur/produit « B808 » risque climatique immobilier trouvé (recherche web sans résultat). Référence interne ou erreur de nom — **à clarifier**. |
| **Cartofriches** | **Non concurrent** — inventaire national de friches (Cerema) pour reconversion foncière ; croisement risques dans UrbanSIMUL pour collectivités, pas scoring portefeuille B2B assurance/immo (consulté 2026-06-20 : https://www.cerema.fr/fr/actualites/cartofriches-pres-10000-sites-friches-repertories). |
| **Géorisques API en masse** | Pas d'endpoint officiel batch ; boucle client ou téléchargement shapefiles — déjà packagé par Apify, Fonciris, ATerraData (0011). |

### Où reste-t-il (marginalement) de l'espace ?

À ce stade, **aucun créneau crédible identifié** pour un nouvel entrant « Géorisques + DRIAS en batch » :

- Le besoin **réglementaire actuel** (ERP, zonages PPRI/TRI/RGA) est couvert par l'API publique + Errial (0011) et les APIs tierces.
- Le besoin **prospectif portefeuille** (CSRD, tarification) est couvert par NamR/Addactis, Callendar, Deepki, Jupiter, Munich Re, Mitiga, Climate X.
- Un positionnement « open data pur, moins cher » se heurte à la **commoditisation** (Apify 0,005 $/adresse) et à l'exigence d'**auditabilité** des acheteurs institutionnels (modèles validés, pas simple spatial join).

---

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0024-risque-climat-actifs` — segments liés pour benchmark concurrence structuré.
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

#### Segment `insurance-insurtech` — Assurance & insurtech

Fichier : [`catalogue-saas/vendors/insurance-insurtech.json`](../../catalogue-saas/vendors/insurance-insurtech.json) (19 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `guidewire` | Guidewire | US | partial | partial |
| `duck-creek` | Duck Creek Technologies | US | partial | partial |
| `lemonade` | Lemonade | unknown | unknown | partial |
| `coalition` | Coalition | US | partial | partial |
| `shift-technology` | Shift Technology | FR | partial | partial |
| `akur8` | Akur8 | FR | strong | partial |
| `wakam` | Wakam | FR | strong | partial |
| `qover` | Qover | BE | partial | partial |
| `luko` | Luko (Allianz Direct) | FR | strong | partial |
| `alan` | Alan | FR | strong | partial |
| `wefox` | wefox | DE | partial | partial |
| `zelros` | Zelros | FR | strong | partial |
| … | _+7 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment environmental-data-fr
```

<!-- catalogue-saas-end -->
## 5. Différenciation

**Très faible, non défendable.**

1. **Même matière première** — Géorisques, TRI, RGA, DRIAS sont en LO 2.0 ; tout concurrent peut les ingérer.
2. **Batch triviallement reproductible** — BAN → boucle API ou spatial join PostGIS/DuckDB sur shapefiles ≈ un sprint technique ; Apify le vend déjà.
3. **Pas de modèle de vulnérabilité** — le seed se limite à l'exposition (aléa × localisation). Les acheteurs B2B (assureurs, banques) exigent **vulnérabilité bâti** (fondations, structure, étage, DPE) : NamR, Deepki, Callendar, Bat-ADAPT l'intègrent déjà.
4. **Pas de projection crédible sans R&D** — scorer horizon 2050 avec DRIAS seul (maille 8 km) sans modèle propriétaire = produit **non auditables** pour CSRD ; les leaders ont 4–6 ans d'avance (Callendar depuis 2019, NamR depuis 2017, Addactis+NamR depuis 2019).
5. **0011 → 0024 = repositionnement déjà occupé** — l'analyse 0011 recommandait le batch B2B prospectif comme seul angle de survie ; cette analyse montre que **Callendar et NamR y sont déjà**.

Seule différenciation théorique : « stack 100 % open data française, traçable, self-hosted pour mid-market » — mais Fonciris (79 €/mois + API) et Bat-ADAPT (secteur immo institutionnel) couvrent déjà une partie de ce positionnement, et le mid-market institutionnel achète plutôt via intégrateurs (Addactis, Axionable+Jupiter).

---

## 6. Faisabilité & fiabilité technique

### Architecture proposée (conforme RAG sens / SQL chiffres)

```
CSV portefeuille (adresses)
  → géocodage BAN (SQL/API traçable)
  → pour chaque actif :
      (A) spatial join local : RGA 2026, TRI 2020, PPRI (shapefiles LO)
      (B) API Géorisques : resultats_rapport_risque + endpoints détaillés
      (C) optionnel : extraction DRIAS grille 8 km → indicateurs prospectifs
  → table normalisée actif × aléa × classement × source × date
  → agrégation portefeuille (SQL : % exposé, concentration géo, top N actifs)
  → LLM : explication métier uniquement (RAG sur doc Géorisques, ESRS E1, définitions PPRI)
```

**Chiffres traçables (SQL)** : zones sismiques 1–5, classes RGA, niveaux TRI, compteurs CatNat, flags inondation PPRI — tous structurés, requêtables, exportables avec `source_id + date_requête`.

**RAG (sens uniquement)** : interprétation « que signifie zone PPRI bleue », obligations CSRD ESRS E1, glossaire Cat Nat — jamais pour produire un score ou un %.

**Limites de fiabilité** :

| Risque | Impact |
|---|---|
| Maille communale (radon, sismique) | Sous-estime/surestime l'exposition parcellaire |
| DRIAS 8 km | Non pertinent pour scoring actif sans downscaling |
| Quota API 10 req/s | Portefeuille 100 k actifs ≈ 3 h minimum en séquentiel (sans shapefile local) |
| Absence modèle vulnérabilité | Score d'exposition ≠ risque assurantiel / financier |
| Projection sans validation | Rapport CSRD non auditables si méthodologie maison non validée |

**Risque d'hallucination numérique** : faible **si** on reste sur champs API/SQL. **Élevé** si le LLM est sollicité pour extrapoler des projections DRIAS ou quantifier des impacts financiers sans modèle actuariel dédié.

---

## 7. Monétisation / impact

**Monétisation faible** pour un nouvel entrant :

- Les institutionnels achètent des **suites** (NamR+Addactis, Deepki ESG, Munich Re) intégrées à leurs process — pas un 10ᵉ agrégateur Géorisques.
- Fonciris fixe un **plancher de prix** API à 79 €/mois pro ; Apify à 0,005 $/adresse — marge impossible sur la matière première gratuite.
- Les budgets CSRD/climat existent (pression BCE, ESRS E1) mais sont **déjà alloués** aux acteurs §4.

**Impact** : un outil supplémentaire n'ajoute pas d'impact incrémental significatif — l'État (Géorisques/Errial), les greentechs installées (NamR, Callendar) et les global players (Jupiter, Munich Re) couvrent le besoin. Impact potentiel limité à une **niche non identifiée** (ex. petites foncières régionales sans budget ESG) à prix très bas — unit economics fragiles.

---

## 8. Risques

| Risque | Gravité | Commentaire |
|---|---|---|
| **Concurrence structurelle** | Critique | 10+ acteurs B2B identifiés ; Addactis a racheté NamR assurance (mai 2025) |
| **Commoditisation** | Critique | Apify + API publique = prix → 0 |
| **Responsabilité / audit** | Élevée | Scores utilisés pour underwriting ou CSRD sans méthodologie validée → responsabilité + rejet auditeur |
| **Dépendance API Géorisques** | Moyenne | Quotas, schéma, authentification — mitigable par miroir shapefiles |
| **Gap exposition → finance** | Élevée | Sans modèle vulnérabilité + scénarios validés, produit inutilisable par cible principale |
| **Effet « repositionnement 0011 »** | Critique | L'angle de survie de 0011 est lui-même saturé — double peine |

---

## 9. Effort MVP

**MVP technique minimal** (2–3 semaines, mais **non crédible** pour la cible B2B) :

1. Ingestion shapefiles RGA 2026 + TRI 2020 + miroir endpoints Géorisques en PostGIS/DuckDB.
2. Pipeline : CSV adresses → BAN → spatial join + API fallback → table `actif_risque`.
3. Dashboard portefeuille : heatmap, top 20 actifs exposés, export CSV, traçabilité source/date.
4. Disclaimers : « informatif, ne remplace pas étude assurantielle / rapport CSRD certifié ».

**MVP crédible institutionnel** (6–12 mois, hors portée seed) :

- Modèles prospectifs TRACC/DRIAS downscalés à la parcelle.
- Module vulnérabilité bâti (BDNB, DPE, imagerie).
- Exports ESRS E1 pré-formatés, audit trail, API enterprise.
- Validation actuarielle / certification méthodologique.

Le MVP rapide souffre du même problème que 0011 : **facile à copier, impossible à vendre** face à NamR/Callendar/Deepki.

---

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 |
| C2 | Cible solvable (qui paie) | 3 | 3 | 9 |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 |
| C5 | Différenciation défendable | 2 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 2 | 4 |
| C8 | Maîtrise des risques | 2 | 2 | 4 |
| C9 | Monétisation / impact | 2 | 2 | 4 |
| | **Total** | | | **57 / 105** |

**Score /100** : 57 / 105 × 100 = **54,3 → 54 / 100** (arrondi final)

Justification note par note :

- **C1 = 4** : douleur forte et croissante (sinistralité Cat Nat, CSRD, stress tests BCE) — le problème est réel, pas un gadget.
- **C2 = 3** : payeurs nommés avec budget constaté (Suravenir/Thélem via Addactis-NamR, banques de premier rang via NamR, AXA IM) — mais budgets **déjà captés** par l'existant ; pas de segment sous-servi démontré.
- **C3 = 4** : données ouvertes excellentes pour l'exposition actuelle (Géorisques, TRI, RGA 2026, LO 2.0) ; pénalisé car DRIAS prospectif sans API simple et maille grossière.
- **C4 = 1** : saturation confirmée — 10 acteurs B2B portefeuille nommés + commoditisation Apify ; pire que « occupé », marché en consolidation (rachat NamR par Addactis).
- **C5 = 1** : même donnée publique, batch copiable en un week-end, leaders avec modèles vulnérabilité + prospectif ; repositionnement suggéré par 0011 déjà pris.
- **C6 = 4** : architecture SQL/spatial join conforme RAG(sens)/SQL(chiffres) pour l'exposition actuelle ; plafonné car scoring financier prospectif exigerait R&D non couverte par open data brute.
- **C7 = 2** : MVP technique rapide mais **non crédible** pour acheteurs institutionnels ; MVP crédible = chantier lourd (modèles, audit CSRD).
- **C8 = 2** : risque concurrentiel dominant non maîtrisable ; responsabilité scores underwriting ; pas de parade produit identifiée.
- **C9 = 2** : marché existe mais capturé ; pression prix (Fonciris 79 €/mois, Apify 0,005 $/adresse) ; impact incrémental faible.

---

## 11. Verdict & décision

❌ **Écartée.**

Score **54/100** (< 55). Même en appliquant strictement le seuil « à retravailler » (55–69), l'idée se situe **sous le plancher** et cumule C4 = C5 = 1 — saturation structurelle, pas un point bloquant isolé.

**Synthèse** : le besoin B2B « scorer un portefeuille d'actifs sur les risques climatiques/naturels pour tarification et reporting TCFD/CSRD » est **réel et urgent**, mais **déjà servi** par une filière mature (Callendar, NamR/Addactis, Deepki, Jupiter, Mitiga, Climate X, Munich Re, Axa Climate, Earthian, Fonciris API, Bat-ADAPT). Le repositionnement que l'analyse 0011 identifiait comme seul espace de survie (batch portefeuille institutionnel) est **confirmé saturé**. Construire un agrégateur Géorisques+DRIAS générique serait un **MVP facile mais invendable** face à des acteurs avec modèles de vulnérabilité, intégrations SI et validation réglementaire.

Aucun critère strictement éliminatoire juridique ou « donnée inexistante », mais la combinaison **saturation + absence de différenciation + MVP non crédible** équivaut à un écartage de fond.

**Prochaine étape concrète** : **ne pas prototyper**. Si une verticale doit être explorée malgré tout, partir d'un **segment précis non couvert** (ex. un type d'actif oublié par NamR — tertiaire non résidentiel ? foncières <50 M€ sans outil ESG ?) et le **démontrer par 5 entretiens** avant toute ligne de code. Sans créneau validé terrain, ne pas réinvestir dans une 3ᵉ variante « risques × adresse/portefeuille ».

---

0024 | Exposition climat/risques d'un portefeuille d'actifs (B2B assurance/immo) | ❌ Écartée | 54/100 | Saturé : NamR, Callendar, Deepki, Jupiter
