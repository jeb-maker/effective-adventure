# Fiche commune intelligente / copilote « ma commune en clair »

- **ID** : 0007
- **Statut** : 🔁 À retravailler
- **Score** : 59 / 100
- **Dernière mise à jour** : 2026-06-21
- **Pitch (1 phrase)** : Transformer les données d'une commune en explications
  claires (« pourquoi ma taxe augmente ? », « ma commune investit-elle plus que
  des communes comparables ? ») — couche **pédagogique** au-dessus des finances
  locales ouvertes.

---

## 1. Problème / douleur

Les comptes et indicateurs communaux sont **publics** (DGFiP, OFGL, REI, fiscalité)
mais **illisibles** pour le citoyen médian : vocabulaire comptable (M57), agrégats
techniques, absence de comparaison contextualisée.

Questions citoyennes récurrentes :
- « Pourquoi ma taxe foncière / taxe d'habitation a-t-elle augmenté ? »
- « Ma commune dépense-t-elle plus que des communes similaires ? »
- « Où va l'argent (investissement vs fonctionnement) ? »

La douleur est **réelle mais tiède** : le citoyen s'intéresse surtout aux échéances
électorales ; le reste du temps, la transparence est un **nice-to-have**. Les élus
et DGS, eux, ont besoin de **communication** — mais disposent déjà d'outils publics
(§4).

**Distinction vs 0003** : 0003 = copilote généraliste multi-domaines ; 0007 =
vertical **finances locales + explication**. Les deux souffrent du même problème :
l'OFGL couvre déjà l'analyse comparative.

---

## 2. Cible & qui paie

