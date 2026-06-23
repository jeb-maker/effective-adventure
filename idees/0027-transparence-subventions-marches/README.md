# Transparence subventions × marchés publics (DECP × SCDL × RNA)

- **ID** : 0027
- **Statut** : 💡 Capturée
- **Score** : — / 100 (à analyser)
- **Dernière mise à jour** : 2026-06-21
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

## 4. Existant / concurrence (première passe)

- **VigiCité** : HATVP × marchés × lobbys — pas subventions SCDL
- **data.economie.gouv.fr / decp.info** : marchés uniquement
- **Regards Citoyens / OpenBar** (subventions) : angle subventions, pas croisement DECP systématique — **à vérifier**
- **Data.Subvention** (Chorus) : accès restreint agents publics

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0027-transparence-subventions-marches` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `public-procurement-intel` — Intelligence marchés publics

Fichier : [`catalogue-saas/vendors/public-procurement-intel.json`](../../catalogue-saas/vendors/public-procurement-intel.json) (15 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `marchespublics-ai` | marchespublics.ai | FR | strong | partial |
| `maitre-ao` | Maître AO | FR | strong | partial |
| `aws-boamp` | BOAMP (open data) | FR | strong | verified |
| `achatpublic` | PLACE (achatpublic.com) | FR | strong | partial |
| `tussell` | Tussell | GB | absent | partial |
| `spend-network` | Spend Network | GB | absent | partial |
| `govwin-deltek` | GovWin (Deltek) | US | absent | partial |
| `open-contracting-partnership` | Open Contracting Partnership | GB | unknown | partial |
| `decp-info` | decp.info | FR | strong | partial |
| `data-economie-gouv` | data.economie.gouv.fr | FR | strong | partial |
| `openbar` | OpenBar (Regards Citoyens) | FR | strong | partial |
| `nextend-ai` | Nextend.ai | FR | strong | partial |
| … | _+3 autres_ | | | |

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

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment public-procurement-intel
```

<!-- catalogue-saas-end -->
## 6. Faisabilité & fiabilité technique

- DECP → DuckDB (comme 0001).
- Subventions : crawl API catalogue data.gouv (`schema=scdl/subventions`) → ingestion
  normalisée — effort significatif, maintenance continue.
- Matching RNA ↔ bénéficiaire : fuzzy sur dénomination — **afficher score de confiance**.
- Principe RAG/SQL strict : montants = SQL ; sens juridique subvention = RAG.

## 11. Verdict & décision

💡 **Capturée** — croisement **pertinent démocratiquement**, données **partiellement
disponibles** (DECP oui, subventions fragmentées). Proche de 0010 (boussole aides)
et 0018 (transparence) — à fusionner ou différencier en analyse.

**Prochaine étape** : inventorier via API catalogue le nombre de jeux tagués
`scdl/subventions` et le taux de conformité Validata — condition sine qua non du MVP.
