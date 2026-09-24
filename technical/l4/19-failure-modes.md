# 19 — Failure modes

**Status:** Architecture contract (docs)  
**Date:** 2026-09-25  
**Normative:** [`00-kernel.md`](00-kernel.md)  
**Related:** [ADR-033](../../decisions/033-039/ADR-033-l4-decision-runtime.md) · [ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md) · [ADR-036](../../decisions/033-039/ADR-036-dual-family-models.md) · [ADR-037](../../decisions/033-039/ADR-037-site-pack-topology.md) · [ADR-038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md) · [`16-operations.md`](16-operations.md) · [`22-missed-opportunities.md`](22-missed-opportunities.md)

Named ways L4 goes wrong on a plant — each with a detection signal and a mitigation that points at the kernel or a sibling doc. When L4 is wrong, the plant should see silence or a clear withhold, not a confident bad card.

---

## Purpose

Give on-call, plant owners, and L4 engineers a shared catalog. Prefer detection and ownership over hope that “the model will be careful.”

---

## Decisions

| # | Decision | Reason |
| --- | --- | --- |
| 1 | Failure modes are named and monitored | Anonymous “quality” dashboards hide the mechanism |
| 2 | Mitigations cite kernel/docs, not new soft tips | Sacred rules stay in one place |
| 3 | HITL stays: bad L4 → withhold/abstain/hold; humans still run the plant | No silent controller recovery |

**Rejected:** treating debate as a reliability feature; averaging judge scores into gates; fixing hard-gate pain by loosening hard stops.

**Would change this:** a Pilot incident that needs a new named mode; retire a mode only when its detection stays dark across plants and the mitigation is obsolete.

---

## Catalog

### 1. Debate cascades

**What:** Multi-round specialist debate or voting replaces the stage graph; latency explodes; confidence floats free of ledger citations.

**Detection:** Stage-graph version shows non-registry stages; trace step count / revision rounds exceed the allowed one revision for cited objections; terminals delayed past tier SLO without L3/PSM faults.

**Mitigation:** Code owns the graph; one blind dual-family draft + one cited critique revision; no debate/voting ([ADR-033](../../decisions/033-039/ADR-033-l4-decision-runtime.md), [`11-models-and-seams.md`](11-models-and-seams.md), [`00-kernel.md`](00-kernel.md)).

---

### 2. Graph-as-product

**What:** L2 (or L4) becomes a plant-wide ontology / traversable graph product; every topology tweak is a store migration; models walk the graph.

**Detection:** New L2 schema requiring graph migrate for site-pack edits; model tool traces showing traverse/hop APIs; PSM elements without admission from family/pattern/constraint kind.

**Mitigation:** Site-pack topology is structure SSOT via L1→L2 typed records ([ADR-037](../../decisions/033-039/ADR-037-site-pack-topology.md)); PSM is a derived cache ([ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md)); builder walks in code; models get typed zoom reads only. ADR-031: no `graph/traverse` for models. See [`02-plant-structure.md`](02-plant-structure.md).

---

### 3. Invented rupees

**What:** A model or prompt writes a rupee / savings figure that is not an L3 calculator reference; wallets get summed into a headline number.

**Detection:** Card or candidate with money fields lacking calculator ref ids; evidence tier set by model; summed multi-section ₹ in UI or trace; grounding violation counters up ([`12-trace-and-eval.md`](12-trace-and-eval.md)).

**Mitigation:** Kernel drops uncited claims; rupees only from L3 calculator path; sections never summed ([`00-kernel.md`](00-kernel.md), [`15-l3-l4-interface.md`](15-l3-l4-interface.md)). Degraded: L3 down → no priced claims.

---

### 4. Memory poisoning

**What:** Untyped memory writes, Ask/decision bank bleed, or Hindsight “lessons” override case-library outcomes and soft thresholds.

**Detection:** Memory write without typed schema; disagreement where Hindsight outcome ≠ case library without a traced resolution; soft-gate thresholds changing outside lockfile; reflect directives applied on the plant path.

**Mitigation:** Typed writes only; case library is outcome authority; Ask banks walled from decision thresholds; mental-model questions owner-gated; advisory rows frozen into the ledger per run ([ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md), [`06-memory.md`](06-memory.md)). Thresholds move only via [`17-change-guide.md`](17-change-guide.md) / [`22-missed-opportunities.md`](22-missed-opportunities.md).

---

### 5. Correlated dual-family error

**What:** Both “families” share provider, prompt lineage, or one-family mode without stricter gates; agreement becomes false confidence.

**Detection:** Agreement rate high while accept/reject quality falls; provider outage couples both slots; lockfile shows same family twice; one-family mode without stricter soft thresholds / hypothesis lane off.

**Mitigation:** Two families by default; disagreement on action/owner/constraint/verification/terminal → withhold ([ADR-036](../../decisions/033-039/ADR-036-dual-family-models.md)); agreement is not proof — evidence and constraints still gate; calibrate agreement against outcomes ([`20-benchmark.md`](20-benchmark.md)); one-family mode is an explicit, stricter pin ([`16-operations.md`](16-operations.md)).

---

### 6. Unknown treated as ok

**What:** Missing constraint data, stale evidence, or unknown evaluator result is waved through because the modeled benefit “looks large.”

