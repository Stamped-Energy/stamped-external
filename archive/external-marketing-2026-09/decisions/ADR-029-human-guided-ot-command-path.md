# ADR-029: Human-guided OT command path (opt-in ActionIntent)

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-08-21 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-001](../001-005/ADR-001-l1-repo-split-and-boundaries.md) · [ADR-005](../001-005/ADR-005-edge-agent-go-architecture.md) · [ADR-019](../016-020/ADR-019-l5-runtime-and-consistency.md) · [ADR-022](../020-023/ADR-022-l6-bff-runtime-boundary.md) · [ADR-024](../024-026/ADR-024-holistic-plant-decisions.md) · [ADR-028](ADR-028-dual-plant-graphs-and-path-d.md) · [`copy/CONTROL_AND_ACTION.md`](../../copy/CONTROL_AND_ACTION.md) · [L1](../../technical/layers/l1-l2/L1-connect-and-normalise.md) · [L5](../../technical/layers/l4-l6/L5-closure-and-verification.md) · [L6](../../technical/layers/l4-l6/L6-experience-and-integration.md) |

---

## Context

Copy already sells **human-guided desk execution** where the plant opts in ([`CONTROL_AND_ACTION.md`](../../copy/CONTROL_AND_ACTION.md)). Clients report Execute friction: prescriptions die when nobody is on the floor to act, or when acting means opening a separate HMI.

Architecture still treated OT write as a hard ban ([ADR-024](../024-026/ADR-024-holistic-plant-decisions.md) non-goals, [ADR-028](ADR-028-dual-plant-graphs-and-path-d.md) non-tradeables, L5 “No SCADA write path”). That contradiction blocks honest sales and Wave C engineering.

Stamped must **not** become a plant OS, EMS, or universal machine control plane. It must remain a **decision + approval + verified command** layer that talks to **plant-owned** command interfaces.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Product | Opt-in **human-guided command path**, not autonomous OT control or plant OS |
| 2 | Non-tradeable rewrite | **No silent or autonomous OT write**; human-approved `ActionIntent` only when plant enables writeback |
| 3 | Approach | **Approach A:** write only to plant-defined PLC/CNC **command tags / vendor remote APIs** — never arbitrary registers, never direct drive I/O in v1 |
| 4 | Ownership | **L5** owns authz, ActionIntent lifecycle, audit; **L1 edge** owns protocol write + ACK; **L6** is Approve/Execute UI only (BFF → L5, never OT) |
| 5 | Beachhead | Soft OT energy actions: idle aux stop, approved setpoint, schedule release — not FANUC cycle start, not e-stop |
| 6 | Staging | Spec now; **code in Wave C** after site survey (remote mode + CMD tags). Wave B = desk assign/confirm without OT write |
| 7 | Safety | Operational stop ≠ e-stop; safety circuits remain independently authoritative |
| 8 | Offline | Edge refuses **new** remote commands when cloud/allowlist unavailable; already-dispatched local handling per plant policy |

---

## 1. Command path (canonical)

```text
L4 Prescription → L6 human Approve/Execute → L5 ActionIntent
  → signed dispatch to L1 edge → OPC UA / Modbus command tags
  → plant PLC validates (remote mode, interlocks, ranges)
  → ACK → L5 verify on telemetry
```

Raw `POST /write-register` is **forbidden**. Semantic commands only (`SET_TEMPERATURE`, `STOP_IDLE_AUX`, `APPLY_STAGGER`, …) mapped via plant allowlist.

---

## 2. Layer duties

| Layer | May | Must not |
| --- | --- | --- |
| L3 / L4 | Prescribe, name command family | Actuate |
| L5 | Create/approve/dispatch ActionIntent; audit; verify | Open OPC/Modbus from cloud |
| L6 | Desk Approve/Execute UX | Call OT or edge write APIs directly |
| L1 edge | Write allowlisted command tags; ACK; refuse when offline/not remote | Expose inbound PLC to internet; bypass plant PLC validation |
| L2 | Store measurements / ledger | Write OT |

---

## 3. Plant prerequisites (Wave C gate)

Site must provide before OT write is enabled:

1. Remote / desk-control mode on target assets  
2. Dedicated command-tag interface (or manufacturer remote API)  
3. Signed allowlist OTA’d to edge (commands, assets, ranges, windows)  
4. Named approver role(s) in L5  

If unmet → **assign-only** (Wave B). No fake Execute button.

---

## 4. Supersedes / amends

| Artifact | Change |
| --- | --- |
| ADR-024 §4 Non-goals | “OT write-back” → no **silent/autonomous** OT write; opt-in ActionIntent per this ADR |
| ADR-028 decision §9 | “no OT write” → **no silent or autonomous OT write**; link this ADR |
| L5 / L1 / L6 SSOTs | Spec ActionIntent + edge write path (follow-on docs commits) |
| Holistic pilot | Wave C opt-in; not Wave A |

Does **not** supersede: calculator-owned money; T4 never sole ₹; negotiation never auto-commits; L5 owns Rx approval for delivery.

---

## Consequences

- Contracts: `action-intent.json`, machine capability / allowlist sketch  
- Handoffs: L5 ActionIntent, L1 write path, OT site checklist, pilot Wave B/C  
- Edge (`connectors-edge`): write plugin flavour later — **not** this ADR’s code scope  
- Copy: keep human-guided language; link this ADR from `CONTROL_AND_ACTION.md`

---

## Alternatives considered

| Option | Rejected because |
| --- | --- |
| Keep hard OT ban forever | Contradicts sold desk path; leaves Execute gap |
| Universal machine control plane | Category break vs decision layer; liability |
| Approach B (direct VFD/servo) in v1 | Bypasses plant ICS; unsafe for beachhead |
| Cloud → PLC inbound | Violates Purdue / Indian plant IT posture |
| Autonomous execute-within-limits now | Needs trust + eval; separate later ADR |
