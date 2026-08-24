# Nearer future — Plant margin optimization

**Horizon:** Nearer than production-efficiency Rx.  
**Peer reference:** [CVector Plant Margin Optimization](https://www.cvector.com/solutions/plant-margin-optimization)  
**Status:** PARKED. Research only. See [`../README.md`](../README.md).

---

## DO NOT BUILD

**Agents must not implement, plan, or ADR this** unless the founder **explicitly** names this track and asks to start it (e.g. “build plant margin optimization from `future/near-term`”).

Until then: no contracts, no L3 ranker changes, no copy, no pilots scoped as “margin product.”

---

## What this is (one paragraph)

Score and rank operating decisions by **contribution margin ₹/$** — not energy ₹ alone and not OEE. Combine plant telemetry, optional ERP/inventory, and external signals (tariff/ToD/MD today; later feedstock/product prices where available) → scenario impact → human-approved prescriptions (shift load, feed/melt timing, storage, maintenance window) with audit trail. Same *category* as Stamped’s decision layer; richer scorecard than bill-only.

## Why nearer than production efficiency

- Fits “operational decision layer” better than MES/OEE.
- Overlaps ADR-024 trade-offs; does not invent a third OEE pillar by default.
- CVector’s public suite (margin + energy + asset health) is a close peer shape.

## Why not now

- India beachhead still wins on **HT bill / ToD / MD** proof; live commodity/feedstock APIs and shared unit economics are often missing.
- Needs commercial/cost data plants may refuse to share.
- Building it early dilutes the energy wedge and confuses EMS objections.

## When to unlock (founder only)

Explicit ask **plus** at least one of:

- Pilot asks for margin-scored moves (power + scrap/feedstock + offtake), not just kWh/₹ bill.
- Willingness to share SKU/contribution or scrap economics with Stamped.
- Separate ADR approved after that ask.

## Pointers

- Research Appendix D: [`../../technical/research/india-mes-ai-and-production-rx-opportunity.md`](../../technical/research/india-mes-ai-and-production-rx-opportunity.md)
- Do **not** confuse with later track: [`../later/production-efficiency-prescriptions.md`](../later/production-efficiency-prescriptions.md)
