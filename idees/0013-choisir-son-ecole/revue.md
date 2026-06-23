# Revue critique (red team) — 0013 Aide au choix d'établissement scolaire (IPS + résultats)

- **Fiche auditée** : `idees/0013-choisir-son-ecole/README.md`
- **Score affiché par la fiche** : 59 / 100 — Verdict affiché : 🔁 À retravailler
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : la fiche est **lucide et bien documentée** sur la
> saturation (C4=1, C5=1 mérités), mais elle reste **complaisante sur C1, C2 et
> C7**, et son inventaire concurrentiel — déjà fourni — s'est **encore alourdi
> depuis le 2026-06-20** (au moins trois réutilisations supplémentaires, dont une
> créée le 10 juin 2026). Recalcul adversarial : **51/100 → ❌ Écartée**.

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « copiable en un week-end — et déjà copié plusieurs fois » | §5 | Le « déjà copié » est **prouvé** (Vis-Ma-Classe, Lucyol, réutilisations) ; le « en un week-end » reste un **jugement** non démontré. Sert à charge donc peu gênant. | **Reformuler** (effort non chiffré) |
| A2 | « payeurs hypothétiques : relocation/expatriation, RH mobilité, immobilier » | §2 | La fiche le reconnaît elle-même : « aucun budget nommé/sourcé ». C'est une **piste**, pas un payeur. Bien signalé, mais ne doit pas soutenir une note C2. | **À valider (entretiens)** |
| A3 | « la qualité scolaire influence l'attractivité d'un quartier » | §2 | Plausible et communément admis, mais asséné sans source pour fonder un payeur immobilier. | **À sourcer / nuancer** |

**À mettre au crédit de la fiche** : §3 (sources DEPP par UAI, licences, fraîcheur,
ruptures de série IPS 2022, seuils de diffusion VA) et §4 (DEPP, presse,
réutilisation data.gouv, Vis-Ma-Classe, Lucyol — tous datés 2026-06-20) sont
**solides**. Le contexte « combat de transparence / ségrégation » est bien posé.
Le défaut n'est pas le sourcing, c'est l'**indulgence du scoring**.

---

## 2. Sur-optimisme : notes de scoring trop généreuses

### C2 — Cible solvable (qui paie) : **2 → 1** (poids ×3)
Point d'attention prioritaire du prompt. La fiche admet : parents = **ne paient
pas** (gratuit partout, usage ponctuel) ; journalistes/chercheurs = budget faible
qui consomment la donnée brute ; B2B (relocation/immobilier/RH) = **« aucun budget
nommé/sourcé »**. Quand **aucun** payeur n'est identifié ni validé, c'est l'ancrage
**1** (« personne ne paie »), pas 2. La note 2 crédite un espoir B2B que la fiche
qualifie elle-même de non sourcé.

### C1 — Intensité du problème : **3 → 2** (poids ×3)
La fiche liste trois atténuateurs : (a) au collège public, choix **contraint par
la carte scolaire** (on est affecté) ; (b) douleur **ponctuelle** (une fois par
enfant), peu propice à un abonnement ; (c) besoin **déjà très bien couvert**
gratuitement. Une douleur ponctuelle, contrainte et déjà servie tend vers
l'ancrage 2 (« besoin tiède »), pas 3. Le 3 surévalue l'intensité **marchande**.

### C7 — Facilité du MVP : **5 → 4** (poids ×2)
Un MVP **crédible** (au sens du barème : livrable utile) ne se limite pas à joindre
des CSV par UAI : il doit **neutraliser les pièges de comparabilité** que la fiche
documente elle-même (rupture de série IPS 2022, bond IPS privé 2023 non comparable,
seuils de diffusion VA ≥ 40 présents, IPS ≠ qualité). Un comparateur naïf serait
trompeur ; le rendre honnête (encarts pédagogiques, avertissements, gestion des
non-renseignés < 5 élèves) ajoute un coût réel. MVP rapide mais pas trivial → 4.

### Notes laissées inchangées (défendables)
- **C3 = 5** : données DEPP complètes, propres, ouvertes (LO 2.0), jointes par UAI,
  MàJ annuelle. Atout réel, OK.
- **C4 = 1** et **C5 = 1** : **mérités et confirmés à charge** (voir §4 ci-dessous,
  saturation aggravée). 
- **C6 = 5** : chiffres 100 % SQL/traçables, LLM borné au sens → fiabilité par
  construction. OK.
- **C8 = 2** : risques économiques (pas de payeur) + éthiques (classement,
  ségrégation, mésusage IPS) réels mais non illégaux. OK.
- **C9 = 2** : revenu grand public ~nul, impact déjà capté ; seule porte B2B non
  validée. OK.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- **Architecture conforme et exemplaire** : IPS, écart-type, taux de réussite/
  mention/accès, valeur ajoutée, effectifs viennent **directement des fichiers
  DEPP** (SQL traçable). Le LLM est cantonné au **sens** (qu'est-ce que l'IPS,
  comment lire une VA négative). Risque d'hallucination quasi nul — point fort,
  à conserver (justifie C6=5).
- **Le vrai risque est interprétatif, pas hallucinatoire** : un chiffre **exact**
  (IPS, VA) peut induire une **lecture fausse** (IPS pris pour un « niveau »,
  comparaison à travers une rupture de série). C'est un risque produit/éthique,
  déjà bien identifié au §6 et §8 — il n'invalide pas l'archi mais pèse sur C7/C8.
