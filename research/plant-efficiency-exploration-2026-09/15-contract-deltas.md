# Contract deltas — coarse fields

**Date:** 2026-09-24
**Status:** Field names for a later schema bump in this submodule. Not JSON Schema yet.
**Authority:** [`09-stamped-founder-vision.md`](09-stamped-founder-vision.md). Shape: [`14-coarse-architecture.md`](14-coarse-architecture.md).

Prescription **1.0.0** is not edited in place. It rejects unknown fields and is energy-shaped. The card proposal is a new schema beside it. L5 reads both until 1.0.0 is retired.

## Finding — additive bump

Keep `status` and `delivery`. `delivery` is L4 only when `status` is emitted. Lab never promotes.

New fields:

- `condition_key` — asset, state window, shift
- `decision_family_id`
- `primary_domain` — from the family registry, not from a model
- `secondary_domains` — optional, each one of the five domain names
- `facts` — each fact has an evidence tier: Measured, Confirmed, Modeled, or Unknown
- `effects` — one entry per domain section that applies. Each entry has method, tier, and an optional calculator reference. No raw rupee from a model.
- `verification_plan` — signal references, post-action window, pass / fail / inconclusive predicate, and the tier that verification will yield
- `constraint_refs_considered`

Findings that share a `condition_key` merge before delivery.

## Card proposal — new schema, L4 output

Emitted only on terminal emit. Withhold and abstain still produce a trace and no customer card.

- `card_proposal_id`, `version`
- `finding_refs`, `condition_key`
- domain sections, copied from the finding. L4 cannot change the primary domain.
- one recommended action
- at most two alternatives, one of which is always no action. Each alternative carries its constraint-check result and calculator-priced effects where a price exists.
- uncertainty, from tier and freshness
- `proposed_owner_role` — one value from the configured set
- `autonomy_class` — a catalog id, or human-only
- `verification_plan` — copied from the finding, allowed only to narrow
- `compile_trace_id`

## Live card — L5

- `card_id`
- `card_proposal_id` and version
- `owner_person` — resolved from the role at assignment
- `state` — Open, Assigned, In progress, Closed-verified, Closed-no change, Rejected, Deferred / expired, or Blocked / disputed
- history of transitions
- the same domain sections
- `ran_as` — human, or the enabled autonomy class id

## Closure event — L5, append-only

The plant bank does not store this whole event. L4 retains a short learning fact drawn from it.

- `card_id`, disposition, reason code, actor, owner at close, timestamps
- verification result, tier, source signal, window
- constraint that fired, if any
- realized effects per section, each with a tier
- `learning_eligible` — false without a verification result or an explicit reason

An ineligible event may become a learning fact that evidence was missing. It must not become an observation that the action worked.

## Autonomy policy — L5

- default: no class enabled
- catalog starts with `suppress_duplicate_notification` and `open_review_task`
- a plant proposal stays `pending` until Stamped sets `certified`
- enablement is a named owner, a plant, a class id, watch, and rollback
- hard-stop classes are absent: safety command, quality release, maintenance authorization, master-data or dispatch write, customer-commitment change, critical-equipment command

## Owner roles — configured

- `production_task` → production head
- `operational_task` → ops head
- L4 selects the role. L5 selects the person who holds it on the shift.
- Idle-load is configured as `operational_task`.

## Decision seams

Each seam has a closed answer set, a confidence, and a generative fallback when confidence is low. A decision model is not the source of the card's explanation. This pass does not call Jev. The seams are listed in [`14-coarse-architecture.md`](14-coarse-architecture.md).

## Hindsight

- One plant bank per plant. Short learning facts and world facts only. No card body. No transcript.
- One dialogue bank per conversation. Stable document id. Threads do not consolidate into plant observations.
- Directives on the plant bank cannot be overridden by reflect.
- Promotion from chat into the plant bank is an explicit fact, not automatic consolidation.
- Hosting is an L4-repo choice.

## What does not change in this evolution's first cut

- `StampedRecordEnvelope`
- dual-lane semantics
- lab never promotes
- emit, withhold, abstain, and a trace on every run
- no model-owned rupee
- only L2 opens the database
- fail-closed clearance
- ops-confirmed is not bill-verified
- the customer view hides withholds
- no equipment write anywhere
- this submodule remains the contract source of truth
