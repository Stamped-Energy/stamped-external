# L4 glossary

Short definitions for the L4 architecture set. Normative behaviour lives in [`00-kernel.md`](00-kernel.md) and the numbered docs.

| Term | Meaning |
| --- | --- |
| **Abstain** | Terminal: insufficient case to decide; always traced |
| **Action footprint** | Assets, shared resources, crew/role, material, time window (start, end, lag) claimed by a candidate or open card |
| **As-known-at** | PSM / ledger snapshot using recorded time so late corrections do not rewrite what L4 knew |
| **Builder read** | Bulk/list read for the PSM builder; not an agent tool; cannot write |
| **Case library** | Episodic store of traces joined with L5 outcomes; authority when it disagrees with Hindsight |
| **Condition key** | Stable id for “this plant condition”; one open card per key |
| **DecisionCase** | One run unit: intake + snapshot + obligations + candidates + terminal |
| **DecisionTrace** | Always-on record: observed, context, action, policy, approval, outcome (and seam decisions) |
| **Discovery** | L4-originated candidate (scanner / pattern / hypothesis), not an L3 Finding |
| **Emit** | Terminal: send one card proposal to L5 |
| **Evidence ledger** | Typed rows (measured / advisory / model partitions) frozen into the trace |
| **Evidence tier** | Measured / Confirmed / Modeled / Unknown — assigned by code from source type |
| **Exploration card** | Opt-in card marked `exploration=true` to test soft-gate blocks |
| **Finding** | L3 detector output admitted to L4 |
| **Gate id** | Stable id of the hard or soft gate that blocked a candidate |
| **Grounded-hypothesis lane** | Owner opt-in path for LLM hypotheses that still pass L3 grounding + dual-family + kernel |
| **Hard gate** | Never tunable, never backlog, never explored |
| **Hold** | L4-internal portfolio outcome; staff-visible; not sent to L5 |
| **Hindsight** | Memory product: plant bank + dialogue banks; advisory except where case library overrides outcomes |
| **Jev seam** | Decision slot with LLM structured output today and a logged record so a classifier (Jev) can later beat it |
| **Kernel** | Frozen normative rules in `00-kernel.md` |
| **Lockfile** | Release pin of registry versions, kernel version, model pins |
| **Opportunity ledger** | Store of every blocked candidate with gate id and later outcome if known |
| **Portfolio** | Dedupe, conflict, attention, supersede among candidates and open cards |
| **Proof floor** | Minimum evidence/structure required before emit (asset bound, verification path, L3 condition test for discoveries) |
| **PSM** | Plant Situation Model — derived per-plant cache in the L4 store |
| **Release lockfile** | See lockfile |
| **Shadow** | Traced, never sent to L5 (uncertified detectors, ungrounded hypotheses, demoted patterns) |
| **Site pack** | Versioned, owner-reviewed plant configuration including topology |
| **Soft gate** | Threshold in registry; calibrated from opportunity ledger + exploration |
| **Supersede** | Terminal: replace prior L4 proposal before owner acceptance |
| **Withhold** | Terminal: do not send; reason recorded |
| **Working ledger** | Per-run ledger frozen into the trace, then discarded |
| **Zoom read** | Allowlisted typed read requested by a model; code executes and appends rows |
| **OE knowledge corpus** | Versioned literature + sparse method ontology; retrieved as advisory rows only — see [`23-oe-knowledge-corpus.md`](23-oe-knowledge-corpus.md) |
| **Shift sweep** | Once-per-shift whole-plant discovery pass — [`08-discovery.md`](08-discovery.md) |
| **Work queue** | Durable per-plant scheduler for Findings, sweeps, Ask — [`25-work-queue-and-concurrency.md`](25-work-queue-and-concurrency.md) |
| **Kill switch** | Control-plane stop of new leases + CardSink — [`28-commissioning-and-controls.md`](28-commissioning-and-controls.md) |
| **Safe-start** | Checklist before `emit_enabled` — [`28-commissioning-and-controls.md`](28-commissioning-and-controls.md) |

---

## v1 slice vs later

Glossary terms are stable for `l4-kernel.v1`. New terms arrive with ADRs or registry packs; this file updates in the same commit as the doc that introduces them.
