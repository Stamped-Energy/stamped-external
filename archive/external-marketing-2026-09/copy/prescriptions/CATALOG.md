# Prescription catalog (compiled)

**Agent use:** sample talk-tracks and floor actions we already show clients. All money figures are **`[illustrative]`** until M&V baseline is locked.

Full card fields (talk track, evidence tags, owners) for the canonical ten types: [`../../demo-decks/prescriptions-examples.md`](../../demo-decks/prescriptions-examples.md).

Refresh deck extracts: `python scripts/decks/checks/extract-deck-rx.py` then regenerate this file.

---

## A · Canonical examples (from prescriptions deck)

| # | Title (short) | Lever |
|---|---------------|-------|
| 1 | Hold the second feeder start 10 minutes | Load staggering / MD |
| 2 | Gravure dryer warm-up 25 min earlier | ToD + thermal timing |
| 3 | Inspect Compressor 2 filter / unload valve | Equipment drift |
| 4 | Switch off packaging line aux after 20 min idle | Idle-load reduction |
| 5 | Start batch chiller later — batch still on time | Utility scheduling + ToD |
| 6 | Schedule negotiation vignette | Agentic feasibility |
| 7 | Reduce furnace holding when roll delayed 45+ min | Thermal / idle holding |
| 8 | Start the mill after the kiln settles | Stagger + WHR preference |
| 9 | Trim chillers when the batch hall is empty | Utility scheduling / HVAC |
| 10 | Check CW pump P-12 — valve may be stuck recirculating | Inspect / tune |

See the markdown twin for full **What / Why / Owner / Impact / Effort / Due / Evidence**.

---

## B · Deck & floor prescriptions (extracted from HTML)

Deduped by title. Sources under `demo-decks/`. Prefer these when matching an industry or named brief.

### Rx cards (scene-prescription)

#### B1. Stagger Compressors 1 & 3 vs furnace-bay start by ≥8 min at Shift B handover

- **Badge:** Rx · MD coincidence
- **Why:** Mon 07:12-07:20 overlap drove the incomer MD window
- **Impact:** ₹2.5-4L / month — treat as illustrative unless labelled locked
- **Source:** `demo-decks/_base.snapshot.html`

#### B2. Stage Compressor Bank B offline during the planned 45-min changeover window

- **Badge:** Rx · Idle / holding
- **Why:** Unload kWh with no production tag on 3 of last 5 changeovers
- **Impact:** ₹80k-1.2L / month — treat as illustrative unless labelled locked
- **Source:** `demo-decks/_base.snapshot.html`

#### B3. Stagger mill start and kiln fans by 10 minutes

- **Badge:** Rx · MD coincidence
- **Why:** Two heavy starts in the same demand window stacked on the incomer. The bill shows the MD peak later, not which mill and kiln fans overlapped while the window was still open.
- **Impact:** ₹3-5L / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/cement.html`

#### B4. Use more WHR in the evening peak; cut grid import

- **Badge:** Rx · WHR / tariff
- **Why:** WHR output was available in the evening peak while the plant still bought grid power. Shift load to the cheaper source before the MD window closes.
- **Impact:** ₹2-4L / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/cement.html`

#### B5. Stagger chillers and autoclave by 10 minutes

- **Badge:** Rx · Load management
- **Why:** Three chillers and autoclave heat started in the same window and pushed the incomer past the demand peak. Hold the second start a few minutes. No classified-zone setpoint change.
- **Impact:** ₹1.8-3.2L / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/pharma.html`

#### B6. Turn down Suite 3 HVAC when no batch is running

- **Badge:** Rx · HVAC idle
- **Why:** AHUs at full flow with no batch occupancy. Schedule adjustment only. No setpoint change in classified zones.
- **Impact:** ₹70k-1.1L / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/pharma.html`

#### B7. Hold the second large feeder start until the first load settles (for example under 95% of its ramp). Usual stagger: 8–12 minutes inside the open MD window.

- **Badge:** Rx · Agnostic · MD
- **Why:** Two heavy feeders started in the same billing slot and stacked on the HT incomer. The monthly bill shows the peak later — not which machines overlapped while the window was still open.
- **Impact:** ₹80,000–₹1.2L / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/prescriptions-examples.html`

#### B8. Start gravure dryer warm-up 25 minutes earlier into the lower MGVCL ToD window before day-shift gravure release, without changing job start time.

- **Badge:** Rx · ToD / warm-up
- **Why:** Warm-up load overlaps the peak ToD band on three of five weekday gravure runs, even when production volume is stable.
- **Impact:** ₹35,000–₹55,000 / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/prescriptions-examples.html`

#### B9. Inspect Compressor 2 inlet filter and unload valve during the next approved low-load window. Use Compressor 1 as standby only if available capacity is confirmed.

