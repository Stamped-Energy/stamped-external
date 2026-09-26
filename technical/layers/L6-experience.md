# L6 — Experience and integration

*Status: as-built · 2026-09-26*  
*Authority:* [STAMPED_ARCHITECTURE.md](../STAMPED_ARCHITECTURE.md) §8 · [ADR-022](../../decisions/020-023/ADR-022-l6-bff-runtime-boundary.md) · [ADR-023](../../decisions/020-023/ADR-023-l6-ems-and-analyst-context.md)

L6 is the **customer control room**: one action queue, cards, close, constraints, Ask. The browser never holds upstream service keys. Home is the next action, not a monitoring dashboard product.

| Label | Meaning |
| --- | --- |
| **as-built** | `experience-integration` (Forge web + BFF) |
| **contract** | BFF composes L2 / L4 / L5 HTTP |
| **direction** | Richer export / webhook evidence surfaces |

---

## Repo

| Repo | Job | Must not |
| --- | --- | --- |
| `experience-integration` | Next.js Forge + Fastify BFF; session auth; Live / Preview honesty | Hold `L2_DATABASE_URL` or bank keys in the browser; five inboxes; summed ₹ headline; OT write |

Typical local: web `:3000` → BFF `:3001`.

---

## Surfaces

| Surface | Job |
| --- | --- |
| **Now / prescriptions / alarms** | One owner-facing queue; hide hard-gate withhold from customer |
| **Card / close** | Accept / edit / reject / defer; honest closure states |
| **Live plant / equipment** | L2 overlay when gates allow; otherwise Preview |
| **Ask** | Conversational view over L4 — does not emit cards |
| **Autonomy / constraints** | Settings UI; L2 stores constraints; autonomy default off |
| **Evidence** | Live vs Preview badges must stay honest |

Dual claim labels: **ops-confirmed ≠ bill-verified**.

---

## BFF boundary (ADR-022)

```text
Browser → BFF (cookies / stk_ keys) → L2 / L4 / L5 HTTP
```

Upstream tokens (`L2_SERVICE_KEY`, `L5_AUTH_TOKEN`, `L4_AUTH_TOKEN`) stay server-side. Fixture Auto vs live gates (`USE_FIXTURES`, `L2_LIVE`, `L5_LIVE`, `L4_LIVE`) control demos without lying about Live.

---

## Related

- Handoff: [`../../handoff/l6/stamped-l6-architecture-handoff.md`](../../handoff/l6/stamped-l6-architecture-handoff.md)
- UI charter: [`../../handoff/l6/stamped-l6-ui-ux-charter.md`](../../handoff/l6/stamped-l6-ui-ux-charter.md)
- L5 closure: [`L5-closure.md`](L5-closure.md)
