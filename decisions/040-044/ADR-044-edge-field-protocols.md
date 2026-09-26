# ADR-044: edge field protocols (BACnet, DLMS, MTConnect)

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-27 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-001](../001-005/ADR-001-l1-repo-split-and-boundaries.md) · [ADR-005](../001-005/ADR-005-edge-agent-go-architecture.md) · research `docs/plans/l1-complete/RESEARCH.md` |

---

## Context

`bacnet`, `dlms`, and `mtconnect` connectors are sim-first: a non-empty field endpoint returns a pilot-gate error. This run needs Docker-proven read paths. Maintained Go libraries were surveyed; proof against a plant meter is out of scope.

---

## Decision

| Protocol | Client | Read-only surface | Simulator (proof) |
| --- | --- | --- | --- |
| **BACnet/IP** | `github.com/otfabric/go-bacnet@v0.3.0` (MIT) | `ReadProperty` / `ReadPropertyMultiple` over UDP **47808**. Wrapper must not call or export Write*, Create/DeleteObject, ReinitializeDevice, DCC | `python:3.12-slim-bookworm` + `bacpypes3==0.0.106` analog-value |
| **DLMS/COSEM** | **In-house** WRAPPER + GET (do not import Gurux; `gxdlms-go` is GPL-2.0) | TCP WRAPPER, LN, AARQ/AARE, **GET** of attribute 2 for OBIS `1.0.1.7.0.255`, `1.0.99.1.0.255`, `1.0.98.1.0.255`. No SET / ACTION / IMAGE | `mcr.microsoft.com/dotnet/sdk:9.0` building Gurux.DLMS.Simulator.Net, TCP **4059**, template `LN-v2-High.xml` |
| **MTConnect** | Go stdlib `net/http` + `encoding/xml` | `GET {endpoint}/current` and `/sample` | `mtconnect/demo:2.7` (official cppagent + simulator; Hub has no `mtconnect/cppagent`) |

Field paths are **simulator-proven** until a named plant run is recorded. Unmapped tags → `unmapped_tag`, never a zero.

---

## Hard stops

- L1 exposes only read or subscribe on field protocol paths.
- No OT write. A test asserts that no write function is reachable from the connector package API.
- No `L2_DATABASE_URL`.
- Lab simulator passwords are not plant secrets.

---

## Consequences

- B6 implements the clients and compose sims; interop against a real device is a later ADR.
- Windows Docker uses a user-defined bridge and **unicast** BACnet ReadProperty (no `--network host`).
- Choosing Gurux in-process later requires a license ADR (GPL vs commercial).

---

## Rejected alternatives

- `alexbeltran/gobacnet` (GPL-era, last 2024).
- Linking `github.com/Gurux/gxdlms-go` into edge-agent.
- Treating sim success as a plant-certified stack.
