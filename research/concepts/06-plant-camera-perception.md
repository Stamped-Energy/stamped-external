---
type: Research Note
title: "Plant camera perception — cameras as structured observation, not a plant brain"
description: "Exploration of plant CCTV as a dense-sensing input for Stamped. Compares narrow vision, VLMs, and world models; maps the one decision cameras can uniquely improve (idle / occupancy); designs a cheap shadow experiment that can fail."
tags: [research, dense-sensing, vision, vlm, world-models, idle-load, shared-context]
lane: FRONTIER
status: exploration
stamped_hooks: [dense-sensing, idle-load, shared-context, world-models]
timestamp: "2026-08-15T00:00:00Z"
---

# Plant camera perception

**Purpose:** decide whether plant camera feeds can make Stamped prescriptions more *practical* — and if so, which model class is the cheapest way to test that.

**This note is an exploration.** It does not add an L1 source, an event-schema type, or an ADR. No connector, no GPU pipeline, no new cameras.

**Identity lock:** Stamped remains a read-only operational decision layer. Cameras, if they ever enter the stack, are **shared context** — the same class as orders and shift calendars — not a third pillar and not a VMS / people-analytics product. Framing: [ADR-026](../../decisions/024-026/ADR-026-two-pillars-shared-context.md).

> Evidence labels: **[Repo]** grounded in current architecture · **[Research]** grounded in published work · **[Inference]** deduction to test, not fact.

---

## 1. Thesis

Stamped already infers plant state from meters, SCADA, bills, and (when present) orders. The recurring hole is **floor reality**.

L3 idle detection is effectively:

```text
kW high  ∧  production = 0   →   idle / phantom-load finding
```

([L3 intelligence core](../../technical/layers/l3/L3-intelligence-core.md) waste classifier: `phantom = kW > floor when production = 0`; `machine state = idle ∧ kW > threshold for > N min`.)

When production tags are missing or the shift calendar is wrong — common on Path B plants — that rule either fires on a running line or misses a parked machine. Supervisors then reject the prescription as impractical. That is a **context** failure, not a model-accuracy failure.

Cameras can close *that* gap. They cannot replace the energy graph, the tariff engine, or the M&V ledger.

Existing strategy already constrains how far this idea may go:

| Constraint | Source |
|---|---|
| World models stay **shadow-only** until they change a decision | [PATHS v2](../strategy/PATHS_FOR_STAMPED_V2.md) Part IX / recommended default #5 |
| Dense sensing is valuable only when it improves observability of decide → close → verify | [INSIGHTS](../strategy/INSIGHTS_FOR_STAMPED.md) executive synthesis |
| Do not add sensors before proving a repeated missing-data problem | PATHS anti-pattern #7 (hardware romanticism) |
| L1 source inventory has **no camera / CCTV** today; phone camera is bill capture only | [L1 spec](../../technical/layers/l1-l2/L1-connect-and-normalise.md) §2.1 |
| Foundation models are **challengers**, never the M&V path of record | [ADR-014](../../decisions/011-015/ADR-014-ts-foundation-model-role.md) |

Referenced concept files (`00-world-models-primer.md`, `03-dinowm.md`, `04-agents-with-world-models.md`) are cited from INSIGHTS but **are not in this repo**. This note fills the vision-modality gap here. It does not reconstruct that KB.

---

## 2. The three options, in plain language

```text
Pixels
  → Vision model     "what objects / states are in this frame?"
  → VLM              "answer a question about this scene in language"
  → World model      "predict the next state if X happens"
```

| Class | What it is | When it wins | Why it usually loses for Stamped |
|---|---|---|---|
| **Narrow vision** (YOLO / pose / occupancy classifier) | Detector or classifier → structured labels (`line_occupied`, `machine_spinning`, `bay_empty`) | One repeated visual fact; edge-cheap; JSON-auditable | Brittle across plants; needs per-site labels |
| **VLM** (Qwen-VL, GPT-4o-vision, MonitorVLM-style) | Image or short clip + prompt → JSON or prose | Open vocabulary; few-shot “is this line running?”; useful as analyst assist | Hallucinates. SteelBench (Jul 2026) best VLM is **42.6%** action accuracy vs **84.6%** human on real plant CCTV (dust, glare, distant workers) **[Research]**. Chain-of-thought VLMs do not scale to many RTSP streams (MonitorVLM-v2 had to *compress* reasoning into a finite rule-ID space to stay real-time) **[Research]** |
| **World model** (V-JEPA 2, DINO-WM, LeWM) | Latent dynamics: predict `z_{t+1}` from `z_t` (+ optional action) | Counterfactuals; planning; “what if we stagger this line” from video | Needs action-labeled trajectories. Stamped is **read-only** — no control writes. Predicts pixels or latents, not ₹. Does not solve tag mapping or operational feasibility ([INSIGHTS §7](../strategy/INSIGHTS_FOR_STAMPED.md)) |

