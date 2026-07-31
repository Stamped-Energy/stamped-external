# Stamped · Client prescription examples

**Sample numbers only.** Use these in client talks. Live prescriptions use your plant tags, tariff, and a locked M&V baseline.

A **prescription** is a clear floor action: what to do, why the data says so, who owns it, which bill line it hits, and how we check the result. These only fire when Stamped watches **many live signals together** (incomer, machine state, tariff clock, and production or idle) in the short window when a decision can still change the bill.

| # | Type | Prescription |
|---|------|----------------|
| 1 | Agnostic | MD co-start stagger |
| 2 | Agnostic | ToD peak load shift |
| 3 | Agnostic | Idle auxiliary cut |
| 4 | Agnostic | Contract demand soft-landing |
| 5 | Steel | Furnace holding cut on delay |
| 6 | Cement | Kiln + mill stagger / prefer WHR |
| 7 | Pharma · utilities | HVAC idle-duty drop |
| 8 | Equipment · compressors | Multi-unit sequencing |
| 9 | Equipment · chillers | Approach / condenser waste |
| 10 | Equipment · pumps | Overpressure recirculation trim |

---

## Agnostic (works on most plants)

### 1 · MD co-start stagger

**Type:** Agnostic · **Priority:** High · **Bill line:** MD (kVA)

#### What
Hold the second big feeder start until the first load settles (for example under 95% of its ramp). Then release it. Usual stagger is **8-12 minutes** inside the open 15-minute MD window.

#### Why
Two heavy feeders started in the same billing slot and stacked on the HT incomer. The monthly bill only shows the peak later. It cannot tell Shift B *which two machines* overlapped *while the window was still open*. You need live feeder starts plus rolling MD.

#### How
1. Spot a co-start (or a second start about to happen) on tagged large feeders.
2. Tell the second owner to hold, with the settle level and minutes left in the MD window.
3. Release when the first feeder drops below the settle level, or log an override if the window closes.
4. Log accept / snooze / override for M&V.

| | |
|---|---|
| **Owner** | Electrical / area supervisor · active shift |
| **Impact (sample)** | ₹2.5-4.5L / month on MD |
| **Effort** | Sequence change · no new equipment |
| **Rule** | `md_overlap@v2.4` · High |
| **Due** | This week · before next peak week |

**Why you need live data:** Rolling MD is set in 15 minutes or less. You need restart flags, incomer MD, and feeder ID *inside that window*. A week-later EMS report is too late.

**Evidence (sample · Mon 07:10-07:22)**

| Tag | Value | Window |
|-----|-------|--------|
| `HT_INCOMER.MD` | 1,180 kVA | 07:14-07:18 |
| `FEEDER_A.RESTART` | TRUE | 07:12 |
| `FEEDER_B.START` | ON | 07:14+ |
| `AUX_BANK.RUN` | ON | 07:13+ |

**Cite:** `physics/md_overlap@v2.4` · model conf 0.91 · tariff MD slab · baseline Apr peak week  
**M&V:** Check next bill MD peak against the locked baseline. Plan locked when the Rx is issued.

---

### 2 · ToD peak load shift

**Type:** Agnostic · **Priority:** High · **Bill line:** ToD energy (₹/kWh peak)

#### What
Move loads you can pause (batch utilities, non-critical auxiliaries, deferrable test loads) **off the peak tariff block** when the process allows. Usually shift them into shoulder or off-peak in the same shift.

#### Why
The plant is buying peak-rate power while tagged pause-able loads are still on and the process is fine. A fixed “run at night” plan misses days when you could move earlier, or forces a move when you should not. Live tariff clock + process ready + incomer draw decide *today’s* move.

#### How
1. At peak start (or 15 min before), list pause-able loads against process and quality rules.
2. Send a ranked cut/shift list with ₹/kWh savings vs leaving them on.
3. Supervisor accepts the list or protects named loads. Stamped watches to bring them back when peak ends.
4. Close on the ToD bill line vs the locked baseline week.

| | |
|---|---|
| **Owner** | Electrical lead · Shift A |
| **Impact (sample)** | ₹0.9-1.8L / month on ToD |
| **Effort** | Dispatch nudge · SOP protect-list |
| **Rule** | `tod_interruptible@v1.6` · High |
| **Due** | Next peak tariff window |

