# ADR-033: L4 decision runtime (Finding → card proposal)

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-25 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-030](../028-032/ADR-030-five-domain-decision-loop.md) · [ADR-031](../028-032/ADR-031-l1-l2-context-records.md) · [ADR-034](ADR-034-plant-situation-model-and-memory.md) · [ADR-035](ADR-035-l4-discovery.md) · [`technical/l4/00-kernel.md`](../../technical/l4/00-kernel.md) · [`technical/l4/07-finding-runtime.md`](../../technical/l4/07-finding-runtime.md) |

---

## Context

L3 emits Findings. L5 owns live cards and verification. Between them, L4 must turn a Finding into at most one owned card proposal — or withhold / abstain with a full trace. Prior notes (`14`, `15`, `17`, `18`) describe the seam shapes but not a runnable architecture. Peer systems and agent literature (see research `19`) show that free multi-agent debate fails industrial reliability; code-owned workflows with models inside steps do better.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Outer control | Code owns the stage graph, terminals, hard stops, money references, constraint evaluation, and the one-card rule |
| 2 | Inner work | Models draft candidates, critique with cited ledger ids, and fill registry-bounded seams |
| 3 | Terminals | `emit`, `supersede`, `withhold`, `abstain` — always with a DecisionTrace |
| 4 | Portfolio hold | L4-internal only; staff-visible; not sent to L5 |
| 5 | Dual family | Two independent plant model families draft blind; one revision for cited objections; no multi-round debate |
| 6 | Evidence | Claims without ledger citations are dropped; rupees only from L3 calculator references |
| 7 | Constraint | Code evaluates; violated or unknown-on-hard → withhold; cannot be overridden by modeled benefit |
| 8 | Normative kernel | [`00-kernel.md`](../../technical/l4/00-kernel.md) is the frozen yardstick; changes only via ADR + version bump + full replay |

---

## Consequences

- L4 is expandable through registries (domains, families, workflows, stages, patterns) without rewriting the kernel.
- Disagreement on action / owner / constraint / verification / terminal → withhold (amends the soft fallback in research `14`/`15`).
- Implementation lives in stamped-l4; this ADR and `technical/l4/` are the contract.

---

## Rejected alternatives

- Multi-round specialist debate as the decision mechanism.
- Model self-reported confidence as the card uncertainty.
- LLM as constraint evaluator or terminal judge.
