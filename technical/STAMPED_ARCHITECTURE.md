# Stamped — Product & Technical Architecture (SSOT)

*Status: current · 2026-07-30*  
*Authority:* this file is the **single** latest product + technical architecture summary. Layer deep-dives live under [`layers/`](layers/). Framing lock: [ADR-026](../decisions/024-026/ADR-026-two-pillars-shared-context.md).

> Honesty: `[~]` approximate · `[!]` evolving — verify before customer-facing claims.

---

## 1. What Stamped is

**Stamped Intelligence** is one product: a **software-first, read-only** overlay on plant OT/IT for Indian energy-intensive manufacturers. It turns meters, SCADA/PLC/EMS, bills, and (when available) orders into **assigned prescriptions with ₹ impact**, then **verifies with evidence** and **improves** from what was followed vs ignored.

| Dimension | Definition |
| --- | --- |
| **Category** | Verified-with-evidence **operational decision layer** (not EMS / monitoring-only) |
| **Buyer outcome** | Verified ₹ / SEC reduction with evidence; effectiveness co-benefits when context exists |
| **Client enemy** | Insight without closure — dashboards and OEE that never become assigned, verified actions |
| **Integration** | Read-only — no control writes, not a hardware retrofit program |
| **Operating loop** | Connect → Observe → Decide → Execute → Verify → **Improve** |
| **Proof phrase** | **Verified with evidence** (ops-cleared / calculated ledger). DISCOM bill confirmation is optional, not the lead claim. |

### Exactly two pillars + shared context (not a third pillar)

```text
One product
 ├── Pillar 1 — Load & Energy Efficiency Intelligence   (hero ₹ / SEC / bill)
 ├── Pillar 2 — Prescriptive Equipment Intelligence     (equipment early warnings)
 └── Shared context — orders, departments, tradeoffs, negotiation, Improve
```

| Say | Do not say |
| --- | --- |
| Two pillars + shared plant context | Third pillar / plant OS / MES product |
| Energy efficiency (hero ₹) | Energy-only forever |
| Plant effectiveness / OEE co-benefits on Rx | Separate OEE / MES product |
| Prescriptive equipment intelligence | Vibration PdM company / full CMMS |
| Read ERP/MES orders | We replace MES scheduling |

**30-second pitch:** (1) Cut energy cost with assigned, evidence-verified actions. (2) Same stack flags equipment issues early for maintenance. (3) For schedule-type actions, read orders/departments so we do not break production — **not your MES**. (4) Management Rx show **₹ energy** (hero) plus **effectiveness co-benefits** when context exists.

**Client narrative (canonical order):** load & energy management → equipment ML baselines → **practical prescriptions** → agentic layer that makes Rx feasible at scale. Do **not** lead with “agentic AI”. Full copy: [Stamped_Client_Positioning_and_Narrative_v1.md](product/Stamped_Client_Positioning_and_Narrative_v1.md).

---

## 2. Named outcomes

| Outcome | Role on prescriptions |
| --- | --- |
| **Energy efficiency** | Hero — ₹ / kWh / SEC on every relevant Rx |
| **Plant effectiveness** | Co-benefit — OEE / order-on-time / downtime risk when order context exists ([ADR-024](../decisions/024-026/ADR-024-holistic-plant-decisions.md) trade-off block). **Not** Pillar 3. |

---

## 3. Operating loop

| Step | Name | What happens |
| --- | --- | --- |
| 01 | Connect | Ingest meters, bills, OT tags, optional ERP/MES orders |
| 02 | Observe | Baselines, SEC, anomalies, equipment health signals |
| 03 | Decide | Findings → ranked prescriptions (energy + optional trade-off) |
| 04 | Execute | Assign owners; WhatsApp / dashboard; optional negotiation revise |
| 05 | Verify | Ops-cleared / calculated M&V → ledger; bill path optional |
| 06 | Improve | Calibration + preference signals from follow/ignore outcomes ([ADR-025](../decisions/024-026/ADR-025-improve-loop-step-06.md)) |

---

## 4. L0–L6 stack

```text
L0  Plant systems (customer-owned, read-only)
L1  Connect & normalise          → connectors-edge / cloud / bill
L2  Universal Repository         → six stores in Postgres+Timescale
L3  Intelligence core            → findings (numeric / rules)
L4  Knowledge & reasoning        → evidence-bound Rx drafting (agentic)
L5  Closure & verification       → workflow, WhatsApp, M&V, ledger
L6  Experience & integration     → dashboard, BFF, exports, APIs
```

| Layer | Spec | Owns |
| --- | --- | --- |
| L1 | [L1](layers/l1-l2/L1-connect-and-normalise.md) | Protocols, edge, bill ingest, normalisation |
| L2 | [L2](layers/l1-l2/L2-universal-repository.md) | TSDB, energy graph, commercial/production context, features, baselines, ledger |
| L3 | [L3 core](layers/l3/L3-intelligence-core.md) | Engines for both pillars; Finding emit |
| L4 | [L4](layers/l4-l6/L4-knowledge-and-reasoning.md) | Dual-lane agent, RAG, Rx draft |
| L5 | [L5](layers/l4-l6/L5-closure-and-verification.md) | Workflow, notify, M&V, ledger append |
| L6 | [L6](layers/l4-l6/L6-experience-and-integration.md) | EMS console, Rx queue, analyst, APIs |
| Cross | [Production](cross-cutting/03-production-engineering.md) · [Eval](cross-cutting/04-evaluation-and-quality.md) | Reliability, quality gates |

