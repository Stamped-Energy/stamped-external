# MQTT topic layout (v1)

Draft — aligns with [ADR-001](../decisions/001-005/ADR-001-l1-repo-split-and-boundaries.md), [ADR-002](../decisions/001-005/ADR-002-build-all-aws-networking.md), and [ADR-031](../decisions/028-032/ADR-031-l1-l2-context-records.md).

**P0 broker:** self-hosted Mosquitto on AWS EC2 (`ap-south-1`), TLS via ACM or Let's Encrypt on instance.

## Conventions

- Prefix: `stamped/v1/`
- Tenant: `{org_id}/{plant_id}/`
- Payload: JSON, UTF-8, validated against `external/contracts/schemas/*.json`
- QoS: **1** for measurements, events, production, orders, bills, context
- Retain: **false** for high-volume streams; **true** only for last-will / health if needed

## Topics

| Topic | Publisher | Payload schema | Notes |
| --- | --- | --- | --- |
| `stamped/v1/{org_id}/{plant_id}/measurements` | edge-agent | `measurement.json` | High volume; edge batches if needed |
| `stamped/v1/{org_id}/{plant_id}/measurements/backfill` | edge-agent | `measurement.json` | Late data beyond buffer horizon; same schema |
| `stamped/v1/{org_id}/{plant_id}/events` | edge-agent, context-agent, bill-ingest | `event.json` | Includes connector health, gaps, `bill_received`, `unmapped_tag` |
| `stamped/v1/{org_id}/{plant_id}/production` | context-agent | `production-record.json` | Lower volume |
| `stamped/v1/{org_id}/{plant_id}/orders` | context-agent | `production-order.json` | Cloud already routes this suffix |
| `stamped/v1/{org_id}/{plant_id}/bills` | bill-ingest | `bill-line.json` (array or NDJSON) | One bill → many BillLine records |
| `stamped/v1/{org_id}/{plant_id}/context` | edge-agent, context-agent, bill-ingest | context wrapper | See below |
| `stamped/v1/{org_id}/{plant_id}/health` | edge-agent, context-agent | `event.json` | Birth/death/heartbeat; 60s |
| `stamped/v1/{org_id}/{plant_id}/cmd/config` | cloud (tag-mapping-api) | `{"manifest_version":"N"}` | Wake-up only; edge pulls signed manifest via HTTPS |

### Context wrapper

Topic `…/context` carries a small wrapper (not a bare record), because every payload schema sets `additionalProperties: false` and cannot hold `record_type`:

```json
{"record_type": "process_batch", "record": { /* schema for that type */ }}
```

`record_type` is one of: `asset_state`, `process_batch`, `flow_position`, `maintenance_context`, `quality_status`, `material_availability`, `shift_roster`, `operating_rate`. Cloud validates `record` against that schema and wraps `StampedRecordEnvelope`. `POST /v1/context` takes the same wrapper for backfill.

> **Note:** `v1/{plant_id}/live/` from production-engineering doc is **deprecated**; use `stamped/v1/...` prefix.

## Idempotency / dedupe

Consumers compute `dedupe_key = sha256:…` then store once. Formulas (pipe-separated fields, UTF-8, then SHA-256 hex):

| record_type | Dedupe string |
| --- | --- |
| `measurement` | `org\|plant\|source_tag\|ts_utc\|granularity\|metric.type` (existing) |
| `event` | existing event formula unchanged |
| `bill_line` | existing bill_line formula unchanged |
| `production_record` | existing production_record formula unchanged |
| `production_order` | existing production_order formula unchanged |
| `asset_state` | `org\|plant\|asset_id\|ts_utc\|state` |
| `process_batch` | `org\|plant\|process_batch\|batch_id\|observed_at` |
| `flow_position` | `org\|plant\|flow_position\|position_id\|observed_at` |
| `maintenance_context` | `org\|plant\|maintenance_context\|work_id\|observed_at` |
| `quality_status` | `org\|plant\|quality_status\|subject_type\|subject_id\|observed_at` |
| `material_availability` | `org\|plant\|material_availability\|sku\|location_id\|observed_at` |
| `shift_roster` | `org\|plant\|shift_roster\|shift_id\|observed_at` |
| `operating_rate` | `org\|plant\|operating_rate\|rate_id\|observed_at` |

Context types use `observed_at` (source modified time when known, else publisher sighting). Retries of the same observation are duplicates. A later change is a new row even if values return to an earlier state (A→B→A stores three rows).

## Security

- TLS 1.2+ mandatory
- Per-plant client certificates or username/password per broker ACL
- ACL: plant client may **publish only** to its `{org_id}/{plant_id}/*` topics
