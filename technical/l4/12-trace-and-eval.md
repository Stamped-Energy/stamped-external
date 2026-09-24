# 12. Trace and evaluation

**Status:** Architecture.  
**ADRs:** [033](../../decisions/033-039/ADR-033-l4-decision-runtime.md) · [036](../../decisions/033-039/ADR-036-dual-family-models.md) · [038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md)  
**Siblings:** [`00-kernel.md`](00-kernel.md) · [`11-models-and-seams.md`](11-models-and-seams.md) · [`13-improvement.md`](13-improvement.md) · [`20-benchmark.md`](20-benchmark.md)

Every L4 run leaves a DecisionTrace. Replay, eval, and improvement all read the same ledger. If it is not in the trace, it did not happen for scoring.

---

## 1. Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Trace always | Every terminal (`emit`, `supersede`, `withhold`, `abstain`) and every portfolio **hold** writes a DecisionTrace |
| 2 | Slot model | XMPro-inspired slots: **observed → context → action → policy → approval → outcome**, plus process step labels |
| 3 | Ledger freeze | Evidence ledger and memory rows used in the run are frozen by hash; replay does not re-query L2 or Hindsight |
| 4 | pass^k | Reliability measured as pass^k on the **same** frozen ledger and lockfile |
| 5 | Process labels | Eval scores process steps, not only final outcome |
| 6 | Replay harness | Any two release lockfiles can be replayed against the same frozen episodes |
| 7 | Opportunity join | Soft-gate blocks join later persistence / exploration / backlog outcomes into the case library stream |

---

## 2. Why

Staff need one artifact for “why this card?”: what was observed, what context was frozen, what was proposed, which policy fired, whether a human approved anything, and what happened later.

Outcome-only scores lie. A verified close can still have taken a bad route. A withhold can be correct process. Process labels and pass^k on a frozen ledger catch both. Plant closures are sparse, delayed, and confounded — they alone cannot train seams safely.

---

## 3. DecisionTrace slots (XMPro-inspired)

Slots are the human-facing spine. Fields under each are the machine contract.

### `observed`

| Contents | Notes |
| --- | --- |
| Origin | Finding, certified pattern, or hypothesis |
| Finding / pattern refs | `detector_id` / `detector_version` when from L3 |
| Condition key | Shared key function with L3 |
| As-known-at PSM snapshot id | Bitemporal; late L2 corrections do not rewrite history |
| Coverage manifest | What the digest included / excluded / marked unknown |

### `context`

| Contents | Notes |
| --- | --- |
| Evidence ledger hash | Measured / advisory / model partitions never merged |
| Frozen memory rows | Hindsight and case-library rows as ledger entries |
| Frozen L3 method outputs | Calculator, condition test, simulator, verification-plan builder |
| Read manifest | Every typed zoom / builder read |
| Proof obligations | Required and met |

### `action`

| Contents | Notes |
| --- | --- |
| Candidates | All drafts from both families |
| Critiques | Cited objections only; one revision |
| Preferred candidate | After selection seam |
| Footprint | Assets, shared resources, crew/role, material, time window |
| Card payload (if emit/supersede) | Sections, owner role, alternatives including no-action |
| Opportunity ledger pointer | If blocked — full candidate kept under ADR-038 |

### `policy`

| Contents | Notes |
| --- | --- |
| Release lockfile hash | Registries, stage graph, kernel version, model pins |
| Seam decision records | Full set from [`11-models-and-seams.md`](11-models-and-seams.md) |
| Constraint results | `satisfied \| violated \| unknown` + conflicting fact set |
| Gate records | Gate id, class (`hard` \| `soft`), threshold, candidate value |
| Portfolio action | Dedupe, conflict, supersede, hold, budget |
| Kernel checkpoint results | After candidates; after constraints; before terminal |
| Step-label slot | Process taxonomy (filled offline or at close) |

### `approval`

| Contents | Notes |
| --- | --- |
| L5 accept / edit / reject / defer | When the card reached the floor |
| Owner backlog promote / dismiss | Soft-gate items only |
| Exploration flag | `exploration=true` when sent under opt-in budget |
| Improve / pin accepts | Links to packs that later changed related registries |

HITL stays explicit: model agreement is not owner acceptance.

### `outcome`

| Contents | Notes |
| --- | --- |
| Closure state | Verified / no-change / rejected / … from L5 |
| Learning fact | Short fact into plant bank; ineligible close → action-worked null |
| Persistence result | For blocked items — did the waste continue? |
| Later-card join | Same condition key later verified or dismissed |
| Exploration result | Unbiased sample of soft-gate rejects |

