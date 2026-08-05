# L5 Internal Console — Stamped ops cockpit (AD-7)

> Wave F sync · **Stamped staff only** · not customer Forge  
> **Authority:** [ADR-025](../../../decisions/024-026/ADR-025-improve-loop-step-06.md) · [ADR-027](../../../decisions/024-026/ADR-027-plant-calibration-champion-promote.md) · Positioning plan AD-5/AD-7  
> **Consumer:** `closure-verification/packages/internal-console` (port **8095**)

---

## Base

| Item | Value |
| --- | --- |
| API prefix | `/v1/internal/*` |
| Auth | `write:admin` |
| Customer L6 | Must **never** list `pending_stamped_review`, `withheld`, or failed-gate Rx |

---

## Positioning alignment

| Client narrative step | Console role |
| --- | --- |
| 1–2 Load / equipment | Filter inbox by `value_domain` / category |
| 3 Prescriptions | All-Rx inbox + gate diagnostics + force send/stop |
| 4 Agentic (lite) | Rank/dedupe already done in L4; staff override delivery only |

---

## Two surfaces, one truth

| Surface | Who | Sees |
| --- | --- | --- |
| **Internal console** | Stamped team | **All** Rx — practical, pending review, withheld, blocked_incomplete, force-sent |
| **L6 customer app** | Plant users | Only approved, client-deliverable Rx |

---

## Screens (Phase 3 minimum)

| Screen | Purpose |
| --- | --- |
| **All prescriptions** | Default landing — every Rx; filters: plant, status, pillar, category, gate result |
| **Review queue** | `stamped_rx_gate_enabled` plants with `pending_stamped_review` |
| **Rx detail** | Card + evidence flip + AD-5 gate checklist + finding refs |
| **Actions** | Approve · Force send (reason required) · Withhold / force stop · Admin note |
| **Plant settings** | Gate profile + `stamped_rx_gate_enabled` + Improve cadence |
| **Improve / ML** | Weekly Improve cycles; champion promote / rollback (ADR-027) |

---

## Staff daily flow

```text
Rx from L4 → gate score + diagnostics
  ├─ pass + gate off  → client delivery
  ├─ pass + gate on   → review queue → approve | force send
  └─ fail             → withheld (or pending if auto_withhold_on_gate_fail=false)
                          └─ fix upstream OR force send with reason
Delivered Rx can still Force stop / withhold.
```

---

## Routes

### Existing

| Method | Path |
| --- | --- |
| GET/PATCH | `/v1/internal/plants/{plantId}/settings` |
| GET | `/v1/internal/rx-review-queue` |
| POST | `/v1/internal/prescriptions/{id}/approve-for-client` |
| POST | `/v1/internal/prescriptions/{id}/withhold` |
| GET/POST | `/v1/internal/plants/{plantId}/improve/cycles` |
| POST | `/v1/internal/improve/cycles/{id}/approve` |
| POST | `/v1/internal/improve/cycles/{id}/reject` |
| GET | `/v1/internal/plants/{plantId}/signals` |
| GET/PUT | `/v1/internal/plants/{plantId}/notes` |
| POST | `/v1/internal/prescriptions/{id}/admin-notes` |
| GET | `/v1/internal/plants/{plantId}/ml/runs` |
| POST | `/v1/internal/plants/{plantId}/ml/finetune` |
| POST | `/v1/internal/plants/{plantId}/ml/runs/{runId}/promote` |
| POST | `/v1/internal/plants/{plantId}/ml/runs/{runId}/rollback` |

### Required additions (Phase 3)

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/v1/internal/prescriptions` | All Rx for staff (includes withheld / blocked); query filters |
| GET | `/v1/internal/prescriptions/{id}/gate-diagnostics` | Per AD-5 check pass/fail + score |
| POST | `/v1/internal/prescriptions/{id}/force-send` | Override gate block; body `{ reason, admin_note? }`; audit + `stamped_review_approved` |

---

## Plant gate profile (`plant-admin-settings` 1.1.0+)

| Setting | Purpose | Default |
| --- | --- | --- |
| `stamped_rx_gate_enabled` | Staff approve before client sees Rx | `false` (pilot often `true`) |
| `practicality_gate_mode` | `strict` \| `balanced` \| `lenient` | `balanced` |
| `require_named_owner` | Reject orphan owners | `true` |
| `require_evidence_refs` | Must have evidence pack | `true` |
| `require_mv_plan` | Must have verification plan | `true` |
| `min_impact_confidence` | Impact confidence floor | mode preset if unset |
| `allow_illustrative_impact` | Permit `[illustrative]` ₹ | `true` |
| `auto_withhold_on_gate_fail` | Fail → `withheld` vs review queue | `true` |

Mode presets (when individual flags unset):

| Mode | `min_impact_confidence` |
| --- | --- |
| strict | 0.6 |
| balanced | 0.5 |
| lenient | 0.4 |

PATCH via `/v1/internal/plants/{plantId}/settings`. Audited.

---

## AD-5 gate diagnostics (per Rx)

Checklist emitted by L4/L5 scoring (same fields for console UI):

1. Concrete action (asset + verb + parameter + stop/override)
2. Reason tied to observed deviation
3. Named ownership (role + department)
4. Feasible window
5. Honest effort
6. Impact (₹/reliability + confidence; illustrative flag OK if allowed)
7. Evidence pack
8. Verification (`mv_plan` + Finding `ops_clearance`)
9. Delivery intent (priority, channel, dedupe_key)

Failed checks → `withheld` or `pending_stamped_review` per plant profile. Never invent missing fields with prose.

---

## Invariants

- Improve job and fine-tune never auto-approve
- `pending_stamped_review` / `withheld` filtered from L6 customer lists
- Force send / withhold require actor + reason; emit workflow events
- Plant notes are manual scratchpad (not Improve Track C)
- No free-form rewrite of `what` in console — only delivery override
