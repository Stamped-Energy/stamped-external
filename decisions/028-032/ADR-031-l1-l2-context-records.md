# ADR-031: L1–L2 context records data plane

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-25 |
| **Deciders** | Product + Engineering |
| **Supersedes** | none |
| **Related** | [ADR-001](../001-005/ADR-001-l1-repo-split-and-boundaries.md) · [ADR-008](../006-010/ADR-008-layer-repo-topology-and-interfaces.md) · [ADR-030](ADR-030-five-domain-decision-loop.md) · workspace `docs/plans/l1-l2-context-records/PRODUCT.md` |

---

## Context

Five decision domains need plant facts beyond meter floats: machine state, batches, queues, maintenance, quality holds, materials, shifts, rates, and constraints. Competitors push Kafka-raw streams or plant-wide semantics. Stamped keeps typed records at the edge, one TimescaleDB in L2, and allowlisted HTTP tools for L4.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Layout | Closed record catalog; `edge-agent` OT, `context-agent` IT, bill human uploads, cloud door + default-off poller, L2 store |
| 2 | Trust | `X-Service-Key` + `X-Org-Id` + RLS; tools never take `org_id`; secrets by reference; agents have no inbound HTTP; read-only |
| 3 | Data | One TimescaleDB; three shapes; dedupe on `observed_at`; latest by `observed_at`; lineage on new rows; migration `014` |
| 4 | Wire | Existing suffixes unchanged; new `context` wrapper `{record_type, record}` |
| 5 | Packs | YAML packs with timezone, date_format, number_grouping, asset_aliases; unresolved → `unmapped_tag` |
| 6 | Run | L2 compose + migrate; cloud real-L2; both Go agents on host |
| 7 | Fail closed | Invalid → DLQ; unvalidated bill refused; unresolved asset/time → event; L2 down → outbox; WAN down → SQLite; poller off |
| 8 | L4 tools | `l2-query-tools.json` at `GET /v1/agent-tools`; no SQL; no graph traverse |

---

## Decision — Layout

**Context.** Meters live on OT; ERP/WMS/CMMS live on IT; people upload bills. One process with all credentials would mix trust zones.

**Decision.** Record catalog: existing `measurement`, `event`, `bill_line`, `production_record`, `production_order` plus `asset_state`, `process_batch`, `flow_position`, `maintenance_context`, `quality_status`, `material_availability`, `shift_roster` (ingest existing schema), `operating_rate`, and `plant_constraint` (table + GET only). Ownership: `edge-agent` publishes OT measurements/events/`asset_state`; `context-agent` publishes IT production and context; bill publishes reviewed human uploads; cloud validates and relays; L2 demuxes into seven schemas.

**Consequences.** Two Go commands in one module. No L1 path invents assets or timestamps.

**Alternatives rejected.** Single agent with ERP + Modbus credentials; second database per domain; plant-wide semantic model before typed records.

---

## Decision — Trust

**Context.** Multi-tenant SaaS must not let a prompt switch orgs or exfiltrate DSNs.

**Decision.** Service auth stays `X-Service-Key` + `X-Org-Id` with row-level security on `org_id`. Tool arguments never carry `org_id`. Pack secrets are env/file references, never literals. Agents expose no inbound HTTP. Every plant path is read-only (no OT write, no ERP write-back, no quality release).

**Consequences.** L4 binds tools with service credentials only. Site packs name `secret_ref`, not passwords.

**Alternatives rejected.** Passing `org_id` in tool JSON; MCP as the product surface; FOCAS or PLC write.

---

## Decision — Data

**Context.** Measurements are dense; state words and business context are sparse. Competitors split engines; we already run one TimescaleDB.

**Decision.** One TimescaleDB. Three physical shapes: dense hypertables for `measurement`; on-change (+60s heartbeat) hypertable for `asset_state`; insert-on-change ordinary tables for context in `features` / `commercial` / `graph`. Dedupe for context is `sha256(org|plant|record_type|business_id|observed_at)`. Latest reads order by `observed_at`, not insert time. Every new context row carries `lineage` (`source_system`, `connector_id`, `pack_id`, `pack_version`, `source_record_id`). Migration `014_context_records.sql` owns the DDL.

**Consequences.** A→B→A history is three rows. Publisher change-detection lives in the agent SQLite last-hash table, not L2.

**Alternatives rejected.** Value-hash dedupe; second TSDB; document store for ERP payloads; graph database for flow.

---

## Decision — Wire

**Context.** Payload schemas set `additionalProperties: false`, so `record_type` cannot sit inside `record`.

**Decision.** Existing MQTT suffixes keep their types (`measurements`, `events`, `health`, `production`, `orders` → `production_order`, `bills`). New suffix `stamped/v1/{org}/{plant}/context` carries wrapper `{"record_type":"...","record":{...}}`. Cloud validates `record` against that schema and wraps the envelope. `POST /v1/context` takes the same wrapper.

**Consequences.** Low-volume context shares one topic. Orders keep `POST /v1/production-orders`.

**Alternatives rejected.** Encoding type inside the payload; one topic per new type; Kafka as the plant bus.

---

## Decision — Packs

**Context.** Indian exports use IST without offsets, `dd-mm-yyyy`, and lakh grouping (`1,00,000`). Machine names on sheets are not asset ids.

**Decision.** Pack schema requires engine (`file_rows`|`rest_rows`|`sql_rows`|`opcua_state`), record type, field map, `timezone` (default `Asia/Kolkata`), `date_format`, `number_grouping` (`lakh`|`international`), `asset_ref`, and optional `secret_ref` (name only). Site `asset_aliases` maps plant names to asset ids. Unresolved asset or time becomes an `unmapped_tag` event, never a guessed row.

**Consequences.** New vendors are YAML, not new services. Bhatia starts as file packs.

**Alternatives rejected.** Guessing UTC; inventing `asset_id`; embedding passwords in packs.

---

## Decision — Run

**Context.** Proof must be a real local stack, not mocks.

**Decision.** R1 boots L2 Docker Compose, applies migrations, runs cloud with the real-L2 profile, and runs both Go agents on the host against Bhatia-shaped fixtures. No cloud deploy in this graph.

**Consequences.** Docker Desktop must be up before R1/T1. Failures escalate, never silent-pass.

**Alternatives rejected.** Contract-only green without containers; cloud deploy as the first proof.

---

## Decision — Fail closed

**Context.** Bad plant data must not become facts.

**Decision.** Invalid schema → DLQ. Unvalidated bill → publish refused. Unresolved asset or time → `unmapped_tag` event, not a typed row. L2 down → cloud outbox holds. WAN down → agent SQLite holds (~72h) then MQTT QoS 1. SaaS poller (`CONTEXT_POLL_ENABLED`) defaults off and an empty poll list polls nothing.

**Consequences.** Default compose makes zero vendor calls. Plant IT host remains the preferred ERP path when it can reach the API or a file drop.

**Alternatives rejected.** Best-effort invent zeros; poller on by default; dropping MQTT acks when L2 is down.

---

## Decision — L4 tools

**Context.** Architecture 14 allowlists typed L2 reads. The model must not get SQL or a free graph walk.

**Decision.** Catalog at `contracts/tools/l2-query-tools.json`, served by L2 at `GET /v1/agent-tools`. Each tool is one bounded query-api path with a JSON Schema for arguments. No `org_id` argument. No SQL. No `graph/traverse`. No baselines, SEC features, health, or admin on the agent list.

**Consequences.** This graph publishes the catalog; L4 binds it later. Body must equal the pinned file.

**Alternatives rejected.** MCP server as product surface; raw SQL tool; semantic-first store before allowlisted reads.
