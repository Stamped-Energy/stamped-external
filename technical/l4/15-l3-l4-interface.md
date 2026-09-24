# 15. L3-L4 interface

**Status:** Architecture. Contract deltas: [`18-contract-deltas.md`](18-contract-deltas.md).  
**ADRs:** [033](../../decisions/033-039/ADR-033-l4-decision-runtime.md) · [035](../../decisions/033-039/ADR-035-l4-discovery.md) · [039](../../decisions/033-039/ADR-039-registries-and-stage-graph.md)  
**Siblings:** [`00-kernel.md`](00-kernel.md) · [`07-finding-runtime.md`](07-finding-runtime.md) · [`08-discovery.md`](08-discovery.md) · [`11-models-and-seams.md`](11-models-and-seams.md)

L3 owns **methods** (detect, price, test, simulate, build verification plans). L4 **consumes** them as typed tools. L4 does not re-implement money, envelopes, or detector science.

---

## 1. Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Finding floor | Intake enforces the evidence / bind / verification floor before any seam |
| 2 | Detector identity | Every Finding carries `detector_id` + `detector_version`; traces and memory re-key on version change |
| 3 | Uncertified | Uncertified detectors / patterns stay **shadow** — traced, not emitted — until certified |
| 4 | Calculator | Rupees and priced effects only via L3 calculator **references**; unreferenced quantities → withhold |
| 5 | Condition test | Discovery / hypothesis emit requires L3 condition test **pass** |
| 6 | Verification-plan builder | L3 builds plans from signals already in L2; L4 may only **narrow** (same boundary, equal or tighter bounds) |
| 7 | Simulators | L3 simulators return Modeled effects inside a **credibility envelope**; out-of-envelope → cannot support emit |
| 8 | Shared registries | Domains, families, patterns, constraint kinds, evidence-tier rules live in one pack; both layers consume |
| 9 | Pattern ↔ detector | When L3 ships a detector for a condition, the L4 pattern **retires** — no double detect |
| 10 | Ownership | L3 owns method code and calibration epochs; L4 owns decision runtime, portfolio, and card proposal |

---

## 2. Why

If L4 invents a parallel calculator, the card and the Finding disagree on money. If L4 skips the condition test, discovery becomes storytelling. If envelopes are ignored, Modeled numbers read like Measured.

Split the work the way the plant already thinks: detection science and pricing methods in one place; “what should we do with this on this shift?” in another. Humans still accept the card.

---

## 3. Finding intake (L3 → L4)

### Floor (must hold before DecisionCase)

| Required | Fail behavior |
| --- | --- |
| Schema-valid Finding | Reject intake; no run |
| Asset / condition binding | Withhold / abstain per kernel |
| Evidence references | Ledger rows required |
| Verification path present (or explicit absence per family rules) | Withhold |
| Evidence tier assigned by code rules | Invalid tier → withhold |
| `detector_id` + `detector_version` | Reject intake if missing |
| Detector certified for plant | Else **shadow** only |
| Calculator references for priced effects | Unreferenced ₹ → withhold |
| Condition key via **shared** key function | Same function L3 used for merge |

Shadow means full trace and opportunity-ledger entry where applicable; nothing sent to L5 as a customer card.

### What L4 may change on the Finding’s plan

Verification plan on the card proposal may only **narrow** the Finding’s plan (or the L3-built discovery plan): same measurement boundary, equal or tighter bounds, subset of allowed methods from the builder’s offer. Widening is a hard fail.

---

## 4. L3 methods port (tools L4 calls)

All calls go through `L3MethodsPort`. Outputs are frozen into the evidence ledger ([`12-trace-and-eval.md`](12-trace-and-eval.md)). L4 cites method id + version; it does not re-implement these methods.

### Calculator

| Rule | Detail |
| --- | --- |
| Input | Typed effect quantities + tariff / tagged fallback refs |
| Output | Priced sections with method id, version, tier |
| L4 duty | Cite calculator reference ids on any ₹ claim |
| Fail | Missing reference → withhold (`unreferenced_rupee`) |

Sections are never summed into one hero ₹ across domains.

### Condition test (discovery / hypothesis)

| Rule | Detail |
| --- | --- |
| Input | Candidate mechanism + signal bindings from PSM / L2 |
| Output | `pass \| fail` + cited signal ids + method version |
| Emit gate | Hypothesis lane and pattern grounding require **pass** |
| Fail | Shadow / ledger only — not a customer card |

### Verification-plan builder

| Rule | Detail |
| --- | --- |
| Input | Condition key, footprint, domain registry entry, available L2 signals |
| Output | Plan: signals, windows, success/fail criteria, method options |
| Constraint | Only signals already available (or commissioned) in L2 |
| L4 seam | May choose among offered methods / tighten bounds — never invent a signal |

### Simulators (credibility envelope)

Every simulator result carries an envelope. Emit may use the result only if **inside** envelope.

