# ADR-035: L4 discovery (beyond Finding intake)

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-25 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-033](ADR-033-l4-decision-runtime.md) · [ADR-034](ADR-034-plant-situation-model-and-memory.md) · [`technical/l4/08-discovery.md`](../../technical/l4/08-discovery.md) |

---

## Context

L3 detectors catch registered conditions. Real plants also waste on overlapping starts, idle auxiliaries, handoff waits, partial loads, and shared-utility imbalance that no Finding names yet. L4 must surface some of that without becoming an unsupervised idea generator flooding the floor.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Mechanisms (order) | Deterministic temporal scanners → L3 system methods → L3 what-if methods → LLM hypotheses |
| 2 | Certified patterns | Registry entries with scanner predicate, footprint, domain, condition-key recipe, verification recipe, owner — emit through the normal decision runtime |
| 3 | Grounded-hypothesis lane | Per-plant owner opt-in; emit only when L3 condition test, pricing, verification plan, footprint, constraints, dual-family agreement, kernel, and volume cap all pass |
| 4 | Everything else | Shadow: traced, never sent to L5 |
| 5 | Origin | Hypothesis cards carry `origin=l4_hypothesis` |
| 6 | Auto-disable | Lane disables when rejected-plus-no-change exceeds the owner-set threshold |
| 7 | Pattern hand-off | When L3 ships a detector for a condition, the L4 pattern retires |
| 8 | Ranking | Feasibility floor, then lexicographic order from a versioned ranking-policy registry (no blended score) |
| 9 | Cadence | Event-triggered on material PSM changes **plus one shift sweep per shift** (whole-plant discovery pass). Finding intake remains separate. Detail: [`08-discovery.md`](../../technical/l4/08-discovery.md) |
| 10 | Origin (patterns) | Certified patterns emit with `origin=l4_pattern`; hypotheses with `origin=l4_hypothesis` |

---

## Consequences

- Discovery candidates meet the same kernel floor, constraint evaluator, and portfolio as Findings.
- Quiet shifts still get a whole-plant opportunity pass — selling point is not “wait for an alarm.”
- Precision tracked per pattern; auto-demotion to shadow on poor precision.
- Successful hypothesis types become pattern proposals for certification.

---

## Rejected alternatives

- Free LLM discovery emit without L3 grounding.
- Blended multi-objective score for ranking.
- Discovery that bypasses the portfolio or attention budget.
- Continuous full-plant LLM sweeps every few minutes (attention flood + cost).

---

## What would change this

- Plants need mid-shift full sweeps (not only event-scoped) → registry cadence, replay attention impact.
- Shift sweep always empty on Pilot → commissioning / scanner coverage, not “add more LLM.”

---

## v1 slice

One shift sweep per shift + event-scoped partial sweeps; certified patterns for Pilot scanners; hypothesis lane opt-in.
