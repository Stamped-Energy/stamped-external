# L5 Internal Console — as-built API surface

> Wave F sync · Stamped staff only · not customer Forge

## Base

- L5 API prefix: `/v1/internal/*`
- Auth: `write:admin` scope (same as other admin routes in P0)
- Console UI: `closure-verification/packages/internal-console` (port **8095**)

## Routes

| Method | Path |
|--------|------|
| GET/PATCH | `/v1/internal/plants/{plantId}/settings` |
| GET | `/v1/internal/rx-review-queue` |
| POST | `/v1/internal/prescriptions/{id}/approve-for-client` |
| POST | `/v1/internal/prescriptions/{id}/withhold` |
| GET/POST | `/v1/internal/plants/{plantId}/improve/cycles` |
| POST | `/v1/internal/improve/cycles/{id}/approve` |
| POST | `/v1/internal/improve/cycles/{id}/reject` |
| GET | `/v1/internal/plants/{plantId}/signals` |
| GET/PUT | `/v1/internal/plants/{plantId}/notes` |
| POST | `/v1/internal/prescriptions/{id}/admin-notes` |
| GET | `/v1/internal/plants/{plantId}/ml/runs` |
| POST | `/v1/internal/plants/{plantId}/ml/finetune` |
| POST | `/v1/internal/plants/{plantId}/ml/runs/{runId}/promote` |
| POST | `/v1/internal/plants/{plantId}/ml/runs/{runId}/rollback` |

## Invariants

- Improve job and fine-tune never auto-approve
- `pending_stamped_review` / `withheld` filtered from L6 customer lists
- Plant notes are manual scratchpad (not Improve Track C)