Case library is the **authority** for outcomes when memory banks disagree.

---

## 4. Process labels (not only outcome)

Offline council ([`13-improvement.md`](13-improvement.md)) labels **steps** against a fixed taxonomy:

| Label | Means |
| --- | --- |
| `bad_route` | Wrong workflow / pattern path |
| `missed_cross_asset` | Conflict visible in PSM, not acted on |
| `flooded_owner` | Attention / portfolio failure |
| `weak_grounding` | Uncited claims or failed condition test |
| `wrong_constraint_subset` | Selection seam missed a binding row |
| `stale_analogue` | Case use past asset/detector epoch |
| `over_strict_block` | Soft gate blocked something that persisted or later verified |
| `over_loose_release` | Card that should have been held |

Where Opus and Sol agree, the label is a candidate. Where they disagree, a human decides. Labels feed playbooks and gate calibration — they do not silently change pins.

---

## 5. Evidence ledger freeze

Before any model call that can produce claims:

1. Code builds the ledger from the PSM snapshot, allowlisted reads, and L3 tool returns.  
2. Partitions stay separate: **measured**, **advisory** (memory), **model** (candidates/claims).  
3. Hash the ledger; store payload in the L4 store.  
4. All claims must cite ledger row ids; uncited claims are dropped.  
5. Replay loads the frozen ledger — it does **not** re-hit L2 or Hindsight.

Out-of-envelope simulator rows are recorded; emit criteria fail honestly ([`15-l3-l4-interface.md`](15-l3-l4-interface.md)).

---

## 6. Replay harness and pass^k

### Exact replay

Inputs: DecisionTrace id (or episode id) + release lockfile hash.  
Restore snapshot, ledger, read results, and L3 frozen outputs; re-run the stage graph; compare terminals, selected candidate, gate ids, and seam finals.

### pass^k

For a fixed episode and lockfile, run the plant model path **k** times on the same frozen ledger.

| Metric | Definition |
| --- | --- |
| pass^k | Fraction of episodes where ≥1 of k runs matches expected terminal and critical seam finals |
| Strict pass^k | All k runs agree with each other and with expected |

A card whose terminal flips across reruns on a frozen ledger is a **defect**, not plant noise. Use the same k across lockfile comparisons. Benchmark harness: [`20-benchmark.md`](20-benchmark.md).

### Cross-lockfile replay

Any two lockfiles replay the same frozen episodes. Core changes are judged here, not by anecdote.

---

## 7. Eval suites and metrics

**Suites:** regression · verified closures · rejected / no-change · adversarial constraints · family / pattern holdouts · plant holdout when available · seeded scenarios (feeder overlaps, idle auxiliaries, shifting bottlenecks) · per-domain suites from the domain registry.

**Metrics (minimum):** terminal accuracy · grounding violations · owner-role accuracy · constraint-conflict miss rate · opportunity recall · false-discovery / nuisance-card rate · bottleneck identification stability · counterfactual calibration per L3 method · portfolio regret · coverage rate · abstain-on-unknown correctness · seam calibration · soft-gate miss rate / block precision (ADR-038).

---

## 8. Rejected alternatives

| Alternative | Why rejected |
| --- | --- |
| Outcome-only scoring | Hides bad process on lucky verifies |
| Re-querying live L2 on replay | Destroys as-known-at truth |
| Model self-reported confidence as pass rate | Not calibrated; not a gate |
| Separate “eval ledger” from production trace | Drift between what ran and what scored |
| pass@k on unfrozen live calls | Measures plant noise, not system reliability |

---

## 9. Evidence that would change this

- Slot model fails staff review → reshape slots; keep freeze and pass^k.  
- pass^k saturates while nuisance cards rise → tighten suites toward process labels and opportunity recall.  
- Plant holdout unavailable for Pilot 1 → seeded scenarios + family holdouts; do not fake a second plant.

---

## 10. v1 slice vs later

| v1 | Later |
| --- | --- |
| Full slot schema + freeze + basic replay | Automated pass^k in CI on every lockfile bump |
| Process taxonomy + council labeling | Higher label volume; verifier models on closed seams |
| Seeded discovery scenarios | Plant-holdout suite when multi-site |
| Soft-gate joins from ADR-038 | Full trade-off curves per gate in ops |

---

## What the trace is not

Not a chat log. Not a place for free-form model confidence. Not the operator home screen (L6 shows the card; staff tools may show traces).
