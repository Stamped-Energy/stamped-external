# Ports and reliability

**Status:** Architecture (production hardness).  
**ADR:** [040](../../decisions/040-044/ADR-040-l4-production-hardness.md)  
**Siblings:** [`16-operations.md`](16-operations.md) · [`26-decision-case-lifecycle.md`](26-decision-case-lifecycle.md) · [`15-l3-l4-interface.md`](15-l3-l4-interface.md) · [`11-models-and-seams.md`](11-models-and-seams.md)

---

## Purpose

L4 is a composition of ports. Production readiness is mostly how those ports fail. This doc defines deadlines, retries, circuit breakers, idempotency, and degraded outcomes — so implementers do not invent per-call behaviour.

---

## Port catalog

| Port | Direction | Side effect? |
| --- | --- | --- |
| `ModelSlot` | Out | No (paid tokens only) |
| `L3MethodsPort` | Out | No (calculator / condition / sim / verify-builder) |
| `BuilderReadPort` | Out | No (PSM bulk/list) |
| `AgentZoomPort` | Out | No (allowlisted zoom) |
| `MemoryPort` | Out | Read plant/dialogue; writes only typed learning via L5 path |
| `OeCorpusPort` | Out | No (advisory retrieval) |
| `L4Store` | In/out | Durable case/trace/ledger/PSM cache |
| `CardSink` | Out | **Yes** — deliver proposal to L5 |
| `WorkQueue` | In/out | Durable enqueue |

No port writes OT, schedules, or master data.

---

## Per-call contract (every outbound port)

| Field | Required |
| --- | --- |
| `deadline_ms` | Yes — from registry by port + latency_tier |
| `idempotency_key` | Yes when side effect or costly duplicate matters |
| `attempt` | Yes |
| `correlation_id` / `decision_case_id` | Yes |
| Result | `ok` \| `retryable` \| `non_retryable` \| `timeout` + typed error code |

---

## Retries

| Class | Policy |
| --- | --- |
| Retryable (5xx, timeout, rate limit) | Exponential backoff + jitter; max attempts from registry |
| Non-retryable (4xx schema, auth, envelope reject) | No retry; case → semantic path or `failed_infra` |
| `CardSink` | Retry with **same** `emit_idempotency_key`; L5 must be idempotent on that key |
| `ModelSlot` | Retry once on timeout; on persistent fail → one-family mode if configured else withhold / `failed_infra` per seam class |

Never retry a successful CardSink. Never invent a second emit key for the same terminalizing attempt.

---

## Circuit breakers

Per plant + port (+ provider for ModelSlot):

| State | Behaviour |
| --- | --- |
| closed | Normal |
| open | Fail fast `retryable` or degrade (below) |
| half-open | Probe one call |

Trip on error rate / consecutive failures (registry thresholds). Open breaker on `L3MethodsPort.calculator` → **no emit with ₹**; withhold or abstain — never invent money.

---

## Idempotency keys

| Operation | Key material (conceptual) |
| --- | --- |
| Finding intake | `plant_id + finding_id + finding_version` → same DecisionCase |
| CardSink emit/supersede | `decision_case_id + operation + proposal_content_hash` |
| Shift sweep enqueue | `plant_id + shift_id + sweep_kind` |
| Learning fact write | `closure_id + fact_schema_version` |

At-least-once delivery from L3 is assumed. Duplicate Finding → attach to existing case or no-op; never two emits for one finding id.

---

## Degraded modes (normative map)

| Failure | Plant path behaviour |
| --- | --- |
| Family A down | One-family mode if pinned; else withhold on action seams |
| Both families down | No draft; `failed_infra` or abstain with ops alert — no fake card |
| Calculator down | No priced emit; withhold if card needs ₹ |
| Condition test down | No discovery emit that requires it; Finding path may continue if Finding already carries floor |
| MemoryPort down | Continue without advisory memory; mark freshness/unknown; do not invent memory |
| OeCorpusPort down | Continue without OE advisory |
| BuilderRead / PSM stale past hard limit | Withhold when proof needs fresh state (`staleness_hard_limit`) |
| CardSink down | Retry; case stays `terminalizing`; alert; no “tell the model to try another channel” |
| L4Store down | **Stop leasing new cases**; fail closed |

---

## Security and tenancy (software strength)

| Rule | Detail |
| --- | --- |
| Plant isolation | Every port call scoped by `plant_id`; no cross-plant read in v1 |
| Secrets | Model API keys / DB creds never in traces or CardSink payloads |
| Authn/z | Service identity between L3/L4/L5; plant-scoped tokens for Ask/ops |
| PII | Roster/person resolution is L5; L4 holds roles, not personal phone dumps in OE corpus |
| Supply chain | Lockfile pins dependency versions for L4 services; SBOMs in release artifact |

---

## Rejected alternatives

| Alternative | Why |
| --- | --- |
| Infinite retries on CardSink | Duplicate cards without idempotency |
| Soft-fail calculator with model-estimated ₹ | Kernel money rule |
| Shared ModelSlot breaker across all plants | One noisy plant takes down fleet |
| Logging full prompts with secrets to the council export | Privacy ([`16`](16-operations.md)) |

---

## What would change this

- Measured L3 p99 forces higher deadlines → registry by latency_tier after Pilot.  
- Need multi-region CardSink → ADR for cross-region idempotency store.

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Deadlines, retries, breakers, idempotency keys as above | Automated breaker tuning |
| Fail closed on L4Store outage | Read replicas for PSM build |
| Manual breaker reset in ops | Same + audited |

---

## Change class

Deadlines / retry counts: **data**. Changing degraded mode so money can be invented: **forbidden**. New port: **this doc + registry + contract delta**.
