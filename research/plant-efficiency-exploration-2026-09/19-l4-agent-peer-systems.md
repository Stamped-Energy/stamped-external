# L4 agent peer systems and literature

**Date:** 2026-09-25  
**Status:** Research for the L4 architecture set. Not an implementation.  
**Authority:** [`09-stamped-founder-vision.md`](09-stamped-founder-vision.md) wins on conflict. Architecture shape: [`../../technical/l4/README.md`](../../technical/l4/README.md).  
**Confidence:** **High** = vendor page, paper, or public repo. **Medium** = consistent secondary account. **Low** = thin public record. Vendor performance numbers are vendor claims, not measurements.

This note extends [`12-peer-architecture-patterns.md`](12-peer-architecture-patterns.md). Prefer this file for L4 agent design; keep `12` for the earlier adopt / adapt / reject map.

---

## 1. What this research answers

L4 turns plant conditions into one owned card proposal. It must reason across the plant (constraints, shared utilities, open cards), keep memory honest, and improve from closures — including what it blocked. This note records what public industrial systems and agent literature actually show, and which mechanisms Stamped adopts.

---

## 2. Six industrial peers

### 2.1 Noetive

**High** (site, seed note): a “brain” that learns how the operation runs, paired with multi-modal sensing pods, integrated on tools people already use. Meant to get more capable through deployment.  
**Medium** (investor write-ups): a real-time digital twin as the only surface agents touch; self-improving agents via memory, distillation, and post-training; orchestration across humans, robots, and software.  
**Low** on the actual training loop. Founded 2026.

| Keep | Leave |
| --- | --- |
| Whole-operation check before a local action; cause-and-effect memory updated from outcomes | Sensing pods; schedule republish; any claim that Stamped runs the plant |

Self-improvement here is Hindsight observations + replay + owner-gated playbook deltas — not silent weight post-training on raw closures.

### 2.2 XMPro MAGS

