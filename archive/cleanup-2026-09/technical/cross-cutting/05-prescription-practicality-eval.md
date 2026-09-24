---
type: Product Architecture
title: "L4 prescription practicality eval — rubric + demo gold"
description: "Eval gates for practical prescriptions. Gold bar is demo-decks/prescriptions-examples.md (shape and feasibility, not illustrative ₹)."
tags: [stamped-energy, l4, eval, prescriptions, adr-028]
timestamp: "2026-08-18T00:00:00Z"
---

# Prescription practicality eval

*Authority:* [ADR-028](../../decisions/028-032/ADR-028-dual-plant-graphs-and-path-d.md) · [plant context graphs](../layers/l4-l6/L4-plant-context-graphs.md) · gold cards: [prescriptions-examples.md](../../demo-decks/prescriptions-examples.md) · parent eval: [04-evaluation-and-quality.md](04-evaluation-and-quality.md)

Demo ₹ remains **`[illustrative]`**. Gold eval is **shape and feasibility**, not matching sample rupees.

---

## 1. Rubric (fail closed on any P0 miss)

| ID | Check | P0 |
| --- | --- | --- |
| P-1 | **What** is a floor action: asset + verb + parameter + stop/override — not “improve efficiency” | yes |
| P-2 | **Why** cites an observed deviation (tag or delta fact), not a slogan | yes |
| P-3 | **Who** is role + department; name only if roster (`owner_resolution`) | yes |
| P-4 | **When** survives Path D: orders + standby + ToD if those facts exist | yes |
| P-5 | **Effort** is honest (hours, permits, production sign-off) | yes |
| P-6 | **Impact** numbers match the calculator; illustrative labelled if unlocked | yes |
| P-7 | **Evidence** on flip / evidence_refs non-empty and resolvable | yes |
| P-8 | **Vertical overlay** when plant vertical ≠ generic (steel / cement / pharma / packaging) | yes if vertical known |
| P-9 | **Template family** preserved — no free-form What rewrite | yes |
| P-10 | **Lane labelled** `quality` or `template_fast_path`; compile-trace present on quality path | yes |

Judge scores language (P-1–P-5, P-8) **after** deterministic P-6/P-7/P-9. Judge never owns ₹.

---

## 2. Gold cases (10 demo cards)

Each case: required Path D facts the compiler must pack. A generated Rx **fails** if it emits the “not” row.

| # | Demo title | Required delta / live facts | Fail if |
| --- | --- | --- | --- |
| 1 | Hold second feeder 10 min | Two feeders + incomer MD window; stagger 8–12 min | Generic “reduce MD” |
| 2 | Gravure dryer warm-up 25 min earlier | ToD peak vs release time; job start unchanged | Change production start |
| 3 | Inspect COMP2 filter | SP +14% vs matched header; next low-load window | “Improve compressor efficiency” |
| 4 | Packaging aux off after 20 min idle | Output=0 + aux kW; SOP protect list | Shed safety loads |
| 5 | Batch chiller later | Batch.START vs hall temp band; ToD peak | Miss batch readiness |
| 6 | Negotiation / next-best | Standby air too low Tuesday; Job 447; Thursday 14:00–16:00 | Due = Tuesday 9–11 |
| 7 | Steel furnace holding | Roll delay ≥45 min; hold-safe SOP | Leave full holding kW |
| 8 | Cement mill after kiln | Kiln settle / 10 min; WHR prefer | Co-start mill+kiln as the advice |
| 9 | Pharma chiller setback | Validated setpoints only; occupancy=0 | Free-text set-point |
| 10 | CW pump P-12 recirc | Header high + bypass open + low demand | Vibration PdM project |

Vinayak / Ghaziabad variants should reuse #1/#3/#6 with plant tags.

---

## 3. How L5 staff use this

Internal console Eval tab shows judge scores next to AD-5 gate. If P-4 fails (infeasible Due) → withhold, even if AD-5 “has a when string.”

Consumer pytest (later pin): one fixture per gold row with packed live index + expected delta_facts kinds.
