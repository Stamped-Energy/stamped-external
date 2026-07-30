# ADR-026: Product framing — two pillars + shared context

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-07-30 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-024](ADR-024-holistic-plant-decisions.md) · [ADR-025](ADR-025-improve-loop-step-06.md) · [03-two-pillar-technical-bridge](../technical/03-two-pillar-technical-bridge.md) · Research canon: `Stamped_Two_Pillar_Technical_Framing_v1.md` |

---

## Context

Holistic plant work (orders, departments, trade-offs, negotiation, Improve) made Stamped easy to misread as a third product — MES / plant OS / production coordinator — or as three separate products (energy vs maintenance vs MES). That dilutes the sales story and invites scope creep.

Product lock (2026-07-30): **one product, two outcome pillars, shared context** (not a third pillar).

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Product shape | **One** Stamped Intelligence product (single L0–L6 core) |
| 2 | Outcome pillars | **Exactly two:** (1) Load & Energy Efficiency · (2) Prescriptive Equipment Intelligence |
| 3 | Shared context | Orders / MES-lite / ERP read, departments, trade-off block, negotiation, Improve — **enablers**, not pillars |
| 4 | Hero outcome | **₹ energy / bill** (efficiency) |
| 5 | Co-benefits | **Plant effectiveness** — OEE / order-on-time / downtime — on management Rx when context exists; **not** Pillar 3 |
| 6 | MES | Read + recommend only — **never** claim to be MES / CMMS / plant OS |
| 7 | Product split | **Forbidden** for now — no separate Energy / Maintenance / MES products or repos |
| 8 | Enforcement | All consumer agents and decks must use this framing (see consumer prompt) |

---

## 1. Mandatory thinking model

```text
One product
 ├── Pillar 1 — Load & Energy Efficiency Intelligence   (hero ₹)
 ├── Pillar 2 — Prescriptive Equipment Intelligence     (equipment early warnings)
 └── Shared context — orders, departments, tradeoffs, negotiation, Improve
```

**30-second pitch (canonical):**

1. We cut **energy cost** with assigned, evidence-verified actions (Pillar 1).  
2. Same stack flags **equipment issues early** for maintenance (Pillar 2).  
3. For schedule-type actions we read **orders/departments** so we do not break production — **not your MES**.  
4. Management Rx show **₹ energy** (hero) plus **effectiveness co-benefits** when context exists.

---

## 2. Language lock

| Say | Do not say |
| --- | --- |
| Two pillars + shared plant context | Third pillar / plant OS / MES product |
| Energy efficiency (hero ₹) | Energy-only forever |
| Plant effectiveness / OEE co-benefits on Rx | We optimize OEE as a separate product |
| Prescriptive equipment intelligence | Vibration PdM company / full CMMS |
| Read ERP/MES orders | We replace MES scheduling |

---

## 3. How ADR-024 / ADR-025 sit under this

| Artifact | Role under ADR-026 |
| --- | --- |
| ADR-024 trade-offs, orders, negotiation | **Shared context** making Pillar 1 management Rx practical |
| ADR-025 Improve loop | **Shared loop step 06** — not a pillar |
| ProductionOrder / department graph | Context stores — not a MES module |

---

## 4. Non-goals

- Third outcome pillar (Production / OEE / MES)  
- Splitting the core into multiple products before pilot proof  
- Building a full OEE / MESA performance product  

Commercial SKUs later (e.g. Energy vs Energy+Equipment) may package the **same** two pillars — they must not invent a MES SKU.

---

## Consequences

- Update two-pillar bridge, product architecture, holistic consumer prompt + audit  
- Sync research-repo canon (`Stamped_Two_Pillar_Technical_Framing_v1.md`)  
- Agents that invent a third pillar or MES product are out of policy  

---

## Alternatives considered

| Option | Rejected because |
| --- | --- |
| Three pillars (Energy / Equipment / Production) | Harder to explain; implies MES-class scope |
| Split into three products | Premature; multiplies decks/repos before closure proof |
| Drop Pillar 2 | Undoes locked two-pillar technical framing |
| Energy-only forever | Makes management Rx (stagger) unusable without order context |
