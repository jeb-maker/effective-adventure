# Revue critique (red team) — 0001 Radar de la commande publique

- **Fiche auditée** : `idees/0001-radar-commande-publique/README.md`
- **Score affiché par la fiche** : 76 / 100 — Verdict affiché : ✅ Go
- **Date de la revue / consultation des sources** : 2026-06-20
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : l'idée repose sur une donnée réelle et une archi
> saine, mais sa **thèse centrale est factuellement fausse** — le créneau
> « analyse d'attribution » présenté comme quasi vierge est déjà occupé par
> plusieurs produits self-service commerciaux. Les notes C4/C5/C8/C9 et le
> verdict Go en découlent et doivent être révisés.

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « aucun acteur n'en a fait un produit self-service récurrent » | §5 Différenciation | **Faux** et non sourcé. Contredit par les preuves §4 de cette revue (Maître AO, Nextend.ai…). | **À supprimer / corriger** |
| A2 | « Analyse d'attribution (DECP) = peu mûr en produit » (ne cite que `decp.info` et `OpenMarchés`) | §4 Existant | Échantillon de concurrents **tronqué** : ignore les produits commerciaux directs. Conclusion biaisée par omission. | **À corriger (compléter)** |
| A3 | « Le seul morceau non saturé du marché des marchés publics est l'analyse d'attribution » | §11 Verdict | Affirmation décisive, non sourcée et **démentie**. C'est le pivot du Go. | **À supprimer / corriger** |
| A4 | « PME/ETI : payent déjà pour de la veille (30–100 €/mois) » | §2 Cible | Fourchette partiellement étayée plus bas (PublikConnect 49 €, AlertOffres 29,99 €) mais le « 30–100 » et surtout le fait qu'elles paieraient **en plus** pour de l'attribution n'est pas démontré. | **À sourcer / nuancer** |
| A5 | « Cette intelligence existe dans les données mais reste difficile à exploiter » | §1 Problème | Plausible mais asséné sans preuve, et désormais discutable (des outils l'exploitent déjà sans code). | **À nuancer** |
| A6 | « Risque d'hallucination faible par construction » | §6 | Conclusion correcte sur l'archi, mais formulée comme un absolu. Voir §3. | **À nuancer** |

**À mettre au crédit de la fiche** : la section §4 source correctement les prix
de la veille (liens datés vers `publikconnect.fr/tarifs`, `alertoffres.fr/tarifs`,
comparatifs olra/remporte) et les sources de données §3 sont bien renseignées
(URL, licence, format, fraîcheur, limites). Le problème n'est pas le sourcing
des prix de veille — c'est le **sourcing absent là où ça compte** : le créneau
attribution.

---

## 2. Sur-optimisme : notes de scoring trop généreuses

### C4 — Espace concurrentiel libre : **3 → 2** (poids ×2)
La fiche traite la veille comme « saturée » mais le créneau attribution comme
quasi libre (« peu mûr en produit »). **C'est faux.** Plusieurs produits
self-service vendent déjà exactement l'analyse d'attribution DECP (voir §4).
Le créneau n'est pas vierge : il se remplit activement (réutilisations DECP
datées de mars 2026, pages produit « Nouveau » chez Maître AO). Note 2 (occupé,
en cours de consolidation), pas 3.

### C5 — Différenciation défendable : **3 → 2** (poids ×2)
Les **trois** différenciateurs revendiqués existent déjà chez des concurrents :
- « fiche acheteur / fiche entreprise (SIREN) » → **Nextend.ai Observatoire**
  (13 974 profils acheteurs, 96 155 fournisseurs).
- « qui a gagné quoi, où, à quel prix » → **Maître AO « Mes Marchés &
  Concurrents »** (82 000+ titulaires, 700 000+ attributions) et
  **marchespublics.ai** (benchmark prix sur 10 M+ contrats).
- « alerte contrats arrivant à échéance » (présentée comme le signal-clé) →
  **déjà chez Maître AO** (« quels marchés arrivent à renouvellement »,
  prédictions de renouvellement) et marchespublics.ai (« suivi des
  renouvellements »).
- « détection d'anomalies / avenants massifs » → **déjà fait par OpenMarchés**
  (que la fiche cite elle-même). Donc cité comme différenciateur ET comme preuve
  qu'un autre l'a déjà fait : contradiction interne.

Différenciation « copiable » mais surtout **déjà copiée**. Note 2.

### C2 — Cible solvable (qui paie) : **4 → 3** (poids ×3)
Point d'attention demandé par le prompt. Deux failles :
1. La fiche se positionne en **complément** d'une veille que le client paie
   déjà → c'est une **dépense additionnelle**, la plus dure à arracher en B2B PME.
