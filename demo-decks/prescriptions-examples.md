# Stamped · Practical prescription examples

**Sample numbers only.** Use these in client talks. Live prescriptions use your plant tags, tariff, and a locked M&V baseline.

A **prescription** is a clear **floor action**: what to do, why the data says so, who owns it, effort and window, and how we check the result. Rx must be **operationally feasible** — if the first suggested window conflicts with standby capacity or an active order, Stamped proposes the **next-best slot** (negotiation), not a generic alarm.

**Plain language on the card.** Talk tracks and card fronts use plant-floor words. Technical proof (tags, baseline, tariff band) lives on **flip for evidence** — for the engineer who asks “how do you know?”

HTML deck: [prescriptions-examples.html](./prescriptions-examples.html). Client narrative SSOT: [Stamped_Client_Positioning_and_Narrative_v1.md](../technical/product/Stamped_Client_Positioning_and_Narrative_v1.md).

---

## How to use in a meeting

1. Pick **one load** example (MD stagger, ToD warm-up, idle aux, or batch chiller) and **one equipment** example (compressor drift or pump check).
2. Read the **talk track** aloud — if it sounds like a spec, skip it.
3. Walk **What → Why → Owner → Due**, then **flip for evidence**.
4. Say figures are **`[illustrative]`** until M&V baseline is locked on their plant.

---

## How we constrain ourselves (agents + L4/L6)

| Constraint | Do |
| --- | --- |
| No vague actions | “Inspect C2 inlet filter in next low-load window” not “improve compressor efficiency” |
| Honest effort | hours, permits, production sign-off |
| Illustrative ₹ until locked | label sample ranges; lock at Rx issue for M&V |
| Role + department owners | never orphan “maintenance” |
| Feasibility check | orders, standby capacity, department graph before final Due |
| Evidence on flip | tags, baseline window, tariff band — supervisor can defend |
| Do not claim | vibration PdM, RUL %, “fine-tuned before connect”, MES scheduling |

---

## Catalog (10 sample types)

| # | Badge | Title | Lever |
| --- | --- | --- | --- |
| 1 | Agnostic · MD | Hold the second feeder start 10 minutes | Load staggering |
| 2 | Agnostic · ToD / thermal | Gravure dryer warm-up 25 min earlier | ToD + thermal timing |
| 3 | Equipment · drift | Inspect Compressor 2 filter / unload valve | Equipment drift |
| 4 | Agnostic · idle | Switch off packaging line aux when nothing runs 20 min | Idle-load reduction |
| 5 | Agnostic · ToD | Start batch chiller later — batch still on time | Utility scheduling + ToD |
| 6 | Shared context | Schedule negotiation vignette | Agentic feasibility |
| 7 | Steel | Reduce furnace holding when roll delayed 45+ min | Thermal / idle holding |
| 8 | Cement | Start the mill after the kiln settles | Stagger + WHR preference |
| 9 | Pharma | Trim chillers when the batch hall is empty | Utility scheduling / HVAC |
| 10 | Equipment · pumps | Check CW pump P-12 — valve may be stuck recirculating | Inspect / tune |

---

## 1 · Hold the second feeder start 10 minutes

**Type:** Agnostic · MD · **Priority:** High

#### Talk track

Two big loads hit your incomer in the same 15-minute MD window — the bill won’t tell you which machines until it’s too late. We can see the overlap live and ask the second owner to wait about ten minutes.

#### Card

| Field | Content |
| --- | --- |
| **What** | Hold the second large feeder start until the first load settles (for example under 95% of its ramp). Usual stagger: **8–12 minutes** inside the open MD window. |
| **Why** | Two heavy feeders started in the same billing slot and stacked on the HT incomer. The monthly bill shows the peak later — not which machines overlapped while the window was still open. |
| **Owner** | Electrical lead + area supervisor · active shift |
| **Impact** | Roughly ₹80k–₹1.2L/month on MD `[illustrative]` |
| **Effort** | Sequence change · no new equipment |
| **Due** | Next morning ramp · before peak week |

**Use when:** Any plant with multiple large feeders on one incomer.

#### Evidence (flip)

| Tag | Value | Window |
| --- | --- | --- |
| `HT_INCOMER.MD` | 1,180 kVA | 07:14–07:18 |
| `FEEDER_A.RESTART` | TRUE | 07:12 |
| `FEEDER_B.START` | ON | 07:14+ |
| `AUX_BANK.RUN` | ON | 07:13+ |

