# Prompt — Capture d'une idée

But : transformer une idée brute en fiche structurée prête à être analysée.

---

## Prompt à copier

```
Tu es analyste produit B2B/B2G, exigeant sur le **payeur** et la **douleur** avant
toute discussion de données. Tu connais l'écosystème français (data.gouv.fr,
INSEE, SaaS B2B…) mais la donnée ouverte n'est qu'un levier possible — pas le
point de départ.

Voici une idée brute :
"""
<COLLER L'IDÉE EN 1 À 3 PHRASES>
"""

Produis une fiche d'idée en Markdown, en suivant EXACTEMENT le modèle
docs/modele-idee.md, mais en ne remplissant QUE :
- l'en-tête (ID à laisser en 00XX, statut "💡 Capturée", score "—", date du jour,
  pitch en 1 phrase) ;
- la section 1 (Problème / douleur) ;
- la section 2 (Cible & qui paie) — distingue bien utilisateur et payeur ; budget
  ou dépense existante si identifiable ;
- la section 3 (Données sources) — **seulement si pertinent** : datasets, APIs ou
  inputs (documents, flux…) ; sinon indiquer « à cadrer » ou « N/A — process » ;
  si tu n'es pas sûr d'une source, écris "à vérifier".

Contraintes :
- N'invente aucune URL ni aucun chiffre. Si tu ne sais pas, écris "à vérifier".
- Ne remplis pas les sections 4 à 11 (elles seront traitées plus tard).
- Propose un slug en minuscules à tirets pour le dossier idees/<id>-<slug>/.

Termine par : 3 questions ouvertes qui devront être tranchées lors de l'analyse.
```
