# 22 — Missed opportunities and gate calibration

**Status:** Architecture contract (docs)  
**Date:** 2026-09-25  
**Authority:** [ADR-038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md)  
**Normative:** [`00-kernel.md`](00-kernel.md)  
**Related:** [`13-improvement.md`](13-improvement.md) · [`12-trace-and-eval.md`](12-trace-and-eval.md) · [`16-operations.md`](16-operations.md) · [`17-change-guide.md`](17-change-guide.md) · [`19-failure-modes.md`](19-failure-modes.md) · [`20-benchmark.md`](20-benchmark.md)

Strict gates protect the floor. The same strictness can hide real waste. Every blocked candidate is kept; soft-gate blocks can reach the owner; a small exploration budget measures what the gates reject; soft thresholds then move on evidence in both directions. Hard gates never enter that loop.

Humans still promote, dismiss, accept, and execute. L4 does not silently turn a block into an emit.

---

## Purpose

Specify the opportunity ledger, owner backlog, exploration cards, calibration, and how this feeds the offline improvement loop — without weakening hard stops.

---

## Decisions

| # | Decision | Reason |
| --- | --- | --- |
| 1 | Every gate is `hard` or `soft`; every block records gate id | Audit and calibration need a name, not a vibe |
| 2 | Hard gates never backlog, never explore, never tune | Sacred floor ([`00-kernel.md`](00-kernel.md)) |
| 3 | Soft-gate blocks → ledger + owner backlog; optional exploration | Owner keeps final say; exploration removes selection bias |
| 4 | Calibration loosens **and** tightens from ledger + exploration | Learning only from sent cards drifts cautious ([`19-failure-modes.md`](19-failure-modes.md) §8) |
| 5 | Promotion re-runs hard gates | Backlog cannot bypass the kernel |

**Rejected:** loosening hard stops to catch more opportunities; silent promotion; ranking patterns by closure rate alone; council labels as automatic truth.

**Would change this:** a new soft-gate kind with a registered threshold location; evidence that exploration caps are too high for a plant’s attention budget.

---

## Hard vs soft

Canonical `gate_id` table: [`00-kernel.md`](00-kernel.md) §11. Summary:

| Class | Examples | Tunable? | Backlog? | Explore? |
| --- | --- | --- | --- | --- |
| **Hard** | Hard stops; constraint violated/unknown-hard; LLM possible conflict; unreferenced rupee; write tool; proof floor; simulator envelope; **action-seam disagreement**; uncertified detector; supersede-after-accept; staleness hard limit | No | No (audit ledger only) | **No** |
| **Soft** | `routing_agreement`; `one_family_confidence`; `evidence_tier_min`; `freshness_margin`; `attention_budget`; `reproposal_cooldown`; `hypothesis_volume_cap`; `pattern_precision` | Yes — registry | Yes | Only if **exploration-eligible** below |

Wrong-looking **hard** blocks (e.g. stale constraint row) are raised as **data**. They never loosen a hard gate.

---

## Opportunity ledger schema

Stored in the L4 operational store (derived data only). One row per candidate that did not become a normal card (includes Finding withholds, discovery drops, hypothesis shadow, portfolio holds, cooldown suppressions).

| Field | Meaning |
| --- | --- |
| `ledger_entry_id` | Stable id |
| `decision_case_id` / case snapshot | DecisionCase reference |
| `candidate_snapshot` | Full candidate set (or winning candidate) at block time: claims, citations, footprint, L3-priced effects per section (Modeled), seam records |
| `ledger_hash` / PSM snapshot id | As-known-at provenance |
| `lockfile_hash` | Release pin at block time |
| `gate_id` | Named gate that blocked |
| `gate_class` | `hard` \| `soft` |
| `gate_threshold` | Threshold then in force (soft only; null for hard) |
| `gate_value` | Candidate’s measured value against the gate |
| `block_terminal` | `withhold` \| `abstain` \| hold \| shadow-drop (as applicable) |
| `origin` | Finding / pattern / hypothesis / portfolio |
| `later_outcome` | Join slot — see below |
| `created_at` | Recorded time |

**Later outcome** (filled as evidence arrives):

| Outcome kind | How |
| --- | --- |
| `persistence` | After the verification window, code runs the verification plan on what happened; L3 prices foregone effect on actual data (Modeled, per section). Vanished condition → block likely correct |
| `later_card` | Same condition key later emitted; closure (verified / rejected / no-change) joined back |
| `owner_promoted` | Backlog promote → card → closure |
| `owner_dismissed` | Dismiss reason; may seed a proposed constraint |
| `explored` | Exploration card closure with `exploration=true` on the learning fact |
| `none_yet` | Still open |

Hard-gate rows keep outcomes for audit and constraint-data debugging. They do not enter backlog selection or exploration sampling.

---

## Owner backlog

Soft-gate ledger rows surface to the **named plant owner** as an unassigned backlog:

- labelled lower confidence;
- gate that held the item in plain words;
- candidate summary and priced sections (calculator refs only);
- actions: **promote**, **dismiss** (with reason), or leave.

**Promote:** re-run every hard gate and the normal decision path; on pass, create a normal card (not an exploration card unless separately sampled). Cannot bypass hard stops.

