# Prescription negotiation loop — L4 / L5 / L6

> **Authority:** [ADR-024](../../decisions/024-026/ADR-024-holistic-plant-decisions.md) · [ADR-023](../../decisions/020-023/ADR-023-l6-ems-and-analyst-context.md) · [`prescription-revision.json`](../../contracts/schemas/intelligence/prescription-revision.json) · [`improvement-signal.json`](../../contracts/schemas/closure/improvement-signal.json)  
> **Audience:** knowledge-reasoning (L4), closure-verification (L5), stamped-l6  
> **Status:** Spec for Phase 2 build

---

## 1. Mission

Let a supervisor **push back** on a management prescription with a constraint ("can't stagger Line 2 until order 8842 clears") and receive a **bounded revised prescription** in the same shift — human confirms before workflow advances.

Distinct from read-only Analyst (ADR-023 Mode A/B).

---

## 2. Sequence

```
Supervisor (L6 Discuss) → L6 BFF → L4 POST /v1/negotiation/revise
  → L4 calls L3 TradeoffEngine with constraints
  → L4 emits PrescriptionRevision (confirmation=proposed)
  → L5 stores thread + revision; emits improvement_signal negotiation_objection
  → L6 shows diff; supervisor Accept | Reject | Escalate
  → on Accept: L5 prescription.revised; new Rx supersedes old; WorkflowEvent
```

---

## 3. L4 API sketch

| Method | Path | Auth | Body |
| --- | --- | --- | --- |
| POST | `/v1/negotiation/revise` | plant-scoped key | `{ rx_id, constraint_summary, constraints?, analyst_envelope? }` |
| GET | `/v1/negotiation/threads/{id}` | read | thread messages + revisions |

**Hard rules:**

- Output must validate `prescription-revision.json`
- `revised_prescription.what` must stay on approved template family (parameter change only)
- Numeric impact from calculator only
- Rules veto before return
- Max 1 LLM call for constraint parsing → structured `constraints`; Prefer structured chips from L6 over free text when possible
- Step/token budget like analyst ReAct; no OT tools

---

## 4. L5 workflow

| Event | When |
| --- | --- |
| `prescription.negotiation_started` | Discuss opened |
| `prescription.revision_proposed` | L4 revision stored |
| `prescription.revised` | Supervisor accepted; old Rx superseded |
| `prescription.negotiation_rejected` | Supervisor rejected revision |

Emit `ImprovementSignal` (`negotiation_objection` or `rx_outcome`) on close of thread.

Thread store: append-only messages `{ role, text, at, constraint_chips[] }` under `negotiation_thread_id`.

---

## 5. L6 UX — "Discuss this prescription"

On Rx detail (management-class only in P0):

1. Button **Discuss**
2. Side panel: chips for protected orders / exclude lines / no_stagger_until (user-visible, removable — same policy as AnalystContextEnvelope)
3. Free-text box for constraint summary
4. **Propose revision** → loading → diff view (what/impact/tradeoff)
5. **Accept revision** / **Keep original** / **Escalate to plant head**

Irreversible: Accept requires explicit click (ADR-023 §9).

Fixture-first seed may mock L4; live wiring is Phase 2.

---

## 6. Safety

| Threat | Control |
| --- | --- |
| Free-text unsafe What | Template-bound only |
| Prompt injection via constraint | Structured constraints; schema validate |
| Silent auto-apply | confirmation.status must leave `proposed` via human |

---

## 7. Acceptance

1. Fixture negotiation produces valid `prescription_revision.valid.json` shape.
2. Accept creates new Rx with `supersedes_rx_id`.
3. ≥30% of deferred/disputed mgmt Rx in pilot resolve via revision (product metric).
