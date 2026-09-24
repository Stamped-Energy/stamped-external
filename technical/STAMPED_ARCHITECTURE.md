# Stamped — Product & Technical Architecture (SSOT)

*Status: current · 2026-09-24*  
*Authority:* product framing is [ADR-030](../decisions/028-032/ADR-030-five-domain-decision-loop.md) and [`research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md`](../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md). This file summarizes **product + technical** architecture. Layer deep-dives live under [`layers/`](layers/).

> Honesty: `[~]` approximate · `[!]` evolving — verify before customer-facing claims. Do not invent savings, customers, or revenue.

---

## 1. What Stamped is

**Stamped** helps plant teams **choose, assign, and verify** the next operating action across **energy, cost, time / throughput, continuity / flow, and short-horizon exceptions**.

One meaningful condition → **one decision card** → **one owner** → honest closure. Energy is the entry wedge, not the product name and not the category. Recommend and assign by default. Hard stops in ADR-030 and vision `09` stay absolute.

| Dimension | Definition |
| --- | --- |
| **Category** | Closed operational decision loop (not EMS / monitoring-only / OpEx suite) |
| **Buyer outcome** | A named next action with owner and evidence that closes — across five domains |
| **Client enemy** | Insight without closure — dashboards that never become assigned, verified actions |
| **Integration** | Read / ingest default; write-back human-confirmed, narrow, allow-listed |
| **Operating loop** | detect → recommend → assign → act → verify (optional propose learning) |
| **Proof** | Evidence labeled Measured / Confirmed / Modeled / Unknown; wallets separate; calculator owns money |

### Five domains on one card

```text
One product — Stamped
 ├── Energy · Cost · Time/throughput · Continuity/flow · Exception response
 ├── One primary domain tag per card; optional secondary tags; one owner
 └── Stack L1→L6 unchanged (ADR-008); claim is the closed action
```

| Say | Do not say |
| --- | --- |
| Stamped | Product name with Energy appended |
| Five-domain decision loop | Withdrawn dual-pillar framing |
| Energy as entry wedge | Energy-only company |
| Choose / assign / verify | Dashboard-only / runs the plant |
| Read ERP/MES context | We replace MES / APS / ERP |

**30-second pitch:** Put the next operating action in front of one named owner. Close it with honest evidence. Start where energy data opens the door; expand when a non-energy decision closes the same way.

External marketing is archived under [`archive/external-marketing-2026-09/`](../archive/external-marketing-2026-09/). Agents do not take identity from that folder.

---

## 2. Named outcome domains

| Domain | Owns | Does not own |
| --- | --- | --- |
| **Energy** | When/how loads run; avoidable use / intensity where data supports | Retail energy, bill-audit firm, meter hardware, critical remote control |
| **Cost** | Visible operating-cost levers | Plant ledger / FP&A |
| **Time / throughput** | Machine-minutes, dwell, constraint-cell next choice | Full plant schedule publish |
| **Continuity / flow** | One handoff / batch / queue decision | New dispatch list / month-ahead plan |
| **Exception response** | Next choice after stop / slip under visible constraints | APS / MRP replacement; quality hold release |

---

## 3. Operating loop

| Step | Name | What happens |
| --- | --- | --- |
| 1 | Ingest | Meters, machine state, production, maintenance context, calendars, structured human input |
| 2 | Normalize | Join enough to name one condition |
| 3 | Detect | ML models / methods / rules → condition worth a card |
| 4 | Recommend | Agent stack: options, constraints, uncertainty, one owner |
| 5 | Assign | Route to the accountable role |
| 6 | Record | Accept / edit / reject / defer + reason |
| 7 | Verify | Named evidence; honest closure state |
| 8 | Propose learning | Named-owner gate for production changes ([ADR-025](../decisions/024-026/ADR-025-improve-loop-step-06.md)) |

---

## 4. L0–L6 stack

```text
L0  Plant systems (customer-owned)
L1  Connect & normalise          → connectors-edge / cloud / bill
L2  Universal Repository         → six stores in Postgres+Timescale
L3  Intelligence core            → findings (numeric / rules)
L4  Knowledge & reasoning        → evidence-bound recommendation drafting
L5  Closure & verification       → workflow, notify, M&V, ledger
L6  Experience & integration     → control room, BFF, exports, APIs
```

