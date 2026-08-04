---
type: Product Concept
title: "Stamped Energy — Client Positioning & Narrative (v1)"
description: "Canonical client-facing narrative — who Stamped is, the four-step story (load, equipment ML, prescriptions, agentic layer), Industry 4.0 gap, WhatsApp/deck templates, and honesty rules for enterprise buyers."
tags: [stamped-energy, product, positioning, gtm, client-narrative, agentic]
timestamp: "2026-08-04T18:00:00+05:30"
---

# Stamped Energy — Client Positioning & Narrative (v1)

*Status: **Canonical client narrative** — use for WhatsApp follow-ups, technical decks, discovery calls, and enterprise accounts (e.g. ITC-scale I4.0 buyers).*  
*Supersedes ad-hoc founder drafts when they conflict.*  
*Honesty:* `[~]` approximate · `[!]` evolving — validate on pilots before customer guarantees.

**Related (this repo):** [STAMPED_ARCHITECTURE.md](../STAMPED_ARCHITECTURE.md) · [ADR-026](../../decisions/024-026/ADR-026-two-pillars-shared-context.md) · [prescriptions-examples.md](../../demo-decks/prescriptions-examples.md) · Research canon: `Stamped-Energy` repo `core-product/`

---

## 1. Who we are (client-facing)

**Stamped Energy** is a **read-only operational decision layer** for energy-intensive Indian manufacturers. We connect to meters, SCADA/EMS, production context, and DISCOM bills — without replacing existing Industry 4.0 stacks, without PLC writes, and without becoming an EMS, MES, or CMMS.

**What we do in one sentence:**

> We help plants **manage load and equipment more efficiently in real time**, turn findings into **assigned prescriptions with ₹ impact**, and **verify outcomes with evidence** — moving from monitoring and alerts to context-aware decisions your team can act on.

**Category:** Verified-with-evidence operational decision layer (product name: **Stamped Intelligence**).

**Enemy:** Insight without closure — dashboards, OEE stacks, and audits that show what happened but never become a named task with proof the outcome improved.

---

## 2. The four-part client narrative (canonical order)

Use this sequence in WhatsApp, technical decks, and discovery deep-dives. **Do not lead with “agentic AI”** — lead with outcomes, then introduce the agentic layer as what makes prescriptions practical at scale.

### Step 1 — Load and energy management (hero)

**Client language:** We continuously combine load, production, and tariff signals to recommend the **best operating decisions in real time** — so the plant runs as efficiently as possible without hurting production commitments.

**Includes (not only MD):**

| Lever | Plain meaning |
| --- | --- |
| Load staggering & sequencing | Desynchronise large starts; avoid coincidence peaks |
| Idle-load reduction | Compressors, lines, aux running with no production |
| Utility scheduling | When to run chillers, dryers, air systems relative to load |
| ToD / tariff windows | Shift flexible consumption to cheaper periods |
| Thermal timing | Preheat, hold, setback for ovens, dryers, HVAC |
| MD control | Attribution is **one part** of load management — not the whole story |

**Proof:** MGVCL/DISCOM bill lines (MD, energy, PF) where applicable; Stamped ledger is primary.

### Step 2 — Equipment intelligence (ML on plant baselines)

**Client language:** Equipment-specific **ML models calibrate to each plant’s own operating baselines** across compressors, chillers, dryers, and production lines. They detect **specific-power drift**, abnormal duty cycles, and changing start/trip behaviour **earlier than fixed-threshold monitoring** — so maintenance can investigate developing issues before they become sustained energy losses or breakdowns.

**Honesty rules:**

| Say | Do not say (until pilot data exists) |
| --- | --- |
| Models **calibrate to the plant’s baselines** | “Already fine-tuned for your site” before connect |
| **Earlier warning than generic thresholds/alarms** | “Predict breakdown 14 days out at 87%” |
| **Inspect / clean / tune** prescriptions | Vibration PdM, bearing RUL, MCA |

Maps to **Pillar 2 — Prescriptive Equipment Intelligence** in [STAMPED_ARCHITECTURE.md](../STAMPED_ARCHITECTURE.md).

