# 10 — Domain analyses

**Status:** Architecture (docs). Analyses are plug-ins; the kernel never lists domains.  
**Date:** 2026-09-25  
**Related:** [`00-kernel.md`](00-kernel.md) · [`07-finding-runtime.md`](07-finding-runtime.md) · [`04-constraints.md`](04-constraints.md) · [ADR-030](../../decisions/028-032/ADR-030-five-domain-decision-loop.md) · [ADR-039](../../decisions/033-039/ADR-039-registries-and-stage-graph.md)

Product framing today is five domains (ADR-030). Architecture treats domains as a **registry**. Each domain analysis is a plug-in bound to its registry entry. Runtime discovers plug-ins by id. Adding a sixth domain is registry + plug-in + replay — not a kernel edit. Product still needs an ADR-030 amendment before a sixth domain is sold as product surface.

HITL: analyses inform the card a human owns. They do not execute. Calculator owns rupees wherever a section is priced.

---

## Decision

- **Constraint analysis** and **cross-section analysis** always run when the investigative path (or any graph stage that requires them) is active; constraint **evaluation** itself is always code and always before portfolio.
- **Domain analyses** run when their proof obligation fires (primary or secondary domain on the case, or cross-section asks for that section).
- Seed domain ids: `energy`, `cost`, `time_throughput`, `continuity_flow`, `exception_response`.
- Kernel, portfolio, trace, and seams iterate registry ids. None of them hard-codes the five names.

---

## Why

Specialist passes catch section-local mistakes. They must reconcile into **one** card. If the runtime names domains in source, a sixth domain is a rewrite. If sections get summed into one hero ₹, dual-wallet honesty dies.

---

## Plug-in contract

Each domain analysis registers:

| Field | Meaning |
| --- | --- |
| `domain_id` | Registry id |
| Objective | What "good" means for this section |
| PSM elements / tools | What it may read (builder reads, L3 tools) |
| Claim kinds | Typed claims it may emit into the model partition |
| Typical conflicts | How it fights other domains |
| Verification sources | What L2 signals can close the loop |
| Forbidden claims | What it must never assert |
| Worked examples | Illustrative only unless labelled site-measured |
| v1 slice | What Pilot ships vs later |

Outputs are ledger-cited claims and optional secondary-domain votes. They do **not** set evidence tiers, do **not** price rupees, and do **not** evaluate constraints.

**New domain:** add registry entry + analysis plug-in + L3 methods/detectors as needed + replay suites. Runtime loads by id. See [`17-change-guide.md`](17-change-guide.md).

---

## Always-on analyses

### Constraint analysis

- **Objective:** Explain code evaluator results; flag possible conflicts for human and for withhold paths; never decide `satisfied | violated | unknown`.
- **Reads:** Typed constraint set on the PSM, candidate footprints, open-card footprints, evaluator result + conflicting fact set.
- **Claim kinds:** `constraint_explanation`, `possible_conflict_flag`, `proposed_constraint_row` (routed to plant owner — not auto-installed).
- **Typical conflicts:** Local benefit vs hard forbid / must-run / feeder bound / mutual exclusion.
- **Verification:** Constraint still active in window; conflicting fact absent after action (where applicable).
- **Forbidden:** Declaring satisfied; overriding a violated/unknown-hard result because of modeled benefit; inventing a constraint id.
- **Worked examples (illustrative):** (1) Idle-aux shed blocked by must-run on a quench pump — evaluator violated; analysis cites the must-run row. (2) Two furnace starts — possible feeder bound conflict flagged; code returns unknown until topology ampacity is confirmed; withhold.
- **v1 slice:** Explain + flag only. Proposed-constraint routing to owner. No auto-install.

### Cross-section analysis

