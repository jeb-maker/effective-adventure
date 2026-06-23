# Aide au choix d'établissement scolaire (IPS + résultats)

- **ID** : 0013
- **Statut** : ❌ Écartée
- **Score** : 51 / 100
- **Dernière mise à jour** : 2026-06-23
- **Pitch (1 phrase)** : Comparer collèges/lycées pour des parents à partir des
  données ouvertes (annuaire, IPS, résultats brevet/bac, valeur ajoutée IVAL/IVAC,
  effectifs) — un créneau **déjà servi par l'État, la presse et plusieurs
  réutilisations gratuites**.

---

## 1. Problème / douleur
Choisir un établissement (ou demander une dérogation, anticiper un déménagement,
arbitrer public/privé) est un moment à fort enjeu émotionnel pour les parents :
les indicateurs existent mais sont dispersés (annuaire, IPS, IVAL/IVAC, effectifs)
et techniques à lire (taux « brut » vs « valeur ajoutée », IPS et son écart-type).

Nuances qui réduisent la douleur réelle :
- Pour le **collège public**, le choix est largement contraint par la **carte
  scolaire** (sectorisation) : on ne « choisit » pas vraiment, on est affecté. Le
  vrai besoin de comparaison se concentre sur les **lycées** (Affelnet,
  spécialités), le **privé**, les **dérogations** et les **déménagements**.
- C'est une douleur **ponctuelle** (une fois par enfant, à chaque transition),
  pas récurrente — peu propice à un abonnement.
- Le besoin est **déjà très bien couvert** gratuitement (voir §4), ce qui abaisse
  la douleur résiduelle non servie.

## 2. Cible & qui paie
- **Parents** : utilisateurs principaux, mais **ne paient pas** pour ce type
  d'info (gratuit partout) et usage ponctuel → pas de payeur.
