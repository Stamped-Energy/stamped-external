# Plant structure and commissioning

| Field | Value |
| --- | --- |
| **Status** | Architecture (docs) |
| **Normative kernel** | [`00-kernel.md`](00-kernel.md) |
| **ADRs** | [ADR-037](../../decisions/033-039/ADR-037-site-pack-topology.md) · [ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md) · [ADR-031](../../decisions/028-032/ADR-031-l1-l2-context-records.md) |
| **Siblings** | [`03-plant-situation-model.md`](03-plant-situation-model.md) · [`04-constraints.md`](04-constraints.md) · [`18-contract-deltas.md`](18-contract-deltas.md) |
| **Change class** | Data (topology rows, suggestions) · Plug-in (new builder-read shapes) · Structural only if publication path changes |

---

## Purpose

Cross-asset checks need more than a list of assets. They need directed flow, buffers, lag, shared utilities, and who draws from what. This doc states where that structure lives, how it reaches L4, what happens when it is missing, and what minimum evidence a family or pattern needs before it may run at a plant.

L4 never invents plant topology into live use. A named plant owner confirms structure into the site pack. Humans decide and execute; L4 recommends against structure that already exists.

---

## Decision 1 — Site-pack topology is the plant-structure SSOT

**Decision.** Plant structure lives in a **versioned topology section of the site pack**, not in an L4-only config and not as an inventable graph inside the Plant Situation Model (PSM).

**Content of the topology section (versioned together):**

| Element | What it carries |
| --- | --- |
| Areas / lines | Stable ids, display names, parent plant, optional process role |
| Flow edges | From-asset → to-asset (or area handoff); **direction**; **buffer size** where known; **lag** (transport or queue delay) |
| Shared resources | Kind + id + **capacity** where known: feeder, transformer, compressor header, chiller loop, furnace, fixture, crew pool (and later kinds via registry) |
| Meter hierarchy | Meter → parent meter / feeder / transformer; which measurements bind to which resource |
| Asset → resource draws | Which assets draw which shared resource; draw class (power, air, cooling, fixture slot, crew role) |

Numbers that are not measured or ops-locked at a site (for example a default buffer of “12 pieces” or lag of “8 minutes” in a worked example) are **illustrative** until the site pack carries the real values.

**Reason.** L3 detectors and L5 verification need the same flow and shared-resource facts L4 uses for footprints and constraint neighbourhoods. If L4 alone owns topology, those layers cannot see it, and the graph drifts from what the plant believes is true.

**Rejected.** L4-only topology config; auto-accepting model-proposed edges into live structure; requiring a full plant ontology before the first card.

**Would change this.** A layer other than the site pack becomes the shared, versioned, owner-reviewed artifact for structure — with the same publication path and owner gate. Until then, site pack stays.

---

## Decision 2 — Publish L1 → L2 as typed topology records; L4 uses builder reads

**Decision.** L1 publishes topology as **typed topology records** into L2 (contract shapes in [`18-contract-deltas.md`](18-contract-deltas.md)). L4 does not parse site-pack YAML at runtime for live decisions.

**Builder reads** (bulk / list APIs for the PSM builder) are separate from the **agent tool catalog** (ADR-031 allowlisted tools). Builder reads:

- feed the PSM builder and propagation code;
- may return area-wide or plant-wide topology slices;
- are **read-only**;
- are **not** exposed as model-callable tools.

Models never walk the graph. They request typed zoom reads that code executes (see [`03-plant-situation-model.md`](03-plant-situation-model.md)).

**Reason.** ADR-031 forbids model graph traverse. Bulk structure for a derived cache is a different job from a focused tool call during a decision run. Mixing them either starves the builder or hands models a traverse surface.

**Rejected.** Giving models a `graph/traverse` tool; having L4 read pack files directly as SoR; writing topology from L4 into L2.

**Would change this.** A measured need for a single read surface that still keeps models off the walk — with proof that bulk builder traffic does not become an agent tool.

---

## Decision 3 — Topology suggestions: propose → owner confirms → site pack

**Decision.** A model (or scanner) may propose a **missing link** or shared-resource draw. The proposal becomes a **topology suggestion** with:

- claimed edge or draw;
- **evidence** (ledger ids / L2 fact refs);
- **expiry**;
- target named plant owner.

It enters the site pack **only** when that owner confirms. Confirmation is a pack version bump, then republish L1 → L2.

**Rejected suggestions** are remembered (negative memory / suggestion ledger). They are **not re-proposed** without **new evidence** (new facts, new epoch, or materially stronger support).

**Reason.** Most plants have incomplete formal topology. Letting the model fill gaps silently produces a private fiction. Forcing every suggestion through a named owner keeps plant truth plant-owned.

**Rejected.** Auto-merge of high-confidence edges; re-proposing the same rejected link every shift.

**Would change this.** A plant opts into a narrow auto-accept class (for example meter→feeder from a certified connector) with owner-set policy — still not free invention of process flow.

---

## Decision 4 — Missing structure → `unknown`; unknown in a constraint neighbourhood → withhold

**Decision.** A cross-asset check that needs a flow edge, lag, buffer, or shared-resource link and cannot find it returns **`unknown`**, not a guessed satisfied.

If that unknown sits in the **constraint neighbourhood** of a candidate (the scopes the candidate’s footprint and applicable constraints touch), the kernel withholds (`reason` includes constraint / structure unknown). Modeled benefit does not override. See [`00-kernel.md`](00-kernel.md) and [`04-constraints.md`](04-constraints.md).

**Reason.** Pretending a feeder relationship exists so a card can emit is how plants lose trust. Honest unknown is better than a confident wrong neighbourhood.