**Default:** treat cameras as a **narrow observation source**, not a plant brain.

- **P0 experiment (this note):** frozen detector or small VLM → structured occupancy labels (`yes` / `no` / `unknown`).
- **P1 (only if P0 lifts a decision):** VLM as L4 analyst assist — “show me the bay at 14:12” — citing a stored keyframe. Never as the finding engine.
- **P2+ shadow:** world-model challenger only if we later have paired `(visual state, electrical state, accepted Rx, verified outcome)` trajectories. Same promotion gate as TimesFM in ADR-014.

### Trade-off: model class

**Decision:** which class to explore first.

**Option A — Narrow CV → structured events.** Pros: cheap, edge-local, JSON-auditable, fits the existing L1 `Event` shape. Cons: one skill per visual fact; plant-specific calibration.

**Option B — VLM as the plant observer.** Pros: flexible questions; faster to demo. Cons: cost, latency, hallucination; DPDP if frames leave India; SteelBench shows industrial CCTV is still hard.

**Option C — World model as plant understanding.** Pros: future counterfactuals. Cons: no action channel today; no unique decision; prestige without a prescription change.

**Default:** A, with B as a shadow captioner on the same keyframes.

**Override:** `PRIORITY = QUALITY` (try B first for a demo) or `PRIORITY = SPEED` (slideware VLM demo — not recommended).

---

## 3. The observability gap cameras can close

**The one decision cameras uniquely improve:** idle / off-shift load prescriptions (`idle_load` waste category; often `mgmt_schedule` when the action is “shut this bay down after shift”).

Visual `bay_empty` vs `line_running` is the missing independent variable when MES production is absent. That is shared context, not a third pillar.

Declared-vs-actual shift is the same gap from the other side. L3 already treats calendar disagreement as a finding ([L3](../../technical/layers/l3/L3-intelligence-core.md) occupancy/shift discovery). A camera that says “bay empty at 14:12 on a declared production shift” is an independent check on that finding — the same way a production count would be, when we have one.

### What cameras do not uniquely improve

Do not start here. Each already has a better primary signal:

| Decision | Why cameras are the wrong first sensor |
|---|---|
| MD stagger / shed | Needs kW profiles and coincidence, not a picture of the floor |
| PF / tariff | Electrical arithmetic |
| Compressor specific power | Needs flow / pressure (or a proxy), not a view of the skid |
| Furnace holding kW | Needs kW + a production/charge window; a door-open classifier is a later luxury |
| Safety / PPE | Different product. MonitorVLM is a safety company. Stamped does not become one. |

A VLM saying “the shop looks busy” is not a finding. If the visual signal cannot change accept / reject on an idle prescription, it is a demo.

---

## 4. Where it would sit (if the experiment works)

Cameras stay customer-owned L0. Stamped never becomes a video-management system or a people-analytics product. Prefer existing CCTV; do not buy cameras.

```text
L0 CCTV (RTSP / NVR)
  → edge sampler (keyframes only — not continuous video)
  → vision extractor (narrow CV, or small VLM as shadow captioner)
  → visual_observation Event   { line_occupied: yes | no | unknown }
  → L2 event store
  → L3 idle / occupancy covariate (confirmation, not engine of record)
  → L4 Rx evidence (optional redacted keyframe cite)
  ╌→ world-model challenger (shadow only; not in this experiment)
```

| Layer | Role | Must not |
|---|---|---|
| L1 | Sample keyframes on-edge; emit a structured `Event` (a future `visual_observation` type — **not added in this pass**) | Stream raw video to cloud; store faces |
| L2 | Store the event + optional redacted keyframe pointer | Become a video archive |
| L3 | Use visual occupancy as a **covariate / confirmation** on idle and shift-mismatch findings | Cite vision in M&V ₹ or prescription `impact` |
| L4 | Attach “bay empty at 14:12” as evidence | Let a VLM draft the Rx from the image alone |
| L5 / L6 | Optional keyframe on the Rx card | Live CCTV wall |