- **Journalistes / chercheurs** : utilisateurs réels mais budget faible ; ils
  consomment surtout la donnée brute (déjà ouverte) et publient eux-mêmes les
  classements (Figaro, Parisien, L'Étudiant, franceinfo).
- **Payeurs hypothétiques** (à explorer, non validés) : agences de **relocation /
  expatriation**, services RH de mobilité, acteurs **immobiliers** (la qualité
  scolaire influence l'attractivité d'un quartier). → piste B2B, mais **aucun
  budget nommé/sourcé** à ce stade.

Utilisateur ≠ payeur, et le payeur n'est pas identifié : faiblesse majeure.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| Annuaire de l'éducation (66 000+ étabts) | https://www.data.gouv.fr/datasets/annuaire-de-leducation | Licence Ouverte 2.0 | CSV / JSON + API Explore | MàJ 2026-06-13 | Source ONISEP/RAMSESE ; champs déclaratifs, complétude variable (mail, sections) |
| API Annuaire Éducation nationale | https://www.data.gouv.fr/dataservices/annuaire-de-leducation-nationale | Licence Ouverte 2.0 | API REST (Opendatasoft) | continue | Recherche/géoloc OK ; pas d'indicateurs de résultats |
| Adresse & géolocalisation des étabts 1er/2nd degré | https://www.data.gouv.fr/datasets/adresse-et-geolocalisation-des-etablissements-denseignement-des-premier-et-second-degres | Licence Ouverte 2.0 | CSV | MàJ 2026-06-19 | Géoloc seule (RAMSESE) ; à joindre par UAI |
| IPS collèges (≥2023) | https://data.education.gouv.fr/explore/dataset/fr-en-ips-colleges-ap2023/ | Licence Ouverte 2.0 | CSV / API | annuelle | Rupture de série 2022 (changement méthodo) ; IPS privé 2023 +3 pts (remontée 2e PCS) non comparable ; non renseigné si <5 élèves |
| IPS lycées (≥2023) | https://www.data.gouv.fr/datasets/ips-lycees-a-partir-de-2023 | Licence Ouverte 2.0 | CSV / API | MàJ 2026-04-14 | Idem rupture/comparabilité ; COM/Nouvelle-Calédonie depuis 2025-26 |
| IVAL — lycées général & techno | https://data.education.gouv.fr/explore/dataset/fr-en-indicateurs-de-resultat-des-lycees-gt_v2/ | Licence Ouverte 2.0 | CSV / API | MàJ 2026-04-03 | « Valeur ajoutée » = indicateur relatif, mal compris du grand public ; séries 2012→2025 |
| IVAC — collèges (résultats DNB + valeur ajoutée) | https://data.education.gouv.fr/explore/dataset/fr-en-indicateurs-valeur-ajoutee-colleges/ | Licence Ouverte 2.0 | CSV / API | annuelle (2022→2025) | VA diffusée seulement si ≥40 présents série générale (seuil relevé en 2024) ; pas de VA si <75 % scores 6e retrouvés |
| DNB par établissement | https://www.data.gouv.fr/datasets/diplome-national-du-brevet-par-etablissement-1 | Licence Ouverte 2.0 | CSV | **gelé** (MàJ 2026-02-06, plus actualisé) | **Déprécié** : le ministère renvoie vers IVAC pour le DNB |

Toutes les sources sont **tabulaires, propres et jointes par code UAI** → socle
idéal pour des requêtes SQL fiables. La donnée n'est pas le problème ; elle est
même la grande force du dossier. (Sources consultées 2026-06-20.)

## 4. Existant / concurrence

> Cartographie B (consultée 2026-06-23).

**Verdict de saturation : SATURÉ au niveau produit.** Le besoin est couvert
gratuitement par l'État, la presse nationale et plusieurs réutilisations.

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **DEPP — Indicateurs collèges/lycées** | https://www.education.gouv.fr/depp/les-indicateurs-de-resultats-des-colleges-et-des-lycees-377729 | Moteur officiel IVAL/IVAC par établissement |
| **Annuaire de l'éducation** | https://www.education.gouv.fr/annuaire | Fiches établissements, effectifs, options |
| **service-public.fr — IPS** | https://www.service-public.gouv.fr/particuliers/actualites/A17256 | Relais citoyen indicateurs scolaires |
| **data.education.gouv.fr** | https://data.education.gouv.fr/ | Open data éducation (effectifs, résultats) |

### Réutilisations data.gouv

| Acteur | URL | Rôle |
|---|---|---|
| **Comparatif des lycées près de chez vous** | https://www.data.gouv.fr/reuses/comparatif-des-lycees-pres-de-chez-vous | Saisie adresse, comparaison 4 lycées (IPS, bac, effectifs) |
| **Carte des établissements** | https://www.data.gouv.fr/reuses/carte-des-etablissements-scolaires | Géolocalisation écoles/collèges/lycées |

### Presse (classements annuels gratuits)

- **Le Figaro Étudiant** — palmarès lycées + moteur par étabt :
  https://etudiant.lefigaro.fr/lycee/classement/ (2026-06-23).
- **Le Parisien Étudiant** — classement noté /20, critères réussite/mentions/VA/
  mixité/spécialités : https://www.leparisien.fr/etudiant/lycee/classement-des-lycees-quels-sont-les-meilleurs-etablissements-de-france-en-2026-LIFJ6QDYEVD7HESSPVY4KC6R5I.php (2026-06-23).
- **L'Étudiant** — 5 indicateurs à poids égal, 2 valeurs ajoutées, indice de
  stabilité (≈2 205 lycées évalués) : https://fr.style.yahoo.com/classement-lyc%C3%A9es-2026-accompagnement-%C3%A9l%C3%A8ves-033100902.html (2026-06-23).
- **franceinfo** — moteurs de recherche lycées **et collèges** (revendique de ne
  PAS hiérarchiser) : https://www.franceinfo.fr/bac/classement-des-lycees/meilleurs-lycees-et-colleges-en-2026-consultez-les-indicateurs-de-reussite-et-comparez-les-etablissements-autour-de-chez-vous_7908476.html (2026-06-23).

### Produits / plateformes communautaires

- **Vis-Ma-Classe.fr** : 68 842 établissements, IPS + jauge vs moyennes nat/acad/
  dépt, IVAL/IVAC, DNB, REP/REP+, carte. https://vis-ma-classe.fr/ (2026-06-23).
- **Lucyol.fr** : cartes interactives écoles/collèges/lycées, comparateurs
  côte-à-côte, **sectorisation collège par adresse**, classements maison,
  comparateur Parcoursup. https://www.lucyol.fr/ et https://www.lucyol.fr/outils (2026-06-23).

**Contexte (sensibilité du sujet)** : la publication des IPS résulte d'un combat
de transparence (journaliste A. Léchenet, décision du TA de Paris du 2022-07-13,
mise en ligne oct. 2022) ; ces données alimentent le débat sur la **ségrégation
scolaire** et la carte scolaire. https://www.politico.eu/article/coulisses-ips-indicateur-secoue-mixite-ecole-pap-ndiaye/
et https://www.sudouest.fr/politique/education/ecoles-et-colleges-ce-journaliste-a-obtenu-la-publication-des-indicateurs-de-position-sociale-12830370.php (2026-06-23).

**Où est l'espace libre ?** Quasi nul sur « comparer collèges/lycées pour
parents ». Créneaux résiduels étroits : (a) **B2B** (relocation/immobilier/RH
mobilité) avec API + scoring sur critères clients ; (b) **anti-classement** :
aide à la décision pédagogique/déontologique (lecture de la valeur ajoutée, mise
en garde contre l'IPS comme proxy de « niveau »), créneau peu rentable.

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0013-choisir-son-ecole` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `territorial-analytics` — Analytics territoriales

Fichier : [`catalogue-saas/vendors/territorial-analytics.json`](../../catalogue-saas/vendors/territorial-analytics.json) (26 entrées)

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
| `smappen` | Smappen | FR | strong | verified |
| `geomarket` | Geomarket | FR | strong | verified |
| `data-b` | Data-B | FR | strong | partial |
| `vigicite` | VigiCité | FR | strong | verified |
| … | _+14 autres_ | | | |

#### Segment `learning-lxp` — Formation & LXP

Fichier : [`catalogue-saas/vendors/learning-lxp.json`](../../catalogue-saas/vendors/learning-lxp.json) (18 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `docebo` | Docebo | US | partial | partial |
| `360learning` | 360Learning | FR | strong | partial |
| `cornerstone` | Cornerstone OnDemand | US | partial | partial |
| `degreed` | Degreed | US | partial | partial |
| `absorb-lms` | Absorb LMS | US | partial | partial |
| `rise-up` | Rise Up | FR | strong | partial |
| `didask` | Didask | FR | strong | partial |
| `teach-on-mars` | Teach on Mars | FR | strong | partial |
| `crossknowledge` | CrossKnowledge (Wiley) | FR | strong | partial |
| `learnworlds` | LearnWorlds | CY | partial | partial |
| `talentlms` | TalentLMS | US | partial | partial |
| `edflex` | Edflex | FR | strong | partial |
| … | _+6 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment territorial-analytics
```

<!-- catalogue-saas-end -->
## 5. Différenciation
Faible et **copiable en un week-end** — et déjà copié plusieurs fois. Le pipeline
(annuaire + IPS + IVAL/IVAC joints par UAI, carte, fiche, comparateur 4 étabts)
est exactement ce que proposent Vis-Ma-Classe, Lucyol et la réutilisation
data.gouv. Aucun moat : même donnée, même Licence Ouverte, même rendu. La seule
différenciation crédible serait un **pivot** (B2B relocation/immobilier, ou
posture « anti-classement » pédagogique), pas le comparateur grand public.

## 6. Faisabilité & fiabilité technique
Très favorable **sur le plan technique** : données tabulaires propres jointes par
**UAI** → DuckDB/SQL. Tous les chiffres affichés (IPS, écart-type, taux de
réussite/mention/accès, valeur ajoutée, effectifs) viennent **directement des
fichiers DEPP** (SQL traçable, aucun calcul inventé). Un LLM ne servirait qu'à
**expliquer le sens** (qu'est-ce que l'IPS, comment lire une VA négative,
avertissements de comparabilité) → **RAG sur le sens, SQL sur les chiffres**,
conforme au principe. Risque d'hallucination quasi nul. Le vrai risque n'est pas
technique mais **interprétatif** : afficher un IPS/VA sans pédagogie induit des
lectures fausses (IPS ≠ qualité d'enseignement ; VA = mesure relative).

## 7. Monétisation / impact
- **Revenu grand public : ~nul.** Personne ne paie pour ce que l'État, la presse
  et 2-3 sites font gratuitement ; usage ponctuel, pas d'abonnement.
- **Impact : déjà capté** par les acteurs existants (transparence, débat carte
  scolaire). Un énième comparateur n'ajoute pas d'impact marginal.
- Seule monétisation crédible = **B2B** (API/intégration relocation, immobilier,
  RH mobilité) — mais payeur **non validé** (à vérifier).

## 8. Risques
- **Saturation concurrentielle** (État + presse + réutilisations gratuites) : tue
  l'acquisition et tout pricing grand public.
- **Risque éthique/réputationnel** : un classement renforce la **ségrégation**
  (fuite vers les « bons » étabts) ; l'IPS est un indicateur **social**, pas de
  qualité — son détournement est un risque image et de société. Non strictement
  éliminatoire (données officielles, publiques et légales) mais impose une posture
  prudente et une pédagogie forte.
- **Comparabilité des données** : ruptures de série IPS (2022), bond IPS privé
  2023, seuils de diffusion VA (≥40 présents) → comparaisons naïves trompeuses.
- **Absence de payeur** : risque économique de fond.

## 9. Effort MVP
Faible (et c'est paradoxalement un signal de banalité) : ingestion annuaire + IPS
+ IVAL/IVAC + géoloc → DuckDB (jointure UAI) ; 3 vues (fiche établissement, carte,
comparateur ≤4) ; encarts pédagogiques + avertissements de comparabilité ;
chaque chiffre tracé à sa source DEPP + millésime. Réalisable rapidement — donc
sans barrière à l'entrée pour qui que ce soit.

## 10. Scoring

> **Scoring ajusté après revue critique du 2026-06-23** (voir [`revue.md`](revue.md)).
> Notes abaissées : C1 (3→2), C2 (2→1), C7 (5→4). Score 59 → **51**, verdict
> 🔁 → ❌. Les notes initiales de la fiche sont rappelées dans la colonne dédiée.

| # | Critère | Poids | Note initiale | Note (post-revue) | Pondéré |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 2 | 6 |
| C2 | Cible solvable (qui paie) | 3 | 2 | 1 | 3 |
| C3 | Disponibilité & fiabilité données | 3 | 5 | 5 | 15 |
| C4 | Espace concurrentiel libre | 2 | 1 | 1 | 2 |
| C5 | Différenciation défendable | 2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | 2 | 5 | 5 | 10 |
| C7 | Facilité du MVP | 2 | 5 | 4 | 8 |
| C8 | Maîtrise des risques | 2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | 2 | 2 | 2 | 4 |
| | **Total** | | | | **54 / 105** |

**Score /100** : 54 / 105 × 100 = **51**

Justification note par note (post-revue) :
- **C1 = 2** (ajusté) : douleur **ponctuelle** (une fois par enfant), **contrainte**
  par la carte scolaire au collège, et déjà très servie gratuitement → besoin tiède
  côté marchand.
- **C2 = 1** (ajusté) : **aucun payeur identifié** — parents ne paient pas,
  journalistes/chercheurs à petit budget, et le B2B (relocation/immobilier/RH) est
  reconnu « non sourcé/non validé » par la fiche elle-même.
- **C3 = 5** : données complètes, propres, ouvertes (Licence Ouverte 2.0),
  jointes par UAI, mises à jour annuellement — quasi idéales.
- **C4 = 1** : saturé (DEPP + Figaro/Parisien/L'Étudiant/franceinfo + réutilisations
  data.gouv + Vis-Ma-Classe + Lucyol), **et saturation aggravée 2026-06-23**
  (EducaScore créé le 10/06/2026, EcoleScope, EcolesInfo).
- **C5 = 1** : aucun moat, pipeline copiable en un week-end et déjà copié plusieurs fois.
- **C6 = 5** : chiffres 100 % SQL/traçables, LLM cantonné au sens → fiabilité par
  construction.
- **C7 = 4** (ajusté) : MVP rapide, mais un comparateur **crédible** doit neutraliser
  les pièges de comparabilité (rupture série IPS 2022, seuils VA, IPS ≠ niveau) →
  coût réel, pas trivial.
- **C8 = 2** : risques économiques (pas de payeur) et éthiques (classements,
  ségrégation, mésusage de l'IPS) réels quoique non illégaux.
- **C9 = 2** : revenu grand public ~nul et impact déjà capté ; seule porte = B2B
  non validé.

## 11. Verdict & décision
❌ **Écartée** (score **51/100** après revue critique du 2026-06-23, < 55).
L'analyse initiale plaçait l'idée à 59 (« 🔁 à retravailler ») tout en concédant que
« sans pivot, le verdict de fait est proche du rejet ». La revue acte ce rejet en
corrigeant des notes complaisantes (C1 : douleur ponctuelle et contrainte ; C2 :
**aucun payeur identifié**, le B2B étant non sourcé ; C7 : MVP crédible exige des
garde-fous de comparabilité). Le dossier garde une **donnée excellente** (C3=5,
C6=5), mais échoue là où ça compte : **espace concurrentiel saturé** (C4=1) — et
**en aggravation** (EducaScore créé le 10/06/2026, EcoleScope, EcolesInfo) —,
**différenciation nulle** (C5=1) et **absence de payeur** (C2=1). Reconstruire un
énième comparateur grand public n'a aucun sens.

**Prochaine étape concrète** : ne PAS construire le comparateur grand public.
Tester en une page de validation l'**unique angle défendable** : un **payeur B2B
nommé** (agences de relocation/expatriation ou acteurs immobiliers) prêt à payer
une **API enrichie « qualité scolaire d'une adresse »** (sectorisation + IPS +
IVAL/IVAC normalisés, avec avertissements de comparabilité). Si aucun payeur ne
se confirme sous cet angle, **basculer l'idée en ❌ Écartée** (saturation + pas de
modèle).

0013 | Aide au choix d'établissement scolaire (IPS + résultats) | ❌ Écartée | 51/100 | Donnée parfaite mais marché saturé (aggravé 2026) et sans payeur ; revue 2026-06-23
