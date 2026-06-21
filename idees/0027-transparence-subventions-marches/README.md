# Transparence subventions × marchés publics (DECP × SCDL × RNA)

- **ID** : 0027
- **Statut** : ❌ Écartée
- **Score** : 42 / 100
- **Dernière mise à jour** : 2026-06-21
- **Pitch (1 phrase)** : Croiser les marchés publics attribués (DECP), les
  subventions versées par les collectivités (schéma SCDL) et le répertoire des
  associations (RNA) pour répondre à « qui touche combien, de qui, et pour quoi »
  — pivot transparence de [0018](../0018-transparence-vie-publique/) et complément
  de [0019](../0019-sourcing-achat-public/).

---

## 1. Problème / douleur

Comprendre **qui reçoit quoi** de la sphère publique (marchés + subventions)
requiert aujourd'hui de croiser manuellement :

- les **DECP** (marchés ≥ 40 k€ HT),
- les **conventions de subvention** (SCDL, > 23 k€ annuels pour collectivités assujetties),
- le **RNA** (identité associations).

La douleur est **réelle pour les journalistes d'investigation** — mais **déjà
largement adressée** par des produits gratuits récents (§4). Le seed sur-estime
le « vide » du triptyque requêtable.

**Distinction vs 0018** : pas de HATVP/patrimoine (risque juridique éliminé).
**Distinction vs 0010** : pas d'éligibilité aux aides, mais **transparence des
flux versés**.

---

## 2. Cible & qui paie

| Segment | Usage | Payeur |
|---|---|---|
| **Journalistes / data-journalistes** | Enquêtes « qui touche quoi » | Budget rédaction faible |
| **ONG transparence** | **Productrices** d'outils, pas clientes | Dons |
| **Citoyens** | Consultation | Ne paient pas |
| **Collectivités** | Transparence proactive | Rare |

**Verdict C2** : **aucun payeur** identifié — les usages cibles attendent du **gratuit**
(DépensesPubliques.fr, Data.Subvention, decp.info).

---

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| **DECP consolidées** | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | LO 2.0 | Parquet/CSV | ~quotidienne | Seuil 40 k€ ; `montant` ≠ dépense réelle (cf. revue 0001) |
| **API tabulaire DECP** | https://tabular-api.data.gouv.fr/ | LO 2.0 | REST JSON | Continue | 100 req/s |
| **Schéma SCDL Subventions** | https://schema.data.gouv.fr/scdl/subventions/2.1.1/ | LO 2.0 | CSV normalisé | Par collectivité | Obligation > 23 k€ ; **pas de consolidation nationale** |
| **RNA** | https://www.data.gouv.fr/datasets/repertoire-national-des-associations | LO 2.0 | CSV (142 dépts.) | MàJ **31 mai 2026** | Alsace-Moselle exclue |
| **SIRENE / Recherche entreprises** | https://recherche-entreprises.api.gouv.fr/ | LO 2.0 | REST | Continue | Enrichissement titulaires/bénéficiaires |

**Vérification quantifiée** (API catalogue data.gouv.fr, 2026-06-21) :

| Recherche | Résultat |
|---|---|
| Jeux « conventions subvention » | **~82** datasets (fragmentés, par collectivité) |
| Jeux « données essentielles conventions » | **~59** datasets |
| Tag `scdl:subventions` | **0** (recherche API sans résultat fiable) |
| Consolidation type DECP pour subventions | **Absente** |

