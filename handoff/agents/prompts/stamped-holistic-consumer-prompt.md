# Prompt — Five-domain decision loop (ADR-030)

> **Use this:** One copy-paste block for **any** Stamped consumer-repo agent (L1–L6).  
> **Platform:** [Vinayak-RZ/stamped-external](https://github.com/Vinayak-RZ/stamped-external)  
> **Authority:** [ADR-030](../decisions/028-032/ADR-030-five-domain-decision-loop.md) · [ADR-025](../../../decisions/024-026/ADR-025-improve-loop-step-06.md) · founder vision [`09`](../../../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md) · agent contract [`10`](../../../research/plant-efficiency-exploration-2026-09/10-stamped-vision-agent-alignment.md) · [console AD-7](../../holistic/improve/stamped-l5-internal-console-handoff.md)

---

## Copy-paste prompt (full — start here)

```text
PLATFORM UPDATE — Five-domain decision loop (ADR-030).
Contracts pin: confirm current stamped-external VERSION / contracts CHANGELOG.

FRAMING (mandatory — read first):
  Product name: Stamped (never append Energy to the product name).
  One product. One decision card. Five domains:
    energy · cost · time/throughput · continuity/flow · short-horizon exceptions
  Default autonomy: recommend and assign; humans decide and execute.
  Energy is the entry wedge, not the category.
  Client narrative: choose → assign → verify the next operating action.
  Do not invent savings bands. Do not teach prior framing (tag v2026.09.24)
  as live identity. Do not replace MES / ERP / APS. Hard stops per ADR-030.

GENERIC-ENERGY FIRST (Wave A) before order-aware Wave B:
  Wave A: MD/PF/ToD + idle_load + compressor_sp_drift (when signals exist)
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
  # Pin to the SHA/tag that includes ADR-030; confirm:
  test -f decisions/028-032/ADR-030-five-domain-decision-loop.md
  git checkout <pin-tag-or-sha> && cd ..
  git add external
  git commit -m "chore(external): pin stamped-external for ADR-030 framing"
  bash external/scripts/contracts/contract-check.sh

═══════════════════════════════════════════════════════════════════
2) MANDATORY READING ORDER
═══════════════════════════════════════════════════════════════════

Shared:
  1. external/decisions/028-032/ADR-030-five-domain-decision-loop.md
  2. external/research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md
  3. external/research/plant-efficiency-exploration-2026-09/10-stamped-vision-agent-alignment.md
  4. external/handoff/holistic/stamped-holistic-pilot-stack.md
  5. external/handoff/holistic/improve/stamped-l5-internal-console-handoff.md
  6. external/decisions/024-026/ADR-025-improve-loop-step-06.md
  7. external/technical/STAMPED_ARCHITECTURE.md
  8. external/contracts/CHANGELOG.md (pin version)
  9. external/AGENTS.md + ponytail skill before any code

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

  - Five-domain decision loop ([ADR-030]); energy wedge only.
  - Not MES/CMMS/APS. Improve weekly human-gated — not L7.
  - Bounded templates only. Contract changes only in stamped-external.
  - Commit after each validated milestone; push check at 10 unpushed.
  - Ponytail: smallest diff. Run contract-check + repo tests after implement.

═══════════════════════════════════════════════════════════════════
4) DELIVERABLE THIS SESSION
═══════════════════════════════════════════════════════════════════

  A. Confirm submodule pin includes ADR-030.
  B. Restate layer (L1…L6) + files read + framing.
  C. IMPLEMENTATION PLAN only; STOP for approval before app code.
  D. Do not edit external/.

If requirements conflict with ADR-030 / 09, STOP — platform wins.
```

---

## Short form

```text
Bump external/ to stamped-external with ADR-030. Read ADR-030 + 09 + 10 +
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

Pin note: use the stamped-external SHA/tag that includes ADR-030.
