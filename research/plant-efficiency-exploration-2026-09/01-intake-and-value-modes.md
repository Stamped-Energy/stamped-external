# 01 — Intake → plant efficiency value modes

**Status:** exploration — not a product lock  
**Authority for intake:** L1 Connect & Normalise (pre-build contracts)  
**Frame:** outcomes are efficiency (cost, time, throughput, quality proxies, intensity); energy ₹ is one verification path, not the product boundary.

---

## 1. What we can take in (software connectors, no new hardware)

L1 emits four canonical record types. Path A may add machine state via existing CNC gateways (MTConnect), still software.

| Record | Typical sources | Cadence | Efficiency role |
|--------|-----------------|---------|-----------------|
| **Measurement** | Incomer/feeder meters (Modbus), EMS/historian CSV, MQTT loggers; P1 OPC UA / SCADA / DLMS / solar-DG; P2 MTConnect energy+state, BACnet HVAC | 1 s–15 min | Load, idle, drift, co-start, utility health signatures |
| **BillLine** | DISCOM PDF (parsed + recomputed) | Monthly | Tariff / MD / PF / TOD commercial verification |
| **ProductionRecord** | Manual/XLSX; P1 ERP/MES quantity | Shift/daily | Unit economics, SEC, throughput context |
| **Event + calendar** | Shift calendar, logbooks, connector health | Ad hoc / continuous | Off-shift waste, maintenance windows, orchestration |

**Not in intake today (blocks many peer categories):** vibration/oil multi-sensors, camera streams, defect codes, lab assays, CAM toolpaths, labour rosters, inventory/ASN, CAD/PLM drawings (unless file-upload Process path is built).

---

## 2. Candidate core

**Primary hypothesis:** *data → assigned action → evidence.*

- Detect a regime or opportunity from trusted tags + context.
- Prescribe a specific action with owner, effort, and predicted impact (**₹ and/or minutes and/or units**).
- Human executes (HITL); system verifies with a machine-checkable predicate and/or commercial document.
- Enemy remains **insight without closure** (dashboards that never become owned work).

**Alternate cores (explore, don’t pick here):**

| Core | Peer rhyme | Risk |
|------|------------|------|
| Intelligence of record | Noetive / BrightAI language | Becomes sensing/hardware story |
| See-layer twin / OEE visibility | Sight Machine, MachineMetrics | Dashboard trap |
| Methods freeze packages | Vision v0.3 Process | Needs drawings/tooling data we mostly lack |

---

## 3. Value mode matrix (software-funded)

| # | Mode | Outcome family | Minimum data | Incumbent replaced / improved | Feasibility now |
|---|------|----------------|--------------|-------------------------------|-----------------|
| 1 | Assigned efficiency actions | Cost + time + ops discipline | Measurements + calendar (+ production if available) | Energy-audit PDF; EE Excel; EMS charts without owners | **Strong** — generalize today’s prescribe loop |
| 2 | Load & utility cost levers | Cost (energy/tariff) | Incomer + bill; feeders deepen | Tariff consultant; EMS MD screens | **Strong** |
| 3 | Machine utilization / idle time | Time / throughput | CNC/MTConnect or SCADA run/idle | Whiteboard; MachineMetrics-class OEE sheets | **Strong if Path A CNC/SCADA** |
| 4 | Energy-aware production timing | Time + cost | Shift qty + meters + tariff | Production whiteboard; energy-blind APS | **Partial** — not finite-capacity APS |
| 5 | Unit economics | Cost per piece/ton | ProductionRecord + feeders | Month-end SEC spreadsheet | **Strong with production upload** |
| 6 | Signature-based maintenance guidance | Downtime risk / cost | Meter/SCADA drift + calendar | Breakdown intuition; not CMMS/PdM sensors | **Narrow strong** |
| 7 | Bill / tariff defence | Commercial cost | BillLine + tariff model | Manual bill check | **Strong** |
| 8 | HITL multi-role orchestration | Closure rate | Findings + workflow + notify | WhatsApp chaos; paper WO | **Strong** (productization) |
| 9 | Capex / asset utilization | Capital efficiency | Feeder kW + nameplate + hours | CoE spreadsheet | **Medium** — needs asset graph metadata |
| 10 | Multi-site benchmark | Portfolio efficiency | Same modes × N plants | Group energy CoE | **After multi-site** |
| 11 | Methods / tooling freezes | Cycle time / cost/part / tool life | Drawings, process docs, tooling, machine capability | ChatGPT ad hoc; CAM seats; consultants | **Weak on current L1** — Process-shaped gap |
| 12 | Closed-loop setpoint write | Margin / yield | Historian + DCS write path | Imubit / OPTIMITIVE / APC | **Out** — HITL only near term |
| 13 | Vision QC / robotics | Yield / labour | Cameras / cells | Cognex / Bright Machines | **Out** — hardware |

---

## 4. Six legacy “waste categories” — reframed

Architecture §3 energy bands remain useful **mechanisms**, not the product name:

| Mechanism | Efficiency reading | Typical bill share `[~]` (historical Energy math) |
|-----------|--------------------|--------------------------------------------------|
| MD / PF / TOD | Cost + schedule discipline | 3–8% of bill when closed |
| Furnace / process heat holding | Energy + cycle / batch time | 2–5% |
| Idle / off-shift load | Non-productive hours + kWh | 2–4% |
| Compressed air drift | Utility cost + leak proxy | 1–3% |
| HVAC / chillers | Cost + comfort/process stability | 1–3% |
| Source mix / dispatch | Cost + carbon intensity | 1–4% |

Use these as **lever libraries** under mode 1–2, not as “Stamped = energy.”

---

## 5. Verification beyond the bill

| Evidence type | When |
|---------------|------|
| BillLine / tariff recompute | Commercial energy levers |
| Ops clearance on tags (stabilize window) | Load/idle/compressor fixes |
| Cycle time / parts per shift | Utilization / methods (if measured) |
| Cost per accepted part | Requires scrap/quality input (often missing) |

**Honesty:** do not invent downtime-% or scrap KPIs without L2 signals.

---

## 6. Path A vs Path B (efficiency lens)

| Path | Data | Modes unlocked fast |
|------|------|---------------------|
| **B** — meter + bill + calendar | Incomer, bills, shifts | 2, 7, partial 1, partial 6 |
| **A** — + feeders / SCADA / CNC | Machine attribution | 3, 4, 5, richer 1 and 6 |
| **Process-shaped** — + docs/tooling | Methods freezes | 11 (new connectors / upload product) |

---

## 7. Incumbent map (summary)

- **Monitoring EMS** (Schneider PME, Elmeasure eWatch, SI dashboards) → improve with assigned actions + evidence.
- **India Energy AI** (Greenovative, ZeroWatt) → peers on lever 2/5/7; category is wider than them.
- **OEE platforms** (Sight Machine, MachineMetrics, Tulip) → adjacent on mode 3; avoid becoming dashboard-only.
- **Process AI** (Fero, Imubit, Braincube, Oden) → rhyme with modes 1/11/12; stop at HITL prescribe.
- **PdM sensor vendors** (Augury, Infinite Uptime, BrightAI toolkit) → absorb “guide the crew”; ignore hardware SKU.
- **APS / MES / CMMS** → do not claim replacement from meter data alone.
