# Control and action (how far we go)

**Lead with this, not “read-only.”** Buyers care that someone on their team stays in charge — and that actions that *can* be done from a desk do not stop at a WhatsApp ping forever.

## Default posture (what we sell today)

1. **Humans decide.** Prescriptions name what to change, who owns it, and when. Operators review and remain in control.  
2. **We do not silently write the plant.** No autonomous PLC / line control. No replacing EMS, MES, CMMS, or plant OS.  
3. **Closure still matters.** Assign → act → verify with evidence (ledger; bill confirmation optional).

Say **operators stay in control** and **human-guided action**. Do **not** open every pitch with “we are read-only.”

## Desk-side action path (when the plant wants it) `[!]`

Many energy and schedule moves are already desk-feasible: stagger a start, change a warm-up time, apply an approved idle setpoint, release a maintenance work request. Managers often want **one click from their desk** after they (or a named role) approve.

Where the plant’s systems expose a safe API or connector, and the customer **opts in**, Stamped can be configured so that **a human-approved prescription triggers the change in the target system** (examples to explore per site: scheduling / BAS setpoints, utility starts, ERP work orders, CNC/CAD or machine-cell interfaces when available).  

Rules for that path:

| Do | Do not |
|----|--------|
| Human approval (or explicit role policy) before any write | Autonomous plant control / “AI runs the line” |
| Plant-configured allowlists (which tags, which machines, which windows) | Blanket write access to OT |
| Audit trail of who approved and what changed | Silent background writes |
| Fall back to assign-only when writeback is off or unavailable | Promise CNC/CAD/PLC write for every plant on day one |

Treat specific write targets as **site-scoped product work**, not a blanket homepage claim until connectors exist.

## One-line variants

| Context | Prefer |
|---------|--------|
| Elevator | Verified-with-evidence decision layer. Your team stays in control. |
| OT / IT security | No silent writes. Human-approved action only where you enable it. |
| Manager who wants desk control | Prescribe, approve, and where you configure it, execute from the desk. |
| Old “read-only” slide footer | Complements Industry 4.0 · humans approve · no autonomous plant control |

## Related

- Client narrative: [`../client/POSITIONING_AND_NARRATIVE.md`](../client/POSITIONING_AND_NARRATIVE.md)  
- Website canon: [`../website/COPY_CANON.md`](../website/COPY_CANON.md)  
- Deck claim sheets: [`../decks/WHAT_WE_SHOW.md`](../decks/WHAT_WE_SHOW.md)
