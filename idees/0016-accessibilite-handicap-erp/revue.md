# Revue critique (red team) — 0016 Accessibilité handicap des lieux (ERP)

- **Fiche auditée** : `idees/0016-accessibilite-handicap-erp/README.md`
- **Score affiché par la fiche** : 52 / 100 — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : le verdict **❌ Écartée est juste** (redondance avec un
> service public + pas de payeur). La revue le **conforte** : acceslibre n'occupe
> pas seulement le grand public, il **investit aussi activement le segment
> collectivités** (obligation d'open data, moissonnage, passerelles SIG, webinaire
> juin 2026), ce qui referme le dernier créneau « pivot » envisagé. Notes C2 et C7
> restent un cran trop hautes → recalcul **48/100**, toujours ❌ Écartée.

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « de l'ordre de 30 % de couverture » (627 887 lieux / ~1,8 M ERP) | §3 | Calcul **dérivé** par l'analyste : numérateur sourcé (acceslibre), dénominateur (~1,8–2 M ERP) sourcé mais **approximatif**, ratio reconstruit. Honnête mais à présenter comme estimation, pas comme fait. | **À nuancer** (estimation) |
| A2 | « Jaccede : + de 100 000 lieux » vs « ~73 218 lieux » | §4 | La fiche **signale elle-même** la contradiction et le « à vérifier ». Correct, mais le chiffre ne doit pas servir d'argument tant que non tranché. | **À vérifier** (déjà signalé) |
| A3 | « Very Important Parking ~800 000 lieux annoncés » | §4 | Marqué « à vérifier » ; OK, mais à ne pas réutiliser tel quel. | **À vérifier** (déjà signalé) |
| A4 | « la conformité réglementaire n'est pas alimentée par les données acceslibre » | §2/§4 | Affirmation **structurante** (elle invalide le seul créneau payeur). Plausible (déclaratif ≠ diagnostic Ad'AP/registre), mais mériterait une source réglementaire explicite. | **À sourcer** (registre public d'accessibilité / Ad'AP) |

**À mettre au crédit de la fiche** : §3 et §4 sont **rigoureux** (API Swagger,
schéma CNIG, client OSS, dataset data.gouv MàJ quotidienne, sources datées
2026-06-20), et l'auto-discipline sur les chiffres incertains (« à vérifier ») est
exemplaire. Le défaut n'est pas le sourcing : c'est que **C2 et C7 restent un peu
indulgents**, et que la pression d'acceslibre sur le segment B2B est sous-estimée.

---

## 2. Sur-optimisme : notes de scoring trop généreuses

### C2 — Cible solvable (qui paie) : **2 → 1** (poids ×3)
La fiche conclut elle-même : usagers ne paient pas (service public + associatif
gratuits) ; ERP non vendables sur cette donnée (déclaratif ≠ conformité) ; État
**finance déjà** l'aide (Fonds territorial d'accessibilité, 300 M€/5 ans) ;
collectivités déjà servies (Someware/Handimap) **et** sollicitées gratuitement par
acceslibre. **Aucun payeur non servi** n'existe → ancrage **1** (« personne ne
paie »), pas 2. Le 2 laisse entendre un payeur résiduel qui n'est pas démontré.

### C7 — Facilité du MVP : **4 → 3** (poids ×2)
Le barème note la facilité d'un **MVP crédible** (livrable utile). Or la fiche dit
elle-même qu'« un MVP honnête ne ferait que dupliquer acceslibre — donc inutile ».
Un MVP techniquement rapide mais **sans livrable valable** ne mérite pas un 4 : le
seul MVP qui aurait du sens (observatoire de couverture, croisement BPE/SIRENE pour
le dénominateur ERP) **requalifie l'idée** et ajoute un vrai coût (dénominateur
fiable). Note 3.

### Notes laissées inchangées (défendables)
- **C1 = 4** : douleur réelle et large (~12 M de personnes) ; le **−1** par rapport
  à 5 (déjà adressée par un service public) est justifié. OK, on ne descend pas
  davantage : la douleur **existe** vraiment.
- **C3 = 3** : ouvert, propre, quotidien, standard CNIG, **mais** couverture ~30 %
  et nature déclarative → plafonné. Juste.
- **C4 = 1**, **C5 = 1** : **mérités et confortés** (voir §4 : acceslibre occupe
  grand public **et** pousse sur les collectivités).
- **C6 = 4** : API/CSV prêts, chiffres SQL-traçables, LLM borné au sens ; pas 5 car
  la donnée elle-même est incomplète. OK.
- **C8 = 2**, **C9 = 2** : redondance service public + responsabilité sur donnée
  déclarative ; ni revenu ni impact additionnel. Justes.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- **Architecture conforme** : nombre de lieux, critères d'accessibilité, taux de
  couverture par commune = **requêtes SQL** sur le CSV/dataset ; LLM borné au sens
  (libellés de critères, synthèse de fiche). Risque d'hallucination faible.
