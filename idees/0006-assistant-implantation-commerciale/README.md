# Assistant d'implantation commerciale (SIRENE + géomarketing)

- **ID** : 0006
- **Statut** : ❌ Écartée
- **Score** : 50 / 100
- **Dernière mise à jour** : 2026-06-20
- **Pitch (1 phrase)** : Aide à la décision pour indépendants/franchises sur le choix
  d'emplacement : concurrence locale (SIRENE/BODACC), pouvoir d'achat et démographie
  (INSEE), flux/mobilité — expliqué clairement pour des non-experts.

---

## 1. Problème / douleur

Choisir un emplacement commercial est une décision à fort enjeu : loyer, travaux,
caution, temps du porteur de projet. Une mauvaise implantation est difficilement
réversible. Les données utiles (concurrence, revenus, population, flux) existent en
open data, mais restent **dispersées**, techniques (codes NAF, IRIS, isochrones) et
souvent interprétées via des outils payants ou des prestations CCI/consultants. Pour
un indépendant ou un candidat à la franchise, le besoin est réel et récurrent — mais
**déjà adressé** par une offre abondante (voir §4).

## 2. Cible & qui paie

| Segment | Besoin | Qui paie ? | Budget observé |
|---|---|---|---|
| **Créateur / indépendant** (commerce, services) | Valider un emplacement avant bail | Lui-même (souvent) | Très sensible au prix ; outils gratuits ou ~42 € HT (Geomarket.one) |
| **Franchiseur / réseau** | ELM (loi Doubin), maillage, zones d'exclusivité | Franchiseur | 42–300 € HT/étude (Geomarket.one) ; 99–399 € HT/mois (Smappen) ; devis (Data-B, Galigeo) |
| **Agent immobilier commercial** | Étude d'implantation pour mandat | Agence / agent | SaaS métier (Data-B sur devis) |
| **CCI / conseillers publics** | Accompagnement création | Pris en charge / subventionné | Gratuit pour le porteur (CCI, Service Public Conseillers) |