**High** (product pages, [public agent repo](https://github.com/XMPro/Multi-Agent)): each specialist runs Observe → Reflect → Plan → Act with its own objective, constraints, tools, and memory. Not every observation becomes a plan. A Decision Trace records observed, context, action, policy, approval, and outcome. Grammar (units, naming, comparison bans) stays in the always-on contract; procedures are retrieved. Cognitive processing stays isolated from physical execution.

| Keep | Leave |
| --- | --- |
| Grammar always on; selective cognition; six-slot decision trace | Voting bus; multi-round debate that hides the single-owner decision |

### 2.3 Decisyon

**High** (current site): App Composer scaffolds data, pages, workflows, and agents. Named agents each bind to a different source of truth and track action to close. Older DAC material is visual composition and edge rules, not a cognitive loop.

| Keep | Leave |
| --- | --- |
| One coordination loop over different truths, then a tracked close | Becoming an app composer or a second plant UI |

### 2.4 Sight Machine

**High** (2026 platform pages): agents reason after tags, assets, processes, and KPIs are mapped. Experts approve mappings. Every signal has provenance. Crews can write reusable analysis tools and speak MCP. Factory Copilot kept the model on language and the platform on data.

| Keep | Leave |
| --- | --- |
| Provenance before a recommendation; model does language, platform owns facts | Line-wide semantic program before one decision; agent-authored production apps; progressive equipment authority |

### 2.5 Tulip

**High** (support docs, 2025–2026): an agent is a goal, instructions, and an explicit tool list. It cannot raise the caller’s permissions. Their build guide: extra tools create extra wrong paths; evaluate with a prompt / expected / actual / pass-fail table. A plant-outcome learning loop is not disclosed.

| Keep | Leave |
| --- | --- |
| Least privilege per analysis; replay table as improvement harness | Read-write on plant tables |

### 2.6 Augury

**High** (2026 workforce notes): an Industrial Context Graph joins machine signals with process and operations. Role agents recommend; a person approves the work order.  
**Medium:** public closure reference is still “work order, then a later healthy-state check.”

| Keep | Leave |
| --- | --- |
| Neighboring signals before a local action; teach from a verified after-state | Setpoint writes; machine-health product claim |

Proof count measures repetition, not truth. An unverified close must not become a high-proof observation that the action worked.

### 2.7 Mechanisms the six do not publish (still needed)

| Source | Mechanism | Confidence | Stamped use |
| --- | --- | --- | --- |
| Cognite Atlas | Side-effecting tool returns typed confirmation; client allow/deny | High | L4 has no write. Extra reads are typed requests; code runs them only if allowlisted |
| Palantir action types | Declarative submission criteria over parameters and object state | High | L4 judge is a versioned criteria list, not prompt branches |
| Seeq | Time-bounded conditions are first-class; each node controls how much upstream output it sees | High | Condition key is the object; each analysis sees a sub-ledger |

---

## 3. Agent literature (2024–2026)

### 3.1 Workflows beat free agents when steps are knowable

Anthropic’s [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) (**High**): a workflow runs models and tools on code-owned paths; an agent lets the model steer. Orchestrator-workers and evaluator-optimizer are still workflows — code owns joining and stopping.

Their [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) (**High**, internal benchmark): gains came mostly from separate context windows, not personas voting. Subagents need an explicit objective, output schema, tool boundary, and stop.

MAST (Cemri et al., NeurIPS 2025, [arxiv](https://arxiv.org/abs/2503.13657)) (**High**): across 1,600+ traces, multi-agent failures cluster into bad specifications, lost information between agents, and weak verification. Better base models do not fix that.

τ-bench ([arxiv](https://arxiv.org/abs/2406.12045)) (**High**): pass^k (succeed on all k reruns) collapses far below pass^1. A card whose terminal flips across reruns of the same ledger is a defect.

**Adopt:** outer graph is code. Models judge inside steps. They do not choose when the run ends. Replay measures pass^k.

### 3.2 Debate and self-correction are the wrong inner loop

Du et al. (ICML 2024) showed multi-instance critique can raise factuality on some tasks. Later work qualifies that:

- Smit et al., “Should we be going MAD?” (ICML 2024): debate did not reliably beat self-consistency.
- “Debate or Vote” (NeurIPS 2025): most of the measured gain is the vote over independent samples, not the exchange.
- “Talk Isn’t Always Cheap” ([arxiv](https://arxiv.org/pdf/2509.05396)): agents flip from a correct answer to agree with a peer. On CommonSenseQA, debate hurt.
- Controlled logical-reasoning study ([arxiv](https://arxiv.org/html/2511.07784v1)): ceiling is the strongest participant’s reasoning. Eloquent-but-wrong arguments sway the group.
- Khan et al. (ICML 2024): a critic helps when it cites **verified** evidence the judge can check.

Huang et al., ICLR 2024 ([arxiv](https://arxiv.org/abs/2310.01798)) (**High**): a model correcting itself with no outside signal often gets worse.

**Adopt:** independent samples from two model families; critic must cite ledger ids; one revision only for objections whose citations resolve. No multi-round debate. No vote.

### 3.3 Judges are biased; agreement is a signal, not proof

- LLM-as-judge ([Zheng et al.](https://arxiv.org/abs/2306.05685)): order, verbosity, and self-preference move scores.
- Panickssery et al.: judges prefer their own family’s outputs. Verga et al. (PoLL): a panel from different families reduces that. Averaging scores lets one bad judge pull the mean.
- Conformal abstention (Yadkori et al., 2024): agreement can be calibrated into abstention — it cannot catch an error both models share.
- Lightman et al., “Let’s Verify Step by Step”: process labels beat outcome-only labels for training a verifier. Plant closures are sparse, delayed, and confounded — label the trace step, not only “the card closed.”

**Adopt:** critic is the other family, author hidden. Code never averages model scores into a gate. Card uncertainty comes from evidence tier, freshness, and whether the two families picked the same action template.

### 3.4 Self-improvement that does not collapse the prompt

- ACE (ICLR 2026, [arxiv](https://arxiv.org/abs/2510.04618)) (**High** on their benchmarks): context as itemised bullets with helpful/harmful counters. Generator → reflector → curator emits add/update/remove. **Deterministic code** merges. Full rewrites cause brevity bias and context collapse.
- GEPA ([arxiv](https://arxiv.org/abs/2507.19457)) (**Medium–High**): trace-driven prompt evolution; Pareto frontier of candidates.
- CoALA: playbooks and registries are **procedural** memory — versioned like code, not chat facts.
- Memory poisoning (AgentPoison, MINJA): a tiny poisoned fraction of a store can dominate later retrieval. Dialogue bank stays a hard wall. Plant bank accepts only typed learning facts from L5.

**Adopt:** month-12 quality is a versioned playbook and prompt set, proposed by one model, red-teamed by the other, replayed on holdouts, shadowed, then accepted by a named owner. Weight post-training of the generator waits until clean step labels exist.

### 3.5 Plant-wide methods

| Method | Source | Use in L4 |
| --- | --- | --- |
| Shifting bottleneck / active-period / blocked-starved | Roser et al. | PSM temporal views; discovery system methods |
| Compressed air / chilled water as supply-demand systems | DOE sourcebooks | Shared-resource scanners; not component-only opportunities |
| Precedence, no-overlap, cumulative capacity | OR-Tools / RCPSP surveys | Typed constraint kinds evaluated by code |
| Bitemporal history | Fowler | PSM snapshots are as-known-at |
| Time-bounded conditions | Seeq capsules | State episodes in the PSM |
| Simulation credibility | NIST twin guidance | L3 methods need intended-use envelope; out-of-envelope cannot support emit |

---

## 4. Dual-model reviews and resolutions

Runtime critique: [Opus 5.5](5abcb111-da7c-4aad-9999-6a052af71d15), [GPT-5.6 Sol](485ba155-8f8c-499c-b2a8-38c7edf92c85).  
Plan critique: [Opus 5.5](f70307de-51f5-4168-8f97-3b99f4b2c9f0), [GPT-5.6 Sol](83b287db-9338-41ee-af44-c5836bb40d1f).

| Disagreement | Resolution |
| --- | --- |
| Who routes mandatory analyses | Code + family registry. Models do not invent stages |
| Unknown family: abstain vs investigate | Investigate; emit only when obligations and both families agree. Uncertified detector versions are shadow |
| One draft vs candidate beam | Each plant model family drafts two candidates; reconciler selects only from that set |
| What “judge” means | Code runs submission criteria; other family does semantic entailment with cited objections |
| Template lane | Certified fast path when applicability predicate holds; escape to investigative on conflict |
| Topology source | Site-pack topology published L1→L2 (not L4-only config) |
| LLM discovery emit | Certified patterns emit; gated grounded-hypothesis lane (owner opt-in) for LLM hypotheses |
| L4 storage | L4 operational store for derived data; L2 remains plant source of truth |
| Soft-gate strictness | Opportunity ledger + owner backlog + opt-in exploration; calibrate soft gates both ways |

---

## 5. What Stamped does not copy

- Multi-round debate, specialist voting, averaged model scores as a gate.
- A free agent that owns tool calls and termination.
- Self-refinement with no outside signal.
- An LLM as the terminal judge or as the constraint evaluator.
- Model self-reported confidence as the card’s uncertainty.
- Monolithic rewrites of playbooks.
- Generator post-training on raw closures.
- Plant-wide ontology as a prerequisite; agent-written production apps; MCP as a product surface.
- Equipment write, schedule publish, setpoint push.

---

## 6. Sources (selected)

Industrial: Noetive site and seed notes; XMPro MAGS pages and GitHub Multi-Agent docs; Decisyon AI Agents / App Composer; Sight Machine semantic model and agentic platform pages; Tulip AI Agents support docs; Augury Industrial AI Workforce notes; Cognite Atlas AI docs; Palantir Foundry action types; Seeq data model docs.

Papers and engineering: Anthropic building-effective-agents; MAST (2503.13657); τ-bench (2406.12045); Huang self-correction (2310.01798); ACE (2510.04618); GEPA (2507.19457); “Talk Isn’t Always Cheap” (2509.05396); Lightman process supervision (2305.20050).

Plant methods: Roser bottleneck work; DOE compressed-air and chilled-water sourcebooks; NIST digital-twin credibility guidance; Fowler bitemporal history.

---

## 7. What would change this note

New public technical detail from Noetive’s training loop; a peer publishing a verified closed-loop learning path with eligible / ineligible outcomes; a paper showing multi-round debate reliably beats independent dual-family sampling on industrial decision tasks with cited evidence constraints.