**Detection:** Constraint result `unknown` paired with emit/supersede; proof-obligation skip; freshness soft-gate bypassed; hard-constraint unknown not withheld.

**Mitigation:** Code evaluates constraints; violated **or** unknown-on-hard → withhold; modeled benefit cannot override ([`00-kernel.md`](00-kernel.md), [`04-constraints.md`](04-constraints.md)). Unknown hard blocks go to the ledger for audit only — never backlog/explore ([ADR-038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md)).

---

### 7. Attention starve

**What:** Attention budget holds everything that is not an exception; owners see empty queues while soft-gate backlog and holds rot; or the opposite — exception exemption abused so the budget never binds.

**Detection:** Hold queue growth with low emit; owner accept rate starved by silence; exception-exempt share of cards far above registry intent; backlog age up without promote/dismiss.

**Mitigation:** Per-role per-shift budget; exception exemption only via domain registry flag; holds are L4-internal and staff-visible ([`09-portfolio.md`](09-portfolio.md)); soft-gate items surface on the owner backlog ([`22-missed-opportunities.md`](22-missed-opportunities.md)); ranking policy is versioned, not a blended score.

---

### 8. Selection bias

**What:** The system learns only from cards it sent; soft gates hide their own misses; patterns ranked by closure rate alone look “precise” because borderline wins never shipped.

**Detection:** Improving closure rate with rising soft-gate miss/foregone effect; pattern rank by closure without ledger/exploration; no `exploration=true` sample on an opted-in plant.

**Mitigation:** Opportunity ledger + observed persistence + later confirmation + exploration ([ADR-038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md), [`22-missed-opportunities.md`](22-missed-opportunities.md), [`13-improvement.md`](13-improvement.md)). Closure rate alone never ranks patterns.

---

### 9. Silent promotion

**What:** Shadow patterns, blocked candidates, or lab detectors become live emits without lockfile pin, owner accept, or hard-gate re-check.

**Detection:** Emit with registry status ≠ `certified` (patterns); backlog item becoming a card without promote action; lockfile hash on trace ≠ deployed pin; threshold/playbook change without owner accept.

**Mitigation:** Shadow → canary → pin ([`16-operations.md`](16-operations.md)); owner promote re-runs hard gates ([`22-missed-opportunities.md`](22-missed-opportunities.md)); nothing self-promotes ([ADR-039](../../decisions/033-039/ADR-039-registries-and-stage-graph.md), [`13-improvement.md`](13-improvement.md)). Hard-gate items never explore and never auto-surface as backlog.

---

### 10. Topology drift

**What:** PSM structure diverges from site-pack truth; L4 suggests topology that never gets owner-confirmed; cards reference dead assets or miss shared feeders.

**Detection:** PSM builder warnings vs site-pack version; footprint assets absent from L2 topology records; recurring constraint unknowns on structure predicates; suggestion queue age without confirm/reject.

**Mitigation:** Site pack is structure SSOT; L4 may suggest, named owner confirms into the pack ([ADR-037](../../decisions/033-039/ADR-037-site-pack-topology.md)); rejection memory on declined suggestions; PSM rebuild from published records; withhold when structure proof obligations fail ([`02-plant-structure.md`](02-plant-structure.md), [`03-plant-situation-model.md`](03-plant-situation-model.md)).

---

## Related modes (same discipline)

| Mode | Signal | Mitigation |
| --- | --- | --- |
| Simulator out of envelope | Modeled claim supports emit outside validated use | Envelope check before emit ([`15-l3-l4-interface.md`](15-l3-l4-interface.md)) |
| Hypothesis flood | Many `l4_hypothesis` cards | Volume cap; auto-disable; precision demotion ([`08-discovery.md`](08-discovery.md)) |
| Supersede after accept | Quiet replace of accepted work | Forbidden; separate card or conflict note ([`09-portfolio.md`](09-portfolio.md)) |
| Ask as second judge | Chat overrides withhold | Ask is view-only ([`14-ask.md`](14-ask.md)) |
| pass^k instability | Same ledger, different hard terminals | Defect; block release ([`12-trace-and-eval.md`](12-trace-and-eval.md), [`20-benchmark.md`](20-benchmark.md)) |

If a new failure mode needs a new hard gate, that is an ADR + kernel bump — not a prompt tweak ([`17-change-guide.md`](17-change-guide.md)).

---

## Cross-cutting plant view

| When L4 fails this way | What the floor should see |
| --- | --- |
| Hard gate / unknown / invented rupee | Withhold or abstain; no card; trace exists |
| Soft gate / attention | Ledger row; backlog item if soft; optional exploration card if opted in |
| Memory / topology / correlated models | Degraded or quiet; staff alerts from [`16-operations.md`](16-operations.md) rates |
| Silent promotion attempt | Blocked by lockfile/status checks; incident for on-call |

Humans decide and execute. L5 records closures. L4 does not “take over” to recover from its own failure.

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| These ten modes named; rates and ledger fields exist to detect them | Automated detectors per mode in ops dashboards; incident runbooks linked by mode id |
| Manual review of correlated-family and poisoning cases | Dedicated suites in CI ([`20-benchmark.md`](20-benchmark.md)) |

---

## Change class

Adding a **named mode** is documentation + monitoring (**data**). Changing the underlying hard rule is **kernel** + ADR ([`17-change-guide.md`](17-change-guide.md)).
