# Tensions emploi par territoire (France Travail × SIRENE × FiLoSoFi)

- **ID** : 0028
- **Statut** : 🔁 À retravailler
- **Score** : 58 / 100
- **Dernière mise à jour** : 2026-06-23
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
| **FiLoSoFi IRIS** | https://www.insee.fr/fr/statistiques/8229323 | LO (Insee) | CSV | Revenus 2021 | Communes ≥ 5 000 hab. ; **données 2021 = 5 ans de retard** |
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

## 4. Existant / concurrence

> Toutes les sources vérifiées le 2026-06-23.

### Concurrent direct et principal — France Travail officiel

**Data Emploi** ([https://dataemploi.francetravail.fr/](https://dataemploi.francetravail.fr/),
consulté 2026-06-23) : plateforme officielle France Travail, **gratuite et
publique**, qui présente déjà les tensions par métier × territoire (bassin emploi,
département, EPCI, commune). Indicateurs disponibles : demandeurs d'emploi par
métier ROME, difficultés de recrutement, offres enregistrées, dynamisme du
territoire (modèle IA prospectif), salaires proposés. Sources : France Travail +
ACOSS + CCMSA + DARES, MàJ trimestrielle. Exports PDF/Excel. **Couvre 80 % du
besoin cible sans aucun développement.**

### Concurrents géomarketing (segment franchiseurs)

**Smappen** ([https://smappen.fr/](https://smappen.fr/), consulté 2026-06-23) :
plateforme SaaS toulousaine, **3 M€ ARR, 1 230 clients dont 470 franchises**
(source : Le Journal des Entreprises, 2026). Zones isochrones + données
démographiques INSEE + SIRENE. **Aucune intégration France Travail tensions
emploi** confirmée. Tarifs : à partir de 49 €/mois. Concurrent direct sur le
segment franchiseur, mais sans la couche emploi.

**Geomarket / Data-B** : outils géomarketing avec données INSEE/SIRENE, sans
tensions emploi France Travail — positionnement similaire à Smappen.

### Outils RH enterprise (segment `hr-talent-ai`)

Les acteurs du catalogue `hr-talent-ai` (Paradox/Olivia, Eightfold, HireVue,
Greenhouse, Textio — tous `partial`, US, `france_market: partial`) sont des ATS
et outils d'assessment **centrés sur le processus de recrutement** — ils n'offrent
pas d'intelligence territoriale sur les tensions de marché du travail par commune.
Non substituables à 0028, mais occupent le budget RH des grandes entreprises.

### Autres acteurs publics

**CCI études de marché** : prestations humaines, pas de self-service. Coût
prohibitif pour une décision de localisation. **France Travail / Mes Services
Locaux** : consultation publique partielle (bassin emploi uniquement, pas commune).

### Benchmark catalogue SaaS — segments liés (`verified`/`partial` uniquement)

#### Segment `territorial-analytics`

| Acteur | Marché FR | Pertinence 0028 | Verdict |
|---|---|---|---|
| data.gouv.fr (`verified`, FR) | strong | Source primaire | Infrastructure, pas produit |
| OFGL Observatoire (`verified`, FR) | strong | Finances locales | Hors périmètre emploi |
| Géoportail (`verified`, FR) | strong | Cartographie | Hors périmètre emploi |
| CARTO (`partial`, ES) | partial | Dashboards territoriaux | Enterprise, pas self-service franchise |

#### Segment `hr-talent-ai`

| Acteur | Marché FR | Pertinence 0028 | Verdict |
|---|---|---|---|
| Paradox (Olivia) (`partial`, US) | partial | ATS/screening | Processus recrutement, pas territorial |
| Eightfold AI (`partial`, US) | partial | Workforce planning | Périmètre RH interne |
| HireVue (`partial`, US) | partial | Entretiens vidéo | Hors périmètre territorial |
| Textio (`partial`, US) | partial | Offres d'emploi IA | Hors périmètre territorial |
| Greenhouse (`partial`, US) | partial | ATS enterprise | Hors périmètre territorial |

Conclusion : **aucun acteur `hr-talent-ai` ne croise tensions emploi × territoire
pour des décisions d'implantation**. La niche est réelle mais déjà adressée par
Data Emploi (gratuit).

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

Fichier : [`catalogue-saas/vendors/hr-talent-ai.json`](../../catalogue-saas/vendors/hr-talent-ai.json) (19 entrées)

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
| … | _+7 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment territorial-analytics
```

<!-- catalogue-saas-end -->

## 5. Différenciation

La valeur différenciante est le **scoring composite SQL-traçable** : `score_territoire
= f(tension_recrutement_FT, revenus_FiLoSoFi, densité_concurrents_SIRENE)`.
Cela n'existe pas en self-service pour les franchiseurs. Mais :

- **Data Emploi** couvre déjà la couche emploi gratuitement.
- **Smappen** couvre déjà les couches démographiques + SIRENE pour les franchiseurs
  (3 M€ ARR = marché prouvé).
- La différenciation = **la synthèse des trois couches dans un seul score** pour
  un non-expert. Défendable à court terme, mais imitable par Smappen en quelques
  semaines (intégration API FT simple).
- Crédible comme **module/partenariat Smappen** plutôt que produit autonome.

## 6. Faisabilité & fiabilité technique

- Ingestion périodique APIs FT (après OAuth) + stock SIRENE + FiLoSoFi → DuckDB.
- Tous les indicateurs chiffrés = **SQL** avec source API + date d'appel.
- Dépendance **credentials France Travail** : risque de changement API / quotas.
- FiLoSoFi 2021 = 5 ans de retard — à afficher explicitement dans l'interface.
- Mapping ROME (métiers FT) ↔ NAF (secteurs SIRENE) = **heuristique** → documenter
  la couverture et les lacunes de correspondance.
- Principe RAG/SQL strict : score composite = SQL ; description du métier = RAG.

## 7. Monétisation / impact

| Modèle | Réalisme |
|---|---|
| Module ajout Smappen/Geomarket (API ou white-label) | Moyen — mais dépendance distributeur |
| Abonnement B2B franchiseurs directs | Moyen — Smappen est déjà là, difficile de vendre seul |
| Abonnement cabinets RH régionaux | Faible — budget limité |
| API B2B intégration SIRH | Moyen à long terme |

Smappen prouve que les franchiseurs paient (3 M€ ARR, 470 franchises). La couche
emploi FT est un différenciateur réel mais insuffisant pour un produit standalone.

## 8. Risques

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Smappen intègre APIs FT (concurrent direct) | Haute | Majeur | Go-to-market rapide, partenariat Smappen |
| Quota / changement API France Travail | Moyenne | Bloquant | Obtenir accord partenaire FT ; fallback BMO CSV |
| FiLoSoFi 2021 = données trop vieilles | Certaine | Réputation | Afficher le millésime ; attendre 2024 (INSEE) |
| Mapping ROME/NAF heuristique → erreurs sectorielles | Haute | Réputation | Publier taux de correspondance, documenter les trous |
| Data Emploi améliore son UX → réduit la niche | Moyenne | Modéré | Différencier sur le score composite franchise |

**Aucun risque éliminatoire** mais cumul de risques de mise en marché élevé.

## 9. Effort MVP

Périmètre minimal crédible :
1. Obtenir credentials OAuth France Travail (sandbox) — condition préalable.
2. Ingestion des 3 APIs FT pour 10 communes pilotes (ex. communes test franchise).
3. Jointure SIRENE NAF commerce par commune.
4. Score composite SQL : `(100 - tension_index_FT) × 0.4 + revenu_médian_FiLoSoFi_normalisé × 0.3 + densité_concurrence_inverse × 0.3`.
5. Interface web simple : carte + classement top 20 communes par secteur NAF.

Estimation : 6–8 semaines développeur. Bloqueur calendaire : obtention credentials
OAuth France Travail (délai administratif imprévisible).

## 10. Scoring

| # | Critère | Poids | Note | Pts |
|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | ×3 | 3 | 9 |
| C3 | Disponibilité & fiabilité des données | ×3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 2 | 4 |
| C5 | Différenciation défendable | ×2 | 3 | 6 |
| C6 | Faisabilité & fiabilité technique | ×2 | 3 | 6 |
| C7 | Facilité du MVP (effort faible) | ×2 | 3 | 6 |
| C8 | Maîtrise des risques | ×2 | 3 | 6 |
| C9 | Monétisation / impact | ×2 | 3 | 6 |
| | **Total** | | | **61 / 105** |

**Score /100 = round(61 / 105 × 100) = 58**

### Détail des notes

- **C1 = 3** : Besoin réel confirmé (Smappen = 3 M€ ARR, 470 franchises). Mais le
  besoin *spécifique* emploi FT est un **module**, pas le cœur de la douleur.
- **C2 = 3** : Franchiseurs paient (Smappen le prouve). Cabinets RH régionaux =
  budget modeste. Payeur identifié, segment de taille limitée.
- **C3 = 3** : APIs FT référencées data.gouv.fr ✅ (déc. 2025). SIRENE ✅.
  FiLoSoFi 2021 ⚠️ (5 ans de retard). OAuth FT = barrière d'accès non triviale.
  Mapping ROME/NAF = heuristique.
- **C4 = 2** : Data Emploi (FT officiel, gratuit) couvre tensions × territoire
  déjà. Smappen sert franchiseurs avec géomarketing. Niche = le croisement
  tripartite en un score, mais les composantes sont déjà servies séparément.
- **C5 = 3** : Score composite SQL-traçable unique en self-service franchise.
  Court terme défendable. Imitable par Smappen en quelques semaines.
- **C6 = 3** : SQL strict respecté. OAuth FT = dépendance externe (quotas,
  changements). Mapping ROME/NAF = heuristique à documenter.
- **C7 = 3** : 6–8 semaines. Bloqueur : OAuth FT (délai administratif). Pas
  trivial mais pas non plus un chantier de 6 mois.
- **C8 = 3** : Risques gérables (partenariat FT, fallback BMO CSV, affichage
  millésime FiLoSoFi). Aucun risque éliminatoire isolément, mais cumul significatif.
- **C9 = 3** : Potentiel de revenu réel (franchiseurs paient). Mais modèle viable
  = module/partenariat, pas SaaS standalone. Impact sociétal modéré.

## 11. Verdict & décision

🔁 **À retravailler** — Score **58/100** (zone 55–69).

**Point bloquant principal** : **Data Emploi** (France Travail, gratuit, officiel)
couvre déjà 80 % du besoin emploi × territoire. La valeur ajoutée réelle de 0028
est le **scoring composite franchise** (FT + SIRENE + FiLoSoFi) — trop mince pour
justifier un produit autonome face à Smappen qui sert déjà les franchiseurs.

**Condition pour avancer** : lever **l'un** de ces deux points :
1. **Partenariat Smappen** : intégrer la couche FT dans Smappen comme module B2B
   (distribution déjà existante, 1 230 clients). Lever bloquant go-to-market.
2. **Niche sectorielle spécifique** : cibler un type de franchise précis (ex.
   restauration rapide) avec un mapping ROME/NAF validé → réduire l'incertitude
   heuristique et concentrer l'effort.

**Prochaine étape** : (1) obtenir credentials OAuth France Travail sandbox et
valider 1 requête « tension métier commerce de détail » × commune pilote, ET (2)
tester l'intérêt d'un partenariat Smappen (contact commercial).
