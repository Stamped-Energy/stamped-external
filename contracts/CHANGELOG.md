# Changelog — stamped-l1-contracts

## [Unreleased]

### Added

- Contracts **0.15.0** (ADR-033 / ADR-038 / ADR-040): L4 decision runtime wire schemas — `decision-case`, `decision-trace`, `card-proposal`, `opportunity-ledger-row` each **1.0.0**. `card-proposal` carries doc-18 L4→L5 fields (`condition_key`, `supersedes`, `emit_idempotency_key`, `origin`, `primary_domain_id`, `owner_role`, `footprint`, `evidence_refs`, `calculator_refs`, `verification_plan`, `lockfile_hash`, `build_sha`). Kernel pin `l4-kernel.v1` on case and trace.
- `finding.json` **1.2.0** (const unchanged, dual-read): optional intake-floor fields `detector_id`, `detector_version`, `decision_family_id`, `condition_key`, `condition_key_material`, `constraint_refs_considered`
- Golden valid/invalid fixtures under `fixtures/intelligence/` for the new schemas
- Contracts **0.16.0**: Finding **2.0.0** (`finding-2.0.0.json`) with detector identity, condition key, family, tiered facts, calculator-referenced effects, and a verification plan. Finding **1.2.0** stays the dual-read schema.
- Registries pack `registries/` (domains, families, evidence tiers, condition-key recipe, lockfile) shared by L3 and L4.
- L3 methods OpenAPI: `contracts/openapi/l3-methods.openapi.json`

### Deprecated

- `prescription.json` **1.0.0** — dual-read retained; new L4 emits use `card-proposal` 1.0.0
- `l4-compile-trace.json` **1.0.0/1.1.0** — dual-read retained; new L4 traces use `decision-trace` 1.0.0
- Contracts **0.14.0** (ADR-031): L1 context records — `asset_state`, `process_batch`, `flow_position`, `maintenance_context`, `quality_status`, `material_availability`, `operating_rate`, `plant_constraint`; pack schema; `tools/l2-query-tools.json`
- Envelope `record_type` enum extended additively (shape and `schema_version` 1.0.0 unchanged)
- MQTT `orders` and `context` topics with wrapper and dedupe strings
- Contracts **0.13.0** (ADR-029): `action-intent`, `machine-capability` — human-guided OT command path (Wave C opt-in)
- Contracts **0.12.0** (ADR-028): `plant-knowledge-graph`, `plant-live-index`, `shift-roster`, `l4-compile-trace`
- `prescription.provenance`: optional `compile_trace_id`, `otel_trace_id`; `lane` enum adds `quality`

### Changed

- `shift-roster`: optional `observed_at` and `lineage` for L2 ingest
- `plant-live-index` **1.0.0**: required `freshness` watermarks; `orders[]` with `window_end_utc` / `uses_asset_ids` (Job 447–class Path D); optional `standby_evidence`; `open_order_ids` kept as deprecated alias
- `l4-compile-trace` **1.0.0**: required `snapshots`, `max_generation_calls`, `terminal` (`emit`|`withhold`|`abstain`); optional `bind`, `template_id`; delta `evidence_refs`
- `plant-knowledge-graph`: document `REMEDY_IN` as AssetClass→Playbook; waste_category / template_id on Playbook node properties

## [0.11.2] — 2026-08-05

- `plant-admin-settings.json` **1.1.0**: add practicality gate profile — `practicality_gate_mode` (`strict`|`balanced`|`lenient`), `require_named_owner`, `require_evidence_refs`, `require_mv_plan`, `min_impact_confidence`, `allow_illustrative_impact`, `auto_withhold_on_gate_fail` (AD-5 / AD-7 L5 Internal Console)
- Expand [stamped-l5-internal-console-handoff.md](../handoff/holistic/improve/stamped-l5-internal-console-handoff.md) — all-Rx inbox, gate diagnostics, force-send, plant gate profile

## 0.11.1 — 2026-08-01 (as-built)

- Add [stamped-l5-internal-console-handoff.md](../../handoff/holistic/improve/stamped-l5-internal-console-handoff.md) — internal API + console surface
- Forge design: Improve = internal weekly human-gated step (L5 console, not customer nav)

## 0.11.0 — 2026-08-01

- `improvement-signal.json` **1.1.0**: add `time_to_outcome`, `ledger_calibration`, `escalation_event`, `workflow_lifecycle`, `admin_manual_input`; extend payload
- Add `improve-cycle.json`, `calibration-patch.json`, `model-run.json` (Improve admin + ML shadow/promote)
- Add `plant-admin-settings.json` — `stamped_rx_gate_enabled`, weekly cadence
- `workflow-event.json`: add `pending_stamped_review`, `withheld` statuses; `stamped_review_approved`, `stamped_review_withheld` event types
- ADR-025 revised (weekly, A+B, human-gated, Track C removed); ADR-027 plant calibration + champion promote
- Improve pipeline spec: weekly ImproveCycle, shadow/promote, plant notes manual

## 0.10.1 — 2026-07-31

- Extend `workflow-event.json` `event_type`: `negotiation_started`, `revision_proposed`, `revised`, `negotiation_rejected` (ADR-024 negotiation lifecycle)
- Extend `workflow-event.json` `reason_code`: `order_deadline`, `ops_challenge`, `not_real`, `other`

