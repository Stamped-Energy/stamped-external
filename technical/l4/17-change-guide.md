# 17 — Change guide

**Status:** Architecture contract (docs)  
**Date:** 2026-09-25  
**Normative:** [`00-kernel.md`](00-kernel.md)  
**Related:** [ADR-033](../../decisions/033-039/ADR-033-l4-decision-runtime.md) · [ADR-038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md) · [ADR-039](../../decisions/033-039/ADR-039-registries-and-stage-graph.md) · [`21-registries-and-stage-graph.md`](21-registries-and-stage-graph.md) · [`12-trace-and-eval.md`](12-trace-and-eval.md) · [`13-improvement.md`](13-improvement.md) · [`16-operations.md`](16-operations.md)

L4 is built to change at the edges and, when needed, at the core — without rewriting the kernel every time. Almost every expansion is a registry entry, a replay pack, and a new lockfile pin. A few surfaces never move without an ADR.

---

## Purpose

Give a recipe for each common expansion, say what every recipe shares (registry + replay + lockfile), and draw the line where ADR + kernel bump is mandatory.

---

## Decisions

| # | Decision | Reason |
| --- | --- | --- |
| 1 | Four change classes: data, plug-in, structural, kernel | Cheap changes stay cheap; rare changes stay rare ([ADR-039](../../decisions/033-039/ADR-039-registries-and-stage-graph.md)) |
| 2 | Every data/plug-in/structural change ships through **registry entry → replay → shadow → canary → lockfile pin** | Same ceremony; different ports |
| 3 | Kernel refers to registries by id; never lists domains or stages by name | A sixth domain must not require a kernel edit |
| 4 | Hard gates, terminals, money ownership, and the write ban never change without ADR + kernel version bump + full replay | These are the frozen yardstick ([`00-kernel.md`](00-kernel.md)) |

**Rejected:** silent plant registry edits; free agents inventing stages at runtime; soft-editing hard stops to “catch more opportunities”; blending change classes into one approval path.

**Would change this:** measured evidence that a surface currently called kernel should be a registry (would need ADR); or that replay suites miss a class of regressions.

---

## Shared path (every recipe below)

1. **Registry entry** — id, semver, status (`draft | shadow | certified | retired`), scope (global or plant override), owner, dependencies, triggered replay suites, deprecation window.
2. **Replay** — candidate lockfile vs pinned lockfile on the required suites ([`12-trace-and-eval.md`](12-trace-and-eval.md)). Holdouts the proposers never saw.
3. **Owner pack** — plant owner for plant scope; Stamped tech lead for global.
4. **Shadow → canary → pin** — ([`16-operations.md`](16-operations.md)). Unpin rolls back.

No path skips the lockfile. Nothing promotes itself.

---

## Change classes

| Class | What moves | Code? | Ceremony |
| --- | --- | --- | --- |
| **Data** | Registry content only | No | Registry + replay + pin |
| **Plug-in** | New code behind an existing port | Yes, behind port | Port conformance + data path |
| **Structural** | Stage graph topology / order | Graph registry release | Must still hit fixed kernel checkpoints; portfolio after constraint evaluator |
| **Kernel** | Terminals, hard stops, money ownership, write ban, constraint semantics at the gate | Yes | **ADR + kernel version bump + full replay** |

---

## Recipes

### Domain

| Step | Action |
| --- | --- |
| Registry | Domain entry: claim kinds, effect units, evidence/verification types, L3 calculator/verification methods, analysis contract, owner roles, cross-section interactions, portfolio flags (e.g. attention exempt), section rendering spec ref, “sections never summed” |
| Plug-in | Domain analysis behind `DomainAnalysis` port |
| Seams | Options appear from registry ids — no seam code change |
| L3 | Methods / detectors as needed via shared pack |
| L5 / L6 | Store section by id; render from rendering spec |
| Product framing | Adding to the **product** story still needs ADR-030 amendment; architecture accepts the registry entry now |
| Suites | Per-domain regression + cross-section conflict + portfolio |

**Class:** data + plug-in. Not kernel.

### Family (decision family)

| Step | Action |
| --- | --- |
| Registry | Family id, allowed workflows, proof obligations, default owner-role set, condition-key hooks |
| Replay | Family holdout suite + terminal accuracy |
| Lockfile | Pin family version |

