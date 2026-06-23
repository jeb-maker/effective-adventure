# Passe V6b — gaps marchés publics × vérification parsing/IDP

- **Pass ID** : `2026-06-v6b-procurement-parsing-verify`
- **Date** : 2026-06-23
- **Script** : `scripts/enrich_catalogue_v6b.py`
- **Contexte** : suite V6 pilote — moisson acteurs FR marchés publics (idée 0001 Radar) et promotion `verified` des parsers/IDP clés (idée 0029 RecordAI), sources officielles uniquement.

## Objectif

1. **Combler les gaps** `public-procurement-intel` identifiés en V6 (Synapse/France Marchés, Tengo, OpenMarchés…).
2. **Promouvoir en `verified`** les parsers email/IDP en `partial` mais sourcés sur domaine officiel (Parseur, Rossum, Dext + 15 autres).
3. Documenter la passe dans `coverage-matrix.json`.

## Segments ciblés

| Segment | Avant | Après | Nouveaux | Promus verified |
|---|---|---|---|---|
| `public-procurement-intel` | 24 | **30** | +6 | — (tous partial, pas de grille publique confirmée) |
| `parsing-inbox` | 51 | 51 | 0 | Parseur, Dext, Mailparser, Parsio, Nylas, Unipile, Mailjet, CloudMailin, EmailEngine, Unstract |
| `document-idp` | 77 | 77 | 0 | Rossum, Klippa, Mindee, Veryfi, Docsumo, Affinda |
| `kyc-aml` | 33 | 33 | 0 | — (passe re-vérification couverture) |
| `compliance-to-spec` | — | — | 0 | Probo, Regulativ.ai |

## Ajouts marchés publics (sources officielles via web search)

| ID | Source consultée | Modèle | verified |
|---|---|---|---|
| `france-marches` | https://www.francemarches.com/offre | freemium | partial |
| `tengo` | https://www.tengo.cc/ | sur devis | partial |
| `openmarches` | https://www.data.gouv.fr/reuses/openmarches-visualisation-des-marches-it-publics | open data | partial |
| `doaken` | https://doaken.fr/solutions | sur devis | partial |
| `olra` | https://olra.fr/fonctionnalites | sur devis | partial |
| `vecteur-plus` | https://www.vecteurplus.com/commande-publique/ | sur devis | partial |

> `openmarches` = analytics attribution DECP (distinct de `decp.info` déjà catalogué).
> `france-marches` = veille majeure FR (distincte de Synapse Entreprises, prestataire dématérialisation profil acheteur).

## Promotions verified (existants `partial` → `verified`)

### parsing-inbox (revue 0029)

| ID | Nouvelle source |
|---|---|
| `parseur` | https://parseur.com/pricing |
| `dext` | https://dext.com/pricing |
| `mailparser` | https://mailparser.io/pricing/ (remplace listicle) |
| `parsio` | https://parsio.io/pricing/ (remplace listicle) |
| `nylas` | https://www.nylas.com/pricing/ |
| `unipile` | https://www.unipile.com/pricing/ |
| `mailjet-parse` | https://www.mailjet.com/pricing/ |
| `cloudmailin` | https://www.cloudmailin.com/pricing |
| `emailengine` | https://emailengine.app/pricing |
| `unstract` | https://unstract.com/pricing/ |

### document-idp (revue 0029)

| ID | Nouvelle source |
|---|---|
| `rossum` | https://rossum.ai/pricing-plans/ (Starter 18 000 $/an publié) |
| `klippa` | https://www.klippa.com/en/pricing/ |
| `mindee` | https://www.mindee.com/pricing |
| `veryfi` | https://www.veryfi.com/pricing/ |
| `docsumo` | https://www.docsumo.com/pricing |
| `affinda` | https://www.affinda.com/pricing |

### compliance-to-spec (revue 0029)

| ID | Nouvelle source |
|---|---|
| `probo` | https://www.probo.io/ (open-source FR) |
| `regulativ-ai` | https://www.regulativ.ai/ |

## Saturation (dernière passe V6b)

| Segment | Candidats | Nouveaux | Taux | Statut |
|---|---|---|---|---|
| `public-procurement-intel` | 13 | 6 | **46,2 %** | Loin du gel (< 5 %) ; cible **L3** |
| `parsing-inbox` | 10 | 0 | passe vérification (pas de moisson) |
| `document-idp` | 10 | 0 | passe vérification (pas de moisson) |
| `kyc-aml` | 5 | 0 | passe vérification couverture |

## Métriques globales post-passe

- **1 422 vendeurs** (+6)
- **80 verified** (+17 vs 63 — Rossum déjà verified, mis à jour source)
- Marchés publics FR : **30 acteurs** (segment non clos — Tendly, Remporte, Tendiz, Espace Marchés Publics restent à moissonner)

## Prochaine passe V6c (suggestion)

1. `public-procurement-intel` : Tendly, Remporte, Tendiz, e-marchespublics, Centrale des Marchés.
2. Confirmer grilles tarifaires (pricing pages) des ajouts V6b → passage `verified`.
3. Vague `verify-eligible` : poursuivre 15-20 promotions/passe depuis les domaines officiels.

## Commandes

```bash
python3 scripts/enrich_catalogue_v6b.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats | grep verified
python3 scripts/catalogue_saas.py verify-eligible | head -30
```