- **Pas de chiffre de marché halluciné** dans la fiche : les volumes (66 000+
  établissements, ~2 205 lycées) sont sourcés. Bon réflexe.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire)

### La saturation **s'est aggravée depuis la rédaction** (renforce C4=1)
Réutilisations gratuites **supplémentaires**, non citées par la fiche, toutes
consultées le 2026-06-23 :
- **EducaScore** — comparateur gratuit écoles/collèges/lycées : IPS, valeur
  ajoutée (DNB + Bac), effectifs par classe et spécialités de Terminale, **et même
  la conformité nutritionnelle des cantines (Ma Cantine)** + dépenses d'éducation
  des communes ; tableaux comparatifs, filtres géo, carto interactive. **Créé le
  10 juin 2026** — c'est-à-dire **après** la rédaction de la fiche. —
  https://www.data.gouv.fr/reuses/educascore-comparateur-decoles-colleges-et-lycees-ips-valeur-ajoutee-cantines
- **EcolesInfo / resultats-lycee.fr** — site gratuit « qualité réelle des
  collèges et lycées » : VA, IPS, taux bac/brevet, données DEPP/data.gouv. —
  https://resultats-lycee.fr/
- **EcoleScope** — 62 884 établissements indexés, IPS + valeur ajoutée DEPP +
  **sectorisation officielle (carte scolaire Paris/Marseille/IDF)**, sans pub ni
  tracking. — https://ecolescope.fr/

→ Le créneau « comparer collèges/lycées pour parents » n'est pas seulement saturé,
il **se densifie en temps réel** (un nouveau réutilisateur en juin 2026). Pire,
EducaScore et EcoleScope **dépassent** déjà le périmètre du seed (cantines,
sectorisation, dépenses communales), invalidant aussi les pistes « d'enrichissement »
envisagées. C4=1 est non seulement mérité mais **conforté**.

### Risques / obstacles non (ou peu) mentionnés
- **Course à l'enrichissement perdue d'avance** : chaque dataset DEPP étant
  ouvert, tout différenciateur (cantines, sectorisation, dépenses) est ajouté par
  un concurrent en quelques semaines (EducaScore l'a fait).
- **Risque réputationnel/éthique** (ségrégation, IPS comme proxy) bien vu §8,
  mais accentué par la multiplication d'acteurs : la **course au classement** est
  un jeu à somme négative pour la société, où arriver 6ᵉ n'apporte rien.
- **Acquisition impossible** : SEO déjà trusté par presse nationale (Figaro,
  Parisien, L'Étudiant, franceinfo) + sites établis ; CAC prohibitif.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | **2** | 6 |
| C2 | Cible solvable (qui paie) | ×3 | 2 | **1** | 3 |
| C3 | Disponibilité & fiabilité données | ×3 | 5 | 5 | 15 |
| C4 | Espace concurrentiel libre | ×2 | 1 | 1 | 2 |
| C5 | Différenciation défendable | ×2 | 1 | 1 | 2 |
| C6 | Faisabilité & fiabilité technique | ×2 | 5 | 5 | 10 |
| C7 | Facilité du MVP | ×2 | 5 | **4** | 8 |
| C8 | Maîtrise des risques | ×2 | 2 | 2 | 4 |
| C9 | Monétisation / impact | ×2 | 2 | 2 | 4 |
| | **Total** | | **62** | | **54 / 105** |

**Score /100** : 54 / 105 × 100 = **51 / 100**.

**Changement de verdict : OUI.**
- Fiche : 59/100 → bande 55–69 → 🔁 À retravailler.
- Revue : 51/100 → bande < 55 → ❌ **Écartée**.

Le §11 de la fiche dit déjà que « sans pivot, le verdict de fait est proche du
rejet » : la revue acte ce rejet. Le pivot B2B reste une **idée nouvelle** à
instruire séparément, pas un argument pour maintenir 59.

---

## 6. Verdict de revue

### **À CORRIGER → confirme l'ÉCART**

Analyse **fiable et honnête** dans le diagnostic, mais **score complaisant** sur
trois critères (C1, C2, C7) au regard de son propre texte (« douleur ponctuelle
et contrainte », « payeur B2B non sourcé », pièges de comparabilité). Une fois
corrigées, l'idée tombe à **51/100 → ❌ Écartée**, d'autant que l'existant gratuit
**s'est densifié depuis la rédaction** (EducaScore créé le 10/06/2026, EcoleScope,
EcolesInfo). Aucun critère sauveur ; le seul atout (donnée parfaite) est ce qui
banalise le produit.

### 3 actions prioritaires
1. **Basculer le statut en ❌ Écartée** (score 51) et mettre à jour le §4 avec
   EducaScore / EcoleScope / EcolesInfo (saturation aggravée 2026-06-23).
2. **Cesser de créditer le B2B non validé** (C2=1) : tout retour de l'idée exige
   d'abord un **payeur nommé** (relocation, immobilier, RH mobilité) confirmé par
   entretiens, traité comme **nouvelle fiche**.
3. **Ne pas reconstruire un comparateur grand public** : il n'y a aucun fossé, et
   chaque enrichissement est rattrapé en semaines par un réutilisateur gratuit.

---

REVUE 0013 | à corriger | score recalculé 51/100 (vs 59) | changement de décision: oui