Utilisateur ≠ payeur pour les indépendants accompagnés par les CCI. Le segment le
plus solvable financièrement (franchiseurs) est aussi le **mieux équipé** et exigeant
sur la conformité ELM.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| Base SIRENE (établissements) | https://www.data.gouv.fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret | Licence Ouverte 2.0 | CSV / Parquet (stock mensuel) ; API INSEE | Mensuelle (image fin de mois précédent) ; API infra-mensuelle | Données personnelles (RGPD, statut diffusion « P ») ; géolocalisation non incluse dans le stock brut ; passage NAF 2025 en 2027 |
| Géolocalisation SIRENE (études stat.) | https://www.data.gouv.fr/datasets/geolocalisation-des-etablissements-du-repertoire-sirene-pour-les-etudes-statistiques | Licence Ouverte 2.0 | CSV | Mis à jour 2026-05-27 (fiche data.gouv.fr) | Jeu statistique, pas le répertoire temps réel ; coordonnées absentes ou masquées pour oppositions |
| BODACC | https://www.data.gouv.fr/datasets/bodacc | Licence Ouverte | Fichiers + API | Quotidienne (5×/semaine) | Créations/cessions/modifications, pas un répertoire concurrentiel temps réel ; données personnelles |
| Population IRIS (RP 2022) | https://www.insee.fr/fr/statistiques/8647014 | Licence Ouverte (Insee) | CSV / XLSX | Millésime 2022, géo au 01/01/2024 | ~15 500 IRIS ; communes <5 000 hab. peu ou pas découpées ; labels qualité IRIS à respecter |
| Contours IRIS® | https://www.data.gouv.fr/datasets/contours-iris-r | Licence Ouverte 2.0 | Shapefile / GeoPackage | Édition 2024 (fiche data.gouv.fr) | Nécessaire pour jointures spatiales |
| Revenus / pouvoir d'achat (FiLoSoFi carroyé) | https://www.data.gouv.fr/datasets/revenus-pauvrete-et-niveau-de-vie-donnees-carroyees | Licence Ouverte 2.0 | Shapefile / GeoPackage / CSV | Millésime FiLoSoFi (revenus 2020 pour diffusion récente) | Secret statistique (<11 ménages) ; imputations ; décalage fiscal vs année courante ; métropole + Martinique + Réunion |
| Revenus IRIS (FiLoSoFi) | https://www.insee.fr/fr/statistiques/8229323 | Licence Ouverte (Insee) | CSV | Revenus 2021 (millésime publié) | IRIS des communes ≥5 000 hab. ; indicateurs non sommables ; secret statistique |
| Base permanente des équipements (BPE) | https://www.data.gouv.fr/datasets/base-permanente-des-equipements-1 | Licence Ouverte 2.0 | CSV / API Insee | Annuelle (au 01/01) | 229 types d'équipements ; qualité géoloc variable (indicateur bon/acceptable/mauvais) ; pas exhaustif vs SIRENE pour le commerce |
| Nomenclature NAF | https://www.data.gouv.fr/datasets/nomenclature-dactivites-francaise-naf | Licence Ouverte 2.0 | CSV | Référentiel | Mapping NAF → secteur commerce : interprétation métier requise |
| Codes postaux / communes | https://www.data.gouv.fr/datasets/base-officielle-des-codes-postaux | Licence Ouverte 2.0 | CSV | 2023 (fiche data.gouv.fr) | Communes multi-codes postaux |
| Découpage administratif | https://www.data.gouv.fr/datasets/decoupage-administratif-1 | Licence Ouverte 2.0 | GeoJSON / SHP | Continu (fiche data.gouv.fr) | Référentiel géographique |
| DVF (transactions immobilières) | https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres | Licence Ouverte 2.0 | TXT / CSV | Semestrielle (DGFIP) | **Principalement résidentiel** ; peu utile pour loyer commercial ou flux piéton |
| Comptages mobilité / piétons | Schéma national : https://schema.data.gouv.fr/etalab/schema-comptage-mobilites/ ; ex. Toulouse : https://www.data.gouv.fr/datasets/comptages-routiers-et-pietons-2025 | Licence Ouverte 2.0 (selon producteur) | CSV normalisé | Variable par collectivité | **Pas de couverture nationale homogène** ; souvent local (Toulouse, Poitiers…) ; flux « piéton » des SaaS concurrents reposent en partie sur données propriétaires (à vérifier par acteur) |
| Isochrones / temps de trajet | Moteurs tiers (OSRM, Valhalla, APIs routage) | Variable (souvent open source + données OSM) | API | Temps réel selon moteur | **Pas une donnée ouverte unique** ; coût calcul + dépendance service externe |
| OpenStreetMap France | https://www.data.gouv.fr/datasets/donnees-openstreetmap-integrales-de-france-metropolitaine | ODbL (OSM) | PBF | 2026-06-19 (fiche data.gouv.fr) | Réseau routier pour isochrones ; pas de flux piéton direct |

**Synthèse données :** le cœur (SIRENE + INSEE démo/revenus + BPE) est **solide et SQL-able**.
Le maillon faible du pitch est le **flux/mobilité** : pas de jeu national ouvert
équivalent à ce que vendent Data-B ou Smappen (flux piéton, attractivité rue).

## 4. Existant / concurrence

**Verdict saturation : saturé** pour un assistant généraliste SIRENE + géomarketing.
L'espace libre éventuel serait une **niche sectorielle très étroite** (ex. un seul
vertical type santé/optique) ou un **canal d'acquisition captif** (CCI, banque) — pas
un produit horizontal « pour tous les indépendants ».

### Réutilisations data.gouv.fr (proches du pitch)

