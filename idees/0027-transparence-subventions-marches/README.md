# Transparence subventions × marchés publics (DECP × SCDL × RNA)

- **ID** : 0027
- **Statut** : ❌ Écartée
- **Score** : 48 / 100 (révisé après revue red team du 2026-06-23 — cf. [`revue.md`](revue.md) ; 51/100 avant revue, C4 et C5 abaissés 2→1)
- **Dernière mise à jour** : 2026-06-23
- **Pitch (1 phrase)** : Croiser les marchés publics attribués (DECP), les
  subventions versées par les collectivités (schéma SCDL) et le répertoire des
  associations (RNA) pour répondre à « qui touche combien, de qui, et pour quoi »
  — pivot transparence de [0018](../0018-transparence-vie-publique/) et complément
  de [0019](../0019-sourcing-achat-public/).

---

## 1. Problème / douleur

Les journalistes d'investigation, les ONG et les citoyens motivés doivent recouper
manuellement :
- les **marchés publics** (DECP — qui vend à l'État/collectivité),
- les **subventions** versées (conventions > 23 k€),
- les **associations** bénéficiaires (RNA).

Aucun outil ne propose ce **triptyque requêtable** en open data, alors que chaque
brique existe séparément. La douleur est réelle mais **niche** (médias, ONG) —
budget faible, impact démocratique élevé.

**Distinction vs 0018** : pas de HATVP/patrimoine (risque juridique) ; focus
**flux financiers** entreprises/associations ↔ collectivités.

## 2. Cible & qui paie

| Segment | Usage | Payeur |
|---|---|---|
| **Journalistes / data-journalistes** | Enquêtes locales | Rédaction (budget outils faible) |
| **ONG transparence** | Produisent déjà des outils — plutôt **producteurs** que clients | Dons |
| **Collectivités** (transparence proactive) | Portail « où va l'argent » | Budget com' — rare |
| **Citoyens** | Consultation | Ne paient pas |

Modèle économique difficile ; valeur surtout **sociétale / réutilisation** (API,
jeu de données propre) plutôt que SaaS.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| **DECP consolidées** | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | LO 2.0 | Parquet/CSV | ~quotidienne | Seuil 40 k€ ; montant ≠ dépense réelle |
| **Schéma SCDL Subventions** | https://schema.data.gouv.fr/scdl/subventions/2.1.1/ | LO 2.0 | CSV normalisé | Par collectivité | **Pas de dump national** ; conformité faible |
| **RNA** | https://www.data.gouv.fr/datasets/repertoire-national-des-associations | LO 2.0 | CSV (142 dépts.) | MàJ **31 mai 2026** | Alsace-Moselle exclue |
| **SIRENE** | https://www.data.gouv.fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret | LO 2.0 | CSV | Mensuelle | Lien bénéficiaire subvention → SIREN |
| **API tabulaire data.gouv** | https://guides.data.gouv.fr/api-de-data.gouv.fr/reference/api-tabulaire | LO 2.0 | REST (beta) | Continue | Pour requêter DECP sans dump complet |

**Vérification disponibilité** (2026-06-21) :
- DECP : consolidé national, ouvert ✅
- Subventions : **fragmenté** — dizaines de jeux par collectivité sur data.gouv
  (ex. conventions > 23 k€ MàJ juin 2026), **pas d'équivalent DECP** ⚠️
- RNA : ouvert, 142 fichiers départementaux ✅

[`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements

| Question | Jointure | Faisabilité |
|---|---|---|
| Entreprise X : marchés + subventions reçus ? | SIRET/SIREN dans DECP.titulaire × SCDL.beneficiaire | **Bonne** si jeux SCDL publiés |
| Association Y : subventions de quelles collectivités ? | RNA × SCDL (nom ou SIRET asso) | **Moyenne** — identifiants hétérogènes |
| Collectivité Z : top bénéficiaires (marchés + subventions) ? | DECP.acheteur_id + SCDL.organisme | **Bonne** |
| Même bénéficiaire : part marchés vs subventions ? | Agrégat SQL par SIREN | **Bonne** — chiffres traçables |

**Bloquant produit** : l'absence de **consolidation nationale des subventions**
(comparable au DECP) impose un pipeline de moissonnage catalogue → coût infra élevé.

## 4. Existant / concurrence

> Cartographie B (consultée 2026-06-23). Toutes les sources vérifiées à cette date.

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **Data.Subvention** | https://datasubvention.beta.gouv.fr/ | Consolidation subventions associatives (SCDL) pour agents publics |
| **data.economie.gouv.fr — DECP** | https://data.economie.gouv.fr/ | Marchés publics, observatoire commande publique |
| **data.gouv.fr — DECP consolidées** | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | Dump tabulaire marchés publics |
| **data.gouv.fr — SCDL** | https://www.data.gouv.fr/datasets/subventions-aux-associations | Subventions aux associations (format standard) |

### Réutilisations data.gouv

| Acteur | URL | Rôle |
|---|---|---|
| **OpenBar** | https://www.data.gouv.fr/reuses/openbar | Transparence subventions (Regards Citoyens) |
| **decp.info** | https://www.data.gouv.fr/reuses/decp-info-interface-dexploration-et-de-telechargement-des-donnees-de-la-commande-publique-au-format-tabulaire | Exploration DECP (marchés uniquement) |
| **VigiCité** | https://www.data.gouv.fr/reuses/vigicite | Croisement élus + marchés + HATVP |

### Concurrents directs (croisement marchés publics × transparence)

**VigiCité** ([https://vigicite.org/](https://vigicite.org/), consulté 2026-06-23) :
croise HATVP + DECP + RNA + registre lobbys pour **6 763 élus** et **2,3 M marchés
publics**. Score transparence par élu. Pipeline reproductible (AGPL-3.0). Actif
(MàJ 2026-06-11). **Fait déjà DECP × RNA** — ne croise pas les subventions SCDL
mais constitue le concurrent civique le plus avancé sur le segment.

**decp.info** ([https://decp.info](https://decp.info), consulté 2026-06-23) :
interface d'exploration et téléchargement des DECP (Parquet/CSV/XLSX). Version
v2.7.3 publiée 2026-04-20. **Marchés publics uniquement** — aucune couche
subventions SCDL. Open source (Python). Free.

**Data.Subvention** ([https://datasubvention.beta.gouv.fr/](https://datasubvention.beta.gouv.fr/),
consulté 2026-06-23) : programme beta.gouv.fr (DJEPVA) qui **centralise les
subventions associatives** (État + collectivités) via SCDL et autres sources.
Accès **restreint aux agents publics** (État, collectivités, opérateurs). API
publique disponible. MàJ janvier 2026. **Substitut direct mais fermé** : fait
exactement la consolidation SCDL pour les agents, pas pour les journalistes/citoyens.

**data.economie.gouv.fr (OECP)** ([https://data.economie.gouv.fr/](https://data.economie.gouv.fr/),
consulté 2026-06-23) : marchés publics uniquement ; tableau de bord Observatoire
Économique Commande Publique. Pas de subventions.

### Benchmark catalogue SaaS — segments liés (`verified`/`partial` uniquement)

#### Segment `public-procurement-intel`

| Acteur | Marché FR | Angle subventions | Verdict |
|---|---|---|---|
| BOAMP open data (`verified`, FR) | strong | ❌ aucun | Source primaire, non concurrent |
| marchespublics.ai (`partial`, FR) | strong | ❌ aucun | Marchés seulement — veille AO |
| Maître AO (`partial`, FR) | strong | ❌ aucun | Alertes AO — hors périmètre |
| PLACE/achatpublic.com (`partial`, FR) | strong | ❌ aucun | e-Procurement acheteurs |

Conclusion segment : **aucun acteur `public-procurement-intel` ne croise les
subventions SCDL** — espace résiduel sur le croisement. Mais acteurs civiques
(VigiCité, Data.Subvention) comblent partiellement le besoin.

#### Segment `territorial-analytics`

| Acteur | Marché FR | Pertinence 0027 | Verdict |
|---|---|---|---|
| data.gouv.fr (`verified`, FR) | strong | Source primaire DECP+RNA | Infrastructure, pas produit |
| OFGL Observatoire (`verified`, FR) | strong | Finances locales | Périmètre budgétaire, pas subventions |
| Géoportail (`verified`, FR) | strong | Cartographie | Non pertinent |

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0027-transparence-subventions-marches` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `public-procurement-intel` — Intelligence marchés publics

Fichier : [`catalogue-saas/vendors/public-procurement-intel.json`](../../catalogue-saas/vendors/public-procurement-intel.json) (42 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `marchespublics-ai` | marchespublics.ai | FR | strong | verified |
| `maitre-ao` | Maître AO | FR | strong | verified |
| `aws-boamp` | BOAMP (open data) | FR | strong | verified |
| `achatpublic` | PLACE (achatpublic.com) | FR | strong | verified |
| `tussell` | Tussell | GB | absent | partial |
| `spend-network` | Spend Network | GB | absent | partial |
| `govwin-deltek` | GovWin (Deltek) | US | absent | partial |
| `open-contracting-partnership` | Open Contracting Partnership | GB | unknown | partial |
| `decp-info` | decp.info | FR | strong | verified |
| `data-economie-gouv` | data.economie.gouv.fr | FR | strong | partial |
| `openbar` | OpenBar (Regards Citoyens) | FR | strong | partial |
| `nextend-ai` | Nextend.ai | FR | strong | verified |
| … | _+30 autres_ | | | |

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

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment public-procurement-intel
```

<!-- catalogue-saas-end -->

## 5. Différenciation

La valeur propre serait **le triptyque public DECP × SCDL × RNA en un seul
outil requêtable par des non-experts** (journalistes, citoyens). Mais :

- **VigiCité** couvre déjà DECP × RNA × HATVP (open source, AGPL-3.0, actif en
  2026) → facilement extensible à SCDL.
- **Data.Subvention** (beta.gouv.fr) fait déjà la consolidation SCDL côté agents
  publics → pourrait ouvrir au public.
- La donnée ouverte n'est pas un avantage défendable : n'importe qui peut
  répliquer le pipeline en quelques semaines.
- Différenciation insuffisante face à des acteurs civiques déjà actifs.

## 6. Faisabilité & fiabilité technique

- DECP → DuckDB (comme 0001).
- Subventions : crawl API catalogue data.gouv (`schema=scdl/subventions`) → ingestion
  normalisée — effort significatif, maintenance continue.
- Matching RNA ↔ bénéficiaire : fuzzy sur dénomination — **afficher score de confiance**.
- Principe RAG/SQL strict : montants = SQL ; sens juridique subvention = RAG.
- Faisabilité technique bonne, mais coût infra/maintenance disproportionné face
  au revenu escompté.

## 7. Monétisation / impact

| Modèle | Réalisme |
|---|---|
| SaaS journalistes/rédactions | Très faible (budgets outils contraints) |
| Subvention / grant (DINUM, Data.gouv) | Possible mais non pérenne |
| API payante ONG/collectivités | Très faible (alternative publique gratuite prévisible) |
| Impact sociétal (transparence démocratie) | Élevé, non monétisable directement |

Valeur principale = **bien commun**, pas revenu. Modèle économique absent.

## 8. Risques

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Data.Subvention ouvre au public (beta.gouv.fr) | Haute | Éliminatoire | Néant — le produit déplace la valeur |
| VigiCité ajoute couche SCDL | Moyenne | Éliminatoire | Néant — open source, facile |
| SCDL fragmentation persistante | Haute | Bloquant MVP | Moissonnage partiel ; taux de couverture affiché |
| Matching RNA/SCDL de mauvaise qualité | Haute | Réputation | Score confiance obligatoire |
| Pas de modèle de revenus | Certaine | Projet non viable | — |

**Risque éliminatoire identifié** : l'État (beta.gouv.fr) construit déjà le
produit cible. Aucune fenêtre de différenciation durable.

## 9. Effort MVP

Périmètre minimal crédible :
1. Ingestion DECP (Parquet existant) + 20–30 jeux SCDL des grandes collectivités.
2. Jointure SIREN/RNA sur bénéficiaires.
3. Interface de recherche : « toutes les aides (marchés + subventions) à l'entité X ».
4. Export CSV.

Estimation : 4–6 semaines développeur. Mais maintenance des jeux SCDL (centaines
de fichiers, mise à jour disparate) = charge continue non viable sans équipe dédiée.

## 10. Scoring

| # | Critère | Poids | Note | Pts |
|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | ×3 | 2 | 6 |
| C3 | Disponibilité & fiabilité des données | ×3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 2 | 4 |
| C5 | Différenciation défendable | ×2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | ×2 | 4 | 8 |
| C7 | Facilité du MVP (effort faible) | ×2 | 3 | 6 |
| C8 | Maîtrise des risques | ×2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 4 |
| | **Total** | | | **54 / 105** |

**Score /100 = round(54 / 105 × 100) = 51**

> **Score révisé après revue red team (2026-06-23) : 48/100** — la revue abaisse
> C4 et C5 de 2 à 1 : l'affirmation §1 « aucun outil ne propose ce triptyque » est
> **fausse** (Éclaireur Public — Anticor + Data for Good, fév. 2025 — croise déjà
> subventions SCDL **et** marchés DECP par collectivité ; DépensesPubliques affiche
> les deux). Total 50/105 → 48/100. Verdict inchangé (❌ Écartée). Recalcul détaillé
> dans [`revue.md`](revue.md).

### Détail des notes

- **C1 = 3** : Douleur réelle (croisement manuel fastidieux) mais niche étroite
  (journalistes, ONG). Pas de masse critique.
- **C2 = 2** : Journalistes = budget outils très faible. ONG = dons. Collectivités
  = très rare. Citoyens = gratuit attendu. Aucun payeur B2B solide.
- **C3 = 3** : DECP ✅ et RNA ✅ consolidés. SCDL = fragmenté ⚠️ (dizaines de
  jeux, pas de dump national). Data.Subvention émergent côté agents publics.
- **C4 = 2** : VigiCité (DECP×RNA×HATVP, actif 2026) et Data.Subvention (SCDL,
  agents publics) occupent le terrain adjacent. Espace résiduel étroit.
- **C5 = 2** : Réplicable par VigiCité en quelques semaines (AGPL, open source).
  Data.Subvention peut ouvrir au public. Aucun avantage durable.
- **C6 = 4** : SQL strict sur données ouvertes, traçabilité garantie. Score
  confiance fuzzy-matching RNA = bonne pratique. Techniquement solide.
- **C7 = 3** : MVP 4–6 semaines sur quelques jeux SCDL. Consolidation nationale =
  chantier continu non viable.
- **C8 = 2** : Risque éliminatoire : Data.Subvention (beta.gouv.fr) peut ouvrir
  au public à tout moment. VigiCité peut étendre. Risques non maîtrisables.
- **C9 = 2** : Impact démocratique élevé mais non monétisable. Aucun modèle
  économique viable identifié.

## 11. Verdict & décision

❌ **Écartée** — Score **51/100** (< seuil 55).

**Motif principal** : **absence de modèle économique viable** combinée à un
**risque éliminatoire institutionnel** (Data.Subvention beta.gouv.fr construit
déjà le produit cible pour les agents publics et pourrait ouvrir au public).
VigiCité couvre déjà DECP × RNA en open source et peut étendre à SCDL facilement.

**Point bloquant** : personne ne paie pour ce type de transparence (C2 = 2) et
l'État (via beta.gouv.fr) construit la même chose avec bien plus de ressources.

**À ne pas reproposer** sans : (1) identification d'un payeur B2B concret avec
budget > 10 k€/an, ET (2) angle de différenciation qui échappe à l'institutionnel.

**Prochaine étape** : aucune — idée écartée, conservée pour référence.

---

0027 | Transparence subventions × marchés publics (DECP × SCDL × RNA) | ❌ Écartée | 48/100 | Triptyque déjà livré par Éclaireur Public (score revu, cf. revue.md)
