# Software quality and release gates

**Status:** Architecture (production hardness). How L4 stays a **product**, not a demo.  
**ADR:** [040](../../decisions/040-044/ADR-040-l4-production-hardness.md)  
**Siblings:** [`16-operations.md`](16-operations.md) · [`12-trace-and-eval.md`](12-trace-and-eval.md) · [`20-benchmark.md`](20-benchmark.md) · [`27-ports-and-reliability.md`](27-ports-and-reliability.md) · [`21-registries-and-stage-graph.md`](21-registries-and-stage-graph.md)

---

## Purpose

Decision integrity (kernel) is necessary but not sufficient. This doc locks the **software** contracts: versioning, tests, CI gates, schema evolution, observability SLOs, and store durability — so execution later cannot “skip the boring parts.”

---

## Versioning

| Artifact | Versioned how |
| --- | --- |
| `l4-kernel` | Semver in kernel doc + ADR on bump |
| Release lockfile | Content hash; immutable once pinned |
| Contracts L3↔L4↔L5 | Explicit schema version; dual-read on bump ([`18`](18-contract-deltas.md)) |
| Registries | Per-entry version + lockfile pin |
| OE corpus | Corpus version + embedding model id |
| Service builds | Git SHA + lockfile hash in CardSink provenance |

Breaking wire changes: dual-read window; never silent field reuse.

---

## Test architecture (required suites)

| Suite | Protects |
| --- | --- |
| Contract tests | Finding intake, CardSink payload, topology records |
| Kernel golden | Hard gates fire; money; write ban; disagreement withhold |
| Concurrency | Queue priorities, dedupe, sweep vs Finding ([`25`](25-work-queue-and-concurrency.md)) |
| Lifecycle | Crash resume, lease expiry, cancel, idempotent emit ([`26`](26-decision-case-lifecycle.md)) |
| Port fault injection | Timeouts, breakers, calculator down ([`27`](27-ports-and-reliability.md)) |
| Replay / pass^k | Frozen ledgers ([`12`](12-trace-and-eval.md), [`20`](20-benchmark.md)) |
| Discovery | Shift sweep enqueue idempotency; pattern shadow |
| OE advisory | OE on/off does not invent ₹ |
| Safe-start | Emit blocked when checklist false ([`28`](28-commissioning-and-controls.md)) |

No pin to plant default without green required suites for that lockfile candidate.

---

## CI / release gates (normative intent)

```text
PR → unit + contract + kernel golden
     → concurrency + lifecycle + fault injection (required for runtime PRs)
lockfile candidate → replay holdouts + pass^k
                  → shadow on plant
                  → canary
                  → plant owner accept (plant scope)
                  → pin
```

Soft-gate threshold PRs must attach opportunity-ledger evidence ([`22`](22-missed-opportunities.md)). Kernel PRs require ADR.

---

## Observability SLOs (architecture-level)

| SLI | SLO intent (ops locks numbers) |
| --- | --- |
| P0/P1 queue wait | Bound for exception Findings |
| Case wall success (terminal or held, not infra fail) | High % per latency tier |
| CardSink success after terminalizing | Near-perfect with idempotent retry |
| Shift-sweep completion per shift | ≥ 1 successful enqueue+finish or alert |
| Stale PSM hard-limit withholds | Alert on spike (data path) |
| Infra fail rate | Page; not soft-gate tune |

Every case carries `correlation_id` through queue → ports → trace → CardSink. Metrics join on `decision_case_id`.

**Abort vs withhold:** infra abort increments infra fail SLI; semantic withhold increments gate_id counters only.

---

## L4 store durability

| Concern | Rule |
| --- | --- |
| What is durable | Cases, traces, opportunity ledger, case library, held proposals, PSM snapshots, control-plane audit |
| RPO / RTO | Declared per deploy profile in ops runbook; architecture requires **non-zero** backup — no “disk is fine” |
| Replay corpus | Export of frozen ledgers retained per policy for pass^k |
| Backup test | Restore drill before first `emit_enabled` ([`28`](28-commissioning-and-controls.md)) |
| Encryption | At rest and in transit; keys not in git |

---

## Compatibility and migrations

- PSM element builders: expand/contract with admission rule.  
- Gate id renames: alias table for one lockfile generation.  
- Dropping a soft gate: migrate ledger queries; never delete historical rows.

---

## Rejected alternatives

| Alternative | Why |
| --- | --- |
| “We’ll add tests after Pilot cards ship” | Non-product |
| Pin without shadow | Floor risk |
| Metrics without correlation id | Cannot debug multi-port cases |
| Single shared DB user across plants | Tenancy hole |

---

## What would change this

- Suite runtime too slow for every PR → split required vs nightly; do not drop concurrency/lifecycle from release gate.  
- Multi-region → ADR for store replication and CardSink idempotency region.

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Suites + CI gates above; backup before emit | Automated canary scorecards in CI |
| SLO intents; ops locks numbers | Error budgets auto-block pins |
| Single-region durability | HA topology |

---

## Change class

SLO numbers: **ops data**. Removing a required suite from release gate: **ADR**.
