# 08 — Beyond-energy action catalog

**Status:** exploration — not a product lock  
**Date:** 2026-09-24  
**Companion:** [`08a-prior-research-landscape.md`](./08a-prior-research-landscape.md) (Phase A prior research)  
**Constraint:** software-only HITL near term; hardware / closed-loop writeback = peer contrast only

---

## 1. Framing / thought experiment

You can pull **software-level data** plants already have (meters, bills, CNC/MTConnect, SCADA, MES, ERP, QMS, CMMS, calendars, Excel, process docs). Stamped’s loop stays:

**data → efficiency decision → assigned action (owner, effort, predicted impact) → human executes → evidence**

Today most shipped prescriptions optimize **energy / tariff ₹**. This catalog asks: **what other operational decisions/actions unlock** when we treat plant efficiency (time, throughput, cost, quality proxies, continuity, capital) as the outcome — including **new families outside** modes 1–13 in `01`.

Prior research (`08a`) already points at dual-wallet hours, continuity levers, ADR-024 management decision classes, and parked production-Rx debates. This file expands that into an explicit action list.

---

## 2. Baseline — what we already prescribe (energy contrast)

These are **not** the ceiling; they are the “already doing” spine so “beyond” is visible.

### 2.1 Six waste-category bands (contract)

| # | Band | Typical decisions / actions |
|---|------|------------------------------|
| 1 | MD / PQ (peak, PF, ToD, CMD) | Stagger co-starts; shift ToD exposure; PF correction; CMD right-size |
| 2 | Furnace / process heat | Reduce soak/hold; setback empty thermal; SEC inspect |
| 3 | Idle / off-shift / baseload | Aux shutdown after idle; off-shift base load cut; (CNC idle co-benefit) |
| 4 | Compressed air | SP drift inspect; leak survey; unload discipline |
| 5 | HVAC / chillers | AHU off-hours; COP degradation inspect |
| 6 | Source mix / dispatch | Realign grid/DG/solar/WHR |

Sources: `finding.json` / `prescription.json` `waste_category`; `01` §4 reframes these as **lever libraries**, not product identity.

### 2.2 Pillar 1 finding → L4 template families (examples)

`md_overlap.stagger_costart.v1`, `tod_exposure.shift_load.v1`, `furnace_holding.reduce_soak.v1`, `idle_load` aux shutdown, `dispatch_gap.realign_source_mix.v1`, PF/CMD variants — see `template_renderer.py` / rulepacks under `incomer`, `tariff`, `furnace`, `idle`, `source_mix`, …

### 2.3 Already adjacent (promote as plant efficiency, not “new physics”)

| Adjacent | Example actions | Efficiency driven |
|----------|-----------------|-------------------|
| Pillar 2 equipment | Inspect/clean/repair; leak; abnormal duty | Uptime + utility cost |
| CNC dual wallet | Kill aux-on-idle; alarm dwell; unattended stop | **Machine minutes** ≠ only kWh |
| Continuity levers (Bhatia) | Handoff wait; HT lot fill; rack util | Throughput / cycle continuity |
| ADR-024 `decision_class` | `maint` vs `mgmt_schedule` / `mgmt_capacity` / `mgmt_cross_dept` | Schedule & capacity decisions with tradeoffs |

**Baseline takeaway:** Moving to plant efficiency is partly **reframing and productizing** band-3 / CNC / continuity / mgmt_* actions — and partly **unlocking new families** when MES/QMS/ERP/docs software data is available.

---

## 3. Software data → efficiency unlock map

Thought experiment: **if this software data is available**, which decision families unlock? (Does not require current L1 to already ingest all of them.)

| Data class | Typical systems / files | Decision families unlocked |
|------------|-------------------------|----------------------------|
| **Meters + bills + tariff** | Modbus/EMS, DISCOM PDF | Energy/tariff levers (baseline); unit ₹ when joined to production |
| **CNC / machine state** | MTConnect, Fanuc FOCAS/MT-LINKi, machine logs | Run/idle/alarm; cycle gaps; aux-on-idle; constraint-cell hours |
| **SCADA / historian tags** | OPC UA, CSV historians | Feeder attribution; utility drift; process signature inspect; setpoint HITL context |
| **MES / production counts** | MES, shop-floor Excel, quantity uploads | Parts/shift; SEC or ₹/piece; bottleneck; scrap rate *if* defect codes exist |
| **ERP** | Orders, BOMs, standard costs, routings | Job priority vs energy/capacity; make-ahead vs overtime; costed action ranking |
| **QMS / quality** | Hold codes, scrap reasons, SPC exports | Scrap Pareto actions; hold release; golden-batch deviation (HITL) |
| **CMMS / maintenance** | Work orders, downtime codes | Align inspect Rx with open WOs; MTTR discipline; avoid duplicate tickets |
| **Shift calendar + logbooks** | Rosters, WhatsApp→structured notes | Off-shift waste; owner assignment; reason codes on rejects |
| **Process docs / drawings / CAM / tooling lists** | PDF/XLSX/PLM exports | Methods freezes; setup reuse; tool-life actions (Process-shaped) |
| **Multi-site schemas** | Same tags/playbooks across plants | Benchmark + reuse same action kernel at plant B |

