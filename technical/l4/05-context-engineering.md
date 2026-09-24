# L4 context engineering — ledger, partitions, zoom

**Status:** Architecture contract (docs).  
**Date:** 2026-09-25  
**Normative:** [`00-kernel.md`](00-kernel.md)  
**Depends on:** [`03-plant-situation-model.md`](03-plant-situation-model.md)  
**Related:** [`06-memory.md`](06-memory.md) · [`11-models-and-seams.md`](11-models-and-seams.md) · [`15-l3-l4-interface.md`](15-l3-l4-interface.md) · [ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md)

Models judge options. They do not invent plant facts, money, or evidence tiers. Context arrives as a typed ledger that code builds, zooms, and freezes. Free text may sit in a cell; it never becomes the structure.

---

## 1. Decision

**Ledger, not prose.** Every fact a model may cite is a typed row. Sources are the PSM snapshot, builder reads, memory reads, and L3 method outputs. Code assigns the evidence tier from the source type. Models may propose candidates and claims; they may not re-tier a row or invent a rupee. Money stays on the L3 calculator path.

**Why.** Unitemised narrative context is how models invent numbers, blur Measured with Modeled, and treat memory as measurement. Itemised rows with provenance make uncited claims droppable and make replay mean the same thing twice.

**Rejected.** Packing a Finding into a long prose brief; letting the model assign tiers; merging measured data with memory advice in one bag.

**Would change this.** A Pilot 1 evaluation showing that a bounded prose appendix (with hard delimiters and no money fields) raises card quality without raising uncited-claim or tier-violation rates. Until then, ledger-only.

---

## 2. Row shape

Every ledger row carries at least:

| Field | Role |
| --- | --- |
| `id` | Stable within the run; cited by claims |
| `source` | PSM element, builder read, memory read, or L3 method output |
| `effective_time` | When the fact held in the plant |
| `recorded_time` | When L4 knew it (as-known-at for the run) |
| `tier` | Assigned by **code** from `source` type — Measured, Confirmed, Modeled, Unknown, or Advisory |
| `unit` | Physical or currency unit when applicable; absent when not |
| `asset_binding` | Asset, area, resource, or plant scope |
| `polarity` | How the fact constrains or supports an option (support, oppose, bound, context-only) |
| `provenance` | Pointer into L2 / PSM / memory / L3 result ids |

Additional typed fields are allowed per source family. A row without `id` or `tier` is not admitted.

**Tier rule.** Source type → tier is a registry map under the release lockfile. Models never write `tier`. An L3 calculator result that returns a money figure remains Modeled (or the calculator’s declared tier) until verification closes against plant meters; the calculator still owns the method.

---

## 3. Partitions — never merged

Three partitions. Code keeps them separate for the whole run. Prompt sections mirror the partitions. Retrieval never folds one into another.

| Partition | Holds | May contain money? |
| --- | --- | --- |
| **measured** | PSM snapshot facts and builder reads grounded in L2 | Only if the source is calculator-owned and labeled; otherwise no |
| **advisory** | Memory reads (plant bank, case summaries, directives) | No — advisory facts point at prior outcomes; they do not reprice |
| **model** | Claims and candidates produced in this run | Only as citations to measured/calculator rows; unreferenced rupees are dropped |

**Why.** Mixing “the meter said X” with “last month we thought Y” is how plants get lied to. Advisory can inform routing; it cannot raise a Measured claim.

**Rejected.** A single ranked bullet list sorted by “relevance”.

---

## 4. Grammar always on; knowledge retrieved

**Grammar** (every prompt, every seam):

- Evidence-tier vocabulary and what each tier may support
- Units and polarity rules
- “No invented rupees” — money only via L3 calculator citations
- Hard stops (sacred constraints): metallurgy, safety, contractual, and named operational blocks
- Section rules (domain sections stay separate; never summed into one headline figure)
- Constraint-result semantics (`satisfied` | `violated` | `unknown`) — models explain; code evaluates

**Knowledge** (retrieved per case, not baked into the system prompt):

- Playbook bullets for the family / pattern
- Prior cases from the case library (summaries as advisory rows)
- Procedures and workflow recipe excerpts under the lockfile
- Mental-model answers when the owner-approved questions apply ([`06-memory.md`](06-memory.md))
- **OE knowledge corpus** hits (sourcebook / method chunks) — advisory only ([`23-oe-knowledge-corpus.md`](23-oe-knowledge-corpus.md))

Grammar is not optional per analysis. If a seam runs, grammar is present. Knowledge may be empty when nothing retrieves; emptiness is logged.

---

## 5. Zoom levels

Context starts small and deepens only on allowlisted typed reads. Models do not walk the plant graph.

```text
digest
  → area
    → resource group
      → asset neighbourhood
        → episode
          → raw series (via L2 builder read)
```