2. Les concurrents **intègrent l'intelligence d'attribution dans leur abonnement
   veille existant** (Maître AO : DECP incluse dans Starter 39 € / Pro 79 €,
   pas en option payante). Le consentement à payer pour un outil *autonome*
   d'attribution tend donc vers **zéro** (feature bundlée/commoditisée).
   Budget existant ≠ budget *additionnel*. Note 3.

### C8 — Maîtrise des risques : **3 → 2** (poids ×2)
La parade affichée (« rester sur l'angle attribution, pas la veille ») **ne tient
plus** : l'angle attribution est lui-même occupé par des acteurs financés qui
arrivent depuis la veille (intégration verticale). Le risque concurrentiel
principal est donc **mal identifié et non maîtrisé**. Ajouter le risque de
commoditisation (cf. C2). Note 2.

### C9 — Monétisation / impact : **4 → 3** (poids ×2)
Conséquence directe de C2/C8 : si la feature devient un inclus gratuit des
suites de veille, le SaaS B2B autonome à 30–100 €/mois est fragile. Le tier
gratuit transparence/journalisme génère de l'usage mais pas de revenu. Note 3.

### Notes laissées globalement inchangées (défendables)
- **C1 Intensité du problème = 4** : douleur réelle et récurrente pour les PME
  répondant aux AO. OK.
- **C3 Données = 4** : DECP consolidées open, ~quotidiennes, schéma documenté
  (`uid`, `modification_id`, `donneesActuelles`) — solide. *Réserve* (voir §3) :
  le `montant` DECP est celui **à la notification / le maximum d'accord-cadre**,
  pas la dépense réelle ; « parts de marché » et « à quel prix » peuvent être
  biaisés. Reste 4 mais la fiche sur-vend « propre donc SQL fiable ».
- **C6 Faisabilité & fiabilité = 5** : archi DuckDB + RAG(sens)/SQL(chiffres)
  conforme §3 de la méthode. Défendable (voir nuance §3).
- **C7 Facilité du MVP = 4** : périmètre crédible ; la normalisation
  titulaires/avenants/`uid` est non triviale mais réaliste. OK.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- **Architecture conforme** : chiffres via SQL DuckDB sur DECP, LLM cantonné à
  l'explication (libellés CPV, procédures). Conforme au §3 de la méthode. Le
  risque d'hallucination « numérique » est effectivement **faible par
  construction** — c'est un vrai point fort, à conserver.
- **Mais le vrai risque de fiabilité n'est pas l'hallucination LLM : c'est la
  sémantique de la donnée.** Le `montant` DECP = montant **à la notification**
  (avant avenants) et, pour les marchés à bons de commande, le **maximum de
  l'accord-cadre**, pas la consommation réelle. Un chiffre « SQL traçable » peut
  donc être **exact et trompeur** (« part de marché », « à quel prix »). La fiche
  affirme « données tabulaires propres, donc SQL fiable » — c'est un raccourci.
  SQL fiable ≠ indicateur métier fiable.
- **Chiffre repris dans la fiche** : « +239 900 % d'avenant » (cf. OpenMarchés).
  **Vérifié et exact** (data.gouv.fr, réutilisation OpenMarchés, MàJ 2026-03-21).
  Bon réflexe de citation — mais il sert d'argument de différenciation alors
  qu'il **prouve qu'un tiers détecte déjà ces anomalies**.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire non mentionnés)

### Concurrents directs OMIS (le plus grave)
Tous consultés le 2026-06-20 :

