# ADR-038: Soft gates, opportunity ledger, and exploration

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-25 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-033](ADR-033-l4-decision-runtime.md) · [ADR-036](ADR-036-dual-family-models.md) · [ADR-025](../024-026/ADR-025-improve-loop-step-06.md) · [`technical/l4/22-missed-opportunities.md`](../../technical/l4/22-missed-opportunities.md) · [`technical/l4/00-kernel.md`](../../technical/l4/00-kernel.md) |

---

## Context

Strict gates protect the floor from bad cards. The same strictness can hide real efficiency when **soft** thresholds are set too high. Learning from refusals must not reopen hard stops or send cards whose owner/action is still in dual-family dispute.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Gate typing | Every gate is `hard` or `soft`; every block records a canonical `gate_id` ([`00-kernel.md`](../../technical/l4/00-kernel.md) §11) |
| 2 | Hard gates | Never tunable, never in backlog, never explored — including **action-seam disagreement** (action / owner / constraint-affecting / verification / terminal) |
| 3 | Soft gates | Thresholds in registry; tunable by evidence. Soft list is routing agreement, one-family floors, evidence-tier mins, freshness margin, attention budget, cooldown, hypothesis volume, pattern precision — **not** action-seam disagreement |
| 4 | Opportunity ledger | Every blocked candidate kept with gate id, snapshot, later outcome if known |
| 5 | Owner backlog | Soft-gate blocks surface to the named plant owner’s backlog (customer Now queue still hides hard-gate withholds) |
| 6 | Exploration | Opt-in `exploration=true` cards only for **exploration-eligible** soft gate ids listed in [`22`](../../technical/l4/22-missed-opportunities.md). Never for hard gates. Always re-runs hard gates + kernel re-check before send |
| 7 | Origin vs flag | `exploration` is a **boolean flag**, not an `origin` enum value |
| 8 | Calibration | Soft gates loosen or tighten from ledger + exploration — never from one anecdote |
| 9 | Selection bias | Closure rate alone never ranks patterns |

---

## Consequences

- Refusals teach the system without shipping disputed cards.
- Hard gates stay frozen; soft-gate changes go through registry + replay + **plant owner** acceptance (global proposals still need per-plant accept or opt-in).
- Exploration is volume-capped and origin-preserving (`l3_finding` / `l4_pattern` / `l4_hypothesis`).

---

## Rejected alternatives

- Loosening hard stops to catch more opportunities.
- Exploring action-seam disagreements.
- Silent promotion of blocked candidates to emit.
- Ranking patterns by closure rate alone.
- Putting `exploration` in the `origin` enum.

---

## What would change this

- Measured evidence that a specific soft gate should become hard (or the reverse) with no rise in hard-stop hits → ADR + kernel bump.
- Plant refuses all exploration forever → calibration uses persistence/backlog only; state that limit in ops.

---

## v1 slice

Soft-gate registry + opportunity ledger + owner backlog + opt-in exploration for eligible soft gates only. Automated CI trade-off curves later.