**Why you need live data:** Peak price changes by the clock, and by whether the process can take a cut *right now*. Monthly averages cannot give a same-shift protect list.

**Evidence (sample · peak block 18:00-22:00)**

| Tag | Value | Window |
|-----|-------|--------|
| `TARIFF.TOD_BLOCK` | PEAK | 18:00-22:00 |
| `HT_INCOMER.kW` | 3,420 kW | 18:22 |
| `LOAD.INTERRUPTIBLE_kW` | 480 kW | same |
| `PROC.READY_SCORE` | 0.82 | 18:20 |

**Cite:** `physics/tod_shift@v1.6` · model conf 0.88 · DISCOM ToD schedule · baseline last 4 peak weeks  
**M&V:** Peak-block kWh × tariff delta vs locked plan. Check on next bill ToD lines.

---

### 3 · Idle auxiliary cut

**Type:** Agnostic · **Priority:** Med-High · **Bill line:** Energy (kWh)

#### What
When the main process shows **zero production for N minutes** (plant-set, often 15-30), switch off tagged auxiliaries: conveyors, idle bag filters, idle pumps, non-critical fans. Use a timed SOP, and restart them when production comes back.

#### Why
Auxiliaries stay on during idle because no one watches production count and machine kW together. Month-end energy looks “a bit high,” but the floor never gets a timed cut with an owner. Live trigger: production = 0 *and* aux kW still high.

#### How
1. Confirm production = 0 for at least N minutes and aux feeder still drawing.
2. Send a cut list by asset, with restart rule (production pulse or supervisor override).
3. Keep safety and quality loads on the protect list.
4. Add up avoided kWh for the billing cycle.

| | |
|---|---|
| **Owner** | Area supervisor · owning process |
| **Impact (sample)** | ₹1.0-2.2L / month on energy |
| **Effort** | Idle SOP · no new equipment |
| **Rule** | `idle_aux@v1.9` · High |
| **Due** | Next idle window of N min or more |

**Why you need live data:** Idle waste is time × kW. Monthly totals hide it. You need production and asset power at the same time for each stop.

**Evidence (sample · last 5 idle events)**

| Tag | Value | Window |
|-----|-------|--------|
| `PROC.COUNT` | 0 | 22+ min avg |
| `AUX_CONV.kW` | 38 kW | same window |
| `AUX_FAN.RUN` | ON | same |
| `IDLE.FLAG` | TRUE | planned / unplanned |

**Cite:** `physics/idle_aux@v1.9` · model conf 0.86 · flat/ToD energy · baseline last 5 idles  
**M&V:** Event kWh avoided × tariff. One ledger entry per closed idle cut.

---

### 4 · Contract demand soft-landing

**Type:** Agnostic · **Priority:** High · **Bill line:** MD (kVA) + CMD / penalty risk

#### What
When rolling MD nears the **contract demand (CMD) headroom band** (for example within 5-8%), hold soft loads and delay starts that can wait, *before* the 15-minute window locks. This is a soft landing, not an emergency trip.

#### Why
Plants often see CMD breaches on the bill, or only at 98% with minutes left. Soft-landing needs the MD trend plus a ranked list of loads you can hold *while headroom still exists*. A single-meter alarm without machine context only shouts. It does not say who holds what.

#### How
1. Estimate window-end MD from the current trend and known pending starts.
2. If projected MD enters the headroom band, issue ranked soft holds (lowest production risk first).
3. Block new deferrable starts until the window closes or headroom recovers.
4. Record near-miss vs breach for CMD review.

| | |
|---|---|
| **Owner** | Electrical lead · plant head on breach path |
| **Impact (sample)** | ₹1.5-5.0L / event avoided (MD slab / penalty) |
| **Effort** | Soft-hold SOP · protect critical path |
| **Rule** | `cmd_headroom@v1.3` · Critical |
| **Due** | Live · inside open MD window |

**Why you need live data:** CMD risk is decided inside one rolling window. You need predicted MD, the start queue, and which loads can wait. Yesterday’s peak log is too late.

**Evidence (sample · open 15-min MD)**

