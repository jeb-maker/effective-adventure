# Rapport de revue critique — Idée 0014 « Analyse électorale fine (bureau de vote) »

**Réviseur** : évaluateur indépendant (red team)  
**Date de revue** : 2026-06-20  
**Fiche auditée** : `idees/0014-analyse-electorale-fine/README.md`  
**Score déclaré dans la fiche** : 55/100 (🔁 À retravailler)  
**Méthode** : `docs/methode-analyse.md` + prompt `docs/prompts/03-revue-critique.md`  
**Vérifications web** : consultées le 2026-06-20 (liens cités en §4)

---

## Synthèse exécutive

La fiche est **honnête sur le fond** : elle décrit correctement une saturation du marché, une différenciation faible et un payeur incertain. C'est un mérite rare. En revanche, elle **se contredit en scoring** : C3=5 et C6=4 tirent le total vers le seuil (55), alors que le texte des sections 4, 5, 7 et 8 justifie plutôt un **écartement**. La revue web de juin 2026 révèle surtout des **concurrents majeurs non inventoriés** qui occupent déjà le créneau pivot proposé (outil self-service multi-scrutins, basculements, UX presse/collectivités). Le risque principal n'est pas l'hallucination sur les chiffres bruts, mais la **survente interprétative** (inférence écologique + narration LLM).

---

## 1. Affirmations non sourcées

