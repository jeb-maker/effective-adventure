# Passe V6d — gaps marchés publics + verified idées 🔁 + fix listicle

- **Pass ID** : `2026-06-v6d-procurement-verify-listicle`
- **Date** : 2026-06-23
- **Script** : `scripts/enrich_catalogue_v6d.py`

## Ajouts marchés publics (+8)

| ID | Source | Notes |
|---|---|---|
| `saqara` | core.saqara.com | Ex-AOS ; AO privés BTP (Chantier Privé) |
| `explore` | explore.fr/solutions/veille-marches-publics | Veille publique + construction privée |
| `dematis` | formation.dematis.com/sam-ia | MPE + Sam IA |
| `centrale-des-marches` | centraledesmarches.com | Medialex ; freemium |
| `tendly` | tendly.eu/fr/pricing | **verified** — 29 €/mois |
| `remporte` | remporte.fr/tarifs | **verified** — 4 000 € HT/an Starter |
| `tendiz` | tendiz.ai | IA réponse AO |
| `e-marchespublics` | e-marchespublics.com | Portail veille Dematis |

→ `public-procurement-intel` : **33 → 41** entrées. Saturation V6d : **~20 %** (8/41) — segment non clos.

## Promotions verified (idées 🔁)

| Segment cible | ID | Source |
|---|---|---|
| 0001 procurement | olra, publikconnect, marchespublics-ai | pages tarifs |
| 0002 open data | validata | validata.fr |
| 0009 énergie/bâtiments | homeys, effy-pro | tarifs publics |
| 0025 proptech | cityscan | cityscan.fr |
| 0026/0028 territorial | smappen, geomarket | pricing |
| 0028 enrichment | dropcontact, hunter-io, datagma, kaspr | pricing |
| 0029 automation/IDP | windmill, kestra, super-ai, budibase, inngest, mailbutler | pricing |

## Fix sources listicle (0029)

| ID | Avant | Après | Statut |
|---|---|---|---|
| zapier, activepieces, airparser, replit, azure-document-intelligence | listicle | site officiel | **verified** |
| make, docparser, microsoft-power-automate, tines, extracta-ai | listicle | site officiel | partial (URL nettoyée) |

## Gel saturation

Inchangé vs V6c (6 segments gelés). `public-procurement-intel` reste ouvert.

## Prochaine passe V6e

- BTP privé : Spigao, Prescriptio, MPF, Bati-Pulse (hors Vecteur Plus/DOAKEN/Olra)
- Poursuivre `verify-eligible` (~20/semaine) sur segments idées 🔁 restants
- Re-vérifier les **~37 listicle-sourced** restants (hors segment 0029)

## Commandes

```bash
python3 scripts/enrich_catalogue_v6d.py
python3 scripts/catalogue_saas.py validate
python3 scripts/catalogue_saas.py stats | grep -E "verified|listicle|public-procurement"
python3 scripts/catalogue_saas.py segment-readiness | grep public-procurement
```
