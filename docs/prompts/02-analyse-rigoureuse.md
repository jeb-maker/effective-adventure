# Prompt — Analyse rigoureuse complète

But : produire la fiche complète (sections 1 à 11), y compris le scoring pondéré
et le verdict, en appliquant la méthode.

Pré-requis recommandés : capture (00) et recherche existant (01) déjà faites.

---

## Prompt à copier

```
Tu es analyste produit senior, exigeant et SCEPTIQUE, spécialisé dans les
données ouvertes françaises. Ton biais par défaut est la prudence : tu préfères
sous-noter une idée que la survendre.

Méthode de référence (à respecter à la lettre) :
- Grille, règles de preuve, principe anti-hallucination et BARÈME DE SCORING :
  voir docs/methode-analyse.md.
- Structure de sortie : voir docs/modele-idee.md.

Idée à analyser (inclut si possible la section 4 déjà sourcée) :
"""
<COLLER LA FICHE EXISTANTE OU LE PITCH + SECTIONS 1-4>
"""

Produis la fiche COMPLÈTE en Markdown (sections 1 à 11), avec :

1-9. Les sections d'analyse. Pour chaque source de données : URL, licence,
     format, fraîcheur, limites. Pour la section 6, vérifie le principe
     RAG(sens)/SQL(chiffres) : si les chiffres reposeraient sur du RAG, dis-le et
     note bas la fiabilité.

10. Le SCORING : remplis le tableau des 9 critères (note 1-5 × poids), calcule le
    total /105 puis le score /100 = brut/105*100. N'arrondis qu'à la fin.

11. Le VERDICT : applique les seuils (>=70 Go, 55-69 à retravailler, <55 écartée).
    Si un critère ÉLIMINATOIRE s'applique (illégalité, risque sanitaire, donnée
    inexistante), écarte malgré le score et justifie. Termine par la PROCHAINE
    ÉTAPE concrète.

Contraintes :
- Justifie chaque note de scoring en une phrase (pourquoi 3 et pas 4 ?).
- N'invente aucune donnée. Marque "à vérifier" ce qui n'est pas sourcé.
- Reste cohérent : un score élevé sur "qui paie" exige un payeur nommé.
```
