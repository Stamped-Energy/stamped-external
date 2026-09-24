# Commissioning, safe-start, and plant controls

**Status:** Architecture (production hardness).  
**ADR:** [040](../../decisions/040-044/ADR-040-l4-production-hardness.md)  
**Siblings:** [`02-plant-structure.md`](02-plant-structure.md) · [`08-discovery.md`](08-discovery.md) · [`16-operations.md`](16-operations.md) · [`23-oe-knowledge-corpus.md`](23-oe-knowledge-corpus.md) · [`00-kernel.md`](00-kernel.md)

---

## Purpose

A correct DecisionCase design can still harm a plant if emit is enabled before topology, constraints, and methods are honest. This doc is the **maturity gate** and the **emergency controls** so production rollout is deliberate.

---

## Plant control plane (flags)

All flags are plant-scoped, audited, and lockfile-aware (control-plane changes are ops events, not silent).

| Flag | Meaning | Default for new plant |
| --- | --- | --- |
| `emit_enabled` | CardSink may deliver to L5 | **false** until safe-start passes |
| `shadow_only` | Run full path; never CardSink | true until first canary |
| `discovery_shift_sweep_enabled` | Shift sweep on | false until scanners commissioned |
| `hypothesis_lane_enabled` | Grounded-hypothesis lane | false (owner opt-in) |
| `exploration_enabled` | Soft-gate exploration cards | false (owner opt-in) |
| `kill_switch` | Force no new leases + no CardSink | false; on-call / owner may set |

When `kill_switch=true`: drain in-flight per [`26`](26-decision-case-lifecycle.md) cancel policy; no new queue leases; existing `terminalizing` may finish only if CardSink idempotent check shows not yet delivered — prefer fail closed on doubt.

---

## Safe-start checklist (must all be true before `emit_enabled=true`)

| # | Gate | Evidence |
| --- | --- | --- |
| 1 | Site-pack topology published for Pilot assets | L2 topology records + owner confirm ([`02`](02-plant-structure.md)) |
| 2 | Constraint rows for those assets reviewed | Named owner |
| 3 | L3 methods for Pilot family certified (calculator, verification builder; condition test if discovery on) | L3 promotion record |
| 4 | Detector or pattern commissioned (shadow precision acceptable) | Ops scorecard |
| 5 | PSM digest coverage manifest above plant minimum | Unknown rate under threshold |
| 6 | Lockfile pinned; shadow suite pass^k green | [`20-benchmark.md`](20-benchmark.md) |
| 7 | CardSink + L5 dual-read verified in staging | Contract check |
| 8 | On-call runbook + kill_switch drill once | Ops sign-off |
| 9 | Plant owner accepts emit | Explicit accept |

Until then: `shadow_only=true`. Staff see traces; Now queue does not get L4 cards from this plant.

---

## Commissioning per family / pattern

Reuse [`02-plant-structure.md`](02-plant-structure.md) minimum topology / signal tables. Add:

- Soft-gate thresholds seeded (not production-calibrated yet).  
- Attention budget set.  
- Owner role mapping present in L5.  
- OE corpus mission allowed for that scenario class (optional).

A family may stay shadow-only while another family is emit-enabled on the same plant.

---

## Emergency and incident controls

| Control | Who | Effect |
| --- | --- | --- |
| `kill_switch` | On-call or plant owner | Stop new work; block CardSink |
| Force `shadow_only` | On-call | Keep learning traces without floor cards |
| Freeze lockfile | Tech lead + plant notify | No pin changes during incident |
| Open ModelSlot breaker | Automatic ([`27`](27-ports-and-reliability.md)) | Degrade per port map |
| Disable hypothesis lane | Automatic or owner | Precision / volume trip |
| Pause exploration | Automatic on nuisance spike | Soft calibration pause |

All control changes write an audit event: who, when, reason, previous value.

---

## OE corpus ops (production)

| Concern | Rule |
| --- | --- |
| Ingest | Tier A public only until license clear; chunk with source_doc_id + version |
| Pin | Corpus version + embedding model in release lockfile |
| QA | Spot-check: no OT-write instructions; no naked savings % as Measured |
| Eval | Replay suite: OE on vs off must not increase unreferenced-₹ or hard-gate misses |
| Poison | Bad chunk → quarantine doc_id; never silent global delete without lineage |
| Plant SOPs (Tier C) | Owner approve; plant partition; not exported to other plants |

Detail: [`23-oe-knowledge-corpus.md`](23-oe-knowledge-corpus.md) · research `20`.

---

## Offline export privacy

Traces sent to offline council:

- Strip secrets, API keys, raw PII beyond role ids.  
- Tokenize asset display names if plant policy requires.  
- Export allow-list fields only (registry).  
- Retention separate from plant L4Store.  
- No re-import of council free text into plant bank without typed learning-fact path.

---

## Rejected alternatives

| Alternative | Why |
| --- | --- |
| Emit on day one of connector install | Unsafe |
| Kill switch that deletes open cases without trace | Audit hole |
| Auto-enable hypothesis when shift sweep is empty | Flood risk |

---

## What would change this

- Pilot proves safe-start too slow → parallelize checklist items; do not remove owner accept.  
- Need staged emit by area → area-scoped `emit_enabled` via registry.

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Plant-level flags + checklist above | Area-scoped emit |
| Manual kill switch in ops tooling | L6 owner control with confirm |
| OE Tier A + QA eval | Tier B/C |

---

## Change class

Flags and checklist items: **data / ops**. Removing owner accept from safe-start: **forbidden** without ADR.
