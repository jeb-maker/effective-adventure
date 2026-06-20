# Copilote d'études territoriales (RAG sur données publiques)

- **ID** : 0003
- **Statut** : 🔁 À retravailler
- **Score** : — / 100 (analyse partielle)
- **Dernière mise à jour** : 2026-06-20
- **Pitch (1 phrase)** : Un assistant qui transforme les données publiques en
  rapports fiables et cités sur un territoire (comparer des communes, expliquer
  des finances locales, etc.).

---

## 1. Problème / douleur
Explorer data.gouv.fr est lent pour un non-spécialiste. Un assistant qui
sélectionne les bons datasets, calcule juste et cite ses sources ferait gagner
beaucoup de temps.

## 3. Données sources (pistes)
INSEE commune/IRIS, SIRENE, DVF, finances locales, transport.data.gouv.fr,
risques naturels, qualité air/eau — multi-domaines.

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