This is the same pattern as ADR-014: a new modality may *challenge* a finding. It may not become the cited path of record until a promotion ADR says so.

### Implications for L1

**Not in L1 P0.** The current P0 connector set is meters, bills, and file exports — installable without an OT ticket. NVR / RTSP access is often a harder ticket than Modbus. Adding cameras to the L1 source inventory, or a `visual_observation` value to [`event.json`](../../contracts/schemas/envelope/event.json), waits on:

1. This experiment showing decision lift (or a clear kill).
2. A plant that will grant consented, read-only keyframe access.
3. A DPA that covers workplace imagery.

Until then, treat camera perception as a research option, not a backlog item that blocks Path B.

---

## 5. Compliance (heavier than meter PII)

CCTV includes people. Faces and gait are personal data. This is a different class of risk from asset-level telemetry, which the [India compliance register](../../compliance/india-compliance-register.md) treats as usually *not* personal when it is asset-level only.

**Defaults if a pilot is ever run:**

| Rule | Why |
|---|---|
| Edge-only inference | Frames need not leave the plant |
| No cloud video | CERT-In / DPDP residency is necessary but not sufficient; the issue is *having* the imagery |
| Blur people before any retain | Occupancy of a *bay* is the fact we want, not who is in it |
| Retain events, not frames | `line_occupied=no` at `ts` is enough for L3; a keyframe is optional evidence and must be redacted |
| Plant DPA + worker notice before any pilot | Workplace surveillance is a customer-fiduciary problem; Stamped is processor |
| India-region inference if any frame must leave the edge | No EU/US VLM API on plant faces |

A public-footage fallback (below) avoids this until a plant consents. That is the default path for the experiment in §6.

---

## 6. Falsifiable experiment (offline, 50–100 keyframes)

Cheapest test that can fail. World-model work is **out of this experiment**.

### 6.1 One visual fact

```text
line_occupied ∈ { yes, no, unknown }
```

on **one bay that already has a feeder meter**. Not “what is happening in the plant.” Not open-ended VQA.

`unknown` is a first-class label. Dust, glare, a blocked view, or a night scene with no useful pixels must abstain. Forcing yes/no is how a demo becomes a false idle Rx.

### 6.2 Data

**Preferred later:** consented plant CCTV, keyframes only, people blurred, paired with that bay’s kW series and the declared shift calendar.

**Default now:** public industrial footage or SteelBench-style stills, plus a *synthetic* kW + calendar pairing so the decision metric can still be computed. Public clips will not prove plant-specific detectors. They *will* prove whether the evaluation harness and the three-way comparison are coherent before we ask a plant for cameras.

Target: **50–100 labeled keyframes**, stratified across occupied / empty / unusable. One person labels; a second person spot-checks 20%. Disagreement → `unknown` or discard.

### 6.3 Three systems, same windows

| System | Input | Output |
|---|---|---|
| **Meter-only (baseline)** | Feeder kW + declared shift / production=0 | Idle finding yes/no using the current L3 rule |
| **Narrow CV** | Keyframe | `line_occupied` |
| **Prompted VLM (shadow)** | Same keyframe + a fixed JSON schema prompt | `line_occupied` + one-sentence rationale (rationale is not scored) |

The VLM is a captioner on the same frames, not a second product path.

### 6.4 Score decision lift, not mAP

mAP answers “did the detector find the forklift?” We do not care.

**Primary metric:** precision and recall of the decision *this machine should be off* (the idle finding), against a human label of “bay empty and not in a declared production window” / “bay running or occupied.”

Compare:

1. Meter-only idle rule.
2. Meter-only **plus** visual `line_occupied=no` as a confirmation gate (finding fires only when both agree).
3. Meter-only **plus** visual `line_occupied=yes` as a veto (finding suppressed when the bay is visually running).

**Lift** = change in precision (fewer impractical “shut it down” Rx) and/or recall (catches parked machines the calendar missed), on windows where the two signals *disagree*. Agreement windows teach nothing.

Secondary (diagnostic only): occupancy accuracy vs human labels, abstention rate, per-class confusion. Useful for debugging. Not the kill/go gate.

### 6.5 Kill criteria

