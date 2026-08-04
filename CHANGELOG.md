# stamped-external changelog

All notable changes to the shared platform pack. Consumer repos pin via git submodule tags.

Format: [Keep a Changelog](https://keepachangelog.com/). Platform tags: `vYYYY.MM.DD` (aligned with [VERSION](VERSION)).

## [Unreleased]

### Added

- Root [`index.html`](index.html) demo hub for GitHub Pages (industry decks, prescriptions, clients, tech)
- [`demo-decks/prescriptions-examples.html`](demo-decks/prescriptions-examples.html) — prescription examples walkthrough
- [`demo-decks/clients/technical-explainer.html`](demo-decks/clients/technical-explainer.html) — Stamped Intelligence technical explainer (11 slides)
- [`demo-decks/clients/itc-nadiad-technical.html`](demo-decks/clients/itc-nadiad-technical.html) — ITC Nadiad account technical brief
- [`demo-decks/clients/itc-nadiad-technical/`](demo-decks/clients/itc-nadiad-technical/) — GitHub Pages deploy root for ITC brief (hero `nadiad-plant.jpg`)
- [`.github/workflows/pages.yml`](.github/workflows/pages.yml) — deploy demo site from `main`

## [2026.07.30] - 2026-07-30

### Added

- [`technical/product/Stamped_Client_Positioning_and_Narrative_v1.md`](technical/product/Stamped_Client_Positioning_and_Narrative_v1.md) — canonical client narrative (four-step story, I4.0 positioning, WhatsApp templates)
- Floor-tied practical prescription illustrations + constraint table in [`demo-decks/prescriptions-examples.md`](demo-decks/prescriptions-examples.md)
- Agent reading order updated (`AGENTS.md`, consumer prompts, `STAMPED_ARCHITECTURE.md`)
- [`handoff/PATH_MAP.md`](handoff/PATH_MAP.md) — old → new path map for submodule consumers
- Contracts **0.10.0**: `production-order`, `prescription-revision`, `improvement-signal`, `plant-preference-profile`, `plant-department-graph`; ProductionRecord **1.1.0**; prescription `decision_class`/`tradeoff`; envelope record_types extended ([contracts/CHANGELOG.md](contracts/CHANGELOG.md))
- [ADR-024](decisions/024-026/ADR-024-holistic-plant-decisions.md) — holistic plant decisions (energy wedge + co-benefits + negotiation)
- [ADR-025](decisions/024-026/ADR-025-improve-loop-step-06.md) — Improve loop step 06
- [ADR-026](decisions/024-026/ADR-026-two-pillars-shared-context.md) — product framing lock (two pillars + shared context; OEE co-benefits; not MES)
- Holistic handoffs + consumer prompts under `handoff/holistic/` and `handoff/agents/`

### Changed

- **Breaking — repo layout:** topic subfolders (handoff, scripts, decisions ADR buckets, technical layers, nested contracts). Meta docs → `project/`. See [PATH_MAP](handoff/PATH_MAP.md).
- CI entrypoint: `scripts/contract-check.sh` → [`scripts/contracts/contract-check.sh`](scripts/contracts/contract-check.sh) (recursive schema/fixture discovery)
- Legacy `technical/00|01|02|03-*.md` are thin pointers under `technical/pointers/` → SSOT
- Framing: two pillars + shared context; proof = **verified with evidence**; effectiveness co-benefits on management Rx

### Added (prior unreleased carry-forward)

- Contracts **0.9.0**: Finding **1.2.0** (`value_domain`, equipment-health categories); `plant-intelligence-score.json` v1.0.0
- Two-pillar mapping onto L0–L6 (now in SSOT) — linked from [technical/README.md](technical/README.md)

## [2026.07.12] - 2026-07-12

### Added

- Platform pack structure for `stamped-platform` repository distribution
- [ADR-010](decisions/006-010/ADR-010-deployment-profiles-and-portability.md) — three deployment modes (`local`, `local-dashboard`, `cloud`)
- [ADR-011](decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md) — submodule single source of truth
- Four portability playbooks (edge, cloud, bill, stamped-l2)
- [deployment-profiles.md](handoff/deployment/deployment-profiles.md) cross-repo mode matrix
- [SUBMODULE.md](SUBMODULE.md) migration guide
- [scripts/contracts/contract-check.sh](scripts/contracts/contract-check.sh) shared CI helper
- Research brief mirrored in consumer repos at `docs/research/` (not in platform pack)

### Changed

- ADR-002, ADR-007, ADR-009 — ADR-010 addenda for deployment modes
- `stamped-l2-ecosystem-integration.md` — three-mode section; `connectors-ingest` reclassified for `local` mode
- `02-technical-architecture.md` §16.4 — deployment mode table
- Contract authority moved to platform repo per ADR-011 (supersedes connectors-edge fork)

### Deprecated

- Manual copy of `external/` folder into new repos — use submodule (ADR-011)

## [Unreleased]

### Added

- Extensive README — architecture (L0–L6), tech stack, ADR catalog, contracts reference, deployment modes, Cursor config
- **L5 architecture overhaul** — authoritative [L5 SSOT](technical/layers/l4-l6/L5-closure-and-verification.md); [ADR-019](decisions/016-020/ADR-019-l5-runtime-and-consistency.md) / [ADR-020](decisions/020-023/ADR-020-l5-mv-claim-governance.md) / [ADR-021](decisions/020-023/ADR-021-l5-notification-and-evidence.md); handoffs [stamped-l5-architecture-handoff.md](handoff/l5/stamped-l5-architecture-handoff.md) + [build plan](handoff/l5/stamped-l5-build-plan.md)
- Contracts **0.7.0** — `workflow-event.json`, envelope `workflow_event`, ledger `supersedes_entry_id` / `emission_factor_ref`
- **Ops-first L5 + L3 enablement** — Finding **1.1.0** `ops_clearance` / `alarm_hint`; ledger `ops_confirmed`; workflow `alarm_*` / `ops_verified` / `ops_regressed`; [L3 ops-clearance consumer prompt](handoff/agents/prompts/stamped-l3-ops-clearance-consumer-prompt.md)
- Contracts **0.8.0** — see [contracts/CHANGELOG.md](contracts/CHANGELOG.md)
- L5 consumer README snapshot — [consumers/readmes/closure-verification.md](consumers/readmes/closure-verification.md) (`Vinayak-RZ/closure-verification`)
- **L6 architecture + UI handoff** — [ADR-022](decisions/020-023/ADR-022-l6-bff-runtime-boundary.md) / [ADR-023](decisions/020-023/ADR-023-l6-ems-and-analyst-context.md); [architecture handoff](handoff/l6/stamped-l6-architecture-handoff.md) · [UI charter](handoff/l6/stamped-l6-ui-ux-charter.md) · [build plan](handoff/l6/stamped-l6-build-plan.md) · [agent onboarding](handoff/agents/onboarding/stamped-l6-agent-onboarding.md); typed seed [consumers/stamped-l6](consumers/stamped-l6/)

### Changed

- L2 `ledger.mv_ledger` DDL sketch aligned to contract `verification_status` (`modeled`, not mutable `superseded`); later **`ops_confirmed`**
- Production-engineering Temporal default superseded by ADR-019 for L5
- Arch §5.2 / §5.4 — Finding 1.1.0 + ops_confirmed / alarm events
- ADR-020 reframed: ops-cleared verification; bill path deferred
- L5 SSOT / handoffs: EMS alarm router; calculated savings; vertical catalog map
- L6 SSOT reconciled ops-first + EMS console + dual-mode analyst (P0 Mode A / P1 Mode B); English through P2

### Planned

- Submodule migration in connectors-edge, connectors-cloud, connectors-bill, universal-repositary
- `stamped-l1-contracts` PyPI/npm publish (optional P1)
- Create `stamped-l5` consumer repo per build plan
- Create `stamped-l6` consumer repo per [handoff/l6/stamped-l6-build-plan.md](handoff/l6/stamped-l6-build-plan.md)
- Bill reconcile / IPMVP Option C as optional add-on (not P0 gate)
