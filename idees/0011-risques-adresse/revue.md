# Revue critique (red team) — 0011 Diagnostic des risques par adresse

- **Fiche auditée** : `idees/0011-risques-adresse/README.md`
- **Score affiché par la fiche** : 60 / 100 — Verdict affiché : 🔁 À retravailler
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : l'analyse est **honnête et bien sourcée** sur la
> saturation (C4=1, C5=1 mérités), mais elle **survit artificiellement au-dessus
> du seuil d'écart** grâce à des notes complaisantes sur C2, C3 et C8. Recalcul
> adversarial : **52/100**, soit **❌ Écartée** — ce que le verdict rédactionnel
> reconnaît déjà à demi-mot (« de fait quasi écartée en l'état »).

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « payent déjà pour des outils de génération de rapport Géorisques (ex. Notiplus, Risqeo à 24,90 €) » | §2 | Le prix Risqeo est sourcé (lien §4), mais l'affirmation que les notaires/diagnostiqueurs **achètent** ces outils, et donc qu'il existe un budget *additionnel* captable, n'est pas démontrée (pas de volume, pas de part de marché). | **À nuancer** |
| A2 | « Apify le vend à 0,005 $/adresse » (preuve que la couche est « reproductible en un week-end ») | §5 | Le tarif Apify est plausible et sourcé, mais « reproductible en un week-end » reste un **jugement** asséné. Il sert ici **à charge** (ça renforce la thèse de saturation), donc moins gênant, mais reste une opinion. | **À conserver (à charge) mais reformuler** |
| A3 | « ~30 % de couverture » des ERP pour les risques | n/a (ce point concerne 0016) | — | — |
| A4 | « le grand public ne paiera pas » | §7 | Plausible et cohérent avec le gratuit officiel, mais asséné sans donnée de disposition à payer. | **À nuancer** (suffisant pour conclure, pas pour chiffrer) |

**À mettre au crédit de la fiche** : le §4 est **exemplaire** sur le sourcing
concurrentiel (Errial, Fonciris, ClimaScore, risques-adresse.fr, Callendar,
Risqeo, Notiplus, ATerraData, Apify — tous liens datés 2026-06-20), et le §3 est
rigoureux (URL, licence LO 2.0, format, fraîcheur, limites par source). Le
problème de la fiche n'est **pas** le sourcing : c'est l'**indulgence du
scoring** sur les critères « qui paie » et « données ».

---

## 2. Sur-optimisme : notes de scoring trop généreuses

### C2 — Cible solvable (qui paie) : **3 → 2** (poids ×3)
Point d'attention prioritaire du prompt. La fiche concède elle-même que (a) les
particuliers ne paieront pas (gratuit officiel + risques-adresse.fr/ClimaScore),
(b) les notaires/diagnostiqueurs **sont déjà équipés** (Notiplus/Risqeo), (c) les
assureurs/banques consomment l'API ou des modèles propres (Callendar). Aucun
payeur **non servi** n'est identifié, et la matière première est gratuite. C'est
l'ancrage 2 (« peu de payeurs, budget déjà capté »), pas 3. La note 3 surévalue
un budget *existant* qu'on confond avec un budget *additionnel* arrachable.

### C3 — Disponibilité & fiabilité des données : **5 → 4** (poids ×3)
La fiche en fait son point d'honneur (« il serait malhonnête de le sous-noter »).
La donnée est effectivement ouverte, propre et traçable — mais un 5 (« inputs
prêts, propres, traçables » **sans réserve**) est trop généreux au regard des
limites que la fiche **liste elle-même au §3** :
- **Maille communale** (et non parcellaire) pour radon, sismicité, plusieurs
  volets GASPAR → le produit « à l'adresse » repose en partie sur une donnée qui
  n'est pas à l'adresse ;
- **buffers indicatifs** (SSP ~200 m, ICPE dans un rayon) à pertinence locale
  variable ;
- **dépendance à une API publique unique** avec **authentification token
  Cerbère (valable 1 an)** et maille variable — fragilité opérationnelle réelle.
« Prêtes et traçables » ≠ « sans réserve de fiabilité métier à la parcelle ».
Note 4 (solide mais pas parfaite).

### C8 — Maîtrise des risques : **3 → 2** (poids ×2)
La fiche identifie pourtant correctement le risque #1 : « concurrence écrasante
(public gratuit + privés établis), structurel ». Or elle note 3 (« risques
gérables par disclaimers »). C'est contradictoire : le risque dominant n'est
**pas** juridique (gérable par disclaimer) mais **concurrentiel/commoditisation**,
et il n'est **pas maîtrisé** — il est *subi*. À cela s'ajoute la dépendance API
(token, schéma, quotas) que la fiche range elle-même en risque. Ancrage 2
(« risques majeurs non maîtrisés »).

### Notes laissées inchangées (défendables)
- **C1 = 3** : besoin réel (achat immo, RGA en hausse, > 3,5 Md€ de dommages
  2022) mais déjà servi gratuitement par Errial → ni gadget, ni douleur non
  couverte. OK.
- **C4 = 1** et **C5 = 1** : **mérités, et confirmés à charge** (voir §4). Cas
  d'école de saturation, positionnement pris jusque dans le nom
  (risques-adresse.fr).
- **C6 = 4** : archi BAN → API Géorisques, chiffres structurels renvoyés par
  l'API (non hallucinés), LLM borné au sens. Conforme. OK.
- **C7 = 4** : MVP rapide — mais cette facilité profite surtout aux concurrents
  (argument déjà bien posé par la fiche). OK.
- **C9 = 2** : monétisation comprimée entre gratuit officiel et concurrents
  < 25 € + API à 0,005 $/adresse. OK.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- **Architecture conforme** : les classements/valeurs (zone sismique 1-5, classe
  radon 1-3, nombre d'ICPE, arrêtés CatNat) sont des **valeurs structurées
  renvoyées par l'API Géorisques**, pas des nombres produits par un LLM. Le
  risque d'hallucination « numérique » est effectivement **faible par
  construction** — point fort réel.
- **Le vrai risque de fiabilité n'est pas l'hallucination, c'est la maille.**
  Présenter un résultat « à l'adresse » alors que radon/sismicité/plusieurs
  volets sont à la **maille communale**, et que SSP/ICPE reposent sur des
  **buffers**, peut produire un affichage **exact mais faussement précis** (« ce
  bien est… » alors que la donnée vaut pour la commune). C'est exactement le type
  d'« exact mais trompeur » que la méthode veut éviter, et qui justifie le C3 à 4.
- **Valeur opposable** : l'État rappelle que seul l'**Errial/ERP signé** fait foi
  (préfecture Seine-Maritime, consulté 2026-06-23 :
  https://www.seine-maritime.gouv.fr/.../Etat-des-risques-et-pollutions). Tout
  produit privé doit donc s'afficher « informatif, non opposable » — il vend du
  confort, pas de la valeur juridique.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire)

### Le concurrent public **se renforce** (aggrave C4)
Le §4 de la fiche est complet ; la revue ajoute une mise à jour **qui empire la
saturation** :
- **Errial (Géorisques) — mise à jour de janvier 2026** : la plateforme officielle
  a intégré de **nouvelles couches de données** (notamment le **recul du trait de
  côte**), interrogation par adresse **ou parcelle**, fiche PDF téléchargeable.
  Consulté 2026-06-23 :
  https://www.georisques.gouv.fr/information-des-acquereurs-et-locataires et
  https://www.data.gouv.fr/pages/onboarding/errial (l'API officielle est
  rappelée comme livrable du service). → Le service public **gratuit** non
  seulement existe, mais **élargit son périmètre** et **réduit** le résidu
  exploitable. Toute couche « différenciante » d'un privé (nouveaux risques,
  carto parcelle) est rattrapée par l'État.
