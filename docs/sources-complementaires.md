# Sources de données complémentaires — vérification & usages

Document de référence pour les croisements de données. Chaque source a été
**vérifiée le 2026-06-21** (fiche data.gouv.fr, appel API ou téléchargement
d'échantillon).

Légende **disponibilité** :
- ✅ **Open** — téléchargeable ou API sans habilitation métier
- 🔑 **Compte** — inscription gratuite requise (quota)
- 🔒 **Restreint** — habilitation administration (API Entreprise, DataPass)
- ⚠️ **Partiel** — couverture nationale incomplète ou qualité hétérogène

---

## Tableau de vérification

| Source | Disponibilité | URL | Format | Fraîcheur vérifiée | Limites | Usages croisables |
|---|---|---|---|---|---|---|
| **RNIC** (copropriétés) | ✅ Open | [data.gouv.fr/datasets/registre-national-dimmatriculation-des-coproprietes](https://www.data.gouv.fr/datasets/registre-national-dimmatriculation-des-coproprietes) | CSV ~430 Mo/trimestre (**virgule** depuis avr. 2026) | MàJ **17 juin 2026** ; MAJ quotidienne depuis avril 2026 | Pas de nom propriétaire ; syndic (SIRET) ~**76 %** des copros (échantillon 100 k, pro) ; changement format avril 2026 | × DPE (adresse), × DECP (SIRET syndic/RGE), × BAN |
| **RNE** (élus) | ✅ Open | [data.gouv.fr/datasets/repertoire-national-des-elus-1](https://www.data.gouv.fr/datasets/repertoire-national-des-elus-1) | CSV (12 fichiers mandats) | MàJ **9 juin 2026** (élections mars 2026) | Trimestriel ; rectifications via préfecture uniquement | × HATVP (nom), × DECP (commune acheteur), × subventions |
| **RNA** (associations) | ✅ Open | [data.gouv.fr/datasets/repertoire-national-des-associations](https://www.data.gouv.fr/datasets/repertoire-national-des-associations) | CSV (142 fichiers dépt.) | MàJ **31 mai 2026** | Alsace-Moselle hors périmètre ; pas de SIREN systématique | × subventions SCDL, × SIRENE (si RNA→SIREN) |
| **RPG** (parcelles agricoles) | ✅ Open | [data.gouv.fr/datasets/registre-parcellaire-graphique-agricole](https://www.data.gouv.fr/datasets/registre-parcellaire-graphique-agricole) | CSV/GeoJSON/ZIP | MàJ **20 juin 2026** | Métropole ; jointure PCI requise | × Géorisques (spatial), × Hub'Eau, × GPU/PLU |
| **API Melodi** (catalogue INSEE) | 🔑 Compte | [data.gouv.fr/dataservices/api-melodi](https://www.data.gouv.fr/dataservices/api-melodi) | REST JSON | 99 jeux associés (ex. IPC MàJ juin 2026) | Inscription portail-api.insee.fr ; quotas | Accès unifié INSEE pour copilotes territoriaux |
| **API Marché du travail** (France Travail) | 🔑 Compte | [data.gouv.fr/dataservices/api-marche-du-travail](https://www.data.gouv.fr/dataservices/api-marche-du-travail) | REST JSON | Référencée déc. 2025 | OAuth France Travail ; pas de dump CSV national simple | × SIRENE (NAF), × FiLoSoFi (IRIS), × communes |
| **API tabulaire data.gouv** | ✅ Open | [guides.data.gouv.fr — API tabulaire](https://guides.data.gouv.fr/api-de-data.gouv.fr/reference/api-tabulaire) | REST (beta) | Continue | Beta ; dépend de la ressource publiée | Requêter DECP, RNIC, etc. sans télécharger |
| **Hub'Eau** (eau) | ✅ Open | [hubeau.eaufrance.fr](https://hubeau.eaufrance.fr/) — ex. hydrométrie v2 | REST JSON | API v2.0.1 répond (test 21/06/2026) | Endpoints multiples ; pas un seul jeu ; v1 parfois obsolète | × RPG (bassins), × Géorisques ICPE, × communes |
| **SSMSI** (délinquance) | ✅ Open | [data.gouv.fr — bases statistiques délinquance](https://www.data.gouv.fr/datasets/bases-statistiques-communale-departementale-et-regionale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales) | CSV (10 fichiers) | MàJ **27 mars 2026** | **Communal/départemental**, pas géolocalisé adresse ; faits enregistrés ≠ ressenti | × FiLoSoFi, × DVF, × implantation commerciale |
| **Cartes de bruit** | ⚠️ Partiel | [data.gouv.fr — zones bruit 4e échéance](https://www.data.gouv.fr/datasets/zones-de-bruit-des-cartes-de-bruit-strategiques-4eme-echeance-1) | Shapefile par infra/dépt. | Variable par agglomération | Pas de couverture homogène nationale ; couches éclatées | × DPE, × DVF (spatial join) |
| **Base Mérimée** (patrimoine) | ✅ Open | [data.gouv.fr/datasets/base-merimee-1](https://www.data.gouv.fr/datasets/base-merimee-1) | CSV/API culture | MàJ régulière (Min. Culture) | Monuments historiques ≠ tout le bâti ancien | × DVF, × DPE, × tourisme |
| **RPLS** (logement social) | ⚠️ Partiel | Pas de jeu national unique ; ex. [RPLS 2021 Ithéa](https://www.data.gouv.fr/datasets/repertoire-des-logements-locatifs-des-bailleurs-sociaux-rpls-2021) (MàJ **mars 2023**) | CSV ~5 Mo (échantillon) | Millésimes locaux/régionaux | **Fragmenté** (11 jeux « RPLS » sur data.gouv, pas de consolidation nationale type DECP) | × DPE (adresse), × OFGL — avec prudence |
| **Subventions SCDL** | ⚠️ Partiel | Schéma : [schema.data.gouv.fr/scdl/subventions](https://schema.data.gouv.fr/scdl/subventions/) | CSV normalisé par collectivité | Jeux hétérogènes (ex. MàJ **21 juin 2026** sur certains dépts.) | Pas de consolidation nationale ; obligation > 23 k€ ; conformité faible | × DECP (SIRET), × RNA, × SIRENE |
| **Copernicus Land** (UE) | ✅ Open | [land.copernicus.eu](https://land.copernicus.eu/) | Raster/API | Continu | Résolution ~10–100 m ; expertise SIG | × parcelles, × DRIAS (complément) |

---

## Clés de jointure pour les nouveaux croisements

| Croisement | Clés | Faisabilité technique |
|---|---|---|
| RNIC × DPE | Adresse normalisée (BAN) ou code INSEE + complément | **Moyenne** — adresses copropriété parfois imprécises |
| RNIC × DECP | SIRET syndic / titulaire RGE | **Bonne** si SIRET présent |
| RPG × Géorisques | Jointure spatiale parcelle/ICPE | **Bonne** en PostGIS |
| DECP × subventions SCDL | SIRET bénéficiaire / titulaire | **Bonne** quand les deux jeux existent |
| HATVP × RNE × DECP | Nom élu (fuzzy) + code commune | **Faible** — matching nominatif risqué |
| France Travail × FiLoSoFi | Code commune / IRIS | **Bonne** |
| SSMSI × FiLoSoFi | Code commune INSEE | **Bonne** (agrégats) |
| DPE × cartes bruit | Coordonnées / parcelle | **Moyenne** — couverture bruit inégale |

---

## Usages recommandés par idée

| Idée | Sources ajoutées | Intérêt |
|---|---|---|
| [0007](../idees/0007-fiche-commune-intelligente/) | Melodi, SSMSI, FiLoSoFi, REI | Fiche commune enrichie multi-indicateurs |
| [0009](../idees/0009-dpe-passoires-thermiques/) | RNIC, RPLS, cartes bruit | Pivot copropriétés / parc social |
| [0018](../idees/0018-transparence-vie-publique/) | RNE, RNA, subventions, DECP | Transparence élargie |
| [0025](../idees/0025-coproprietes-renovation-rnic/) | RNIC × DPE × DECP | **Nouvelle** — syndics/bailleurs |
| [0026](../idees/0026-exposition-parcelles-agricoles/) | RPG × Géorisques × Hub'Eau | **Nouvelle** — agriculteurs/aménageurs |
| [0027](../idees/0027-transparence-subventions-marches/) | DECP × SCDL × RNA | **Nouvelle** — journalistes/ONG |
| [0028](../idees/0028-tensions-emploi-territoire/) | France Travail × SIRENE × FiLoSoFi | **Nouvelle** — franchises/recrutement |

---

## Sources écartées ou non retenues

| Source | Raison |
|---|---|
| Fichier délinquance **géolocalisé** (ancien SSMSI fin) | Jeu national géolocalisé **introuvable** sur data.gouv (404) ; seul le communautaire SSMSI est disponible |
| RPLS national consolidé | **Absent** — uniquement extraits locaux/régionaux |
| API Entreprise (bilans, URSSAF) | 🔒 Habilitation — hors périmètre open data strict |
| Enedis/RTE consommation | 🔒 Accès restreint pour la majorité des usages |

---

*À mettre à jour lors de chaque nouvelle idée ou changement de disponibilité.*
