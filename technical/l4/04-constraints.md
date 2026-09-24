# Constraints and resources

**Status:** Architecture. Kernel constraint rules: [`00-kernel.md`](00-kernel.md) §5.  
**Siblings:** [`03-plant-situation-model.md`](03-plant-situation-model.md) · [`09-portfolio.md`](09-portfolio.md) · [`22-missed-opportunities.md`](22-missed-opportunities.md)

---

## Purpose

“Code withholds on a known constraint conflict” is only true if code can evaluate the constraint. Plant constraints are mostly unwritten. This doc defines a minimal typed vocabulary, how rows are stored, how the evaluator works, and how tacit constraints become typed without an LLM deciding the gate.

---

## Constraint kinds (registry)

Admitted when a family or pattern uses one:

| Kind | Intent |
| --- | --- |
| `forbid` | Named action / state must not occur in scope |
| `must-run` | Asset or resource must remain available / running |
| `time_window` | Only valid inside / outside a window |
| `bound` | e.g. feeder max kW |
| `cumulative_capacity` | Shared resource capacity over a window |
| `mutual_exclusion` | Two footprints cannot both hold |
| `precedence` / min separation | A before B, or minimum gap |
| `reserve_margin` | Headroom that must remain |
| `availability` | Crew, material, fixture |
| `do_not_disturb_order` | Order / due as do-not-disturb context |

New kinds are registry entries + evaluator binding + replay — not a kernel edit ([`21-registries-and-stage-graph.md`](21-registries-and-stage-graph.md)).

---

## Constraint row

| Field | Meaning |
| --- | --- |
| scope | asset, flow edge, shared resource, area, plant |
| applicability | mode, product, shift, state |
| effective_time / recorded_time | bitemporal |
| severity | `hard` · `conditional-hard` · `advisory` |
| owner | named plant role |
| source | site pack, owner edit, proposed-from-rejection |
| expiry | optional |
| version | row version |

---

## Evaluator (code)

Returns `satisfied` | `violated` | `unknown`, plus the smallest conflicting fact set, recorded in the DecisionTrace.

| Result | Kernel |
| --- | --- |
| `violated` | `withhold` |
| `unknown` on hard / conditional-hard treated as hard for the neighbourhood | `withhold` (`reason=constraint_unknown`) |
| `satisfied` | continue |

The Constraint analysis **model** explains results and may flag possible conflicts. It **never** decides satisfied / violated / unknown. An LLM “possible conflict” without a code result → withhold ([`00-kernel.md`](00-kernel.md)).

Missing structure needed for a cross-asset check → `unknown` ([`02-plant-structure.md`](02-plant-structure.md)).

---

## Tacit constraints

Rejection reasons and owner edits become **proposed constraint rows**, routed to the named plant owner. Most real plant constraints are unwritten; this is how they become typed. Proposed rows are advisory until confirmed. Rejected proposals are remembered (same spirit as topology suggestions).

---

## Action footprint

Every candidate and open card carries:

- assets
- shared resources
- crew / role
- material
- time window with start, end, and lag

Portfolio conflict = footprint overlap **and/or** constraint evaluation conflict ([`09-portfolio.md`](09-portfolio.md)). The claims index in the PSM holds open-card footprints for that check.

---

## Hard vs soft (do not confuse)

| | Constraint severity | Kernel gate |
| --- | --- | --- |
| Hard constraint violated / unknown | severity on the row | **Hard gate** — never tunable |
| Soft gates (agreement, attention, …) | not constraint kinds | Soft gate registry ([`22-missed-opportunities.md`](22-missed-opportunities.md)) |

Advisory constraint severity may inform ranking and explanations; it does not by itself force withhold unless a family maps it into a hard neighbourhood.

---

## Why typed

Constraint-programming practice (precedence, no-overlap, cumulative resources) covers most shared-resource cases without a scheduler or a plant ontology. Prose in a prompt is not a gate.

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Kinds needed by Pilot families (forbid, bound, time window, availability, do-not-disturb, mutual exclusion where topology exists) | Full kind set as families commission |
| Code evaluator + unknown→withhold on hard | Same |
| Tacit → proposed rows → owner confirm | Same; richer suggestion UX |
| Advisory severity informs rank/explain only | Optional family maps of advisory→hard neighbourhoods |
