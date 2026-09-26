# L3 — Finding contract and L4 intake

*Status: as-built · 2026-09-26*  
*Contract:* [`contracts/schemas/intelligence/finding.json`](../../contracts/schemas/intelligence/finding.json) · **const `1.2.0`**  
*Forward schema (direction):* [`finding-2.0.0.json`](../../contracts/schemas/intelligence/finding-2.0.0.json) — not what core emits today

## What core emits

| Field / rule | As-built |
| --- | --- |
| `schema_version` | **`1.2.0`** (`stamped_l3_core.models.finding`) |
| `ops_clearance` | Required — measurement boundary, related tags, predicate, stabilize / reopen |
| `value_domain` | `energy_efficiency` \| `equipment_health` (product framing is four outcomes in the master document; field not migrated yet) |
| Money | Tariff-cited decomposition; no silent invent |
| Dual-lane | Outbox only when `status=emitted` **and** `delivery=l4` |
| Envelope | `record_type=finding` via `StampedRecordEnvelope` |

In-memory `tradeoff` attached for Lab / L4 tool paths is **stripped** before outbox (Prescription / card scoped).

Historical build docs that say Finding **1.1.0** are outdated for emit.

---

## How a Finding becomes L4 work

```text
Core outbox publish
  → L4 inbox / DecisionRuntime intake
  → floor checks (schema, bind, evidence, verification, detector identity when present)
  → staged graph → terminals emit | supersede | withhold | abstain
  → card-proposal only when emit allowed
```

Normative L4 side: [`../l4/15-l3-l4-interface.md`](../l4/15-l3-l4-interface.md) · [`../l4/07-finding-runtime.md`](../l4/07-finding-runtime.md) · as-built map [`../l4/30-as-built.md`](../l4/30-as-built.md).

| L3 owns | L4 owns |
| --- | --- |
| Detection methods, calculator references, verification-plan builder | Decision runtime, portfolio, card proposal |
| Dual-lane emit | Terminals; never invent ₹ |

Lab / Discovery rows never become customer cards without a new `emitted`+`l4` Finding (or a certified L4 discovery path — contract, not a Lab promote).

---

## Pivot fields L4 cares about

| Need | Why |
| --- | --- |
| Schema-valid **1.2.0** | Reject intake otherwise |
| `ops_clearance` | L5 clearance poll later |
| Impact / evidence / `dedupe_key` / engine identity | Bind and audit |
| Envelope `emitted` + `l4` | Only of-record work enters the decision runtime |

Optional intake-floor fields (`detector_id`, `detector_version`, `condition_key`, …) may appear on 1.2.0 without a schema bump — see finding.json description and `15-l3-l4-interface.md`.
