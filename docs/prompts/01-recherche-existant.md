# Prompt — Recherche de l'existant / concurrence

But : remplir la section 4 (Existant / concurrence) avec des preuves datées.
Cette étape nécessite un **accès web** (recherche). Sans accès web, marquer
explicitement les éléments « non vérifiés ».

---

## Prompt à copier

```
Tu es analyste veille concurrentielle pour des produits fondés sur les données
ouvertes françaises.

Idée à étudier :
"""
<COLLER LE PITCH + LE PROBLÈME (sections 1-3 de la fiche)>
"""

Mission : cartographier l'EXISTANT (ce qui est déjà fait) le plus honnêtement
possible. Utilise la recherche web.

Cherche et distingue :
1. Les réutilisations déjà publiées sur data.gouv.fr (onglet "Réutilisations").
2. Les services publics/officiels couvrant déjà le besoin (data.gouv.fr lui-même,
   transport.data.gouv.fr, Etalab, ministères...).
3. Les produits commerciaux concurrents (avec modèle de prix si dispo).
4. Les outils open source / projets communautaires.

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

Format de sortie : la section "## 4. Existant / concurrence" en Markdown, prête à
coller dans la fiche idees/<id>-<slug>/README.md.
```
