# START HERE — reader primer for this pack

**Read this file first.** Then open numbered docs. Do **not** start with `07` until you finish this primer (and ideally `00` + `01` skim).

**Folder:** `docs/research/plant-efficiency-exploration-2026-09/`  
**What this pack is:** exploration notes about how Stamped might grow from “energy software” into “plant efficiency software.” Nothing here is a final company decision.

---

## 1. The story in one minute

1. Stamped started with **energy** (meters, electricity bills, savings on the DISCOM bill).
2. On the plant floor and in investor talks (Vaibhav / Together.fund), the bigger story is **overall plant efficiency** — cost, time, idle machines, utilization — not only the power bill.
3. Near term we stay **software-only** (no new vibration sensors, robots, or camera QC as the product).
4. This pack maps: what data we already get → what value we can sell → what peers do → what company shapes (A–E) are possible → a council’s recommended path (`07`) → **what actions unlock beyond energy** (`08` / `08a`).

**Enemy of the product (repeated everywhere):** dashboards that show insight but nobody owns a fix. The preferred loop is:

**data → assigned action (with owner) → human does it → evidence it worked**

---

## 2. Words you’ll see everywhere

| Term | Plain meaning |
|------|----------------|
| **L1** | The “connect & normalise” layer: how we pull plant data into Stamped (meters, bills, etc.). |
| **Intake** | The data types we can actually read today (see §3). |
| **Mode (1–13)** | A *kind of value* we could deliver from that data. Numbered catalog in [`01-intake-and-value-modes.md`](./01-intake-and-value-modes.md). When people say “modes 1, 2, 7, 8,” they mean those rows. |
| **Path B** | Lighter data: main meter + bill + calendar (and maybe production Excel). |
| **Path A** | Richer data: feeders / SCADA / CNC (e.g. MTConnect) already in the plant — still software connectors, not new hardware we sell. |
| **HITL** | Human-in-the-loop: we recommend; people execute; we don’t silently write setpoints to a DCS. |
| **DISCOM bill** | The electricity utility bill — used as a trusted ₹ proof, not as the whole product identity. |
| **SEC** | Specific energy consumption (energy per unit produced). |
| **Process (capital P)** | Vision idea of a second product: manufacturing *methods* (cycle time, tooling, process docs) — **not** Celonis-style IT process mining. Needs drawings/docs we mostly don’t ingest yet. |
| **Options A–E** | Five possible *company/product shapes* scored in [`05`](./05-product-vision-option-space.md). See §5 below. |
| **Hypothesis / not a lock** | Opinion to test with plants — not a board decision. |
| **Founder-reported** | Claim from our pilots/team (e.g. Faridabad cycle-time story) — not audited proof. |
| **Vendor-claimed** | Competitor marketing numbers — treat carefully. |

---

## 3. What data we take in (the fuel)

From [`01`](./01-intake-and-value-modes.md):

| Record | Everyday example |
|--------|------------------|
| **Measurement** | kW from meters / SCADA / CNC energy tags |
| **BillLine** | Lines on the monthly electricity bill (tariff, MD, PF, TOD) |
| **ProductionRecord** | How many pieces/tons this shift (Excel/MES) |
| **Event + calendar** | Shifts, maintenance windows, “connector down” |

**We generally do *not* take in yet:** vibration stickers, cameras, CAD drawings, CAM toolpaths, labour rosters. That is why “Process freezes” and hardware PdM are later / out.

---

## 4. The modes (1–13) — plain English

**Source of truth:** [`01-intake-and-value-modes.md`](./01-intake-and-value-modes.md) §3.

When `07` says “ship modes 1, 2, 7, 8,” it means these product capabilities:

| Mode | Name | In one sentence | Can we do it soon? |
|------|------|-----------------|--------------------|
| **1** | Assigned efficiency actions | System finds an opportunity, assigns a person a concrete fix with expected ₹ or minutes, then checks if it landed. | **Yes — core product** |
| **2** | Load & utility cost levers | Cut bill cost via MD / PF / TOD / load patterns (not just “use less kWh”). | **Yes** |
| **3** | Machine utilization / idle | See run vs idle from CNC/SCADA and act on wasted machine time. | **Yes if Path A** (CNC/SCADA already connected) |
| **4** | Energy-aware production timing | Nudge *when* to run loads vs tariff — not a full factory scheduler (APS). | **Partial** |
| **5** | Unit economics | Cost or kWh **per piece/ton** (needs production numbers). | **Yes if production uploaded** |
| **6** | Signature maintenance guidance | “This meter/SCADA pattern looks wrong” — guidance only, **not** vibration PdM. | **Narrow** |
| **7** | Bill / tariff defence | Recompute the bill; catch tariff/MD mistakes; prove ₹ on commercial paper. | **Yes — trust anchor** |
| **8** | HITL orchestration | Workflow: finding → owner → notify → done (beats WhatsApp chaos). | **Yes — closure product** |
| **9** | Capex / asset utilization | Is this asset earning its keep? Needs asset metadata. | **Medium** |
| **10** | Multi-site benchmark | Compare the same playbook across plants. | **After plant #2+** |
| **11** | Methods / tooling freezes | Parse process docs / tooling and “freeze” a better method (cycle time, tool life). | **Weak today** — needs new intake |
| **12** | Closed-loop setpoint write | Software writes to DCS/PLC without a human. | **Out** near term |
| **13** | Vision QC / robotics | Cameras / robot cells. | **Out** — hardware |

