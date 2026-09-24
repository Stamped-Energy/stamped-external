# 20 — Benchmark

**Status:** Architecture contract (docs)  
**Date:** 2026-09-25  
**Normative:** [`00-kernel.md`](00-kernel.md)  
**Related:** [ADR-033](../../decisions/033-039/ADR-033-l4-decision-runtime.md) · [ADR-036](../../decisions/033-039/ADR-036-dual-family-models.md) · [ADR-038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md) · [`12-trace-and-eval.md`](12-trace-and-eval.md) · [`13-improvement.md`](13-improvement.md) · [`22-missed-opportunities.md`](22-missed-opportunities.md)

L4 works when held-out DecisionCases, gates, and human closures say so — not when a vendor claims a model is “best for manufacturing.” Numbers that are not measured on a named suite or plant are illustrative or omitted.

---

## Purpose

Define how we know the decision runtime is fit for a pin: what is frozen, what is scored, and what never counts as proof.

---

## Decisions

| # | Decision | Reason |
| --- | --- | --- |
| 1 | Primary proof is **held-out DecisionCases** + replay under a lockfile | Same inputs must yield stable terminals under the kernel |
| 2 | Report **pass^k**, not a single lucky run | Agent systems flatter single-shot accuracy |
| 3 | Patterns need **precision and recall**; soft gates need **calibration curves**; exploration needs **lift** | Selection bias otherwise ([`19-failure-modes.md`](19-failure-modes.md)) |
| 4 | Human **accept / reject / no-change** rates are first-class | HITL is the product loop; model self-scores are not |
| 5 | Vendor leaderboards and brochure % are out of scope | They do not cite our lockfile, ledger, or plant |

**Rejected:** judging L4 by detector AUC alone; ranking by closure rate without the opportunity ledger; shipping on council vibe without replay.

**Would change this:** a new suite type required by a sixth domain; measured need for plant-holdout before any global pin (already preferred when available).

---

## What is frozen in a benchmark episode

For each DecisionCase / episode:

- release lockfile hash (or pair of hashes for A/B replay);
- as-known-at PSM snapshot id + ledger hash;
- origin (Finding, pattern, hypothesis);
- expected opportunities (for discovery/seeded scenarios);
- forbidden cards (must not emit);
- hard-gate expectations (must withhold/abstain);
- optional human gold terminal and owner role.

Replay is exact from the frozen snapshot and ledger ([`12-trace-and-eval.md`](12-trace-and-eval.md)).

---

## Metrics

### Held-out DecisionCases

| Metric | Definition |
| --- | --- |
| Terminal accuracy | Share of cases where terminal ∈ {emit, supersede, withhold, abstain} matches gold / rubric |
| Grounding violations | Uncited claims or invented rupee refs (target: zero on pin) |
| Owner-role accuracy | Proposed role matches gold when emit/supersede |
| Constraint-conflict miss rate | Failed to withhold on violated/unknown-hard |
| Coverage | Share of cases that reach a terminal without infra abort |

Suites: regression, verified closures, rejected/no-change, adversarial constraints, family/pattern holdouts, plant holdout when available, seeded discovery scenarios, per-domain suites from the domain registry.

### pass^k

Rerun the same frozen case k times under the same lockfile (fresh model samples where the seam is stochastic). **pass^k** = fraction of cases that pass the rubric on at least one of k runs, reported alongside **pass@1** and agreement of terminals across reruns. Pins require declared k (illustrative default for design: k=3; ops locks the number per suite).

Stochastic seams may vary candidate text; kernel terminals and hard-gate behaviour must not flip on citation-complete equivalent ledgers without a traced soft-gate boundary.

### Pattern precision / recall

| Metric | Definition |
| --- | --- |
| Precision | Among pattern-origin emits (and certified matches), share that later verify or are accepted without nuisance reject/no-change |
| Recall | Among seeded/holdout opportunities the pattern should catch, share matched |
| Shadow precision | Same on shadow traces before certification |

Auto-demotion to shadow on poor precision ([ADR-035](../../decisions/033-039/ADR-035-l4-discovery.md)). Closure rate alone is not precision ([ADR-038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md)).

### Soft-gate calibration curves

Per soft-gate id, from the opportunity ledger ([`22-missed-opportunities.md`](22-missed-opportunities.md)):

- block precision vs threshold;
- miss rate / foregone effect (L3-priced, Modeled, **per section — never summed**) vs threshold;
- nuisance cost of loosening (reject/no-change among explored).

Curves come from replaying the ledger at alternate thresholds. Pins move thresholds only with an owner pack showing both directions.

### Exploration lift

On plants with exploration opt-in:

| Metric | Definition |
| --- | --- |
| Exploration verify rate | Share of `exploration=true` cards that close verified |
| Lift vs holdout policy | Verify/accept rate of explored soft-gate items vs rate implied by keeping them blocked (persistence / later confirmation) |
| Nuisance | Reject + no-change among exploration cards; attention consumed |

Exploration is the unbiased sample of soft-gate rejects. No exploration sample → do not claim soft gates are well-calibrated.

### Time-to-card

| Tier | Bar (design target; Pilot locks measured values) |
| --- | --- |
| Exception response | Minutes |
| Flow / time | About 15 minutes |
| Energy / cost | May take longer |

Measure intake → terminal (emit/supersede) or definitive withhold/abstain. Exclude human accept latency (that is L5/owner). Degraded modes report separately.

### Human accept / reject / no-change

| Rate | Use |
| --- | --- |
| Accept | Pin health; not a license to loosen hard gates |
| Reject | Over-loose soft gates or bad grounding; feeds tightening |
| No-change | Condition vanished or action unnecessary; feeds both pattern precision and gate scorecards |

Ineligible closes do not count as proof ([ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md)). Proof counts need independent eligible closures across shifts and dates where the suite says so.

---

## Acceptance posture for a pin

A candidate lockfile may pin when, on the required suites:

1. Hard-gate and grounding bars pass (no invented rupees; unknown-on-hard withheld).
2. pass^k and terminal accuracy meet the suite thresholds registered for that change class.
3. Pattern changes show precision/recall within registered floors (or stay shadow).
4. Soft-gate changes show calibration curves and exploration/persistence evidence in both directions when thresholds move.
5. Owner pack accepted (plant or tech lead per scope).

Shadow and canary still follow [`16-operations.md`](16-operations.md).

---

## What does not count

- Provider marketing scores, arena Elo, or “industrial LLM” blog numbers.
- In-sample replay the proposers tuned against.
- Council labels without human break-glass on disagreement ([`13-improvement.md`](13-improvement.md)).
- Summed multi-domain ₹ “impact.”
- Closure rate without ledger miss rate.

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Suites and metrics specified; Pilot fills numeric thresholds from traffic | CI gates on pass^k and grounding; plant-holdout required for global pins |
| Seeded scenarios for discovery recall | Broader plant-holdout library |

Illustrative thresholds in early dashboards stay labelled **illustrative** until a suite version locks them.

---

## Change class

Suite definitions and thresholds are **data** (registry). Changing what a hard gate means to “pass” a benchmark is **kernel** + ADR ([`17-change-guide.md`](17-change-guide.md)).
