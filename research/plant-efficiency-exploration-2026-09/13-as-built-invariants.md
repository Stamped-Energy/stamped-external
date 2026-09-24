# As-built L1–L6 invariants

**Date:** 2026-09-24  
**Status:** What the stack does today. The target is [`14-coarse-architecture.md`](14-coarse-architecture.md).  
**Authority for behavior:** layer atlas and READMEs below. **Authority for the company:** [`09-stamped-founder-vision.md`](09-stamped-founder-vision.md).

The parent folder `L1-L6` is a map of sibling repos. Contracts live in this `stamped-external` submodule. Only L2 opens the database. L3 through L6 use query HTTP.

## Path

Plant and document signals enter L1. Connectors-cloud validates and relays a `StampedRecordEnvelope` into L2. L3 reads L2 over HTTP, runs detectors, and emits Finding **1.2.0**. Only `status=emitted` and `delivery=l4` leave toward L4. L4 compiles those findings into Prescription **1.0.0** on emit, and always writes a compile trace (`emit`, `withhold`, or `abstain`). L5 ingests the prescription, notifies when enabled, and runs fail-closed clearance against L2. L6 shows customer-safe cards. Withhold and abstain stay off the customer screen.

Source: `docs/atlas/STACK.md` in the L1–L6 map (sibling of this submodule).

## Hops that must stay true until a contract bump

- **Edge to cloud.** Canonical JSON on MQTT. Tag mapping is signed. No OT write. Trust breaks on unmapped tags. Source: `docs/atlas/layers/L1-edge.md`, `docs/atlas/layers/L1-cloud.md`.
- **Bill to cloud.** A bill line publishes only after the rupee gate (`recompute_bill` within one rupee). Source: `docs/atlas/layers/L1-bill.md`.
- **Cloud to L2.** HTTP ingest, schema, dedupe. L2 down holds the outbox. Source: `docs/atlas/layers/L2.md`.
- **L2 to L3.** Query HTTP only. No `L2_DATABASE_URL` in L3–L6. Source: `docs/atlas/STACK.md` decision 1, `docs/atlas/layers/L3.md`.
- **L3 to L4.** Finding **1.2.0** with `status=emitted` and `delivery=l4`. Lab statuses never become operator work. Source: `docs/atlas/layers/L3.md`, `docs/atlas/STACK.md` decision 2.
- **L4 to L5.** Prescription **1.0.0** on emit. Compile trace always. Source: `docs/atlas/layers/L4.md`.
- **L5 to L6.** Customer UI hides staff-only statuses. Ops-confirmed is not bill-verified. Source: `docs/atlas/layers/L5.md`, `docs/atlas/layers/L6.md`.

## What each layer refuses today

- **L1 edge** does not write OT registers and does not open the L2 database. Protocols in code include Modbus, MQTT, OPC UA, file, REST, and historian. DLMS, BACnet, and MTConnect are documented as sim-first. Source: `docs/atlas/layers/L1-edge.md`.
- **L3** does not invent rupees. Tariff comes from L2 or a tagged fallback. Hot, warm, and cold paths exist. Many CNC and adaptive engines stay dark until a flag and tags exist. Shadows are not operator truth. Source: `docs/atlas/layers/L3.md`.
- **L4** is a gated compiler. The language model does not browse raw graph state, the open web, or L2 SQL, and does not invent rupees. Template lane uses no model for money proof runs. Ask Analyst is a separate bounded read surface. Source: `docs/atlas/layers/L4.md`.
- **L5** workflow today is open, in progress, done, verified. Clearance fails closed when data is insufficient. WhatsApp is default off. Source: `docs/atlas/layers/L5.md`.
- **L6** never holds upstream keys in the browser. Live and Preview badges stay distinct. Source: `docs/atlas/layers/L6.md`.

## What a later contract change has to touch

Prescription **1.0.0** is the break point for a new card. It is energy-shaped and rejects unknown fields. Finding **1.2.0** can gain fields only as an explicit bump. The dual-lane rule, the L2-only database, the rupee gate, and “lab never promotes” are invariants of the spine, not of the old compiler.
