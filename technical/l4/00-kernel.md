# L4 kernel (normative)

**Version:** `l4-kernel.v1`  
**Status:** Frozen surface — changes only through an ADR, a kernel version bump, and a full replay.  
**Authority:** This file. Sibling docs link here; they must not restate these rules in softer language.  
**ADRs:** [033](../../decisions/033-039/ADR-033-l4-decision-runtime.md) · [038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md) · [039](../../decisions/033-039/ADR-039-registries-and-stage-graph.md)

“Frozen” means replay has a fixed yardstick and the plant has a stable promise. It does not mean the kernel never changes. It is kept small and parameterised by registries, so most expansions never touch it.

---

## 1. Terminals

Every DecisionCase ends in exactly one terminal, always with a DecisionTrace:

| Terminal | Meaning |
| --- | --- |
| `emit` | Send one card proposal to L5 |
| `supersede` | Replace a prior L4 proposal for the same condition key **before** owner acceptance |
| `withhold` | Do not send; reason recorded (constraint, disagreement, proof floor, etc.) |
| `abstain` | Insufficient case to decide; reason recorded |

**Portfolio hold** is not a terminal. It is L4-internal: the proposal stays in the L4 store, visible to staff, and is **not** sent to L5.

---

## 2. One-card rule

- One card per **condition key**.
- One recommended action; at most two alternatives; one alternative is always **no action**.
- One owner role from the configured role set.
- Primary domain is a **domain registry id**, taken from the family registry (Findings) or the pattern registry (discoveries).
- The kernel refers to registries by id. It never lists domains by name.

---

## 3. Write ban

No L4 tool writes equipment, schedules, dispatch, quality holds, maintenance authorization, master data, or customer commitments. Reads only. Side effects belong to L5 policy (default off) after a human accepts.

---

## 4. Money