Baseline: Apr peak week · MD slab · Stamped check: co-start inside rolling 15-min window.

---

## 2 · Gravure dryer warm-up 25 min earlier

**Type:** Agnostic · ToD / thermal · **Priority:** Med · **Canonical**

#### Talk track

Warm-up is eating peak ToD even when output is the same — shift warm-up, not production start. Start the gravure dryer 25 minutes earlier into the cheaper window; jobs still release on time.

#### Card

| Field | Content |
| --- | --- |
| **What** | Start gravure dryer warm-up **25 minutes earlier** into the lower MGVCL ToD window before day-shift gravure release — **without changing job start time**. |
| **Why** | Warm-up load overlaps the peak ToD band on three of five weekday gravure runs, even when production volume is stable. |
| **Owner** | Utilities lead + gravure shift supervisor |
| **Impact** | Roughly ₹35k–₹55k/month on ToD energy `[illustrative]` |
| **Effort** | Schedule change only · production sign-off |
| **Due** | Next gravure day-shift cycle |

**Use when:** Printing, packaging, gravure, or any thermal warm-up before release.

#### Evidence (flip)

| Tag | Value | Window |
| --- | --- | --- |
| `TARIFF.TOD_BLOCK` | PEAK during warm-up | Mon–Fri avg |
| `DRYER.kW` | elevated | 25 min pre-release |
| `GRAVURE.RELEASE` | unchanged | shift start |
| `HT_INCOMER.kW` | +120 kW vs shoulder | warm-up overlap |

Baseline: last 4 gravure weeks · MGVCL ToD schedule · warm-up vs release timestamp.

---

## 3 · Inspect Compressor 2 filter / unload valve

**Type:** Equipment · drift · **Priority:** High · **Canonical**

#### Talk track

Compressor 2 is using more power than usual for the same air pressure — nine days straight. Inspect before it becomes extra bill and a breakdown.

#### Card

| Field | Content |
| --- | --- |
| **What** | Inspect Compressor 2 inlet filter and unload valve during the next approved low-load window. Use Compressor 1 as standby only if available capacity is confirmed. |
| **Why** | Compressor 2 is working harder than its own recent baseline for the same header pressure and shift load — drift for nine days. |
| **Owner** | Utilities lead + mechanical maintenance |
| **Impact** | Roughly ₹45k–₹70k/month on the air system `[illustrative]` |
| **Effort** | ~2 hours · subject to isolation and permit |
| **Due** | Next approved low-load maintenance window |

**Use when:** Compressed air, any multi-unit house with metered compressors.

#### Evidence (flip)

| Tag | Value | Window |
| --- | --- | --- |
| `COMP2.kW` | +14% vs matched baseline | 9-day trend |
| `HEADER.BAR` | matched band | same runs |
| `COMP2.SPEC_PWR` | elevated | 8-week baseline |
| `COMP2.RUN_HRS` | normal | same |

Baseline: eight-week matched specific-power · same header pressure and run hours.

---

## 4 · Switch off packaging line aux when nothing runs 20 min

**Type:** Agnostic · idle · **Priority:** Med-High

#### Talk track

Conveyors and fans stay on when the line is empty — nobody connects “no output” to aux power in real time. After 20 minutes with zero output, switch aux off per SOP; bring back when production returns.

#### Card

| Field | Content |
| --- | --- |
| **What** | When packaging line output is zero for **20 minutes**, switch off tagged auxiliaries (conveyors, idle fans, non-critical pumps). Restart when production pulse returns or supervisor overrides. |
| **Why** | Auxiliaries stay on during idle because production count and machine power are not watched together in time. |
| **Owner** | Area supervisor · packaging line + utilities lead |
| **Impact** | Roughly ₹50k–₹90k/month on energy `[illustrative]` |
| **Effort** | Idle SOP · safety loads on protect list |
| **Due** | Next idle window of 20 min or more |

**Use when:** Packaging, FMCG, any line with clear output counter + aux feeders.

#### Evidence (flip)

| Tag | Value | Window |
| --- | --- | --- |
| `LINE.OUTPUT` | 0 | 22+ min avg |
| `AUX_CONV.kW` | 38 kW | same |
| `AUX_FAN.RUN` | ON | same |
| `IDLE.FLAG` | TRUE | planned / unplanned |

