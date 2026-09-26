# L5 — Closure and verification

*Status: as-built · 2026-09-26*  
*Authority:* [STAMPED_ARCHITECTURE.md](../STAMPED_ARCHITECTURE.md) §5 · §7 · [ADR-019](../../decisions/016-020/ADR-019-l5-runtime-and-consistency.md) · [ADR-020](../../decisions/020-023/ADR-020-l5-mv-claim-governance.md) · [ADR-021](../../decisions/020-023/ADR-021-l5-notification-and-evidence.md)

L5 owns the **live card**: assign a person, notify, track workflow, verify against L2 telemetry, close honestly, write ledger intents. It does not draft recommendations (L4) and is not the customer Forge UI (L6).

| Label | Meaning |
| --- | --- |
| **as-built** | `closure-verification` (`stamped-l5`) |
| **contract** | prescription / card-proposal dual-read · workflow-event · ledger-entry |
| **direction** | Full IPMVP bill M&V as product gate (ops clearance is the shipped verification path) |

---

## Repo

| Repo | Job | Must not |
| --- | --- | --- |
| `closure-verification` | Ingest proposals → alarm → notify → workflow → clearance → ledger; internal console | L3 detectors; invent recommendations; override L4 withhold; `L2_DATABASE_URL` |

Primary surfaces: FastAPI `:8080` · worker tick · internal console `:8095`.

---

## Pipeline (as-built)

```text
POST /v1/prescriptions/ingest
  → gates / delivery judge (when stamped gate off)
  → alarm (when open)
  → notify (WhatsApp; SMS fallback)
  → workflow (open → in_progress → done → verified)
  → clearance poll on L2 tags (ops_clearance)
  → ledger (potential → ops_confirmed realised)
```

| Evidence label | Meaning |
| --- | --- |
| `ops_confirmed` | Telemetry clearance passed — **not** DISCOM bill-verified |
| `bill_label` | Separate; default unverified until bill reconciliation matches |

Customer L6 must hide staff-only statuses (withhold / pending review). Internal console sees them.

---

## Autonomy and hard stops

**Default: no autonomous actions.** A class runs only after Stamped certifies it and a named plant owner enables it. Idle-load and equipment actions are not in the catalog.

Hard stops that never become autonomy classes: automatic safety / remote critical-equipment command; quality hold release; maintenance authorization; silent change to customer priority, promise date, routing, master data, or full dispatch.

Optional human-guided OT path is allow-listed ActionIntent only ([ADR-029](../../decisions/028-032/ADR-029-human-guided-ot-command-path.md)) — not silent control.

---

## Related

- Layer handoff: [`../../handoff/l5/stamped-l5-architecture-handoff.md`](../../handoff/l5/stamped-l5-architecture-handoff.md)
- L4 proposals: [`../l4/30-as-built.md`](../l4/30-as-built.md)
- L6 experience: [`L6-experience.md`](L6-experience.md)