| Produit | URL | Ce qu'il fait | Limites / ce qu'il ne fait pas |
|---|---|---|---|
| **Assistant d'Opportunités Économiques et d'Implantation** (Khalil Khabbaz) | Réutilisation : https://www.data.gouv.fr/reuses/assistant-dopportunites-economiques-et-dimplantation — App : https://www.123calculus.com/assistant-opportunites-economiques-page-20-20-100.html | Carte de visite économique par secteur + lieu ; SIRENE + API BOAMP + démo/géo | Pas de zone de chalandise isochrone avancée ni ELM ; interface calculateur, pas SaaS récurrent |
| **Outil Entreprises sur Zone** (Geomarket.one / Resilience Technologies) | https://www.data.gouv.fr/reuses/outil-de-prospection-commerciale — https://ancre.geomarket.one/library.php?a=outil_entreprises_locales | Carte gratuite des entreprises par secteur ; liens annuaire, Pages Jaunes, LinkedIn | Prospection B2B, pas d'analyse revenus/flux ; renvoie vers étude payante pour vue globale |
| **Études de marché et ELM** (Geomarket.one) | https://www.data.gouv.fr/reuses/etudes-de-marche-et-etat-local-de-marche-elm — https://ancre.geomarket.one/pricing.php | Étude/ELM auto : zones de chalandise, démo, concurrence, attracteurs de flux ; **42 € HT** (Standard), 52–60 € HT (Avancée/Pro), 300 € HT/mois (abonnement Pro) | Prix plancher très bas ; promet déjà IA + score d'opportunité IRIS (offre Avancée) |
| **Outil de Zones de Chalandise** (Geomarket.one) | https://www.data.gouv.fr/reuses/outil-de-zones-de-chalandise | Tracé de zones de chalandise (gratuit, compte requis) | Complément des études payantes |
| **EoGIS Commerce** | https://www.data.gouv.fr/reuses/eogis-commerce | Listes et cartes d'établissements SIRENE par zone/NAF ; export tableaux/rapports | Orienté prospection B2B / SIG, pas d'assistant pédagogique grand public |
| **Logiciel de géomarketing Data-B** | https://www.data.gouv.fr/reuses/logiciel-de-geomarketing — https://data-b.com/data-expertise-elm/ | Géomarketing rue/IRIS, flux piéton, ELM loi Doubin, >80 indicateurs ; SaaS sur devis ; étude ponctuelle **259 € HT** (page produit Data Expertise, à vérifier au moment de l'achat) | Cible immobilier commercial / franchises ; prix non public sur abonnement |
| **Identifiez les meilleures zones d'implantation** (Data-B) | https://www.data.gouv.fr/reuses/identifiez-les-meilleures-zones-dimplantation | Analyse démo + flux piéton pour franchises/enseignes | Même écosystème Data-B |
| **État local de marché** (Asterop) | https://www.data.gouv.fr/reuses/etat-local-de-marche | ELM, isochrones, densité commerciale, rapports réseau ; données INSEE/SIRENE | Prix non affiché sur la fiche data.gouv.fr |
| **Analyse de zone de chalandise** (Smappen) | https://www.data.gouv.fr/reuses/analyse-de-zone-de-chalandise — https://www.smappen.fr/ | Zones isochrones, 360 indicateurs INSEE, POI, rapports ELM Word | **Gratuit** (10 zones) ; **99 € HT/mois** (Essentiel) ; **199 € HT/mois** (Pro) ; **399 € HT/mois** (Avancé) — sources : https://www.smappen.com/pricing/ , https://www.smappen.fr/blog/nouveau-plan-avance-smappen/ , https://iapac.to/smappen-guide-complet-logiciel-geomarketing/ |

### Produits commerciaux (hors fiche data.gouv.fr)

| Produit | URL | Prix (si dispo) | Positionnement |
|---|---|---|---|
| **Smappen** | https://www.smappen.fr/ | Voir ci-dessus | Leader français géomarketing accessible ; ELM illimité en Pro |
| **Data-prospection.fr** | https://www.data-prospection.fr/search/ — CGV : https://data-prospection.fr/cgv | Fichiers à partir de **4,99 €** ; pas d'abonnement (CGV) ; plateforme SaaS géomarketing selon CGU | Prospection + cartes + isochrones ; fichiers entreprises ponctuels |
| **Mygeomarket** | https://mygeomarket.com/ | Sur devis (estimations tierces : 300–500 €/mois — à vérifier) | Retail / franchise, prévision CA IA |
| **GEO Business** (Ciril GROUP) | https://geo-business.com/fr/ | Sur devis | Réseaux de points de vente, 300+ indicateurs, exports PDF/Excel |
| **Galigeo** | https://www.galigeo.com/solutions/retail | Sur devis | Retail, simulation CA, flux piétons, intégration BI |

### Services publics / gratuits

