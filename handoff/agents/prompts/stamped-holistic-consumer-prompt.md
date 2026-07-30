# Prompt — Holistic plant effectiveness (ADR-024 / ADR-025)

> **Use this:** One copy-paste block for **any** Stamped consumer-repo agent (L1–L6).  
> **Also paste into:** company onboarding / internal eng channel when spinning agents on this work.  
> **Platform:** [Vinayak-RZ/stamped-external](https://github.com/Vinayak-RZ/stamped-external)  
> **Authority:** [ADR-026](../../../decisions/024-026/ADR-026-two-pillars-shared-context.md) · [ADR-024](../../../decisions/024-026/ADR-024-holistic-plant-decisions.md) · [ADR-025](../../../decisions/024-026/ADR-025-improve-loop-step-06.md) · [architecture audit](./stamped-holistic-architecture-audit.md)

---

## Copy-paste prompt (full — start here)

```text
PLATFORM UPDATE — Holistic plant shared context (ADR-024/025) under the
two-pillar product lock (ADR-026).

FRAMING (mandatory — read first):
  One product. Exactly TWO outcome pillars:
    1) Load & Energy Efficiency Intelligence (hero ₹)
    2) Prescriptive Equipment Intelligence
  Shared context (NOT a third pillar, NOT an MES product):
    orders / MES-lite / departments / tradeoffs / negotiation / Improve
  Named outcomes: energy efficiency (hero) + plant effectiveness/OEE
  co-benefits on management Rx. Do not invent Pillar 3 or split products.

stamped-external is the single source of truth (ADR-011). Your product repo
must bump the `external/` submodule, READ the listed files, then PLAN (and
only after plan approval IMPLEMENT) the consumer-side changes for YOUR layer.
Do not invent a MES. Do not add L7. Do not edit files under external/.

═══════════════════════════════════════════════════════════════════
1) UPDATE THE PLATFORM SUBMODULE
═══════════════════════════════════════════════════════════════════

In this consumer repo:

  git submodule update --init --recursive
  test -f external/VERSION || { echo "missing external/"; exit 1; }

  cd external
  git fetch origin
  # Prefer a release tag after platform merge, e.g.:
  #   git checkout v2026.07.30
  # Until tagged, pin the SHA that contains contracts 0.10.0 + ADR-024/025:
  #   git log --oneline -- contracts/CHANGELOG.md decisions/ADR-024*
  git checkout <pin-tag-or-sha>
  cd ..

  # Confirm contracts bump:
  grep -n "0.10.0" external/contracts/CHANGELOG.md
  test -f external/decisions/024-026/ADR-024-holistic-plant-decisions.md
  test -f external/decisions/024-026/ADR-025-improve-loop-step-06.md

  git add external
  git commit -m "chore(external): pin stamped-external for ADR-024/025 holistic plant"

Run platform contract check (from repo root, if submodule scripts are used):

  bash external/scripts/contracts/contract-check.sh
  # or: sh external/scripts/contracts/contract-check.sh

═══════════════════════════════════════════════════════════════════
2) MANDATORY READING ORDER (all layers — do this before planning)
═══════════════════════════════════════════════════════════════════

Shared (everyone):
  1. external/decisions/024-026/ADR-026-two-pillars-shared-context.md
  2. external/handoff/holistic/stamped-holistic-architecture-audit.md
  3. external/decisions/024-026/ADR-024-holistic-plant-decisions.md
  4. external/decisions/024-026/ADR-025-improve-loop-step-06.md
  5. external/technical/STAMPED_ARCHITECTURE.md  (§2.1 six-step loop, Rx card, anti-confusion)
  6. external/technical/STAMPED_ARCHITECTURE.md  (§7 Improve + §7b Shared context)
  7. external/handoff/holistic/stamped-holistic-pilot-stack.md
  8. external/contracts/CHANGELOG.md  (0.10.0 section)
  9. external/AGENTS.md + ponytail skill before any code

Then layer-specific (read ONLY your layer block after shared):

── L1 connectors-edge / connectors-cloud / connectors-bill ──
  A. external/handoff/holistic/stamped-mes-erp-integration-brief.md
  B. external/contracts/schemas/plant/production-order.json
  C. external/contracts/schemas/telemetry/production-record.json
  D. external/contracts/schemas/envelope/stamped-record-envelope.json
  E. external/technical/layers/l1-l2/L1-connect-and-normalise.md  (ERP/MES sections)
  Plan: CSV MES-lite + optional SAP/Tally/OData path; emit production_order
        envelopes; never write to ERP.

── L2 universal-repositary ──
  A. external/contracts/schemas/plant/plant-department-graph.json
  B. external/contracts/schemas/plant/production-order.json
  C. external/contracts/schemas/telemetry/production-record.json
  D. external/technical/layers/l1-l2/L2-universal-repository.md  (§2.1 Production*)
  E. external/handoff/l2/core/stamped-l2-spec.md  (if present)
  Plan: store + query orders + department graph; no graph DB product.

── L3 intelligence-core + intelligence-rulepacks ──
  A. external/handoff/holistic/stamped-l3-tradeoff-engine-spec.md
  B. external/contracts/schemas/intelligence/finding.json  (optional decision_class)
  C. external/contracts/schemas/intelligence/prescription.json  (tradeoff, decision_class)
  D. external/contracts/fixtures/plant/plant_department_graph.valid.json
  E. external/contracts/fixtures/plant/production_order.valid.json
  Plan: TradeoffEngine for stagger_costart / load_shift_tod /
        furnace_preheat_early; never recommend hot-line stagger as primary
        when due_at blocks it.

── L4 knowledge-reasoning ──
  A. external/handoff/holistic/stamped-prescription-negotiation-spec.md
  B. external/contracts/schemas/intelligence/prescription-revision.json
  C. external/contracts/fixtures/intelligence/prescription_revision.valid.json
  D. external/decisions/020-023/ADR-023-l6-ems-and-analyst-context.md  (propose≠commit)
  E. external/technical/layers/l4-l6/L4-knowledge-and-reasoning.md
  Plan: POST /v1/negotiation/revise; template-bound only; human confirm.

── L5 closure-verification ──
  A. external/handoff/holistic/stamped-prescription-negotiation-spec.md
  B. external/handoff/holistic/improve/stamped-improve-pipeline-spec.md
  C. external/handoff/holistic/improve/stamped-improve-report-template.md
  D. external/contracts/schemas/closure/improvement-signal.json
  E. external/contracts/schemas/plant/plant-preference-profile.json
  Plan: revision workflow events; emit ImprovementSignal; monthly Improve
        job (draft prefs + markdown report); NO auto-promote without approval.

── L6 stamped-l6 ──
  A. external/handoff/holistic/stamped-prescription-negotiation-spec.md
  B. external/handoff/holistic/stamped-holistic-pilot-stack.md
  C. external/decisions/020-023/ADR-023-l6-ems-and-analyst-context.md
  D. external/design/forge-industrial-design-system.md  (six-step)
  Plan: Discuss UX on Rx detail; tradeoff on card; BFF→L5 live;
        fixtures only as USE_FIXTURES fallback. Improve report is INTERNAL
        (devs), not a customer nav item.

═══════════════════════════════════════════════════════════════════
3) HARD RULES (non-negotiable)
═══════════════════════════════════════════════════════════════════

  - Positioning: ₹ energy is the HERO; order/OEE/throughput are CO-BENEFITS
    (plant effectiveness — not Pillar 3).
  - Framing: two pillars + shared context only ([ADR-026]).
  - Not an MES / CMMS / quality system. Read + recommend only.
  - Improve is step 06, plant-scoped, human-gated — not a new layer repo.
  - Bounded action templates only (no free-text physical instructions).
  - Contract changes only in stamped-external PRs — never fork schemas here.
  - Ponytail: smallest diff; plan → approve → implement.
  - After implement: run external/scripts/contracts/contract-check.sh + repo tests.

═══════════════════════════════════════════════════════════════════
4) YOUR DELIVERABLE IN THIS SESSION
═══════════════════════════════════════════════════════════════════

  A. Confirm submodule pin (tag/SHA) and contracts 0.10.0 visible.
  B. Restate which layer you are (L1…L6) and which files you read.
  C. Restate framing: two pillars + shared context (not MES).
  D. Produce an IMPLEMENTATION PLAN only:
       Goal / Scope / Non-goals / Dependencies / Risks / Phases
  E. STOP for human approval before writing application code.
  F. Do not edit external/. Do not edit the holistic plan file.

If requirements conflict with ADR-024/025/026, STOP and ask — platform wins.
```

---

## Short form (Slack / ticket one-liner)

```text
Bump external/ to stamped-external pin with contracts 0.10.0 + ADR-024/025/026.
Read external/decisions/024-026/ADR-026-two-pillars-shared-context.md first, then
external/handoff/agents/prompts/stamped-holistic-consumer-prompt.md (full block). Plan YOUR
layer only — two pillars + shared context, no MES, no L7, no edits under external/.
```

---

## Per-repo checklist (company internal)

| Repo | Owner agent pastes | Done when |
| --- | --- | --- |
| connectors-edge / cloud | Full prompt + L1 block | `production_order` ingest Path B CSV |
| universal-repositary | Full prompt + L2 block | Orders + department graph queryable |
| intelligence-core / rulepacks | Full prompt + L3 block | Tradeoff on stagger/TOD/preheat |
| knowledge-reasoning | Full prompt + L4 block | Negotiation revise API |
| closure-verification | Full prompt + L5 block | Revision workflow + Improve job draft |
| stamped-l6 | Full prompt + L6 block | Discuss UX + live BFF path |

Pin note: until `v2026.07.30` (or later) is tagged on stamped-external, use the merge SHA that contains `contracts/CHANGELOG.md` **0.10.0**.
