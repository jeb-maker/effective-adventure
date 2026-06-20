# Due diligence & scoring de tiers/fournisseurs (B2B)

- **ID** : 0022
- **Statut** : ❌ Écartée
- **Score** : 53 / 100
- **Dernière mise à jour** : 2026-06-20
- **Pitch (1 phrase)** : Agréger les données ouvertes françaises (SIRENE, BODACC, RNE, DECP, RGE…) pour scorer la fiabilité d'un fournisseur — le seed décrit un produit **déjà saturé** par l'État, Pappers et une dizaine d'acteurs commerciaux.

---

## 1. Problème / douleur

Avant de contractualiser avec un fournisseur ou partenaire, les directions achats, les PME et les équipes compliance doivent vérifier l'**existence légale**, la **santé financière**, les **procédures collectives**, les **dirigeants** et, selon le secteur, des **certifications** (RGE, Qualibat…). Cette due diligence est récurrente (onboarding, renouvellement annuel, alertes) et chronophage si faite manuellement sur bodacc.fr, l'INPI et des fichiers Excel.

La douleur est **réelle** : une fraude ou une défaillance fournisseur peut coûter des dizaines de milliers d'euros (RiskSonnar cite 47 000 € par incident en moyenne, source Euler Hermes 2024 — [risksonnar.com](https://www.risksonnar.com/), consulté 2026-06-20 ; à traiter comme argument marketing du concurrent, non comme étude indépendante vérifiée). Les obligations KYC/KYB léger et la conformité achats (Sapin 2, LCB-FT pour certains secteurs) renforcent le besoin.

**Limite** : la douleur est largement **déjà adressée** par des outils gratuits (Annuaire des Entreprises) ou abordables (Pappers, Societe.com, RiskSonnar à 9,90 € le scan). Le problème n'est pas l'absence de solution, mais le choix entre des dizaines d'offres existantes.

## 2. Cible & qui paie

