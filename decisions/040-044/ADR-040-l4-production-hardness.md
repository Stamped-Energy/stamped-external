# ADR-040: L4 production hardness (queue, lifecycle, ports, controls)

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-25 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-033](../033-039/ADR-033-l4-decision-runtime.md) · [`25-work-queue-and-concurrency.md`](../../technical/l4/25-work-queue-and-concurrency.md) · [`26-decision-case-lifecycle.md`](../../technical/l4/26-decision-case-lifecycle.md) · [`27-ports-and-reliability.md`](../../technical/l4/27-ports-and-reliability.md) · [`28-commissioning-and-controls.md`](../../technical/l4/28-commissioning-and-controls.md) · [`29-software-quality-and-release.md`](../../technical/l4/29-software-quality-and-release.md) |

---

## Context

The L4 decision kernel (ADR-033–039) specifies correct single-case behaviour: gates, dual-family seams, discovery, opportunity ledger. An always-on plant also needs concurrency control, durable case lifecycle, port failure contracts, safe-start, kill switches, and release gates. Without those, implementation will ship a clever demo that fails under overlapping sweeps and Finding floods.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Work queue | One durable queue per plant; typed work items; strict priority; in-flight dedupe; parallelism caps ([`25`](../../technical/l4/25-work-queue-and-concurrency.md)) |
| 2 | DecisionCase lifecycle | Explicit states, leases, timeouts, cancel, crash resume; infra fail ≠ semantic withhold ([`26`](../../technical/l4/26-decision-case-lifecycle.md)) |
| 3 | Ports | Deadlines, retries, circuit breakers, idempotency keys; degraded mode map; fail closed on L4Store outage ([`27`](../../technical/l4/27-ports-and-reliability.md)) |
| 4 | Safe-start | `emit_enabled` false until commissioning checklist + plant owner accept ([`28`](../../technical/l4/28-commissioning-and-controls.md)) |
| 5 | Kill switch | Plant control-plane flag stops new leases and CardSink; audited |
| 6 | Software gates | Required test suites + lockfile shadow/canary/pin; observability SLOs; store backup before emit ([`29`](../../technical/l4/29-software-quality-and-release.md)) |
| 7 | Token budget | Required proof rows never silently truncated → withhold/abstain |
| 8 | Kernel | Unchanged: queue and ports cannot bypass hard gates or invent ₹ |

---

## Consequences

- stamped-l4 implementation must include queue, lifecycle store, port middleware, and control plane — not “later ops niceties.”
- Pilot emit is gated by safe-start, not by connector install day.
- On-call has a defined kill path.

---

## Rejected alternatives

- Stateless request/response DecisionCases only.
- Unlimited parallel LLM stages per plant.
- Emit before commissioning checklist.
- Treating infra timeouts as soft-gate learning signal.

---

## What would change this

- Multi-region Active-Active → new ADR for fencing and CardSink idempotency region.
- Area-scoped emit flags → registry extension under ADR-040 spirit, documented in `28`.

---

## v1 slice

Single-region; docs `25`–`29` + this ADR; implement before first production `emit_enabled`.
