# 14. Ask

**Status:** Architecture.  
**Authority:** [STAMPED_ARCHITECTURE](../STAMPED_ARCHITECTURE.md) §6 · [ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md) · [ADR-033](../../decisions/033-039/ADR-033-l4-decision-runtime.md)  
**Siblings:** [`00-kernel.md`](00-kernel.md) · [`05-context-engineering.md`](05-context-engineering.md) · [`06-memory.md`](06-memory.md) · [`11-models-and-seams.md`](11-models-and-seams.md)

Ask is a **view over L4**, not a second product. Same plant picture, same evidence rules, same hard stops. Chat does not get a back door past the kernel.

L6 paints the thread; L4 owns the session and tools.

---

## 1. Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Product shape | One decision loop. Ask reads PSM, memory, case library, and open-card state — it does not emit cards |
| 2 | Session owner | L4 holds the Ask session; L6 renders |
| 3 | Dialogue banks | Per-thread Hindsight dialogue bank; **hard-walled** from the plant bank and from other threads |
| 4 | Promotion | Thread content enters the plant bank **only** on explicit confirm or verified closure |
| 5 | Tools | **No write tools** — no equipment, schedule, master data, autonomy, or card emit |
| 6 | Evidence | Same ledger citation rules; rupees only from L3 calculator references; uncited claims dropped |
| 7 | Discovery | Ask may **request** a discovery run; it may not bypass grounding or gates |
| 8 | Seams | `ask_intent_routing` and `ask_answer_framing` are LLM-only until Jev beats them |

---

## 2. Why

Operators will ask “what’s going on on feeder 3?” before they accept a card. If Ask invents a second brain with looser rules, they will trust the chat and ignore the card — or the reverse. One brain, two surfaces.

Dialogue must not silently become operating truth. Shift jokes, hypotheticals, and incomplete stories stay in the thread until a human confirms or a verified close produces a short learning fact.

HITL: Ask informs; the named owner still accepts cards and confirms promotions.

---

## 3. Rules

| Rule | Detail |
| --- | --- |
| Same evidence rules | Claims cite ledger rows; no invented rupees; tiers assigned by code |
| No write tools | Same write ban as the decision runtime |
| Dialogue banks | Per-thread Hindsight dialogue bank; **hard wall** from the plant bank |
| Promotion | Dialogue → plant bank only on explicit confirmation or verified closure |
| No second terminal | Ask does not emit / supersede / withhold cards; the decision runtime does |
| Grammar always on | Units, comparison bans, hard-stop language from the always-on contract |
| Case library wins | Dialogue memory is never outcome authority |

---

## 4. What Ask may do

| Allowed | How |
| --- | --- |
| Explain plant state | Typed reads over PSM digest / zoom; frozen into an Ask ledger for the turn |
| Explain an open or closed card | Case library + trace slots (observed → outcome) |
| Compare alternatives | Only with L3 calculator / simulator citations; Modeled labeled |
| Request a discovery sweep | Enqueues the normal discovery path; results still need grounding |
| Cite constraints | Code-evaluated results; Ask explains, does not re-judge |
| Draft a clarification for the owner | Text only — no side effects |
| Refuse | Hard stops, unknown hard constraints, missing proof — say so plainly |

---

## 5. What Ask must not do

| Forbidden | Reason |
| --- | --- |
| Emit / supersede / withhold as a chat side effect | Cards go through Finding / discovery → portfolio → kernel |
| Change or enable autonomy classes | L5 + named owner |
| Write equipment, setpoints, schedules, quality holds, master data | Kernel hard stop |
| Assign the on-shift person | L5 resolves role → person |
| Promote dialogue → plant bank without confirm / verified closure | Memory hard wall |
| Invent ₹ or evidence tiers | Calculator and code own those |
| Cross-query other threads’ dialogue banks | Hard wall |
| Bypass portfolio or attention hold | Portfolio stays authoritative |
| Accept a constraint override because a chat thread “agreed” | Constraints are code |
| Become the home screen instead of the card queue | L6 product rule |
| Call Opus / Sol on the plant Ask path | Offline council only |