| Segment | Utilisateur | Payeur ? | Budget constaté (concurrent) |
|---|---|---|---|
| **PME / TPE** (10–200 salariés) | Dirigeant, comptable, acheteur occasionnel | Faible | Pappers **gratuit** en web ; API dès **30 €/mois** (500 crédits) — [pappers.fr/api](https://www.pappers.fr/api), consulté 2026-06-20 |
| **PME avec due diligence récurrente** | Responsable achats, compliance | Oui, mais déjà servi | RiskSonnar **9,90 €/scan** ou abonnements **19–649 €/mois** — [risksonnar.com](https://www.risksonnar.com/), consulté 2026-06-20 |
| **ETI / grands comptes** | Direction achats, risk management, conformité | Oui, budgets élevés | Infolegale Essential Risk Management **dès 1 980 €/an** (165 €/mois) — [infolegale.fr/nos-tarifs](https://www.infolegale.fr/nos-tarifs), consulté 2026-06-20 ; Ellisphere/Altares/Creditsafe sur devis |
| **Agents publics** | Acheteurs publics, services instructeurs | Oui (budget public) | **Annuaire des Entreprises** gratuit + **API Entreprise** (habilitation DINUM) — pas un marché SaaS B2B libre |
| **Éditeurs SRM / achats** | Weproc, Oxalys… | Indirect (bundling) | KYC fournisseur **inclus** dans suites P2P/SRM — [weproc.com/fr/logiciel-srm](https://www.weproc.com/fr/logiciel-srm/), consulté 2026-06-20 |

**Utilisateur ≠ payeur** pour les PME : l'utilisateur fait la vérification, mais le **gratuit de l'Annuaire des Entreprises et de Pappers** capte la majorité des usages ponctuels. Les budgets achats/compliance des ETI sont **déjà alloués** à Infolegale, Ellisphere, Altares ou Creditsafe — un nouvel agrégateur open data n'a pas de ligne budgétaire évidente.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| **Base SIRENE** (identité, NAF, effectifs, diffusion) | https://www.data.gouv.fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret | Licence Ouverte 2.0 | CSV stock ; API JSON (compte INSEE requis) | Stock mensuel ; API **quotidienne** (mise à jour nocturne) — [sirene.fr doc v3.11](https://www.sirene.fr/static-resources/htm/sommaire_311.html), consulté 2026-06-20 | **Diffusion partielle** (statut « P ») : identité/adresse masquées pour oppositions — [fiche SIRENE data.gouv](https://www.data.gouv.fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret), consulté 2026-06-20 ; pas de données financières détaillées |
| **API Sirene open data** | https://dev.data.gouv.fr/dataservices/api-sirene-open-data | Licence Ouverte | REST JSON | Quotidienne (dernière MàJ fiche : 2026-05-01) | Inscription obligatoire ; quotas ; historique depuis 1973 |
| **BODACC** (procédures collectives, radiations, modifications) | https://www.data.gouv.fr/datasets/bodacc | Licence Ouverte 2.0 | CSV ; API Opendatasoft JSON/CSV/Excel | Jeu de données MàJ **aujourd'hui** (fiche data.gouv) | Lien SIREN parfois imparfait ; rectificatifs ; **pas d'expérience de paiement** ; RGPD sur données personnelles — [API BODACC](https://www.data.gouv.fr/dataservices/api-bulletin-officiel-des-annonces-civiles-et-commerciales-bodacc), consulté 2026-06-20 |
| **API BODACC DILA** | https://www.dila.gouv.fr/services/api/api-bodacc-bulletin-officiel-des-annonces-civiles-et-commerciales-124/ | Licence Ouverte 2.0 | API REST (endpoint Opendatasoft v2.1) | Flux continu | Même limites ; 2 000–5 000 annonces/jour (RiskSonnar blog, à prendre comme ordre de grandeur) |
| **RNE / INPI** (dirigeants, actes, comptes) | https://www.data.gouv.fr/datasets/registre-national-des-entreprises ; API https://registre-national-entreprises.inpi.fr/api/companies | Licence homologuée État (open data INPI) — [CGU INPI](https://data.inpi.fr/content/editorial/cgu), consulté 2026-06-20 | JSON, PDF | Flux formalités + stock ; comptes depuis 2017 | **Compte INPI obligatoire** ; opposition prospection (art. R. 123-320 C. com.) ; données confidentielles réservées aux habilités — [doc API formalités v4.0](https://www.inpi.fr/sites/default/files/2025-06/documentation%20technique%20API%20formalit%C3%A9s_v4.0.pdf), consulté 2026-06-20 |
| **Documents et comptes** (HVD UE) | https://www.data.gouv.fr/datasets/documents-et-comptes-des-entreprises | Licence Ouverte 2.0 | API data.inpi.fr | Dernière MàJ fiche : 2026-01-26 ; fréquence non respectée (métadonnées) | Couverture inégale (micro-entreprises sans comptes détaillés) |
| **DECP consolidées** (références marchés publics attribués) | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | Licence Ouverte 2.0 | Parquet / CSV ; API tabulaire data.gouv | ~quotidienne | `montant` = **notification / max accord-cadre**, pas dépense réelle ; MAPA sous seuil souvent absents ; délais de publication variables — cf. analyse 0001 |
| **Certifications RGE** | https://www.data.gouv.fr/dataservices/api-professionnels-rge | Licence Etalab (open data) | API REST | Mises à jour régulières (portail ADEME) | **Périmètre sectoriel** (rénovation énergétique) ; rate limit ~10 appels/s — [api.gouv.fr](https://github.com/betagouv/api.gouv.fr/blob/master/_data/api/api_professionnels_rge.md), consulté 2026-06-20 |
| **API Recherche d'entreprises** (agrégat Annuaire) | https://recherche-entreprises.api.gouv.fr/docs/ | Open data (État) | REST JSON | Alignée sur sources agrégées (50+ jeux) | **7 req/s/IP** ; pas la base SIRENE complète ; pas de scoring — [doc API](https://recherche-entreprises.api.gouv.fr/docs/), consulté 2026-06-20 |
| **Annuaire des Entreprises** (produit État, 50+ sources) | https://annuaire-entreprises.data.gouv.fr/donnees/sources | Open data | Web + API recherche | Sources MàJ **20/06/2026** (page sources) | **Concurrent direct gratuit** : agrège déjà SIRENE, BODACC, RNE, RGE, ratios financiers INPI, liens capitalistiques, certifications Qualibat/Qualifelec… |

**Synthèse données** : les briques open data existent et sont exploitables en SQL. En revanche, les **données qui font la valeur d'un scoring crédible** (expérience de paiement, comportement fournisseurs, réseau DunTrade d'Altares, scores propriétaires Creditsafe) ne sont **pas** en open data. Un scoring fondé uniquement sur SIRENE + BODACC + DECP sera structurellement **inférieur** aux scores Ellisphere/Altares/Creditsafe.

## 4. Existant / concurrence

> Règle appliquée : chaque acteur = lien + date 2026-06-20. Verdict de saturation en fin de section.

### Services publics / open data (gratuits — concurrents de fait)

| Acteur | URL | Ce qu'il fait | Limites |
|---|---|---|---|
| **Annuaire des Entreprises** (DINUM / beta.gouv) | https://annuaire-entreprises.data.gouv.fr/ ; https://beta.gouv.fr/startups/annuaire-entreprises.html | Moteur de recherche + fiche unifiée par SIREN : SIRENE, BODACC, RNE, RGE, ratios financiers, dirigeants, certifications sectorielles (50+ sources) | Pas de scoring propriétaire ; API recherche limitée (7 req/s) ; pas de portefeuille/alertes métier achats |
| **API Recherche d'entreprises** | https://recherche-entreprises.api.gouv.fr/docs/ | Même agrégat, intégrable (Mon Entreprise, Code du travail numérique…) | Limites volumétrie ; pas de scoring |
| **Origami** (réutilisation data.gouv) | https://www.data.gouv.fr/reuses/origami | ~29 M fiches SIRENE + BODACC + RNE ; API JSON ; indicateurs créations/cessations | Gratuit ; pas de scoring fournisseur ni KYC |

### Agrégateurs freemium / API (cœur du seed)

| Acteur | URL | Ce qu'il fait | Prix (si public) |
|---|---|---|---|
| **Pappers** | https://www.pappers.fr/ ; API https://www.pappers.fr/api | SIRENE + INPI/RNE + BODACC + bilans ; surveillance 10 entités gratuites ; **scoring** (30 crédits/scoring seul, 50 crédits/rapport PDF) ; conformité PEP/sanctions | Web gratuit ; API **30 €/mois** (500 crédits) — page API consultée 2026-06-20 (403 sur fetch direct ; tarifs confirmés via [hayot-expertise.fr](https://hayot-expertise.fr/blog/pappers-outil-recherche-entreprise-avis), 2026-06-20) |
| **Societe.com** | https://www.societe.com/solutions/surveillance | 13,5 M entreprises ; score solvabilité **CreditSafe** ; surveillance 500–2 000 entités ; API 500–2 500 crédits/mois | **16,90–49,90 € HT/mois** — [societe.com/solutions/surveillance](https://www.societe.com/solutions/surveillance), 2026-06-20 |
| **Infogreffe** | https://www.infogreffe.fr/ | Kbis certifié, actes RCS, source primaire juridique | Payant à l'acte (ex. Kbis ~3,20 € cité par comparatifs tiers) ; pas de scoring intégré |

### Scoring / risk management B2B (segment premium)

| Acteur | URL | Ce qu'il fait | Prix |
|---|---|---|---|
| **Ellisphere — ELLIPRO Supplier Risk Management** | https://ellisphere.com/solution/ellipro-supplier-risk-management | Score défaillance 3 ans, risque fraude, KYS, surveillance continue, 230+ pays | Sur devis — 2026-06-20 |
| **Altares-D&B — Intuiz+** | https://www.altares.com/fr/solutions/credit-risk-intuiz/ | +22 M entreprises FR ; score défaillance (Gini 83,2 % revendiqué) ; attitude de paiement DunTrade ; évaluation risque fournisseur | Sur devis — 2026-06-20 |
| **Creditsafe France** | https://www.creditsafe.com/fr/fr/solutions-gestion-du-risque/rapports-de-solvabilite/rapports-de-solvabilite-france.html | Score 1–100, limite de crédit ; 80 % défaillances à 12 mois revendiqué ; données INSEE/INPI/BODACC + **paiement** | Packs TPE sur devis — [creditsafe.com packs](https://www.creditsafe.com/fr/fr/en-savoir-plus/aide-support/nos-packs-creditsafe-france.html), 2026-06-20 |
| **Infolegale** | https://www.infolegale.fr/risk-management | TPRM 360° : solvabilité, fraude (Vidocq IA), cyber, compliance Sapin 2/KYC | **dès 1 980 €/an** — [infolegale.fr/nos-tarifs](https://www.infolegale.fr/nos-tarifs), 2026-06-20 |

### Produit quasi homologue (open data + scoring — **concurrent direct du seed**)

| Acteur | URL | Ce qu'il fait | Prix |
|---|---|---|---|
| **RiskSonnar** | https://www.risksonnar.com/ | Agrège Pappers, BODACC, INPI, sanctions OFAC/ONU, PEP ; scoring A–D ; rapport PDF ; surveillance | **9,90 €/scan** ; abonnements **19–649 €/mois** — 2026-06-20 |

### SRM / qualification fournisseur (bundling KYC)

| Acteur | URL | Ce qu'il fait |
|---|---|---|
| **Weproc** | https://www.weproc.com/fr/logiciel-srm/ | Onboarding fournisseur, collecte Kbis/assurances, contrôles KYC, portail fournisseur — SaaS français |
| **Oxalys** | https://www.oxalys.fr/suppliers-quality-management/logiciel-srm-qualification-des-articles-et-des-fournisseurs/ | Qualification articles/fournisseurs, audits, scoring performance, conformité |

### Réutilisations data.gouv (intelligence économique)

| Acteur | URL | Ce qu'il fait |
|---|---|---|
| **Atometrics** | https://www.data.gouv.fr/reuses/atometrics-module-ventes-de-fonds-de-commerce | BODACC : procédures collectives, santé financière, alertes |
| **decp.info** | https://www.data.gouv.fr/reuses/decp-info-interface-dexploration-et-de-telechargement-des-donnees-de-la-commande-publique-au-format-tabulaire | Exploration DECP par titulaire/acheteur (outil, pas scoring) |

### Verdict de saturation : **SATURÉ**

Le seed (SIRENE + BODACC + DECP + RGE + dirigeants → scoring fournisseur) est **déjà couvert** :
- **gratuitement** par l'Annuaire des Entreprises (qui agrège plus de sources que le seed) ;
- **en freemium** par Pappers (avec scoring et API à 30 €/mois) ;
- **en produit commercial ciblé** par RiskSonnar (même logique open data + scoring, dès 9,90 €) ;
- **en premium** par Infolegale, Ellisphere, Altares, Creditsafe (avec données de paiement propriétaires).

**Espace libre résiduel (étroit)** : un angle **ultra-spécialisé** non couvert par les généralistes — ex. scoring « conformité achats publics » croisant DECP + RGE + procédures pour **fournisseurs BTP/énergie** uniquement, avec traçabilité audit. Même là, Pappers + DECP manuel + Annuaire couvrent 80 % du besoin sans abonnement.

## 5. Différenciation

**Pourquoi nous ?** — Aucune différenciation défendable identifiée sur le périmètre du seed.

| Angle revendiqué (seed) | Déjà fait par |
|---|---|
| Agrégation SIRENE + BODACC + dirigeants | Annuaire des Entreprises, Pappers, Origami |
| Procédures collectives / alertes | Pappers, Societe.com, RiskSonnar, Infolegale |
| Certifications RGE | Annuaire des Entreprises, API RGE ADEME |
| Références marchés publics (DECP) | decp.info, Maître AO, Nextend.ai (idée 0001) — pas un différenciateur due diligence |
| Scoring / note de risque | Pappers (scoring), Societe.com (CreditSafe), RiskSonnar (A–D), Infolegale, Altares, Creditsafe |
| KYC/KYB léger PME | RiskSonnar (9,90 €), Pappers (conformité PEP API) |
| API B2B | Pappers API, API Recherche d'entreprises (gratuite mais limitée) |

**Imitable en un week-end ?** L'agrégation minimale oui (datasets publics + DuckDB). Un **scoring crédible** non : sans données de paiement ni historique propriétaire, le score sera une **règle métier banale** (procédure collective = rouge) que RiskSonnar et Pappers proposent déjà. L'**Annuaire des Entreprises** est maintenu par l'État avec 50+ sources — impossible de rivaliser en exhaustivité sur l'open data pur.

**Seul créneau potentiel** (non exploré dans le seed) : due diligence **sectorielle verticale** avec règles métier opposables (ex. chaîne alimentaire + contrôles sanitaires MAATE déjà dans l'Annuaire) — mais ce n'est pas ce que décrit le seed.

## 6. Faisabilité & fiabilité technique

### Architecture proposée (si l'idée n'était pas écartée)

```
Sources (SIRENE, BODACC, RNE/INPI, DECP, RGE)
    → ETL batch (quotidien) → entrepôt DuckDB/PostgreSQL
    → Scoring SQL (règles explicites + pondérations documentées)
    → API fiche fournisseur + portefeuille + alertes
    → LLM (optionnel) : résumé narratif, explication des signaux — RAG sur doc métier uniquement
```

### Respect RAG(sens) / SQL(chiffres)

| Type d'information | Mécanisme | Fiabilité |
|---|---|---|
| SIREN, état administratif, NAF, effectif | SQL sur SIRENE | ✅ Traçable |
| Nb procédures collectives, dates BODACC | SQL sur BODACC (`familleavis`) | ✅ Traçable ; attention aux homonymes SIREN |
| Nb marchés DECP, montants déclarés | SQL sur DECP (`titulaire_id`, `donneesActuelles=true`) | ✅ Chiffres exacts mais **sémantique trompeuse** (montant ≠ dépense) |
| Certifié RGE oui/non | SQL jointure SIRET sur API/dataset RGE | ✅ Traçable |
| Bilans, ratios | SQL sur comptes INPI (si présents) | ⚠️ Couverture partielle |
| **Score composite 0–100** | Règles SQL pondérées (pas LLM) | ⚠️ Valide techniquement, **faible valeur prédictive** vs Creditsafe (pas de paiement) |
| « Fournisseur fiable / à risque » (texte) | LLM + RAG sur définitions procédures | ✅ OK pour le sens, jamais pour le chiffre |

**Risque d'hallucination numérique** : faible si le LLM est cantonné au commentaire. **Risque métier** : élevé — un score open-data peut être **exact et inutile** (tout le monde noté « moyen » faute de signal) ou **trompeur** (entreprise saine sans comptes déposés = données absentes ≠ risque nul).

## 7. Monétisation / impact

| Modèle | Faisabilité | Commentaire |
|---|---|---|
| SaaS PME 20–50 €/mois | **Faible** | Pappers web gratuit + RiskSonnar 9,90 €/scan ; prix plancher très bas |
| SaaS ETI 100–200 €/mois | **Très faible** | Infolegale à 165 €/mois avec scores propriétaires + compliance ; switching cost élevé |
| API à crédits | **Faible** | Pappers API 30 €/mois ; API Recherche d'entreprises gratuite (limitée) |
| Freemium + premium scoring | **Faible** | Annuaire des Entreprises gratuit sur le même agrégat |
| Vente à un éditeur SRM (Weproc, Oxalys) | **Moyenne** | Possible en **composant** DECP/RGE, pas en produit autonome |

**Impact sociétal** (transparence, lutte fraude) : réel via un outil gratuit, mais **l'Annuaire des Entreprises remplit déjà cette mission** sans nouveau produit.

## 8. Risques

1. **Saturation / commoditisation** — Le segment est occupé par l'État (gratuit) et 10+ acteurs payants ; ARPU structurellement comprimé.
2. **Plafond de verre scoring** — Sans données de paiement (DunTrade, CreditSafe…), impossible de rivaliser sur la **prédiction de défaillance** (cœur de la valeur Infolegale/Altares).
3. **Concurrence État** — L'Annuaire des Entreprises intègre continuellement de nouvelles sources ([page sources](https://annuaire-entreprises.data.gouv.fr/donnees/sources), 2026-06-20) ; tout agrégat open data converge vers ce hub.
4. **Responsabilité du score** — Une note « vert » sur une entreprise qui fait faillite expose à un risque réputationnel/juridique ; les incumbents ont des disclaimers et des modèles validés statistiquement.
5. **RGPD / prospection** — Oppositions RNE (art. R. 123-320) ; diffusion partielle SIRENE ; usage des données pour scoring commercial à cadrer.
6. **Coût d'ingestion vs marge** — Multiplication des APIs (INPI compte, INSEE compte, BODACC, DECP ~1,8 Go) pour un revenu incertain.
7. **Concurrent direct RiskSonnar** — Même proposition (open data + scoring + PDF), déjà en marché avec tarifs publics agressifs.

## 9. Effort MVP

Périmètre minimal crédible (si l'on ignorait la saturation) :

1. **Ingestion** : SIRENE stock + flux BODACC (procédures) + DECP titulaires + RGE ; compte INPI pour dirigeants.
2. **Fiche fournisseur** (SIREN) : identité, signaux BODACC, certifications RGE, nb/contrats DECP (avec disclaimer montants).
3. **Score SQL** : règles transparentes (ex. procédure collective active = critique ; radiation = bloquant ; absence comptes = neutre).
4. **Portefeuille** : 50–500 fournisseurs surveillés + alerte email sur nouveau BODACC.
5. **Traçabilité** : chaque signal → source + date + requête SQL.

**Effort estimé** : 4–8 semaines pour un agrégat correct (ETL, dédoublonnage SIREN/SIRET, UI). **Valeur marginale vs Annuaire + Pappers** : faible. Le MVP le plus rapide serait une **couche DECP** sur un profil Annuaire — trop étroit pour un produit.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 | Due diligence fournisseur récurrente et coûteuse si manuelle ; douleur réelle mais déjà adressée. |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 | Budgets existent (Infolegale 1 980 €/an, Societe.com 17–50 €/mo) mais **captés par incumbents** ; PME utilisent le gratuit (Annuaire, Pappers). |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 | Sources open documentées et SQL-compatibles ; manque les données de paiement qui font la qualité du scoring. |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 | **Saturé** : État (Annuaire) + Pappers + Societe.com + RiskSonnar + 4 acteurs premium + SRM. |
| C5 | Différenciation défendable | 2 | 1 | 2 | Le seed est **déjà implémenté** par au moins 3 produits (Annuaire, Pappers, RiskSonnar) ; pas d'avantage durable. |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 | Agrégation SQL + règles de scoring traçables conformes RAG(sens)/SQL(chiffres) ; valeur prédictive limitée. |
| C7 | Facilité du MVP | 2 | 3 | 6 | ETL multi-sources non trivial (comptes INPI/INSEE, normalisation DECP) pour un résultat proche du gratuit. |
| C8 | Maîtrise des risques | 2 | 2 | 4 | Responsabilité du score, RGPD, concurrence État, plafond qualité sans data propriétaire. |
| C9 | Monétisation / impact | 2 | 2 | 4 | ARPU comprimé (9,90 €/scan RiskSonnar, Pappers gratuit) ; impact transparence déjà porté par l'Annuaire. |
| | **Total** | | | **56 / 105** | |

**Score /100** : 56 / 105 × 100 = **53,3 → 53 / 100**

## 11. Verdict & décision

**❌ Écartée** (score 53 < 55).

Le problème est réel et les données ouvertes sont exploitables techniquement (SQL traçable, LLM cantonné au sens). En revanche, le seed décrit un produit **sans espace marché** : l'**Annuaire des Entreprises** offre gratuitement un agrégat plus riche que celui envisagé ; **Pappers** couvre le freemium et l'API avec scoring ; **RiskSonnar** commercialise déjà la même thèse (open data + score + PDF) à 9,90 € ; les ETI paient **Infolegale, Ellisphere, Altares ou Creditsafe** pour des scores fondés sur des données de paiement que l'open data ne fournit pas.

Reproduire un « Pappers + DECP + score maison » n'apporte pas de valeur défendable face à ces acteurs. La leçon des analyses précédentes (sous-estimation systématique de C4 et C2) s'applique avec force ici : **10+ concurrents nommés**, budgets déjà alloués, gratuit État en face.

**Critère éliminatoire** : non juridique ni sanitaire, mais la **saturation concurrentielle** combinée à l'**absence de donnée différenciante** (paiement, réseau) rend le scoring open-data **non compétitif** — équivalent à une donnée « inexistante » pour l'usage métier visé (prédiction de défaillance).

**Prochaine étape** : **ne pas prototyper**. Si le dépôt d'idées veut explorer la filière « tiers », chercher un angle **non agrégatif** : ex. audit trail conformité achats publics (croisement DECP + attestations via API Entreprise pour administrations habilitées), ou vertical sectoriel avec règles métier non couvertes — pas un agrégateur généraliste.

---

0022 | Due diligence & scoring de tiers/fournisseurs (B2B) | ❌ Écartée | 53/100 | Marché saturé, pas de créneau
