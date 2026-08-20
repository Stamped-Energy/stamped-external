# Client decks

Linked from the main demo hub via **Clients** → [`index.html`](./index.html).

These are **11-scene technical briefs** (Nestlé / ITC shell), not industry Proof Runs. Copy follows the live website pillars: Industry Energy Management and Asset Health Intelligence. HTML is hand-authored. `python scripts/decks/build/build-client-decks.py` only syncs `assets/`.

| File | Use |
|------|-----|
| [index.html](./index.html) | Client deck picker |
| [nestle-pantnagar-technical/](./nestle-pantnagar-technical/) | Nestlé Pantnagar Maggi leave-behind (warehouse HVAC, ToD / MD). Quality bar. Uses "rupee(s)", not ₹. |
| [itc-nadiad-technical/](./itc-nadiad-technical/) | ITC Nadiad technical brief (deploy folder) |
| [itc-nadiad-technical.html](./itc-nadiad-technical.html) | Flat twin of the ITC folder index |
| [lnm-auto-faridabad-technical/](./lnm-auto-faridabad-technical/) | LNM Auto Faridabad Sector 59 leave-behind (precision forge / machine / HT / surface) |
| [lohia-corp-brief.html](./lohia-corp-brief.html) | Named Lohia brief (DIC, not a second audit, Chaubepur visit) |
| [auto-forge-ht.html](./auto-forge-ht.html) | Anonymous forge / HT / die-cast brief (must not name LNM) |
| [machinery-oem.html](./machinery-oem.html) | Anonymous packaging-machinery OEM brief (60-day Proof Run if justified) |
| [machinery-oem/](./machinery-oem/) | Optional standalone deploy root |
| [technical-explainer.html](./technical-explainer.html) | Generic sales collateral (60-day close) |
| [assets/](./assets/) | Co-located images (open HTML from this folder) |

**Gate:** `python scripts/decks/checks/check-client-decks.py`
