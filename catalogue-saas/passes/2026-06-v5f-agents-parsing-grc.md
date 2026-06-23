# Passe V5f — agents, voix, parsing inbox, GRC

| Champ | Valeur |
|---|---|
| `discovery_pass` | `2026-06-v5f-agents-parsing-grc` |
| Date | 2026-06-22 |
| Niveau | L3 (agents) / L2+ (parsing, GRC) |

## Segments enrichis

| Segment | Ajoutés | Exemples |
|---|---:|---|
| `support-sales-agents` | +8 | Parloa, Cognigy, Kore.ai, Replicant, LivePerson |
| `voice-speech-ai` | +5 | Bland AI, Vapi, Speechmatics, Cartesia |
| `parsing-inbox` | +6 | Nylas, SendGrid Inbound, Mailjet (FR), MailSlurp |
| `grc-security` | +6 | Sprinto, Riskonnect, Swimlane, Resolver |
| Segments fins (×7) | +7 | Crisp, Scribe, FloQast, Greenhouse, LinkSquares… |

**Total : +32 vendeurs** (hors patches cross-segments)

## Patches

- Zendesk, Intercom, Freshworks → `helpdesk-platforms`
- Power Automate → `rpa-enterprise`
- Cognigy, Bland → `voice-speech-ai` + `support-sales-agents`

## Saturation (estimée)

```bash
python3 scripts/catalogue_saas.py saturation
```

Passe réelle avec taux ~15–25 % sur agents/parsing — **non gelée** (seuil 5 %).

## Script

```bash
python3 scripts/enrich_catalogue_v5f.py
python3 scripts/sync_idees_catalogue.py
```
