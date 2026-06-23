# Revue critique (red team) — 0008 Veille d'appels d'offres (BOAMP)

- **Fiche auditée** : `idees/0008-veille-ao-boamp/README.md`
- **Score affiché par la fiche** : — / 100 (écartée : marché saturé) — Verdict affiché : ❌ Écartée
- **Date de la revue / consultation des sources** : 2026-06-23
- **Posture** : évaluateur indépendant et adversarial (cf. `docs/prompts/03-revue-critique.md`)

> **Synthèse en une ligne** : décision d'écart **incontestable** — la veille d'AO
> est le segment le plus saturé du marché des marchés publics (12+ acteurs cités,
> plusieurs avec IA), et les acteurs « attribution » récents (Maître AO,
> Nextend.ai, marchespublics.ai) **font aussi de la veille**, achevant la
> saturation. Score reconstruit ≈ 54/100, ❌ Écartée maintenue. Cohérent avec le
> renvoi vers 0001 (attribution).

---

## 1. Affirmations non sourcées (à sourcer / à supprimer)

| # | Affirmation (citation) | Section | Problème | Verdict |
|---|---|---|---|---|
| A1 | « La valeur résiduelle est sur l'analyse d'attribution (passé), traitée dans l'idée 0001 » | §11 Verdict | **Affirmation à nuancer** : la revue de 0001 a justement montré que l'attribution est elle-même occupée (Maître AO, Nextend.ai, marchespublics.ai). Renvoyer la « valeur » vers 0001 comme s'il était libre est **optimiste**. | **À nuancer (cf. revue 0001)** |
| A2 | « plusieurs avec IA (scoring, analyse DCE, mémoire technique) » | §4 Existant | Vrai et **bien sourcé** (olra, remporte) ; rien à redire. | OK |

**À mettre au crédit de la fiche** : §4 correcte et datée (comparatifs olra,
remporte) ; la liste des acteurs de veille est représentative. C'est une fiche
**minimale mais juste** : elle écarte le bon segment pour la bonne raison.

---

## 2. Sur-optimisme : notes de scoring (la fiche n'en a pas)

La fiche écarte sur critère éliminatoire (saturation) **sans tableau**.
Reconstruction en §5. Attention C2/C4 :

- **C2 (qui paie) = 3** : ici, fait rare, le payeur **existe vraiment** — les PME
  paient déjà 29,99 à 300+ €/mois pour de la veille (AlertOffres, PublikConnect,
  Vecteur Plus). Ce n'est donc **pas** C2 qui tue l'idée. Note 3 (et non plus
  haut, car le budget est déjà capté par les incumbents).
- **C4 (espace libre) = 1** : **plancher justifié**. 12+ acteurs frontaux + IA +
  convergence des acteurs « attribution » vers la veille. Aucun créneau libre.

---

## 3. Risque d'hallucination / respect RAG(sens) / SQL(chiffres)

- Une veille d'AO = essentiellement de l'**agrégation et du filtrage** de flux
  (BOAMP/TED/profils). Le risque d'hallucination est faible (peu de génération de
  chiffres), sauf si on ajoute un « scoring IA » de pertinence — auquel cas la
  traçabilité du score devrait être assurée. Ce n'est pas le point qui tue l'idée.
- La fiabilité technique n'est **pas** le problème ici : c'est la **saturation**.

---

## 4. Angles morts (concurrents, risques, coûts, réglementaire non mentionnés)

### Concurrents — la saturation est encore pire que décrite (consultés 2026-06-23)

- **Veille frontale** (déjà citée, OK) : Vecteur Plus, France Marchés, Synapse,
  Doaken, Olra, PublikConnect (49 € HT), AlertOffres (29,99 €), AOS, Explore,
  Marchés Online, Dématis, Centrale des Marchés.
