# L4 architecture gap audit — agentic stack + industrial hardness

**Date:** 2026-09-25  
**Status:** Audit + closure map. Gaps below were open; **must-have / should-have production items are now specified** in docs `25`–`29` and [ADR-040](../../decisions/040-044/ADR-040-l4-production-hardness.md).  
**Already closed earlier:** OE literature RAG ([`23-oe-knowledge-corpus.md`](23-oe-knowledge-corpus.md)).

---

## Closure map

| Former gap | Now specified in |
| --- | --- |
| Work queue / concurrency | [`25-work-queue-and-concurrency.md`](25-work-queue-and-concurrency.md) |
| DecisionCase lifecycle | [`26-decision-case-lifecycle.md`](26-decision-case-lifecycle.md) |
| Port failures / idempotency / breakers | [`27-ports-and-reliability.md`](27-ports-and-reliability.md) |
| Token-budget required proof | [`26`](26-decision-case-lifecycle.md) § token budget |
| Commissioning / safe-start | [`28-commissioning-and-controls.md`](28-commissioning-and-controls.md) |
| Kill switch / control plane | [`28`](28-commissioning-and-controls.md) |
| OE corpus ops + offline privacy | [`28`](28-commissioning-and-controls.md) |
| Observability SLOs / store durability / CI suites | [`29-software-quality-and-release.md`](29-software-quality-and-release.md) · [`16-operations.md`](16-operations.md) |

---

## Still later (conscious deferrals — not silent holes)

- Cross-plant priors  
- OE Tier B/C (licensed books, plant SOPs) under license  
- Ask Adaptive Router / heavy GraphRAG on Ask  
- Multi-region HA / chaos topology  
- Automated error-budget auto-block of pins  
- Area-scoped `emit_enabled`  

---

## Not missing (do not reopen)

Kernel integrity, dual-family seams, PSM, discovery/shift sweep, opportunity ledger, HITL, money/write bans, OE advisory corpus — see original audit criteria in git history of this file / README eight ideas.

---

## Implementer rule

Before first production `emit_enabled=true`, stamped-l4 must implement **kernel + `25`–`29`**, not kernel alone. ADR-040 is the lock.
