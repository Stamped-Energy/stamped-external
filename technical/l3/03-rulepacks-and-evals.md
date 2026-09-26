# L3 — Rulepacks and evals

*Status: as-built · 2026-09-26*

## Rulepacks (`intelligence-rulepacks`)

Filesystem catalog of versioned YAML rulepacks, vertical priors, and DISCOM HT tables. **Not a runtime.** Core loads them with `RULEPACK_PATH` pointing at the rulepacks repo root.

| Owns | Does not own |
| --- | --- |
| Thresholds, formula ids, suppressions, `ops_clearance` defaults, vertical overlays | Detector Python; outbox; Lab UI |
| `rulepack://{pack}/{semver}#{rule_id}` citations on Findings | Setting `delivery` / `status` (core owns dual-lane) |

**Math runs in `intelligence-core`.** Rule YAML is sheet music; engines are the orchestra.

Typical layout: `domain/{pack}/{semver}/` · `verticals/{id}/params.yaml` · tariff tables · `schemas/formula_registry.json` · `schemas/catalog_index.json`.

Counts drift — prefer `schemas/catalog_index.json` in the rulepacks repo over copied numbers here.

### Load order (as-built)

1. Domain pack for the engine’s `pack_id` / `rule_id`
2. Optional vertical overlay (`VERTICAL_ID`)
3. Shared suppressions + metric registry

Plant secrets stay outside the rulepacks repo.

---

## Evals (`intelligence-evals`)

Offline scores for L3 RunArtifacts plus an internal Lab UI. **Observation only** — no promote Lab → L4.

| Surface | Job |
| --- | --- |
| CLI `stamped-l3-eval` | Backtest goldens; gate check (`precision_min` in `config/gates.yaml`) |
| Lab UI | Triage candidates; L4 board = `delivery=l4` ∧ `status=emitted`; Discovery keeps the rest |

Default corpus is checked-in RunArtifact **1.1.0** goldens — no live L2 required. Optional attach to core Lab export is secondary.

---

## Split of duty

```text
rulepacks  →  thresholds / citations
core       →  engines / dual-lane / outbox
evals      →  offline score / Lab triage
```

Next: [`04-finding-contract.md`](04-finding-contract.md).
