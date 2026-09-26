# L4 — As-built decision runtime

*Status: as-built · 2026-09-26*  
*Repo:* `knowledge-reasoning` · package `stamped_l4`  
*Normative contract:* [`README.md`](README.md) · [`00-kernel.md`](00-kernel.md) · ADRs [033](../../decisions/033-039/ADR-033-l4-decision-runtime.md)–[040](../../decisions/040-044/ADR-040-l4-production-hardness.md)

This page maps **what is implemented today** under `src/stamped_l4/runtime/`. Prefer the numbered contract docs (`00`–`29`) for design rules; use this page for package paths and live compile behavior.

---

## Live compile path

```text
Finding envelope (emitted ∧ l4) or enqueue/sweep
  → PlantWorkQueue
  → DecisionRuntime.process_one()  (worker/decision_runner.py)
  → stages: candidates → constraints → portfolio → minimizer → kernel_recheck → terminal
  → DecisionTrace (always)
  → CardSink.deliver only if PlantFlags.can_emit()
```

**Semantic terminals:** `emit` | `supersede` | `withhold` | `abstain`.

**Not the compile path:** legacy LangGraph quality / Lane A graphs under `graph/` remain in the tree (analyst and history) but are **not** invoked from `worker/runner.py` for inbox/preview compile. Preview responses map terminals to legacy status strings; **`prescription` body is null** on the runtime path — card-proposal is the customer-facing proposal object.

Safe local default: `emit_enabled=false`, `shadow_only=true` (traces without sink delivery).

---

## Package map (`stamped_l4.runtime`)

| Package | Responsibility |
| --- | --- |
| `kernel` | Pure terminals, hard/soft gates, evidence tiers — no I/O |
| `contracts` | Pydantic models vs `external/contracts/schemas/intelligence/*` |
| `registry` | Versioned registries + default stage sequence |
| `psm` | Plant Situation Model snapshots / digest |
| `constraints` | Typed predicates + evaluator |
| `seams` | Dual-family model slots, budget, economy cache |
| `stages` | Intake floor, condition key, proof, stage executor |
| `portfolio` | Dedupe, conflict, supersede, attention, hold |
| `ledger` | Opportunity ledger + owner backlog |
| `discovery` | Scanners, shift sweeps, hypothesis lane hooks |
| `queue` | Plant work queue |
| `lifecycle` | DecisionCase states, leases, resume |
| `ports` | Protocols + reliability middleware |
| `control` | Flags, safe-start, kill switch |
| `sinks` | `StubCardSink` (file) · `HttpCardSink` |
| `trace` | DecisionTrace builder, replay |
| `obs` | In-process metrics |

**Trust:** kernel never imports adapters. `CardSink` is the only outbound side-effect for customer-facing proposals. `failed_infra` is ops/lifecycle, not a semantic withhold.

---

## Control flags (defaults)

| Flag | Default | Meaning |
| --- | --- | --- |
| `emit_enabled` | `false` | Allow sink when not shadowing |
| `shadow_only` | `true` | Full path, block sink |
| `kill_switch` | `false` | Engaged via kill API/CLI |
| `sweep_enabled` | `true` | Shift/sweep work |
| `discovery_shift_sweep_enabled` | `false` | Discovery scanners on sweep |
| `hypothesis_enabled` | `false` | Hypothesis lane |

`can_emit()` = emit on **and** not shadow **and** not kill.

---

## Surfaces

| Surface | Notes |
| --- | --- |
| HTTP inbox / preview | Runtime-backed; legacy path names kept |
| `/v1/runtime/*` | Cases, traces, ledger, backlog, flags, enqueue, kill |
| CLI `stamped-l4` | enqueue, sweep, flags, kill, trace, replay, bench |
| Ask Analyst | Read-only; does not emit cards |

---

## Storage note

Alembic migration `0003` creates durable runtime tables (cases, traces, queue, ledger, flags, …). Boot may persist control flags to SQLite; full SQL-backed case/trace loop wiring into `DecisionRuntime` may still use in-memory stores locally — check the consumer README / `EXTENSIVE_DECISION_RUNTIME.md` for the pin you are on.

---

## Related

- L3 Finding emit: [`../l3/04-finding-contract.md`](../l3/04-finding-contract.md)
- Handoff: [`../../handoff/l4/stamped-l4-architecture-handoff.md`](../../handoff/l4/stamped-l4-architecture-handoff.md)