**Class:** data.

### Workflow

| Step | Action |
| --- | --- |
| Registry | Workflow recipe: stages used, seam option bindings, latency tier |
| Replay | Workflow suite on held-out DecisionCases |
| Lockfile | Pin |

**Class:** data (unless it needs a new stage → structural).

### Stage (pipeline stage)

| Step | Action |
| --- | --- |
| Registry | Stage id, typed in/out, version, place in stage graph |
| Checkpoints | Graph must still satisfy [`00-kernel.md`](00-kernel.md) §12 (constraint → portfolio → minimizer → re-check → terminal). Do not restate or weaken that list here. |
| Replay | Old graph lockfile vs new graph lockfile |
| Lockfile | Stage-graph version bump |

**Class:** structural. Changing the checkpoints themselves is kernel + ADR.

### Analysis (domain analysis field / plug-in)

| Step | Action |
| --- | --- |
| Registry | Bind analysis id to domain id; declare reads, claim kinds, forbidden claims |
| Plug-in | Implement `DomainAnalysis` contract |
| Conformance | Port tests: no money invention, no constraint evaluation, citations required |
| Replay | Domain suite |

**Class:** plug-in (+ data binding).

### Pattern (discovery)

| Step | Action |
| --- | --- |
| Registry | Scanner predicate, footprint, domain, condition-key recipe, verification recipe, owner; status starts `shadow` |
| Path | Emit only when `certified`; shadow traces otherwise ([ADR-035](../../decisions/033-039/ADR-035-l4-discovery.md)) |
| Hand-off | When L3 ships a detector, retire the L4 pattern |
| Replay | Pattern holdout + precision/recall ([`20-benchmark.md`](20-benchmark.md)) |

**Class:** data (+ scanner plug-in if new scanner code).

### Constraint kind

| Step | Action |
| --- | --- |
| Registry | Predicate kind, evaluator rule, behaviour on **unknown** (hard → withhold; never “treat as ok”) |
| Code | Evaluator in constraint engine — models never evaluate |
| Replay | Adversarial constraint suite |

**Class:** data + deterministic evaluator code (not LLM). Semantics of hard unknown remain kernel-aligned.

### Tool

| Step | Action |
| --- | --- |
| Registry | Tool id, port (`ToolAdapter` / L3 methods / builder read), allowed callers, least privilege |
| Ban | No equipment write tools; write ban is kernel |
| Replay | Tool contract + grounding tests |

**Class:** plug-in. New write capability = kernel + ADR (rejected in v1).

### Prompt

| Step | Action |
| --- | --- |
| Registry | Prompt id, seam or stage binding, version, ACE/GEPA bullet deps |
| Replay | Seam calibration + terminal accuracy on holdouts |
| Lockfile | Pin |

**Class:** data.

### Memory mission

| Step | Action |
| --- | --- |
| Registry | Mission id, tags, reflect-only directives, mental-model questions (owner-gated) |
| Writes | Typed only; case library wins on outcome conflict ([ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md)) |
| Replay | Memory poisoning / negative-memory suites |

**Class:** data (backend swap = plug-in behind `MemoryPort`).

### Model pin

| Step | Action |
| --- | --- |
| Registry | Slot, provider, family, revision/digest |
| Replay | Dual-family agreement calibration; one-family mode if applicable |
| Ops | Shadow → canary → pin ([`16-operations.md`](16-operations.md)) |

**Class:** data.

### Soft-gate threshold

| Step | Action |
| --- | --- |
| Registry | Gate id, threshold, scope, owner ([ADR-038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md)) |
| Evidence | Opportunity ledger scorecard + exploration — both directions ([`22-missed-opportunities.md`](22-missed-opportunities.md)) |
| Replay | Threshold trade-off curves on ledger holdouts |
| Ban | Hard gates are not thresholds |

**Class:** data.

### Ranking policy

| Step | Action |
| --- | --- |
| Registry | Ordered lexicographic criteria (no blended score); versioned |
| Replay | Portfolio regret + attention-budget suites |
| Lockfile | Pin |

**Class:** data.

---

## What requires ADR + kernel bump