Baseline: last 5 idle events · flat/ToD energy tariff.

---

## 5 · Start batch chiller later — batch still on time

**Type:** Agnostic · ToD · **Priority:** High

#### Talk track

You’re cooling for a batch that doesn’t start for 90 minutes — that’s peak-rate power you can move. Start the batch chiller later; batch hall still hits temperature before start.

#### Card

| Field | Content |
| --- | --- |
| **What** | Delay batch chiller pull until **90 minutes before** batch start (instead of 150 min early), when validated temp band allows. |
| **Why** | Pre-cooling runs through the peak ToD block while the batch hall is still empty — kWh you can shift to shoulder rate without missing batch readiness. |
| **Owner** | Utilities lead + batch hall supervisor |
| **Impact** | Roughly ₹40k–₹75k/month on ToD energy `[illustrative]` |
| **Effort** | Schedule change · quality sign-off on temp band |
| **Due** | Next scheduled batch in peak block |

**Use when:** Pharma, food, any batch hall with pre-cool before batch start.

#### Evidence (flip)

| Tag | Value | Window |
| --- | --- | --- |
| `TARIFF.TOD_BLOCK` | PEAK | pre-batch window |
| `CHILLER.kW` | 180 kW | 90 min early pull |
| `BATCH.START` | T+90 min | scheduled |
| `HALL.TEMP` | in band at start | historical |

Baseline: last 4 batch cycles · DISCOM ToD schedule · hall temp at batch start.

---

## 6 · Schedule negotiation vignette

**Type:** Shared context · not a full Rx · **Priority:** —

#### Talk track

We suggested Tuesday inspection but standby air was too low — so we moved it to Thursday after Job 447 closes. That’s negotiation, not a new alarm.

#### Narrative

> Compressor 2 filter inspection was suggested for **Tuesday 9–11 am**, but standby air capacity that day is too low to isolate safely. Stamped flags that and proposes **Thursday 2–4 pm** instead, after **Job 447** closes.

| Before | After |
| --- | --- |
| **Due:** Tue 9–11 am | **Due:** Thu 2–4 pm after Job 447 |
| **Blocker:** standby air below isolation threshold | **Feasible:** production order cleared · standby confirmed |

Bounded negotiation ([ADR-024](../decisions/024-026/ADR-024-holistic-plant-decisions.md)): revise window and parameters, not rewrite the Rx from scratch.

**Use when:** Explaining agentic layer vs static CMMS work orders.

---

## 7 · Reduce furnace holding when roll is delayed 45+ min

**Type:** Steel · melt shop · **Priority:** Med-High

#### Talk track

Holding power keeps running through a delay — the melt schedule and furnace kW aren’t looked at together until the shift ends. On a 45+ minute roll delay, cut holding per melt-shop SOP.

#### Card

| Field | Content |
| --- | --- |
| **What** | On a planned cast or roll delay **longer than 45 minutes**, reduce furnace holding power per melt-shop SOP (controlled ramp to hold-safe). Do not leave full holding kW with zero heats. |
| **Why** | Holding power with no cast or roll on three of the last five delay events burned kWh the shift did not need. |
| **Owner** | Melt-shop supervisor · Furnace 2 + utilities lead |
| **Impact** | Roughly ₹60k–₹1.0L/month on energy `[illustrative]` |
| **Effort** | Holding SOP · note restart lead time before cast resumes |
| **Due** | Next delay window over 45 min |

**Use when:** Steel melt shop, EAF / holding furnaces with production delay flags.

#### Evidence (flip)

| Tag | Value | Window |
| --- | --- | --- |
| `FURNACE2.HOLD` | ON | 48 min avg |
| `ROLL.PROD` | 0 | same window |
| `FURNACE2.kWh` | ~180 kWh | per event |
| `DELAY.FLAG` | TRUE | planned |

Baseline: last 5 delay events · ToD energy · normal hold profile.

---

## 8 · Start the mill after the kiln settles

**Type:** Cement · pyro + grinding · **Priority:** High

#### Talk track

Kiln and mill ramp together every morning — that’s when demand and peak grid import hurt. Hold the mill start ~10 minutes until the kiln settles; use WHR when it’s available instead of peak grid.

#### Card