**Layer-per-repo** communicates only through versioned contracts in this pack ([ADR-008](../decisions/006-010/ADR-008-layer-repo-topology-and-interfaces.md)).

---

## 5. Shared context (not a pillar)

These enable practical management Rx; they are **not** a MES product.

| Artifact | Role |
| --- | --- |
| Production orders (ERP/MES/MES-lite read) | Schedule windows, order risk on stagger/shed Rx |
| Department graph + incentives | Who owns the action; conflict visibility |
| Trade-off block on management Rx | ₹ energy (hero) + effectiveness co-benefits + alternatives |
| Prescription negotiation | Bounded parameter revise — not free-form rewrite |
| Improve (step 06) | ML calibration + agent preferences + monthly UI report |

Contracts (0.10.0+): `production-order`, `plant-department-graph`, `prescription-revision`, `improvement-signal`, `plant-preference-profile`; Rx fields `decision_class` / `tradeoff`.

Handoff hub: [`../handoff/holistic/`](../handoff/holistic/).

---

## 6. How 15–20% savings is engineered

Savings are **not** one model score. They are:

> **Σ (closed prescriptions across waste categories) × closure rate**, defended by **evidence-backed M&V**.

Architecture must (a) detect across categories, (b) convert detections into executed actions, (c) verify on telemetry/ledger (bill optional). Detection without closure is not the product.

---

## 7. Technology defaults (cost-first)

| Concern | Default | Upgrade when |
| --- | --- | --- |
| TSDB | TimescaleDB on Postgres | Scale / retention pressure |
| Messaging | Mosquitto MQTT (L1) · Postgres outbox | Need Redpanda-class bus |
| Runtime shape | Modular monoliths per layer repo | Clear satellite boundaries |
| Deploy modes | `local`, `local-dashboard`, `cloud` ([ADR-010](../decisions/006-010/ADR-010-deployment-profiles-and-portability.md)) | Same contracts in all modes |
| Edge | Go agent, read-only OT | — |

India compliance by design: CERT-In residency, DPDP, read-only OT — [`../compliance/`](../compliance/).

---

## 8. Prescription card (hero UX)

**Practical floor action** — not a chart insight. Client-visible fields:

- **What** · **Why** · **Owner** (role + department) · **Effort** · **Impact** (₹ hero, `[illustrative]` until M&V locked) · **Due** (real window: shift, job, maintenance slot) · **Priority**
- **Flip for evidence** — tags, baseline comparison, tariff window
- **Management-class:** trade-off block (energy + effectiveness co-benefits + alternatives)
- **Discuss:** bounded negotiation when first window is unsafe (low standby, active order) → next-best slot
- Proof: verified with evidence badges (ops vs bill paths separate)

Illustrative cards + constraints: [prescriptions-examples.md](../demo-decks/prescriptions-examples.md). Client wording: [product/Stamped_Client_Positioning_and_Narrative_v1.md](product/Stamped_Client_Positioning_and_Narrative_v1.md) §2 step 3.

---

## 9. Anti-confusion

| Concern | Stamped is | Stamped is not |
| --- | --- | --- |
| Energy | Pillar 1 | Passive EMS charts only |
| Equipment | Pillar 2 early-warning Rx | Full CMMS / vibration PdM company |
| Effectiveness / OEE | Co-benefit via shared context | Separate OEE / MES product |
| MES / ERP | Read orders & schedules | Dispatch / WIP / scheduling SoR |

---

## 10. Reading map (agents)

| Priority | Doc |
| --- | --- |
| 1 | **This file** |
| 2 | [Client positioning & narrative](product/Stamped_Client_Positioning_and_Narrative_v1.md) — WhatsApp, decks, I4.0 buyers, Rx practicality |
| 3 | [ADR-026](../decisions/024-026/ADR-026-two-pillars-shared-context.md) · [ADR-024](../decisions/024-026/ADR-024-holistic-plant-decisions.md) · [ADR-025](../decisions/024-026/ADR-025-improve-loop-step-06.md) |
| 4 | [prescriptions-examples.md](../demo-decks/prescriptions-examples.md) — floor-tied illustrative Rx |
| 5 | [handoff/README.md](../handoff/README.md) → your layer / [`agents/prompts/stamped-holistic-consumer-prompt.md`](../handoff/agents/prompts/stamped-holistic-consumer-prompt.md) |
| 6 | [`contracts/`](../contracts/) + `scripts/contracts/contract-check.sh` |
| 7 | Layer specs under [`layers/`](layers/) as needed |
| Legacy names | Thin pointers in [`pointers/`](pointers/) redirect here |

Research/ML bibliography: [`research/stamped-research-and-ml-citations.md`](research/stamped-research-and-ml-citations.md).
