# ABB OPTIMAX vs Stamped — plain English

## In one sentence
ABB Ability™ OPTIMAX® is a global **Energy Management and Optimization** suite that monitors a site’s energy, forecasts demand/prices, and can **send optimal setpoints in open or closed loop** to generation, storage, and loads — often paired with ABB Advanced Process Control.

## What they actually do (no jargon)
- Two steps: (1) **Monitoring & reporting** (including ISO 50001-style reports); (2) **Control & optimisation** — day-ahead and intraday schedules, then real-time balancing of supply and demand.
- Can run **open-loop** (advise suggests setpoints) or **closed-loop** (software writes setpoints to controllable assets: generators, batteries, chargers, loads).
- Uses AI / AutoML-style forecasting of load, generation, and energy prices as input to the optimiser.
- Industrial Sites package orchestrates multi-asset sites and microgrids; other packages cover steam & power, oil & gas, virtual power plants, hydrogen, data centres, etc.
- Can participate in energy markets / demand response when conditions favour selling surplus.
- Deploy as SaaS, cloud, edge, on-prem, or hybrid (OPTIMAX 7.0 emphasises managed SaaS + Kubernetes).
- Global industrial buyer; public pages are **not** packaged around Indian DISCOM Time-of-Day / Maximum Demand billing quirks.
- Vendor claims up to ~10% energy cost reduction — marketing, not our proof.

## What Stamped already does in the same area
- We already cover the “monitor → decide → assign → verify” story for India HT plants, with EnPI/SEC and compliance evidence enable.
- We already recommend peak / load-band style actions as **Prescriptions with owners**, not as automatic setpoints.
- We already ingest multi-source plant signals; we do **not** claim battery autonomy.
- We already win on India tariff-true ₹ and bill ingest — an area OPTIMAX does not lead with publicly.
- We are explicit: autonomous / silent PLC write is a **non-goal**; human-guided soft writeback is specified later, not shipped.

## What they can do that we cannot (the real gaps)

### Closed-loop real-time setpoint write to plant energy assets
- **What it is:** Optimiser calculates best setpoints and **writes them** to controllable systems, correcting deviations live.
- **Why a plant would care:** Large sites want the energy stack to run itself within safe bands while people focus on production.
- **Software, hardware, or both?** Software + plant control interfaces.
- **Can Stamped add this?** No — category is decision layer overlay, not EMS/EMOS. “Do not build ABB.”
- **Should we?** No. Partner / coexist; ingest their tags into Findings.

### Day-ahead / intraday optimisation + market / flexibility trading
- **What it is:** Schedules from forecasts, prices, and loads; peak avoidance; sell capacity / energy when profitable.
- **Why a plant would care:** Big industrials and microgrids treat energy as a traded commodity, not only a DISCOM bill.
- **Software, hardware, or both?** Software.
- **Can Stamped add this?** No as Stamped core (EMS/VPP platform). Yes with partners for market desks that consume our Findings.
- **Should we?** No core build.

### AI forecasting as the optimiser’s driver
- **What it is:** Auto forecasts of demand, generation, and prices feed closed-loop schedules.
- **Why a plant would care:** Better nominations and less surprise peak cost.
- **Software, hardware, or both?** Software.
- **Can Stamped add this?** Yes as advisory/Lab shadow; No as money-of-record autonomous forecast.
- **Should we?** Keep forecasts in shadow; TOW-P stays baseline of record.

### Virtual Power Plant (VPP) aggregate dispatch
- **What it is:** Control many distributed energy resources as one portfolio for grid services.
- **Why a plant would care:** Portfolio owners monetise flexibility.
- **Software, hardware, or both?** Both.
- **Can Stamped add this?** No — conflicts with EMS non-goal.
- **Should we?** No.

### APC / MPC for boilers, turbines, steam networks
- **What it is:** Advanced Process Control / Model Predictive Control that closes the loop on process variables (combustion, boiler start-up heritage, etc.).
- **Why a plant would care:** Process plants save fuel and stabilise quality with APC — different job from energy Prescriptions.
- **Software, hardware, or both?** Software.
- **Can Stamped add this?** No — becomes an APC company; out of two pillars.
- **Should we?** No.

### Full multi-asset EMOS “energy OS” for the site
- **What it is:** Single pane that orchestrates PV, BESS, EV charging, self-gen, peaks, and markets in closed loop.
- **Why a plant would care:** One vendor for energy control of the whole site.
- **Software, hardware, or both?** Software.
- **Can Stamped add this?** No — replacing EMS is an explicit non-goal. Reading EMOS tags is fine.
- **Should we?** No. Battlecard: we are the decision layer with an ops-cleared ledger, not the setpoint writer.

### Enterprise deploy flexibility at ABB scale
- **What it is:** SaaS / edge / on-prem / hybrid with global support comfort.
- **Why a plant would care:** IT/OT procurement checkboxes for majors.
- **Software, hardware, or both?** Software / ops.
- **Can Stamped add this?** Yes software directionally (we already do edge + cloud).
- **Should we?** Keep deploy options honest; do not use this as an excuse to copy control.

## Bottom line for Stamped
OPTIMAX is a **different category** — respect it as the ceiling on control claims, ignore it as a peer Prescription product. They win “plant energy OS + closed-loop optimisation.” We win “India manufacturer Prescription desk with DISCOM ₹ truth.” Never say we are like OPTIMAX in sales. Partner/coexist; clarify the battlecard; add ISO evidence reports if RFPs demand; never invent their ~10% cost cut as our number.
