# ADR-029: Manual perception pipeline, compile attempts, credibility, prompt cache

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-08-20 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-028](ADR-028-dual-plant-graphs-and-path-d.md) · [ADR-017](../016-020/ADR-017-l4-adaptive-retrieval-and-web-trust.md) · [ADR-015](../016-020/ADR-015-l3-dual-lane-lab-detections.md) · [ADR-019](../016-020/ADR-019-l5-runtime-and-consistency.md) · [ADR-022](../020-023/ADR-022-l6-bff-runtime-boundary.md) · [`l4-compile-trace.json`](../../contracts/schemas/intelligence/l4-compile-trace.json) |

---

## Context

Staff need a single L5 internal-console action that runs a fresh L3 hot detection cycle on current plant data, compiles every emitted Finding through the ADR-028 quality path, and shows every outcome — including `withhold` / `abstain` — with transparent credibility. Today:

- L3 has `run_hot_path` + outbox but no detection-run API or L4 relay.
- L4 does not emit compile traces for non-emits (`prescription_id` was required).
- Reflection is a single Lane-B claim repair, not a judge loop with optional Path H expansion.
- L6 can still surface `blocked` as a customer lane.

OpenAI and DeepSeek prompt caching reward byte-stable prefixes; the quality loop must not bust cache by putting plant/run volatility ahead of stable instructions.

## Decision

1. **Staff-only manual pipeline.** L5 `POST /v1/internal/plants/{plantId}/pipeline/runs` creates a `pipeline_run` (`write:admin`, actor + reason + idempotency key, one active run per plant). L5 orchestrates correlation only. L3 owns detection; L4 owns compile; L5 owns staff visibility and prescription workflow. Never expose on L6.

2. **L3 detection-run API.** `POST /v1/internal/detection-runs` queues a hot path with `org_id`, `plant_id`, `as_of`, `pipeline_run_id`. Engines use declared rolling lookbacks (no hard-coded demo windows). Outbox envelopes include `delivery=l4` ∧ `status=emitted` at the producer. An at-least-once relay POSTs to L4 `/v1/jobs/inbox`. Finding business `dedupe_key` is preserved; `pipeline_run_id` correlates attempts.

3. **Compile attempt ≠ Prescription.** Every quality-path invocation produces an `l4-compile-trace` (aka compile attempt) with `terminal ∈ {emit, withhold, abstain}` (plus rejected/failed as L5-side attempt statuses). `prescription_id` is **required only when `terminal.status = emit`**. L5 stores all attempts append-only. Only emit → L5 prescription ingest → customer-visible workflow after gates.

4. **Bounded reflection with Path H.** Judge actions: `pass` | `rewrite` | `retrieve_more` | `abstain`. Initial Path H is mandatory. At most **two** targeted Path H expansions. Default `max_generation_calls = 12`. No open web on the Rx path. Deterministic verify/veto cannot be repaired away. Graph A/B + Path D freeze for the compile; only document context expands.

5. **Credibility (staff).** Band `high|medium|low|insufficient` plus a documented 0–100 operational heuristic (not a statistical probability). Components: Finding confidence, bind quality, Graph B freshness, evidence coverage, Path H trust tier, verify/veto, practicality scores. Failed bind / stale required live data / verify fail / veto → `insufficient`. Bill trust (`inr_trust`) stays separate.

6. **Prompt-cache hygiene.** Byte-stable message order: stable policy → schema/tools → versioned action-family instructions → frozen compile context → volatile repair/task feedback. Separate prefixes for draft / judge / repair. Record `prompt_version`, `prompt_prefix_hash`, `tool_schema_version`, and normalized usage (`input_tokens`, `cached_input_tokens`, `uncached_input_tokens`, `output_tokens`, estimated cost). Support OpenAI and DeepSeek via OpenAI-compatible adapters.

7. **Prescription contract alignment.** Additive optional `execution_mode`, `inr_trust`, `ops_clearance` on `prescription.json` (L4 already emits; L5 depends on them).

8. **L6 privacy.** `blocked` joins `pending_stamped_review` and `withheld` as customer-hidden. Pipeline attempts, compile traces, and credibility never reach L6 DTOs.

## Consequences

- Bump `l4-compile-trace` to **1.1.0** (nullable `prescription_id`, pipeline/credibility/generation/prompt-cache fields).
- Additive prescription fields; consumers pin the same `external/` SHA.
- L3, L4, L5, L6 implement detection-run, quality path, attempt store, and privacy in follow-on consumer PRs.
- Eval gains Path D goldens, reflection/RAG expansion cases, and opt-in live cache-hit checks.

## Alternatives considered

| Option | Rejected because |
| --- | --- |
| L4 detects without L3 Finding | Breaks layer charter; invents waste |
| Force-promote withhold/abstain to L6 | Undermines gates; customer sees unsafe Due |
| Unbounded ReAct reflection | Cost + non-determinism; Path D already owns schedule |
| Require `prescription_id` always | Blocks staff visibility of non-emits |
| Provider-specific prompt DSLs in domain graph | Couples L4 to one vendor |
| Store chain-of-thought | Privacy / retention risk; structured drafts suffice |
