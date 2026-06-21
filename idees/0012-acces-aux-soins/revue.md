# Rapport de revue critique — Idée 0012 « Observatoire de l'accès aux soins »

**Réviseur** : agent red team indépendant  
**Date de revue** : 2026-06-20  
**Fiche auditée** : `idees/0012-acces-aux-soins/README.md` (score déclaré : 57/100, statut 🔁 À retravailler)  
**Méthode** : `docs/methode-analyse.md` + `docs/prompts/03-revue-critique.md`  
**Vérifications web** : consultées le 2026-06-20 (sources citées en §4)

---

## Synthèse exécutive

L'analyse est **globalement lucide** sur la saturation du créneau « mesurer/cartographier » et sur l'absence de payeur pour un doublon de CartoSanté/Rézone. Le texte du verdict (§11) est plus sévère que le score : il qualifie le seed de « de fait écarté » tout en conservant un statut 🔁 grâce à un score à 57.

**Faille majeure de la fiche** : l'inventaire concurrentiel est **incomplet au moment de la rédaction**. Entre le 11 et le 17 juin 2026, l'**Observatoire SKEMA-UniCA de l'accès aux soins** a été lancé publiquement — avec le même positionnement (« observatoire », national → infra-communal, 22 catégories, données CNAM/Insee). De plus, l'**Observatoire de l'accès aux soins** de l'Assurance Maladie (Data ameli, sept. 2025) n'est pas cité, alors qu'il porte **littéralement le nom du produit envisagé**.

Le score 57 est **légèrement complaisant** sur C2, C5, C7, C8 et C9. Recalcul adversarial : **44/100** → seuil ❌ Écartée.

---

## 1. Affirmations non sourcées