| Layer | Spec | Owns |
| --- | --- | --- |
| L1 | [L1](layers/l1-l2/L1-connect-and-normalise.md) | Protocols, edge, bill ingest, normalisation |
| L2 | [L2](layers/l1-l2/L2-universal-repository.md) | TSDB, plant graph, commercial/production context, features, baselines, ledger |
| L3 | [L3 core](layers/l3/L3-intelligence-core.md) | Detection engines; Finding emit |
| L4 | [L4](layers/l4-l6/L4-knowledge-and-reasoning.md) | Dual-lane agent, RAG, recommendation draft |
| L5 | [L5](layers/l4-l6/L5-closure-and-verification.md) | Workflow, notify, M&V, ledger append |
| L6 | [L6](layers/l4-l6/L6-experience-and-integration.md) | Next-action surfaces, queue, analyst, APIs |
| Cross | [Production](cross-cutting/03-production-engineering.md) · [Eval](cross-cutting/04-evaluation-and-quality.md) · [Practicality](cross-cutting/05-prescription-practicality-eval.md) | Reliability, quality gates |

**Layer-per-repo** communicates only through versioned contracts in this pack ([ADR-008](../decisions/006-010/ADR-008-layer-repo-topology-and-interfaces.md)).

---

## 5. Plant context (enablers, not a second product)

| Artifact | Role |
| --- | --- |
| Production orders (ERP/MES read) | Constraint context for near-term choices — never own dispatch |
| Department / owner graph | Who owns the action |
| Dual plant graphs + Path D (L4) | Canonical + live index ([ADR-028](../decisions/028-032/ADR-028-dual-plant-graphs-and-path-d.md)) |
| Bounded negotiation | Parameter revise with human confirm — not free-form rewrite |
| Improve | Learning from closed cards ([ADR-025](../decisions/024-026/ADR-025-improve-loop-step-06.md)) |

Handoff hub: [`../handoff/`](../handoff/).

---

## 6. How value is engineered

Value is **not** one model score and **not** a fixed 15–20% identity claim.

> Closed decision cards × honest closure (including rejection and no-change) × evidence that matches its tier.

Architecture must (a) detect conditions across domains, (b) assign an owner, (c) verify with labeled evidence. Detection without closure is outside the product center.

---

## 7. Technology defaults (cost-first)

| Concern | Default | Upgrade when |
| --- | --- | --- |
| TSDB | TimescaleDB on Postgres | Scale / retention pressure |
| Messaging | Mosquitto MQTT (L1) · Postgres outbox | Need Redpanda-class bus |
| Runtime shape | Modular monoliths per layer repo | Clear satellite boundaries |
| Deploy modes | `local`, `local-dashboard`, `cloud` ([ADR-010](../decisions/006-010/ADR-010-deployment-profiles-and-portability.md)) | Same contracts in all modes |
| Edge | Go agent; OT write only if plant-accepted earned path (hard stops bind) | — |

India compliance by design: CERT-In residency, DPDP — [`../compliance/`](../compliance/).

---

## 8. Decision card (hero UX)

**Practical next action** — not a chart insight:

- **What** · **Why** · **Owner** · **Effort** · **Expected effect** (domain wallets separate; ₹ only via calculator) · **Due / review** · **Primary domain tag**
- **Evidence** — Measured / Confirmed / Modeled / Unknown beside the result
- **Closure** — verified / no change / rejected / deferred / blocked
- Hard stops always visible in product claims

---

## 9. Anti-confusion

| Concern | Stamped is | Stamped is not |
| --- | --- | --- |
| Energy | Entry wedge + one domain | Energy-only product / EMS dashboard |
| Time / flow / exception | Domains on the same card | APS / logistics SKU / plant OS |
| Equipment / maintenance | May escalate with evidence | Full CMMS / vibration PdM company |
| MES / ERP | Read context | Dispatch / WIP / scheduling SoR |
| Agents | Latest-tech presentation for recommend + learn | The company itself |

---

## 10. Reading map (agents)

| Priority | Doc |
| --- | --- |
| 1 | [`AGENT-START.md`](../research/plant-efficiency-exploration-2026-09/AGENT-START.md) → [`09`](../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md) → [`10`](../research/plant-efficiency-exploration-2026-09/10-stamped-vision-agent-alignment.md) |
| 2 | [ADR-030](../decisions/028-032/ADR-030-five-domain-decision-loop.md) |
| 3 | **This file** (stack + layer map) |
| 4 | [handoff/README.md](../handoff/README.md) → your layer |
| 5 | [`contracts/`](../contracts/) + `scripts/contracts/contract-check.sh` |
| 6 | Layer specs under [`layers/`](layers/) as needed |
| Legacy names | Thin pointers in [`pointers/`](pointers/) redirect here |

Prior product snapshot: tag `v2026.09.24`. Marketing archive is not identity.