## 4. Exploratory action / decision catalog

Beyond pure bill/tariff energy. Each row: **operator/manager language** → how it drives efficiency → data → evidence.  
`new-family:*` = outside or wider than current `01` modes 1–13.  
`promote:*` = already adjacent in Stamped (CNC/continuity/ADR) — reframe as plant efficiency.

| ID | Action / operational decision | Efficiency driven | Mechanism | Software data | Evidence | Tag |
|----|------------------------------|-------------------|-----------|---------------|----------|-----|
| A1 | Shut aux / idle machine after N min run-idle | Time + cost | Removes non-productive machine hours and parasitic kWh | CNC/MTConnect or meter+calendar | Idle minutes cut; optional kWh | promote:availability |
| A2 | Clear alarm dwell / abandoned e-stop on constraint cell | Time / throughput | Returns bottleneck capacity | CNC alarms + state | Minutes to clear; parts/shift | promote:availability |
| A3 | Stop unattended long-stop with spindle/aux still drawing | Time + cost | Prevents “ghost running” | CNC state + meter | Idle window closed | promote:availability |
| A4 | Re-sequence jobs so constraint cell never starves | Throughput | Flow > local efficiency | MES/ERP routing + CNC state | Queue time; parts/shift | new-family:flow-capacity |
| A5 | Kill handoff wait (e.g. forge→HT / cell→cell) | Continuity / time | Cross-dept idle is invisible on one meter | Calendar + MES timestamps + meters | Wait minutes; WIP age | new-family:flow-continuity |
| A6 | Fill batch / HT lot / rack before release | Throughput + energy co-benefit | Partial loads destroy hours and SEC | MES lot size + furnace/SCADA | Fill %; cycle count | promote:continuity |
| A7 | Changeover start discipline (ready tooling before stop) | Time | Setup waits dominate OEE loss | CNC stop codes + tooling checklist (soft) | Changeover minutes | new-family:changeover |
| A8 | Shift heavy load into cheaper tariff window *as schedule decision* | Cost + schedule | Same physics as ToD energy Rx, framed as ops plan | Tariff + MES plan + meters | Bill line + on-time | promote:mgmt_schedule |
| A9 | Overtime vs extra shift vs defer job (capacity triage) | Cost + capacity | Explicit tradeoff, not silent energy advice | ERP due dates + constraint hours | On-time %; OT hours | new-family:capacity-triage |
| A10 | Scrap Pareto action: top defect code this week → owner | Quality / cost | Quality often > electricity in plant cost stack | QMS scrap codes + production | Scrap rate; ₹ scrap | new-family:quality-actions |
| A11 | Hold-release decision with evidence pack | Quality / flow | Stops silent WIP death | QMS holds + MES | Hold age; release reason | new-family:quality-actions |
| A12 | Operator-approved setpoint / recipe nudge (HITL only) | Yield / materials / energy | Peers (Fero/Braincube/Green Factory); no DCS write | Historian/MES tags | Spec compliance; unit intensity | new-family:setpoint-hitl |
| A13 | Materials intensity action (air/steam/chem per unit spiked) | Cost / materials | Multi-utility efficiency ≠ electricity-only | Utility meters + production | Intensity trend | new-family:materials-intensity |
| A14 | Unit economics spike: ₹ or kWh per piece → investigate idle mix | Cost / time | Joins energy to output | ProductionRecord + feeders/CNC | ₹/piece or SEC | promote:unit-econ |
| A15 | Signature inspect before weekend (compressor/chiller drift) | Uptime / cost | Guidance from software tags — not vibration PdM SKU | SCADA/meter drift + calendar | Inspect closed; failure avoided (proxy) | promote:maint-signature |
| A16 | Align CMMS WO with Stamped finding (one owner) | Closure / uptime | Avoids double systems | CMMS WO + finding id | WO closed ↔ finding verified | new-family:maint-orchestration |
| A17 | Methods freeze: adopt setup sheet / speeds from best run | Cycle time / cost/part | Process beachhead | Docs/CAM/tooling + CNC cycles | Cycle time delta | new-family:methods-freeze |
| A18 | Tool-life action: change insert at predicted wear window | Cost / quality | Prevents scrap and crash | Tooling list + CNC load/time | Tool changes; scrap | new-family:methods-freeze |
| A19 | Multi-site: replay idle/MD playbook that worked at plant A | Portfolio efficiency | Same kernel, less PE heroics | Shared schema + mode history | Sites with same playbook | promote:multi-site |
| A20 | Assign → escalate → verify (closure action on any finding) | Closure rate | Multiplies all families | Workflow + notify | Closure % | promote:closure |
| A21 | Capex triage: defer purchase if hours wallet shows headroom | Capital | Uses utilization truth | Feeder/CNC hours + nameplate | Hours used vs claim | promote:capex-util |
| A22 | Priority: run constraint SKU before non-constraint during peak | Throughput + tariff | Couples capacity and ToD | ERP priority + CNC + tariff | Constraint utilization | new-family:capacity-triage |

**Count:** 22 rows; ≥15 beyond pure bill/tariff energy. Energy baseline actions (MD stagger, PF, pure ToD shift without ops framing) intentionally omitted here — see §2.

---