| Tag | Value | Window |
|-----|-------|--------|
| `HT_INCOMER.MD_ROLL` | 4,720 kVA | T+6 min |
| `CMD.LIMIT` | 5,000 kVA | contract |
| `MD.HEADROOM_PCT` | 5.6% | live |
| `STARTS.PENDING` | 2 deferrable | queued |

**Cite:** `physics/cmd_softland@v1.3` · model conf 0.90 · CMD contract · baseline peak weeks  
**M&V:** Window-end MD vs what would have happened with no soft hold. CMD breach flag = 0.

---

## Plant / equipment specific

### 5 · Steel · Furnace holding cut on delay

**Type:** Steel · melt shop · **Priority:** Med-High · **Bill line:** Energy (kWh)

#### What
On a **planned cast or roll delay longer than 30 minutes**, cut furnace holding power per melt-shop SOP (controlled ramp to a hold-safe state). Do not leave full holding kW with zero heats.

#### Why
Holding power with no cast or roll on 3 of the last 5 delay events burned kWh you did not need. Delay flags sit in production systems. Furnace kW sits in EMS. Nobody joins them in time for the supervisor to cut hold.

#### How
1. Detect delay over 30 min with cast / roll production = 0.
2. Confirm furnace in HOLD and kW above the hold-cut level.
3. Tell melt-shop supervisor: run holding SOP; note restart lead time before cast resumes.
4. Check event kWh vs the normal hold profile.

| | |
|---|---|
| **Owner** | Melt-shop supervisor · Furnace 2 |
| **Impact (sample)** | ₹1.0-1.8L / month on energy |
| **Effort** | Holding SOP · no new equipment |
| **Rule** | `idle_hold@v1.8` · High |
| **Due** | Next delay window over 30 min |

**Why you need live data:** Delay length and furnace hold state change during the event. A post-shift report cannot get back the kWh already spent.

**Evidence (sample · last 5 delay / hold events)**

| Tag | Value | Window |
|-----|-------|--------|
| `FURNACE2.HOLD` | ON | 35 min avg |
| `CAST.PROD` | 0 heats | same window |
| `FURNACE2.kWh` | ~180 kWh | per event |
| `DELAY.FLAG` | TRUE | planned |

**Cite:** `physics/idle_hold@v1.8` · model conf 0.87 · ToD energy · baseline last 5 delays  
**M&V:** Holding kWh per delay event vs locked SOP baseline.

---

### 6 · Cement · Kiln + mill stagger / prefer WHR

**Type:** Cement · pyro + grinding · **Priority:** High · **Bill line:** MD (kVA) + peak grid energy

#### What
Stagger **Kiln 1** and **Raw Mill 2** start by about 10 minutes into the TOD peak. Prefer available **WHR** over peak grid import when WHR is online and the process allows.

#### Why
Kiln and mill started together in the peak window and pushed rolling MD toward CMD while WHR sat under-used. Cement EMS often logs kiln, mill, WHR, and incomer as separate screens. The overlap and WHR preference only show when all four are watched live together.

#### How
1. On kiln ramp, hold mill start until kiln load settles (for example under 95% of design) or 10 minutes pass with MD headroom.
2. If WHR is available and peak grid import is high, prefer WHR before starting grind load that can wait.
3. Release the mill when MD trend and process allow.
4. Close on MD + peak import vs the locked week.

| | |
|---|---|
| **Owner** | CCR / pyro supervisor · Shift B |
| **Impact (sample)** | ₹84k / mo MD · plus peak energy when WHR preferred |
| **Effort** | Sequence + dispatch · no new equipment |
| **Rule** | `md_overlap@v2.4` + `whr_prefer@v1.2` · High |
| **Due** | This week · before next peak |

**Why you need live data:** Co-start and WHR availability change by the minute. Preferring WHR after the peak block ends does not fix the bill line that already locked.

**Evidence (sample · Tue 09:40 IST)**

| Tag | Value | Window |
|-----|-------|--------|
| `KILN1.LOAD_PCT` | 108% | 09:40 |
| `RAWMILL2.START` | ON | 09:40 (co-start) |
| `HT_INCOMER.MD` | 4,680 kVA | rolling 15-min |
| `WHR.AVAIL_kW` | 1,100 kW under-used | same |

