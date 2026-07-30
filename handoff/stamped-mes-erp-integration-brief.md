# MES / ERP integration brief — integrate + MES-lite

> **Authority:** [ADR-024](../decisions/ADR-024-holistic-plant-decisions.md) · [L1](../technical/layers/L1-connect-and-normalise.md) · [L6 ERP reality](../technical/layers/L6-experience-and-integration.md) · [`production-order.json`](../contracts/schemas/production-order.json)  
> **Audience:** connectors-cloud / connectors-edge / L2 / L6  
> **Non-goal:** Stamped is **not** an MES

---

## 1. Positioning (ISA-95)

Stamped is a **read-only decision overlay** beside Level 3 (MES) and Level 4 (ERP). It recommends timing/maintenance actions; it does not dispatch orders, manage WIP, or own quality SPC.

| MOM domain | Stamped role |
| --- | --- |
| Production | **Read** orders/schedules; recommend timing |
| Maintenance | Prescribe (Pillar 2); optional CMMS webhook |
| Quality | Out of scope v1 |
| Inventory | SEC denominator only if exposed |

---

## 2. Tier A — Integrate (MES/ERP present)

| System | Protocol | Fields to map → ProductionOrder |
| --- | --- | --- |
| SAP S/4 / ECC | OData / IDoc / scheduled CSV | order_id, line, sku, qty, due_at, status |
| Oracle / Tally | REST / ODBC / export | same |
| SAP ME / Opcenter / custom MES | REST / DB view / CSV | WIP line state, charge windows, routing_step |
| CMMS (if separate) | REST / webhook | Open PM WO — suppress duplicate maint Rx |

**Outbound:** signed webhooks + SFTP/CSV for savings / WO hints — **no direct ERP writes** in P0–P2 (named connector only when ≥3 customers request).

L1 build: extend REST poller / file profile for `production_order` envelope record_type.

---

## 3. Tier B — MES-lite (no MES)

Minimum order context without scheduling:

1. **CSV template** upload (shift/daily): `order_id,line_id,department_id,sku,qty,due_at_utc,priority,status`
2. **Hot-order flag** in L6: supervisor marks critical orders for next 4h (`source=hot_order`, `hot=true`)
3. **Shift planner view** (read-only): known orders + Stamped timing overlays

Path B plants use Tier B; Path A may still use CSV as bootstrap before OData goes live.

---

## 4. Mapping checklist (per plant)

- [ ] Confirm ERP/MES vendor and export path
- [ ] Map plant lines → `line_id` / `department_id` ([plant-department-graph](../contracts/schemas/plant-department-graph.json))
- [ ] Due-date timezone = plant TZ
- [ ] Idempotent dedupe on `org|plant|order_id|window`
- [ ] Shadow: orders appear in L2 before enabling TradeoffEngine in production

---

## 5. Acceptance

1. Tier B CSV alone enables `order_context=known` on stagger Rx for pilot plant.
2. Tier A SAP/Tally export (when present) replaces manual CSV without schema change.
3. No Stamped UI path creates or releases production orders.