- **Objective:** Before emit, check sections that share the condition: upstream starve, downstream block, shared utilities, shift roster load, open related cards.
- **Reads:** Propagation views on the PSM, open footprints, domain interaction table from the registry.
- **Claim kinds:** `cross_asset_conflict`, `shared_resource_pressure`, `open_card_interference`.
- **Typical conflicts:** Energy shed that starves a bottleneck cell; flow pull that spikes demand charge; exception response that ignores an accepted maintenance window.
- **Verification:** Neighbor state and shared-resource envelope after the action window.
- **Forbidden:** Publishing a new schedule; summing section effects into one savings claim; traversing the plant graph inside the model (models request typed zooms; code walks structure).
- **Worked examples (illustrative):** (1) Aux load cut on a blocked cell — cross-section notes downstream already blocked; time section shows no throughput lift. (2) Overlapping furnace starts — feeder pressure cited; portfolio conflict follows.
- **v1 slice:** Upstream/downstream/shared-utility checks for commissioned topology. Richer cumulative packs later.

---

## Seed domains

Figures below are **illustrative** unless a plant locks meters and tariffs.

### Energy (`energy`)

| | |
| --- | --- |
| **Objective** | Avoidable load / intensity decisions with production constraints visible. Bill alone is not proof. |
| **PSM / tools** | Meter hierarchy, load episodes, mode baselines (L3), shared-utility envelopes, L3 calculator for ₹ where tariff methods exist |
| **Claim kinds** | `avoidable_load`, `intensity_deviation`, `idle_auxiliary_on`, `peak_window_exposure` |
| **Typical conflicts** | vs continuity (shed that stops flow); vs exception (keep-warm for recovery); vs cost (tariff vs kWh-only story) |
| **Verification sources** | Circuit / machine load already in L2; post-action window; IPMVP-style isolation where configured ([`16`](../../research/plant-efficiency-exploration-2026-09/16-pilot-and-hard-stops.md)) |
| **Forbidden** | Model-authored ₹; bill-as-sole proof; claiming equipment wrote off; summing energy ₹ with unrelated wallets |
| **Examples (illustrative)** | (1) Machine idle, aux loads still on → ops-head card, energy primary, calculator-priced kWh if method exists. (2) Partial furnace load that could consolidate inside a shift window → energy + cost sections separate. |
| **v1 slice** | Idle-load family. Peak/feeder stories when topology and meters commissioned. |

### Cost (`cost`)

| | |
| --- | --- |
| **Objective** | Visible operating-cost tradeoffs (overtime, wait, alternate capacity, tariff shape). Finance/calculator owns ₹. |
| **PSM / tools** | Tariff methods via L3 calculator, overtime / crew availability constraints, alternate capacity flags, demand-envelope proximity |
| **Claim kinds** | `tariff_window_effect`, `overtime_exposure`, `alternate_capacity_cost`, `demand_charge_risk` |
| **Typical conflicts** | vs time (pay overtime to recover throughput); vs energy (run off-peak but longer); vs continuity (hold batch vs ship cost) |
| **Verification sources** | Tariffs and timekeeping signals in L2; calculator recompute on actual window |
| **Forbidden** | Prose ₹ estimates; combining demand and efficiency wallets into one hero number; silent master-data rate changes |
| **Examples (illustrative)** | (1) Shift work into a cheaper tariff window — cost primary; energy secondary if kWh unchanged. (2) Overtime to clear a bottleneck — cost vs time sections both present, not summed. |
| **v1 slice** | Tariff-linked pricing where L3 methods exist. Overtime/crew cost later as constraints and signals allow. |

### Time / throughput (`time_throughput`)

| | |
| --- | --- |
| **Objective** | Productive machine-minutes, idle/alarm dwell, constraint-cell response — not a full schedule. |
| **PSM / tools** | State episodes, bottleneck residence, blocked/starved propagation (L3), alarm dwell, queue positions |
| **Claim kinds** | `idle_dwell`, `alarm_dwell`, `bottleneck_residence`, `starved_or_blocked` |
| **Typical conflicts** | vs energy (keep utilities up for readiness); vs cost (overtime); vs continuity (local speed vs handoff) |
| **Verification sources** | Machine state / production counters in L2; pre/post windows on closed cards |
| **Forbidden** | Emitting a dispatch list or promise-date change; APS/MRP replacement claims; inventing counts without ledger rows |
| **Examples (illustrative)** | (1) Alarm dwell on constraint cell — time primary; exception secondary if stop risk. (2) Starved cell behind a blocked buffer — time claim cites propagation rows; action is local, not a new schedule. |
| **v1 slice** | Idle/alarm dwell on commissioned assets. Full bottleneck pack as L3 methods land. |

