# 16 — Operations

**Status:** Architecture contract (docs)  
**Date:** 2026-09-25  
**Normative:** [`00-kernel.md`](00-kernel.md)  
**Related:** [ADR-010](../../decisions/006-010/ADR-010-deployment-profiles-and-portability.md) · [ADR-033](../../decisions/033-039/ADR-033-l4-decision-runtime.md) · [ADR-036](../../decisions/033-039/ADR-036-dual-family-models.md) · [ADR-038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md) · [ADR-039](../../decisions/033-039/ADR-039-registries-and-stage-graph.md) · [`11-models-and-seams.md`](11-models-and-seams.md) · [`12-trace-and-eval.md`](12-trace-and-eval.md) · [`13-improvement.md`](13-improvement.md) · [`22-missed-opportunities.md`](22-missed-opportunities.md)

L4 on a live plant is a pinned release, a dual-family model slot, and a short list of rates somebody watches. Humans still decide and execute. Ops owns availability and promotion discipline; it does not own money, hard stops, or card authority.

---

## Purpose

Say how L4 is deployed, what a release pins, how shadow and canary work, which rates on-call watches, and how the plant path stays separate from the offline improvement path.

---

## Decisions

| # | Decision | Reason |
| --- | --- | --- |
| 1 | Deploy through ADR-010 profiles (`cloud`, `local`, `local-dashboard`) | Same product, different residency; contracts stay invariant |
| 2 | Every plant deploy is a **release lockfile** hash | Replay and audit need one pin for registries, stage graph, kernel version, model pins, soft-gate thresholds |
| 3 | Model pins live in the lockfile; nothing auto-promotes | Silent pin drift is a failure mode ([`19-failure-modes.md`](19-failure-modes.md)) |
| 4 | Registry / prompt / threshold changes go **shadow → canary → pin** | Plant owner (plant scope) or Stamped tech lead (global) accepts before pin |
| 5 | Plant request path never calls the offline council | Opus/Sol improve offline; DeepSeek Flash + Luna (or configured pair) serve the floor ([ADR-036](../../decisions/033-039/ADR-036-dual-family-models.md)) |
| 6 | On-call owns rates and degraded modes, not semantic gate tuning | Soft-gate thresholds move through [`13-improvement.md`](13-improvement.md) and [`22-missed-opportunities.md`](22-missed-opportunities.md), not pager guesswork |

**Rejected:** floating “latest model” deploys; council models on the live path; plant-scoped silent registry edits without lockfile; treating withhold rate as a model-quality KPI alone.

**Would change this:** a certified air-gap profile that requires a different pin ceremony; measured evidence that canary windows are too short or too long for Pilot plants.

---

## Deploy profiles

| Profile | L4 models | Hindsight / memory | Offline council | Notes |
| --- | --- | --- | --- | --- |
| `cloud` | Hosted APIs in the dual-family slot (default) | Cloud Hindsight allowed | Stamped-operated, off plant path | Default Pilot 1 path |
| `local` | Self-hosted open weights in the same slots | Self-host or plant-local memory backend behind `MemoryPort` | Not required on site; may run in Stamped lab on exported traces | No internet; same contracts |
| `local-dashboard` | Same as `local` | Same as `local` | Same as `local` | Adds L6/internal UI per ADR-010 |

Ports (`ModelSlot`, `MemoryPort`, `L3MethodsPort`, `CardSink`, `L4Store`) stay stable across profiles. Providers and residency change; stage graph and kernel do not.

**v1 slice:** Pilot plants run `cloud`. Local modes stay design-portable; no Pilot claim that air-gap L4 is proven until a plant runs it.

---

## Release lockfile

One hash pins, at minimum:

- kernel version;
- stage-graph version;
- every registry entry version in scope (domains, families, workflows, stages, analyses, patterns, constraint kinds, tools, prompts, memory missions, ranking policy, soft-gate thresholds);
- model pins (provider, family id, revision or weight digest);
- L3 methods port / shared registry pack versions consumed at the L3–L4 seam.

Every DecisionTrace carries this hash ([`12-trace-and-eval.md`](12-trace-and-eval.md)). Replay of an old run uses the lockfile that was live then, not today’s tip.

Plant overrides layer on a global entry with explicit precedence and appear in the same lockfile digest for that plant.

---

## Model pins