**Cite:** `physics/md_overlap@v2.4` · `whr_prefer@v1.2` · conf 0.89 · TOD + MD · baseline peak week  
**M&V:** Peak MD and peak-block grid import vs co-start with no stagger. Credit WHR MWh.

---

### 7 · Pharma · HVAC idle-duty drop

**Type:** Pharma / batch utilities · **Priority:** Med · **Bill line:** Energy (kWh)

#### What
Drop HVAC from **full duty to idle/setback** when batch occupancy and cleanroom demand show no active batch for a set window (for example 4 of last 6 idle windows), without breaking validated env limits.

#### Why
Full HVAC runs across empty batch blocks because of validation worry and split BMS/SCADA ownership. Energy dashboards show high HVAC kWh. They do not give a *timed, zone-specific* setback with an owner when the area is actually empty.

#### How
1. Confirm occupancy / batch = idle for the zone window, and temp/RH stay inside the validated band.
2. Propose setback set-points (temp/RH/ACH) from the approved SOP list only. No free-text changes.
3. Utilities lead accepts. Auto-revert on batch start or env alarm.
4. Add up HVAC kWh saved vs full duty.

| | |
|---|---|
| **Owner** | Utilities / HVAC lead · Block C |
| **Impact (sample)** | ₹0.8-1.6L / month on energy |
| **Effort** | Validated setback SOP · no new equipment |
| **Rule** | `hvac_idle_duty@v1.4` · Med |
| **Due** | Next confirmed idle batch window |

**Why you need live data:** Occupancy and env band are live. A monthly HVAC intensity number cannot safely allow a setback mid-shift.

**Evidence (sample · last 6 idle windows)**

| Tag | Value | Window |
|-----|-------|--------|
| `BATCH.OCCUPANCY` | 0 | 4 / 6 windows |
| `HVAC.DUTY` | FULL | same |
| `ZONE.TEMP_RH` | in band | continuous |
| `HVAC.kW` | +42 kW vs setback | per idle hour |

**Cite:** `physics/hvac_idle@v1.4` · model conf 0.84 · energy tariff · validated env envelope  
**M&V:** HVAC kWh in idle hours × duty delta. No env trips blamed on the setback.

---

### 8 · Compressors · Multi-unit sequencing

**Type:** Equipment · compressed air · **Priority:** High · **Bill line:** Energy (kWh) + peak kW

#### What
Keep **two of three 75 kW VFD compressors** online when header pressure stays in band. Stop or unload the third unit that is running at part-load. Fix sequencing with SOP first. Add PLC + small receiver later if people keep overriding.

#### Why
Three machines stayed online at partial load when two would have met demand. About **130 MWh/year** avoidable. Each compressor follows its own pressure switch. Without live header pressure plus per-unit kW and % load, the floor keeps all three on “to avoid dips.”

#### How
1. Detect 10+ minutes with three units ON and header in 6.5-7.3 bar.
2. Pick the lowest-loaded unit. Stop or unload it under watch, with Lag armed (+30 s).
3. Trial two-unit running. Alarm if all three stay online over 10 min again.
4. Optional later: commission sequencer + receiver after the trial is stable.

| | |
|---|---|
| **Owner** | Utilities supervisor · compressor house |
| **Impact (sample)** | ₹9.0-12.5L / year |
| **Effort** | Sequencing SOP · optional sequencer later |
| **Rule** | `comp_sequence@v2.1` · High |
| **Due** | This week · supervised trial |

**Why you need live data:** Part-load waste is a live header plus three power readings. Monthly compressor kWh cannot tell you *which* unit to stop *this hour*.

**Evidence (sample · 06:30 IST)**

| Tag | Value | Window |
|-----|-------|--------|
| `COMP1.kW` | 43 (57%) | part-load |
| `COMP2.kW` | 54 (72%) | part-load |
| `COMP3.kW` | 68 (91%) | near loaded |
| `HEADER.BAR` | 6.9 in band | same |

**Cite:** `physics/comp_sequence@v2.1` · model conf 0.92 · energy + peak kW · baseline 30-day load profile  
**M&V:** Minutes with 3 units ON at or under 5%. Yearly kWh vs locked baseline.

---

### 9 · Chillers · Approach / condenser waste

