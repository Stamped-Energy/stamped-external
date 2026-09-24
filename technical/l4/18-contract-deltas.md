# Contract deltas (cross-layer)

**Status:** Deltas required so L4 architecture can run. Not a full rewrite of L1–L6 contracts.  
**Related:** [ADR-031](../../decisions/028-032/ADR-031-l1-l2-context-records.md) · [ADR-037](../../decisions/033-039/ADR-037-site-pack-topology.md) · [ADR-033](../../decisions/033-039/ADR-033-l4-decision-runtime.md) · [`L1-L2-DATA-PLANE.md`](../L1-L2-DATA-PLANE.md)

These are documentation and schema intents. Implementation follows in the layer repos under separate plans.

---

## 1. L1 → L2: topology records

**New record kinds** (site-pack topology section published as typed context records):

| Kind | Payload (conceptual) |
| --- | --- |
| `topology.area` | area id, parent plant, lines |
| `topology.flow_edge` | from asset/area, to asset/area, direction, buffer size, lag |
| `topology.shared_resource` | resource id, type (feeder, transformer, compressor header, chiller loop, furnace, fixture, crew pool, …), capacity where known |
| `topology.meter_node` | meter id, parent, children |
| `topology.asset_draw` | asset id → shared resource id, draw role |

**Rules:**

- Versioned with the site pack; owner-reviewed before publish.
- L4 PSM builder consumes via **builder reads** (bulk/list). Not agent tools.
- Suggestions from models do **not** publish here until owner confirmation ([`02-plant-structure.md`](02-plant-structure.md)).

---

## 2. L2 → L4: builder reads vs agent tools

| Path | Purpose | Write? |
| --- | --- | --- |
| Builder reads | PSM construction, incremental watermarks, list topology / state / episodes | No |
| Agent tool catalog | Allowlisted zoom reads during a DecisionCase | No |

Both are read-only. Contract docs must name the two catalogs so an agent cannot call a builder bulk export as a “tool.”

---

## 3. L3 → L4: Finding floor (unchanged intent, sharpened)

L4 intake requires (existing research `15` floor, made explicit for implementers):

- `detector_id`, `detector_version`
- condition / asset binding
- evidence references
- verification plan (or explicit absence → shadow / withhold per family rules)
- calculator references for any priced effect

**Uncertified** detector versions → shadow only.

**Discovery support from L3** (new consumption, not new L3 product claim):

- condition test API for hypothesis grounding
- verification-plan builder from signals already in L2
- simulator methods with **intended-use envelope**
- system methods (bottleneck, blocked/starved, utility balance) where certified

Detail: [`15-l3-l4-interface.md`](15-l3-l4-interface.md).

---

## 4. L4 → L5: card proposal

Emit / supersede payload remains one card proposal. Fields:

| Field | Purpose |
| --- | --- |
| `origin` | `l3_finding` \| `l4_pattern` \| `l4_hypothesis` — **not** `exploration` |
| `exploration` | boolean; default false. Orthogonal to `origin` |
| `condition_key` | Shared key function |
| `footprint` | Action footprint for conflict / verification |
| `lockfile_id` | Replay pin |
| `decision_trace_id` | Link to full trace in L4 store |
| `operation` | `emit` \| `supersede` |
| `supersedes_proposal_id` | Required when `operation=supersede` — prior L4 proposal id |
| `supersedes_proposal_version` | Prior proposal version |
| `pattern_ref` | When `origin=l4_pattern` |
| `hypothesis_type_id` | When `origin=l4_hypothesis` |
| `finding_refs` | When `origin=l3_finding` |

L5 does not re-judge kernel criteria. It owns live card lifecycle, notification, and verification execution. On `operation=supersede`, L5 marks the prior open proposal **superseded** (not a new closure state) only if that proposal is not yet owner-accepted; otherwise L5 rejects the supersede and L4 must emit a separate card or conflict note.

**Hold** never appears on this interface — holds stay in the L4 store.

---

## 5. L5 → L4: learning facts

Typed learning facts for Hindsight / case library (eligible vs ineligible close, outcome null rules): see [`06-memory.md`](06-memory.md). Ineligible closes must not inflate proof counts.

---

## 6. L6 Ask

Ask is a **view** over L4 (and L5 card state). No second memory judge. Dialogue banks are hard-walled ([`14-ask.md`](14-ask.md)). No new write contract.

---

## 7. Soft-gate / opportunity ledger (L4-internal)

No cross-layer contract required for the ledger itself. Soft-gate threshold changes stay inside L4 registries. Exploration cards that emit use the L4→L5 fields above with `exploration=true`.

---

## 8. Disagreement policy amendment

Research notes `14` / `15` described low confidence falling back to a generative agent. **Amended:** seams touching action, owner, constraint, verification, or terminal **withhold** on dual-family disagreement. Routing seams use the registry default. Documented in [`11-models-and-seams.md`](11-models-and-seams.md) and ADR-036.

---

## Implementation order (suggested)

1. Topology record kinds + site-pack section (L1/L2)
2. Builder-read catalog (L2)
3. L4 store + PSM builder (L4)
4. Finding intake + kernel (L4)
5. L5 consume new proposal fields
6. Discovery scanners + patterns
7. Opportunity ledger + soft-gate calibration

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Topology kinds + builder reads + Finding proposal fields + `supersede` marker | Full discovery method catalog as L3 certifies |
| Domain registry ids on the wire | Additional domains without schema rewrite |
| Soft-gate backlog is L4/L6 ops surface | Exploration volume growth under owner caps |