---

## 6. Memory walls

```text
Plant bank     ← world facts + short learning facts (eligible closes)
Dialogue bank  ← this Ask thread only (stable document id)
Case library   ← traces + outcomes (authority when banks disagree)
```

| Rule | Detail |
| --- | --- |
| Hard wall | Hindsight has no cross-bank query. L4 may merge **reads** for an answer; it does not merge stores |
| Retention | Dialogue retention stated per deployment; expiry does not copy into the plant bank |
| Promotion | Explicit user confirm (“save this as plant fact”) or verified closure learning fact — both audited |
| Rejection | Declined promotions remembered; no re-nag without new evidence |

Mental-model questions stay owner-approved. Ask may draft a suggested update; it does not pin it ([`13-improvement.md`](13-improvement.md)).

---

## 7. Evidence rules (same as card path)

1. Build a turn ledger from allowlisted reads (PSM, L2 builder reads, case library, open cards, L3 tools as needed).  
2. Partition measured / advisory / model — never merge into one undifferentiated blob.  
3. Every factual claim cites a ledger row id.  
4. Money only via L3 calculator reference.  
5. Free text from the user is delimited data; instruction-like user text is flagged and not treated as policy.  
6. Trace the turn (Ask subset of DecisionTrace): intent seam, reads, framing seam, citations, refusals.

Disagreement on framing is a routing-class seam → registry default. Ask never uses disagreement to invent an action for the floor.

---

## 8. Intent routing and answer framing

| Seam | Job |
| --- | --- |
| `ask_intent_routing` | Map utterance → allowlisted read plan / refuse / suggest card queue |
| `ask_answer_framing` | Order evidence, label tiers, refuse out-of-scope asks |

Both are closed-option seams ([`11-models-and-seams.md`](11-models-and-seams.md)). Both stay LLM-only until replacement beats the seam decision records.

Ask may use the plant runtime pair under the same dual-family / one-family rules, or a designated Ask slot in the model-pin registry. Offline council models stay offline.

Latency: prefer digest-level answers first; zoom only on request or when proof obligations require it.

---

## 9. Relationship to cards and discovery

| Situation | Behavior |
| --- | --- |
| User asks about a live card | Read-only explanation from L5 state + trace |
| User wants “make this a card” | Point to promotion / backlog / normal emit path — Ask does not emit |
| Soft-gate backlog item | Owner may promote via backlog UI; Ask can explain the gate in plain words |
| Discovery request | Runs scanners + methods under normal caps; hypothesis lane still needs plant opt-in and dual-family agreement |

---

## 10. Rejected alternatives

| Alternative | Why rejected |
| --- | --- |
| Ask as a separate agent product | Two brains; split trust; doubled governance |
| Soft write tools “just for notes” | Notes become de-facto setpoints without audit |
| Auto-promote chat summaries nightly | Contaminates plant bank with unverified talk |
| Weaker evidence rules in chat | Operators will prefer the looser path |
| Council models answering Ask live | Wrong path; cost and improvement contamination |

---

## 11. Evidence that would change this

- Owners need a supervised “create draft card from this thread” → add an explicit **draft proposal** that still runs full kernel checks (contract delta; still not a silent emit).  
- Dialogue promotion too rare → improve confirm UX; do not auto-promote.  
- Intent routing error rate high under pass^k → tighten closed intents or add Jev when records exist.

---

## 12. v1 slice vs later

| v1 | Later |
| --- | --- |
| Read-only Ask over PSM + cards + case library | Richer zoom tools; same walls |
| Manual confirm to promote facts | Same HITL; better “what would be saved” preview |
| Discovery request = enqueue sweep | Optional draft-card-from-thread under full gates |
| LLM intent / framing seams | Jev on high-volume intents when earned |