### Continuity / flow (`continuity_flow`)

| | |
| --- | --- |
| **Objective** | One handoff / batch / queue decision at a time — not a new dispatch system. |
| **PSM / tools** | Flow edges, buffer size and lag, batch/queue positions, handoff wait episodes |
| **Claim kinds** | `handoff_wait`, `buffer_starvation`, `buffer_block`, `batch_release_timing` |
| **Typical conflicts** | vs energy (keep line warm); vs time (local OEE vs system flow); vs exception (expedite one order) |
| **Verification sources** | Queue/batch signals in L2; handoff timestamps; buffer level if instrumented |
| **Forbidden** | Publishing a plant-wide sequence; replacing MES routing; ignoring lag on flow edges |
| **Examples (illustrative)** | (1) Recurring handoff wait between melt and cast — one release timing recommendation. (2) Buffer block propagating upstream — continuity primary; time secondary on starved minutes. |
| **v1 slice** | One handoff family where topology edges exist. Deeper batch logic later. |

### Exception response (`exception_response`)

| | |
| --- | --- |
| **Objective** | Next-hours choice after a stop or slip — not APS/MRP replacement. |
| **PSM / tools** | Alarms/events, maintenance/quality status, due context as do-not-disturb, open cards, roster |
| **Claim kinds** | `stop_recovery_option`, `slip_containment`, `bypass_with_constraint_check` |
| **Typical conflicts** | vs quality/safety hard stops; vs continuity (expedite breaks flow); vs cost (premium freight — only if calculator method exists) |
| **Verification sources** | Event clear + production restart signals; explicit owner close reasons |
| **Forbidden** | Safety/critical remote command; quality hold release; maintenance authorization; customer-commitment change; constraint override for modeled benefit |
| **Examples (illustrative)** | (1) Short stop — recovery sequence recommendation with must-run constraints cited. (2) Order slip inside shift — containment action; dues stay read-only context. |
| **Portfolio flag** | Seed registry entry sets `attention_budget_exempt=true` ([`09-portfolio.md`](09-portfolio.md)). |
| **v1 slice** | Narrow stop/slip families with reviewed constraints. No autonomy classes that touch hard stops. |

---

## How they sit in a run

1. Proof obligations decide which domain plug-ins fire.  
2. Each plug-in writes cited claims into its sub-ledger (token-budgeted).  
3. Cross-section reconciles interactions from the registry.  
4. Constraint **evaluator** (code) gates; constraint **analysis** explains.  
5. Candidates carry sections; wallets stay separate; calculator refs only for ₹.  
6. Portfolio and kernel see domain **ids**, not a fixed enum.

---

## Rejected alternatives

| Rejected | Why |
| --- | --- |
| Hard-coded five-way switch in kernel/runtime | Blocks a sixth domain without rewrite |
| Five inboxes / five tickets | Breaks one-card product |
| Analyses that evaluate constraints or emit ₹ | Violates calculator and code-gate rules |
| Summed cross-domain savings headline | Dual-wallet dishonesty |

---

## What evidence would change this

- Pilot closures showing a section never cited and never verified → retire or demote that claim kind.  
- Repeated cross-section misses on one interaction edge → add a typed interaction to the registry and a scanner.  
- Product decision to sell a sixth domain → ADR-030 amendment + registry entry + plug-in (architecture path already open).

---

## v1 slice vs later (set-wide)

| v1 | Later |
| --- | --- |
| Five seed domains + constraint + cross-section | Open registry; more domains by ADR + plug-in |
| Idle-load energy path live; others as topology/signals allow | Full claim catalogs per domain as L3 methods ship |
| Illustrative examples in this doc | Site-measured worked traces in the case library |

---

## Links

- Kernel (no domain list): [`00-kernel.md`](00-kernel.md)
- Runtime when obligations fire: [`07-finding-runtime.md`](07-finding-runtime.md)
- Portfolio exemption flag: [`09-portfolio.md`](09-portfolio.md)
- Registries: [`21-registries-and-stage-graph.md`](21-registries-and-stage-graph.md)