| Slot | Default (illustrative until ops locks) | Promotion rule |
| --- | --- | --- |
| Family A | DeepSeek V4.1 Flash (`deepseek-flash`) | Replay + shadow + canary + owner accept; Pro replaces Flash in-slot the same way |
| Family B | GPT-5.6 Luna | Same |
| One-family mode | Two correlated samples; stricter soft thresholds; hypothesis lane off | Declared in lockfile; not a silent fallback |

Pins are data-class changes ([`17-change-guide.md`](17-change-guide.md)). Hosted vs self-hosted is a deploy-profile choice behind `ModelSlot`, not a kernel change.

---

## Shadow and canary

| Stage | What runs | What the plant sees |
| --- | --- | --- |
| **Shadow** | Candidate lockfile runs in parallel; terminals and cards are compared to the pinned lockfile; no L5 emit from the candidate | Staff can inspect diffs; owners are not flooded |
| **Canary** | Candidate serves a declared plant slice or traffic share | Real cards; exploration and backlog rules still apply |
| **Pin** | Lockfile becomes the plant default | Unpin = rollback to the previous hash |

In-flight runs stick to the lockfile they started under. Open cards keep their proposal lockfile reference; supersede after a pin uses the new lockfile and re-checks kernel gates.

Rollback never invents a third “hotfix” pin outside the lockfile ceremony.

---

## Monitoring (plant path)

On-call watches rates **and** the production-hardness signals. Full SLO intents: [`29-software-quality-and-release.md`](29-software-quality-and-release.md). Queue: [`25-work-queue-and-concurrency.md`](25-work-queue-and-concurrency.md). Lifecycle: [`26-decision-case-lifecycle.md`](26-decision-case-lifecycle.md). Ports: [`27-ports-and-reliability.md`](27-ports-and-reliability.md).

On-call watches rates, not narrative quality scores.

| Signal | What it means | First response |
| --- | --- | --- |
| **Withhold rate** (by gate id, hard vs soft) | Floor may be too strict, or evidence/L3/PSM is degraded | Split hard vs soft; hard spikes → data/constraint ownership; soft spikes → backlog + calibration queue |
| **Cross-family agreement rate** (per seam class) | Confidence signal health ([ADR-036](../../decisions/033-039/ADR-036-dual-family-models.md)) | Drop + rising withholds on action seams → check providers, prompts, or correlated outage |
| **Soft-gate block rates** (per gate id) | Feeds [`22-missed-opportunities.md`](22-missed-opportunities.md) scorecard | Sustained miss/foregone effect → improvement proposal, not pager threshold edit |
| **Exploration outcomes** (`exploration=true` closures) | Unbiased sample of soft-gate rejects | Spike in reject/no-change → pause exploration budget for that plant; do not loosen hard gates |
| **Latency by tier** | Exception (minutes), flow/time (~15 min), energy/cost (may be longer) | Queue depth, L3 methods health, model slot health |
| **PSM freshness / builder lag** | Stale as-known-at snapshots | Degraded mode: withhold when proof floor needs fresh state |
| **L3 methods / calculator errors** | Money path or condition test down | No invented rupees; withhold or abstain per kernel |
| **CardSink / L5 emit failures** | Proposal not delivered | Retry with idempotency ([`27`](27-ports-and-reliability.md)); do not “fix by asking the model again” |
| **Hypothesis-lane volume / auto-disable** | Discovery flood or precision collapse | Lane off until owner resets ([ADR-035](../../decisions/033-039/ADR-035-l4-discovery.md)) |
| **Shift-sweep completion / duration** | Whole-plant discovery cadence ([`08-discovery.md`](08-discovery.md)) | Missed sweep → queue backlog; overrun → shrink max_candidates or defer hypothesis stage |
| **Shift-sweep emit vs shadow ratio** | Are quiet shifts producing honest cards or only shadow? | Persistent zero emit with high scanner hits → ranking/attention/commissioning review |
| **Queue depth / age by priority** | Concurrency / starvation ([`25`](25-work-queue-and-concurrency.md)) | Raise caps or pause P5 sweeps; never drop P0 without alert |
| **Infra fail / timed_out rate** | Lifecycle vs semantic withhold ([`26`](26-decision-case-lifecycle.md)) | Page; do not tune soft gates |
| **Kill switch / shadow_only / emit_enabled** | Control plane ([`28`](28-commissioning-and-controls.md)) | Confirm intentional; audit who flipped |

Hard-gate block volume is audit and constraint-data ownership, not a soft-gate tuning input.