### Step 3 — Prescriptions (what the buyer receives)

**Client language:** Findings become **practical prescriptions** — what to change or inspect, why it matters, who should act, effort level, and expected **₹ or reliability impact**. Delivered via **WhatsApp and dashboard**; tracked to completion; verified on Stamped’s **potential vs realised ledger** (DISCOM bill confirmation optional).

**Prescription card fields (client-visible):** What · Why · Who · Effort · Impact · When · **Flip for evidence**

**Practicality rules (agents must enforce):**

| Rule | Meaning |
| --- | --- |
| **Floor-tied** | Rx names a concrete action in a real window (shift, job, maintenance slot) — not “optimise compressor” |
| **Owner is a role + department** | e.g. Utilities lead + gravure shift supervisor — not “plant” |
| **Effort is honest** | hours, permit, production sign-off — not hidden in jargon |
| **Impact is illustrative until locked** | mark `[illustrative]` / sample ranges until M&V baseline locked |
| **Schedule-aware** | if first window is unsafe (low standby air, active order), **negotiate** to next feasible slot — see [ADR-024](../../decisions/024-026/ADR-024-holistic-plant-decisions.md) |
| **Evidence on flip** | tag readings, baseline comparison, tariff window — supervisor can defend the Rx |

Examples: [prescriptions-examples.md](../../demo-decks/prescriptions-examples.md) — talk tracks + 10 sample cards (plain language front, evidence on flip).

### Step 4 — Agentic intelligence layer (alongside, not “under the hood”)

**Client language:** Alongside this runs an **agentic intelligence layer** that works with the ML models and plant context — production constraints, tariff logic, maintenance playbooks — to turn raw findings into those prescriptions and suggest the **next-best action** when the first option conflicts with production.

**What it does (client-facing):**

- Combines signals across load, equipment, schedule, and tariff
- Ranks and deduplicates actions so supervisors are not flooded
- Grounds recommendations in plant data and domain playbooks (not generic chat)
- Routes ownership to the right role (electrical, utilities, maintenance, production)

**What Industry 4.0 typically has vs Stamped:**

| Typical I4.0 / EMS / OEE stack | Stamped adds |
| --- | --- |
| Real-time monitoring, dashboards, OEE, fault codes | **Context-aware operational decisions** |
| Threshold alarms | **Ranked prescriptions with ₹ and owner** |
| Post-hoc analysis | **Real-time load and drift decisions** |
| Audit PDFs / EnMS opportunity logs | **Assigned action + verified outcome loop** |

**Positioning line for I4.0-native buyers (e.g. ITC PPB):**

> You already monitor. Stamped is the layer that helps decide **what to do next**, checks whether it is **operationally feasible**, **assigns it**, and **measures the result**.

**Technical honesty (internal / deep technical only):** Bounded tool-using agent; physics and tariff guardrails; read-only on OT; human approval for high-risk/capex. Do **not** lead client conversations with “rules engine veto” — say **grounded in plant data and operational playbooks**.

---

## 3. One-line distinctions

| Audience | Line |
| --- | --- |
| Plant head / factory head | “From monitoring to **decisions your team can act on** — with evidence.” |
| Electrical / utilities | “**Real-time load decisions** and equipment drift — assigned to your team, verified on the ledger.” |
| I4.0 / digital lead | “The **closure layer** your monitoring stack does not own — prescriptions, not another dashboard.” |
| CFO / commercial | “**₹ impact per action**, verified with evidence — optional bill confirmation.” |

---

## 4. WhatsApp templates

### 4.1 Standard follow-up (canonical)

```text
At Stamped, we work across two connected areas.

First is load and energy management. We continuously combine load, production and tariff signals to recommend the best operating decisions in real time — load staggering, idle-load reduction, utility scheduling, ToD optimisation and MD control — without disrupting production commitments.

Second is equipment intelligence. Equipment-specific ML models calibrate to the plant’s own baselines across compressors, chillers, dryers and production lines. They detect specific-power drift, abnormal duty cycles and changing start/trip behaviour earlier than fixed-threshold monitoring, so maintenance teams can investigate developing issues before they become sustained energy losses or breakdowns.

Alongside this, an agentic intelligence layer combines each finding with production constraints, tariff context and maintenance knowledge, then converts it into a practical prescription: what to change or inspect, why, who should act and the expected ₹ or reliability impact.

The value above a typical Industry 4.0 stack is the move from monitoring and alerts to context-aware decisions, assigned action and verified outcomes.
```

