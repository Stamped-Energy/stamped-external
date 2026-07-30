# connectors-cloud — Cloud + air-gap portability playbook

> **Authority:** [ADR-010](../../../decisions/006-010/ADR-010-deployment-profiles-and-portability.md) · [ADR-007](../../../decisions/006-010/ADR-007-connectors-cloud-repo-charter.md)  
> **Downstream:** [connectors-cloud-downstream-context.md](./connectors-cloud-downstream-context.md)

---

## 1. Current state (from README + audit)

**Repo:** `Vinayak-RZ/connectors-cloud` (private — audit from handoff)

| Area | `cloud` mode today | Gap for `local*` |
|------|-------------------|------------------|
| ingest | ECS Fargate; MQTT + HTTP | Compose service |
| relay | Sidecar POST to L2 | Same logic; `L2_INGEST_URL` on Docker network |
| Postgres | RDS `connectors_cloud` | Container Postgres |
| MQTT broker | External EC2 Mosquitto | Bundled `mosquitto` in compose |
| Secrets | SSM Parameter Store | `.env` / Docker secrets |
| mock-l2 | Dev reference | `local` mode uses real stamped-l2 |

### Audit appendix

```text
Audit checklist (connectors-cloud)
├── README stated deployment model     → AWS Fargate + RDS + EC2 Mosquitto
├── deploy/ directory inventory        → docker-compose.cloud.yml (dev)
├── AWS-specific dependencies          → boto3 for SSM (ingest/relay)
├── Hardcoded external URLs            → L2_INGEST_URL configurable ✓
├── MQTT broker assumptions            → env MQTT_BROKER_URL
├── Secrets management path            → SSM → needs file fallback
├── OTA/update mechanism               → CI/CD deploy
└── Existing compose vs prod gap       → compose exists; needs profiles/
```

**Gap matrix:**

| Capability | `cloud` | `local` | Change required |
|------------|---------|---------|-----------------|
| MQTT ingest | Yes | Partial | Bundle Mosquitto in compose |
| Outbox + relay | Yes | Yes (same code) | Postgres container |
| jsonschema validation | Yes | Yes | No change |
| SSM secrets | Yes | No | File/env secrets |
| Zero egress | No | Target | Egress CI |

---

## 2. Target: mode support matrix

| Package | `local` | `local-dashboard` | `cloud` |
|---------|---------|-------------------|---------|
| ingest | compose | compose | Fargate |
| relay | compose sidecar | compose | Fargate sidecar |
| mosquitto | compose service | compose | EC2 |
| postgres | compose | compose | RDS |

---

## 3. Architecture changes

1. **Secrets abstraction** — `SECRET_BACKEND=ssm|file|env`; default `ssm` in `cloud`, `env` in `local*`.
2. **No boto3 in hot path when `STAMPED_DEPLOYMENT_MODE=local`** — lazy import or adapter pattern.
3. **Compose profile** — `deploy/profiles/local.yml` = production for air-gap customers.
4. **Relay URL** — `L2_INGEST_URL=http://stamped-l2-ingest:8090/v1/ingest/records` on compose network.

---

## 4. File-by-file change list

| Path | Action | Detail |
|------|--------|--------|
| `deploy/profiles/local.yml` | **add** | mosquitto + postgres + ingest + relay |
| `deploy/profiles/cloud.yml` | **add** | Pointer to Terraform/ECS |
| `deploy/docker-compose.cloud.yml` | **modify** | Align with profiles/local.yml services |
| `packages/ingest/` | **modify** | `SECRET_BACKEND` adapter |
| `packages/relay/` | **modify** | Retry config from env |
| `.env.example` | **modify** | All mode vars documented |
| `docs/egress-inventory.md` | **add** | Repo inventory |
| `scripts/egress-check.sh` | **add** | CI gate |
| `mocks/stamped-l2/` | **keep** | Reference until real L2 parity |

---

## 5. New env vars and defaults per profile

| Variable | `local` default | `cloud` default |
|----------|-----------------|-----------------|
| `STAMPED_DEPLOYMENT_MODE` | `local` | `cloud` |
| `DATABASE_URL` | `postgresql://cloud:cloud@postgres:5432/connectors_cloud` | RDS URL via SSM |
| `MQTT_BROKER_URL` | `mqtt://mosquitto:1883` | `mqtts://...` EC2 |
| `L2_INGEST_URL` | `http://stamped-l2-ingest:8090/v1/ingest/records` | Fargate L2 URL |
| `L2_INGEST_SERVICE_KEY` | dev secret in `.env` | SSM |
| `SECRET_BACKEND` | `env` | `ssm` |
| `RELAY_POLL_INTERVAL_SEC` | `8` | `8` |

---

## 6. deploy/profiles/ layout

```text
deploy/profiles/
├── local.yml              # Production air-gap
├── local-dashboard.yml    # Extends stamped-l2 master profile
├── cloud.yml              # ECS task reference
└── ARCHITECTURE.md
```

Master full-stack compose lives in **stamped-l2** repo; cloud repo profile is embeddable fragment.

---

## 7. Egress inventory (repo-specific)

| Call | Package | `local` | Mitigation |
|------|---------|---------|------------|
| MQTT subscribe | ingest | Internal broker only | compose mosquitto |
| L2 HTTP POST | relay | Internal Docker network | stamped-l2-ingest |
| SSM | ingest | **None** | `SECRET_BACKEND=env` |
| OTel SaaS | ingest | **None** | Disable or local collector |
| jsonschema refs | ingest | Local files only | `external/contracts/` |

---

## 8. CI gates

- [ ] Dedupe golden matches [dedupe_golden.json](../../../contracts/fixtures/golden/dedupe_golden.json)
- [ ] `scripts/egress-check.sh` on PR
- [ ] Compose E2E: MQTT bill_line → outbox → mock-l2/real-l2
- [ ] No `import boto3` when `STAMPED_DEPLOYMENT_MODE=local` in test matrix

---

## 9. OTA / update bundle process

**`cloud`:** Existing CI/CD → ECR → ECS rolling deploy.

**`local`:** Signed bundle with pre-loaded images + migration SQL + `.env.template`. Customer runs `docker compose up` after bundle ingest.

---

## 10. Testing: E2E per profile

```bash
# local
docker compose -f deploy/profiles/local.yml up -d
mosquitto_pub -h localhost -t stamped/v1/org/plant/bills -f fixtures/bill_line.valid.json
psql -c "SELECT count(*) FROM l1_outbox;"
curl -X POST $L2_INGEST_URL ...  # relay drains

# cloud — existing pilot scripts
```

---

## 11. Phase breakdown

| Phase | Ships |
|-------|-------|
| **P0** | `deploy/profiles/local.yml`; secret adapter; egress CI; joint E2E with stamped-l2 |
| **P1** | Terraform `cloud` profile; OTel optional |
| **P2** | Multi-tenant broker ACL automation |

---

## 12. Non-goals

- Writing L2 tables directly (unchanged anti-pattern)
- Redpanda/Kafka at P0
- Stamped cloud control plane in `local` mode
