# ADR-023: L6 next-action surfaces and dual-mode analyst context

| Field | Value |
| --- | --- |
| **Status** | Accepted (identity revised 2026-09-24) |
| **Date** | 2026-07-21 |
| **Deciders** | Engineering (L6 architecture + UI handoff) |
| **Related** | [ADR-018](../016-020/ADR-018-l4-pilot-execution-knowledge-reasoning.md) · [ADR-020](ADR-020-l5-mv-claim-governance.md) · [ADR-021](ADR-021-l5-notification-and-evidence.md) · [ADR-022](ADR-022-l6-bff-runtime-boundary.md) · [ADR-030](../028-032/ADR-030-five-domain-decision-loop.md) · [L5 SSOT](../../technical/layers/l4-l6/L5-closure-and-verification.md) · [L4 SSOT](../../technical/layers/l4-l6/L4-knowledge-and-reasoning.md) · [workflow-event.json](../../contracts/schemas/envelope/workflow-event.json) |

---

## Context

Product decisions (2026-07-21), restated under ADR-030 (2026-09-24):

1. L6 is an **ops-first control room** for the next operating action — not a chart gallery and not an energy-management product.
2. Alarms and exceptions are detected/hinted by L3, routed by L5, and **rendered/acted in L6**.
3. The analyst needs a **full workspace** and a **route-aware side assistant**.
4. Cognitive load stays low: advanced modules appear via **progressive reveal**.

L4 owns RAG/agent runtime ([ADR-018](../016-020/ADR-018-l4-pilot-execution-knowledge-reasoning.md)); L6 owns chat UX only. Product identity: [ADR-030](../028-032/ADR-030-five-domain-decision-loop.md).

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Alarm / exception UI | **L6 renders** the console; **L5 owns** raise/ack/escalate/silence/clear truth |
| 2 | Alarm states | `raised` · `acked` · `escalated` · `silenced` · `cleared` (from L5 / `WorkflowEvent`) |
| 3 | Home density | Today shows **≤7** decision signals; advanced modules behind role-aware **More / Reveal** |
| 4 | Analyst modes | **Dual-mode**: (A) contextual side assistant, (B) full `/analyst` workspace |
| 5 | Analyst phasing | Contextual shell contracts + UI in **P0**; full workspace + L4 live chat in **P1** |
| 6 | Context policy | Side assistant receives an **explicit, user-visible, removable** screen-context envelope — never silent page scrape |
| 7 | RAG | Always via L4 HTTP; L6 does not embed vectors or run tools |
| 8 | Language | **English through P2** ([ADR-018](../016-020/ADR-018-l4-pilot-execution-knowledge-reasoning.md) §10) — Hindi deferred |
| 9 | Irreversible actions | Ack / defer / reject / silence require explicit user action; agent may **propose**, never auto-commit |

---

## 1. Alarm and exception console (P0)

| Concern | Rule |
| --- | --- |
| Data | L5 alarm list query + SSE `alarm_*` / `ops_*` events |
| Actions | Ack / escalate / silence / open evidence / link decision card — POSTs through L6 BFF → L5 with Idempotency-Key |
| UX | Severity-first, ageing badges, keyboard triage, stale-connection banner, mobile-capable ack |
| Colour | ISA-101: grayscale normal; colour only for abnormal / overdue |
| Non-goal | L6 is **not** a SCADA HMI or OT alarm system of record |

---

## 2. Progressive disclosure

Primary nav (always): **Today · Alarms · Decision cards · Evidence · Analyst · Reports**.

Role-gated **More** reveals: Energy domain analytics, Equipment health, TOD/MD, Intensity/CO₂, Integrations, Admin.

Rules:

- Reveal preference remembered per user.
- Critical open alarms and assigned cards **cannot** be hidden by collapsing More.
- Today never becomes a dashboard of every module.

---

## 3. Dual-mode analyst

### Mode A — Contextual side assistant (P0 shell)

Mounted beside a working screen (Alarms, Decision cards, Evidence, …).

```text
AnalystContextEnvelope {
  org_id, plant_id, user_id, role
  route_id, screen_title
  focus_entity?: { type: alarm|prescription|asset|ledger_entry, id }
  visible_summary: string[]     # user-visible chips only
  time_range?: { from, to }
  exclude_keys?: string[]       # user removed chips
}
```

- UI shows attached chips; user can remove any chip before send.
- BFF validates tenant match and strips secrets / hidden DOM / raw tokens.
- L4 still runs RAG over corpus + tools; screen context is **additional**, not a replacement.

### Mode B — Full analyst workspace (P1)

Route `/analyst`: conversation column, sources/citations, evidence canvas, saved investigations, **handoff-to-action** (create/open card, deep-link alarm) with human confirm.

---

## 4. Security constraints

1. No prompt injection via untrusted page HTML — only structured envelope fields.
2. Cross-tenant `focus_entity` IDs rejected at BFF.
3. Audit: every analyst turn logs model id, tokens, latency, tool calls (from L4), and envelope hash.
4. WhatsApp / magic-link surfaces must not feed raw chat into agent context ([ADR-018](../016-020/ADR-018-l4-pilot-execution-knowledge-reasoning.md)).

---

## Consequences

- L6 SSOT phasing: conversational analyst **P0 contextual / P1 full**.
- UI charter specifies alarm/exception console and both analyst modes.
- Reference seed implements Mode A chrome + Mode B layout against fixtures; live L4 wiring is consumer P1.

---

## Alternatives considered

| Option | Rejected because |
| --- | --- |
| Drawer-only AI (demo `AiDrawer`) | Undervalues investigation; context of active screen is weak |
| Full analyst in P0 | Blocks queue closure on L4 maturity |
| Silent full-page context scrape | Prompt injection + PII/secret leak risk |
| Separate alarm micro-frontend | Over-splits one product; progressive reveal covers density |