- **Badge:** Rx · Equipment · drift
- **Why:** Specific power is 14% above its eight-week baseline for matched header pressure, run hours, and shift load. The drift has persisted for nine days.
- **Impact:** ₹45,000–₹70,000 / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/prescriptions-examples.html`

#### B10. When packaging line output is zero for 20 minutes, switch off tagged auxiliaries (conveyors, idle fans, non-critical pumps). Restart when production pulse returns or supervisor overrides.

- **Badge:** Rx · Idle auxiliaries
- **Why:** Auxiliaries stay on during idle because production count and machine power are not watched together in time.
- **Impact:** ₹50,000–₹90,000 / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/prescriptions-examples.html`

#### B11. Delay batch chiller pull until 90 minutes before batch start (instead of 150 min early), when validated temp band allows — batch hall still hits temperature before start.

- **Badge:** Rx · Batch chiller
- **Why:** Pre-cooling runs through the peak ToD block while the batch hall is still empty — kWh you can shift to shoulder rate without missing batch readiness.
- **Impact:** ₹40,000–₹75,000 / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/prescriptions-examples.html`

#### B12. On a planned cast or roll delay longer than 45 minutes, reduce furnace holding power per melt-shop SOP (controlled ramp to hold-safe). Do not leave full holding kW with zero heats.

- **Badge:** Rx · Furnace holding
- **Why:** Holding power with no cast or roll on three of the last five delay events burned kWh the shift did not need — delay flags and furnace kW are rarely joined in time for the supervisor to act.
- **Impact:** ₹60,000–₹1.0L / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/prescriptions-examples.html`

#### B13. Hold Raw Mill 2 start until Kiln 1 load settles (for example under 95% of ramp) or ~10 minutes pass. Prefer available WHR over peak grid import when WHR is online.

- **Badge:** Rx · Kiln + mill
- **Why:** Kiln and mill co-start in the morning peak window pushed rolling MD up while WHR sat under-used — EMS often shows kiln, mill, WHR, and incomer on separate screens.
- **Impact:** ₹50,000–₹90,000 / month [illustrative] MD + peak import — treat as illustrative unless labelled locked
- **Source:** `demo-decks/prescriptions-examples.html`

#### B14. Trim chiller duty when batch hall occupancy is zero for the idle window, using approved setback set-points only (temp/RH/ACH). Auto-revert on batch start or env alarm.

- **Badge:** Rx · Chiller trim
- **Why:** Full chiller duty runs across empty batch blocks — validation worry and split BMS ownership mean no timed, zone-specific setback with an owner when the area is actually empty.
- **Impact:** ₹45,000–₹85,000 / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/prescriptions-examples.html`

#### B15. Inspect CW pump P-12 bypass / recirc valve and VFD set-point during next low-load window. Trim or close bypass per skid SOP; keep min-flow protection for critical users.

- **Badge:** Rx · Pump recirc
- **Why:** Pump power stayed high for 40+ minutes while header pressure was above set-point and process demand was low — likely open recirc, not more useful flow.
- **Impact:** ₹25,000–₹55,000 / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/prescriptions-examples.html`

#### B16. Stagger furnace and mill start by 8 minutes

- **Badge:** Rx · MD coincidence
- **Why:** Furnace restart and mill bite stacked in the same demand window. The incomer saw the peak; the floor never got a named stagger with a rupee figure.
- **Impact:** ₹2.5-4.5L / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/steel.html`

#### B17. Cut furnace holding on delays longer than 30 minutes

- **Badge:** Rx · Idle / holding
- **Why:** Furnace held at full power through delays with no cast or roll scheduled. Cut holding when the delay passes the agreed window.
- **Impact:** ₹1-1.8L / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/steel.html`

#### B18. Stagger Press Line 1 start versus SQF furnace preheat by 10-12 minutes at day-shift start. Hold the second start until the first load settles.

- **Badge:** Rx · Energy · MD
- **Why:** Press ramp and furnace preheat stacked in the same MD window. The incomer saw the peak; the floor never got a named stagger with a rupee figure.
- **Impact:** ₹45k-70k / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/auto-forge-ht.html`

#### B19. Stagger extrusion start versus compressor and chiller start by 10 minutes at handover. Hold the second start until the first load settles.

- **Badge:** Rx · Energy · MD
- **Why:** Extrusion start and plant air stacked in the same MD window. The incomer saw the peak; the floor never got a named stagger with a rupee figure.
- **Impact:** ₹45k-70k / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/lohia-corp-brief.html`

#### B20. Stagger machine-acceptance trials versus compressor and chiller start by 10 minutes at handover. Hold the second start until the first load settles.

