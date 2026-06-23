# Radar de la commande publique (intelligence d'attribution)

- **ID** : 0001
- **Statut** : 🔁 À retravailler
- **Score** : 66 / 100
- **Dernière mise à jour** : 2026-06-20
- **Révision critique** : voir [`revue.md`](revue.md) — score abaissé de **76 à 66**
  après audit adversarial (concurrents directs omis : Maître AO, Nextend.ai,
  marchespublics.ai… ; `montant` DECP ≠ dépense réelle ; délais de publication).
  L'analyse ci-dessous reflète le 1er passage et reste à corriger.
- **Pitch (1 phrase)** : Un outil d'**intelligence concurrentielle** sur les
  marchés publics **attribués** (qui a gagné quoi, où, à quel prix, chez quels
  acheteurs récurrents) — pas une énième veille d'avis à venir.

---

## 1. Problème / douleur
Répondre aux appels d'offres est vital pour beaucoup de PME/ETI, mais elles
pilotent à l'aveugle sur le **passé** : qui sont mes concurrents réels sur mon
secteur, quelle part de marché ils captent, quels acheteurs sont récurrents,
quels contrats arrivent à échéance (donc à reconquérir). Cette intelligence
existe dans les données mais reste difficile à exploiter.

## 2. Cible & qui paie
- **PME/ETI répondant aux AO** : payent déjà pour de la veille (30–100 €/mois).
- **Cabinets / consultants / fédérations professionnelles** : études sectorielles.
- **Journalistes / chercheurs / transparence** : faible budget, mais excellents
  pour la crédibilité et l'acquisition.

Utilisateur = payeur dans le cas PME, ce qui est sain.

## 3. Données sources

| Source | URL | Licence | Format | Fraîcheur | Limites |
|---|---|---|---|---|---|
| DECP consolidées (marchés **attribués**) | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | Licence Ouverte 2.0 | Parquet / CSV | ~quotidienne | Qualité hétérogène, marchés non conformes écartés, MAPA < 90 k€ souvent absents |
| API DECP (publication) | https://www.data.gouv.fr/datasets/api-decp | Licence Ouverte 2.0 | XML/JSON via `files.data.gouv.fr/decp` | continue | Fichiers par SIRET, pensés pour la publication, pas la conso |
| BOAMP (avis **à venir** + résultats) | https://www.data.gouv.fr/dataservices/api-bulletin-officiel-des-annonces-des-marches-publics-boamp | Licence Ouverte 2.0 | API CSV/JSON/Excel | continue | Partiel (jeu de seuils) ; terrain de la veille, **saturé** |
| Base SIRENE | https://www.data.gouv.fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret | Licence Ouverte | CSV | mensuelle (INSEE) | Enrichissement titulaires |

Clés techniques DECP : `uid` = SIRET acheteur + id marché ; plusieurs lignes par
marché (titulaires multiples, avenants via `modification_id`) ; `donneesActuelles`
= dernière version. → **données tabulaires propres, donc SQL fiable**.

## 4. Existant / concurrence

> Cartographie B complète (consultée 2026-06-23). Catalogue SaaS segment
> `public-procurement-intel` : 42 entrées — voir ci-dessous.

**Verdict saturation** : veille AO **saturée** ; analyse d'attribution **disputée**
(Maître AO, Nextend.ai, marchespublics.ai intègrent déjà DECP).

### Services publics / .gouv.fr

| Acteur | URL | Rôle |
|---|---|---|
| **BOAMP (open data)** | https://www.boamp.fr/ / https://www.data.gouv.fr/datasets/boamp | Source officielle avis de marché |
| **data.economie.gouv.fr — DECP** | https://data.economie.gouv.fr/ | Données essentielles commande publique consolidées |
| **PLACE / profils acheteurs** | https://www.achatpublic.com/ , https://www.maximilien.fr/ | Dématérialisation côté acheteurs |
| **Tableau de bord comptes collectivités** | https://data.economie.gouv.fr/explore/dataset/comptes-individuels-des-collectivites/ | Contexte acheteur public (adjacent) |

### Réutilisations data.gouv

| Acteur | URL | Rôle |
|---|---|---|
| **decp.info** | https://www.data.gouv.fr/reuses/decp-info-interface-dexploration-et-de-telechargement-des-donnees-de-la-commande-publique-au-format-tabulaire | Exploration DECP tabulaire (outil, pas produit SaaS) |
| **OpenMarchés** | https://www.data.gouv.fr/reuses/openmarches-visualisation-des-marches-it-publics | Analytics attribution marchés IT (479k+ contrats) |
| **OpenBar / subventions** | https://openbar.fr/ | Transparence subventions (adjacent idée 0027) |

### Produits commerciaux (veille + attribution)

