# Exposition risques des parcelles agricoles (RPG × Géorisques × Hub'Eau)

- **ID** : 0026
- **Statut** : ❌ Écartée
- **Score** : 52 / 100
- **Dernière mise à jour** : 2026-06-21
- **Pitch (1 phrase)** : Cartographier l'exposition des parcelles agricoles aux
  risques industriels (ICPE), hydriques et réglementaires (PLU) en croisant le
  Registre parcellaire graphique, Géorisques et Hub'Eau — pour agriculteurs,
  coopératives, aménageurs ruraux et collectivités.

---

## 1. Problème / douleur

Un acteur territorial (chambre d'agriculture, DDT, EPCI rural, aménageur) qui
étudie un bassin versant ou une zone agricole doit croiser manuellement :

- le **RPG** (occupation des sols, assolements),
- les **ICPE / BASIAS** (Géorisques),
- la **qualité / quantité de l'eau** (Hub'Eau),
- le **zonage PLU** (pression urbanisation).

Ces données sont ouvertes mais **dispersées** entre portails SIG, APIs unitaires
et couches WMS. La douleur est **réelle pour les structures de développement
territorial** — moins pour l'agriculteur individuel, qui passe par la PAC/Télépac
et des conseillers.

**Nuances importantes** :
- Le RPG open data est **anonymisé** (pas de lien exploitation individuelle sans
  habilitation ASP) — instruction DGPE/SDGP/2 (consulté 2026-06-21 :
  https://info.agriculture.gouv.fr/boagri/instruction-2022-106/telechargement).
- Depuis le millésime **2024**, le RPG se décompose en **7 bases** (plus une seule
  table) — https://cartes.gouv.fr/aide/fr/partenaires/ign/generalites-ign/actualites/2025-11-rpg24/
  (consulté 2026-06-21).

---

## 2. Cible & qui paie

| Segment | Besoin | Payeur ? |
|---|---|---|
| **Chambres d'agriculture / DDT / OFB** | Diagnostic territorial, politiques publiques | Budget public — outils internes ou prestations |
| **EPCI ruraux / syndicats de bassin** | Planification, captages, ICPE | Budget public |
| **Agriculteurs / CUMA** | « Ma parcelle est-elle exposée ? » | **Non** (sensible au prix) |
| **Aménageurs fonciers** | Pression PLU + contraintes env. | Déjà clients **Kel Foncier / Géofoncier** (0021) |

**Verdict C2** : pas de payeur SaaS récurrent identifié ; marché = **prestations
SIG/conseil** ou **logiciels publics gratuits** (RPG Explorer).

---

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| **RPG** (IGN/ASP) | https://www.data.gouv.fr/datasets/registre-parcellaire-graphique-agricole — flux : https://geoservices.ign.fr/rpg | LO 2.0 | CSV/GeoJSON/WFS | MàJ **20 juin 2026** ; millésime 2024 = 7 BDD | Anonymisé ; métropole ; évolution format 2024 |
| **API Géorisques** | https://www.data.gouv.fr/dataservices/api-georisques | LO 2.0 | REST JSON | Continue | **10 req/s** ; pas de batch ; 1 point/coord |
| **Hub'Eau** | https://hubeau.eaufrance.fr/ — hydrométrie v2 testée 2026-06-21 | LO 2.0 | REST JSON | API v2.0.1 opérationnelle | Endpoints multiples ; pas un dump unique |
| **GPU / PLU** | https://www.geoportail-urbanisme.gouv.fr/ | LO 2.0 | WFS/WMS | Continue | Qualité hétérogène entre communes |
| **PCI / cadastre** | https://www.data.gouv.fr/datasets/cadastre | LO 2.0 | GeoJSON | Continue | Jointure RPG ↔ parcelle |

[`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements

| Croisement | Technique | Bloquant |
|---|---|---|
| RPG × ICPE (500 m) | PostGIS ST_DWithin sur shapefiles ICPE | Volume national lourd |
| RPG × Hub'Eau | Stations à proximité du centroïde parcelle | Bassin versant ≠ proximité euclidienne |
| RPG × GPU | Zonage constructible | Interprétation PLU ≠ automatisable |
| Batch national parcelles × Géorisques API | 1 req/point | **Quota 10 req/s** = inviable sans dump spatial ICPE |

---

## 4. Existant / concurrence

**Verdict saturation : SATURÉ** sur l'analyse RPG territoriale ; **partiellement
couvert** sur le croisement env. complet (ICPE × eau × PLU).

### Concurrent direct RPG (gratuit, public)

| Produit | URL | Ce qu'il fait | Prix (2026-06-21) |
|---|---|---|---|
| **RPG Explorer** (INRAE / AgroParisTech / SADAPT) | https://rpgexplorer.fr/ | Logiciel **gratuit** : assolements, rotations, dynamiques parcellaires, évolution paysage ; lauréat **prix national science ouverte 2025** — https://www.agroparistech.fr/actualites/rpg-explorer-laureat-prix-national-science-ouverte-2025 | **Gratuit** ; formation en ligne |
| **Géoportail — couche RPG** | https://geoservices.ign.fr/actualites/2024-08-rpg2023 | Visualisation WMS/WFS RPG | Gratuit |
| **Télépac / portail agriculteur** | (ASP) | Déclaration PAC, pas croisement risques | Gratuit agriculteurs |

### Concurrents SIG / foncier (adjacents)

| Produit | URL | Recoupement |
|---|---|---|
| **Géorisques** | https://www.georisques.gouv.fr/ | Fiche risques à l'adresse/coord — unitaire |
| **Géofoncier / Kel Foncier** | cf. 0021 | Fiche parcelle PLU + risques — angle **foncier BTP**, pas agricole |
| **Errial** | Service public | Risques adresse — pas RPG |

**Ce qui manque** : une fiche « parcelle agricole RPG + ICPE + eau + PLU » en un
clic pour non-SIG. Mais **RPG Explorer** couvre déjà 80 % de la valeur pour les
organismes publics agricoles ; le reste relève de **prestations SIG** (consultants,
DDT) plutôt que d'un SaaS.

---

## 5. Différenciation

**Faible.** Le croisement spatial ICPE × RPG est reproductible en QGIS/PostGIS par
tout cabinet SIG. **RPG Explorer** est gratuit, institutionnellement légitime (INRAE,
prix science ouverte 2025) et déjà adopté par les structures de développement.

L'angle « fiche parcelle agricole unifiée » n'est pas défendable face à :
- RPG Explorer (occupation sols),
- Géorisques (risques ponctuels),
- prestataires SIG locaux (DDT, chambres d'agri).

---

## 6. Faisabilité & fiabilité technique

- **PostGIS** pour RPG + couches ICPE en shapefile (dump Géorisques) = faisable
  **département pilote**.
- **Batch national** via API Géorisques unitaire = **non viable** (quota 10 req/s).
- Chiffres (surface, distance ICPE, nb stations) = **SQL/spatial traçable**.
- LLM : explication ICPE/PLU uniquement (RAG sens).
- **Risque métier** : proximité ICPE ≠ impact agricole ; eau = station lointaine.

---

## 7. Monétisation / impact

- **Revenu** : quasi nul en SaaS ; marché = marchés publics de prestation (DDT,
  chambres d'agri) utilisant RPG Explorer + QGIS.
- **Impact** : utile pour politiques publiques — déjà porté par RPG Explorer et
  financements OFB/ADEME (cité sur agroparistech.fr, 2026-06-21).

---

## 8. Risques

- **Concurrence gratuite** RPG Explorer (internalisation par l'écosystème recherche-public).
- **Complexité format RPG 2024** (7 bases) — coût maintenance.
- **Quota Géorisques** si approche API naïve.
- **Attentes sur-analysées** : PLU ≠ constructibilité automatique.

---

## 9. Effort MVP

**Élevé** pour un MVP crédible national :
1. Ingestion RPG millésime (GeoPackage département).
2. Couches ICPE shapefile (téléchargement massif Géorisques).
3. PostGIS ST_DWithin parcelle-ICPE.
4. Hub'Eau stations proximité.
5. Interface carte.

Un **pilote 1 département** est faisable ; produit national = chantier SIG lourd
sans payeur.

---

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 |
| C4 | Espace concurrentiel libre | 2 | 2 | 4 |
| C5 | Différenciation défendable | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | 2 | 3 | 6 |
| C7 | Facilité du MVP | 2 | 2 | 4 |
| C8 | Maîtrise des risques | 2 | 3 | 6 |
| C9 | Monétisation / impact | 2 | 2 | 4 |
| | **Total** | | | **55 / 105** |

**Score /100** : 55 / 105 × 100 = **52**

Justification :
- **C1 = 3** : douleur réelle pour organismes publics, pas aiguë pour agriculteur.
- **C2 = 2** : budget public / prestation, pas SaaS.
- **C3 = 4** : RPG, Géorisques, Hub'Eau ouverts ; format RPG 2024 complexifié.
- **C4 = 2** : RPG Explorer gratuit et reconnu ; Géorisques/Géofoncier adjacents.
- **C5 = 2** : croisement SIG copiable ; pas de moat.
- **C6 = 3** : PostGIS OK ; API Géorisques batch = bloquant.
- **C7 = 2** : MVP national lourd.
- **C8 = 3** : risques concurrence gratuite et sur-interprétation.
- **C9 = 2** : impact public existant via RPG Explorer.

---

## 11. Verdict & décision

❌ **Écartée** (score **52/100**, < 55).

Le croisement RPG × risques est **techniquement pertinent** mais **économiquement
non viable** en produit autonome : **RPG Explorer** (gratuit, INRAE/AgroParisTech,
prix science ouverte 2025) couvre déjà l'analyse territoriale RPG pour les
organismes publics ; le complément ICPE/eau relève de workflows SIG existants
(DDT, chambres d'agri) ou de **Géofoncier/Kel Foncier** pour l'angle foncier.

**Prochaine étape** : aucun prototype recommandé. Si intérêt persistant : contribuer
à **RPG Explorer** ou à une couche WMS « ICPE × bassin versant » côté OFB/DDT
 plutôt qu'un SaaS tiers.

**Liens** : extension agricole de [0021](../0021-veille-fonciere-amenageurs/) (écartée)
 et [0011](../0011-risques-adresse/) (risques unitaires).
