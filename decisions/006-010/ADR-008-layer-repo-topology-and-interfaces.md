# ADR-008: Layer repo topology and cross-service interfaces

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-07-10 |
| **Deciders** | Vinayak (product), engineering |
| **Related** | [ADR-007](ADR-007-connectors-cloud-repo-charter.md) · [Technical architecture §5](../../technical/STAMPED_ARCHITECTURE.md) · [Layer interfaces](../../architecture/layer-interfaces-l2.md) |

---

## Context

Stamped's L0–L6 stack is implemented as **separate deployable repositories** communicating through **versioned contracts only** — no layer may reach around its upstream interface ([technical architecture §5](../../technical/STAMPED_ARCHITECTURE.md)).

Production patterns applied (see [layer-interfaces-l2.md](../../architecture/layer-interfaces-l2.md) §1):

- **Transactional outbox** for reliable cross-service publish after local commit ([AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html), [Conduktor outbox glossary](https://www.conduktor.io/glossary/outbox-pattern-for-reliable-event-publishing))
- **Idempotent consumers** with durable inbox / unique constraints ([Conduktor idempotent consumers](https://www.conduktor.io/blog/building-idempotent-consumers))
- **Contract-first JSON Schema** with BACKWARD compatibility CI ([KloudVin data contracts](https://kloudvin.com/article/data-contracts-schema-registry-reliable-pipelines/))
- **Transport dedup + business dedup** separation ([Granit IoT ingestion](https://granit-fx.dev/dotnet/iot/telemetry-ingestion/))

Skills applied: `backend-architecture`, `system-design-tradeoffs`, `agentic-system-design` (L4 tool boundaries).

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Topology | **One repo per layer** (L1 split into edge/cloud/bill; L2–L6 each own repo) |
| 2 | Communication | **Async events** across layer boundaries; sync HTTP only for query APIs with defined SLOs |
| 3 | Contract store | **`stamped-platform/contracts/`** (submodule at `external/contracts/` in consumers) — canonical for all repos ([ADR-011](../011-015/ADR-011-stamped-platform-submodule-distribution.md)) |
| 4 | Compatibility | **BACKWARD** JSON Schema mode; CI blocks breaking PRs |
| 5 | Delivery | **At-least-once**; consumers **idempotent** via `dedupe_key` + processed inbox |
| 6 | Envelope | All cross-layer messages wrap payload in `StampedRecordEnvelope` (see layer-interfaces.md) |
| 7 | Observability | `correlation_id`, `trace_id` (OpenTelemetry) on every envelope |
| 8 | Agent tools (L4) | Narrow HTTP/gRPC tools against L2/L3 query APIs — no direct DB access from L4 |

---

## 1. Repository map

```text
L1  connectors-edge     Plant runtime, tag mapping, contracts source
L1  connectors-cloud    Cloud ingest → L1→L2 boundary
L1  connectors-bill     Bill PDF → BillLine MQTT

L2  stamped-l2          Universal Repository (Timescale, graph, commercial, ledger…)
L3  stamped-l3          Intelligence engines → Finding
L4  stamped-l4          Prescription agent → Prescription
L5  stamped-l5          Workflow, M&V → LedgerEntry
L6  stamped-l6          Dashboard, public API, exports
```

---

## 2. Interface matrix

| Boundary | Transport (P0) | Payload contract | Producer repo | Consumer repo |
| --- | --- | --- | --- | --- |
| Plant → L1 cloud | MQTT QoS 1 | L1 schemas raw | connectors-edge, connectors-bill | connectors-cloud |
| L1 → L2 | Outbox → poll/HTTP | `L1RecordEnvelope` + Measurement/Event/ProductionRecord/BillLine | connectors-cloud, connectors-bill | stamped-l2 |
| L2 → L3 | Outbox / internal bus | `L2SnapshotRef`, query API responses | stamped-l2 | stamped-l3 |
| L3 → L4 | Outbox | `Finding` | stamped-l3 | stamped-l4 |
| L4 → L5 | Outbox | `Prescription` | stamped-l4 | stamped-l5 |
| L5 → L6 | Outbox + query API | `LedgerEntry`, workflow state | stamped-l5 | stamped-l6 |

---

## 3. Non-negotiable rules

1. **No shared database writes across repos** — each service owns its tables; coupling only via events or documented query APIs.
2. **No cross-repo SQL joins** — L3 never queries L2 tables directly; uses `stamped-l2` internal API.
3. **Schema changes are additive** within a major version; breaking changes require new major + migration plan.
4. **Dedupe keys are stable** — derived from business fields in TOPICS.md / technical architecture §5, not broker message IDs alone.
5. **Late data** carries `late: true` on envelope; L2/L3 must handle per L1 spec §5.

---

## 4. P0 build order (after L1 cloud complete)

| Order | Repo | Exit criterion |
| --- | --- | --- |
| 1 | connectors-cloud | All MQTT topics ingested; outbox publishing; contract tests green |
| 2 | stamped-l2 | L1 consumer inbox; measurement hypertable; RLS; first evidence pointer resolvable |
| 3 | stamped-l3 | One engine (MD/demand) consuming L2 API; emits `Finding` |
| 4 | stamped-l4 | Agent drafts `Prescription` from `Finding` with verifier loop |
| 5 | stamped-l5 | Workflow + ledger append |
| 6 | stamped-l6 | Prescription queue API + one dashboard module |

---

## 5. Consequences

- Higher repo count than monolith — accepted for failure-domain isolation and parallel team/agent workspaces.
- Contract CI is load-bearing — without it, microservices become a distributed monolith with silent breakage.
- `external/technical/` specs remain research authority; `docs/architecture/layer-interfaces.md` is the **implementation contract** for agents.

---

## 6. Alternatives considered

| Option | Rejected because |
| --- | --- |
| Modular monolith L2–L6 in one repo | User chose layer-per-repo microservice topology |
| gRPC everywhere | JSON + Schema CI sufficient at pilot scale; HTTP query APIs for L2 tools |
| Exactly-once broker semantics | Impractical across Postgres sinks; idempotent consumers are industry standard |
