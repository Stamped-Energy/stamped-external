# IMPLEMENTATION PLAN — Beyond-energy action catalog

**Profile:** nawab lite  
**Pack:** `docs/research/plant-efficiency-exploration-2026-09/`  
**Branch:** `cursor/beyond-energy-action-catalog`  
**Commit budget:** 10 (hard)  
**Status:** exploration — not a product lock

## §0 Metadata

| Field | Value |
|-------|-------|
| Mode | feature (docs / exploration) |
| Delivery | This file + PROGRESS_ACTION_CATALOG.md + Cursor plan |
| Git | `git add -f` for `/docs/*` (ignored); no push unless asked |

## §1 Objective

Exploratory catalog of efficiency-driving operational decisions/actions unlocked if Stamped can ingest software-level plant data broadly — beyond today’s energy prescriptions, not limited to modes 1–13 — after (1) inventorying other Stamped research and (2) additive peer research.

## Research Wave

| Phase | Commit | Deliverable |
|-------|--------|-------------|
| A Prior landscape | 2 | `08a-prior-research-landscape.md` |
| B Additive peers | 6 | Peer digests in `08` + `SOURCES.md` |
| C Crosswalk | 7 | Crosswalk section in `08` |

## §9 Commit matrix

| # | Message | Paths |
|---|---------|-------|
| 1 | docs: scaffold beyond-energy action catalog plan | IMPLEMENTATION_PLAN_ACTION_CATALOG.md, PROGRESS_ACTION_CATALOG.md |
| 2 | docs: inventory prior Stamped research for efficiency actions | 08a-prior-research-landscape.md |
| 3 | docs: baseline energy prescriptions for action contrast | 08-beyond-energy-action-catalog.md (framing + baseline) |
| 4 | docs: map software plant data to efficiency unlocks | append to 08 |
| 5 | docs: catalog beyond-energy efficiency actions | append to 08 |
| 6 | docs: additive peer research digests for efficiency actions | append to 08; SOURCES.md |
| 7 | docs: crosswalk prior research to unlocked actions | append to 08 |
| 8 | docs: propose new efficiency action families | append to 08 |
| 9 | docs: link action catalog from pack reader guides | START-HERE.md, README.md |
| 10 | docs: close beyond-energy action catalog exploration | PROGRESS_ACTION_CATALOG.md; PROGRESS.md note |

## §16 Exit (P0)

- [ ] 08a inventories other Stamped research
- [ ] 08 has framing, baseline, data map, action catalog
- [ ] Catalog not limited to modes 1–13
- [ ] 10 commits with `git add -f`; no push

## §18 Protocol

Sequential commits 1→10; one row one commit; Research Wave on 2 / 6 / 7; no batching; no push.