| Service | URL | Couverture |
|---|---|---|
| **Cartographie infracommunale INSEE** | https://www.insee.fr/fr/outil-interactif/7737357/documentation.html | Gratuit : population, revenus carroyés FiLoSoFi, équipements BPE par IRIS/carreau — **sans assistant métier ni concurrence SIRENE par adresse** |
| **Annuaire des Entreprises (export SIRENE)** | https://annuaire-entreprises.data.gouv.fr/export-sirene | Export CSV filtré (500 SIREN/SIRET max par liste) ; MAJ quotidienne |
| **ODIL (INSEE)** | https://www.generali.fr/professionnel/actu/odil-outil-aide-creation-entreprise/ | **Arrêté janvier 2021** — référence historique, remplacé par offre privée + CCI |
| **Service Public Conseillers entreprises** | https://conseillers-entreprises.service-public.gouv.fr/ | Orientation gratuite vers CCI/CMA, pas d'outil géomarketing intégré |
| **CCI** | https://www.cci.fr/ressources/creation-dentreprise/accompagnement-et-aides/la-cci-votre-partenaire-pour-entreprendre | Accompagnement humain ; outils locaux variables |

### Open source / académique

| Projet | URL | Intérêt | Limites |
|---|---|---|---|
| **optimal-pos** (TSE, 2020) | https://github.com/guillemforto/optimal-pos | Modèle d'interaction SIRENE + IRIS, app Shiny | Prototype cours ; non maintenu comme produit |
| **spopt** (modèle Huff, R) | https://walker-data.com/spopt-r/reference/huff.html | Part de marché / potentiel par gravité | Bibliothèque, pas produit FR clé en main |
| **france-data-mcp** | https://github.com/cturkieh/france-data-mcp | Croisement SIRENE + référentiels (santé surtout) | MCP technique, pas interface implantation commerce |

## 5. Différenciation

Le pitch initial — « concurrence + pouvoir d'achat + flux, expliqué aux
non-experts » — est **déjà tenu** par au moins trois acteurs sur data.gouv.fr
(Geomarket.one à 42 €, Assistant Opportunités gratuit, Smappen freemium) et par
une dizaine de SaaS métier.

Angles théoriques restants, tous **facilement copiables** :

- **Vulgarisation IA** : Geomarket.one et Smappen revendiquent déjà pédagogie + IA
  (articles 2025–2026 sur geomarket.one).
- **Prix indépendant** : plancher à 42 € HT rend difficile toute monétisation
  supérieure sans valeur ajoutée nette (flux propriétaires, conformité ELM, support).
- **Niche verticale** (ex. uniquement boulangeries, uniquement santé) : défendable
  à court terme, mais réduit fortement le TAM et reste imitable.

**Conclusion :** pas d'avantage durable identifiable pour un produit horizontal.

## 6. Faisabilité & fiabilité technique

Architecture réaliste :

1. **Ingestion** : SIRENE géolocalisé + BPE + IRIS/contours + FiLoSoFi → PostGIS ou
   DuckDB spatial.
2. **Requêtes chiffrées (SQL)** : comptage concurrents par NAF dans buffer/isochrone ;
   population et revenu médian par IRIS intersecté ; densité BPE.
3. **Isochrones** : moteur routier (OSRM/Valhola) sur OSM — calcul, pas RAG.
4. **LLM (RAG sens uniquement)** : expliquer NAF, ELM, « pourquoi ce quartier » à
   partir de la doc INSEE et des métadonnées ; **interdit** de faire produire des
   chiffres par le LLM.

**Points de fragilité :**

- **Flux piéton / fréquentation** : pas de source nationale ouverte homogène → soit
  omettre (produit incomplet vs concurrence), soit acheter des données propriétaires
  (Mytraffic, etc.), soit afficher des comptages locaux épars avec avertissement —
  sinon risque de **sur-vendre** la fiabilité.
- **Géoloc SIRENE** : incomplète ou masquée ; BPE complète partiellement le commerce.
- **Prévision de CA** : modèles Huff/prédictifs = autre produit, données internes
  client souvent nécessaires (comme Galigeo/Mygeomarket).

Conforme au principe RAG(sens)/SQL(chiffres) **pour le cœur démo/concurrence** ;
**non conforme** si le pitch inclut flux/CA sans source traçable nationale.

## 7. Monétisation / impact

- **B2C indépendant** : freemium + étude à l'acte 20–60 € — **compressé** par
  Geomarket.one (42 € HT, ELM inclus) et Smappen (gratuit 10 zones).
- **B2B franchiseur** : abonnement 100–400 €/mois — marché occupé (Smappen, Data-B,
  Galigeo) avec exigence ELM et support.
- **Impact sociétal** : utile si gratuit et pédagogique, mais l'**Assistant
  Opportunités** et la **cartographie INSEE** couvrent déjà une partie du besoin
  sans monétisation.