| Surface | Why |
| --- | --- |
| New or removed **terminal** | Changes what L5 may receive |
| **Hard gate** set or semantics (hard stops, unknown-on-hard, proof floor, invented-rupee ban, write ban) | Frozen yardstick |
| **Money ownership** (who may mint a rupee reference) | Calculator path only; L3 owns methods |
| **Write ban** / equipment actuation from L4 | HITL; read-default |
| Constraint evaluation leaving code | Model-as-gate is rejected |
| Anything that lets emit bypass kernel checkpoints | Stage graph would stop being safe to expand |

Path: write ADR → bump kernel version in [`00-kernel.md`](00-kernel.md) → full replay across suites → shadow/canary/pin with tech-lead acceptance.

---

## What never changes without ADR

These are not soft preferences:

1. **Hard gates** — not tunable by ledger calibration; wrong hard blocks are data/constraint ownership problems ([`22-missed-opportunities.md`](22-missed-opportunities.md)).
2. **Terminals** — `emit`, `supersede`, `withhold`, `abstain` (plus hold as L4-internal, not a terminal to L5).
3. **Money ownership** — L3 calculator references only; models never assign rupees or evidence tiers.
4. **Write ban** — L4 does not write equipment or schedule; humans execute; L5 records.

Also fixed without this guide’s data path: L2 remains plant source of truth; PSM is derived cache; no multi-round debate as the decision mechanism ([ADR-033](../../decisions/033-039/ADR-033-l4-decision-runtime.md)); unknown on hard → withhold; one-card / one-owner rules.

---

## Production hardness (required for product emit)

Implement and change via [ADR-040](../../decisions/040-044/ADR-040-l4-production-hardness.md) docs — not optional “ops later”:

| Doc | Surface |
| --- | --- |
| [`25`](25-work-queue-and-concurrency.md) | Queue priorities, caps, dedupe |
| [`26`](26-decision-case-lifecycle.md) | Case states, leases, resume |
| [`27`](27-ports-and-reliability.md) | Port deadlines, breakers, idempotency |
| [`28`](28-commissioning-and-controls.md) | Safe-start, kill switch |
| [`29`](29-software-quality-and-release.md) | Suites, CI, SLOs, durability |

Caps and deadlines are **data**. Removing safe-start or fail-closed L4Store behaviour needs an ADR.

---

## Worked sketches

### Add a sixth domain

Shared registry pack gains the domain entry → L3 adds methods/detectors → L4 adds analysis plug-in → seams pick up the id → L5 stores the section id → L6 uses rendering spec → replay domain + cross-section suites → pin. Kernel untouched. Product marketing still waits on ADR-030 if the domain is sold as first-class.

### Insert a pipeline stage

New stage registry entry + stage-graph release → confirm kernel checkpoints still fire in order → replay old vs new graph → pin. Do not put portfolio before the constraint evaluator.

### Swap memory backend

New `MemoryPort` adapter → conformance tests → same mission registry → replay poisoning/outcome-authority suites → pin. Missions unchanged.

### Allow model to override a feeder bound for savings

**Rejected.** Hard gate. Would need ADR and should not ship.

---

## Doc dependency map (when a surface moves)

| Surface | Update these docs |
| --- | --- |
| Domain / family / pattern / constraint kind | `21`, `10`, `08`, `04`, `18`, shared registries |
| Stage graph | `21`, `01`, `07`, this guide |
| Soft-gate threshold | `22`, `13`, `16`, ADR-038 |
| Model pin / seam | `11`, `16`, ADR-036 |
| Kernel / terminals / hard gates | `00`, ADR-033, this guide, [`19-failure-modes.md`](19-failure-modes.md) |
| Money / L3 tools | `15`, `18`, SSOT sync |

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Recipes above as the contract; fitness checks stated for CI | Automated fitness CI: no hard-coded domain names outside seed; every stage typed/versioned |
| Five domains in product framing | Sixth domain when ADR-030 and Pilot evidence agree |

---

## Change class of this document

This guide is **data** relative to the kernel: clarifying recipes does not change terminals. If a recipe contradicts [`00-kernel.md`](00-kernel.md), the kernel wins until an ADR says otherwise.