| Affirmation (fiche) | Problème | Verdict |
|---|---|---|
| « ≈ 70 000 » bureaux de vote en France (§1, §3) | Chiffre plausible mais non sourcé ; les sources officielles oscillent (~65 000–69 000 selon millésime/OM). | **À sourcer** (INSEE REU ou jeu agrégé Etalab) |
| « le coût d'assemblage […] s'est **fortement réduit depuis 2023** » (§1) | Jugement qualitatif sans métrique (heures, €, lignes de code, délai J+8→outil). | **À sourcer ou nuancer** |
| « la presse régionale a **peu de budget** outil » (§2) | Affirmation économique sans étude, barème média ou témoignage daté. | **À sourcer** |
| « Explain […] ~**3 000 € et plus** pour une campagne » (§4, §11) | L'article L'Express cité rapporte le témoignage d'**un** candidat (« plus de 3000 euros »), pas une grille tarifaire officielle ; la fourchette réelle va de quelques dizaines €/mois à « plusieurs dizaines de milliers d'euros » selon le même article ([L'Express, 2026-06-20](https://www.lexpress.fr/informations/explain-quorum-ces-strateges-numeriques-plebiscites-par-les-candidats-aux-municipales_2118220.html)). | **À reformuler** (fourchette + source primaire produit) |
| « DigitaleBox […] à partir de **19 €/mois** » (§2, §4) | Lien marketing, pas de capture tarifaire datée ni de périmètre fonctionnel (BV+INSEE ?). | **À sourcer** (page tarifs datée) |
| « Quorum, NationBuilder, **Spallian** » (§4d) | Cités en vrac sans lien individuel ni date ; Spallian n'est pas détaillé. | **À sourcer** ou **à supprimer** |
| Projet « **Le carré social** » (§4c) | Mentionné sans URL ; pourtant central dans la méthodo IRIS/BV (dataset data.gouv.fr). | **À sourcer** ([data.gouv.fr — Position des IRIS dans le carré social](https://www.data.gouv.fr/datasets/position-des-iris-insee-dans-le-carre-social), [Le carré social — Jérémy Perrin, mars 2026](https://www.data.gouv.fr/datasets/liaison-iris-bureaux-de-vote-de-2024)) |
| Pivot « villes moyennes 10k–100k hab. où **la recherche dit** que les progrès les plus importants pourront être accomplis » (§4, §11) | Citation implicite non référencée dans le README. | **À sourcer** ([PDF La Grande Conversation / Donnée électorale, oct. 2023](https://www.lagrandeconversation.com/app/uploads/2023/10/donnee-electorale-pourquoi-tout-va-changer-la-grande-conversation.pdf)) |
| C3 = 5 : « données **propres**, jointures **déjà outillées** » (§10) | Contredit par les limites documentées dans la même fiche (~3 000 BV à identifiants divergents, contours Voronoï non autoritaires, structure agrégée modifiée janv. 2026). | **À corriger** (note + libellé) |
| « **Pas de risque éliminatoire** » / « légalité OK » (§8, §11) | Trop absolu : RPP (oct. 2025) et guide CNIL 2025 encadrent le ciblage politique en ligne ; un outil de ciblage expose à conformité RGPD/RPP non analysée. | **À nuancer** |

**Verdict global §1** : la section concurrence (§4) est mieux sourcée que la moyenne du dépôt, mais plusieurs chiffres-clés (volume BV, prix, budgets presse) et le pivot « recherche / villes moyennes » restent **non recevables** au sens strict de `methode-analyse.md` §2.

---

## 2. Sur-optimisme du scoring

La fiche affiche une tension interne : le narratif plaide la saturation, le barème reste au seuil grâce à C3 et C6.

| Critère | Note fiche | Note revue | Écart | Justification adversarial |
|---|---|---|---|---|
| **C1** — Intensité du problème | 3 | **3** | 0 | Besoin réel à chaque scrutin, mais douleur analytique modérée ; la fiche le dit elle-même. |
| **C2** — Cible solvable | 2 | **1** | −1 | Seuls payeurs = campagnes, segment **capté et intermittent** ; le pivot presse régionale/collectivités n'a **aucune preuve de solvabilité** ; concurrents à 20–30 €/mois (Politiciae) ou packages campagne (Explain, Qomon, Terre de Données) absorbent les budgets restants. Presse = utilisatrice, pas payeuse (contenus publiés en open access). |
| **C3** — Données | 5 | **3** | −2 | Données **existantes** sous Licence Ouverte ≠ données « prêtes, propres » (ancrage 5). Hétérogénéité multi-scrutins, rupture schéma janv. 2026 ([jeu agrégé](https://www.data.gouv.fr/datasets/donnees-des-elections-agregees)), ~4 % de BV à rapprochement REU incertain, socio Filosofi en N−3 avec imputations, contours **estimés** (Voronoi, non autoritaires — [blog INSEE](https://blog.insee.fr/a-vote-a-chaque-bureau-de-vote-ses-electeurs/)). C3=3 = « disponibles mais travail lourd ». |
| **C4** — Espace libre | 1 | **1** | 0 | Déjà au minimum ; la revue web **renforce** ce constat (voir §4). La note est cohérente, mais le verdict global devrait en tirer les conséquences (écartement, pas « à retravailler »). |
| **C5** — Différenciation | 2 | **1** | −1 | Méthode publiée (Souidi & Vonderscher, janv. 2026 ; [Éditions Textuel](https://www.editionstextuel.com/livre/nouvelle_cartographie_electorale_de_la_france)), graphes « Le carré social », Explain/Qomon déjà sur BV×INSEE. Le pivot « multi-scrutins + basculements » est **déjà en produit** (Ballotage, Politic Data). |
| **C6** — Faisabilité / fiabilité | 4 | **3** | −1 | SQL sur résultats bruts = OK. Mais la **valeur produit** repose sur corrélations socio×vote (inférence écologique) et potentielle narration LLM : zone grise entre sens et chiffres. Architecture déclarée saine, **produit final** fragile. |
| **C7** — Facilité MVP | 3 | **2** | −1 | Homogénéisation 2017→ et basculements = travail déjà fait par Datagère/Ballotage (2002–2024, [méthodologie](https://www.datagere.com/methodologie-et-traitement-des-donnees-electorales/)) ; miroir Hugging Face ([dataset agrégé](https://huggingface.co/datasets/Data-Gouv-FR/donnees-des-elections-agregees)). Battre l'existant gratuit demande plus qu'un MVP technique. |
| **C8** — Maîtrise des risques | 2 | **1** | −1 | Saturation commerciale + risque réputationnel (mésusage interprétatif) + **cadre RPP/CNIL 2025** sur ciblage politique ([guide CNIL](https://cnil.fr/sites/default/files/2025-11/guide_communication_politique.pdf)) non traité comme risque produit. |
| **C9** — Monétisation / impact | 2 | **1** | −1 | Monétisation faible confirmée ; impact civique **déjà produit** (presse, chercheurs, ouvrage de référence, apps communautaires). Valeur incrémentale marginale. |

**Point focal C2/C4** : la fiche sous-estime C2 en laissant un espoir de pivot presse/collectivités sans signal payeur, et **sous-trait C4** en omettant des acteurs qui comblent exactement l'espace résiduel qu'elle décrit. C4=1 est juste ; C2 devrait être à **1**, pas 2.

---

## 3. Risque d'hallucination / RAG(sens)–SQL(chiffres)

### Ce qui est conforme

- L'architecture déclarée (§6) respecte le principe **RAG(sens) / SQL(chiffres)** pour les résultats électoraux bruts et les indicateurs INSEE tabulaires.
- La fiche mentionne correctement l'**inférence écologique** et l'incertitude géographique.

### Ce qui manque ou inquiète

| Risque | Gravité | Commentaire |
|---|---|---|
| **Valeur = interprétation, pas chiffres** | Élevée | Le pitch (« comprendre *pourquoi* un territoire vote ») pousse le LLM à produire des causalités plausibles à partir de corrélations agrégées. Les chiffres SQL seront exacts ; les **explications** seront le point de défaillance. |
| **Jointures estimées présentées comme profil BV** | Moyenne | Filosofi 200 m → IRIS/BV → « profil socio estimé » : sans garde-fous UI stricts, l'utilisateur perçoit une vérité individuelle. |
| **Absence de spec anti-hallucination** | Moyenne | Pas de mention de citations obligatoires, de refus systématique sur causalité individuelle, ni de tests de régression sur requêtes SQL. |
| **Chiffres dans le narratif sans requête** | Faible dans la fiche | Le README ne cite pas de KPI marché inventés ; mais les notes C3/C5 supposent une qualité données « excellente » non démontrée par un audit. |

**Verdict §3** : pas de hallucination flagrante dans la fiche elle-même, mais le **couple produit + LLM** est à haut risque si l'outil répond à « pourquoi » plutôt qu'à « quoi (avec incertitude) ». C6=4 est **trop généreux** compte tenu de l'objet réel du produit.

---

## 4. Angles morts (non mentionnés ou sous-estimés)

### Concurrents / réutilisations absents de §4

| Acteur | Ce qu'il fait | Source (2026-06-20) | Impact sur l'idée |
|---|---|---|---|
| **Ballotage / Datagère** | App multi-scrutins, harmonisation 2002–2024 au BV, basculements, exports PDF, hébergement FR | [data.gouv.fr/reuses/ballotage](https://www.data.gouv.fr/reuses/ballotage), [méthodologie](https://www.datagere.com/methodologie-et-traitement-des-donnees-electorales/) | **Colle au pivot exact** de la fiche (self-service, historique, basculements) ; MAJ mars 2026 post-municipales |
| **Qomon** | BV×INSEE, indicateurs maison (force électorale, évolution, reports T1/T2), export PDF territoire | [fr.qomon.com](https://fr.qomon.com/produit/donnees-et-cartographie), [aide données BV](https://help.qomon.com/fr/articles/3272235-donnees-repertoire-des-donnees-presentes-dans-l-onglet-carte) | Segment payeur campagne, déjà sur le croisement |
| **Terre de Données — Data Vote** | Résultats BV depuis 2002 × socio INSEE, carto, fiches PDF | [terrededonnees.fr/data-vote](https://www.terrededonnees.fr/data-vote/) | Concurrent direct campagne locale |
| **Politiciae DATA** | Carto commune/IRIS/BV, 200 m, dès 29,99 €/mois, 35 000 communes | [politicae.fr](https://politicae.fr/lanalyse-data-de-ma-commune/) | Prix d'entrée bas, municipales 2026 |
| **Politic Data** | 68 816 BV, 2017–2026, visualisation multi-échelles | [politicdata.com](https://www.politicdata.com/) | Pack payant département/circonscription |
| **Le carré social** (J. Perrin) | Graphes électoraux infra-communaux, méthode IRIS/BV publiée | [dataset carré social](https://www.data.gouv.fr/datasets/position-des-iris-insee-dans-le-carre-social) | Diffusion méthode + viz — concurrence **gratuite/académique** |
| **Souidi & Vonderscher** | Ouvrage de référence janv. 2026, ~70 000 BV × INSEE | [Éditions Textuel](https://www.editionstextuel.com/livre/nouvelle_cartographie_electorale_de_la_france) | Fixe le plafond de nouveauté analytique grand public |
| **Hugging Face — dataset agrégé** | Miroir communautaire Parquet du jeu Etalab | [huggingface.co/datasets/Data-Gouv-FR/donnees-des-elections-agregees](https://huggingface.co/datasets/Data-Gouv-FR/donnees-des-elections-agregees) | Réduit la barrière technique du MVP |
| **Muni-API** | API statique communes (élections + démo + équipements), défi data.gouv 2026 | [data.gouv.fr/reuses/muni-api](https://www.data.gouv.fr/reuses/muni-api-le-moteur-de-donnees-des-enjeux-locaux-2026) | Concurrent infra presse/collectivités |
| **Contours BDV** (C. Mandron) | API GeoJSON BV, DuckDB | [GitHub contours_bdv](https://github.com/clementmandron/contours_bdv) | Gratuit, réduit le coût d'assemblage géo |
| **Geoffrey Pion** | Géomarketing sous-BV (rue/bâtiment), guide 2026 | [geoffreypion.com](https://geoffreypion.com/2026/02/le-geomarketing-electoral-definition/) | Concurrence **plus fine** que le BV pour campagnes |

### Risques / coûts / réglementation

- **RPP (application oct. 2025)** : contraintes sur ciblage et publicité politique en ligne à partir de données indirectes ([CNIL, nov. 2025](https://cnil.fr/sites/default/files/2025-11/guide_communication_politique.pdf)) — pertinent si le produit s'adresse aux campagnes ou recommande des zones de porte-à-porte.
- **Critiques éthiques ciblées sur Explain/LMP** : agrégation INSEE + BV perçue comme contournement du ciblage individuel ([Privacy International](https://www.privacyinternational.org/examples/4389/france-data-violations-recent-elections)) — risque réputationnel pour tout nouvel entrant sur le segment campagne.
- **Contexte mars 2026** : municipales viennent de saturer l'attention (Ballotage MAJ 23/03/2026) ; fenêtre commerciale fermée jusqu'au prochain scrutin majeur.
- **Presse** : Le Monde publie déjà des analyses BV×revenu ([juil. 2024](https://www.alternatives-economiques.fr/le-revenu-variable-cle-du-premier-tour-des-legislatives-2024)) et cite Souidi/Vonderscher ([fév. 2026](https://www.lemonde.fr/idees/article/2026/02/18/quand-la-cartographie-du-vote-permet-d-identifier-ou-se-joue-l-election_6667290_3232.html)) — la presse **est productrice**, pas cliente d'un SaaS générique.
- **Collectivités** : logiciels métier (ex. Logitud Scrutin) couvrent la **nuit électorale** opérationnelle, pas l'analyse socio-électorale — mais le budget « comprendre le vote » reste théorique.

### Sous-estimation du travail produit

La fiche reconnaît l'effort d'homogénéisation multi-scrutins (§9), mais **sous-estime** qu'un acteur (Ballotage) revendique déjà 20 ans de BV harmonisés et des « dizaines de millions de lignes » optimisées. Reproduire « mieux que l'existant gratuit » n'est pas un MVP : c'est un **projet data platform**.

---

## 5. Recalcul du score

### Tableau revue

| # | Critère | Poids | Note fiche | **Note revue** | Pondéré fiche | **Pondéré revue** |
|---|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 3 | **3** | 9 | **9** |
| C2 | Cible solvable | ×3 | 2 | **1** | 6 | **3** |
| C3 | Données | ×3 | 5 | **3** | 15 | **9** |
| C4 | Espace concurrentiel | ×2 | 1 | **1** | 2 | **2** |
| C5 | Différenciation | ×2 | 2 | **1** | 4 | **2** |
| C6 | Faisabilité / fiabilité | ×2 | 4 | **3** | 8 | **6** |
| C7 | Facilité MVP | ×2 | 3 | **2** | 6 | **4** |
| C8 | Maîtrise des risques | ×2 | 2 | **1** | 4 | **2** |
| C9 | Monétisation / impact | ×2 | 2 | **1** | 4 | **2** |
| | **Total** | | | | **58 / 105** | **39 / 105** |

```
Score fiche   : round(58 / 105 × 100) = 55 / 100
Score revue   : round(39 / 105 × 100) = 37 / 100
```

### Changement de verdict

| | Fiche | Revue |
|---|---|---|
| Score | 55/100 | **37/100** |
| Seuil | 🔁 À retravailler (55–69) | ❌ **Écartée** (< 55) |
| Décision | Garder sous réserve de pivot payeur | **Écarter** — le pivot proposé est déjà occupé (Ballotage, Politic Data, carré social) et le payeur alternatif non démontré |

**Changement de décision : oui.** La fiche elle-même décrit un marché saturé (C4=1) et une monétisation faible ; le score 55 est un artefact de **C3 surévalué** qui contredit les sections données et concurrence.

---

## 6. Verdict de revue

**Verdict : à corriger** (analyse qualitative utile, scoring et inventaire concurrentiel incomplets ; pas « à refaire » car l'honnêteté sur la saturation évite une réécriture totale).

### 3 actions prioritaires

1. **Compléter §4** avec les acteurs vérifiés en juin 2026 — au minimum Ballotage/Datagère, Qomon, Terre de Données, Politicae, Politic Data, Le carré social — et reclasse le pivot « multi-scrutins + basculements + self-service » comme **déjà adressé**, pas comme niche libre.

2. **Rebasculer C3 (5→3) et C2 (2→1)** avec justification alignée sur le texte existant : données ouvertes mais jointures estimées, schémas hétérogènes, concurrence gratuite sur la chaîne complète. Recalculer le score ; si < 55, passer le statut à ❌ Écartée sans attendre un panel presse régionale auquel la fiche ne donne aucun signal positif.

3. **Trancher le périmètre LLM** : si l'outil explique le « pourquoi » du vote, documenter des garde-fous testables (refus causalité individuelle, disclaimers systématiques, zéro chiffre hors SQL) ; sinon **retirer le LLM** et se limiter à un explorateur SQL/carto — ce qui renforce la concurrence directe avec Ballotage et abaisse encore C5.

---

REVUE 0014 | à corriger | score recalculé 37/100 (vs 55) | changement de décision: oui
