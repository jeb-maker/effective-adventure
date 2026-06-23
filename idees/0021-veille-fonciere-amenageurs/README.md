# Veille foncière & urbanisme pour promoteurs/aménageurs (B2B)

- **ID** : 0021
- **Statut** : ❌ Écartée
- **Score** : 50 / 100
- **Dernière mise à jour** : 2026-06-21
- **Pitch (1 phrase)** : Outil B2B pour promoteurs, aménageurs et marchands de biens :
  détecter des opportunités foncières en croisant permis (Sitadel), DVF, PLU/zonage,
  friches (Cartofriches), parcelles et propriétaires personnes morales — distinct du
  grand public (cf. idée 0004).

---

## 1. Problème / douleur

Le **développement foncier** est le goulot d'étranglement du neuf : sans terrain
constructible au bon prix, pas de programme. Les développeurs fonciers passent une
part importante de leur temps à **croiser manuellement** cadastre, PLU, permis déposés,
transactions, friches et propriétaires — avant même une étude de faisabilité.

La douleur est **réelle, récurrente et à fort enjeu financier** (marge foncier typique
15–30 % du CA programme selon Kel Foncier). Urbanease (groupe PriceHubble) la qualifie
explicitement de « nerf de la guerre » pour les prospecteurs
(https://urbanease.io/, consulté 2026-06-20).

**Mais** cette douleur est déjà adressée par une offre B2B mature et installée depuis
plus d'une décennie (Kel Foncier depuis 2012 — https://www.landdetector.com/societe-kel-foncier/,
consulté 2026-06-20). Le problème n'est pas l'absence de solution : c'est l'**accès à
une solution déjà payée et dominante**.

## 2. Cible & qui paie

| Segment | Besoin | Qui paie ? | Budget constaté (sources datées) |
|---|---|---|---|
| **Promoteurs immobiliers** (neuf logements, bureaux) | Veille + faisabilité + prospection propriétaire | Direction développement / foncier | Kel Foncier : tarif sur devis par zone (agglomération → France entière) — https://www.kelfoncier.com/tarifs-kelfoncier/ (2026-06-20) ; témoignage « je ne pense pas qu'il y ait un promoteur qui n'utilise pas KelFoncier » — https://www.kelfoncier.com/ (2026-06-20) |
| **Aménageurs / lotisseurs** | Parcelles constructibles, division, viabilisation | Aménageur | IZIRED : **84,99 €/mois** (module analyse terrain) — https://izired.com/logiciel-promotion-immobiliere/ (2026-06-20) |
| **Marchands de biens / foncières** | Opportunités off-market, patrimoine PM | Direction asset / foncier | Urbanease (PriceHubble) : abonnement sur devis — https://www.pricehubble.com/fr/products/urbanease-par-pricehubble (2026-06-20) |
| **Agents immo / notaires / géomètres** (périmètre adjacent) | Fiche parcelle, DVF, urbanisme | Professionnel | Géofoncier Pack Immobilier : **80–87 €/mois** — https://www.geofoncier.fr/professionnels-de-l-immobilier/ (2026-06-20) |

Utilisateur = payeur dans la plupart des cas (développeur foncier interne). La cible
**paie déjà** des outils spécialisés ; l'enjeu pour un nouvel entrant n'est pas
« existe-t-il un budget ? » mais « arrachera-t-on un abonnement **supplémentaire** à
Kel Foncier / Urbanease / Géofoncier déjà souscrits ? » — réponse probablement non
sans différenciation majeure (non identifiée, cf. §5).

**Hors périmètre** : Bien'ici Pro = diffusion d'annonces neuf pour promoteurs, pas
veille foncière — https://solutionspro.bienici.com/contact (2026-06-20). Edicia =
sécurité urbaine (CITYZEN), pas foncier — https://www.odoo.com/fr_FR/customers/edicia-7039755
(2026-06-20).

