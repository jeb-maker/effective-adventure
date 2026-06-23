# Copilote d'études territoriales (RAG sur données publiques)

- **ID** : 0003
- **Statut** : ❌ Écartée (produit généraliste)
- **Score** : 46 / 100
- **Dernière mise à jour** : 2026-06-23
- **Révision critique** : voir [`revue.md`](revue.md) — score posé à **46/100**
  et statut passé de 🔁 à **❌ Écartée** après audit adversarial (concurrent grand
  public direct **Urbaa.app** omis, briques OSS **h-genai** / **france-data-mcp**,
  outillage public **OFGL** et **POC Albert** ; le créneau « brancher un LLM sur
  data.gouv » est tenu par l'acteur officiel ; aucun payeur identifié — §2 absente).
  La valeur résiduelle (couche de fiabilité transverse au-dessus d'un vertical
  comme 0001) n'est **pas un produit à prototyper seul**.
- **Pitch (1 phrase)** : Un assistant qui transforme les données publiques en
  rapports fiables et cités sur un territoire (comparer des communes, expliquer
  des finances locales, etc.).

---

## 1. Problème / douleur
Explorer data.gouv.fr est lent pour un non-spécialiste. Un assistant qui
sélectionne les bons datasets, calcule juste et cite ses sources ferait gagner
beaucoup de temps.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| API catalogue + MCP data.gouv.fr | https://github.com/datagouv/datagouv-mcp | LO 2.0 | MCP/JSON | Continue | Métadonnées + tabulaire, pas de calcul fiable via LLM |
| API Melodi (catalogue INSEE unifié) | https://www.data.gouv.fr/dataservices/api-melodi | LO (Insee) | REST JSON | 99 jeux (vérifié 2026-06-21) | Compte requis ; remplace les dumps CSV dispersés |
| API tabulaire data.gouv (beta) | https://guides.data.gouv.fr/api-de-data.gouv.fr/reference/api-tabulaire | LO 2.0 | REST | Continue | Beta ; dépend de la qualité de chaque ressource |
| OFGL, SIRENE, DVF, transport.data.gouv.fr | (cf. idées verticales 0001, 0006, 0007) | LO 2.0 | Variable | Variable | Multi-domaines — risque de généraliste peu fiable |

> [`docs/sources-complementaires.md`](../../docs/sources-complementaires.md)

### 3bis. Croisements envisagés

- **Melodi × OFGL × communes** : comparer des territoires homogènes sans ingérer
  manuellement chaque dump INSEE.
- **API tabulaire × catalogue MCP** : sélection automatique du bon jeu + requête SQL
  traçable (principe RAG sens / SQL chiffres).
- **Vertical first** : le copilote ne doit pas rester généraliste — chaque vertical
  (0001 commande publique, 0007 finances locales) apporte ses jointures métier.

## 4. Existant / concurrence

> Cartographie B (consultée 2026-06-23). L'État et les réutilisations couvrent déjà
> l'accès IA aux données territoriales ouvertes.

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **data.gouv.fr — MCP officiel** | https://github.com/datagouv/datagouv-mcp , https://guides.data.gouv.fr/intelligence-artificielle/le-serveur-mcp-de-data.gouv.fr | Serveur MCP catalogue/métadonnées/ressources/tabulaire |
| **Albert API (Etalab)** | https://albert.api.etalab.gouv.fr/ | LLM souverain pour agents publics |
| **OFGL — data.ofgl.fr** | https://data.ofgl.fr/ | Ratios financiers collectivités (SQL traçable) |
| **Melodi (INSEE)** | https://www.insee.fr/fr/statistiques/5031326 | API statistiques territoriales officielles |

### Réutilisations data.gouv

| Acteur | URL | Rôle |
|---|---|---|
| **Urbaa.app** | https://www.data.gouv.fr/reuses/urbaa-app | Copilote territorial open data (indicateurs par commune) |
| **france-data-mcp** (OSS) | https://github.com/habib256/france-data-mcp | MCP communautaire jeux data.gouv |
| **h-genai** (OSS) | https://github.com/huggingface/h-genai | RAG sur catalogues open data FR |

### Produits commerciaux / OSS

data.gouv.fr **avance déjà** sur l'IA :
- Serveur **MCP officiel** (lecture catalogue/métadonnées/ressources/tabulaire) —
  https://github.com/datagouv/datagouv-mcp ,
  https://guides.data.gouv.fr/intelligence-artificielle/le-serveur-mcp-de-data.gouv.fr
- **Skill data.gouv.fr** (doc structurée pour LLM) —
  https://github.com/datagouv/datagouv-skill
- MCP tiers (ex. recherche d'entreprises). (Consultés 2026-06-23.)

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0003-copilote-territorial-rag` — segments liés pour benchmark concurrence structuré.
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

#### Segment `rag-knowledge` — RAG & knowledge enterprise

Fichier : [`catalogue-saas/vendors/rag-knowledge.json`](../../catalogue-saas/vendors/rag-knowledge.json) (19 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `glean` | Glean | US | partial | partial |
| `dust` | Dust | FR | partial | partial |
| `coveo` | Coveo | US | partial | partial |
| `contextual-ai` | Contextual AI | US | partial | partial |
| `vespa` | Vespa.ai | US | partial | partial |
| `onyx-enterprise` | Onyx (Danswer) | US | partial | partial |
| `kapa-ai` | kapa.ai | US | partial | partial |
| `ragie` | Ragie | US | partial | partial |
| `guru` | Guru | US | partial | partial |
| `bloomfire` | Bloomfire | US | partial | partial |
| `elastic-enterprise-search` | Elastic Enterprise Search | NL | partial | partial |
| `deepset` | deepset | DE | partial | partial |
| … | _+7 autres_ | | | |

#### Segment `bi-analytics-platforms` — BI & analytics

Fichier : [`catalogue-saas/vendors/bi-analytics-platforms.json`](../../catalogue-saas/vendors/bi-analytics-platforms.json) (18 entrées)

| ID | Nom | HQ | Marché FR | Vérification |
|---|---|---|---|---|
| `tableau` | Tableau (Salesforce) | US | partial | partial |
| `power-bi` | Microsoft Power BI | US | partial | partial |
| `looker` | Looker (Google Cloud) | US | partial | partial |
| `thoughtspot` | ThoughtSpot | US | partial | partial |
| `mode-analytics` | Mode | US | partial | partial |
| `qlik-sense` | Qlik Sense | SE | partial | partial |
| `domo` | Domo | US | partial | partial |
| `sisense` | Sisense | IL | partial | partial |
| `metabase` | Metabase | US | partial | partial |
| `hex-tech` | Hex | US | partial | partial |
| `sigma-computing` | Sigma Computing | US | partial | partial |
| `microstrategy` | MicroStrategy | US | partial | partial |
| … | _+6 autres_ | | | |

Commandes :
```bash
python3 scripts/catalogue_saas.py stats
python3 scripts/catalogue_saas.py gaps --segment territorial-analytics
```

<!-- catalogue-saas-end -->
## 6. Faisabilité & fiabilité technique
Piège majeur : **mélanger RAG et chiffres**. data.gouv.fr le dit pour son propre
MCP : réponses « approximatives ou erronées », « en aucun cas une source
officielle ». Impose RAG(sens)/SQL(chiffres) strict.

## 10. Scoring

> Tableau posé par la revue critique (la fiche n'en avait pas). Notes adversariales.

| # | Critère | Poids | Note (1-5) | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 3 | 9 | Douleur réelle mais diffuse et déjà asséchée par le MCP officiel + Urbaa. |
| C2 | Cible solvable (qui paie) | 3 | 2 | 6 | Aucun payeur identifié (§2 absente) ; alternatives gratuites (MCP, Urbaa). |
| C3 | Disponibilité & fiabilité données | 3 | 3 | 9 | Inputs prêts (MCP, Melodi, OFGL) mais fiabilité généraliste fragile. |
| C4 | Espace concurrentiel libre | 2 | 1 | 2 | Occupé par l'acteur officiel + Urbaa.app + OSS (h-genai, france-data-mcp). |
| C5 | Différenciation défendable | 2 | 2 | 4 | « Fiabilité vérifiable » non prouvée, copiable, déjà visée par l'État. |
| C6 | Faisabilité & fiabilité technique | 2 | 3 | 6 | RAG/SQL en intention OK, mais inapplicable en généraliste sans verticaux. |
| C7 | Facilité du MVP | 2 | 2 | 4 | Périmètre « tout data.gouv » trop large ; la fiche admet « vertical first ». |
| C8 | Maîtrise des risques | 2 | 2 | 4 | Risque concurrentiel (acteur officiel) + fiabilité non maîtrisés. |
| C9 | Monétisation / impact | 2 | 2 | 4 | Pas de revenu (gratuit public) ; impact déjà porté par data.gouv/Albert. |
| | **Total** | | | **48 / 105** | |

**Score /100** : 48 / 105 × 100 = **46**

## 11. Verdict & décision
❌ **Écartée** (produit généraliste) — décision **issue de la revue critique**
(score recalculé 46/100, < 55).

Bonne **vision**, mauvais **point de départ** : trop large, et l'acteur officiel
occupe déjà le terrain « brancher un LLM sur data.gouv.fr » (MCP officiel public
sans clé, POC Albert). Surtout, un **concurrent grand public direct** existe —
**Urbaa.app** (35 000 communes analysées par IA, comparaison de territoires,
finances locales, 29 sources open data, consulté 2026-06-23) — et le « copilote
finances locales » est déjà disponible en **open source** (h-genai) comme dans
l'**outillage public** (OFGL). La valeur n'est pas la connexion (déjà faite) ni
même un produit horizontal : c'est, au mieux, une **couche transverse de
fiabilité** au-dessus d'un vertical (ex. 0001). Tant qu'aucun **payeur précis**
ni **différenciateur prouvé** face à Urbaa/MCP n'est démontré, ne pas prototyper.

**Prochaine étape** : si l'angle revient, le traiter comme module de fiabilité de
0001 (et non comme idée généraliste autonome), avec payeur B2B/B2G identifié.