- **Badge:** Rx · Energy · MD
- **Why:** Test-bay load and plant air stacked in the same MD window. The incomer saw the peak; the floor never got a named stagger with a rupee figure.
- **Impact:** ₹45k-70k / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/machinery-oem/index.html`

#### B21. After the last warehouse dispatch for the night, switch warehouse cooling to the approved idle setpoints. Keep production halls unchanged. Revert before the first inbound of the morning.

- **Badge:** Rx · Energy · idle HVAC
- **Why:** Cooling stays on full duty after trucks leave on four of the last six weekday nights, even when the warehouse is quiet.
- **Impact:** 45,000-70,000 rupees / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/nestle-pantnagar-technical/index.html`

#### B22. Start process dryer warm-up 25 minutes earlier into the lower utility ToD window before day-shift production release, without changing job start time.

- **Badge:** Rx · ToD / warm-up
- **Why:** Warm-up load overlaps the peak ToD band on three of five weekday runs, even when production volume is stable.
- **Impact:** ₹35,000-₹55,000 / month [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/technical-explainer.html`

### Floor phone (__FLOOR_RX__)

#### B23. Stagger mill start and kiln fans by 10 min

- **Badge:** Floor · High
- **Why:** MD peak from Monday overlap
- **Impact:** ₹3-5L/mo on MD line [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/cement.html`

#### B24. Raise WHR draw in the ToD peak window

- **Badge:** Floor · High
- **Why:** Peak grid import while WHR capacity sits idle
- **Impact:** ₹1.2-2.4L/mo on ToD line [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/cement.html`

#### B25. Stage idle mill offline on kiln stop

- **Badge:** Floor · Med
- **Why:** Mill left online across kiln stop with no clinker pull
- **Impact:** ₹0.8-1.5L/mo on energy [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/cement.html`

#### B26. Stagger chillers and autoclave by 10 min

- **Badge:** Floor · High
- **Why:** MD peak from Monday load overlap
- **Impact:** ₹1.8-3.2L/mo on MD line [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/pharma.html`

#### B27. Set back AHU Suite 3 in idle window

- **Badge:** Floor · High
- **Why:** Full duty HVAC with no batch occupancy
- **Impact:** ₹0.7-1.4L/mo on energy [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/pharma.html`

#### B28. Stage utility island off across changeover

- **Badge:** Floor · Med
- **Why:** Non-critical loads left on between batches
- **Impact:** ₹0.5-1.1L/mo on energy [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/pharma.html`

#### B29. Stagger furnace and mill start by 8 min

- **Badge:** Floor · High
- **Why:** MD peak from Monday overlap
- **Impact:** ₹2.5-4.5L/mo on MD line [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/steel.html`

#### B30. Cut furnace holding on planned delay

- **Badge:** Floor · High
- **Why:** Holding power during cast delay with no production
- **Impact:** ₹1.5-2.8L/mo on energy [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/steel.html`

#### B31. Shift non-critical load off peak tariff

- **Badge:** Floor · Med
- **Why:** Peak grid draw that can move to shoulder
- **Impact:** ₹0.9-1.8L/mo on ToD [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/steel.html`

#### B32. Stagger Press Line 1 start versus SQF furnace preheat by 10-12 min

- **Badge:** Floor · High
- **Why:** Press and furnace overlapped in the same MD window
- **Impact:** ₹0.8-1.2L/mo on MD line [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/auto-forge-ht.html`

#### B33. Inspect Compressor 2 inlet filter and unload valve

- **Badge:** Floor · Med
- **Why:** Specific power 14% above eight-week baseline for matched header pressure and shift load; persisted nine days
- **Impact:** ₹45k-70k/mo if curve returns to baseline [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/auto-forge-ht.html`

#### B34. Shift gravure dryer warm-up into lower ToD window

- **Badge:** Floor · Med
- **Why:** Warm-up load overlaps MGVCL peak ToD on three of five weekday gravure runs
- **Impact:** ₹35-55k/mo [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/itc-nadiad-technical/index.html`

#### B35. Stagger extrusion versus compressor / chiller start by 10 min

- **Badge:** Floor · High
- **Why:** Extrusion start and plant air overlapped in the same MD window
- **Impact:** ₹0.8-1.2L/mo on MD line [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/lohia-corp-brief.html`

#### B36. Stagger machine trials versus compressor / chiller start by 10 min

- **Badge:** Floor · High
- **Why:** Test bay and plant air overlapped in the same MD window
- **Impact:** ₹0.8-1.2L/mo on MD line [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/machinery-oem/index.html`

#### B37. Switch warehouse cooling to idle after last dispatch

- **Badge:** Floor · High
- **Why:** Cooling stays on full duty after trucks leave on four of six weekday nights, even when the warehouse is quiet
- **Impact:** 45-70k rupees/mo if idle setpoints hold [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/nestle-pantnagar-technical/index.html`

#### B38. Shift dryer warm-up into lower ToD window

- **Badge:** Floor · Med
- **Why:** Warm-up load overlaps peak ToD on three of five weekday production runs
- **Impact:** ₹35-55k/mo [illustrative] — treat as illustrative unless labelled locked
- **Source:** `demo-decks/clients/technical-explainer.html`