Revenu réaliste pour un nouvel entrant horizontal : **faible**, sauf partenariat
institutionnel (CCI, banque) non identifié dans le seed.

## 8. Risques

- **Saturation / prix plancher** : Geomarket.one à 42 € HT et outils gratuits sur
  data.gouv.fr rendent l'acquisition payante très difficile.
- **Données flux** : promesse du pitch non tenable en open data pur → désavantage
  structurel vs Data-B/Smappen.
- **RGPD SIRENE** : statuts de diffusion, oppositions, usage commercial des données
  personnelles d'entrepreneurs.
- **Conformité ELM** (si cible franchise) : obligation légale (loi Doubin) ; erreur
  = responsabilité franchiseur — barrière de confiance pour un nouvel acteur.
- **Dépendance moteur isochrone** : coût infra + qualité routière OSM en zone
  dense.
- **Évolution NAF 2025** (bascule 2027) : maintenance référentiels.

## 9. Effort MVP

Périmètre minimal crédible (non trivial) :

1. Géocoder adresse candidat (BAN / API Géoplateforme).
2. Tracer zone 10–15 min voiture/pied (isochrone).
3. SQL : concurrents SIRENE/BPE par NAF dans la zone ; population + revenu médian
   IRIS ; comparaison vs moyenne communale.
4. Écran carte + fiche chiffrée traçable (lien dataset + date + requête).
5. Couche LLM : résumé en langage clair **sans chiffres inventés**.

**Hors MVP** (mais dans le pitch seed) : flux piéton, prévision CA, ELM conforme,
comparaison multi-emplacements, alertes réseau.

Estimation : **plus lourd** qu'un MVP data.gouv « tabulaire pur » (type DECP) à cause
du stack géospatial et de l'isochrone.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 | Mauvais emplacement = coût lourd et peu réversible pour commerçants/franchisés. |
| C2 | Cible solvable (qui paie) | 3 | 3 | 9 | Payeurs existent (franchiseurs, agents immo) mais ARPU bas et concurrence sur le même budget. |
| C3 | Disponibilité & fiabilité données | 3 | 3 | 9 | Cœur INSEE/SIRENE solide ; flux piéton et géoloc incomplète fragilisent le pitch complet. |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 | >10 produits sur data.gouv.fr + SaaS établis (Smappen, Data-B, Geomarket…) — marché saturé. |
| C5 | Différenciation défendable | 2 | 1 | 2 | « Open data + explication simple » déjà fait ; pas de moat technique ou réglementaire. |
| C6 | Faisabilité & fiabilité technique | 2 | 3 | 6 | SQL/RAG(sens) OK pour démo/concurrence ; flux/CA sans donnée nationale = fiabilité partielle. |
| C7 | Facilité du MVP | 2 | 2 | 4 | PostGIS, isochrones, NAF, multi-sources : effort supérieur à un produit tabulaire simple. |
| C8 | Maîtrise des risques | 2 | 2 | 4 | RGPD, ELM, guerre des prix à 42 €, dépendance données tierces pour flux. |
| C9 | Monétisation / impact | 2 | 2 | 4 | Monétisation possible en niche mais plafonnée ; impact déjà couvert par l'existant gratuit. |
| | **Total** | | | **52 / 105** | |

**Score /100** : 52 / 105 × 100 = **50**

## 11. Verdict & décision

❌ **Écartée.** Le besoin est réel (C1 élevé) mais le couple **saturation × prix
plancher × données flux non nationales** rend un nouvel assistant horizontal non
défendable. L'existant sur data.gouv.fr (Assistant Opportunités, Geomarket.one,
Smappen, Data-B, EoGIS) couvre déjà SIRENE + démographie + zones de chalandise, avec
des prix allant de **gratuit à 42 € HT** l'étude. Aucun critère éliminatoire
juridique ou absence de donnée sur le cœur SIRENE/INSEE, mais le score < 55 et
l'absence de créneau clair imposent l'écart.

**Prochaine étape :** ne pas prototyper ce horizontal. Si l'écosystème revient sur
l'implantation, explorer uniquement une **niche verticale** non couverte (secteur +
réglementation spécifique) ou un **partenariat d'acquisition** (CCI, réseau de
franchise) — sinon prioriser des idées à concurrence plus faible (ex. 0001).