Stop. Do not write an L1 connector, an event type, or an ADR.

| Kill | Meaning |
|---|---|
| No lift on **≥ 30 conflicting windows** | Cameras do not change the idle decision vs kW + calendar |
| Plant refuses camera access **and** public footage cannot produce 30 conflicting windows | We cannot run a real test; park the idea |
| DPDP / customer legal blocks retention of even redacted keyframes **and** event-only (no frame) inference is refused | The modality is commercially closed |
| Visual model abstains on > 40% of frames that a human can label | The view is not usable (angle, lighting, occlusion) — fix the camera, do not train a bigger model |

A “pretty demo” that never hits 30 disagreements is a kill, not a maybe.

### 6.6 What would count as a pass (still not a product)

On ≥ 30 conflicting windows, visual confirmation improves idle-finding precision by a margin a supervisor would notice (target: **+0.15 precision** without a recall collapse worse than −0.05) **[Inference — threshold to revisit after the first labeled set]**.

A pass unlocks a *design* conversation: draft `visual_observation` on `Event`, an L1 “not P0” source row, and a shadow-challenger ADR in the ADR-014 shape. It does not unlock a CCTV product, a live wall, or M&V citation.

---

## 7. When (not) to revisit world models

A world model is a dynamics model: it predicts the next state given the current state and, usually, an action. Stamped’s action channel today is a **human-closed prescription**, not a control write.

Revisit a video world-model challenger only when all of these are true:

1. The occupancy experiment passed (§6.6) or was killed for a reason that does not apply to dynamics (e.g. we have occupancy another way).
2. We have trajectories of `(visual state, electrical state, recommended action, human response, verified outcome)` — the intervention record [INSIGHTS §1](../strategy/INSIGHTS_FOR_STAMPED.md) already treats as the atomic data asset.
3. There is a **specific decision** a latent rollout would change that TOW-P + the stagger simulator cannot (PATHS founder question 16: “What decision can a world model make uniquely better — not merely predict more accurately?”).

Until then, “we should use a world model on the cameras” is model prestige. PATHS recommended default #5 still holds: run world models in shadow against **decision-level** metrics, not video-prediction loss.

---

## 8. Risks (short)

- **Category drift.** Safety, productivity, and people-tracking vendors already sell CCTV analytics. Stamped stays energy / equipment decisions with visual confirmation.
- **Plant IT.** RTSP access is often harder than Modbus. Existing CCTV or nothing.
- **Cost.** Multi-stream VLM is not viable on typical edge boxes; detectors are.
- **False practicality.** Language about the scene is not a finding.
- **Surveillance optics.** Even with blur and event-only retain, a plant may refuse. That is a kill, not a procurement problem.

---

## 9. Assumptions

| Assumption | Reason | Impact if wrong |
|---|---|---|
| First gap is idle / bay occupancy | Highest overlap with an existing L3 finding and a known Path B hole (missing production tags) | Experiment target changes — rewrite §6.1, do not keep the same labels |
| No consented plant CCTV in this pass | We have not asked; DPDP is unresolved | Public-footage fallback; plant CCTV is a later gated step |
| Written exploration is the deliverable | Approved plan: docs only | No connector, no GPU work, no schema bump |

---

## 10. Related

- [INSIGHTS_FOR_STAMPED.md](../strategy/INSIGHTS_FOR_STAMPED.md) — dense sensing improves the loop’s observability; world models address only dynamic heterogeneity
- [PATHS_FOR_STAMPED_V2.md](../strategy/PATHS_FOR_STAMPED_V2.md) — shadow-only WMs; hardware romanticism
- [L3 intelligence core](../../technical/layers/l3/L3-intelligence-core.md) — idle rule, shift discovery
- [L1 connect & normalise](../../technical/layers/l1-l2/L1-connect-and-normalise.md) — no camera source today
- [ADR-014](../../decisions/011-015/ADR-014-ts-foundation-model-role.md) — challenger template
- [ADR-026](../../decisions/024-026/ADR-026-two-pillars-shared-context.md) — shared context, not a third pillar
- [India compliance register](../../compliance/india-compliance-register.md) — DPDP / PII
- SteelBench: [arXiv:2607.05264](https://arxiv.org/abs/2607.05264) (Jul 2026)
- MonitorVLM-v2: [arXiv:2608.00975](https://arxiv.org/html/2608.00975) (Aug 2026)
