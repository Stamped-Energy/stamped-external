# ADR-024: Holistic plant decisions — energy wedge + co-benefits + negotiation

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-07-30 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-013](ADR-013-counterfactual-savings-ledger.md) · [ADR-018](ADR-018-l4-pilot-execution-knowledge-reasoning.md) · [ADR-020](ADR-020-l5-mv-claim-governance.md) · [ADR-023](ADR-023-l6-ems-and-analyst-context.md) · [ADR-025](ADR-025-improve-loop-step-06.md) · [03-two-pillar-technical-bridge](../technical/03-two-pillar-technical-bridge.md) · [`production-order.json`](../contracts/schemas/production-order.json) · [`prescription-revision.json`](../contracts/schemas/prescription-revision.json) |

---

## Context

Stamped's management prescriptions (stagger, TOD shift, shed) optimise for energy/₹ without enough **order deadline**, **department incentive**, or **cross-shop** context. Supervisors cannot negotiate a prescription — only ack / defer / reject / dispute. Plants without MES have no order floor; plants with ERP/MES are not yet wired for due dates.

Product lock (2026-07-30):

1. Keep **₹ energy / bill** as the hero wedge.
2. Add **plant-effectiveness co-benefits** (order risk, OEE/throughput, downtime) on the same prescriptions.
3. **Integrate** MES/ERP where present; offer **MES-lite** order context where absent.
4. Do **not** replace MES dispatch, CMMS, or quality systems.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Positioning | Energy wedge + co-benefits; not a plant OS / MES |
| 2 | Decision class | Tag Findings/Rx: `maint` \| `mgmt_schedule` \| `mgmt_capacity` \| `mgmt_cross_dept` |
| 3 | Trade-off block | Required on **management-class** prescriptions; optional on maint |
| 4 | Orders | Read `ProductionOrder` from ERP/MES or MES-lite CSV/hot-order; never own dispatch |
| 5 | Departments | Minimal plant → department → line → asset graph in L2 |
| 6 | Negotiation | Bounded `PrescriptionNegotiation` surface (L4); human confirms every revision |
| 7 | MES stance | Tier A integrate · Tier B MES-lite · no MES replacement |
| 8 | Outbound | Webhooks / CSV / SFTP only — no direct ERP writes in P0–P2 |

---

## 1. Decision taxonomy

| Class | Examples | Order context | Negotiation |
| --- | --- | --- | --- |
| `maint` | SP drift inspect, leak survey, trip cluster | No | Optional |
| `mgmt_schedule` | Stagger, TOD shift, preheat timing | **Yes** | **Yes** |
| `mgmt_capacity` | CMD rightsize, shed vs keep line | **Yes** | **Yes** |
| `mgmt_cross_dept` | Coincidence across body/paint/assembly | **Yes** | **Yes** |

`decision_class` is additive on Finding / Prescription (see contracts). Pillar `value_domain` remains orthogonal (energy_efficiency vs equipment_health).

---

## 2. Trade-off block (management Rx)

Every management-class prescription MUST include a deterministic trade-off object (L3 TradeoffEngine → L4 formats prose):

| Field | Purpose |
| --- | --- |
| `energy_benefit` | ₹ / kWh / tCO₂e (calculator-owned) |
| `throughput_risk` | Order / line impact narrative + structured order refs |
| `oee_impact` | Optional co-benefit / risk |
| `recommended_window` | When to act without breaching due dates |
| `alternatives[]` | Bounded template alternatives |
| `department_owners[]` | Roles that must accept |

**Rule:** Never recommend stagger/shed for a line without checking open orders with `due_at` in the action window when order context exists. If order context is missing, set `order_context: unknown` and lower confidence — do not invent deadlines.

---

## 3. Negotiation boundary

Distinct from read-only Analyst ([ADR-023](ADR-023-l6-ems-and-analyst-context.md)):

| Concern | Rule |
| --- | --- |
| Input | Supervisor constraint text + structured chips (order_id, no_stagger_until, …) |
| Engine | L3 recomputes under constraints; L4 proposes revision |
| Output | `PrescriptionRevision` with `supersedes_rx_id`, diff, same template family |
| Safety | Template-bound parameters only; rules veto; agent never auto-commits |
| Audit | L5 `prescription.revised` + negotiation thread |

---

## 4. Non-goals

- MES scheduling / dispatch / WIP ownership
- Full CMMS / quality SPC
- OT write-back
- Auto-accept of negotiated revisions
- Cross-plant preference sharing (see ADR-025)

---

## Consequences

- Contracts: `production-order.json`, extended `production-record.json`, `prescription-revision.json`, optional trade-off on prescription
- Handoffs: MES/ERP brief, TradeoffEngine spec, negotiation loop spec, pilot stack checklist
- Product copy: six-step loop includes Improve (ADR-025); trade-off card on Rx UX
- L3 P1: deadline-aware stagger / TOD / shed ranking

---

## Alternatives considered

| Option | Rejected because |
| --- | --- |
| Reposition as plant decision OS | Dilutes wedge; MES scope creep |
| Energy-only Rx forever | Unusable for multi-dept management actions |
| Free-form agent rewrite of What | Safety / eval (bounded templates) |
| Direct SAP write-back for Rx | Indian ERP reality; webhook/CSV sufficient ([L6](../technical/layers/L6-experience-and-integration.md)) |