| Level | Who builds it | Typical use |
| --- | --- | --- |
| Digest | Code from PSM ([`03-plant-situation-model.md`](03-plant-situation-model.md)) | First look; scanners; hypothesis shortlist |
| Area | Builder read | Cross-asset conflict, shared utility |
| Resource group | Builder read | Feeder / compressed-air / chilled-water envelope |
| Asset neighbourhood | Builder read + propagation rules | Starve vs block, lag, buffer |
| Episode | Builder read over temporal views | Condition window, pre/post-action |
| Raw series | L2 via builder port | Verification plan signals, fine interval |

**Zoom rule.** A model requests a typed read from an allowlist. Code runs the read, appends rows to the correct partition, and logs the request as a **seam decision** (inputs, option chosen, result ids). Models never call L2 directly. Graph walk stays in the PSM builder and propagation code ([ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md)).

**Why.** Free traversal burns tokens and lets models cherry-pick. Allowlisted zooms keep the footprint honest and the trace complete.

**Rejected.** Giving the model a `graph/traverse` tool; dumping full series into every draft.

**Would change this.** Measured pass^k and cost curves showing that an extra zoom level (or a narrower allowlist) improves eligible-close quality without raising injection or stale-context incidents.

---

## 6. Sub-ledgers, budgets, freshness

Each analysis stage gets its own **sub-ledger** (slice of the run ledger): intake, draft, critique, constraint explain, portfolio note, Ask thread turn, and so on. Sub-ledgers share ids when they cite the same fact; they do not silently rewrite another stage’s rows.

**Token budgets** are per analysis and per family call, declared in the workflow recipe. When a budget binds, code truncates by partition priority: measured first, then model claims already cited, then advisory. Digest rows that carry open footprints and hard-stop constraints are last to drop.

**Freshness** is a first-class criterion, not a comment:

- Each row (or its source watermark) carries a freshness label relative to the run’s as-known-at time
- Soft gates may require a freshness margin ([`22-missed-opportunities.md`](22-missed-opportunities.md))
- Stale PSM or failed builder reads surface as degraded mode — L4 withholds or abstains rather than guessing ([`00-kernel.md`](00-kernel.md))

---

## 7. Free text is data

Logbook notes, rejection reasons, Ask answers, and owner edits may enter the ledger as delimited free-text fields on typed rows.

Rules:

1. Delimited — clear start/end markers; never interleaved into grammar sections.
2. Flagged when instruction-like (imperatives aimed at the model, “ignore previous”, tool-call shapes). Flagged text stays visible as data; the model is told it is untrusted content, not instructions.
3. Never a vehicle for money, tiers, or constraint evaluation results.
4. Promotion of free text into typed world facts or constraints requires a human path (proposed constraint row → named plant owner), not silent rewrite.

This is the prompt-injection control that matches how plants actually write notes.

---

## 8. HITL and money

L4 recommends. A named role accepts, edits, rejects, or defers. L5 records. Nothing in this document authorises equipment write or silent schedule change.

Any rupee that appears in a candidate must cite an L3 calculator (or tariff) result row in the measured partition. Dual wallets stay in separate domain sections. Unreferenced money is dropped before portfolio.

---

## 9. Failure modes the plant should expect

| Failure | What L4 does | What the plant sees |
| --- | --- | --- |
| Builder read fails / PSM stale | Withhold or abstain; trace the gap | No new card, or a deferred path if policy allows |
| Model cites a missing id | Claim dropped; if proof floor fails, withhold | No invented evidence on the card |
| Instruction-like free text | Flagged; not executed as instructions | Notes still visible to the owner as notes |
| Partition bleed attempted | Code rejects the merge | Card never carries memory as Measured |

---

## 10. v1 slice vs later

| In v1 | Later |
| --- | --- |
| Full row shape; three partitions; grammar always on | Optional bounded prose appendix if eval justifies it |
| Zoom allowlist through episode + L2 raw series | Additional zoom kinds only via registry + replay |
| Per-analysis token budgets and freshness criterion | Tuned budgets from production cost tables ([`16-operations.md`](16-operations.md)) |
| Free-text delimit + instruction-like flag | Stronger classifiers behind the same seam |
| Seam-logged zoom decisions | Jev replacement of the zoom-choice seam when a deterministic policy passes replay |

---

## 11. Links

| Doc | Why |
| --- | --- |
| [`00-kernel.md`](00-kernel.md) | Proof floor, terminals, hard stops |
| [`03-plant-situation-model.md`](03-plant-situation-model.md) | Digest and temporal views that feed the ledger |
| [`06-memory.md`](06-memory.md) | Advisory partition sources |
| [`11-models-and-seams.md`](11-models-and-seams.md) | Seam decision record for zoom |
| [`14-ask.md`](14-ask.md) | Ask uses the same ledger rules |
| [`15-l3-l4-interface.md`](15-l3-l4-interface.md) | Calculator and builder-read contracts |
| [`22-missed-opportunities.md`](22-missed-opportunities.md) | Freshness as a soft gate |
| [ADR-034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md) | Decision record |
