# Revue critique (red team) — 0015 Observatoire des déserts de mobilité

- **Fiche auditée** : `idees/0015-deserts-de-mobilite/README.md`
- **Score affiché par la fiche** : 54 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : le verdict **❌ Écartée est juste et bien argumenté**
> (paradoxe de couverture + concurrent public gratuit). La revue le **conforte et
> l'enfonce** : l'écosystème public est encore plus dense que décrit (Cerema gère
> aussi un **observatoire des politiques locales de mobilité** et un **observatoire
> des plans de mobilité**), et les notes C2/C9 restent légèrement complaisantes.
> Recalcul adversarial : **50/100** — toujours ❌ Écartée, marge confortée.

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « ~76 % de la population, ~350 territoires sur 1 156 » (couverture GTFS) | §3 | Chiffre **décisif** (il fonde le « paradoxe de couverture ») attribué à transport.data.gouv.fr sans lien profond daté ni capture. À tracer précisément. | **À sourcer** (URL + date + page exacte du PAN) |
| A2 | « Isocarto, Smappen… prix non détaillés → à vérifier » | §4 | Honnête (l'auto-réserve est notée), mais aucune comparaison tarifaire ne peut être tirée tant que non sourcée. | **À sourcer avant comparaison** |
| A3 | « aucun observatoire des déserts de mobilité identifié comme produit dominant » sur le PAN | §4 | Recevable comme constat, mais incomplet : l'absence d'un *produit dominant nommé* ≠ absence de couverture publique (cf. §4 ci-dessous, Cerema). | **À compléter** |

**À mettre au crédit de la fiche** : le §4 identifie déjà **Cerema Networks/Musliw,
Capamob, Cerema isochrones gares, Observatoire des territoires (ANCT), INSEE**, et
le §8 nomme correctement le **paradoxe de la donnée** comme point quasi
éliminatoire. Le sourcing données (§3) est rigoureux (licences mixtes LO/ODbL,
formats, limites). C'est une fiche **honnête** ; la revue ne corrige qu'à la marge.

---

## 2. Sur-optimisme : notes de scoring trop généreuses

### C2 — Cible solvable (qui paie) : **3 → 2** (poids ×3)
La fiche décrit pourtant un payeur **structurellement difficile** : budget mobilité
public **mais** achat par **marché public** (cycle long), culture du « faire faire »
par bureau d'études, **pas d'acheteur récurrent en self-service**, et une
**alternative gratuite officielle** (Cerema). Ce faisceau correspond à l'ancrage 2
(« peu de payeurs, budget capté/indirect »), pas 3. Le 3 surévalue l'existence d'un
budget que personne ne dépensera en abonnement SaaS.

### C9 — Monétisation / impact : **3 → 2** (poids ×2)
La fiche s'appuie sur « c'est l'impact, pas le revenu, qui sauve la note ». Or
l'impact est **déjà capté** par les dispositifs publics — et davantage que la fiche
ne le dit : le Cerema diffuse depuis 2023 un **observatoire des politiques locales
de mobilité** (avec DGITM, Intercommunalités de France, Gart) et depuis 2022 un
**observatoire des plans de mobilité** permettant de **comparer des collectivités au
profil proche** (voir §4). L'impact marginal d'un énième observatoire est faible →
ancrage 2.

### Notes laissées inchangées (défendables)
- **C1 = 3**, **C3 = 3** : justes (problème réel mais diagnostic épisodique ;
  données ouvertes mais couverture GTFS partielle, la plus faible là où ça compte).
- **C4 = 2** : défendable. On pourrait plaider 1 (cœur saturé par Cerema + ANCT +
  INSEE + géomarketing + nouveaux observatoires Cerema), mais un mince résidu de
  *packaging* « observatoire national clé en main » subsiste → 2 maintenu, **avec
  réserve** (voir §4).
- **C5 = 2**, **C6 = 4**, **C7 = 2**, **C8 = 2** : correctement notées ; le C7=2
  (chantier d'assemblage GTFS + routing national) et le C8=2 (paradoxe + concurrent
  public) sont particulièrement bien vus.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- **Architecture conforme** : nb de départs/jour, temps d'accès, population
  desservie sous X min sortent de **routing déterministe / SQL** ; LLM borné aux
  définitions et synthèses de zone. Risque d'hallucination faible par construction.
- **Le vrai risque est le « faux-vrai » de couverture** : afficher « 0 desserte »
  ou « désert » là où c'est en réalité un **trou de données GTFS** (rural, TAD non
  modélisé) produit un chiffre traçable mais **trompeur** — exactement le danger
  que la méthode veut éviter. La fiche l'a identifié (§8) et propose d'afficher le
  **taux de couverture** : bon réflexe, à ériger en garde-fou produit non
  négociable. Cela ne sauve pas l'idée mais évite l'erreur méthodologique.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire)