- **Acteurs « attribution » qui font AUSSI de la veille** (angle mort) :
  - **Maître AO** — DECP + BOAMP, alertes sur avis à venir + intelligence marché
    (https://www.maitre-ao.fr/) ;
  - **Nextend.ai — Observatoire** — DECP **+ BOAMP**, MàJ quotidienne
    (https://nextend.ai/observatoire) ;
  - **marchespublics.ai** — veille + suivi des renouvellements
    (https://marchespublics.ai/).
  → La frontière veille/attribution **se referme** : les nouveaux entrants
  couvrent les deux. Cela **fragilise aussi le renvoi vers 0001** (cf. revue 0001).
- **BOAMP open data** : flux source gratuit (catalogue SaaS `aws-boamp`,
  `verified`) → barrière à l'entrée nulle, ce qui aggrave la saturation.

### Risques / coûts

- **Commoditisation** : la matière première (BOAMP/TED) est gratuite et ouverte ;
  la valeur est dans la distribution et le scoring, déjà industrialisés.
- **Guerre des prix** : plancher à ~30 €/mois (AlertOffres) ; nouvel entrant sans
  base installée = CAC élevé, ARPU bas.

---

## 5. Recalcul du score avec mes notes

| # | Critère | Poids | Note revue | Pondéré | Justification (1 phrase) |
|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | 12 | Douleur réelle et récurrente pour les répondants aux AO. |
| C2 | Cible solvable (qui paie) | ×3 | 3 | 9 | Payeur réel (29,99–300 €/mois) mais budget déjà capté par les incumbents. |
| C3 | Disponibilité & fiabilité données | ×3 | 4 | 12 | BOAMP/TED ouverts, prêts, exploitables. |
| C4 | Espace concurrentiel libre | ×2 | 1 | 2 | Très saturé : 12+ acteurs frontaux + IA + convergence attribution→veille. |
| C5 | Différenciation défendable | ×2 | 1 | 2 | Aucune en frontal ; matière première gratuite, scoring déjà fait. |
| C6 | Faisabilité & fiabilité technique | ×2 | 4 | 8 | Agrégation/filtrage robuste ; peu d'hallucination. |
| C7 | Facilité du MVP | ×2 | 4 | 8 | MVP simple (données prêtes) — ce qui nourrit la saturation. |
| C8 | Maîtrise des risques | ×2 | 1 | 2 | Saturation + commoditisation + guerre des prix non maîtrisées. |
| C9 | Monétisation / impact | ×2 | 1 | 2 | Marché tiré vers le bas ; pas de revenu défendable pour un entrant. |
| | **Total** | | | **57 / 105** | |

**Score /100** : 57 / 105 × 100 = **54 / 100**.

**Changement de décision : NON.**
- Fiche : ❌ Écartée (saturation, sans score).
- Revue : 54/100 → < 55 → ❌ **Écartée**, renforcée par le critère éliminatoire de
  saturation. Convergence. *(Note : C1/C2/C3/C6/C7 élevés maintiennent le score
  juste sous le seuil — preuve que seule la saturation/différenciation tue
  l'idée, pas la donnée ni le besoin.)*

---

## 6. Verdict de revue

### **ANALYSE FIABLE** → ❌ Écartée confirmée

La fiche est **minimale mais correcte** : bon segment écarté, bonne raison
(saturation), §4 datée. La revue confirme l'écart, pose le score à 54/100, et
**aggrave** le constat : les nouveaux acteurs « attribution » font aussi de la
veille, fermant définitivement le segment frontal. Seule réserve : la fiche
présente l'attribution (0001) comme le refuge de la « valeur résiduelle », alors
que la revue de 0001 a montré que ce refuge est lui-même disputé.

### 3 actions prioritaires
1. **Acter le score 54/100** pour tracer l'écart (au lieu d'un éliminatoire sans
   note).
2. **Nuancer le renvoi vers 0001** : préciser que l'attribution n'est pas un
   espace libre (cf. `idees/0001-radar-commande-publique/revue.md`).
3. **Ne pas rouvrir** la veille frontale ; toute énergie sur ce domaine doit
   passer par un différenciateur prouvé (verticalisation, intégration) — sinon
   abandon.

---

REVUE 0008 | analyse fiable | score recalculé 54/100 (vs —) | changement de décision: non (❌ confirmée)
