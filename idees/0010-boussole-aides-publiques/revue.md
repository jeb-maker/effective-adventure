# Rapport de revue critique — Idée 0010 « Boussole des aides et subventions publiques »

**Réviseur** : évaluateur adversarial indépendant  
**Date de revue** : 2026-06-20  
**Fiche auditée** : `idees/0010-boussole-aides-publiques/README.md` (score déclaré 55/100, statut 🔁 À retravailler)  
**Méthode** : `docs/methode-analyse.md` + prompt `docs/prompts/03-revue-critique.md`  
**Vérifications web** : consultées le 2026-06-20 (sources citées ci-dessous)

---

## Synthèse exécutive

L'analyse est **nettement au-dessus de la moyenne** du dépôt : elle reconnaît la saturation, le risque RAG, les verrous de licence et propose un pivot crédible. C'est précisément ce qui la rend difficile à défendre au score 55 : la fiche **sous-estime encore la concurrence** (C4), **surestime la solvabilité réelle** du segment entreprises (C2) et **surestime la maturité du pivot « radar subventions versées »**, déjà occupé par Éclaireur Public et quasi-dupliqué par l'idée 0001 validée.

Le seed « assistant généraliste d'éligibilité » mérite un **écart définitif**. Le pivot transparence n'est pas un simple « à retravailler » : c'est **une autre idée**, en concurrence directe avec des produits existants et avec 0001.

---

## 1. Affirmations non sourcées ou insuffisamment étayées

