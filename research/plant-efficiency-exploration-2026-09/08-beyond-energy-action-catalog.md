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

*(Sections 3+ appended in later commits: software-data map, action catalog, peers, crosswalk, new families.)*