- **Maître AO — « Mes Marchés & Concurrents »** (Lumina Systèmes) :
  https://www.maitre-ao.fr/fr/intelligence-marche et
  https://www.maitre-ao.fr/fr/guide/intelligence-marche-decp — self-service,
  DECP + SIRENE, « qui gagne quoi, à quel prix », fiche concurrent, prix de
  référence, acheteurs cibles, **prédictions de renouvellement / échéances**,
  82 000+ titulaires, 700 000+ attributions. Tarifs 39 € / 79 € / 199 €/mois
  (https://www.maitre-ao.fr/fr/a-propos). **C'est le produit décrit par la fiche.**
- **Nextend.ai — Observatoire de la commande publique** :
  https://nextend.ai/observatoire — DECP + BOAMP, MàJ quotidienne, 13 974
  profils acheteurs, 96 155 fournisseurs, fiches acheteur/fournisseur. =
  exactement les « 3 écrans » du MVP (§9).
- **marchespublics.ai** : https://marchespublics.ai/ — DECP « contrats
  attribués : qui a gagné quoi, à quel prix », benchmark prix sur 10 M+ contrats,
  suivi des renouvellements.
- **attribution-intelligence.fr** : https://attribution-intelligence.fr/ —
  rapports sectoriels d'attribution (BTP + IT), 13 306 avis analysés.
- **olra.fr** (cité comme veille) bascule aussi vers l'analyse d'attribution
  DECP : https://olra.fr/blog/decp-donnees-essentielles-analyser-concurrents
  (croise DECP/CPV pour estimer concurrents probables et fourchette de prix).

→ Conclusion : la fiche n'a pas « manqué un » concurrent, elle a **manqué tout
le segment** qu'elle prétend défricher. La veille et l'attribution **convergent**
(les acteurs de veille internalisent l'attribution).

### Risques non mentionnés
- **Commoditisation / bundling** : l'attribution devient une feature *incluse*
  des suites veille → pression prix vers 0 pour un produit autonome.
- **Sémantique des montants** (cf. §3) : risque de produire des classements
  faux-vrais (part de marché basée sur des maxima d'accords-cadres).
- **Couverture / fraîcheur réelle** : seuil de déclaration DECP maintenu à
  40 000 € HT (le relèvement à 60 000 € du seuil de *dispense* au 01/04/2026 est
  sans effet sur la déclaration — source DAJ/Weka 2026), mais les MAPA <
  seuil restent absents ; surtout, **délais de publication pouvant atteindre
  plusieurs années** (Nextend.ai le documente) → les alertes « contrats à
  échéance » et les stats récentes sont **structurellement incomplètes**. Le
  signal-clé (échéances) repose sur `dateNotification` + `dureeMois`, champs
  souvent absents/approximatifs et inopérants pour les accords-cadres.
- **Réputation / juridique** : nommer des entreprises sur « attributions sans
  concurrence » / « anomalies » expose à un risque réputationnel/diffamation si
  l'anomalie est en réalité une erreur de saisie (fréquentes dans les DECP).
- **Coûts d'exploitation non chiffrés** : ingestion quotidienne (~1,8 Go JSON /
  Parquet), enrichissement SIRENE mensuel, hébergement — modeste, mais ARPU
  faible + CAC B2B PME = unit economics à démontrer.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 4 | 12 |
| C2 | Cible solvable (qui paie) | ×3 | 4 | **3** | 9 |
| C3 | Disponibilité & fiabilité données | ×3 | 4 | 4 | 12 |
| C4 | Espace concurrentiel libre | ×2 | 3 | **2** | 4 |
| C5 | Différenciation défendable | ×2 | 3 | **2** | 4 |
| C6 | Faisabilité & fiabilité technique | ×2 | 5 | 5 | 10 |
| C7 | Facilité du MVP | ×2 | 4 | 4 | 8 |
| C8 | Maîtrise des risques | ×2 | 3 | **2** | 4 |
| C9 | Monétisation / impact | ×2 | 4 | **3** | 6 |
| | **Total** | | **80** | | **69 / 105** |

**Score /100** : 69 / 105 × 100 = **65,7 → 66 / 100**.

**Changement de verdict : OUI.**
- Fiche : 76/100 → seuil ≥ 70 → ✅ Go.
- Revue : 66/100 → seuil 55–69 → 🔁 **À retravailler**.

L'idée n'est pas à écarter (≥ 55, donnée et archi réelles), mais le **Go n'est
pas justifié** en l'état : il repose sur une hypothèse concurrentielle erronée.

---

## 6. Verdict de revue

### **À CORRIGER** (proche de « à refaire » sur les sections 4–5–11)

La donnée, l'architecture (RAG/SQL conforme) et l'intensité du problème sont
solides et bien traités. Mais la **thèse centrale** (créneau attribution quasi
vierge, seul segment non saturé) est **factuellement infirmée**, ce qui invalide
les sections Existant, Différenciation, plusieurs notes de scoring et le verdict
Go. Ce n'est pas un détail à la marge : c'est le pilier de la décision. Si la
réécriture de ces sections ne fait pas émerger un différenciateur réel et
défendable, l'idée passe de « à corriger » à « à refaire / écarter ».

### 3 actions prioritaires
1. **Refaire la section 4 (Existant) honnêtement** : intégrer Maître AO, Nextend.ai,
   marchespublics.ai, attribution-intelligence.fr, olra (liens datés 2026-06-20)
   et reconnaître la convergence veille↔attribution. Supprimer A1/A3.
2. **Trouver / prouver un différenciateur encore libre** (sinon, pas de Go) :
   ex. profondeur d'analyse anomalies/avenants avec garde-fous juridiques,
   verticalisation sectorielle, ou angle transparence/data-journalisme — et le
   confronter à ce que font déjà les concurrents. Re-noter C4/C5/C8 en
   conséquence.
3. **Corriger la promesse « chiffres fiables »** : documenter explicitement la
   sémantique du `montant` DECP (notification / max accord-cadre ≠ dépense),
   les délais de publication et les trous de couverture ; afficher un taux de
   couverture par requête (déjà esquissé §9, à ériger en garde-fou produit).

---

REVUE 0001 | à corriger | score recalculé 66/100 (vs 76) | changement de décision: oui