| Affirmation (README) | Problème | Verdict |
|---|---|---|
| « milliers de dispositifs » (§1) sans chiffre ni source | Vague ; les chiffres existent chez les porteurs (3 000 / 6 000 / 10 000+) | **À sourcer** ou remplacer par les volumes déjà cités en §3–4 |
| « non-recours », « temps perdu », « dépendance à des cabinets coûteux » (§1) | Conséquences plausibles mais **sans lien ni ordre de grandeur** | **À sourcer** (études DGE, Cour des comptes, etc.) ou reformuler en hypothèse |
| « 1,5 M assos » (Data.Subvention, §3) | Chiffre non rattaché à une URL de doc API au moment de la revue | **À sourcer** depuis la doc Data.Subvention |
| « ~60 prestations (PNDS) » OpenFisca (§3) | Pas de lien vers la doc OpenFisca / PNDS | **À sourcer** |
| « > 1 000 aides » pour 1jeune1solution (§4) | Pas de lien daté vers la source officielle | **À sourcer** |
| « conformité réelle faible » SCDL (§3) | Intuition correcte mais **sous-chiffrée** dans la fiche | **À sourcer** — Éclaireur Public : 99,5 % des communes obligées n'ont publié aucune donnée subventions 2024 ([JSS, 2026](https://jss.fr/post/anticor-et-data-for-good-lancent-eclaireur-public-une-plateforme-pour-scruter-les-budgets-locaux)) |
| Licences API Aides-territoires et aides-entreprises « **à vérifier** » (§3) | Honnête, mais pour une idée data-first c'est un **trou de preuve** sur la faisabilité commerciale | **À sourcer** avant tout MVP |
| « ≥ 5 produits IA commerciaux » (§11) | **Sous-compte** : au moins 8 acteurs identifiés en revue (voir §4) | **À corriger** |
| « coût cumulé Mes Aides ~1,25 M€ » (§7) | Lien beta.gouv présent — **recevable** | OK |
| « 49–199 €/an » marché entreprises (§2, §7) | Confirmé pour MaSubventionPro (49/189 € HT, [CGV 2026](https://www.masubventionpro.com/cgv)), URBANCash (199 €/an, [site](https://urbancash.app/)) | OK |
| Recentrage Aides-territoires mars 2026 | Confirmé sur [aides-territoires.beta.gouv.fr](https://aides-territoires.beta.gouv.fr/) | OK |
| Interdiction usage lucratif les-aides.fr | Confirmé [CGU API](https://les-aides.fr/api) | OK |

**Bilan** : peu d'hallucinations factuelles, mais plusieurs affirmations de contexte (non-recours, qualité SCDL, taille du marché payant) restent **narratives plutôt que probantes**. Les licences « à vérifier » sur deux sources centrales sont un angle mort méthodologique.

---

## 2. Sur-optimisme du scoring

### Tableau recalculé (revue)

| # | Critère | Poids | Note fiche | Note revue | Pondéré revue | Justification courte |
|---|---|---|---|---|---|---|
| C1 | Intensité du problème | ×3 | 4 | **4** | 12 | Douleur réelle, bien documentée côté collectivités (Aides-territoires). Inchangé. |
| C2 | Cible solvable (qui paie) | ×3 | 3 | **2** | 6 | Un payeur existe en théorie, mais **l'acquisition est quasi bloquée** : MAPi à 6,75 € HT/mois via LCL ([entrepreneur.lcl.fr](https://www.entrepreneur.lcl.fr/services/mapi)), simulateurs gratuits BNP ([subventions.entreprises.bnpparibas](https://subventions.entreprises.bnpparibas/)), canal experts-comptables verrouillé (MAPI × CNOEC, [Infogreffe 2025](https://www.infogreffe.fr/actualites/l-espace-expert-de-mesaidespubliques-infogreffe-au-service-des-experts-comptables-et-de-leurs-clients)). Les 3 autres cibles ne paient pas. |
| C3 | Disponibilité & fiabilité données | ×3 | 3 | **2** | 6 | Open data « dispositifs » exploitable côté entreprises, mais **données chiffrées pivot SCDL quasi absentes** (99,5 % communes sans publication subventions 2024, Éclaireur Public). Deux sources riches (les-aides, Data.Subvention) **inexploitables** en commercial. |
| C4 | Espace concurrentiel libre | ×2 | 2 | **1** | 2 | Seed = **saturé maximal** (services publics ×4 publics + ≥8 commerciaux). Pivot « transparence subventions » = **déjà occupé** par [Éclaireur Public](https://eclaireurpublic.fr/) (Anticor × Data for Good, open source, gratuit) et **recouvre l'idée 0001** (radar commande publique, score 76, validée). Pas « peu mûr » : c'est un créneau actif. |
| C5 | Différenciation défendable | ×2 | 2 | **2** | 4 | Correct pour le seed. Pour le pivot, différenciation vs Éclaireur Public / 0001 **non démontrée** dans la fiche. |
| C6 | Faisabilité & fiabilité technique | ×2 | 2 | **2** | 4 | Diagnostic RAG/SQL honnête. Point quasi éliminatoire bien identifié pour l'éligibilité. |
| C7 | Facilité du MVP | ×2 | 3 | **2** | 4 | Agrégateur textuel = rapide mais **sans valeur face au gratuit** ; MVP « fiable » ou pivot SCDL = chantier lourd (ingestion hétérogène, taux de conformité catastrophique). |
| C8 | Maîtrise des risques | ×2 | 2 | **2** | 4 | Saturation + responsabilité éligibilité + licences : bien vu. Manque IA Act / RGPD SIRET (voir §4). |
| C9 | Monétisation / impact | ×2 | 3 | **2** | 4 | Revenu théorique mais **marché tiré vers 0** (banques, public, commissions au succès MAPi 10–12 %). Impact non-recours déjà porté par l'État. |
| | **Total** | | | | **44 / 105** | |

**Score /100 recalculé** : round(44 / 105 × 100) = **42/100** (arrondi méthodologique ; fourchette 42–44 selon arrondi).

### Écarts majeurs vs fiche

- **C2 (3 → 2)** : confondre « des entreprises paient quelque part » et « notre cible paiera ». Le prix affiché (49–199 €) est un **plafond de willingness-to-pay**, pas un marché adressable. La distribution bancaire (MAPi/LCL, BNP) et le canal EC (subvention360, MAPI Pro) **captent le budget** avant tout nouvel entrant.
- **C4 (2 → 1)** : la fiche traite le pivot comme « sous-angle moins mûr ». En juin 2026, Éclaireur Public publie indices A–E sur subventions **et** marchés, avec outil d'interpellation des élus ([eclaireurpublic.fr](https://eclaireurpublic.fr/)). L'idée 0001 couvre déjà l'analytics structuré sur dépenses publiques locales. Le pivot n'ouvre pas un espace libre : il **change de segment** sans avantage démontré.
- **C3 (3 → 2)** : pour un produit fondé sur des montants SQL, le désert SCDL est plus grave que « conformité faible ». Sans données, pas de radar — seulement un outil de shame comme Éclaireur Public.
- **C7 et C9 (3 → 2)** : un MVP agrégateur est techniquement rapide mais **stratégiquement inutile** ; la monétisation est un combat à perte contre des acteurs capitalisés (MAPI : 200 000+ utilisateurs, levée 4,4 M€ d'aides clients en 2024 selon [Le Journal des Entreprises](https://www.lejournaldesentreprises.com/article/les-entreprises-ont-tout-interet-se-pencher-sur-les-aides-publiques-2138624)).

---

## 3. Risque d'hallucination / architecture RAG(sens)–SQL(chiffres)

### Ce que la fiche fait bien

- Reconnaît que les critères d'éligibilité sont du **texte libre** → terrain RAG, pas SQL.
- Identifie OpenFisca comme seul moteur de règles fiable côté particuliers.
- Signale le risque de responsabilité sur une éligibilité erronée.

### Failles résiduelles

| Risque | Détail |
|---|---|
| **Montants « par bénéficiaire »** | Les concurrents (URBANCash : « montant chiffré par dispositif », [urbancash.app](https://urbancash.app/)) affichent des chiffres issus de champs textuels « Montants » — même piège. La fiche ne précise pas que **tout affichage de montant personnalisé sans moteur de règles = hallucination probable**, même si le chiffre existe dans la fiche dispositif. |
| **Promesse du pitch** | « À quelles aides ai-je droit » implique une **décision binaire** (éligible / non). RAG + disclaimers ne suffit pas au regard du §3 méthode ; la fiche le dit en §6 mais le pitch et C7 restent ambivalents. |
| **Pivot SCDL** | Là, l'architecture SQL est **théoriquement** saine (montants structurés). Mais avec 99,5 % de communes sans données publiées, le produit afficherait surtout des **trous** — risque d'extrapolation ou d'agrégats trompeurs (moyennes sur échantillon biaisé). |
| **Enrichissement SIRET + site web** | MaSubventionPro analyse SIRET + site ([blog 2026](https://www.masubventionpro.com/blog/masubventionpro-en-detail)) ; si l'idée 0010 emprunte cette voie, **RGPD + IA Act** (système à impact pour décisions d'accès à des financements publics) ne sont pas traités. |

**Verdict fiabilité** : pour le seed, la fiche sous-note à peine le risque (C6=2 est juste mais pourrait être 1 avec critère éliminatoire explicite). Pour le pivot, la fiabilité SQL est **conditionnelle à l'existence des données** — aujourd'hui largement absente.

---

## 4. Angles morts (concurrents, risques, coûts, réglementation)

### Concurrents / services non mentionnés ou sous-représentés

| Acteur | Type | Pourquoi c'est un angle mort |
|---|---|---|
| **subvention360** | B2B EC / conseil, 10 000+ dispositifs, IA | Même écosystème que MaSubventionPro ([subvention360.com](https://subvention360.com/)) — canal de distribution **professionnel** ignoré |
| **MAPI × CNOEC / Infogreffe** | B2B2C experts-comptables, marque blanche | Partenariat institutionnel ([Infogreffe](https://www.infogreffe.fr/actualites/l-espace-expert-de-mesaidespubliques-infogreffe-au-service-des-experts-comptables-et-de-leurs-clients)) — verrouillage du mid-market |
| **Espace Subventions BNP Paribas** | Banque, simulateur gratuit + accompagnement | [subventions.entreprises.bnpparibas](https://subventions.entreprises.bnpparibas/) — concurrent **gratuit** non listé |
| **Mon Budget OPCO** | Gratuit, SIREN + NAF + sync API aides-entreprises | [mon-budget-opco.fr/aides-regionales](https://mon-budget-opco.fr/aides-regionales) — réutilisation directe de l'open data cible |
| **Simulateur DGE aides fiscales innovation** | Public, juillet 2025, 6 dispositifs (CIR, CII, JEI…) | [entreprises.gouv.fr](https://www.entreprises.gouv.fr/la-dge/actualites/un-simulateur-daides-fiscales-pour-accompagner-les-entreprises-innovantes) — **moteur de règles** sur le segment le plus rentable |
| **Éclaireur Public** | Transparence subventions + marchés, gratuit, OSS | [eclaireurpublic.fr](https://eclaireurpublic.fr/) — **concurrent direct du pivot proposé** |
| **Idée 0001** (radar commande publique) | Validée, score 76, SCDL/DECP | Même logique « radar chiffré des dépenses publiques locales » — risque de **doublon interne** |
| **Reki** | MCP Claude, 49 €/mois, dossiers | Confirmé ([reki.eu/mcp](https://www.reki.eu/mcp)) — la fiche le cite, mais sous-estime la **course à l'agentification** (MCP = intégration native dans le workflow) |

### Risques réglementaires / coûts non traités

- **IA Act** : assistants d'éligibilité commercialisés revendiquent déjà la conformité ([MaSubventionPro, janv. 2026](https://www.masubventionpro.com/blog/masubventionpro-en-detail)) — coût de mise en conformité non budgété.
- **Responsabilité civile / conseil déguisé** : au-delà de l'hallucination, le montage de dossiers (roadmap concurrents) frôle l'**activité réglementée** de conseil en financement.
- **Propriété intellectuelle CCI** : les-aides.fr revendique la PI sur le contenu vulgarisé ([CGU API](https://les-aides.fr/api)) — risque si ré-agrégation de textes même via d'autres sources.
- **Chorus / Data.Subvention** : accès agents publics seulement pour le flux le plus riche côté assos — le pivot « Chorus » n'est pas détaillé (conditions d'accès, licence, API).
- **Coût de maintenance** : veille sur 10 000+ dispositifs évolutifs = **OPEX permanent** ; les acteurs incumbents ont 5–10 ans d'avance (Gus revendique 5 ans de R&D, [gus.fr](https://gus.fr/)).

### Incohérence interne de la fiche

Le §11 conclut que le seed est « **à écarter** » (quasi éliminatoire sur fiabilité), mais le statut reste 🔁 À retravailler au score **seuil bas** (55). La revue estime que le score devrait refléter l'écart du seed (**< 55**) et que le pivot devrait être **traité comme spin-off / fusion avec 0001**, pas comme prolongement de 0010.

---

## 5. Recalcul du score et changement de verdict

| | Fiche | Revue |
|---|---|---|
| **Score brut** | 58 / 105 | 44 / 105 |
| **Score /100** | 55 | **42** |
| **Seuil méthode** | 55–69 = À retravailler | < 55 = Écartée |
| **Verdict décisionnel** | 🔁 À retravailler (pivot SCDL) | ❌ **Écartée** (seed + pivot non différencié) |

**Changement de décision : oui.** Le score 55 tient grâce à C2=3, C4=2 et C7/C9=3, tous **trop généreux** au regard des vérifications web. Même en ne corrigeant que C2 et C4, on tombe à 50/105 ≈ **48/100** — sous le seuil.

Le pivot « radar subventions versées » ne sauve pas l'idée 0010 en l'état : il existe déjà (Éclaireur Public) et recoupe 0001. La prochaine étape n'est pas un prototype 0010, c'est un **arbitrage portfolio** (fusion, abandon, ou nouvelle fiche dédiée avec différenciation explicite vs Éclaireur Public).

---

## 6. Verdict de revue et actions prioritaires

**Verdict de revue : à corriger**

L'analyse est **sérieuse et rarement auto-complaisante** sur le fond (saturation, RAG, licences). Elle reste **optimiste sur le scoring** (C2, C4, C7, C9) et **naïve sur le pivot**, qui n'est pas un espace libre en 2026. La qualité rédactionnelle mérite conservation dans le dépôt ; la **décision** doit être reclassée.

### 3 actions prioritaires

1. **Écarter le seed** « assistant généraliste d'éligibilité multi-publics » — espace saturé, fiabilité RAG incompatible avec le §3 méthode, responsabilité juridique. Ne pas prototyper.
2. **Arbitrer le pivot avec 0001 et Éclaireur Public** : soit fusionner dans 0001 (extension module subventions SCDL), soit rédiger une **nouvelle fiche** avec différenciation explicite (B2B vs citoyen, analytics vs indice, périmètre Chorus/assos) — pas un « retravail » de 0010.
3. **Avant toute réouverture** : publier un audit chiffré SCDL (taux de publication par strate, volumétrie lignes, fraîcheur) en s'appuyant sur [Éclaireur Public / méthodologie](https://eclaireurpublic.fr/methodologie) et data.gouv.fr ; sans cela, le pivot n'a pas de donnée produit.

---

REVUE 0010 | à corriger | score recalculé 42/100 (vs 55) | changement de décision: oui