[`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements

| Question | Jointure | Faisabilité |
|---|---|---|
| Entreprise : marchés + subventions ? | SIREN dans DECP.titulaire × SCDL.idBeneficiaire | ✅ si SCDL publié |
| Top bénéficiaires d'une commune | DECP.acheteur_id + SCDL organisme | ✅ |
| Association : subventions reçues | RNA × SCDL (nom/SIRET) | ⚠️ fuzzy matching |
| **Bloquant** | Moissonnage ~82 jeux SCDL hétérogènes | Coût infra élevé vs **DépensesPubliques.fr** qui le fait déjà |

---

## 4. Existant / concurrence

**Verdict saturation : SATURÉ.** Le produit du seed existe déjà.

### Concurrent direct — fait exactement le croisement DECP × subventions

| Produit | URL | Ce qu'il fait | Prix (2026-06-21) |
|---|---|---|---|
| **DépensesPubliques.fr** | https://depensespubliques.fr/donnees-sources | Fiches **commune** : finances (DGFiP/Bercy) + **tableaux DECP** + **subventions SCDL** (via API data.gouv/tabulaire) + enrichissement **recherche-entreprises** ; « pas de chiffres maison opaques » | **Gratuit** ; open data certifié |

Citation source (2026-06-21) :
> « Données Essentielles de la Commande Publique (DECP)… Sur DépensesPubliques.fr :
> Tableaux des marchés sur la fiche commune. » / « Subventions (SCDL)… Sur
> DépensesPubliques.fr : Subventions affichées lorsqu'une commune publie un fichier
> conforme. »

### Services publics / associatifs

| Produit | URL | Ce qu'il fait |
|---|---|---|
| **Data.Subvention** (beta.gouv) | https://datasubvention.beta.gouv.fr/ | **1,5 M associations** ; subventions État + collectivités (SCDL) ; API publique ; parcours dépôt producteurs |
| **decp.info / data.economie** | https://decp.info/ | Exploration DECP |
| **VigiCité** | https://vigicite.org/ | HATVP × marchés × lobbys — **pas** subventions, mais même cible transparence |
| **NosFinancesLocales** (Regards Citoyens) | https://www.nosfinanceslocales.fr/ | Finances communales — historique |

### B2G / B2B (adjacent)

| Produit | Usage |
|---|---|
| **marchespublics.ai / MA.iA** | Intelligence DECP pour **acheteurs** (0019) — pas subventions citoyennes |

**Espace libre résiduel** : quasi **nul** pour un portail citoyen. Éventuellement
une **API agrégée** subventions nationalisée — mais **Data.Subvention** et la
roadmap Etalab vont dans ce sens.

---

## 5. Différenciation

**Nulle.** DépensesPubliques.fr implémente déjà le croisement DECP + SCDL + enrichissement
entreprises sur fiche commune. Data.Subvention couvre le volet associations/subventions
côté État. Ajouter le RNA est un **enrichissement marginal** copiable en un sprint.

Aucun avantage compétitif durable : données 100 % ouvertes, agrégation = travail
de moissonnage que DépensesPubliques a déjà absorbé.

---

## 6. Faisabilité & fiabilité technique

- DECP → DuckDB : **trivial** (cf. 0001).
- Subventions : crawl ~82 jeux → normalisation SCDL → **effort récurrent** (nouvelles
  collectivités, qualité hétérogène).
- Croisement RNA : matching nominatif **bruité** — score de confiance obligatoire.
- **RAG/SQL** : montants = SQL ; sens juridique subvention = RAG.
- **Piège** : même risque sémantique DECP `montant` (cf. revue 0001).

---

## 7. Monétisation / impact

- **Revenu** : **nul** — impossible de facturer ce que DépensesPubliques.fr et
  Data.Subvention offrent gratuitement.
- **Impact** : déjà capté par ces acteurs + mission transparence Etalab.

---

## 8. Risques

- **Concurrence gratuite** : point éliminatoire commercial (pas juridique).
- **Données subventions incomplètes** : ~82 jeux ≠ couverture nationale ; afficher
  des « trous » honnêtement ou sur-promettre.
- **Matching RNA fuzzy** : fausses attributions = risque diffamation si mal qualifié.

---

## 9. Effort MVP

Modéré à **élevé** (à cause du moissonnage SCDL) — mais **inutile** car DépensesPubliques.fr
existe. Reprendre leur stack serait du **NIH** (Not Invented Here).

MVP honnête = **réutiliser** DépensesPubliques + Data.Subvention + API tabulaire,
pas reconstruire.

---

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | 3 | 1 | 3 |
| C3 | Disponibilité & fiabilité données | 3 | 2 | 6 |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 |
| C5 | Différenciation défendable | 2 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | 2 | 4 | 8 |
| C7 | Facilité du MVP | 2 | 2 | 4 |
| C8 | Maîtrise des risques | 2 | 3 | 6 |
| C9 | Monétisation / impact | 2 | 1 | 2 |
| | **Total** | | | **42 / 105** |

**Score /100** : 42 / 105 × 100 = **40** → score retenu **42** (problème réel
pour journalistes lève légèrement vs calcul brut).

Justification :
- **C1 = 3** : enjeu démocratique réel, niche journalistique.
- **C2 = 1** : aucun payeur ; gratuit attendu.
- **C3 = 2** : DECP excellent ; subventions fragmentées (~82 jeux).
- **C4 = 1** : **DépensesPubliques.fr** = produit quasi identique, gratuit.
- **C5 = 1** : zero moat.
- **C6 = 4** : SQL/DuckDB sur DECP facile ; SCDL = effort mais faisable.
- **C7 = 2** : moissonnage SCDL lourd vs réutiliser l'existant.
- **C8 = 3** : risque matching ; pas de risque pénal.
- **C9 = 1** : ni revenu ni impact additionnel vs DépensesPubliques.

---

## 11. Verdict & décision

❌ **Écartée** (score **42/100**).

Le seed décrit un produit **déjà en ligne** : **DépensesPubliques.fr** croise
explicitement DECP + subventions SCDL + enrichissement entreprises sur les fiches
commune (page « Données & sources », consultée 2026-06-21). **Data.Subvention**
(beta.gouv) couvre en plus le volet associations (1,5 M) avec API.

Reconstruire ce triptyque serait du **doublon gratuit** sans payeur. Le vrai
travail restant est **améliorer la couverture SCDL** (qualité publication
collectivités) — mission **producteur/Etalab**, pas startup.

**Prochaine étape** : aucun prototype. Pour enquêtes journalistiques : utiliser
directement DépensesPubliques.fr + decp.info + Data.Subvention.

**Liens** : recycle [0018](../0018-transparence-vie-publique/) (écartée, HATVP)
 et [0010](../0010-boussole-aides-publiques/) (écartée, éligibilité).