**Type:** Equipment · chiller + cooling tower · **Priority:** Med-High · **Bill line:** Energy (kWh)

#### What
When **approach temperature** and condenser temperature rise vs outdoor air go past the plant band, clean the condenser/tower and check fan staging before efficiency drops further. Time the job from live readings, not only from a calendar.

#### Why
Fouling and weak tower staging show up as slow efficiency drift. Operators see “chiller busy.” Energy teams see higher kWh per TR weeks later. Live approach vs design plus outdoor air flags the week to clean *before* the bill.

#### How
1. Flag approach / condenser rise above band for X hours or more while load is above Y%.
2. Send clean + fan-stage check to utilities with a target approach to restore.
3. Re-check efficiency (kW per TR) after the work.
4. Lock the seasonal baseline for the next drift check.

| | |
|---|---|
| **Owner** | Utilities / HVAC · chiller plant |
| **Impact (sample)** | ₹1.2-2.5L / month when fouling is real |
| **Effort** | Cleaning + fan staging · scheduled window |
| **Rule** | `chiller_approach@v1.5` · High |
| **Due** | Next maintenance window within 7 days |

**Why you need live data:** Approach vs outdoor air is continuous. Calendar cleaning misses early fouling. Yearly energy intensity is too late.

**Evidence (sample · 14-day drift)**

| Tag | Value | Window |
|-----|-------|--------|
| `CHILLER1.APPROACH_C` | +2.1 vs design | 14-day |
| `COND.DTdw` | high vs ambient | same |
| `CHILLER1.kW_per_TR` | +12% | vs baseline |
| `CT.FAN_STAGES` | under-staged | peak hours |

**Cite:** `physics/chiller_approach@v1.5` · model conf 0.85 · energy · seasonal baseline  
**M&V:** Approach back in band + kW/TR change after clean vs locked pre-clean week.

---

### 10 · Pumps · Overpressure recirculation trim

**Type:** Equipment · process / utility pumps (VFD) · **Priority:** Med · **Bill line:** Energy (kWh)

#### What
When **header pressure is high**, recirculation / bypass is open, and process demand is low, **trim the VFD set-point** or close bypass so the pump stops wasting power. Keep min-flow protection for critical users.

#### Why
Pumps run hard against an open bypass. Power stays high while useful flow is low. One pump ammeter does not show the bypass + low demand mismatch. Watching several tags together does.

#### How
1. Detect high header pressure + bypass open + low process demand for N minutes or more.
2. Propose VFD trim (lower Hz / bar set-point) or bypass close per SOP, with min-flow protect.
3. Area owner does it under watch. Alarm if pressure drops below band.
4. Measure kWh saved at the same delivered process volume.

| | |
|---|---|
| **Owner** | Area / utilities supervisor · pump skid |
| **Impact (sample)** | ₹0.6-1.4L / month on energy |
| **Effort** | Set-point / bypass SOP · no new equipment |
| **Rule** | `pump_recirc@v1.1` · Med |
| **Due** | Next confirmed overpressure window |

**Why you need live data:** High pressure + open bypass + low demand lasts a short time. End-of-shift logs miss the hours the pump recirculated.

**Evidence (sample · overpressure window)**

| Tag | Value | Window |
|-----|-------|--------|
| `PUMP_A.HEADER_BAR` | high vs set-point | 42 min |
| `BYPASS.POS` | OPEN | same |
| `PROC.DEMAND` | low | same |
| `PUMP_A.kW` | +18% vs trimmed | same |

**Cite:** `physics/pump_recirc@v1.1` · model conf 0.83 · energy · skid baseline  
**M&V:** kWh per delivered m³ (or batch) vs locked trim set-point week.

---

## How to use these with a client

1. Pick **one agnostic** and **one plant/equipment** example that matches their site.
2. Walk **What → Why → How**, then flip (or scroll) to **evidence tags**. That is the “only with live data” moment.
3. Stress **owner + bill line + M&V lock**. Do not lead with a vague savings claim.
4. Say clearly: figures are **samples**. A live audit binds tags, tariff, and baseline to *their* plant.

Companion deck (flip cards, keyboard nav): [`prescriptions-examples.html`](./prescriptions-examples.html)