- **ERNMT-Officiel** : propose en plus un état des risques/pollutions **gratuit**
  en ligne — un acteur privé de plus sur le créneau « ERP gratuit ». Consulté
  2026-06-23 : https://www.ernmt-officiel.com/blog/article/Errial-nouveau-projet-du-gouvernement

### Risques non (ou mal) mentionnés
- **Commoditisation** (déjà bien vue en §8, mais sous-pondérée dans le scoring) :
  matière première gratuite + agrégateurs à 0,005 $/adresse → valeur captée → 0.
- **Faux sentiment de précision** : afficher « à l'adresse » des risques à maille
  communale engage une **responsabilité** si l'acheteur surinterprète.
- **Dépendance régalienne** : l'État pousse Errial comme **référence
  réglementaire unique** (mention obligatoire dans les annonces immobilières) ;
  un privé est structurellement **en aval** d'un monopole d'usage de fait.

### Coûts non chiffrés
Ingestion multi-endpoints, renouvellement annuel du token Cerbère, veille sur les
changements de schéma API, hébergement carto — modestes, mais à mettre face à un
ARPU quasi nul. Unit economics non démontrées.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | 3 | 9 |
| C2 | Cible solvable (qui paie) | ×3 | 3 | **2** | 6 |
| C3 | Disponibilité & fiabilité données | ×3 | 5 | **4** | 12 |
| C4 | Espace concurrentiel libre | ×2 | 1 | 1 | 2 |
| C5 | Différenciation défendable | ×2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | ×2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | ×2 | 4 | 4 | 8 |
| C8 | Maîtrise des risques | ×2 | 3 | **2** | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **63** | | **55 / 105** |

**Score /100** : 55 / 105 × 100 = **52 / 100**.

**Changement de verdict : OUI.**
- Fiche : 60/100 → bande 55–69 → 🔁 À retravailler.
- Revue : 52/100 → bande < 55 → ❌ **Écartée**.

Le basculement est cohérent avec le §11 de la fiche, qui qualifie déjà l'idée de
« de fait quasi écartée en l'état » : le score 60 ne tenait que par un C3=5
complaisant et un C8=3 contradictoire avec le texte.

---

## 6. Verdict de revue

### **À CORRIGER → confirme l'ÉCART**

L'analyse est **fiable sur le fond** (existant, données, architecture) et son
auto-diagnostic est lucide. Mais le score est **maintenu artificiellement** au-dessus
du seuil d'écart par trois notes trop indulgentes (C2, C3, C8) qui contredisent
le corps du texte. Une fois corrigées, l'idée tombe à 52/100 : **❌ Écartée**, sans
aucun critère sauveur. La donnée excellente (le seul vrai atout) est précisément
ce qui commoditise le produit.

### 3 actions prioritaires
1. **Basculer le statut en ❌ Écartée** (score 52) : aligner la décision sur le
   constat de saturation déjà écrit au §11.
2. **Ne pas confondre budget existant et budget additionnel** (C2) : si l'on
   réinstruit un jour, exiger un payeur **non servi** nommé avant toute relance.
3. **Réserver toute relance au seul angle marginal restant** : scoring climatique
   **prospectif** B2B portefeuille (assureurs/prêteurs) — et le confronter à
   Callendar **avant** d'écrire une nouvelle fiche, pas en sauvetage de celle-ci.

---

REVUE 0011 | à corriger | score recalculé 52/100 (vs 60) | changement de décision: oui
