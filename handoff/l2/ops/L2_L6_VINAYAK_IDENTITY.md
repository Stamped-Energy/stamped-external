# L2→L6 — Vinayak plant identity handoff

> **Audience:** Agents and engineers wiring demo / QA tenants across L2…L6.  
> **Status:** Commit C-ext prep — document only; do **not** bump consumer submodule pins until this lands on a tagged `stamped-external` commit.  
> **Submodule note:** Consumers may see detached / dirty `external/` checkouts while this file is prepared locally.

---

## 1. Canonical identity

| Field | Canonical value |
|-------|-----------------|
| `plant_id` | `plant_vinayak_1` |
| `org_id` | `org_acme` |
| Display name | **Vinayak Plant** |

Use these IDs consistently in seeds, fixtures, BFF session plant context, and curl smokes. Do not invent parallel demo plant IDs for the Vinayak path.

---

## 2. L4 → L5 ingest

L4 emits prescriptions into L5 via:

```http
POST /v1/prescriptions/ingest
X-API-Key: <l5-scoped-key>
Content-Type: application/json
```

Body is a `Prescription` with `org_id=org_acme` and `plant_id=plant_vinayak_1`. Successful ingest opens workflow and raises an EMS alarm for that plant.

Finding intake that must accompany fixture paths: seed findings first (`POST /v1/fixtures/findings` in L5 CI/dev) with the same `plant_id` / `org_id` so clearance refs resolve.

---

## 3. L5 plant-scoped reads

L5 is source of closure truth. Plant-scoped GETs (auth: `X-API-Key`):

| Method | Path |
|--------|------|
| `GET` | `/v1/plants/plant_vinayak_1/alarms?org_id=org_acme` |
| `GET` | `/v1/plants/plant_vinayak_1/prescriptions?org_id=org_acme` |

Alarm list items are L6-friendly: `id`, `plant_id`, `severity`, `state`, `summary`, `related_prescription_id` (plus `prescription_id` alias).

L5 smoke doc (consumer repo): `closure-verification/docs/VINAYAK_SMOKE.md`.

---

## 4. L6 BFF

L6 (`experience-integration` / stamped-l6) exposes session + plant-scoped BFF routes that proxy L5:

| BFF | Upstream L5 |
|-----|-------------|
| `GET /api/alarms` | `GET /v1/plants/{plantId}/alarms` |
| `GET /api/prescriptions` | `GET /v1/plants/{plantId}/prescriptions` |

Active plant context for the Vinayak demo must resolve to `plant_vinayak_1` under `org_acme` (display **Vinayak Plant**).

---

## 5. L3→L4 envelope filter

L4 inbox only accepts Finding envelopes that satisfy:

```text
delivery = l4  ∧  status = emitted
```

(`record_type=finding` as implemented). Lab-only / suppressed / shadow / hypothesis deliveries must not reach L5 for this path.

When seeding or bridging findings for Vinayak, wrap payloads with `delivery: "l4"` and `status: "emitted"` before L4 intake.

---

## 6. Full-stack deploy pointer

Workspace deploy narrative (L2 through L6):  
`knowledge-reasoning/docs/DEPLOY_L2_TO_L6.md`

---

## Changelog

| Date | Change |
|------|--------|
| 2026-07-29 | Initial Vinayak identity handoff (C-ext prep) |
