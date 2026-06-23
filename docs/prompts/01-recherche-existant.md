# Prompt — Recherche de l'existant / concurrence

But : remplir la section 4 (Existant / concurrence) avec des preuves datées,
en couvrant **toute** la cartographie B — pas seulement le catalogue SaaS.

Méthode : [`docs/cartographie-existant.md`](../cartographie-existant.md) §2.

Cette étape nécessite un **accès web** (recherche). Sans accès web, marquer
explicitement les éléments « non vérifiés ».

---

## Prompt à copier

```
Tu es analyste veille concurrentielle pour des produits B2B/B2G.

Idée à étudier :
"""
<COLLER LE PITCH + LE PROBLÈME (sections 1-2 de la fiche)>
"""

Mission : cartographier l'EXISTANT (cartographie B) le plus honnêtement possible.
Utilise la recherche web. Consulte aussi les segments pertinents du catalogue SaaS
(catalogue-saas/) — mais ne t'y limite PAS.

Parcours OBLIGATOIRE (checklist docs/cartographie-existant.md §2) :

1. **Réutilisations data.gouv.fr** — onglet « Réutilisations » des jeux cités ;
   recherche sur data.gouv.fr/reuses.
2. **Services publics / .gouv.fr** — ministères, beta.gouv, observatoires officiels,
   outils gratuits couvrant déjà le besoin (souvent le concurrent n°1).
3. **Produits commerciaux** — FR/EU, avec modèle de prix si disponible ;
   croiser avec catalogue-saas/ si segment pertinent.
4. **Open source / académique** — GitHub, HAL, projets communautaires.
5. **Bricolage** — Zapier/Make, Excel, scripts internes, Notion.

Pour CHAQUE élément trouvé, donne :
- nom + URL + date de consultation ;
- ce qu'il fait précisément ;
- ses limites / ce qu'il ne fait pas.

Règles strictes :
- N'affirme rien sans lien. Une affirmation sans source = à supprimer ou marquer
  "(non vérifié)".
- N'invente jamais un concurrent ou une URL.
- Conclus par un verdict de saturation : "vierge / partiel / saturé", justifié,
  et indique précisément OÙ se trouve l'espace libre éventuel (le créneau non
  couvert).

Format de sortie : la section "## 4. Existant / concurrence" en Markdown avec
les sous-sections ### obligatoires (Services publics, Réutilisations data.gouv,
Produits commerciaux, Open source, Bricolage — omettre une sous-section vide
seulement si vraiment rien trouvé après recherche), prête à coller dans la fiche
idees/<id>-<slug>/README.md.
```
