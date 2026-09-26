# L3 — Engine catalog

*Status: as-built · 2026-09-26*  
*Sources:* `intelligence-core` `engines/registry.py` (`HOT_PATH_ENGINES`) · `scheduler.py` (MD/PF/TOD and adaptive packs)

Shipping a module ≠ shipping a Finding. Many detectors stay dark until an enable flag or `PROOF_RUN=1` plus required tags on L2.

## How engines turn on

| Mechanism | Behavior |
| --- | --- |
| Hot money defaults | MD exceedance default on; PF/TOD with config; tradeoff tagging default on |
| `ENABLE_*` flag | Explicit opt-in for adaptive / CNC / equipment packs |
| `PROOF_RUN=1` | Allows adaptive candidates when required tags exist (proof / demo) |
| Warm emit | Warm residuals reach outbox only with `ENABLE_WARM_EMIT` or Proof Run |
| Shadow ML | TimesFM / TabPFN / LGBM MD — cold/shadow only; not production L4 |

## Money path (scheduler)

| Id | Flag | Default | Detects |
| --- | --- | --- | --- |
| `md` | `ENABLE_MD_EXCEEDANCE` | **yes** | Incomer MD / demand-charge exposure |
| `tod` | TOD config; tradeoff via `ENABLE_TRADEOFF_ENGINE` | **yes** (with config) | Time-of-day surcharge exposure |
| `pf` | `ENABLE_PF_LEADING` / Proof Run | no | Power-factor slab / penalty risk |
| `tradeoff` | `ENABLE_TRADEOFF_ENGINE` | **yes** | Tags tradeoffs for L4 language (not free ₹ invent) |
| `md_lgbm` | `ENABLE_LGBM_MD` | no | MD LGBM **shadow** — not production L4 |

## Registry hot engines (`HOT_PATH_ENGINES`)

| Id | Flag | Default | Detects |
| --- | --- | --- | --- |
| `idle_load` | `ENABLE_IDLE_LOAD` | no | Non-productive idle load |
| `compressor_sp_drift` | `ENABLE_COMPRESSOR` | no | Compressor specific-power drift |
| `idle_cnc_spindle` | `ENABLE_CNC` | no | Spindle idle while machine idle |
| `cnc_aux_on_idle` | `ENABLE_CNC` | no | Aux power on while CNC idle |
| `cnc_state_energy_split` | `ENABLE_CNC` | no | Energy by machine state |
| `cnc_alarm_dwell` | `ENABLE_CNC` | no | Time spent in alarm |
| `cnc_sec_per_part_drift` | `ENABLE_CNC` | no | SEC / part drift |
| `cnc_spindle_load_signature` | `ENABLE_CNC` | no | Spindle load signature anomaly |
| `unattended_long_stop` | `ENABLE_CNC` | no | Long unattended stop |
| `abandoned_estop` | `ENABLE_CNC` | no | Abandoned e-stop |
| `alarm_hygiene` | `ENABLE_CNC` | no | Alarm hygiene / noise |
| `parasitic_baseload` | `ENABLE_CNC` | no | Parasitic baseload on CNC context |

CNC fleet loop: `list_assets` → each `cnc_machine` when `ENABLE_CNC` or Proof Run. Soft ERP joins (SEC-by-SKU, export-due idle) live beside these engines.

## Adaptive / ops packs (scheduler flags)

| Id / pack | Flag | Default | Detects |
| --- | --- | --- | --- |
| `hall_empty` | `ENABLE_HALL_EMPTY` | no | Hall empty / lighting-HVAC waste |
| `source_mix` | `ENABLE_SOURCE_MIX` | no | Source mix / WHR-style |
| `furnace` | `ENABLE_IDLE_FURNACE` | no | Furnace idle / setback-class |
| `sec` | `ENABLE_SEC` | no | Specific energy / part |
| `enpi` | `ENABLE_ENPI` | no | EnPI-style efficiency |
| `compressor_ops` | `ENABLE_COMPRESSOR_OPS` | no | Compressor ops pack |
| `hvac_ops` | `ENABLE_HVAC_OPS` | no | HVAC ops pack |
| `finishing_flow` | `ENABLE_FINISHING_FLOW` | no | Finishing flow waste |
| Equipment health (e.g. `trip_cascade_risk`) | `ENABLE_EQUIPMENT_HEALTH` | no | Trip / duty / feeder-class health |

## Warm / cold machinery (not standalone L4 detectors)

| Module | Role |
| --- | --- |
| `anomaly_ewma` · `cusum_h` · `residual_emit` | Warm unexplained draw |
| `baseline_towp` | Cold baseline of record |
| TimesFM / TabPFN shadows | Cold advisory only |

## Agentic detector ids (direction / experimental)

`stamped_l3_core.agentic.detectors` names families such as `aux_on_idle`, `blocked_starved`, `material_gated_idle`. Treat as **direction** unless a Finding path is wired through dual-lane like the registry engines above.

## Product framing note

As-built Findings still stamp `value_domain` as `energy_efficiency` | `equipment_health`. Product framing is five domains under [ADR-030](../../decisions/028-032/ADR-030-five-domain-decision-loop.md); do not pretend the field was migrated until core emits ADR-030 domain sections.

Next: [`03-rulepacks-and-evals.md`](03-rulepacks-and-evals.md).