**Dismiss:** label for improvement; may become a proposed constraint row for the constraint owner.

Hard-gate items stay hidden from this backlog (amends “UI hides all withholds”: hard stay hidden; soft may show as backlog — ADR-038).

---

## Exploration cards

| Rule | Detail |
| --- | --- |
| Opt-in | Per plant, named owner |
| Cap | Small weekly budget (registry); attention-aware |
| **Exploration-eligible soft gates only** | `evidence_tier_min`, `freshness_margin`, `pattern_precision`, `one_family_confidence` (when in one-family mode). **Not eligible:** `attention_budget` (hold stays hold), `reproposal_cooldown`, `hypothesis_volume_cap`, `routing_agreement`, **any hard gate** including `action_seam_disagreement` |
| Selection | Random within eligible set (unbiased sample) |
| Origin | Preserved (`l3_finding` / `l4_pattern` / `l4_hypothesis`); `exploration=true` is a flag only |
| Before send | Re-run **every hard gate** + card minimizer + kernel re-check; fail → do not send |
| Label | Lower confidence; learning fact carries `exploration=true` |
| Closure | Same L5 verify / reject / no-change path |

Exploration is the only source that shows what eligible soft gates would have missed without selection bias. Ops watches exploration reject/no-change ([`16-operations.md`](16-operations.md)); a nuisance spike pauses the budget — it does not loosen hard gates.

Exploration is the only source that shows what soft gates would have missed without selection bias. Ops watches exploration reject/no-change ([`16-operations.md`](16-operations.md)); a nuisance spike pauses the budget — it does not loosen hard gates.

---

## Per-gate scorecard

| Metric | Definition |
| --- | --- |
| Block precision | Share of blocked items truly not worth sending (vanished, dismissed, rejected when explored) |
| Miss rate | Share that would have helped (persisted with priced waste, later verified, promoted+verified, explored+verified) |
| Foregone effect | L3-priced, Modeled, per domain section — **never summed** across sections |
| Nuisance cost of loosening | Reject + no-change among explored; owner attention used |
| Trade-off curve | Replay ledger at alternate thresholds: what X catches vs lets through |

Triggers for a calibration proposal: miss rate or foregone effect crosses a registered bar, or block precision drops below a registered floor — or released cards keep getting rejected (tighten).

---

## Calibration (both directions)

1. **Trigger** from scorecard bars or improvement taxonomy labels (`over-strict block`, `over-loose release`) ([`13-improvement.md`](13-improvement.md)).
2. **Council** (Opus 5.5 + Sol, offline) proposes a threshold change per gate (and per domain/plant when evidence splits). The other model red-teams nuisance cost and hard-gate adjacency. Disagreement → human.
3. **Replay** on ledger + holdouts; owner pack shows both curves ([`20-benchmark.md`](20-benchmark.md)).
4. **Accept** — tech lead (global) or plant owner (plant override).
5. **Shadow → canary → pin** ([`16-operations.md`](16-operations.md)).

Direction is symmetric: loosen on measured misses; tighten on measured nuisance. Starting stance at a new plant: moderate thresholds, measured from week 1.

**Hard gates are outside this loop.**

---

## Feed into `13-improvement`

| Stream | What the loop learns |
| --- | --- |
| Sent cards + closures | Over-loose release, bad route, weak grounding, flooded owner |
| Opportunity ledger | Over-strict soft blocks; persistence and later-card joins |
| Backlog promote/dismiss | Owner priors; proposed constraints |
| Exploration (`exploration=true`) | Unbiased soft-gate error |

Without the second stream, self-improvement drifts toward caution: gates hide their own mistakes. Taxonomy labels for over-strict / over-loose become registry proposals (thresholds, prompts, patterns) — still replay-gated. Generator weight training stays off until clean step labels exist ([`13-improvement.md`](13-improvement.md)).

Council judgement on a sample of blocked items **prioritises human review**; it is not an automatic label and never auto-emits.

---

## Worked sketches (illustrative)

**Loosen:** Soft gate `evidence_tier_min` blocks idle-auxiliary candidates that later show persistence with Modeled foregone kWh (calculator path). Exploration verify rate on that **eligible** gate is healthy; nuisance low. Owner pack shows the curve; plant owner accepts a lower tier floor for that family; shadow → canary → pin. (Action-seam disagreement is hard — never loosened this way.)

**Tighten:** Soft gate `attention_budget` holds were too rare because exception exemption was over-wide; accept rate fine but reject/no-change up on non-exception cards. Domain exemption registry tightened; replay shows lower nuisance; each plant owner accepts the pin.

Numbers in live packs are site-measured or labelled illustrative.

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Ledger schema, backlog, opt-in exploration, manual scorecards | Automated trade-off curves in CI; paging on miss-rate bars |
| Moderate soft thresholds at Pilot plants | Per-plant overrides with clear precedence in the lockfile |

---

## Change class

Ledger fields, backlog UX, exploration caps, and soft thresholds are **data** (registry + L4 store). Changing hard-gate membership or allowing exploration of hard blocks is **kernel** + ADR ([`17-change-guide.md`](17-change-guide.md)) — and is rejected unless a future ADR explicitly overturns ADR-038.
