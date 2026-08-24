# Later future — Production efficiency / volume prescriptions

**Horizon:** Later than plant margin optimization.  
**Status:** PARKED. Research only. See [`../README.md`](../README.md).

---

## DO NOT BUILD

**Agents must not implement, plan, or ADR this** unless the founder **explicitly** names this track and asks to start it (e.g. “start production-efficiency Rx from `future/later`”).

Until then: no `prod_*` decision_class, no OEE M&V ledger, no third pillar, no MES repositioning.

---

## What this is (one paragraph)

A possible **third prescription lane** where hero outcomes are **production volume / efficiency** (throughput, OEE A×P×Q, cycle, scrap)—not energy ₹. Would need cycle/scrap/downtime feeds, new L3 engines, and throughput verification. Conflicts with current ADR-026 “no third Production/OEE/MES pillar” until that ADR is deliberately reopened by founder ask.

## Why later than margin

- Category risk: fights MES / DMO / OEE stacks (especially ITC / Nestlé-class / JBM).
- Data gap: Stamped has orders/qty for SEC and deadline-aware energy Rx—not OEE loss trees.
- EMS objection is fixed by job clarity (monitor vs assigned ₹), not by becoming a production product.

## Capability ladder (reminder)

| Level | Meaning | Policy today |
|-------|---------|--------------|
| 0 | Production as **co-benefit** on management Rx | Allowed under ADR-024/026 |
| 1 | Availability from energy/equipment stack | Allowed as energy/reliability framing |
| 2 | Production-hero Rx lane | **This doc — parked** |

Doing Level 0–1 on the main product is **not** permission to open Level 2.

## When to unlock (founder only)

Explicit ask **plus** kill criteria from research (memo §6), e.g.:

- ≥3 qualified pilots refuse energy-first unless OEE/units is the hero metric, **and**
- They will provide cycle/scrap/downtime feeds, **and**
- Category/legal review accepts near-MES positioning, **and**
- New ADR supersedes ADR-026 for this scope.

## Pointers

- Full research: [`../../technical/research/india-mes-ai-and-production-rx-opportunity.md`](../../technical/research/india-mes-ai-and-production-rx-opportunity.md)
- Prefer nearer track first if expanding: [`../near-term/plant-margin-optimization.md`](../near-term/plant-margin-optimization.md)
- Policy: [ADR-026](../../decisions/024-026/ADR-026-two-pillars-shared-context.md)