| Envelope field | Meaning |
| --- | --- |
| Intended use | What decision class this method supports |
| Calibration epoch | When the method was last validated |
| Validation summary | Pass/fail of last validation suite (ref) |
| Uncertainty | Reported uncertainty / ranges |
| Out-of-domain behavior | Explicit: refuse, degrade, or widen uncertainty |

| Result | L4 behavior |
| --- | --- |
| In envelope | May cite as **Modeled** with method+version |
| Out of envelope | Record in ledger; **cannot** support emit on that claim |
| Method down | Degraded mode — evidence-only path or withhold; no invented counterfactual |

Also consumed when certified: system methods (bottleneck, blocked/starved, utility balance) and baselines for PSM history views.

L4’s `l3_method_choice` and `simulate_vs_evidence` seams select among registered methods; they do not author physics ([`11-models-and-seams.md`](11-models-and-seams.md)).

---

## 5. Discovery hand-off

```text
L4 scanners / hypotheses
        │
        ▼
L3 condition test ──fail──► shadow + opportunity ledger
        │ pass
        ▼
L3 calculator (per section)
        │
        ▼
L3 verification-plan builder
        │
        ▼
L4 DecisionCase → same kernel as Findings
```

Certified patterns name their L3 method dependencies in the registry. Grounded-hypothesis lane also requires dual-family action agreement and plant owner opt-in ([`08-discovery.md`](08-discovery.md)).

---

## 6. Shared registry pack

Both layers read versioned entries under `stamped-external/registries/` (ADR-039):

| Registry | L3 uses for | L4 uses for |
| --- | --- | --- |
| Domains | Claim kinds, pricing units, detectors | Sections, analyses, seam options |
| Families | Finding family → domain | Workflow route, owner roles |
| Patterns | Hand-off targets | Discovery emit recipes |
| Constraint kinds | — | Evaluator predicates |
| Evidence-tier rules | Finding floor | Ledger tier assignment |
| Condition-key recipe | Merge | Dedupe / portfolio |

A new domain is declared once. L3 adds methods/detectors; L4 adds an analysis plug-in. Kernel and seams iterate by id — they do not hard-code the five names.

Lockfile skew between L3 and L4 releases is a failure mode: intake should refuse or shadow when required method versions are missing.

---

## 7. Pattern → detector retirement

When L3 certifies a detector that covers an L4 discovery pattern’s condition key recipe:

1. Registry marks pattern `retiring` with deprecation window.  
2. New emits prefer the Finding path.  
3. After window, pattern `retired`; scanners may still feed Lab, not customer cards.  
4. Trace links `pattern_ref` → `detector_id` for learning continuity.

Two active detectors for one condition is a bug, not a feature ([`08-discovery.md`](08-discovery.md)).

---

## 8. What L4 must not ask L3 to do

- Override a hard constraint for modeled benefit  
- Publish topology (site pack / L1 path)  
- Accept chat as a detector  
- Sum section wallets  
- Silently promote detector weights from L4 closures  

---

## 9. Ownership summary

| Concern | Owner |
| --- | --- |
| Detector code, Lab vs certified lane | L3 |
| Calculator, condition test, simulators, verification-plan builder | L3 |
| Method calibration epochs and envelopes | L3 |
| Finding merge on condition key | L3 |
| PSM, portfolio, seams, terminals, card proposal | L4 |
| Constraint evaluation at decide time | L4 (rows from L2; kinds from shared registry) |
| Live card, person, verify, close | L5 |
| Learning facts and outcomes | L5 → L4 memory ([`06-memory.md`](06-memory.md)) |
| Named-owner accept of pins / topology / lane opt-in | Human |

Offline improvement may **propose** detector or pattern ideas for L3/L4 owners — it does not silently promote them ([`13-improvement.md`](13-improvement.md)).

---

## 10. Rejected alternatives

| Alternative | Why rejected |
| --- | --- |
| L4 re-implements pricing in prompts | Invented ₹; drifts from Finding |
| Emit discovery without condition test | Ungrounded cards |
| Widening Finding verification plans in L4 | Lowers the bar after detect |
| Ignoring simulator envelopes | Modeled treated as Measured |
| Separate domain enums per layer | Dual maintenance; sixth domain breaks one side |
| Keeping L4 pattern after L3 detector ships | Double cards for one condition |

---

## 11. Evidence that would change this

- Envelope schema too coarse for Pilot 1 methods → extend fields; do not drop envelope checks.  
- Condition tests too slow for shift sweep → cache typed results with as-known-at; do not skip the test.  
- Registry skew incidents in staging → tighten release coupling or add explicit compatibility windows in the lockfile.

---

## 12. v1 slice vs later

| v1 | Later |
| --- | --- |
| Finding floor + detector id/version + shadow uncertified | Richer Lab metrics into shadow review |
| Calculator + condition test + verification-plan builder + ≥1 enveloped simulator per seed domain that needs it | Broader method catalog; same port |
| Shared registry pack consumed by both | Sixth domain as registry+plugin only |
| Pattern retirement rule documented | Automated retirement workflow in ops |
