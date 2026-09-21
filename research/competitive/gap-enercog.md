# EnerCog vs Stamped — plain English

## In one sentence
EnerCog (Pune) sells India-focused software **and** edge hardware that **automatically run batteries (BESS), solar, and diesel gensets** to cut Maximum Demand and Time-of-Day charges on industrial electricity bills.

## What they actually do (no jargon)
- Sell a **Battery Energy Storage System Energy Management System (BESS EMS)** — software that decides when the battery charges and discharges, and **writes those commands** to the battery’s power converter.
- Sell **Synapse** — a DIN-rail industrial box on site that keeps controlling even if the cloud drops; talks utility protocols (IEC 60870-5-104, DNP3, IEC 61850, etc.) and can buffer months of data for solar / PM-KUSUM-style projects.
- Run **Cortex** — their tariff/AI layer that knows major Indian DISCOM Time-of-Day (ToD) windows and schedules battery charge off-peak / discharge on-peak.
- Attack three bill levers together: energy (kWh), **Maximum Demand (MD)** — the peak power spike that can set a big charge for the whole month — and ToD peak rates.
- Coordinate **solar + battery + diesel genset + grid** as one stack (including zero-export and genset protection).
- Offer Solar Power Plant Controller (PPC) and utility solar monitoring products aimed at RE / DISCOM tenders — a different buyer than a plant “next action” desk.
- Report savings via **Clarity** UI and WhatsApp/email reports (vendor marketing claims large MD % cuts — treat as claims, not proof).

## What Stamped already does in the same area
- We already spot MD, ToD, and Power Factor (PF) problems and turn them into **Findings** with evidence.
- We already score **Prescriptions in ₹** from real tariff tables and ingest DISCOM HT bills (not invent %).
- We already recommend load stagger / peak shed / contract demand rightsizing — as **assigned next steps**, not silent battery commands.
- We already poll meters (Modbus and friends) and can notify owners on WhatsApp.
- We already refuse to claim “bill-verified ₹ saved” without a defendable path.

## What they can do that we cannot (the real gaps)

### Autonomous battery charge/discharge (closed-loop BESS EMS)
- **What it is:** Software that watches demand every second and **automatically** tells the battery to discharge before an MD spike or ToD peak, and charge when power is cheap or solar is surplus.
- **Why a plant would care:** If they already bought (or must buy) a battery, they want the battery to earn its keep on the bill without a human clicking every hour.
- **Software, hardware, or both?** Both — EMS software plus write access to the battery converter (PCS).
- **Can Stamped add this?** No (and why) — becoming a BESS EMS / silent plant writer conflicts with our two-pillars overlay posture and explicit “no battery-storage claim.” Partner the EMS; keep Stamped on Finding → Prescription → verify.
- **Should we?** No. Partner at hybrid sites.

### Local Synapse-style control box that keeps dispatching offline
- **What it is:** An on-site controller that keeps running battery/solar setpoints when internet dies, with long local data retention.
- **Why a plant would care:** Controllers that freeze on a network blip can miss MD peaks or fail tender rules.
- **Software, hardware, or both?** Hardware + edge software.
- **Can Stamped add this?** Yes with partners — we already buffer ingest data at the edge; we are not a control RTU OEM.
- **Should we?** Partner only; do not start a hardware line.

### Solar plant controller + diesel–solar sync / zero-export
- **What it is:** Fast control at the grid connection point, plus protection so solar does not damage a diesel genset.
- **Why a plant would care:** Hybrid C&I and RE sites get fined or damaged without this coordination.
- **Software, hardware, or both?** Both.
- **Can Stamped add this?** No as Stamped-built PPC; Yes with partners to **read** their telemetry and prescribe around it.
- **Should we?** Partner / ignore as a product line.

### Utility / SLDC protocols and India-built hardware for PSU tenders
- **What it is:** Speaks grid-dispatch protocols; hardware positioned for domestic-content tenders (SECI/NTPC/DISCOM class).
- **Why a plant would care:** Mostly matters for RE interconnection and PSU bids — not for “who owns this idle compressor Prescription.”
- **Software, hardware, or both?** Both.
- **Can Stamped add this?** Yes software for *read* ingest where useful; No as certified SLDC RTU / DCR OEM.
- **Should we?** Soft read connectors later if a deal needs them; never bid as hardware OEM.

### Turning the same MD Finding into automatic battery action
- **What it is:** The insight we already have (MD spike coming) executed by battery discharge without a human.
- **Why a plant would care:** Closes the loop from “alert” to “bill avoided.”
- **Software, hardware, or both?** Both.
- **Can Stamped add this?** No as autonomous PCS write. Human-guided soft writeback is **specified, not shipped**, and still not silent battery control.
- **Should we?** Keep recommend + verify; partner EMS for execution.

## Bottom line for Stamped
EnerCog is an **adjacent partner niche**, not a peer on the Prescription desk. They win RFPs that say “run my battery and solar against DISCOM ToD/MD.” We win when the plant wants India HT Findings → assigned ₹ Prescriptions → closure and honest verify — without buying a control platform. Overlap on *talking about* ToD/MD is real; overlap on *who writes battery setpoints* should stay zero. Do not copy BESS autonomy or Synapse hardware; partner and strengthen our bill-true ₹ Rx story. Never quote their 20–40% MD marketing as our proof.
