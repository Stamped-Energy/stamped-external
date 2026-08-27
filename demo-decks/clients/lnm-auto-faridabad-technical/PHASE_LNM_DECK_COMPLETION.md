# LNM execution-first deck — example variety

> Date: 2026-08-27 · Target: `demo-decks/clients/lnm-auto-faridabad-technical/index.html`

## Completed

- Stopped using CNC_14 S1/S2 as the through-line across evidence, flip cards, phone, ledger and offer.
- Evidence board now shows fleet state, DISCONNECT/ALARM, Gantt product, event volume, and induction.
- Flip cards: repeating short-stop cluster (asset health) and induction vs machining stagger (energy timing).
- Phone cards are a different set: DISCONNECT walk, long idle, live Gantt job `1774*P/M`.
- Ledger and offer match that spread (3-5 machine mixed cell, not "preferably CNC_14").
- `check-client-decks.py` gates: no CNC_14 S1/S2 centre, flip vs floor titles must not overlap, required example types present.

## Validation

- `python scripts/decks/checks/check-client-decks.py`
- `./scripts/contracts/contract-check.sh`

## Known limitations

- Evidence is still labelled snapshot/sample-derived, not live Andon.
- Alarm-name routing and rupee quantum still depend on plant configuration asks.
- Cell-partner idle remains valid ammunition in the FANUC pack; it is no longer the leave-behind story.

## What you learned

- One sampled cell is proof we read their collector. Repeating it on every slide reads as the only job we can do.
- Flip cards and the phone mockup are two rooms in the same meeting. Different jobs there make the product look wider.
- Honest variety still has to stay inside states we actually have: OPERATE, STOP, DISCONNECT, ALARM, Gantt product, induction on FANUC.
