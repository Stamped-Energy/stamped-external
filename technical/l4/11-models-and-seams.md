# 11. Models and seams

**Status:** Architecture.  
**ADR:** [036](../../decisions/033-039/ADR-036-dual-family-models.md) · [033](../../decisions/033-039/ADR-033-l4-decision-runtime.md)  
**Siblings:** [`00-kernel.md`](00-kernel.md) · [`12-trace-and-eval.md`](12-trace-and-eval.md) · [`13-improvement.md`](13-improvement.md)

L4 puts models inside named seams. Code owns the stage graph, money references, constraint evaluation, and terminals. A human owns the plant action. The model never runs the floor.

Amends research `14` / `15`: disagreement on action-affecting seams **withholds** — it does not fall back to a generative agent.

---

## 1. Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Plant runtime pair | Provider-agnostic dual-family slot. Default: **DeepSeek V4.1 Flash** (`deepseek-flash`) + **GPT-5.6 Luna** |
| 2 | Hosting | Hosted API or self-hosted open weights — same slot contract |
| 3 | Pro upgrade | DeepSeek V4.1 Pro replaces Flash in its family slot when released, **via replay** — not a silent pin |
| 4 | One-family mode | Two correlated samples, **stricter** numeric thresholds, grounded-hypothesis lane **off** |
| 5 | Offline council | **Opus 5.5** + **GPT-5.6 Sol** — never on the plant request path |
| 6 | Confidence | Cross-family **agreement**, calibrated against outcomes — not a model self-score |
| 7 | Disagreement | Action / owner / constraint / verification / terminal → **withhold**. Routing → **registry default** |
| 8 | Seam contract | Typed features, closed options from registries, structured output, seam decision record, Jev route |
| 9 | v1 seams | Every catalog row is **LLM-only** until a classifier / Jev candidate beats the logged set under replay |

---

## 2. Why

Single-model drafting correlates mistakes. Same-family judges prefer their own drafts. Two families drafting blind, then one cited critique pass, catches a bad route without a debate club on the shift.

Plant latency and cost belong on Flash + Luna. Offline critique belongs on Opus + Sol. Mixing those paths slows cards and contaminates improvement.

When families disagree on who owns the action or what to do, the honest terminal is **withhold**. Staff see the trace; the floor does not get a coin-flip card.

---

## 3. Plant runtime slots

### Dual-family default

```text
Family A slot  →  deepseek-flash   (DeepSeek V4.1 Flash)
Family B slot  →  gpt-5.6-luna     (GPT-5.6 Luna)
```

Pins live in the release lockfile. Providers are adapters behind `ModelSlot`. Application code asks for family A / B, not a vendor name.

### Pro upgrade path

1. Pin Pro as a **candidate** in family A.  
2. Replay holdouts and verified-closure suites against Flash.  
3. Shadow on an opted-in plant.  
4. Tech lead proposes the global pin; **each plant’s named owner** accepts (or has opted in to automatic acceptance of global model pins).  
5. Unpin Flash for that plant scope.

### One-family mode

| Rule | Behavior |
| --- | --- |
| Samples | Two correlated draws from the one family |
| Thresholds | Stricter than dual-family (registry placeholders until Pilot 1 calibrates) |
| Hypothesis lane | Off — that lane needs independent family agreement |
| Label | Trace records `model_mode=one_family` |

### Offline council (not plant path)

Opus 5.5 and GPT-5.6 Sol label traces and propose playbook / prompt / threshold deltas. They do **not** draft live candidates, fill live seams, or answer Ask on the floor. See [`13-improvement.md`](13-improvement.md).

---

## 4. Seam contract

A **seam** is a closed choice the runtime must make. v1 fills it with structured LLM output. Later, Jev (or a trained classifier) may replace the LLM only after it beats the logged set.

| Piece | Rule |
| --- | --- |
| Typed features | Schema of inputs (ledger ids, registry ids, scores code already computed). Free-text plant narrative only if delimited and flagged |
| Closed options | Enum from registries (domains, families, workflows, patterns, roles). New domain → new option, no seam code change |
| Structured output | One option id (or small fixed struct). Unparseable → disagreement / withhold per policy |
| Cross-family agreement | Both families fill blind; agreement is the confidence signal |
| Calibration | Agreement vs later outcomes measured per `seam_id` |
| Seam decision record | Logged every fill — training and comparison set for Jev |

### Seam decision record

`seam_id` / version · features (hash + payload ref) · options · `choice_family_a` / `choice_family_b` · final action · disagreement branch · `release_lockfile_hash` · later outcome join.

### Disagreement policy

| Seam class | On disagreement |
| --- | --- |
| Action, owner role, constraint subset (selection), verification bound, terminal (withhold vs abstain) | **Withhold** |
| Routing (workflow route, optional analysis, pattern routing, Ask intent, latency tier, …) | **Registry default** |

Code still owns emit. A seam never overrides a hard gate.

### Never a seam (stays deterministic)

Constraint evaluation (all intersecting hard rows), evidence tier, freshness past the hard limit, money / calculator numbers, schema validity, footprint overlap / one-card dedupe, attention-budget hold when over cap, re-proposal cooldown enforcement, autonomy class from action-template registry, code-rubric orderings.

---

## 5. Seam catalog (Jev replacement rows)

Every row is **LLM-only** in v1. Status flips only after replay proves a replacement (declared min record count + holdout metric per seam in ops).

**Typed features (per seam):** each seam reads only the feature schema named in the “Features” column. Free plant narrative is never a feature unless delimited and flagged. Seams must not see other families’ private scratch.