### 4.2 Shorter variant

```text
Stamped sits read-only on your meters, SCADA/EMS and bills.

We help you manage load in real time (stagger, idle waste, utilities, ToD, MD) and flag equipment drift earlier via ML baselines on compressors, dryers and chillers.

An agentic layer turns findings into assigned prescriptions (what/why/who/₹) and verifies outcomes — the step most I4.0 stacks stop short of.

Happy to share a short technical brief if useful.
```

### 4.3 Enterprise / I4.0-native opener (one extra line)

Add after paragraph 1:

```text
We complement your existing I4.0 and line monitoring — we don’t replace sequencing or OT control.
```

---

## 5. Technical deck — narrative slide map

For a **10-slide** technical brief, use this arc. Only **one slide** emphasises agentic + ML architecture; the rest lead with core outcomes.

| # | Slide | Focus |
| --- | --- | --- |
| 1 | Title | Stamped Intelligence · read-only decision layer |
| 2 | The gap | Monitoring without decisions / closure |
| 3 | Where we sit | On top of SCADA / EMS / I4.0 |
| 4 | **Pillar 1** | Real-time load & energy management (broad levers) |
| 5 | **Pillar 2** | ML baselines · equipment drift · earlier warning |
| 6 | Prescriptions | What the floor receives · WhatsApp · ledger |
| 7 | **Agentic + ML** | *From detected deviation to the next best plant decision* (see §6) |
| 8 | Verify | Potential vs realised · evidence pack |
| 9 | vs I4.0 | What you have vs what Stamped adds (table §2 step 4) |
| 10 | Boundaries + ask | 60-Day Proof Run |

---

## 6. Deck slide — agentic emphasis (single slide)

**Kicker:** How it becomes actionable  
**Headline:** From detected deviation to the next best plant decision

**Three columns:**

| ML intelligence | Agentic layer | What the plant gets |
| --- | --- | --- |
| Load & SEC baselines | Combines findings with production + tariff context | Real-time load decisions |
| Drift & anomaly on equipment | Turns signals into ranked prescriptions | Assigned maintenance actions |
| Attribution across assets | Suggests next-best option if first conflicts with schedule | Better operational judgement than alerts alone |

**Example strip (customise per vertical):**

> Compressor duty drift + morning load ramp → ML flags drift → agent drafts inspect Rx **and** stagger option with ₹ on bill line → Utilities lead on WhatsApp → verified on ledger.

**Footer:** Read-only on OT · complements Industry 4.0 · does not replace MES or line control

---

## 7. Alignment with two pillars (internal map)

| Client narrative step | Technical pillar |
| --- | --- |
| Load and energy management | **Pillar 1 — Load & Energy Efficiency Intelligence** |
| Equipment ML baselines | **Pillar 2 — Prescriptive Equipment Intelligence** |
| Prescriptions + verify | **Connect → Improve loop** (steps 03–06) |
| Agentic layer | **L4 knowledge & reasoning** (bounded prescription agent) |

Shared plant context (orders, departments, trade-offs) is **not** a third product — it keeps prescriptions feasible in a real multi-department plant.

---

## 8. What we still are / are not

**Is:** Load and energy decision layer · equipment drift intelligence · prescriptions · evidence verification · read-only integration

**Is not:** EMS replacement · MES · CMMS · vibration PdM · solar/EPC · autonomous plant control · “fine-tuned for you” before plant connect

---

## 9. Document changelog

| Date | Change |
| --- | --- |
| 2026-08-04 | v1 — canonical client narrative; four-step story; WhatsApp templates; single agentic deck slide |
| 2026-08-04 | Mirrored to stamped-external `technical/product/`; practicality rules + floor-tied Rx examples cross-linked |

---

*Iterate after field calls; keep marketing category stable while refining client narrative wording.*