**Rejected.** Defaulting missing edges to “no interaction”; LLM judgment that “they are probably independent.”

**Would change this.** Evidence that a specific check class is safe with a declared default, registered per family, still failing closed outside that class.

---

## Decision 5 — Commissioning: minimum evidence before a family or pattern activates

**Decision.** Each **decision family** and **discovery pattern** declares a commissioning checklist. Until the named plant owner marks the checklist satisfied for that plant, the family/pattern stays **shadow** or inactive for emit.

### Checklist dimensions

| Dimension | Minimum before activation |
| --- | --- |
| Topology | Required areas, flow edges, and asset bindings named by the family/pattern |
| Shared resources | Required resource kinds with capacity or explicit “capacity unknown → bound checks withhold” |
| Constraints | Required constraint kinds present (or explicit advisory-only mode if the family allows) |
| Verification signals | L2 signals named in the verification recipe must resolve for in-scope assets |

### Worked commissioning rows (illustrative families / patterns)

These rows are **illustrative** templates for the registries — not a claim that any named plant already meets them.

| Family / pattern (illustrative id) | Topology minimum | Shared-resource minimum | Constraint minimum | Verification-signal minimum |
| --- | --- | --- | --- | --- |
| `family.idle_auxiliary_load` | Asset in an area; meter or load binding for the asset | Feeder or panel draw for the asset (or explicit single-asset scope) | Availability / quality-hold if the family touches restart | `asset_state` + load measurement path used by the Finding verification plan |
| `family.demand_spike_response` | Meter hierarchy up to the billed or controlled level the card names | Feeder / transformer capacity where a bound applies | `bound` on feeder or contract window if claiming a demand limit | Interval demand / meter series L3 already uses for the Finding |
| `pattern.shared_furnace_overlap` | Flow or schedule-adjacent assets that share the furnace resource | Furnace (or fixture) resource with capacity | Mutual exclusion or cumulative capacity on that resource | Asset start/stop or batch start events for both assets |
| `pattern.compressor_header_contention` | Assets drawing the header | Compressor header + capacity or envelope method | Cumulative capacity or reserve margin | Header pressure / kW and asset draw signals |
| `pattern.handoff_wait_recurring` | Directed flow edge with lag between upstream and downstream | Buffer size if the pattern claims starvation vs block | Precedence / min separation if claiming sequence | Queue or `flow_position` / batch timestamps on both sides |
| `family.exception_after_stop` | Asset + area | Crew pool if recommending a call-out role | Do-not-disturb / quality / maintenance constraints that block restart | Stop event + post-stop `asset_state` |

Activation is **per plant**. Global certification of a pattern is not the same as plant commissioning.

**Reason.** A pattern that needs a shared furnace will invent conflicts if the furnace resource is missing. Commissioning makes the gap visible before the first live card.

**Rejected.** “Ship the family; fill topology later”; plant-wide ontology as a prerequisite for any card.

**Would change this.** Measured safe emit for a family with a reduced checklist, still with explicit unknown→withhold on the omitted dimensions.

---

## Why site pack (not L4-only)

Plant structure is **plant truth**. L3 uses it for detectors that span assets. L5 uses it for verification neighbourhoods and footprint display. Ask and offline improvement need the same ids. The site pack is already the per-plant, versioned, owner-reviewed artifact (ADR-031 packs). Owning structure only inside L4 would hide it from every other layer and turn suggestions into silent writes.

The PSM ([`03-plant-situation-model.md`](03-plant-situation-model.md)) **caches** published topology with provenance. It is not the system of record.

---

## Failure modes the plant sees

| Failure | What L4 does | What the plant sees |
| --- | --- | --- |
| Topology unpublished / stale pack version | Builder cannot refresh structure; runs that need it withhold or stay shadow | Fewer cards; staff see structure-unknown in traces / backlog where soft gates apply |
| Suggestion rejected | Remembered; no re-spam | Owner is not asked again without new evidence |
| Capacity unknown on a shared resource | Bound / cumulative checks return `unknown` → withhold when hard | No card that pretends the feeder limit is known |
| Family activated without commissioning | Blocked by release / plant override rules | Pattern stays shadow until owner completes checklist |

---

## Relation to constraints and the kernel

- Constraint rows reference topology scopes (asset, edge, shared resource, area). See [`04-constraints.md`](04-constraints.md).
- Hard vs soft **gates** are kernel concerns ([`00-kernel.md`](00-kernel.md), [ADR-038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md)). Missing structure that yields `unknown` on a **hard** constraint is a hard-gate withhold — not a soft threshold to tune.

---

## v1 slice vs later

| In v1 | Later |
| --- | --- |
| Topology section fields above; L1→L2 typed records; builder reads for PSM | Richer resource kinds via registry; optional narrow auto-accept classes |
| Suggestions with evidence, expiry, owner confirm, rejection memory | Connector-certified meter hierarchy auto-proposals under owner policy |
| Per-family / per-pattern commissioning checklists for Pilot 1 families | Full catalog coverage as families certify |
| Missing structure → unknown → withhold in neighbourhood | Declared safe defaults only where registered and proven |

---

## Open gaps

1. Exact topology record schemas and builder-read paths land in [`18-contract-deltas.md`](18-contract-deltas.md) (not fully specified here).
2. Seed commissioning checklists for every registry family/pattern are owned by the shared registry pack once that pack exists under `stamped-external/registries/`.
3. [`00-kernel.md`](00-kernel.md) may still be landing in the same docs set; this file links it as the normative gate surface and does not restate terminals.
)
