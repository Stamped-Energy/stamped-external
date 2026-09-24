# Work queue and concurrency

**Status:** Architecture (production hardness). Normative for always-on L4.  
**ADR:** [040](../../decisions/040-044/ADR-040-l4-production-hardness.md)  
**Siblings:** [`08-discovery.md`](08-discovery.md) · [`07-finding-runtime.md`](07-finding-runtime.md) · [`26-decision-case-lifecycle.md`](26-decision-case-lifecycle.md) · [`27-ports-and-reliability.md`](27-ports-and-reliability.md) · [`16-operations.md`](16-operations.md)

---

## Purpose

Findings, PSM events, shift sweeps, Ask sweeps, and backlog promotes arrive together. Without one queue architecture, L4 double-spends dual-family calls, races supersede, or silently drops work. This doc is the scheduler contract implementers must build.

---

## Decision

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Single plant work queue | One durable queue per `plant_id` (logical). All intake kinds enqueue here |
| 2 | Work item kinds | `finding`, `discovery_event`, `shift_sweep`, `ask_sweep`, `backlog_promote`, `recheck` |
| 3 | Priority | Strict order below; same priority → FIFO by `enqueued_at` |
| 4 | In-flight dedupe | Same `condition_key` (or sweep id) → merge or suppress, never two parallel DecisionCases that both may emit |
| 5 | Parallelism | Cap concurrent DecisionCases per plant; LLM-heavy stages never overlap for the same plant beyond the cap |
| 6 | Starvation | Lower priorities must still run: aging boost after registry timeout |
| 7 | Kernel unchanged | Queue never bypasses hard gates, money, or write ban |

---

## Priority (high → low)

| Priority | Kind | Why |
| --- | --- | --- |
| P0 | `finding` with exception-response family / exempt domain | Floor safety of attention |
| P1 | Other `finding` | Named detector conditions |
| P2 | `backlog_promote` | Human already asked |
| P3 | `discovery_event` (scoped) | Material plant change |
| P4 | `ask_sweep` | Staff on-demand |
| P5 | `shift_sweep` | Whole-plant cadence |
| P6 | `recheck` | Background refresh |

Exception attention exemption ([`09-portfolio.md`](09-portfolio.md)) applies to **emitted cards**, not to skipping the queue — P0 still goes through kernel.

---

## In-flight and dedupe rules

```text
enqueue(item)
  if item.kind == finding OR discovery candidate:
    if open DecisionCase for same condition_key in {running, awaiting_ports}:
      attach as supersede_candidate or drop (idempotent) — do not start second case
    if open L5 proposal for same condition_key (not accepted):
      new case may supersede only under kernel supersede rules
  if item.kind == shift_sweep:
    if shift_sweep for same shift_id already running or queued:
      drop duplicate (idempotent)
    if previous shift_sweep still in LLM stages:
      queue behind; do not start second LLM-heavy sweep
  if item.kind == discovery_event:
    coalesce events for same footprint neighbourhood within coalesce_window_ms
```

**Coalesce window** — registry soft knob (illustrative default 30s until site-locked).

---

## Parallelism caps (registry, plant-scoped)

| Cap | Meaning | v1 default intent |
| --- | --- | --- |
| `max_concurrent_decision_cases` | Running cases per plant | Small (e.g. 2–3) — lock in ops |
| `max_concurrent_llm_stages` | Cases inside dual-family draft/critique | 1 per plant recommended for Pilot |
| `max_scanner_parallelism` | Deterministic scanners only | Higher OK — no model |

Scanner-only work for a queued shift sweep may prepare shortlists while a Finding runs LLM stages. LLM stages still respect `max_concurrent_llm_stages`.

---

## Starvation and aging

If a P5/P6 item waits longer than `queue_aging_threshold` (registry), bump one priority step once. Never bump above P1. Log `queue_aged=true` on the work item.

---

## Fairness vs attention

The queue decides **what runs**. Portfolio attention budget decides **what emits to L5**. A shift sweep may produce many ranked candidates; only `max_candidates_to_runtime` enter DecisionCases ([`08-discovery.md`](08-discovery.md)); over-budget results → hold / opportunity ledger, not silent discard without a ledger row.

---

## Observability (required)

Every enqueue / dequeue / merge / drop emits:

- `work_item_id`, `kind`, `priority`, `plant_id`, `condition_key` or `shift_id`
- `correlation_id` (propagates into DecisionCase and DecisionTrace)
- reason if dropped or merged

On-call watches: queue depth by priority, age of oldest P0/P1, shift-sweep miss rate ([`16-operations.md`](16-operations.md)).

---

## Rejected alternatives

| Alternative | Why |
| --- | --- |
| Separate queues per kind with no cross-priority | Starves Finding under sweep load or vice versa |
| Unlimited parallel DecisionCases | Cost blast + supersede races |
| Dropping shift sweeps when busy with no ledger | Quiet-shift product claim dies silently |
| Queue that can skip constraint evaluator | Kernel violation |

---

## What would change this

- Measured queue wait showing P0 starved → raise Finding parallelism or lower sweep LLM share.
- Plants need mid-shift full sweeps as P4 → registry; replay attention impact.

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Single logical queue per plant; priorities above; coalesce + sweep dedupe | Multi-region queue HA |
| Caps in plant registry | Auto-tune caps from latency SLOs |
| Metrics exported | Same + SLO burn alerts |

---

## Change class

Queue priorities and caps: **data** (registry). Changing “queue may skip a hard gate”: **forbidden**. Adding a new work-item kind: **registry + this doc** + replay of concurrency suites.