**The council’s “build now” shortlist:** **1 + 2 + 7 + 8**, plus **5** when you have production data, plus **3** when CNC/SCADA is connected.

---

## 5. Options A–E (company shapes)

**Source of truth:** [`05-product-vision-option-space.md`](./05-product-vision-option-space.md).

| Option | Meaning | Pack vibe |
|--------|---------|-----------|
| **A** | Stay energy-only (bill ₹ / SEC). | Too narrow; team + Vaibhav already past this as *sole* identity. |
| **B** | One “plant efficiency” product (actions across cost/time/energy). | Good idea; risk of unfocused mush without a niche. |
| **C** | Two products now: Energy + Process (Vision v0.3). | Nice map long-term; heavy early; Process data missing. |
| **D** | Efficiency wedge **now** (like B on meters/SCADA) → Process **later**. | **Strong default hypothesis** in the pack and in `07`. |
| **E** | Lead with docs/methods for multi-site MNCs. | Interesting for scale; abandons meter beachhead if done first. |

`07` recommends **D** (hypothesis, not a lock).

---

## 6. What each numbered file is for

| File | Read when… |
|------|------------|
| **This file (START HERE)** | Always first. |
| [`00-framing…`](./00-framing-vaibhav-and-vision.md) | Why the pack exists; Vaibhav call; Vision v0.3 in one table. |
| [`01-intake…`](./01-intake-and-value-modes.md) | Modes 1–13 and what data funds them. **Bookmark this.** |
| [`02` / `03` / `04`](./02-usa-deep-dive.md) | Competitor surveys (USA / Europe / India + physical AI). Optional until later. |
| [`05-…option-space`](./05-product-vision-option-space.md) | Options A–E scored. |
| [`06-synthesis…`](./06-synthesis-and-open-questions.md) | Pack’s own wrap-up and open questions. |
| [`07-product-vision-council`](./07-product-vision-council.md) | Five models + synthesis: phased “now / pilots / before hardware.” |
| [`08-beyond-energy-action-catalog`](./08-beyond-energy-action-catalog.md) | **Actions unlocked beyond energy** — software-data map + decision catalog. |
| [`08a-prior-research-landscape`](./08a-prior-research-landscape.md) | Other Stamped research packs inventory (not only this pack). |

Supporting: `README.md`, `PROGRESS.md`, `SOURCES.md`, `IMPLEMENTATION_PLAN.md` — skip until you care about process/meta.

---

## 7. Suggested reading order (if you are cold)

### Pass A — ~25–40 minutes (enough to understand `07` / `08`)

1. **This primer** (you are here)
2. [`00-framing-vaibhav-and-vision.md`](./00-framing-vaibhav-and-vision.md) — skim sections 1–3
3. [`01-intake-and-value-modes.md`](./01-intake-and-value-modes.md) — sections 1–3 (intake + modes table)
4. [`05-product-vision-option-space.md`](./05-product-vision-option-space.md) — options A–E + comparative table only
5. [`07-product-vision-council.md`](./07-product-vision-council.md) — sections 4–5 first (recommendation + phased capabilities), then 2–3 if curious
6. [`08-beyond-energy-action-catalog.md`](./08-beyond-energy-action-catalog.md) — §§1–4 (beyond-energy actions); skim [`08a`](./08a-prior-research-landscape.md) for prior-research context

### Pass B — ~90 minutes

Add [`06-synthesis-and-open-questions.md`](./06-synthesis-and-open-questions.md), then skim peers in `02`/`03`/`04` only for names that sound like your wedge.

---

## 8. How to read `07` without getting lost

`07` assumes you already know modes and A–E. Decode it like this:

1. **Roster** = which AI models argued (Composer, Grok, Luna, Sol, Opus).
2. **Stances** = each said roughly “pick D.”
3. **Final recommendation** = company = plant efficiency; product = assigned actions with evidence; energy proves ₹, doesn’t limit the company.
4. **Phase 1 / 2 / 3** = *when* to build what:
   - Phase 1 = with data you already have (modes above)
   - Phase 2 = while talking to plants / early pilots
   - Phase 3 = bigger vision still **before** selling hardware
5. When you see “modes 1, 2, 7, 8” → jump back to **§4 of this primer**.

---

## 9. One picture

```text
Plant data (meters, bills, production, calendar)
        │
        ▼
   Detect opportunity
        │
        ▼
 Assign action to a person  ←── Mode 1 + Mode 8
        │
        ▼
 Human does the work (HITL)
        │
        ▼
 Evidence: bill ₹ (Mode 7/2) and/or minutes/idle (Mode 3) and/or unit cost (Mode 5)
```

Later (not now): Mode 11 methods docs → still software → only then consider hardware.

---

**Next click:** [`00-framing-vaibhav-and-vision.md`](./00-framing-vaibhav-and-vision.md)
