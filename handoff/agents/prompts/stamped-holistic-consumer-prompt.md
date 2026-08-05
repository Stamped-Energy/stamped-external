# Prompt — Positioning + holistic plant (ADR-024–027)

> **Use this:** One copy-paste block for **any** Stamped consumer-repo agent (L1–L6).  
> **Platform:** [Vinayak-RZ/stamped-external](https://github.com/Vinayak-RZ/stamped-external)  
> **Authority:** [ADR-026](../../../decisions/024-026/ADR-026-two-pillars-shared-context.md) · [ADR-024](../../../decisions/024-026/ADR-024-holistic-plant-decisions.md) · [ADR-025](../../../decisions/024-026/ADR-025-improve-loop-step-06.md) · [architecture audit](../../holistic/stamped-holistic-architecture-audit.md) · [console AD-7](../../holistic/improve/stamped-l5-internal-console-handoff.md)

---

## Copy-paste prompt (full — start here)

```text
PLATFORM UPDATE — Positioning-aligned generic-energy pilot + holistic Phase 5
(ADR-024/025/026/027). Contracts ≥ 0.11.2.

FRAMING (mandatory — read first):
  One product. Exactly TWO outcome pillars:
    1) Load & Energy Efficiency Intelligence (hero ₹)
    2) Prescriptive Equipment Intelligence
  Shared context (NOT a third pillar, NOT an MES product):
    orders / MES-lite / departments / tradeoffs / negotiation / Improve
  Client narrative order (do NOT lead with "agentic AI"):
    load → equipment ML → practical prescriptions → agentic layer
  Named outcomes: energy efficiency (hero) + plant effectiveness/OEE
  co-benefits on management Rx. Do not invent Pillar 3 or split products.

GENERIC-ENERGY FIRST (Wave A) before order-aware Wave B:
  Pillar 1: MD/PF/ToD + idle_load
  Pillar 2: compressor_sp_drift (abnormal_duty only if signals exist)
  L5 Internal Console: ALL Rx visible to Stamped staff; force send/stop;
  plant practicality_gate_mode. Customer L6 sees approved only.

AD-5 PRACTICALITY GATE (client-visible Rx must have):
  concrete action · reason · role+department owner · feasible window ·
  honest effort · impact ([illustrative] OK if allowed) · evidence ·
  mv_plan/ops_clearance · delivery intent. Incomplete → withheld /
  pending_stamped_review — never fill gaps with prose.

stamped-external is the single source of truth (ADR-011). Your product repo
must bump the `external/` submodule, READ the listed files, then PLAN (and
only after plan approval IMPLEMENT) the consumer-side changes for YOUR layer.
Do not invent a MES. Do not add L7. Do not edit files under external/.

═══════════════════════════════════════════════════════════════════
1) UPDATE THE PLATFORM SUBMODULE
═══════════════════════════════════════════════════════════════════

  git submodule update --init --recursive
  test -f external/VERSION || { echo "missing external/"; exit 1; }
  cd external && git fetch origin
  # Prefer v2026.08.05+ ; confirm:
  grep -n "0.11.2" contracts/CHANGELOG.md
  git checkout <pin-tag-or-sha> && cd ..
  git add external
  git commit -m "chore(external): pin stamped-external for practical Rx gates"
  bash external/scripts/contracts/contract-check.sh

═══════════════════════════════════════════════════════════════════
2) MANDATORY READING ORDER
═══════════════════════════════════════════════════════════════════

Shared:
  1. external/decisions/024-026/ADR-026-two-pillars-shared-context.md
  2. external/technical/product/Stamped_Client_Positioning_and_Narrative_v1.md
  3. external/demo-decks/prescriptions-examples.md
  4. external/handoff/holistic/stamped-holistic-architecture-audit.md
  5. external/handoff/holistic/stamped-holistic-pilot-stack.md
  6. external/handoff/holistic/improve/stamped-l5-internal-console-handoff.md
  7. external/decisions/024-026/ADR-024-holistic-plant-decisions.md
  8. external/decisions/024-026/ADR-025-improve-loop-step-06.md
  9. external/technical/STAMPED_ARCHITECTURE.md
  10. external/contracts/CHANGELOG.md (0.11.2)
  11. external/AGENTS.md + ponytail skill before any code

Layer blocks:

── L1 ── Wave A: meter + idle/output + compressor kW/pressure + bill MD/PF.
  Wave B later: production_order (mes-erp brief). Never OT write.

── L2 ── Wave A: baselines SEC/duty; Finding/Prescription ingest.
  Wave B: ProductionOrder + department graph. No graph DB.

── L3 ── Wave A: emit idle_load + compressor_sp_drift with value_domain;
  MD/PF/ToD remain; golden/eval. Wave B: TradeoffEngine. Shadow never customer-facing.

── L4 ── Wave A: pilot templates; AD-5 fields; rank/dedupe; gate diagnostics.
  No free-form What rewrite. Wave B: POST /v1/negotiation/revise.

── L5 ── Wave A: gate vs plant-admin-settings; all-Rx console; force-send/
  withhold; approve-for-client; WhatsApp shadow. Wave B: negotiation + Improve full.
  Read: stamped-l5-internal-console-handoff.md

── L6 ── Wave A: BFF→L5 live; Rx card + flip evidence; exclude withheld/
  pending_stamped_review. Wave B: Discuss + tradeoff. Improve is INTERNAL only.

═══════════════════════════════════════════════════════════════════
3) HARD RULES
═══════════════════════════════════════════════════════════════════

  - ₹ energy HERO; order/OEE CO-BENEFITS. Two pillars only ([ADR-026]).
  - Not MES/CMMS. Improve weekly human-gated — not L7.
  - Bounded templates only. Contract changes only in stamped-external.
  - Commit after each validated milestone; push check at 10 unpushed.
  - Ponytail: smallest diff. Run contract-check + repo tests after implement.

═══════════════════════════════════════════════════════════════════
4) DELIVERABLE THIS SESSION
═══════════════════════════════════════════════════════════════════

  A. Confirm submodule pin and contracts ≥ 0.11.2.
  B. Restate layer (L1…L6) + files read + framing.
  C. IMPLEMENTATION PLAN only; STOP for approval before app code.
  D. Do not edit external/.

If requirements conflict with ADR-024/025/026, STOP — platform wins.
```

---

## Short form

```text
Bump external/ to stamped-external ≥ 0.11.2 / v2026.08.05. Read ADR-026 +
stamped-holistic-consumer-prompt.md. Wave A = generic-energy (idle + compressor
SP + practical Rx gates + L5 console). Wave B = orders/Tradeoff/Discuss. No MES, no L7.
```

---

## Per-repo checklist (Wave A done when)

| Repo | Done when |
| --- | --- |
| connectors-edge / cloud / bill | Pilot tags + bill MD/PF envelopes publish |
| universal-repositary | Baseline/evidence queries for idle + compressor |
| intelligence-core / rulepacks | Findings emit with `value_domain` |
| knowledge-reasoning | Practical templates compile |
| closure-verification | Gate + all-Rx console + force send/stop |
| stamped-l6 | Live approved-only Rx + flip evidence |

Pin note: use `v2026.08.05` or SHA with contracts **0.11.2**.