**Distinction vs 0004** : l'idée 0004 (dossier DVF grand public) est écartée pour
saturation consumer ; 0021 cible le B2B promoteur — segment différent, mais **même
stack données** et concurrence B2B encore plus dense.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| Sitadel — permis & autorisations d'urbanisme | https://www.data.gouv.fr/datasets/liste-des-permis-de-construire-et-autres-autorisations-durbanisme | Licence Ouverte 2.0 | ZIP/CSV (fichiers mensuels SDES) | Mensuelle ; dernière MàJ fiche **12 juin 2026** | Pas de géoloc parcelle native fiable dans le brut ; enrichissement BAN nécessaire (~89 % géolocalisés selon PermisAPI — https://www.data.gouv.fr/reuses/permisapi-1-2-million-de-permis-de-construire-de-france-en-acces-direct, 2026-06-20) ; délais de saisie collectivités |
| Sitadel — séries logements (stats) | https://www.data.gouv.fr/datasets/logements-autorises-et-commences-series-mensuelles-communales-en-date-de-prise-en-compte | Licence Ouverte 2.0 | CSV | Mensuelle ; MàJ **18 juin 2026** | Agrégats communaux, pas fiche parcelle |
| DVF (brut DGFiP) | https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres | Licence Ouverte 2.0 | TXT (pipe) | **Semestrielle** (avril/octobre) ; MàJ **7 avril 2026** | 5 ans glissants ; hors Alsace-Moselle et Mayotte ; pas de vendeur/acheteur ; interdiction réidentification (https://cadastre.data.gouv.fr/dvf, 2026-06-20) |
| DVF+ (Cerema, géolocalisé) | https://www.data.gouv.fr/datasets/dvf-open-data | Licence Ouverte 2.0 | PostgreSQL/PostGIS, GeoPackage, CSV | MàJ fiche **12 juin 2026** | Géoloc via PCI ; qualité variable ; pas de prix foncier « terrain nu » isolé trivial |
| PLU / GPU (zonage, documents) | https://www.geoportail-urbanisme.gouv.fr/services/?subcategory=services_api | Licence Ouverte (Etalab) | WMS/WFS, API GPU, API Carto module Urbanisme | Continue (publication obligatoire PLU exécutoires depuis 2023) | Hétérogénéité qualité numérisation PLU entre communes ; règles complexes ≠ simple zonage ; couches IGN soumises à CGU séparées (https://www.geoportail-urbanisme.gouv.fr/cgu/, 2026-06-20) |
| Cadastre — parcelles (PCI / Etalab) | https://www.data.gouv.fr/datasets/cadastre | Licence Ouverte 2.0 | GeoJSON, Shapefile | Continue (PCI vecteur couvre ~35 000 communes depuis sept. 2025) | **Aucune info propriétaire** dans PCI (https://guides.data.gouv.fr/guides/reutiliser-des-donnees/autour-du-cadastre/manipuler-les-donnees-du-cadastre, 2026-06-20) |
| MAJIC — personnes morales (parcelles & locaux) | https://www.data.gouv.fr/datasets/fichiers-des-locaux-et-des-parcelles-des-personnes-morales | Licence Ouverte 2.0 | Fichiers départementaux (texte) | **Annuelle** (situation au 1er janvier) ; fiche officielle MàJ **25 mars 2021** (fréquence non respectée sur la fiche) | Personnes physiques **exclues** ; SCI unipersonnelles exclues ; pas de coordonnées propriétaire ; jointure PCI requise |
| MAJIC unifié (communauté) | https://www.data.gouv.fr/datasets/fichiers-des-locaux-et-des-parcelles-des-personnes-morales-version-unifiee | Licence Ouverte 2.0 | Parquet national | MàJ **3 nov. 2025** | Reprise communautaire, pas producteur officiel ; dénominations bruitées |
| Cartofriches — sites référencés | https://www.data.gouv.fr/datasets/sites-references-dans-cartofriches | Licence Ouverte 2.0 | CSV/Geo (table nationale) | ~trimestrielle ; MàJ **15 juin 2026** | **Non exhaustif** (~3 000 sites nationaux + locales) ; hétérogène territorialement ; « friche potentielle » ≠ terrain disponible (https://www.data.gouv.fr/datasets/sites-references-dans-cartofriches, 2026-06-20) |
| Base SIRENE (enrichissement PM) | https://www.data.gouv.fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret | Licence Ouverte | CSV/Parquet/API | Mensuelle | Lien MAJIC → SIREN pas toujours trivial ; RGPD |
| **RPG** (registre parcellaire graphique) | https://www.data.gouv.fr/datasets/registre-parcellaire-graphique-agricole | LO 2.0 | CSV/GeoJSON | MàJ **20 juin 2026** (vérifié 2026-06-21) | Parcelles agricoles ; pression foncière vs zonage PLU |
| **Cartes de bruit** (zones stratégiques) | https://www.data.gouv.fr/datasets/zones-de-bruit-des-cartes-de-bruit-strategiques-4eme-echeance-1 | LO 2.0 | Shapefile | Variable par territoire | Couverture inégale ; complément risques pour implantation |

> [`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements envisagés

| Croisement | Signal foncier | Faisabilité |
|---|---|---|
| **Sitadel × DVF+ × MAJIC PM** | Permis déposé → ventes réalisées → propriétaire PM | **Bonne** (cœur du seed) — déjà fait par Kel Foncier |
| **MAJIC × RPG × GPU** | Parcelle agricole en zone constructible PLU (pression foncière) | Spatial PostGIS — **bonne** |
| **Cartofriches × Sitadel × DVF** | Friche référencée avec permis/valeur en hausse | **Moyenne** — Cartofriches non exhaustif |
| **DPE × parcelle** (via BDNB) | Passoires sur foncier à potentiel | Adresse — voir 0009/0025 |

Voir [0026](../0026-exposition-parcelles-agricoles/) pour l'angle agricole (RPG × risques).

**Synthèse données** : le cœur tabulaire (Sitadel, DVF, MAJIC PM) est **SQL-able** une fois
ingéré et géo-jointé — conforme au principe RAG(sens)/SQL(chiffres). Le maillon faible
est l'**interprétation du PLU** (règles d'emprise, hauteur, mixité) : les concurrents
matures (Kel Foncier, Senari, IZIRED) y ajoutent de la **préfaisabilité experte** ou du
dessin assisté, pas du simple croisement open data. Les coordonnées de propriétaires
physiques et l'enrichissement contact ne sont **pas** dans l'open data — les acteurs
installés revendiquent ces données comme avantage propriétaire (Kel Foncier :
« identité des propriétaires, leurs coordonnées » — https://www.kelfoncier.com/, 2026-06-20).

## 4. Existant / concurrence

**Verdict saturation : saturé** au niveau produit B2B. Le seed de l'idée décrit
**exactement** l'offre de Kel Foncier et de plusieurs concurrents directs. L'espace
libre éventuel serait une **niche verticale très étroite** (ex. foncière solaire,
bailleur social) ou un **canal captif** (intégration ERP promoteur type PEGAO) — pas
un SaaS horizontal « croiser Sitadel + DVF + PLU + friches + PM ».

### Produits commerciaux B2B (concurrence directe — 8+ acteurs)

| Produit | URL | Ce qu'il fait (recoupement seed) | Prix / modèle (si dispo) | Limites |
|---|---|---|---|---|
| **Kel Foncier** | https://www.kelfoncier.com/ — promoteurs : https://www.kelfoncier.com/promoteur-immobilier/ | Veille automatisée (CU, permis, mutations, successions, annonces) ; 50+ critères ; PLU 35 000 communes ; préfaisabilité experte ; propriétaires + CRM + courriers postaux ; taxe d'aménagement | Sur devis par zone ; essai 48 h — https://www.kelfoncier.com/tarifs-kelfoncier/ (2026-06-20) | Pricing opaque ; données contact propriétaire non sourcées open data |
| **Urbanease** (PriceHubble) | https://urbanease.io/ — https://www.pricehubble.com/fr/products/urbanease-par-pricehubble | Prospection + CRM terrain ; parcelles haut potentiel ; permis ; patrimoine propriétaires PM ; PLU/PLUi ; stratégies prospection clés en main | Sur devis (2026-06-20) | Groupe PriceHubble bien financé |
| **ORUS App** (1Spatial) | https://1spatial.com/fr/produits/orus-app/ | Recherche intelligente parcelles ; PLU, PM, DVF, permis ; SDP en 3 clics ; 3D | 1 mois essai gratuit sur demande (2026-06-20) | Racheté par acteur SIG international |
| **Géofoncier Expert** | https://www.geofoncier.fr/professionnels-de-l-immobilier/ | 200+ couches (Sitadel, PLU, DVF, PM, risques) ; fiche parcelle ; filtres multi-critères ; rapports PDF | Pack Immobilier **80–87 €/mois** (2026-06-20) | Portail OGE ; moins orienté « alertes opportunité » que Kel Foncier |
| **IZIRED** | https://izired.com/logiciel-promotion-immobiliere/ | Analyse terrain : PLU, risques, prix neuf/ancien, coûts construction ; module IZI Foncier (rapport urbaniste 48 h) | **84,99 €/mois** (2026-06-20) | Faisabilité plutôt que veille passive |
| **Senari** | https://senari.fr/ | Étude faisabilité 15 min ; PLU ; plan de masse ; dossier comité | Sur devis (2026-06-20) | Orienté dossier décision, moins veille territoriale |
| **CityScan / Modelo Insight** (Septeo) | https://www.cityscan.fr/ — pro : https://www.journaldelagence.com/1175945-cityscan-lance-son-nouveau-service-dedie-aux-professionnels-de-limmobilier | 120+ indicateurs ; évaluation emplacement ; API ; clients promoteurs (Altarea, Kaufman Broad cités) | Sur devis (2026-06-20) | Plutôt évaluation/avis de valeur que prospection foncière pure |
| **PermisAPI** | https://www.data.gouv.fr/reuses/permisapi-1-2-million-de-permis-de-construire-de-france-en-acces-direct — https://permisapi.fr | API Sitadel enrichie (géoloc BAN, DVF, zonage PLU, risques BRGM) ; MCP/HTTP | Gratuit 500 req/mois ; **49–199 €/mois** (2026-06-20) | Couche données, pas produit métier complet — mais commoditise l'ingestion |

### Acteurs adjacents (gestion de projet, pas veille — mais bundling possible)

| Produit | URL | Positionnement |
|---|---|---|
| **PEGAO** | https://pegao.fr/ | ERP promoteur/aménageur A→Z (foncier → livraison) ; pas veille territoriale native |
| **Aprilyos** | https://www.aprilyos.com/logiciel-lotisseur/ | Logiciel lotisseur (division, viabilisation, GED) |

### Réutilisations data.gouv.fr (même stack, déjà commercialisée)

- **Géofoncier** cite explicitement Sitadel, DVF, GPU, MAJIC dans sa fiche parcelle —
  https://www.geofoncier.fr/conseils/la-fiche-parcelle-par-le-menu-pour-une-analyse-poussee-du-foncier/
  (2026-06-20).
- **Cartofriches** (Cerema) : application + open data —
  https://www.data.gouv.fr/reuses/cartofriches (2026-06-20).
- **API Données foncières** (Cerema) : accès friches et foncier —
  https://www.data.gouv.fr/reuses/api-donnees-foncieres (2026-06-20).
- **Version unifiée MAJIC** (Parquet France) —
  https://www.data.gouv.fr/reuses/version-unifiee-des-fichiers-des-locaux-et-des-parcelles-des-personnes-morales
  (2026-06-20).

### Services publics (consultation, pas veille B2B)

| Service | URL | Couverture |
|---|---|---|
| Explorateur DVF (grand public) | https://explore.data.gouv.fr/fr/immobilier | Transactions ; saturé côté consumer (cf. 0004) |
| Géoportail de l'urbanisme | https://www.geoportail-urbanisme.gouv.fr/ | Consultation PLU/SUP ; pas d'alertes ni scoring foncier |
| Cartofriches (visualisation) | https://cartofriches.cerema.fr/ | Inventaire friches ; pas de croisement promoteur |

### Open source / APIs tierces

| Projet | URL | Intérêt | Limites |
|---|---|---|---|
| apifoncier (Cerema) | https://cerema.github.io/apifoncier/ | Client Python données foncières | Données, pas produit |
| SOGEFI API ADS / MAJIC | https://www.sogefi-sig.com/geoservices-apis-wms/api-ads-autorisation-du-droit-des-sols/ | Sitadel + parcelle ; SIRENE déposant PM | API commerciale |
| SOGEFI Open MAJIC | https://www.sogefi-sig.com/geoservices-apis-wms/api-open-majic/ | PM par parcelle | API commerciale ; MAJ annuelle |

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0021-veille-fonciere-amenageurs` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `real-estate-proptech` — Immobilier & proptech

Fichier : [`catalogue-saas/vendors/real-estate-proptech.json`](../../catalogue-saas/vendors/real-estate-proptech.json) (15 entrées)

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
| … | _+3 autres_ | | | |

#### Segment `geospatial-gis-fr` — Géospatial & carto FR

Fichier : [`catalogue-saas/vendors/geospatial-gis-fr.json`](../../catalogue-saas/vendors/geospatial-gis-fr.json) (16 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `geofoncier` | Géofoncier | FR | strong | partial |
| `alkante` | Alkante | FR | strong | partial |
| `ign-geoservices` | IGN Géoservices | FR | strong | partial |
| `cartelie` | Cartélie (IGN) | FR | strong | partial |
| `opendatasoft-geo` | Opendatasoft | FR | strong | partial |
| `ordnance-survey` | Ordnance Survey | GB | absent | partial |
| `esri-arcgis` | Esri ArcGIS | US | partial | partial |
| `mapbox` | Mapbox | US | partial | partial |
| `here-technologies` | HERE Technologies | NL | partial | partial |
| `geoperso` | GÉOPERSO | FR | strong | partial |
| `makina-corpus` | Makina Corpus | FR | strong | partial |
| `geoportail-urbanisme` | Géoportail de l'urbanisme (GPU) | FR | strong | partial |
| … | _+4 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment real-estate-proptech
```

<!-- catalogue-saas-end -->
## 5. Différenciation

Le pitch seed — « croiser Sitadel + DVF + PLU + Cartofriches + parcelles + PM pour
promoteurs » — est **la proposition centrale de Kel Foncier** depuis 2012 et reprise
quasi mot pour mot par ORUS App et Urbanease.

Angles théoriques restants, tous **non défendables** face à l'existant :

| Angle revendiqué | Déjà fait par | Verdict |
|---|---|---|
| Alertes permis / signaux fonciers | Kel Foncier (CU, PC, mutations, successions, annonces) | Copié |
| Filtres multi-critères parcelle | Kel Foncier (50+), Géofoncier (200 couches), ORUS | Copié |
| Préfaisabilité / SDP | Kel Foncier (experts), Senari, IZIRED, ORUS (3 clics) | Copié + expertise humaine |
| Propriétaires PM + patrimoine | Urbanease, ORUS, Kel Foncier, Géofoncier | Copié |
| Friches | Cartofriches officiel + intégration possible par tout acteur | Commodity |
| Prix abordable open data | IZIRED 84,99 € ; Géofoncier 80 € ; PermisAPI 49 € | Plancher bas |

**Différenciation durable** : non identifiée. Un nouvel entrant n'apporterait ni données
exclusives (tout est open ou déjà enrichi par les incumbents), ni canal d'acquisition
(identifié), ni verticalisation prouvée.

## 6. Faisabilité & fiabilité technique

**Architecture cible (conforme RAG sens / SQL chiffres) :**

1. **Ingestion** : Sitadel mensuel → PostGIS/DuckDB ; DVF+ (mutations géolocalisées) ;
   MAJIC Parquet unifié ; GPU (WFS zonage) ; Cartofriches trimestriel ; PCI parcelles.
2. **Jointures spatiales** : parcelle_id comme clé ; index géospatial pour alertes
   par secteur.
3. **SQL** : prix/m² médian DVF par secteur, comptage permis, surface plancher autorisée
   (champs Sitadel), filtres PM (dénomination, forme juridique).
4. **RAG (sens uniquement)** : documentation PLU (métadonnées GPU, définitions zonage,
   glossaire urbanisme) pour **expliquer** un zonage — pas pour calculer une SDP.
5. **LLM** : résumé « pourquoi cette parcelle » à partir de faits SQL + extraits doc ;
   jamais de chiffre inventé.

**Risques de fiabilité (hors hallucination LLM) :**

- **Sémantique DVF** : ventes multi-lots, dépendances, prix global ≠ prix terrain nu.
- **Sitadel ↔ parcelle** : lien imparfait sans géocodage ; délais de publication.
- **PLU** : interpréter le règlement (hauteur, CES, mixité) requiert un moteur de règles
  ou des experts — c'est le cœur de métier des concurrents, pas un simple croisement.
- **Propriétaires physiques** : hors open data → trou dans le pitch « à qui contacter ».

Conformité RAG/SQL : **partielle** — les chiffres marché et permis sont traçables, mais
la **préfaisabilité** (promesse métier centrale) ne peut pas reposer sur du SQL seul sans
reproduire des années de règles métier.

## 7. Monétisation / impact

Modèle théorique : SaaS B2B **80–200 €/mois/utilisateur** par zone géographique,
aligné sur Géofoncier (80–87 €), IZIRED (84,99 €) et PermisAPI (49–199 €).

**Problème** : ces prix sont déjà pratiqués par des acteurs installés avec CRM,
préfaisabilité, support et données propriétaires enrichies. Kel Foncier revendique une
adoption quasi universelle chez les promoteurs. Le CAC B2B promoteur (cycle de vente
long, démo terrain) face à un ARPU modéré rend les **unit economics défavorables**
pour un entrant sans angle d'acquisition.

Impact sociétal potentiel (meilleure utilisation du foncier, ZAN) : réel mais **déjà
porté** par les outils existants et Cartofriches public.

## 8. Risques

| Risque | Gravité | Commentaire |
|---|---|---|
| **Saturation concurrentielle** | Critique | Kel Foncier, Urbanease/PriceHubble, ORUS, Géofoncier couvrent le seed |
| **Données propriétaires/contact** | Élevée | Open data = PM seulement ; concurrents revendiquent coordonnées (source non ouverte) |
| **RGPD / réidentification DVF** | Élevée | DGFIP interdit réidentification (https://cadastre.data.gouv.fr/dvf, 2026-06-20) |
| **Qualité PLU hétérogène** | Élevée | Erreurs d'interprétation → responsabilité produit |
| **Effort ingestion nationale** | Élevée | PCI + GPU + Sitadel + MAJIC = pipeline lourd à maintenir |
| **Commoditisation API** | Moyenne | PermisAPI/SOGEFI réduisent la barrière technique d'entrée pour d'autres concurrents |
| **Confusion avec 0004** | Faible | Cibles différentes mais risque de re-proposer une « carte DVF+ » sans valeur B2B |

## 9. Effort MVP

Périmètre minimal **crédible** pour un promoteur (pas un POC carte) :

1. Ingestion nationale : PCI parcelles + Sitadel géolocalisé + DVF+ + GPU zonage +
   MAJIC PM + Cartofriches.
2. Moteur de recherche : 10+ filtres (surface, zonage U/AU, type PM, permis récents,
   prix/m² DVF secteur).
3. Fiche parcelle unifiée + 3 alertes (nouveau permis, nouvelle vente DVF, changement PLU
   sur secteur).
4. Traçabilité : chaque chiffre → requête SQL + source + date millésime.

**Estimation** : plusieurs mois à 2–3 ETP data/geo + 1 dev fullstack pour atteindre un
niveau **inférieur** à Kel Foncier v1 — sans CRM, sans préfaisabilité experte, sans
données contact. Les concurrents ont 5–15 ans d'avance produit et données enrichies.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 | Douleur forte et récurrente pour développeurs fonciers — mais déjà soulagée par l'existant. |
| C2 | Cible solvable (qui paie) | 3 | 3 | 9 | Payeurs et budgets constatés (Kel Foncier, Géofoncier 80 €, IZIRED 85 €) — mais marché déjà équipé, peu de budget additionnel. |
| C3 | Disponibilité & fiabilité données | 3 | 3 | 9 | Sources open solides mais jointures lourdes, MAJIC annuel, DVF semestriel, Cartofriches incomplet, PLU hétérogène. |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 | Saturé : 8+ produits B2B couvrent exactement le seed (Kel Foncier en tête). |
| C5 | Différenciation défendable | 2 | 1 | 2 | Aucun angle non déjà tenu par Kel Foncier, Urbanease, ORUS ou Géofoncier. |
| C6 | Faisabilité & fiabilité technique | 2 | 3 | 6 | SQL OK pour chiffres marché/permis ; préfaisabilité PLU = hors scope SQL simple. |
| C7 | Facilité du MVP | 2 | 2 | 4 | Pipeline geo national + moteur règles urbanisme = chantier lourd vs produits matures. |
| C8 | Maîtrise des risques | 2 | 2 | 4 | Concurrence dominante, RGPD, données contact hors open data — risques mal maîtrisables. |
| C9 | Monétisation / impact | 2 | 2 | 4 | ARPU comparable aux incumbents mais sans avantage compétitif ; CAC B2B promoteur élevé. |
| | **Total** | | | **52 / 105** | |

**Score /100** : 52 / 105 × 100 = **49,5 → 50 / 100**

## 11. Verdict & décision

❌ **Écartée** — score 50/100 (< seuil 55) **et** critère éliminatoire de **saturation
marché B2B** (même logique que 0004 côté grand public, mais ici la concurrence
professionnelle est encore plus frontale).

Le seed décrit le produit de **Kel Foncier** (leader revendiqué, utilisé « par tous les
promoteurs » selon leurs témoignages) et de **six autres acteurs** minimum. Reproduire ce
croisement open data n'apporte pas de valeur incrémentale identifiable ; les données
contact propriétaire et la préfaisabilité — cœur de la proposition de valeur — reposent
sur des enrichissements **hors open data** que les incumbents détiennent déjà.

**Prochaine étape** : ne pas prototyper. Si l'on souhaite rester sur le foncier B2B,
explorer une **niche non couverte** par Kel Foncier/Urbanease (ex. foncières
institutionnelles, énergie, bailleurs) avec un différenciateur prouvé par entretiens
terrain — ou pivoter vers un angle data purement **API/infra** (type couche PermisAPI)
plutôt qu'un SaaS veille frontal.

---

0021 | Veille foncière & urbanisme pour promoteurs/aménageurs (B2B) | ❌ Écartée | 50/100 | Marché B2B saturé Kel Foncier
