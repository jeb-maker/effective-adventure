# Rapport de revue critique — Idée 0017 « Empreinte carbone des territoires / PME »

**Réviseur** : évaluateur indépendant (red team)  
**Date de revue** : 2026-06-20  
**Fiche auditée** : `idees/0017-empreinte-carbone-territoire/README.md`  
**Score déclaré** : 56/100 — statut 🔁 À retravailler  
**Méthode** : `docs/methode-analyse.md` + prompt `docs/prompts/03-revue-critique.md`  
**Vérifications web** : effectuées le 2026-06-20 (sources citées ci-dessous)

---

## Synthèse exécutive

L'analyse est **globalement honnête** sur la saturation du marché bilan GES entreprise et sur la faiblesse du seed PME. Elle sous-estime toutefois l'ampleur de l'existant **gratuit** côté PME, et surtout **ne cartographie pas l'offre publique territoriale qui réalise déjà le pivot proposé** (bouquet RARE/OREC avec émissions GES pré-calculées à la maille EPCI). Le conditionnel de sauvetage (« pré-diagnostic territorial automatique ») est donc **beaucoup plus fragile** que ne le laisse entendre le verdict « à retravailler ». Le score 56/100 est **légèrement complaisant** ; un recalcul adversarial conduit à **~48–51/100**, soit sous le seuil d'écart.

---

## 1. Affirmations non sourcées ou insuffisamment sourcées

