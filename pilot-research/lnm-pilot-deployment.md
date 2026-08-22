# LNM Faridabad — pilot deployment (2 containers + Lambda + Vercel)

Internal. Locked shape for the **LNM demo → one-factory pilot** (not the full 12-service compose farm).

**Related:** [`lnm-runbook-26aug-9sep.md`](./lnm-runbook-26aug-9sep.md) · [`lnm-plant-ee-me-sw.md`](./lnm-plant-ee-me-sw.md) · reusable cost note [`../handoff/deployment/cost-effective-aws-pilot.md`](../handoff/deployment/cost-effective-aws-pilot.md)

**Mode:** `STAMPED_DEPLOYMENT_MODE=cloud`  
**Plant:** one Faridabad factory (pick on walk). Jaipur / other two sheds = later.

---

## 1. Topology (locked)

```text
┌────────────── LNM plant PC ──────────────┐
│  FANUC DC / incomer Modbus / CSV         │
│                                          │
│  [1] connectors-edge   ← only plant box  │
│      (Modbus + OPC UA/REST/filewatch     │
│       inside ONE process — not separate  │
│       “connector” containers)            │
│      SQLite buffer ≥72 h                 │
│      outbound MQTT/TLS or HTTPS only     │
└────────────────────┬─────────────────────┘
                     │
                     ▼
┌────────────── Stamped AWS ap-south-1 ────┐
│  [2] pilot-core  (ONE container / task)  │
│      · MQTT receive (or HTTPS ingest)    │
│      · validate / dedupe                 │
│      · L2 Timescale write + query API    │
│      (Mosquitto colocated OR edge posts  │
│       HTTPS — see §3)                    │
│                                          │
│  Not containers:                         │
│  · RDS Postgres+Timescale (shared OK)    │
│  · S3 bill PDFs                          │
│  · Lambda — bill extract on S3 event     │
│  · Vercel / CloudFront — L6 dashboard    │
│  · Frontier LLM API — rules-only for soak│
└──────────────────────────────────────────┘
```

| # | Runtime | Role |
|---|---------|------|
| **1** | Docker on **their PC** | `connectors-edge` — all L1 drivers in one agent |
| **2** | One ECS Fargate task **or** one process set on shared Mosquitto EC2 | **pilot-core** — ingest + L2 colocated |
| — | Lambda | Bills only (cold start OK) |
| — | Vercel | EMS-class screens + Rx UI |
| — | RDS / S3 | Managed — do not count as Docker |

**Total always-on containers for LNM: 2.**

Do **not** stand up separate containers for Modbus, OPC UA, REST, filewatch, ingest-only, L2-query-only, MinIO, local-llm, or stamped-l6 compose on site.

---

## 2. Why this is enough for demo + pilot

| Need by 27 / 29 | How this topology covers it |
|---------------|------------------------------|
| EMS-class monitoring | Edge → pilot-core → Vercel reads L2 query API |
| 5–10 FANUC machines | Drivers inside edge; northbound only (no FOCAS) |
| Incomer + bills | Modbus on edge; PDF → S3 → Lambda → L2 `BillLine` |
| ≥1 prescription | L3/L4 can call frontier API; staff-gate Rx; no extra container |
| History insights | Batch upload bills / CSV to S3 or edge filewatch — scripts, not new services |

Wave A product checklist still applies: [`../handoff/holistic/stamped-holistic-pilot-stack.md`](../handoff/holistic/stamped-holistic-pilot-stack.md). This file only locks **runtime shape**.

---

## 3. pilot-core packing options

Prefer the cheapest ops story that already exists in ADR-002 / L2 P0.

| Option | Pack | When |
|--------|------|------|
| **A (default)** | Shared Mosquitto on existing `t4g.small` EC2 **+** one Fargate task = ingest+L2 | Multi-pilot fleet; reuse `stamped-pilot` |
| **B (true 2-box)** | Mosquitto process **inside** the same host/task supervisor as ingest+L2 | Want literally two Docker images total for LNM |
| **C (Path F-ish)** | Edge posts HTTPS envelopes; no always-on Mosquitto for this plant | IT hates MQTT; CSV/bills already file-heavy |

For LNM: start **A** if `stamped-pilot` already has Mosquitto. If not, use **B** so the customer-facing story stays “two containers.”

---

## 4. Explicitly out of scope (this deployment file)

| Out | Use instead |
|-----|-------------|
| `local-dashboard` 11–13 compose services on plant PC | Only if IT blocks all outbound — escape hatch, not default |
| Per-protocol containers | One edge agent |
| Always-on bill Fargate | Lambda |
| Second FOCAS client | Their FANUC collector northbound |
| Second VPC / dedicated RDS for LNM | Shared `stamped-pilot` |
| Jaipur / factories 2–3 | Expansion after Factory 1 works |

---

## 5. Plant PC checklist

| Need | Notes |
|------|--------|
| Always-on | Edge must survive overnight soak |
| Outbound 443 / 8883 | No inbound ports |
| Reach collector + incomer | Same LAN or USB/RS-485 |
| Disk | SQLite ≥72 h at full tag rate |
| One named IT contact | Certs if OPC UA |

---

## 6. Cost posture (pointer)

Infra math lives in [`../handoff/deployment/cost-effective-aws-pilot.md`](../handoff/deployment/cost-effective-aws-pilot.md) (~₹5k dedicated stack; much less incremental if Mosquitto+RDS already shared).

LNM-specific: **LLM tokens** are the variable risk — soak with `rules-only` / capped frontier if needed. Do not grow RDS because the campus bill is ₹22L/mo.

---

## 7. Smoke path (deployment acceptance)

1. Edge publishes ≥1 measurement envelope (incomer or CNC state).  
2. pilot-core accepts; L2 query returns the point.  
3. Vercel (or L6) shows EMS-class incomer + machine overlay.  
4. One bill PDF → S3 → Lambda → `BillLine` visible.  
5. One staff-gated idle Rx with ₹ **illustrative**.

If any step needs a third always-on container, stop and justify — default answer is no.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-08-22 | LNM pilot deployment locked: 2 containers + Lambda + Vercel |
