# OT write site prerequisite checklist (Wave C)

> **Authority:** [ADR-029](../../decisions/028-032/ADR-029-human-guided-ot-command-path.md) · [L1 §5.4](../../technical/layers/l1-l2/L1-connect-and-normalise.md) · [L5 ActionIntent](../l5/stamped-l5-action-intent.md)  
> **Use:** Gate before enabling plant `machine-capability.writeback_enabled`. If any **Must** row fails → assign-only (Wave B).

---

## Must (all required)

| # | Check | Y/N | Notes |
| --- | --- | --- | --- |
| 1 | Plant IT accepts outbound-only edge (no inbound PLC exposure) | | |
| 2 | Target assets have **remote / desk-control mode** | | |
| 3 | Dedicated **command-tag interface** (or manufacturer remote API) — Approach A | | |
| 4 | Signed **allowlist** drafted (commands, assets, ranges, windows) | | |
| 5 | Named **approver role(s)** agreed for ActionIntent | | |
| 6 | Operational stop ≠ e-stop documented with plant OT | | |
| 7 | Beachhead commands limited to energy-soft set (idle aux / setpoint / schedule) | | |
| 8 | L5 ActionIntent + L1 write flavour available on this pin | | |

---

## Should

| # | Check | Y/N |
| --- | --- | --- |
| 9 | ACK + readback tags defined for verify | |
| 10 | Maintenance / OT contact for interlock rejects | |
| 11 | Liability / insurance note reviewed | |

---

## Site notes

**LNM / FANUC (example):** Prefer **read** via MTConnect / DC first. Enable write only if a PLC command IF or vendor remote API exists in front of the cell — not raw FOCAS memory writes in v1.

**Kill:** If 2 of 3 pilot targets fail Must rows within 60 days, keep Wave C architecture-only and sell Wave B desk assign + IT/CMMS writeback.

---

## Sign-off

| Role | Name | Date |
| --- | --- | --- |
| Plant OT / IT | | |
| Stamped pilot lead | | |
