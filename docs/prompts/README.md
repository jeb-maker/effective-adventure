# Prompts d'analyse des idées

Prompts réutilisables pour traiter une **hypothèse produit B2B/B2G** de façon
**reproductible**, en appliquant la méthode définie dans
[`../methode-analyse.md`](../methode-analyse.md).

> **Objectif du dépôt** : filtrer avant de construire. Partir du payeur et de la
> douleur, pas d'un dataset. Voir §0 de `methode-analyse.md`.

> Principe : ces prompts **ne redéfinissent pas** le barème ni les règles. Ils
> renvoient à `methode-analyse.md` et `modele-idee.md`, qui restent la **source
> unique de vérité**. Si la méthode change, on ne touche pas aux prompts.

## Quel prompt utiliser quand

| Étape | Prompt | Quand |
|---|---|---|
| 1. Capture | [`00-capture-idee.md`](00-capture-idee.md) | une idée brute (1–3 phrases) à structurer |
| 2. Existant | [`01-recherche-existant.md`](01-recherche-existant.md) | vérifier concurrence/existant avec sources |
| 3. Analyse | [`02-analyse-rigoureuse.md`](02-analyse-rigoureuse.md) | analyse complète + scoring + verdict |
| 4. Revue | [`03-revue-critique.md`](03-revue-critique.md) | challenger une analyse déjà rédigée |

## Enchaînement recommandé

```text
idée brute
   │
   ▼  00-capture-idee        → fiche sections 1–3 (statut 💡)
   │
   ▼  01-recherche-existant  → section 4 sourcée et datée
   │
   ▼  02-analyse-rigoureuse  → fiche complète + scoring + verdict (statut 🔍→décision)
   │
   ▼  03-revue-critique      → rapport de revue (OBLIGATOIRE), score ajusté si besoin
   │
   ▼  mise à jour du registre dans /README.md
   │
   ▼  si ✅ Go → statut 🚧 Prototype (sortie attendue)
```

## Règles communes à tous les prompts

- **Sourcer** : toute affirmation sur l'existant = lien + date de consultation.
  Toute donnée chiffrée = source. Pas de source → marquer « non vérifié ».
- **Cartographie** : §4 = cartographie B complète (cf. `cartographie-existant.md`) ;
  catalogue SaaS = cartographie A seulement.
- **Revue** : statut final (🔁❌✅🚧) interdit sans `revue.md` — contrôle :
  `python3 scripts/check_idees.py --strict`.
- **Anti-hallucination** : ne jamais inventer un chiffre, un concurrent, une URL.
  En cas de doute, écrire « à vérifier » plutôt que de combler.
- **Format** : produire du Markdown conforme à `docs/modele-idee.md`.