### L'écosystème public est **plus dense** que décrit (renforce C4/C9)
Tous consultés le 2026-06-23 :
- **Cerema — Observatoire des politiques locales de mobilité** (depuis 2023, via
  **France Mobilités**, animé avec DGITM, Intercommunalités de France, Gart) :
  diffusion libre d'une connaissance sur l'organisation des mobilités, **base AOM
  mise à jour chaque année** (composition, bassins de mobilité, contrats
  opérationnels, versement mobilité URSSAF depuis 2024), travail de fiabilisation
  des données d'offre avec le PAN. —
  https://www.cerema.fr/fr/actualites/dossier-bases-donnees-autorites-organisatrices-mobilite
- **Cerema — Observatoire des plans de mobilité** (depuis juin 2022) : recense les
  PDM des agglomérations, leurs caractéristiques d'offre et **permet de comparer
  les plans de collectivités au profil proche** — exactement la fonction
  « comparaisons inter-territoires » revendiquée comme différenciateur §5. —
  même source.
- **Cerema — extension QGIS « Networks »/Musliw** : confirmée comme **outil libre**
  diffusé aux collectivités/bureaux d'études/agences/associations, avec
  **formations 2026** (Lille, 17-19 mars et 13-15 octobre) couvrant cartes
  d'accessibilité multimodale, cartes d'offre (passages/circulations) et
  **croisement avec données socio-économiques**. — 
  https://www.cerema.fr/fr/activites/services/formation-analyser-cartographier-offre-transport-multimodale

→ Le « packaging national clé en main » censé être le résidu libre (§4/§5) est
**déjà adressé** côté comparaison inter-territoires (observatoire PDM) et côté
diagnostic d'accessibilité (Networks + formations actives en 2026). Le C4=2 est un
**plafond** : il n'y a pas de marché self-service à conquérir face à un acteur
public qui **forme** la cible à faire elle-même l'analyse, gratuitement.

### Risques / coûts non (assez) soulignés
- **Maintenance du routing national** : la fiche le note (§6/§9), mais le coût
  récurrent de réassemblage des **GTFS fragmentés** (versions, calendriers,
  dédoublonnage) face à un ARPU public faible rend les unit economics intenables.
- **Concurrence par la gratuité ET la formation** : Cerema ne se contente pas de
  fournir l'outil, il **transfère la compétence** — ce qui assèche durablement la
  demande pour un SaaS payant.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | ×3 | 3 | **2** | 6 |
| C3 | Disponibilité & fiabilité données | ×3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 2 | 2 | 4 |
| C5 | Différenciation défendable | ×2 | 2 | 2 | 4 |
| C6 | Faisabilité & fiabilité technique | ×2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | ×2 | 2 | 2 | 4 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 3 | **2** | 4 |
| | **Total** | | **57** | | **52 / 105** |

**Score /100** : 52 / 105 × 100 = **50 / 100**.

**Changement de verdict : NON** (reste ❌ Écartée ; la marge sous le seuil de 55
**s'élargit** de 54 → 50). Le point quasi éliminatoire (paradoxe de couverture +
concurrent public gratuit **qui forme la cible**) est confirmé.

---

## 6. Verdict de revue

### **ANALYSE FIABLE** (légèrement complaisante sur C2/C9, sans effet sur la décision)

La fiche atteint la bonne conclusion (❌ Écartée) avec un bon argumentaire. La revue
ne change pas la décision mais (a) corrige deux notes optimistes (C2, C9), (b)
**renforce** le constat de saturation publique en documentant les observatoires
Cerema (politiques locales de mobilité, plans de mobilité) et les formations 2026,
qui couvrent jusqu'à la « comparaison inter-territoires » présentée comme
différenciateur. Score recalculé **50/100**.

### 3 actions prioritaires
1. **Maintenir ❌ Écartée** et mettre à jour le §4 avec les observatoires Cerema
   (PDM + politiques locales) — la cible est non seulement servie mais **formée**
   gratuitement à faire l'analyse elle-même.
2. **Tracer le chiffre de couverture GTFS** (76 % / 350 territoires) avec URL + date
   avant toute réutilisation de l'argument « paradoxe de couverture ».
3. **Réserver toute relance au seul angle non servi** : suivi **temporel** des
   dégradations d'offre (diff entre versions GTFS) comme système d'alerte AOM — et
   seulement si un payeur récurrent nommé est confirmé (sinon, ne pas rouvrir).

---

REVUE 0015 | analyse fiable | score recalculé 50/100 (vs 54) | changement de décision: non