Rupees only from **L3 calculator references**. An unreferenced **rupee** (or any money field without a calculator citation) → drop the claim; if the candidate still depends on that unreferenced rupee → `withhold`. Models never invent or assign a rupee. Non-money quantities without citations are dropped as uncited claims ([§13](#13-evidence)); they do not by themselves force withhold unless a family proof obligation requires them. Section wallets are never summed into one hero number.

---

## 5. Constraint evaluator

Code evaluates typed constraints. Result:

| Result | Kernel action |
| --- | --- |
| `violated` | `withhold` |
| `unknown` on a **hard** constraint | `withhold` (`reason=constraint_unknown`) |
| LLM “possible conflict” without a code result | `withhold` (`gate_id=llm_possible_conflict`, **hard**) |

None of these can be overridden by modeled benefit. Code always evaluates **every hard constraint row whose footprint intersects the candidate**. Models may only **add** advisory rows to evaluate; they may never omit a matching hard row.

---

## 6. Verification plan

A verification plan may only **narrow** its source plan (Finding plan or L3-built discovery plan): same boundary, equal or tighter bounds. It may not invent new signals or widen scope.

---

## 7. Supersede

Supersede only **before** owner acceptance. After acceptance → a separate card or a conflict note — never silent replace. Wire fields: [`18-contract-deltas.md`](18-contract-deltas.md).

---

## 8. Simulator output

L3 simulator output is evidence tier **Modeled**, cites method and version, and must sit inside that method’s validated envelope to support `emit`. Out-of-envelope → `withhold` (`gate_id=simulator_out_of_envelope`, **hard**).

---

## 9. Hard stops

Hard stops from ADR-030 / vision `09` always apply: no automatic safety / critical remote command; no quality hold release; no maintenance authorization; no silent master-data or full dispatch change; no constraint override for a model benefit alone.

---

## 10. No self-promotion

Nothing in procedural memory, prompts, registries, thresholds, or model pins promotes itself. Changes go through release lockfile, replay, and a named owner where required. A **global** pin applies at a plant only after that plant’s named owner accepts it (or has opted in to automatic acceptance of global pins).

---

## 11. Gates: hard vs soft

Every gate is typed `hard` or `soft`. Every block records the **gate id** (canonical table below). Detail and exploration eligibility: [`22-missed-opportunities.md`](22-missed-opportunities.md).

### Hard gates (never tunable, never in backlog, never explored)

| `gate_id` | Trigger |
| --- | --- |
| `hard_stop` | ADR-030 sacred constraints |
| `constraint_violated` | Code evaluator `violated` |
| `constraint_unknown_hard` | `unknown` on hard / conditional-hard neighbourhood |
| `llm_possible_conflict` | Model flags conflict without code result |
| `unreferenced_rupee` | Money without calculator citation after claim drop |
| `write_tool` | Write / OT side-effect tool attempted |
| `proof_floor` | Missing asset bind, verification path, or L3 condition test (discoveries) |
| `simulator_out_of_envelope` | Modeled support outside validated use |
| `action_seam_disagreement` | Dual-family disagreement on action / owner / constraint-affecting / verification / terminal seams |
| `uncertified_detector` | Uncertified detector version (shadow / withhold — never emit) |
| `supersede_after_accept` | Attempt to supersede after owner acceptance |
| `staleness_hard_limit` | Freshness past the hard staleness limit |

**Action-seam disagreement is hard**, not soft. Two families either picked the same closed option or they did not — there is no tunable “agreement floor” for action-affecting seams.

### Soft gates (thresholds in registry; tuned by evidence; exploration-eligible only when listed in [`22`](22-missed-opportunities.md))

| `gate_id` | Trigger |
| --- | --- |
| `routing_agreement` | Disagreement on **routing-class** seams only (workflow, optional analysis, …) — uses registry default; soft for calibration of whether default was right |
| `one_family_confidence` | One-family mode numeric floors |
| `evidence_tier_min` | Soft minimum tier for emit path |
| `freshness_margin` | Soft freshness (hard limit is `staleness_hard_limit`) |
| `attention_budget` | Over per-role shift budget → hold |
| `reproposal_cooldown` | Negative memory cooldown |
| `hypothesis_volume_cap` | Grounded-hypothesis lane volume |
| `pattern_precision` | Pattern demotion to shadow |

---

## 12. Stage-graph checkpoints

Every stage graph (see [`21-registries-and-stage-graph.md`](21-registries-and-stage-graph.md)) must still pass:

1. Constraint evaluator before portfolio
2. Portfolio before terminal
3. Card minimizer (one primary domain, wallets not summed, verification narrowed) **before** kernel re-check
4. Kernel re-check on the chosen set before terminal

Default order: **candidates → constraint evaluator → portfolio → card minimizer → kernel re-check → terminal**.

### Kernel re-check (normative list)

On the chosen set, code re-verifies: money references; write ban; constraint results for intersecting hard rows; proof floor; one-card / one-owner shape; verification narrow-only; action-seam disagreement not present; simulator envelope if Modeled supports emit. Failure → `withhold` / `abstain` with reason — never quiet emit.

---

## 13. Evidence

- Every claim cites a ledger row id. Uncited claims are dropped by code (`gate_id` recorded when drop invalidates the candidate).
- Evidence tiers are assigned by **code** from source type (Measured / Confirmed / Modeled / Unknown). Models never assign a tier.
- Partitions (measured, advisory, model) are never merged.

---

## 14. Primary domain

Primary domain is a **domain registry id**:

- Findings → from the family registry
- Certified patterns → from the pattern registry
- Grounded hypotheses → from the hypothesis type’s registry entry (required field before the lane may emit)

The kernel never lists domain names.

---

## Change control

| Change | Path |
| --- | --- |
| Soft-gate threshold | Registry + replay + owner acceptance |
| New domain / stage / pattern | Registry + replay ([`17-change-guide.md`](17-change-guide.md)) |
| Any rule in this file | ADR + `l4-kernel` version bump + full replay |

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| This kernel version (`l4-kernel.v1`) as the yardstick | New version only via ADR + full replay |
| Hard vs soft gate split as listed | Soft list may grow via registry; hard list only via ADR |
| Dual-family disagreement → withhold on action-affecting seams | Same unless an ADR changes disagreement policy |
