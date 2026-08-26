# LNM execution-first deck — completion

> Date: 2026-08-27 · Target: `demo-decks/clients/lnm-auto-faridabad-technical/index.html`

## Completed

- Retargeted all 11 scenes from generic forge/HT energy brief to execution-first FANUC MT-LINKi story (C → B → A → D).
- Replaced `scene-fit` with measured evidence board (31 machines, CNC_14 cell split, 1774*P/M, ~527 state cuts, INDUCTION assets).
- LNM-specific prescription flip cards (cell split + induction/CNC timing) with honest readiness labels.
- Six-step decision engine including Verify → Improve with human-review guardrails.
- Floor phone: three LNM workflow cards; Acknowledge / Done / Escalate controls; inbox-clear end state.
- Honest ROI ledger (baseline required / partially ready) replacing fictitious realised ₹ rows.
- Integration slide: three starting asks on existing FANUC stack; close slide: one closed action on a 3-5 machine cell.

## Validation

- `python scripts/decks/checks/check-client-decks.py` — OK (naming + Playwright gates)
- `python scripts/decks/checks/check-floor-phone.py` — ALL_CHECKS_PASSED
- Editorial: no Press/SQF/Compressor generic samples; no em/en dashes in visible HTML; ₹ only where honest

## Known limitations

- Evidence is labelled snapshot/sample-derived, not live Andon.
- Alarm-name routing and rupee quantum depend on plant configuration asks.
- Six agent steps may wrap on narrow mobile; acceptable for room presentation.

## What you learned

- LNM's wedge is last-mile action from data they already collect, not another monitoring layer.
- Honest readiness labels (`Ready now` / `Unlock next`) keep energy visible without fake ₹ on zero kWh samples.
- Improve loop must stay plant-scoped with human review to avoid silent retrain concerns in the room.
