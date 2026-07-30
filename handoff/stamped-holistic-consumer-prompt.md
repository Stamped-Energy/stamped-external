# Prompt — Holistic plant effectiveness (ADR-024 / ADR-025)

> **Use this:** One copy-paste block for **any** Stamped consumer-repo agent (L1–L6).  
> **Also paste into:** company onboarding / internal eng channel when spinning agents on this work.  
> **Platform:** [Vinayak-RZ/stamped-external](https://github.com/Vinayak-RZ/stamped-external)  
> **Authority:** [ADR-024](../decisions/ADR-024-holistic-plant-decisions.md) · [ADR-025](../decisions/ADR-025-improve-loop-step-06.md) · [architecture audit](./stamped-holistic-architecture-audit.md)

---

## Copy-paste prompt (full — start here)

```text
PLATFORM UPDATE — Holistic plant effectiveness (energy wedge + order/MES
context + prescription negotiation + Improve step 06).

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
  test -f external/decisions/ADR-024-holistic-plant-decisions.md
  test -f external/decisions/ADR-025-improve-loop-step-06.md

  git add external
  git commit -m "chore(external): pin stamped-external for ADR-024/025 holistic plant"

Run platform contract check (from repo root, if submodule scripts are used):

  bash external/scripts/contract-check.sh
  # or: sh external/scripts/contract-check.sh

═══════════════════════════════════════════════════════════════════
2) MANDATORY READING ORDER (all layers — do this before planning)
═══════════════════════════════════════════════════════════════════

Shared (everyone):
  1. external/handoff/stamped-holistic-architecture-audit.md
  2. external/decisions/ADR-024-holistic-plant-decisions.md
  3. external/decisions/ADR-025-improve-loop-step-06.md
  4. external/technical/01-product-architecture.md  (§2.1 six-step loop, Rx card)
  5. external/technical/03-two-pillar-technical-bridge.md  (§7 Improve)
  6. external/handoff/stamped-holistic-pilot-stack.md
  7. external/contracts/CHANGELOG.md  (0.10.0 section)
  8. external/AGENTS.md + ponytail skill before any code

Then layer-specific (read ONLY your layer block after shared):

── L1 connectors-edge / connectors-cloud / connectors-bill ──
  A. external/handoff/stamped-mes-erp-integration-brief.md
  B. external/contracts/schemas/production-order.json
  C. external/contracts/schemas/production-record.json
  D. external/contracts/schemas/stamped-record-envelope.json
  E. external/technical/layers/L1-connect-and-normalise.md  (ERP/MES sections)
  Plan: CSV MES-lite + optional SAP/Tally/OData path; emit production_order
        envelopes; never write to ERP.

── L2 universal-repositary ──
  A. external/contracts/schemas/plant-department-graph.json
  B. external/contracts/schemas/production-order.json
  C. external/contracts/schemas/production-record.json
  D. external/technical/layers/L2-universal-repository.md  (§2.1 Production*)
  E. external/handoff/stamped-l2-spec.md  (if present)
  Plan: store + query orders + department graph; no graph DB product.

── L3 intelligence-core + intelligence-rulepacks ──
  A. external/handoff/stamped-l3-tradeoff-engine-spec.md
  B. external/contracts/schemas/finding.json  (optional decision_class)
  C. external/contracts/schemas/prescription.json  (tradeoff, decision_class)
  D. external/contracts/fixtures/plant_department_graph.valid.json
  E. external/contracts/fixtures/production_order.valid.json
  Plan: TradeoffEngine for stagger_costart / load_shift_tod /
        furnace_preheat_early; never recommend hot-line stagger as primary
        when due_at blocks it.

── L4 knowledge-reasoning ──
  A. external/handoff/stamped-prescription-negotiation-spec.md
  B. external/contracts/schemas/prescription-revision.json
  C. external/contracts/fixtures/prescription_revision.valid.json
  D. external/decisions/ADR-023-l6-ems-and-analyst-context.md  (propose≠commit)
  E. external/technical/layers/L4-knowledge-and-reasoning.md
  Plan: POST /v1/negotiation/revise; template-bound only; human confirm.

── L5 closure-verification ──
  A. external/handoff/stamped-prescription-negotiation-spec.md
  B. external/handoff/stamped-improve-pipeline-spec.md
  C. external/handoff/stamped-improve-report-template.md
  D. external/contracts/schemas/improvement-signal.json
  E. external/contracts/schemas/plant-preference-profile.json
  Plan: revision workflow events; emit ImprovementSignal; monthly Improve
        job (draft prefs + markdown report); NO auto-promote without approval.

── L6 stamped-l6 ──
  A. external/handoff/stamped-prescription-negotiation-spec.md
  B. external/handoff/stamped-holistic-pilot-stack.md
  C. external/decisions/ADR-023-l6-ems-and-analyst-context.md
  D. external/design/forge-industrial-design-system.md  (six-step)
  Plan: Discuss UX on Rx detail; tradeoff on card; BFF→L5 live;
        fixtures only as USE_FIXTURES fallback. Improve report is INTERNAL
        (devs), not a customer nav item.

═══════════════════════════════════════════════════════════════════
3) HARD RULES (non-negotiable)
═══════════════════════════════════════════════════════════════════

  - Positioning: ₹ energy is the HERO; order/OEE/throughput are CO-BENEFITS.
  - Not an MES / CMMS / quality system. Read + recommend only.
  - Improve is step 06, plant-scoped, human-gated — not a new layer repo.
  - Bounded action templates only (no free-text physical instructions).
  - Contract changes only in stamped-external PRs — never fork schemas here.
  - Ponytail: smallest diff; plan → approve → implement.
  - After implement: run external/scripts/contract-check.sh + repo tests.

═══════════════════════════════════════════════════════════════════
4) YOUR DELIVERABLE IN THIS SESSION
═══════════════════════════════════════════════════════════════════

  A. Confirm submodule pin (tag/SHA) and contracts 0.10.0 visible.
  B. Restate which layer you are (L1…L6) and which files you read.
  C. Produce an IMPLEMENTATION PLAN only:
       Goal / Scope / Non-goals / Dependencies / Risks / Phases
  D. STOP for human approval before writing application code.
  E. Do not edit external/. Do not edit the holistic plan file.

If requirements conflict with ADR-024/025, STOP and ask — platform wins.
```

---

## Short form (Slack / ticket one-liner)

```text
Bump external/ to stamped-external pin with contracts 0.10.0 + ADR-024/025.
Read external/handoff/stamped-holistic-consumer-prompt.md (full block) and
external/handoff/stamped-holistic-architecture-audit.md, then plan YOUR layer
only — no MES, no L7, no edits under external/.
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
