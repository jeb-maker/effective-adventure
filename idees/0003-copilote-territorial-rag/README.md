# Copilote d'études territoriales (RAG sur données publiques)

- **ID** : 0003
- **Statut** : 🔁 À retravailler
- **Score** : — / 100 (analyse partielle)
- **Dernière mise à jour** : 2026-06-21
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
data.gouv.fr **avance déjà** sur l'IA :
- Serveur **MCP officiel** (lecture catalogue/métadonnées/ressources/tabulaire) —
  https://github.com/datagouv/datagouv-mcp ,
  https://guides.data.gouv.fr/intelligence-artificielle/le-serveur-mcp-de-data.gouv.fr
- **Skill data.gouv.fr** (doc structurée pour LLM) —
  https://github.com/datagouv/datagouv-skill
- MCP tiers (ex. recherche d'entreprises). (Consultés 2026-06-20.)

## 6. Faisabilité & fiabilité technique
Piège majeur : **mélanger RAG et chiffres**. data.gouv.fr le dit pour son propre
MCP : réponses « approximatives ou erronées », « en aucun cas une source
officielle ». Impose RAG(sens)/SQL(chiffres) strict.

## 11. Verdict & décision
🔁 **À retravailler.** Bonne **vision**, mauvais **point de départ** : trop large,
et l'acteur officiel occupe déjà le terrain « brancher un LLM sur data.gouv.fr ».
La valeur n'est pas la connexion (déjà faite) mais la **fiabilité vérifiable**.
À reprendre comme couche transverse au-dessus d'un vertical (ex. 0001), pas comme
produit généraliste de premier MVP.
