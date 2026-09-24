# Propagation into the layer repos

**Date:** 2026-09-24  
**Amended:** 2026-09-25 — insert after contracts: implement from [`../../technical/l4/`](../../technical/l4/) (docs already written). Shared registries target `stamped-external/registries/` (schemas + seed; not created in this docs pass). L1/L2 topology records before PSM builder. L4 operational store is allowed for derived data; L2 remains plant SoR.  
**Status:** Order of work after these notes. Not a task list inside those repos yet.
**Authority:** [`09-stamped-founder-vision.md`](09-stamped-founder-vision.md) wins. Design: [`14-coarse-architecture.md`](14-coarse-architecture.md) + [`../../technical/l4/`](../../technical/l4/). Fields: [`15-contract-deltas.md`](15-contract-deltas.md) + [`../../technical/l4/18-contract-deltas.md`](../../technical/l4/18-contract-deltas.md).

Do this in order. Do not start a later step by editing a layer repo while the contract it depends on is still unnamed.

0. **L4 architecture docs (done).** [`../../technical/l4/`](../../technical/l4/) · ADRs 033–039 · research [`19`](19-l4-agent-peer-systems.md).
1. **Contracts, in this submodule.** Card proposal schema beside Prescription 1.0.0 (include `origin`, `supersede`, footprint, lockfile). Finding fields. Closure event + `superseded` marker. Autonomy policy. Owner-role configuration. Shared registry pack under `stamped-external/registries/`.
2. **L1/L2 topology.** Site-pack topology records published L1→L2 ([ADR-037](../../decisions/033-039/ADR-037-site-pack-topology.md)).
3. **L2.** Constraint registry, shift roster, condition key, builder-read catalog. Still the plant SoR database.
4. **L3.** Verification plan on the finding. Merge on condition key. Primary domain from the family. Method tools L4 will call. Idle-load stays the first family.
5. **L4 implementation.** Runtime from `technical/l4/`: PSM, dual-family seams, discovery, portfolio, opportunity ledger, Hindsight + case library. Template / certified fast path remains. Hindsight hosting chosen here.
6. **L5.** Eight closure states, `superseded` marker, verification job, short learning fact back to L4, autonomy policy default off, certification before enablement.
7. **L6.** One card with domain sections, constraint form, autonomy setting, Ask as a view over L4; owner opportunity backlog for soft-gate blocks.
8. **Pilot 1.** Idle-load, ops head, IPMVP Option B on the named auxiliary circuit. See [`16-pilot-and-hard-stops.md`](16-pilot-and-hard-stops.md).
9. **A second family** only after that pilot's closures exist. Alarm dwell, then one handoff or exception.

The atlas in the L1–L6 map (`docs/atlas/STACK.md`) is not updated in this pass. Update it when a layer repo actually changes.

Fine-grained Hindsight deployment, screen layout, and detector thresholds stay in the layer repos. [`17-do-not-build.md`](17-do-not-build.md) still applies there.