| Affirmation (README) | Problème | Verdict |
|---|---|---|
| « > 3 000 facteurs » (Base Empreinte) | Chiffre repris via blogs (wecount.io, hellocarbo.com), pas source ADEME officielle ; d'autres sources citent 2 500+ ou 1 100+ selon périmètre | **À sourcer** (page doc Base Empreinte ou note méthodologique ADEME) |
| « Plateforme Bilans GES ADEME : dépôt officiel + **module de saisie guidée** » | Source = blog les-rencontres-ecologie-travail.fr ; la plateforme officielle est surtout un **portail de dépôt/consultation** et de guides sectoriels ([bilans-ges.ademe.fr](https://bilans-ges.ademe.fr/), [ADEME](https://agirpourlatransition.ademe.fr/entreprises/conseils/industrie/decarbonation/etat-des-lieux/bilan-ges), consulté 2026-06-20) | **À corriger / à sourcer** |
| Prix Greenly, Carbo, Sweep via logiciel-bilan-carbone.fr et greenly.earth **sans date** sur plusieurs liens §4 | Non conforme à la règle « lien + date de consultation » | **À sourcer** (date manquante sur 4 liens §4) |
| Sami « ~5 000 €/an » via vsmexperts.fr **sans date** | Idem | **À sourcer** |
| « Budgets constatés 1 500–15 000 €/an » (PME) | Agrégateur commercial (logiciel-bilan-carbone.fr), pas étude de marché | **À sourcer** (ou nuancer : fourchette marketing) |
| « Copiable en un week-end » (§5) | Jugement d'opinion, aucune démonstration | **À supprimer ou reformuler** en hypothèse non prouvée |
| « MAJ ~annuelle (V23.6 juil. 2025, *version exacte à vérifier*) » | Auto-incertitude ; V23.6 confirmée par sources tierces ([greencalculus.com](https://greencalculus.com/standards/ademe-base-carbone-base-empreinte/), consulté 2026-06-20) mais pas vérifiée sur portail ADEME dans la fiche | **À sourcer** (lien direct version officielle) |
| API SDES « Fraîcheur : Continue » | Vague ; SDES indique millésime 2024, MAJ 1er oct. 2025 ([SDES](https://www.statistiques.developpement-durable.gouv.fr/donnees-locales-de-consommation-denergie), consulté 2026-06-20) — incohérent avec « MAJ 12 jan. 2026 » côté ORE | **À corriger** (harmoniser fraîcheur ORE vs SDES) |
| « Collectivités > 50 000 hab. : obligées (PCAET/BEGES) » (§2) | **Confusion réglementaire** : PCAET = EPCI > **20 000** hab. ; BEGES collectivité = > **50 000** hab. ([ADEME PCAET](https://agirpourlatransition.ademe.fr/collectivites/conseils/amenagement/pcaet), [Sénat 2025](https://www.senat.fr/questions/base/2025/qSEQ250705482.html), consulté 2026-06-20) | **À corriger** |
| « existence à vérifier au cas par cas » (observatoires) | Prudence louable mais insuffisante : l'existence nationale du bouquet OREC est **documentée et datée** | **À sourcer** (voir §4) |

**Points correctement sourcés** (à conserver) : seuils BEGES 500/250 salariés, amendes 50 000/100 000 € ([portail-rse.beta.gouv.fr](https://portail-rse.beta.gouv.fr/fiches-reglementaires/bilan-eges-et-plan-de-transition/), [hayot-expertise.fr](https://hayot-expertise.fr/blog/beges-entreprises-50-500-salaries-2026), consulté 2026-06-20) ; PME non assujetties par effectif seul ; limites ecoinvent ([nosgestesclimat.fr mentions légales](https://nosgestesclimat.fr/mentions-legales-base-empreinte), consulté 2026-06-20).

---

## 2. Sur-optimisme du scoring

La fiche est sévère sur C4/C5 mais **encore généreuse sur C2, C4, C6 et partiellement C9**. Le tableau ci-dessous reprend les notes déclarées et les contre-propositions justifiées.

| Critère | Note fiche | Note revue | Écart | Justification adversarial |
|---|---|---|---|---|
| **C1** Intensité problème | 3 | **3** | = | OK : douleur réelle pour assujettis BEGES, tiède pour PME seed. |
| **C2** Cible solvable | 3 | **2** | −1 | Segment qui paie bien (ETI/GE) = capté et concurrentiel. Segment seed (PME) : **empreinte-carbone.org** offre un bilan complet gratuit ([empreinte-carbone.org](https://empreinte-carbone.org/), consulté 2026-06-20) ; **Diag Décarbon'Action** = 6 000 € HT subventionné pour un bilan scopes 1-2-3 accompagné ([Bpifrance](https://www.bpifrance.fr/catalogue-offres/diag-decarbonaction), consulté 2026-06-20). Willingness-to-pay SaaS très faible. |
| **C3** Données | 3 | **3** | = | Facteurs ADEME solides en SQL ; trou d'activité client et ecoinvent correctement identifiés. |
| **C4** Espace libre | 2 | **1** | −1 | Saturé côté entreprise **et** côté pivot territorial : le bouquet RARE/OREC diffuse déjà consommations **et émissions GES** à la maille EPCI, par secteur et vecteur ([data.gouv.fr](https://www.data.gouv.fr/datasets/bouquet-dindicateurs-communs-energie-climat-des-orec), [RARE](https://rare.fr/nos_actions/bouquet-dindicateurs-communs-energie-climat-a-lechelle-des-epci/), consulté 2026-06-20). Espace produit quasi nul, pas « mince ». |
| **C5** Différenciation | 2 | **1** | −1 | Le pré-remplissage territorial proposé = **réplication d'un travail national en cours** (RARE + Ecolab + ADEME/TeT). Aucun fossé. |
| **C6** Faisabilité / fiabilité | 4 | **3** | −1 | RAG(sens)/SQL(chiffres) OK en théorie, mais : (1) **SaaS commercial + ecoinvent** → licence Developer ecoinvent obligatoire, coût non chiffré ([ecoinvent.org/licenses/developer](https://ecoinvent.org/licenses/developer/), consulté 2026-06-20) ; (2) croiser conso territoriale agrégée × facteurs ≠ bilan organisationnel — risque de **chiffres traçables mais méthodologiquement faux** pour une PME. |
| **C7** Facilité MVP | 3 | **2** | −1 | POC territorial = concaténation de datasets existants déjà publiés ; MVP « crédible face aux incumbents » reste lourd (scope 3, conformité, import compta). |
| **C8** Risques | 2 | **2** | = | Saturation, ABC®, ecoinvent, crédibilité : bien vu. |
| **C9** Monétisation / impact | 3 | **2** | −1 | Modèle SaaS prouvé ailleurs, mais **capture impossible** face au gratuit + subvention publique ; impact réel si produit redondant avec bouquet RARE = faible. |

---

## 3. Risque d'hallucination / RAG(sens)–SQL(chiffres)

### Chiffres affichés dans la fiche

La fiche ne présente **pas de chiffres de marché inventés** dans le scoring ; les montants (amendes, prix concurrents) ont des sources, parfois faibles (blogs comparateurs).

### Architecture proposée

- **Conforme en principe** : facteurs en tabulaire, calcul arithmétique, LLM pour le sens — aligné avec `docs/methode-analyse.md` §3.
- **Risques sous-évalués** :
  1. **Proxy territorial** : afficher un « ordre de grandeur GES » pour une organisation à partir de consommations **communales/EPCI masquées ou agrégées** produirait des nombres SQL-tracés mais **sémantiquement trompeurs** (mélange bilan territorial vs bilan organisationnel, secret statistique, secteurs NAF agrégés).
  2. **ecoinvent en SaaS** : l'EULA interdit le partage automatisé de résultats calculés à des tiers sans licence Developer ([ecoinvent EULA](https://support.ecoinvent.org/eula), consulté 2026-06-20). La fiche mentionne la limite mais **ne la traite pas comme contrainte produit bloquante** pour un SaaS B2B.
  3. **Choix du facteur par LLM** : même en RAG(sens), le risque d'erreur de périmètre scope/facteur reste non chiffré ; un mauvais facteur SQL-validé donne un **faux chiffre traçable**.

**Verdict fiabilité** : architecture nominalement saine, mais **le scénario d'usage territorial automatisé maximise le risque « chiffre exact, conclusion fausse »** — pire qu'une hallucination LLM car plus crédible.

---

## 4. Angles morts (non mentionnés ou insuffisamment traités)

### Concurrents / substituts absents de la fiche

| Acteur | Menace | Source (consulté 2026-06-20) |
|---|---|---|
| **empreinte-carbone.org** | SaaS **100 % gratuit**, bilan complet scopes 1-2-3, facteurs ADEME, cible PME/ETI | [empreinte-carbone.org](https://empreinte-carbone.org/) |
| **Diag Décarbon'Action** (Bpifrance/ADEME) | Offre publique subventionnée (~6 000 € HT) pour PME < 500 sal., bilan complet accompagné | [mission-transition-ecologique.beta.gouv.fr](https://mission-transition-ecologique.beta.gouv.fr/aides-entreprise/diag-decarbon-action) |
| **Bouquet d'indicateurs communs énergie-climat (RARE/OREC)** | **Émissions GES pré-calculées** à la maille EPCI (fichiers `emissions-ges-secteur`, `emissions-ges-vecteur`, etc.) — invalide le pivot territorial | [data.gouv.fr](https://www.data.gouv.fr/datasets/bouquet-dindicateurs-communs-energie-climat-des-orec) |
| **IGT Citepa** | Inventaire GES territorialisé par commune/EPCI, « par défaut » pour PCAET | [citepa.org](https://www.citepa.org/donnees-air-climat/donnees-gaz-a-effet-de-serre/igt-inventaire-ges-territorialise/) |
| **ENERGIF / ROSE** (ex. Île-de-France) | Outil collectivités : conso + **émissions GES** multi-échelles pour PCAET/SCoT | [roseidf.org/energif](https://www.roseidf.org/energif/) |
| **Portail RSE** (État/beta.gouv) | Hub gratuit obligations RSE/CSRD/BEGES, tableau de bord ESG, logique « dites-le-nous une fois » | [portail-rse.beta.gouv.fr](https://portail-rse.beta.gouv.fr/) |
| **Template Excel EFRAG + Base Carbone** | Stack gratuite utilisée par consultants VSME | [vsmexperts.fr](https://vsmexperts.fr/blog/guide-rse/5-outils-automatiser-bilan-carbone-pme) |

### Risques réglementaires / marché omis

- **Simplification CSRD (« Omnibus »)** : relèvement des seuils CSRD (ex. ~1 000 salariés / 450 M€ CA selon analyses récentes) réduit la pression sur le segment 500–1 000 salariés — assouplit la douleur « induite » PME/ETI ([projetcelsius.com](https://projetcelsius.com/blog/beges-obligatoire-guide-conformite/), consulté 2026-06-20).
- **Dispense BEGES si reporting CSRD** (depuis avril 2025 pour certaines structures) : change le positionnement des outils « conformité BEGES ».
- **Coût licence ecoinvent Developer** : poste de coût structurel non estimé pour tout SaaS utilisant une partie des facteurs Base Empreinte.
- **Initiative publique en cours sur le bouquet** : RARE + **Ecolab** travaillent à harmoniser métadonnées et diffusion nationale ([RARE, déc. 2025](https://rare.fr/les-actualites-du-rare/le-bouquet-dindicateurs-communs-energie-climat-mis-a-jour/)) — fenêtre d'intervention privée en rétrécissement.
- **Distinction PCAET (20k) / BEGES collectivité (50k)** : la cible « collectivités » est mal découpée dans la fiche ; le vrai besoin territorial est surtout **PCAET/BEGES-T** pour EPCI 20k–50k, déjà outillé.

### Coûts cachés

- Intégrations comptables, multi-sites, audit trail réglementaire, support métier : budgets concurrents 20–50 % du coût licence en année 1 ([zelio-impact.com](https://zelio-impact.com/index.php/2026/02/19/logiciel-bilan-carbone-comparatif-2026-des-meilleures-solutions-pour-entreprises/), consulté 2026-06-20).
- Maintenance synchronisation Base Empreinte (portail compte requis) vs API data.gouv potentiellement en retard sur la version opérative.

---

## 5. Recalcul du score

### Scénario revue (notes adversariales retenues)

| # | Critère | Poids | Note fiche | Pondéré fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | 9 | 3 | 9 |
| C2 | Cible solvable | ×3 | 3 | 9 | **2** | **6** |
| C3 | Données | ×3 | 3 | 9 | 3 | 9 |
| C4 | Espace concurrentiel | ×2 | 2 | 4 | **1** | **2** |
| C5 | Différenciation | ×2 | 2 | 4 | **1** | **2** |
| C6 | Faisabilité / fiabilité | ×2 | 4 | 8 | **3** | **6** |
| C7 | Facilité MVP | ×2 | 3 | 6 | **2** | **4** |
| C8 | Maîtrise risques | ×2 | 2 | 4 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 3 | 6 | **2** | **4** |
| | **Total** | | | **59/105** | | **46/105** |

```
Score fiche   : 59/105 → 56/100 (arrondi)
Score revue   : 46/105 → 44/100 (arrondi)
```

**Scénario intermédiaire** (seuls C2=2 et C4=1, reste inchangé) : 54/105 → **51/100** — sous le seuil 55.

### Changement de verdict

| | Fiche | Revue |
|---|---|---|
| Score /100 | 56 | **44** (ou 51 en scénario minimal) |
| Seuil | 55–69 = À retravailler | < 55 = Écartée |
| Décision | 🔁 À retravailler | **❌ Écartée** |

**Oui, le verdict doit changer.** Même en ne corrigeant que C2 et C4, on tombe à 51/100. Le « retravail » proposé (POC pré-diagnostic territorial ORE × Base Carbone) **recoupe un livrable public existant** (bouquet RARE) ; il ne lève pas le point bloquant, il le confirme.

---

## 6. Verdict de revue et actions prioritaires

### Verdict : **à corriger** (proche de **à refaire**)

L'analyse initiale mérite crédit pour son auto-scepticisme sur la PME et la saturation, mais elle **survit à sa propre conclusion** : en proposant un pivot territorial comme condition de sauvetage sans vérifier le bouquet OREC/RARE ni empreinte-carbone.org, elle maintient un score au-dessus du seuil d'écart pour un projet dont **les deux branches** (entreprise et territoire) sont déjà couvertes par l'écosystème public et des acteurs financés.

### 3 actions prioritaires

1. **Cartographier l'existant territorial avant tout POC** — télécharger et analyser le bouquet `bouquet-dindicateurs-communs-energie-climat-des-orec` (fichiers `emissions-ges-*`) et confronter méthodologie + fraîcheur + couverture aux observatoires régionaux (ROSE/ENERGIF, IGT Citepa). Si le delta de valeur est nul, **clôturer l'idée**.

2. **Trancher le positionnement PME avec preuves de willingness-to-pay** — documenter face à empreinte-carbone.org (gratuit) et Diag Décarbon'Action (6 000 € subventionné) : quel segment paierait encore un SaaS, pour quelle fonction **non couverte** (pas « un calculateur de plus ») ?

3. **Intégrer la contrainte ecoinvent comme go/no-go produit** — quantifier le coût licence Developer et le périmètre facteurs réutilisables sans ecoinvent ; sans cela, toute note C6 ≥ 4 est non recevable pour un SaaS commercial.

---

REVUE 0017 | à corriger | score recalculé 44/100 (vs 56) | changement de décision: oui