| Field | Content |
| --- | --- |
| **What** | Hold **Raw Mill 2** start until **Kiln 1** load settles (for example under 95% of ramp) or ~10 minutes pass. Prefer available **WHR** over peak grid import when WHR is online. |
| **Why** | Kiln and mill co-start in the morning peak window pushed rolling MD up while WHR sat under-used. |
| **Owner** | CCR / pyro supervisor + electrical lead · Shift B |
| **Impact** | Roughly ₹50k–₹90k/month MD + peak import `[illustrative]` |
| **Effort** | Sequence + dispatch · no new equipment |
| **Due** | Next morning ramp · before peak week |

**Use when:** Cement, lime, or any pyro + grind with WHR.

#### Evidence (flip)

| Tag | Value | Window |
| --- | --- | --- |
| `KILN1.LOAD_PCT` | 108% | 09:40 |
| `RAWMILL2.START` | ON (co-start) | 09:40 |
| `HT_INCOMER.MD` | 4,680 kVA | rolling 15-min |
| `WHR.AVAIL_kW` | 1,100 under-used | same |

Baseline: peak week morning ramp · TOD + MD · WHR availability log.

---

## 9 · Trim chillers when the batch hall is empty

**Type:** Pharma · batch utilities · **Priority:** Med

#### Talk track

Full chiller run on an empty batch block — utilities can trim within your approved temperature band. Setback when hall is empty; auto-revert when batch starts.

#### Card

| Field | Content |
| --- | --- |
| **What** | Trim chiller duty when batch hall occupancy is zero for the idle window, using **approved setback set-points** only (temp/RH/ACH). Auto-revert on batch start or env alarm. |
| **Why** | Full chiller duty runs across empty batch blocks because validation worry and split BMS ownership — no timed, zone-specific setback with an owner. |
| **Owner** | Utilities / HVAC lead · Block C + batch supervisor |
| **Impact** | Roughly ₹45k–₹85k/month on energy `[illustrative]` |
| **Effort** | Validated setback SOP · no free-text set-point changes |
| **Due** | Next confirmed idle batch window |

**Use when:** Pharma, biotech, regulated batch halls with validated env envelope.

#### Evidence (flip)

| Tag | Value | Window |
| --- | --- | --- |
| `BATCH.OCCUPANCY` | 0 | 4 / 6 windows |
| `CHILLER.DUTY` | FULL | same |
| `ZONE.TEMP_RH` | in band | continuous |
| `CHILLER.kW` | +42 kW vs setback | per idle hour |

Baseline: validated env envelope · last 6 idle windows · energy tariff.

---

## 10 · Check CW pump P-12 — valve may be stuck recirculating

**Type:** Equipment · pumps · **Priority:** Med

#### Talk track

Pump working harder than needed for the same flow — a two-hour mechanical check, not a vibration project. Valve may be stuck open at partial recirc.

#### Card

| Field | Content |
| --- | --- |
| **What** | Inspect CW pump **P-12** bypass / recirc valve and VFD set-point during next low-load window. Trim or close bypass per skid SOP; keep min-flow protection for critical users. |
| **Why** | Pump power stayed high for 40+ minutes while header pressure was above set-point and process demand was low — likely open recirc, not more useful flow. |
| **Owner** | Area supervisor · pump skid + mechanical maintenance |
| **Impact** | Roughly ₹25k–₹55k/month on energy `[illustrative]` |
| **Effort** | ~2 hours mechanical check · no new equipment |
| **Due** | Next confirmed overpressure window or scheduled maint slot |

**Use when:** Utility pumps, cooling water, any VFD pump with bypass/recirc.

#### Evidence (flip)

| Tag | Value | Window |
| --- | --- | --- |
| `P12.HEADER_BAR` | high vs set-point | 42 min |
| `P12.BYPASS` | OPEN ~40% | same |
| `PROC.DEMAND` | low | same |
| `P12.kW` | +18% vs trimmed | same |

Baseline: skid matched-flow profile · 30-day pump baseline.

---

## How to use these with a client

1. Pick **one agnostic** and **one plant/equipment** example that matches their site.
2. Read **talk track** → walk **What → Why → Owner → Due** → flip for evidence.
3. Stress **owner + department + M&V lock**. Do not lead with a vague savings claim.
4. Say clearly: figures are **samples**. A live audit binds tags, tariff, and baseline to *their* plant.

Companion deck (flip cards, keyboard nav): [`prescriptions-examples.html`](./prescriptions-examples.html)