- **Le vrai risque est la fiabilité de la source, pas l'archi** : données
  **déclaratives** (oui/non/inconnu, non auditées) et **incomplètes** (~30 %).
  Afficher « accessible » à tort vis-à-vis d'un **public vulnérable** engage la
  responsabilité — un chiffre « traçable » peut être **faux à la source**. Bien
  identifié au §8 ; pèse sur C3 (déjà à 3) et C8 (déjà à 2), pas besoin d'aggraver.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire)

### Le service public **occupe aussi le segment collectivités** (referme le pivot)
La fiche présente l'« intelligence territoriale / conformité collectivités » comme
le seul créneau éventuel. Or acceslibre **y est déjà actif**, tous liens consultés
2026-06-23 :
- **Open data obligatoire + moissonnage** : les données d'accessibilité sont
  d'« intérêt social » et doivent être ouvertes (CRPA, art. L.300-1 à L.300-4) ;
  acceslibre **moissonne** automatiquement les jeux déjà publiés par les
  collectivités, fournit un **générateur CSV + validateur** au standard, et
  **teste des passerelles** pour connecter les SIG/logiciels de gestion
  d'accessibilité des collectivités. —
  https://fabrique-numerique.gitbook.io/acceslibre/presentation-dacceslibre/acceslibre-pour-les-collectivites/lopen-data-et-les-collectivites
  et https://mairesdefrance.com/contribuez-a-acceslibre-plateforme-accessibilite-article-924-0
- **Acceslibre Mobilités (ALM)** + **webinaire du 5 juin 2026** sur les dernières
  nouveautés de collecte voirie/transports (export NeTEx) : l'État **outille et
  anime** activement la cible publique, gratuitement. —
  https://www.ecologie.gouv.fr/politiques-publiques/donnees-daccessibilite-acceslibre-mobilites
- **Dataset MàJ quotidienne** (data.gouv, dernière MàJ ~18-20 juin 2026) + **API**
  documentée : l'État pousse la **réutilisation** chez les tiers (service-public.fr,
  etc.), donc ne laisse pas de vide produit rémunérateur. —
  https://www.data.gouv.fr/datasets/accessibilite-des-etablissements-recevant-du-public-erp-pour-les-personnes-en-situation-de-handicap

→ Le créneau « collectivités » que la fiche envisageait comme pivot est **déjà
investi par l'État lui-même** (collecte, standard, validation, passerelles SIG),
en plus de Someware/Handimap côté privé. Il ne reste **aucun** segment non servi
exploitable à partir de cette donnée. C4=1 et C5=1 sont confortés.

### Risques / coûts non (assez) soulignés
- **Concurrence par l'institution** : refaire acceslibre, c'est concurrencer un
  service public mieux doté en données et **soutenu réglementairement** (open data
  obligatoire) → position structurellement perdante.
- **Responsabilité morale/juridique** renforcée vis-à-vis d'un public vulnérable
  sur une donnée déclarative incomplète (déjà §8).
- **Dénominateur ERP coûteux** : le seul pivot crédible (observatoire de
  couverture) suppose de construire un dénominateur fiable (BPE/SIRENE), travail
  non trivial — c'est ce qui justifie d'abaisser C7.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 4 | 12 |
| C2 | Cible solvable (qui paie) | ×3 | 2 | **1** | 3 |
| C3 | Disponibilité & fiabilité données | ×3 | 3 | 3 | 9 |
| C4 | Espace concurrentiel libre | ×2 | 1 | 1 | 2 |
| C5 | Différenciation défendable | ×2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | ×2 | 4 | 4 | 8 |
| C7 | Facilité du MVP | ×2 | 4 | **3** | 6 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **55** | | **50 / 105** |

**Score /100** : 50 / 105 × 100 = **48 / 100**.

**Changement de verdict : NON** (reste ❌ Écartée ; marge sous le seuil de 55
élargie de 52 → 48). Le critère quasi éliminatoire (redondance avec un service
public **qui occupe désormais aussi les collectivités**) est confirmé.

---

## 6. Verdict de revue

### **ANALYSE FIABLE** (deux notes légèrement hautes, sans effet sur la décision)

La fiche conclut correctement (❌ Écartée) et de manière bien sourcée. La revue
corrige C2 (aucun payeur non servi → 1) et C7 (un MVP crédible requalifie l'idée
→ 3), et surtout **renforce** la saturation : acceslibre n'est pas seulement le
concurrent grand public, c'est aussi l'acteur qui **outille, standardise et
moissonne** les collectivités — refermant le pivot envisagé. Score recalculé
**48/100**.

### 3 actions prioritaires
1. **Maintenir ❌ Écartée** et compléter le §4 : acceslibre occupe aussi le segment
   collectivités (open data obligatoire, validateur, passerelles SIG, ALM,
   webinaire 06/2026).
2. **Ne plus créditer de payeur** (C2=1) : la donnée déclarative ne se vend ni aux
   ERP (≠ conformité) ni aux collectivités (déjà servies par l'État + Someware).
3. **Si un thème handicap est conservé**, en faire une **nouvelle fiche** sur un
   angle non couvert et chiffrable (ex. observatoire de **complétude** par commune,
   dénominateur BPE/SIRENE), avec un **payeur public nommé** validé avant analyse.

---

REVUE 0016 | analyse fiable | score recalculé 48/100 (vs 52) | changement de décision: non