| Segment | Besoin | Payeur ? |
|---|---|---|
| **Citoyens** | Comprendre les finances de leur commune | **Non** — attendent du gratuit |
| **Élus / DGS / communicants** | Expliquer les choix budgétaires | Possible (budget com') — mais **OFGL gratuit** |
| **Journalistes locaux** | Enquêtes finances | Faible budget ; utilisent déjà OFGL / NosFinancesLocales |
| **Chercheurs / étudiants** | Données comparables | Quasi nul |

**Problème structurel** : utilisateur (citoyen) ≠ payeur. Le seul payeur théorique
(commune) peut obtenir 90 % du besoin sur **data.ofgl.fr** sans abonnement.

**Verdict C2** : payeur **non identifié** avec budget récurrent pour un SaaS tiers.

---

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| **OFGL / data.ofgl.fr** | https://data.ofgl.fr/ | LO 2.0 | API Explore, CSV, dataviz | Données **2024** définitives publiées (2025-2026) | **Concurrent direct gratuit** — compare déjà les communes |
| Comptes individuels DGFiP | https://www.data.gouv.fr/datasets/comptes-individuels-des-communes | LO 2.0 | CSV | Annuelle | Brut, illisible sans traitement |
| REI (fiscalité locale) | https://www.data.gouv.fr/datasets/recensement-des-equipements-des-services-aux-particuliers | LO 2.0 | CSV | Millésime REI | Taux imposition, bases |
| **API Melodi** (INSEE) | https://www.data.gouv.fr/dataservices/api-melodi | LO (Insee) | REST JSON | Continue | Compte requis ; strates démographiques |
| FiLoSoFi / démographie | https://www.insee.fr/fr/statistiques/8229323 | LO (Insee) | CSV | Revenus 2021 | Contextualisation socio-éco |
| SSMSI délinquance | https://www.data.gouv.fr/datasets/bases-statistiques-communale-departementale-et-regionale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales | LO 2.0 | CSV | MàJ mars 2026 | Faits enregistrés, sensible |
| APL (accès soins) | https://data.drees.solidarites-sante.gouv.fr/ | LO 2.0 | CSV | Annuelle DREES | Complément « qualité de vie » |

[`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements envisagés

| Croisement | Question | Faisabilité SQL |
|---|---|---|
| OFGL × strate Melodi (population) | Dépenses vs communes comparables | ✅ OFGL le fait déjà nativement |
| DGFiP × REI | Investissement vs fiscalité | ✅ |
| FiLoSoFi × SSMSI | Contexte social (prudence rédactionnelle) | ✅ agrégat communal |
| OFGL × DECP (commune acheteur) | « Combien la commune achète ? » | ✅ extension possible |

Architecture : **SQL** pour tous les chiffres ; **RAG** uniquement sur glossaire
OFGL / guides Etalab (définitions « épargne brute », « DGF », etc.).

---

## 4. Existant / concurrence

**Verdict saturation : SATURÉ** sur la couche **données + comparaison** ;
**espace étroit** sur la seule couche **récit pédagogique IA** (non couverte par l'État).

### Services publics (gratuits, très complets)

| Produit | URL | Ce qu'il fait (2026-06-21) |
|---|---|---|
| **data.ofgl.fr** (OFGL) | https://data.ofgl.fr/ | Fiches financières, cartographies, **comparaison à un groupe de référence** (taille, géo, profil), **datastories** interactives, strates personnalisées — https://data.ofgl.fr/pages/strates-population-personnalisees-analyses-financieres-comparatives-20240325/ |
| **OFGL — actualités 2024** | https://www.collectivites-locales.gouv.fr/actualites/donnees-financieres-definitives-2024-disponibles-sur-dataofglfr | Données 2024 définitives, outils d'analyse à jour |
| **Tableau de bord comptes collectivités** | https://www.data.economie.gouv.fr/ | Visualisations Économie/Finances |
| **NosFinancesLocales.fr** (Regards Citoyens) | https://www.nosfinanceslocales.fr/ | Transparence finances communales, cartes temporelles — https://contrepoints-archives.org/nosfinanceslocales-fr-pour-une-meilleure-transparence-financiere-de-nos-communes/ (historique) |

### Initiatives proches du « copilote »

| Produit | URL | Limite |
|---|---|---|
| **Idée 0003** (copilote territorial RAG) | `idees/0003-copilote-territorial-rag/` | Même risque ; MCP data.gouv officiel |
| **MCP / skill data.gouv.fr** | https://github.com/datagouv/datagouv-mcp | Connexion LLM au catalogue — pas finances pédagogiques |

**Ce qui manque réellement** : un **récit en langage clair** (« votre commune dépense
X €/habitant en investissement, soit Y % de plus que la moyenne des communes de
taille similaire en région Z ») généré **à partir** des chiffres OFGL — pas un
nouveau dashboard.

---

## 5. Différenciation

**Très faible** sur les chiffres (OFGL les affiche et compare déjà). **Modérée
mais copiable** sur la couche récit :
- Un LLM + prompts + glossaire OFGL peut produire des explications — reproductible
  en un sprint par Regards Citoyens, un média local ou l'OFGL lui-même (roadmap IA).
- Pas de donnée propriétaire, pas d'effet réseau.
- **Avantage temporaire** : être le premier « explicateur citoyen » sur OFGL — faible.

Positionnement défendable **uniquement** comme :
- **Vertical 0003** « finances locales » avec partenariat commune (distribution) ;
- ou **feature** d'un média local / association (impact, pas revenu).

---

## 6. Faisabilité & fiabilité technique

- **Excellente** si architecture RAG(sens)/SQL(chiffres) respectée :
  - Chiffres : requêtes API OFGL / Melodi → traçables.
  - Texte explicatif : LLM conditionné au glossaire OFGL + chiffres injectés (pas de
    génération de nombres).
- **Risque** : le LLM paraphrase mal les agrégats comptables → afficher **toujours**
  le chiffre SQL à côté de l'explication.
- **Dépendance** : API OFGL (disponibilité, doc) — pas de dump unique mais APIs
  stables.

---

## 7. Monétisation / impact

- **Revenu** : faible. Citoyens ne paient pas ; communes peu motivées à payer
  pour de l'explication quand OFGL est gratuit et institutionnellement légitime.
- **Impact démocratique** : réel en période électorale — mais NosFinancesLocales
  et OFGL couvrent déjà une partie du besoin de transparence.
- **Modèle viable** : subvention Média / fondation / partenariat B2G (prestation
  ponctuelle communication électorale) — pas SaaS récurrent.

---

## 8. Risques

- **Concurrence gratuite État** : l'OFGL ajoute régulièrement des datastories et
  outils comparatifs — internalisation probable d'une couche IA.
- **Réputation** : explication fiscale erronée = polémique locale (CGT, opposition).
- **Scope creep** : tendance à ajouter SSMSI, APL, etc. → devient 0003 généraliste.
- **Pas de risque juridique majeur** (données agrégées publiques).

---

## 9. Effort MVP

Faible à modéré :
1. Connecteur API OFGL (1 commune pilote) + strate comparative OFGL.
2. RAG glossaire finances locales (guides Etalab, FAQ OFGL).
3. Génération fiche « 5 questions-réponses » avec chiffres SQL inline + sources.
4. Page statique par commune (pas besoin de 35 000 communes au jour 1).

Effort **technique** faible ; effort **distribution** (trafic citoyen) élevé.

---

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 |
| C3 | Disponibilité & fiabilité données | 3 | 5 | 15 |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 |
| C5 | Différenciation défendable | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 4 | 8 |
| C8 | Maîtrise des risques | 2 | 3 | 6 |
| C9 | Monétisation / impact | 2 | 2 | 4 |
| | **Total** | | | **62 / 105** |

**Score /100** : 62 / 105 × 100 = **59**

Justification :
- **C1 = 3** : besoin réel mais tiède hors élections ; OFGL répond déjà partiellement.
- **C2 = 2** : pas de payeur récurrent identifié.
- **C3 = 5** : OFGL + Melodi + DGFiP = données excellentes, traçables.
- **C4 = 1** : OFGL + NosFinancesLocales + dashboards Économie = saturé.
- **C5 = 2** : seul le récit IA diffère — copiable.
- **C6 = 4** : RAG+SQL adapté ; risque paraphrase comptable.
- **C7 = 4** : MVP rapide sur 1 commune.
- **C8 = 3** : risque erreur explicative / concurrence État.
- **C9 = 2** : impact possible, revenu faible.

---

## 11. Verdict & décision

🔁 **À retravailler** (score **59/100**).

L'angle « explication citoyenne » est **sympathique** et techniquement faisable,
mais le **gros du besoin** (données, comparaison, cartographie) est **déjà servi
gratuitement** par l'OFGL — qui renforce même ses outils comparatifs (strates
personnalisées, datastories 2024). La valeur ajoutée résiduelle = **couche récit
LLM** — insuffisante pour un produit autonome, suffisante comme **démo vertical**
de 0003 ou campagne électorale ponctuelle.

**Prochaine étape concrète** :
1. **Ne pas** lancer un produit grand public autonome.
2. Si poursuite : prototyper **1 fiche commune** (ex. commune 20–50 k hab.) avec
   API OFGL + explication RAG — mesurer si des élus/journalistes locaux la trouvent
   plus claire que data.ofgl.fr seul.
3. Si non : fusionner dans **0003** comme vertical « finances locales » ou ❌ Écartée.

**Lien** : priorité inférieure à **0001** (66/100) et **0025** (64/100).