Veille **saturée** : Vecteur Plus, France Marchés, Synapse, Doaken, Olra,
PublikConnect (49 € HT), AlertOffres (29,99 €), Saqara (ex-AOS), Explore,
Marchés Online, Dématis, Centrale des Marchés, Tendly, Remporte, Maître AO,
Nextend.ai, marchespublics.ai — plusieurs avec IA (scoring DCE, mémoire technique).
Sources comparatifs (2026-06-20) : https://olra.fr/blog/alternatives-synapse-france-marches-comparatif ,
https://remporte.fr/blog/plateformes-appels-offres-comparatif/ ,
https://publikconnect.fr/tarifs/ , https://www.alertoffres.fr/tarifs

**Attribution DECP** : plus « vierge » qu'annoncé — Maître AO (82k+ titulaires),
Nextend.ai (observatoire), marchespublics.ai (benchmark 10 M+ contrats), DOAKEN,
OpenMarchés.

### Open source / bricolage

- Requêtes API tabulaire data.gouv + DuckDB sur dump DECP Parquet
- Excel / Metabase sur jeux BOAMP + DECP open data

<!-- catalogue-saas-begin -->

### Référence catalogue SaaS (dépôt)

**Idée** : `0001-radar-commande-publique` — segments liés pour benchmark concurrence structuré.
**Mise à jour** : 2026-06-23 — ne pas utiliser les entrées `unverified` pour scorer.

#### Segment `public-procurement-intel` — Intelligence marchés publics

Fichier : [`catalogue-saas/vendors/public-procurement-intel.json`](../../catalogue-saas/vendors/public-procurement-intel.json) (20 entrées)

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
| … | _+8 autres_ | | | |

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
## 5. Différenciation
Ne pas concurrencer la veille frontalement. Se positionner sur **l'intelligence
d'attribution récurrente** : fiche acheteur, fiche entreprise (SIREN), vue
secteur (CPV + région), détection d'anomalies (attributions sans concurrence,
avenants massifs — cf. OpenMarchés : +239 900 % d'avenant constaté), et surtout
**alerte « contrats arrivant à échéance »** (signal de prospection). Imitable à
terme, mais aucun acteur n'en a fait un produit self-service récurrent.

## 6. Faisabilité & fiabilité technique
DECP consolidé → DuckDB → requêtes structurées. Tous les chiffres (montants,
parts de marché, comptes) viennent de SQL traçable. Le LLM ne sert qu'à
**expliquer** (libellés CPV, procédures, « pourquoi ce marché t'intéresse »).
Conforme au principe RAG(sens)/SQL(chiffres). **Risque d'hallucination faible
par construction.**

## 7. Monétisation / impact
SaaS B2B 30–100 €/mois, aligné sur le marché existant, en se branchant comme
complément « intelligence » à la veille que les clients ont déjà. Tier gratuit
transparence/journalisme pour l'acquisition.

## 8. Risques
- Concurrents bien financés → rester sur l'angle attribution, pas la veille.
- Qualité/couverture DECP → **afficher honnêtement le taux de couverture**.
- Sensibilité du « qui a gagné » → discours transparence, pas délation.

## 9. Effort MVP
1. Ingestion DECP consolidé → DuckDB (normalisation `uid`/titulaires/avenants).
2. 3 écrans : fiche acheteur, fiche entreprise (SIREN), vue secteur (CPV+région).
3. 2 alertes : nouveaux marchés sur périmètre ; contrats arrivant à échéance.
4. Traçabilité : chaque chiffre → ligne DECP source + date + taux de couverture.

## 10. Scoring

| # | Critère | Poids | Note (1-5) | Pondéré |
|---|---|---|---|---|
| C1 | Intensité du problème | 3 | 4 | 12 |
| C2 | Cible solvable (qui paie) | 3 | 4 | 12 |
| C3 | Disponibilité & fiabilité données | 3 | 4 | 12 |
| C4 | Espace concurrentiel libre | 2 | 3 | 6 |
| C5 | Différenciation défendable | 2 | 3 | 6 |
| C6 | Faisabilité & fiabilité technique | 2 | 5 | 10 |
| C7 | Facilité du MVP | 2 | 4 | 8 |
| C8 | Maîtrise des risques | 2 | 3 | 6 |
| C9 | Monétisation / impact | 2 | 4 | 8 |
| | **Total** | | | **80 / 105** |

**Score /100** : 80 / 105 × 100 = **76**

## 11. Verdict & décision
✅ **Go.** Meilleur ratio « donnée prête × cible qui paie × créneau libre ». Le
seul morceau non saturé du marché des marchés publics est l'**analyse
d'attribution**. Prochaine étape : spécifier le schéma DECP exact + requêtes
DuckDB de référence, puis prototyper la fiche acheteur.
