# Passe V6c — compléter FR + verified RecordAI + gel saturation

- **Pass ID** : `2026-06-v6c-procurement-recordai-freeze`
- **Date** : 2026-06-23
- **Script** : `scripts/enrich_catalogue_v6c.py`

## Ajouts marchés publics (+3)

| ID | Source |
|---|---|
| `synapse-entreprises` | synapse-entreprises.com/espace-entreprises/alerte-marches |
| `wanao` | wanao.com |
| `first-ao` | firstao-appel-offre.fr |

→ `public-procurement-intel` : **30 → 33** entrées. Saturation V6c : **~23 %** (3/13) — toujours non clos.

## Promotions verified (chaîne RecordAI 0029)

| ID | Source |
|---|---|
| `levity` | levity.ai/pricing |
| `pipefy` | pipefy.com/pricing |
| `tonkean` | tonkean.com/pricing |
| `extend-ai` | extend.ai/pricing |
| `nanonets` | nanonets.com/pricing |

Mise à jour `olra` → source tarifs (reste `partial`, devis uniquement).

## Gel saturation

Après V6b, **5 segments** passent sous 5 % :

- `parsing-inbox`, `document-idp`, `kyc-aml` (re-vérification V6b, 0 % nouveaux)
- `voice-speech-ai`, `real-estate-proptech` (déjà proches)

```bash
python3 scripts/enrich_catalogue_v6c.py   # merge + saturation freeze
python3 scripts/catalogue_saas.py segment-readiness
```

## Prochaine passe V6d

- `public-procurement-intel` : Synapse couvert ; reste **AOS**, comparateurs, marchés privés BTP
- Vague `verify-eligible` ciblée segments idées 🔁 (20/semaine)
- Re-vérifier les **48 listicle-sourced** restants