**Correlation:** every work item and DecisionCase carries `correlation_id` through ports, traces, and CardSink.

---

## On-call ownership

| Role | Owns | Does not own |
| --- | --- | --- |
| **L4 on-call (Stamped)** | Availability, lockfile deploy health, model slot health, rate alerts, degraded-mode runbooks, **kill_switch**, queue health | Soft-gate threshold values; hard-stop semantics; plant execution |
| **Plant owner (named)** | Plant overrides, hypothesis-lane opt-in, exploration budget opt-in, backlog promote/dismiss, topology confirmations, **emit_enabled accept**, plant kill_switch | Global registry pins; kernel changes |
| **Stamped tech lead** | Global pins after replay packs | Acting as plant executor |
| **Constraint / site-pack owner** | Constraint rows and topology truth in the site pack | L4 “workaround” emits |

Pager pages on availability and rate anomalies. Semantic “should this gate be 0.7 or 0.6?” is an improvement-loop ticket with an owner pack, not a 3 a.m. edit.

---

## Plant path vs offline path

```text
Plant request path
  L2 / L3 / site pack → PSM snapshot → stage graph (pinned lockfile)
  → dual-family plant models → kernel checkpoints → L5 or withhold/abstain
  → DecisionTrace + opportunity ledger row

Offline path (never on the request hot path)
  Traces + ledger + closures → Opus 5.5 + Sol council
  → proposals (prompt, registry, soft-gate, stage graph, Jev)
  → replay on holdouts → owner pack → shadow → canary → pin
```

Exported traces for offline work strip or tokenize per DPDP and plant contract. Offline labels do not write plant source-of-truth. Case library remains outcome authority when memory disagrees ([ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md)).

---

## Degraded modes (summary)

Normative port map and breakers: [`27-ports-and-reliability.md`](27-ports-and-reliability.md). Control plane: [`28-commissioning-and-controls.md`](28-commissioning-and-controls.md).

| Condition | Behaviour |
| --- | --- |
| One model family down | One-family mode if configured; else withhold on seams that require agreement |
| Both families down | No generative draft; `failed_infra` / abstain + alert — no fake card |
| L3 methods / calculator down | No priced rupee claims; withhold claims that need them |
| PSM stale beyond hard limit | Withhold (`staleness_hard_limit`) |
| Memory / OE corpus down | Run without advisory rows; do not invent |
| CardSink down | Stay `terminalizing`; retry with idempotency key; alert |
| L4Store down | **Stop leasing new cases**; fail closed |
| `kill_switch` | No new leases; no CardSink |

Infra failures are **not** soft-gate learning signals ([`26`](26-decision-case-lifecycle.md)). Humans on shift still run the plant. L4 being quiet is preferable to L4 guessing.

---

## L4 store (ops note)

The L4 operational store holds derived snapshots, traces, case library rows, registries/lockfile copies, the opportunity ledger, work-queue state, and control-plane audit. It does not hold plant source-of-truth ([ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md)).

**Durability:** backup + declared RPO/RTO; restore drill **before** first `emit_enabled` ([`28`](28-commissioning-and-controls.md), [`29`](29-software-quality-and-release.md)). Retention and DPDP follow the plant contract; keep traces/ledger long enough for calibration and replay.

**Offline export:** allow-listed fields only; strip secrets/PII per [`28`](28-commissioning-and-controls.md).

---

## Safe-start (ops)

Do not set `emit_enabled=true` until the commissioning checklist in [`28-commissioning-and-controls.md`](28-commissioning-and-controls.md) is green and the plant owner accepts. New plants start `shadow_only=true`.

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Cloud profile; dual-family hosted pins; lockfile + shadow/canary; queue + lifecycle + port contracts documented | Proven local profile; automated canary scorecards in CI ([`29`](29-software-quality-and-release.md)) |
| Manual rate dashboards + correlation ids | Per-gate scorecard wired to paging / error budgets |
| Kill switch + safe-start checklist | L6 owner controls with confirm |
| Cost/latency per sweep from Pilot traffic | Same as tuning input; never weakens hard stops |

---

## Change class

Operations procedures and dashboards are **data / plug-in** around stable ports. Changing hard gates, terminals, money ownership, or the write ban is **kernel** and needs an ADR ([`17-change-guide.md`](17-change-guide.md)). Production-hardness surfaces: [ADR-040](../../decisions/040-044/ADR-040-l4-production-hardness.md).
