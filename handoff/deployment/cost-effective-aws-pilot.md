# Cost-effective AWS pilot — plant-PC edge + cheap cloud

> **Reusable** across accounts (LNM Faridabad is one consumer of this pattern).  
> **Authority:** [ADR-002](../../decisions/001-005/ADR-002-build-all-aws-networking.md) · [ADR-010](../../decisions/006-010/ADR-010-deployment-profiles-and-portability.md) · [deployment-profiles.md](./deployment-profiles.md) · [stamped-l2-aws-deployment.md](../l2/ops/stamped-l2-aws-deployment.md)  
> **Pricing script:** [`scripts/pricing/pilot-aws-one-factory.py`](../../scripts/pricing/pilot-aws-one-factory.py) (deterministic; no mental arithmetic)

---

## 1. Default topology

**Mode:** `STAMPED_DEPLOYMENT_MODE=cloud`

```text
┌──────────── Customer plant ────────────┐
│  FANUC DC / meters / CSV               │
│           │                            │
│  [existing PC]  connectors-edge        │
│  SQLite buffer · tag map               │
│  outbound MQTT/TLS :8883 or :443 only  │
└──────────────────┬─────────────────────┘
                   │
                   ▼
         Stamped AWS ap-south-1
         Mosquitto (t4g.small EC2)
         Fargate ingest / L2 / bill path
         Shared RDS db.t4g.small
         S3 bills
```

| Layer | Where | Notes |
|-------|--------|--------|
| Edge agent | **Their existing PC** | Always-on; outbound HTTPS; no inbound ports |
| MQTT | Stamped EC2 Mosquitto | Not IoT Core at pilot scale |
| Ingest + L2 | Fargate + shared RDS | Reuse `stamped-pilot` — **no second VPC** |
| Bills | S3 + connectors-bill | PDF / photo path |
| Dashboard | Existing L6 cloud path | |

**Fallback:** `local-dashboard` — full compose on that same PC if IT refuses outbound MQTT. Heavier ops; offer as escape hatch, do not lead with air-gap.

---

## 2. Do / do not buy

| Do | Do not |
|----|--------|
| Reuse shared RDS + Mosquitto + Fargate | New VPC per customer |
| Edge on their PC | Dedicated mini-PC if theirs stays on |
| Single-AZ RDS | Multi-AZ / Aurora / Tiger Cloud at seed |
| Public subnet + strict SG | NAT Gateway (~₹2.5k+/mo per AZ) |
| Cap frontier LLM tokens / rules-only soak | Unmetered LLM as default |
| Consume their FANUC collector northbound | Kepware SKU or Stamped FOCAS DLL |

---

## 3. One-factory monthly cost (script output)

**As of:** 2026-08-21 UTC · **Region:** `ap-south-1` · **Hours:** 730  
**FX:** USD→INR **83.5 ESTIMATED** (display only)  
**Source:** public AWS Price List offer files via [`pilot-aws-one-factory.py`](../../scripts/pricing/pilot-aws-one-factory.py)

| Component | Monthly USD (script) | Monthly ₹ ESTIMATED | Label |
|-----------|----------------------|---------------------|--------|
| EC2 t4g.small (Mosquitto) | 8.18 | ~683 | ACTUAL × FX EST |
| RDS db.t4g.small Single-AZ Postgres | 30.66 | ~2,560 | ACTUAL × FX EST |
| EBS gp3 50 GB | 4.56 | ~381 | ACTUAL × FX EST |
| Public IPv4 ×1 | 3.65 | ~305 | ACTUAL × FX EST |
| Fargate 0.25 vCPU / 0.5 GB | 9.47 | ~790 | ACTUAL × FX EST |
| S3 Standard 5 GB | 0.13 | ~10 | ACTUAL × FX EST |
| CloudWatch Logs ~5 GB ingest | 2.50 | ~209 | ESTIMATED rate |
| **Infra total (dedicated stack)** | **~59.14** | **~₹4,940** | script sum |

**Important:**

1. **Shared `stamped-pilot`:** if Mosquitto + RDS already exist for other pilots, **incremental** cost for one more factory is mostly edge (₹0 opex) + tiny S3/logs + LLM — often **≪ ₹5k**.  
2. **LLM is the real blow-up risk.** Cap tokens; use rules-only for soak if needed. Infra is not the problem.  
3. **ADR-002 ceiling ₹15–25k/mo** is for **≤10 plants**. One factory sits well under that.  
4. A ₹22L/month site electricity bill does **not** justify a bigger RDS.

Re-run: `python scripts/pricing/pilot-aws-one-factory.py`

---

## 4. Plant-PC requirements (checklist)

| Need | Why |
|------|-----|
| Always-on Windows or Linux PC | Edge must not sleep overnight |
| Outbound HTTPS / 8883 | MQTT TLS to Stamped |
| LAN reach to collector and/or meter | OPC UA / REST / CSV / Modbus |
| Disk for SQLite ≥72 h buffer | Store-and-forward |
| Named IT contact | Certs / firewall if OPC UA |

Cellular 4G gateway remains Path B default when plant LAN is refused ([ADR-002](../../decisions/001-005/ADR-002-build-all-aws-networking.md)).

---

## 5. LNM Faridabad sizing note

| Fact | Implication |
|------|-------------|
| Three adjacent factories, ~₹22L/mo combined bill (field) | Pilot **one** factory first |
| Weak EMS today | Demo shows monitoring screens; still sell prescriptions + verify |
| FANUC DC partially populated | Edge reads northbound; no FOCAS |
| Existing PCs on site | Default: agent on their PC + this AWS profile |

Account-specific narrative: [`pilot-research/`](../../pilot-research/).

---

## 6. Upgrade triggers (unchanged from ADR-002 / L2 doc)

| Signal | Action |
|--------|--------|
| RDS CPU >70% sustained 7d | `db.t4g.medium` |
| Storage >80% | Grow gp3 |
| Ingest lag p95 >2 min | Split Fargate ingest vs query |
| Enterprise private-only | NAT / private subnets (cost jumps) |
| Fleet >30 plants or Multi-AZ SLA | Multi-AZ + read replica |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-08-21 | Initial reusable plant-PC + cheap AWS note; Price List script totals for ap-south-1 |
