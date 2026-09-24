# Memory

**Status:** Architecture.  
**ADR:** [034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md) · [038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md)  
**Siblings:** [`05-context-engineering.md`](05-context-engineering.md) · [`13-improvement.md`](13-improvement.md) · [`14-ask.md`](14-ask.md) · [`22-missed-opportunities.md`](22-missed-opportunities.md)

---

## Purpose

Memory improves the next card without poisoning thresholds, inventing outcomes, or letting Ask chat rewrite plant truth. Each tier earns its place. When Hindsight disagrees with the case library on outcomes, the **case library wins** and the disagreement is traced.

---

## Tiers

### Working ledger (per run)

Typed rows for one DecisionCase. Frozen into the DecisionTrace, then discarded. Keeps a run bounded and replayable. Replay does not re-query Hindsight; it reads the frozen rows.

### Hindsight plant bank (per plant)

- Typed **world facts** and short **learning facts** from L5
- **Observations** with proof counts
- `observations_mission` tuned to durable operating patterns
- **Directives** mirror hard stops as a soft second layer (never a substitute for kernel hard stops)
- **Mental models:** owner-approved questions (per asset, constraint, family); refreshed content is **advisory only** and never changes a threshold or playbook

### Hindsight dialogue banks (per Ask thread)

Hard wall from the plant bank. Stated retention. Promotion to the plant bank only on **explicit confirmation** or **verified closure**. Ask does not get a second judge ([`14-ask.md`](14-ask.md)).

### Case library (episodic)

Past traces joined with L5 outcomes, retrievable by condition key, asset, family, pattern, footprint. Lives in the **L4 store**. **Authority for outcomes.**

### Negative memory

Re-proposal cooldown per condition key and pattern after reject or no-change. Lifted only by materially new evidence. Soft-gate threshold; calibrated via the opportunity ledger.

### Procedural memory

Registries, workflow recipes, analysis contracts, patterns, playbook bullets, prompts, seam thresholds — all under the **release lockfile**. Versioned like code (CoALA procedural memory).

### OE knowledge corpus (general methods — not plant memory)

Versioned document store + sparse method ontology for industrial efficiency literature (DOE sourcebooks, lean/energy toolkits, curated method cards). Retrieved into the **advisory** partition only. See [`23-oe-knowledge-corpus.md`](23-oe-knowledge-corpus.md). This is **not** Hindsight and **not** the case library: it answers “what methods exist for this class of waste,” not “what worked on this asset last Tuesday.”

### Not in v1: cross-plant priors

Designed as a future seam (anonymised, owner-approved bullets). Transfer validity and privacy cannot be judged from one pilot plant.

---

## Rules

| Rule | Detail |
| --- | --- |
| Ineligible close | Outcome set to **null** — does not count as success or failure for proof |
| Proof counts | Only **independent eligible closures** across shifts and dates |
| Selection bias | Outcomes exist only for proposed actions; closure rate alone never ranks patterns |
| Bias correction | Opportunity ledger + exploration outcomes (`exploration=true`) stored alongside ordinary closures |
| Version / epoch change | Memory re-keyed or quarantined when detector/pattern version, asset epoch, or Hindsight version changes |
| Replay | Every memory read frozen as ledger rows |
| Domain tags | Use **domain registry ids** so a new domain gets its own scope without re-tagging |

---

## What memory must not do

- Change hard gates, money ownership, or write bans
- Promote playbook / prompt / threshold / model pin without lockfile + owner path
- Accept free chat into the plant bank
- Treat an unverified close as a high-proof “action works here”

---

## Improvement link

Plant bank learning facts and case-library outcomes feed the offline council ([`13-improvement.md`](13-improvement.md)). Soft-gate blocks feed the opportunity ledger ([`22-missed-opportunities.md`](22-missed-opportunities.md)). That is half of how the system improves: learning from what it said no to.

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Working ledger + Hindsight plant/dialogue banks + case library + negative memory + procedural lockfile | Same tiers |
| Cross-plant priors | Not in v1; designed as future seam |
| Mental-model questions owner-gated; content advisory | Same |
| Opportunity-ledger linkage for selection-bias correction | Full calibration scorecards in ops |