| Seam id | Closed choice | Features (typed) | Options from | Disagreement | Jev status |
| --- | --- | --- | --- | --- | --- |
| `workflow_route` | Fast vs investigative | family_id, plant_id, proof_flags, certified_recipe_bool | Workflow registry | Registry default | LLM-only until Jev beats it |
| `optional_analysis` | Extra analyses beyond mandatory | domain_ids_admitted, proof_obligations | Domain registry | Registry default | LLM-only until Jev beats it |
| `secondary_domain` | Optional secondary section ids | primary_domain, claim_kinds_present | Domain registry | Withhold if changes claim set; else default | LLM-only until Jev beats it |
| `owner_role` | Proposed owner role | action_template_id, domain_id, footprint_roles | Role registry | **Withhold** (hard) | LLM-only until Jev beats it |
| `cross_section_conflict` | Attach note / withhold / request evidence | cross_section_facts, open_footprints | Fixed enum | **Withhold** (hard) | LLM-only until Jev beats it |
| `constraint_add` | Which **extra** advisory rows to evaluate | constraint_index_ids, footprint | Constraint index | Registry default | LLM-only until Jev beats it |
| `l3_method_choice` | Which L3 method / simulator | candidate_template, methods_admitted | L3 methods registry | Registry default | LLM-only until Jev beats it |
| `simulate_vs_evidence` | Simulator vs evidence-only | method_envelope_ok | Fixed enum | Registry default | LLM-only until Jev beats it |
| `verification_method` | Among builder-offered options | builder_options | Builder output | **Withhold** (hard) | LLM-only until Jev beats it |
| `verification_bound_tighten` | Whether / how to narrow | source_plan_bounds | Builder envelope | **Withhold** (hard) | LLM-only until Jev beats it |
| `context_zoom` | Next typed read / zoom | zoom_allowlist, token_budget_left | Allowlisted reads | Registry default | LLM-only until Jev beats it |
| `historical_analogue` | Apply or skip retrieved case | case_ids, similarity_features | Case library ids | Registry default | LLM-only until Jev beats it |
| `candidate_selection` | Preferred drafted candidate | candidate_ids, citation_ok flags | Candidate ids | **Withhold** (hard) | LLM-only until Jev beats it |
| `alternatives_include` | Which alternatives ship (incl. no-action) | candidate_set | Candidate set | **Withhold** (hard) | LLM-only until Jev beats it |
| `terminal_withhold_abstain` | Withhold vs abstain when emit blocked | block_reasons | Fixed enum | **Withhold** (hard) | LLM-only until Jev beats it |
| `discovery_triage` | Promote / shadow / drop | scanner_score, pattern_id | Fixed enum | Default for routing; withhold if emit-bound | LLM-only until Jev beats it |
| `pattern_routing` | Which certified pattern | scanner_hits | Pattern registry | Registry default | LLM-only until Jev beats it |
| `portfolio_conflict_action` | Prefer A / prefer B / hold both / request evidence | footprints, rank_keys | Fixed enum (code filters illegal “keep two open cards”) | **Withhold** (hard) | LLM-only until Jev beats it |
| `supersede_vs_new` | Supersede vs new card | prior_acceptance_state, better_candidate_bool | Fixed enum (code filters: if accepted → only new/conflict) | **Withhold** (hard) | LLM-only until Jev beats it |
| `latency_tier` | Exception / flow / energy-cost | domain_id, exception_flag | Latency registry | Registry default (cannot grant attention exempt) | LLM-only until Jev beats it |
| `ask_intent_routing` | Ask read plan / refuse | ask_utterance_features | Ask intent registry | Registry default | LLM-only until Jev beats it |
| `ask_answer_framing` | Evidence order / what to refuse | ledger_partition_ids | Framing templates | Registry default; never invents ₹ | LLM-only until Jev beats it |
| `oe_retrieval_mission` | Which OE corpus mission / filters | scenario_class, domain_id | Mission registry | Registry default | LLM-only until Jev beats it |

**Removed from seams (deterministic code):** `autonomy_class_label` (from action-template registry); `constraint_subset` omit path (code always evaluates intersecting hard rows; seam is add-only as `constraint_add`); `merge_vs_keep_both` (one-card dedupe); `hold_vs_send_budget` (over budget → hold); `repropose_vs_suppress` (cooldown gate).

One-family mode: two samples disagreeing on an action-affecting seam → **withhold** (`action_seam_disagreement`).

---

## 6. Rejected alternatives

| Alternative | Why rejected |
| --- | --- |
| Single plant model with self-critique | Correlated error; self-scores are not gates |
| Averaging model confidence into a blend | Hides disagreement |
| Opus / Sol on the live plant path | Latency, cost, wrong incentives |
| Soft fallback to generative agent on low confidence | Amends `14`/`15` |
| Open-ended free-text “decision” | Cannot calibrate; cannot replace with Jev |
| Silent weight post-training on raw closures | See [`13-improvement.md`](13-improvement.md) |

---

## 7. Evidence that would change this

- Dual-family agreement anti-correlates with verified closures on a seam → revisit agreement-as-confidence for that seam.  
- One-family miss rates match dual-family at stricter thresholds → allow hypothesis lane under extra hard gates (needs ADR).  
- Jev / classifier beats LLM on holdout seam records with no rise in constraint miss or nuisance → flip that row.  
- Flash→Pro replay fails → keep Flash.

---

## 8. v1 slice vs later

| v1 | Later |
| --- | --- |
| Dual-family default; one-family mode | Per-seam calibrated thresholds from site data |
| Full catalog as LLM-only | First Jev swaps on high-volume routing seams |
| Placeholder one-family thresholds | Measured from opportunity ledger ([ADR-038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md)) |
| Opus / Sol offline only | Same — do not migrate onto plant path |
| Pro upgrade path documented | Execute when Pro exists and replay passes |