## 0.10.0 — 2026-07-30

- Add `production-order.json` v1.0.0 — ERP/MES/MES-lite order context (ADR-024)
- `production-record.json` **1.1.0**: optional `department_id`, `order_id`, `due_at_utc`, `priority`, `routing_step`; source adds `csv`
- Add `prescription-revision.json` v1.0.0 — negotiated Rx supersession (ADR-024)
- `prescription.json`: optional `decision_class`, `tradeoff`, `supersedes_rx_id` (BACKWARD additive)
- `finding.json`: optional `decision_class` (BACKWARD additive; schema_version unchanged)
- Add `improvement-signal.json` v1.0.0 + `plant-preference-profile.json` v1.0.0 (ADR-025 Improve loop)
- Add `plant-department-graph.json` v1.0.0 — department/line topology for TradeoffEngine
- Extend `stamped-record-envelope.json` `record_type`: `production_order`, `improvement_signal`, `prescription_revision`
- Golden fixtures for all new schemas; bump `production_record.valid.json` to 1.1.0

## 0.9.1 — 2026-07-28

- Consumer `stamped-l3-eval` RunArtifact schema: optional `plant_intelligence_score` (Lab dual-pillar export)

## 0.9.0 — 2026-07-28

- `finding.json` **1.2.0**: required `value_domain` (`energy_efficiency` | `equipment_health`); add categories `trip_cascade_risk`, `abnormal_duty`, `feeder_unexplained_draw`, `air_leak_survey` (two-pillar L3)
- Add `plant-intelligence-score.json` v1.0.0 + golden fixture — dual-pillar plant Intelligence Score (not RUL / not DISCOM substitute)
- Fixture `finding.valid.json` bumped to 1.2.0 with `value_domain`
- Aligns with `technical/STAMPED_ARCHITECTURE.md`

## 0.8.0 — 2026-07-21

- `finding.json` **1.1.0**: additive `ops_clearance` + optional `alarm_hint` for L5 ops-first verification / EMS alarms
- `ledger-entry.json`: add `ops_confirmed` to `verification_status` (`verified` reserved for deferred bill path)
- `workflow-event.json`: add `alarm_raised|acked|cleared`, `ops_verified`, `ops_regressed`; actor `clearance_engine`
- Fixtures: `finding` with clearance, `workflow_event_ops_verified`, ledger `ops_confirmed`
- ADR-020 revised ops-first

## 0.7.0 — 2026-07-20

- Add `workflow-event.json` v1.0.0 — L5 → L6 workflow/notification stream (ADR-019)
- Extend `stamped-record-envelope.json` `record_type` with `workflow_event` (BACKWARD additive)
- `ledger-entry.json`: add optional `supersedes_entry_id`, `emission_factor_ref`; clarify `verification_status` (pending|verified|disputed|modeled) — no `superseded` status (corrections are new rows)
- `prescription.json`: document that `status` is intake-only; L5 verified/disputed live on WorkflowState
- Golden fixture `workflow_event.valid.json`
- Aligns with L5 architecture overhaul (ADR-019/020/021)

## 0.6.1 — 2026-07-14

- Docs: reconcile `Finding` examples in L3/L4/`02-technical-architecture` §5.2 to match `finding.json` field names (`baseline_value`/`actual_value`, required `plant_id`/`org_id`, top-level `engine` + `rule_or_model_ref`). Schema unchanged.

## 0.6.0 — 2026-07-13

- Add L3–L5 intelligence schemas: `finding.json`, `prescription.json`, `ledger-entry.json`, `capex-proposal.json`
- Extend `stamped-record-envelope.json` record_type enum: finding, prescription, ledger_entry, capex_proposal (BACKWARD additive)
- Add golden fixtures for Finding, Prescription, LedgerEntry (incl. opportunity_cost)
- ADR-012/013/014 accepted

## 0.5.0 — 2026-07-11

- Extend `event.json` enum: `bill_validated`, `bill_rejected`, `bill_published`, `document_received`, `ems_published`, `shift_calendar_uploaded`, `tariff_order_received` (BACKWARD additive)

## 0.4.0 — 2026-07-10

- Add `bill-line.json` for MQTT `bills` topic ingest
- Add required `seq` to `event.json` (layer-interfaces §2.2 dedupe)
- Require `batch_id` and `line_id` on `production-record.json` for dedupe stability

## 0.3.0 — 2026-07-10

- Add `stamped-record-envelope.json` — L1→L2 boundary wrapper (ADR-008, layer-interfaces.md)
- Document eight-repo topology: connectors-cloud (L1 cloud only); stamped-l2…l6 separate repos

## 0.2.0 — 2026-07-09

- Add `measurements/backfill` MQTT topic for late data beyond edge buffer horizon
- Add `tag_remapped?` event type for drift watch (L1 §4.5)
- Site config schema extended: `opcua`, `historian`, `rest_poller`, `dlms` connector blocks

## 0.1.0 — 2026-07-09

- Initial P0 schemas: measurement, event, production-record, site-config, mapping-config, tag-inventory, modbus-profile
- MQTT topic layout v1 in TOPICS.md (add `cmd/config` wake-up topic)