| Affirmation (fiche) | Problème | Verdict |
|---|---|---|
| « budget attractivité médicale réel mais fléché vers des aides à l'installation, pas vers un nouvel outil cartographique » (§2) | Aucun lien ni entretien ; affirmation économique non démontrée | **À sourcer** (budgets ARS/collectivités, marchés publics) ou **à nuancer** |
| « accompagnement ARS gratuitement » pour les collectivités (§2) | Vrai en pratique via PAPS/CartoSanté, mais non sourcé | **À sourcer** — ex. https://sante.gouv.fr/professionnels/se-former-s-installer-exercer/article/les-portails-d-accompagnement-des-professionnels-de-sante-paps (consulté 2026-06-20) |
| « Rézone — cartographie nationale (toutes régions) » (§4) | Le datalogue IdF mentionne encore « treize régions » ; la couverture nationale est plausible via PAPS mais pas prouvée par le lien fourni | **À sourcer** avec URL d'accès national (ex. portail ameli/PAPS) |
| CartoSanté : « 8 professions libérales » (§4) | data.gouv.fr et ARS indiquent **8+ professions** (ophtalmologues, orthoptistes ajoutés depuis nov. 2023) | **À corriger** — https://www.data.gouv.fr/fr/datasets/cartosante/ (consulté 2026-06-20) |
| « pas de produit commercial dominant » (§4) | Explicitement « recherche non exhaustive » — recevable comme hypothèse, mais insuffisant pour C4/C5 | **À approfondir** (Guide Santé, médias, éditeurs B2G) |
| « copiable en un week-end » (§5, §10) | Opinion de l'analyste, pas de benchmark effort | **À sourcer** ou reformuler en jugement qualitatif |
| Metric Insee : URL « *(à vérifier l'URL exacte de diffusion)* » (§3) | L'analyste signale lui-même l'incertitude ; la méthode exige URL + fraîcheur | **À sourcer** avant tout MVP |
| « déjà intégré dans l'APL » pour Metric et population Insee (§3) | Correct méthodologiquement (DREES cite Metric) mais sans lien direct dans la fiche | **À sourcer** — https://drees.solidarites-sante.gouv.fr/sources-outils-et-enquetes/lindicateur-daccessibilite-potentielle-localisee-apl (consulté 2026-06-20) |

**Affirmations correctement sourcées** (vérifiées) :
- 87 % fragilité médicale, 151 intercommunalités « zones rouges », ~2–2,5 M habitants — confirmé par la réutilisation data.gouv et presse du 27/06/2025.
- APL MG 3,3 en 2022/2023 vs 3,8 en 2015 — confirmé communiqué DREES.
- CartoSanté 300+ indicateurs, Atlasanté — confirmé data.gouv.fr.

---

## 2. Sur-optimisme du scoring

| Critère | Note fiche | Note revue | Justification adversarial |
|---|---|---|---|
| **C1** Intensité du problème | 4 | **4** | La douleur macro (déserts médicaux) est réelle et politiquement saillante ; la fiche distingue correctement douleur sociétale ≠ douleur produit. Pas de surévaluation majeure. |
| **C2** Cible solvable (qui paie) | 2 | **1** | ARS **produisent** CartoSanté ; la CNAM a lancé l'« Observatoire de l'accès aux soins » (sept. 2025, Data ameli) ; SKEMA-UniCA (juin 2026) vise les mêmes décideurs publics gratuitement. Aucun payeur identifié, et l'espace B2G se referme. Sources : https://www.assurance-maladie.ameli.fr/presse/2025-09-25-cp-lancement-observatoire-acces-soins , https://www.skema.edu/fr/news/deserts-medicaux-skema-business-school-et-universite-cote-dazur-lancent-le-premier (consultés 2026-06-20). |
| **C3** Données | 4 | **3** | Données APL/RPPS/FINESS existent et sont SQL-compatibles, mais : fréquence APL irrégulière (signalée), refonte FINESS été 2026, URL Metric non validée, indicateurs CNAM les plus frais issus du **SNDS** (non entièrement ouverts). « Prêtes » ≠ « sans risque opérationnel ». |
| **C4** Espace concurrentiel | 1 | **1** | Note cohérente. La saturation s'est **aggravée** depuis la rédaction (SKEMA-UniCA). |
| **C5** Différenciation | 2 | **1** | La fiche admet une différenciation « faible » sur le seed. Les pivots (matching, spécialistes, API) sont hors périmètre du pitch et non validés commercialement. À ce stade, c'est dupliquer l'existant — ancrage 1 du barème. |
| **C6** Faisabilité technique | 4 | **4** | Architecture RAG(sens)/SQL(chiffres) adaptée ; données structurées communales. Réserve RGPD RPPS légitime mais ne justifie pas de descendre sous 4 sur la **technique pure**. |
| **C7** Facilité MVP | 3 | **2** | Techniquement rapide à coder, mais la fiche dit elle-même le MVP serait « inutile ». Un MVP sans valeur livrable n'est pas « facile » au sens du barème (MVP **crédible**). |
| **C8** Maîtrise des risques | 3 | **2** | RGPD, mésinterprétation et réputation territoriale sont cités, mais manquent : homonymie avec l'observatoire CNAM (risque confusion/marque), contexte législatif Garot (débats Sénat 11/06/2026), dépendance à des outils publics gratuits rendant tout doublon politiquement sensible. |
| **C9** Monétisation / impact | 2 | **1** | Impact sociétal fort, mais **impact différentiel du produit** quasi nul face aux outils publics + SKEMA + médias (Franceinfo). Revenu non démontré ; le gratuit institutionnel est un mur, pas un obstacle mineur. |

---

## 3. Risque d'hallucination / RAG(sens)–SQL(chiffres)

### Points conformes
- La fiche impose correctement SQL pour APL, comptes PS, FINESS, temps d'accès.
- Le LLM limité aux définitions/méthodologie est le bon pattern.
- Les chiffres cités (87 %, 151 EPCI, APL 3,3/3,8) sont **traçables** vers DREES/data.gouv.

### Risques non traités ou sous-estimés

| Risque | Gravité | Commentaire |
|---|---|---|
| **Recommandations « leviers d'action »** | Élevée | La réutilisation « Santé & Territoires » (citée §4) propose des leviers (renforts mobiles, transport…). Si le produit évolue vers ce type de sortie LLM, on sort du SQL strict → risque de prescriptions plausibles mais non fondées. |
| **RPPS nominatif** | Moyenne | Agrégation communale OK ; toute réexposition nominative ou micro-géolocalisation PS sans cadre CNIL = risque juridique et erreurs de jointure. |
| **Redondance Metric** | Faible | Metric est déjà dans le calcul APL DREES ; le présenter comme valeur ajoutée distincte peut induire une double comptabilisation si mal architecturé. |
| **SNDS pour indicateurs « frais »** | Élevée | L'observatoire CNAM (patients sans MT, installations récentes) repose sur le SNDS. Un concurrent open data ne peut pas reproduire ces indicateurs sans accès régulé — la fiche ne tranche pas sur ce plafond de verre. |
| **Définition « désert médical »** | Moyenne | Pas de définition unique (APL seul vs Guide Santé 3 critères vs IRDES 7 classes). Un LLM qui « résume » sans ancrage méthodologique fixe peut mélanger les définitions. |

**Verdict fiabilité chiffrée** : architecture saine **si** le périmètre reste indicateurs SQL agrégés. Dès qu'on ajoute conseil, matching ou synthèse territoriale, le risque hallucination monte vite.

---

## 4. Angles morts (concurrents, risques, coûts, réglementation)

### Concurrents / produits absents de la fiche

| Acteur | Périmètre | Pourquoi c'est bloquant | Source (2026-06-20) |
|---|---|---|---|
| **Observatoire SKEMA-UniCA** | National → quartier ; 22 catégories ; 15 ans d'historique ; libre accès | Concurrent **homonyme et plus riche** que le seed ; lancé le 11/06/2026, même fenêtre que la MAJ de la fiche | https://www.skema.edu/fr/news/deserts-medicaux-skema-business-school-et-universite-cote-dazur-lancent-le-premier |
| **Observatoire CNAM / Data ameli** | 8 indicateurs clés, national→départemental, open data SNDS | Porte le **nom exact** du produit envisagé ; mis à jour régulièrement (ex. données 2025 ajoutées 11/06/2026) | https://data.ameli.fr/pages/acces-aux-soins/ |
| **Observatoire des Territoires (ANCT)** | APL par profession, cartes & exports | Référence pour collectivités et élus ; canal B2G déjà occupé | https://www.observatoire-des-territoires.gouv.fr/accessibilite-potentielle-localisee-apl-aux-medecins-generalistes |
| **IRDES — typologie 7 classes** | Approche pluriprofessionnelle (MG, IDE, kiné, pharma, urgences…) | Concurrent académique plus fin que « APL seul » ; publié juillet 2024 | https://www.irdes.fr/presse/communiques/260-mise-a-disposition-de-la-typologie-communale-de-l-accessibilite-aux-soins-de-premier-recours-en-france.html |
| **Franceinfo — carte interactive** | 5 professions, commune par commune, moteur de recherche | Couvre la cible « citoyen » sans friction ; données DREES 2023 | https://www.franceinfo.fr/sante/carte-generalistes-dentistes-sages-femmes-votre-commune-est-elle-mieux-lotie-que-les-autres-en-matiere-d-acces-aux-soins_7011872.html |
| **Guide Santé** | Cartographie commerciale/média (APL + pharma + urgences) | Concurrent privé sur le narratif « désert médical » | https://www.le-guide-sante.org/actualites/sante-publique/deserts-medicaux-etat-des-lieux-solutions |
| **PAPS (13 régions + OM)** | Guichet unique installation, renvoie vers CartoSanté/Rézone | Canal institutionnel d'**action** déjà en place pour soignants | https://sante.gouv.fr/professionnels/se-former-s-installer-exercer/article/les-portails-d-accompagnement-des-professionnels-de-sante-paps |
| **Rézone CPTS** | Diagnostic territorial pour porteurs de projet CPTS | Couvre une partie du pivot « action » évoqué §4 | https://www.normandie.paps.sante.fr/rezone-cpts-10 |
| **Zonages ARS 2026 (ZIP/ZAC)** | Arrêtés au 01/01/2026, aides conditionnées | Le diagnostic est désormais **normatif** (éligibilité aides), pas seulement descriptif | https://www.nouvelle-aquitaine.ars.sante.fr/index.php/le-zonage-des-medecins-en-nouvelle-aquitaine |

### Risques / coûts non mentionnés

- **Coût d'acquisition utilisateur** : face au gratuit public + couverture média, le CAC vers collectivités/ARS est prohibitif sans niche réglementaire ou données exclusives (SNDS).
- **Marque / homonymie** : « Observatoire de l'accès aux soins » est déjà le nom du produit CNAM — risque de confusion, de réputation et d'opposition institutionnelle.
- **Obsolescence rapide** : pacte déserts médicaux 2025, zonages 2026, loi Garot en navette (Sénat 11/06/2026) — le cadre politique bouge plus vite qu'un MVP open data.
- **Effet réputationnel élargi** : étiqueter une commune « désert » peut affecter attractivité résidentielle/économique ; la fiche le mentionne mais sans stratégie de com (légitimité scientifique, gouvernance des indicateurs).
- **Télémedecine (Doctolib, Qare…)** : les zones sous-dotées sont déjà ciblées par l'offre numérique ; un observatoire purement géographique ignore une partie de l'offre réelle de soins.

---

## 5. Recalcul du score

| # | Critère | Poids | Note fiche | Pondéré fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 12 | 4 | 12 |
| C2 | Cible solvable (qui paie) | ×3 | 2 | 6 | **1** | **3** |
| C3 | Données | ×3 | 4 | 12 | **3** | **9** |
| C4 | Espace concurrentiel | ×2 | 1 | 2 | 1 | 2 |
| C5 | Différenciation | ×2 | 2 | 4 | **1** | **2** |
| C6 | Faisabilité technique | ×2 | 4 | 8 | 4 | 8 |
| C7 | Facilité MVP | ×2 | 3 | 6 | **2** | **4** |
| C8 | Maîtrise des risques | ×2 | 3 | 6 | **2** | **4** |
| C9 | Monétisation / impact | ×2 | 2 | 4 | **1** | **2** |
| | **Total** | | | **60/105** | | **46/105** |

```
score_brut_revue  = 46
score_sur_100     = round(46 / 105 × 100) = 44
score_fiche       = 57
écart             = −13 points
```

| | Fiche | Revue |
|---|---|---|
| Score /105 | 60 | 46 |
| Score /100 | **57** | **44** |
| Seuil méthode | 🔁 À retravailler (55–69) | ❌ Écartée (< 55) |

### Changement de verdict

**Oui.** Le texte du §11 dit déjà que le seed « mesurer/cartographier » est « de fait écarté », mais le score 57 le maintient en 🔁. Avec l'inventaire concurrentiel complété (SKEMA-UniCA, observatoire CNAM) et les notes C2/C5/C9 abaissées, le recalcul tombe à **44/100** → **❌ Écartée** au sens strict de `docs/methode-analyse.md`.

Le pivot « action / API / spécialistes » reste une **idée nouvelle**, pas un ajustement du score actuel : il mériterait une **nouvelle fiche** après entretiens payeur, pas un maintien artificiel à 57.

---

## 6. Verdict de revue

**Verdict** : **à corriger** — l'analyse est honnête dans le fond et bien structurée sur les données, mais **incomplète sur l'existant récent** et **légèrement complaisante au scoring** par rapport à son propre verdict rédactionnel.

### 3 actions prioritaires

1. **Compléter §4 avant toute décision** : intégrer Observatoire SKEMA-UniCA (11/06/2026), Observatoire CNAM/Data ameli (09/2025), Observatoire des Territoires, IRDES, Franceinfo, PAPS/Rézone CPTS — puis **renommer** le concept (homonymie CNAM).
2. **Trancher le périmètre** : soit ❌ Écartée pour le seed « observatoire/cartographie », soit **nouvelle fiche** explicitement pivotée (ex. API d'agrégation pour éditeurs, spécialistes hors APL, ou outil d'aide à décision d'installation **au-delà** de Rézone) avec hypothèse payeur testée.
3. **Conduire les 5–8 entretiens ARS/collectivités/URPS** (déjà recommandés §11) **avant tout code** ; critère d'échec : si aucun interviewé ne confirme un budget pour autre chose que CartoSanté/Rézone/PAPS, clôturer l'idée sans délai.

---

REVUE 0012 | à corriger | score recalculé 44/100 (vs 57) | changement de décision: oui
