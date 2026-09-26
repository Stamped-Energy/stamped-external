# L2 — Universal repository

*Status: as-built · 2026-09-26*  
*Authority:* [STAMPED_ARCHITECTURE.md](../STAMPED_ARCHITECTURE.md) §4 · [ADR-009](../../decisions/006-010/ADR-009-stamped-l2-repo-charter.md) · [ADR-031](../../decisions/028-032/ADR-031-l1-l2-context-records.md) · **configure & prove:** [L1-L2-DATA-PLANE.md](../L1-L2-DATA-PLANE.md)

L2 is the **only** layer that opens Timescale for **plant truth**. L1 posts envelopes; L3–L6 read through HTTP with service keys. L4 may hold *derived* operational data (PSM, traces) in its own store — never a second plant system of record.

| Label | Meaning |
| --- | --- |
| **as-built** | `universal-repositary` on main |
| **contract** | Envelope ingest + query API + ADR-031 context records |
| **direction** | Plant-wide industrial graph product (explicit non-goal) |

---

## Repo

| Repo | Job | Must not |
| --- | --- | --- |
| `universal-repositary` | Timescale seven schemas; HTTP ingest; query-api; ops console | L1 protocol adapters; customer Forge UI; hand `L2_DATABASE_URL` to L3–L6 |

Typical ports (local compose): ingest `:8090` · query `:8091` · console `:8092` · admin `:8093` · Timescale `:5433`.

---

## Seven schemas (as-built)

| Schema | Holds | Writers |
| --- | --- | --- |
| `ingest` | Dedup inbox + audit | ingest only |
| `telemetry` | measurement / event hypertables, aggregates, evidence archives, `asset_state` | ingest |
| `graph` | Asset topology | seed / admin |
| `commercial` | tariffs, bills, bill lines, operating rates | ingest + seed |
| `features` | production, orders, department graph, context tables | ingest + seed |
| `baselines` | baseline models | seed / admin |
| `ledger` | M&V ledger intents | L5 flows via ops/SQL paths — not L1 stream |

Detail and retention: consumer `docs/EXTENSIVE.md`. Configure meters and context into these stores via [L1-L2-DATA-PLANE.md](../L1-L2-DATA-PLANE.md).

---

## How facts land

1. L1 relay `POST /v1/ingest/records` with `StampedRecordEnvelope`.
2. Validate against contracts → insert `ingest.l1_processed_inbox` on `dedupe_key`.
3. New → demux to schema tables (**201**); conflict → **200** `{inserted: false}`.
4. `bill_line` requires `extraction.validated=true` or **422**.
5. Historian backfill: `POST /v1/ingest/measurements/backfill` forces `late=true` and stamps lineage — same measurement store.

---

## What L3–L6 may ask

| Allowed | Forbidden |
| --- | --- |
| Query HTTP (`X-Service-Key` + `X-Org-Id`): measurements, assets, tariffs, context | `L2_DATABASE_URL` in L3–L6 |
| Constraint / roster / condition context reads | Treating L2 as a plant-wide graph product |

L3 engines KeyError or empty when required tags are missing — that is fail-closed, not invent.

---

## Hard rules

| Rule | Why |
| --- | --- |
| Only L2 opens Timescale for plant truth | Spine invariant |
| Dedupe on `dedupe_key` | At-least-once L1 relays |
| No invent `asset_id` / timestamps | Data plane honesty |
| Ops console ≠ customer UI | Customer surface is L6 |

---

## Related

- Data plane (configure + prove): [L1-L2-DATA-PLANE.md](../L1-L2-DATA-PLANE.md)
- Handoffs: [`../../handoff/l2/`](../../handoff/l2/) — prefer **this page** for architecture
