# Improve pipeline (step 06) — monthly job spec

> **Authority:** [ADR-025](../decisions/ADR-025-improve-loop-step-06.md) · [04-evaluation-and-quality §3.5](../technical/cross-cutting/04-evaluation-and-quality.md) · [`improvement-signal.json`](../contracts/schemas/improvement-signal.json) · [`plant-preference-profile.json`](../contracts/schemas/plant-preference-profile.json)  
> **Audience:** closure-verification and/or intelligence-evals  
> **Shape:** One cron job, three outputs — no L7 service

---

## 1. Cadence

| Job | Frequency | Output |
| --- | --- | --- |
| Calibration refresh | Weekly (optional) | Track A shrinkage multipliers (config draft) |
| Improve monthly | **Monthly** per plant | Track A patch + Track B preference draft + Track C markdown report |

---

## 2. Inputs

- L5 workflow outcomes (acted / deferred / rejected / disputed + reason codes)
- L5 ledger predicted vs realised
- Negotiation threads / `ImprovementSignal` rows
- Optional L6 audit: view counts before ack (P2)

---

## 3. Track A — ML calibration

1. Aggregate calibration table per waste_category (eval §3.5 shape).  
2. If ratio < 0.7 and n ≥ 5 → draft shrinkage multiplier.  
3. If reject+"not_real" rate high → draft threshold raise for category.  
4. Write **draft** plant config; promote via existing T4 / engineer review — never silent.

---

## 4. Track B — Agent preferences

1. Cohort: `followed` = done/verified within SLA; `ignored` = deferred/rejected/open>14d.  
2. Diff dimensions: decision_class, waste_category, template_id, owner_role, effort, order_conflict, evidence types.  
3. Emit `PlantPreferenceProfile` with `approval.status=draft`.  
4. Engineer approves → L4 ranker / template prefs / owner_map_corrections apply.

Negotiation patterns: top objection tags → `preferred_alternative_template`.

---

## 5. Track C — Developer UI report

Generate internal markdown (example sections):

```markdown
# Improve report — {plant_id} — {month}
## Closure
## Followed vs ignored contrast
## Negotiation themes
## Evidence challenges
## Friction hotspots (L6)
## Suggested UI tweaks (do not auto-apply)
## Suggested L6 config pins
```

Deliver to Stamped eng channel / ticket queue. Customer UI changes only after human implement of **config pins** (nav defaults, Rx card columns).

---

## 6. Module home

**P0:** `improve/` package inside **closure-verification** (owns workflow signals) **or** nightly job in **intelligence-evals**. Prefer L5 if emitting signals there already.

---

## 7. Guardrails

- Plant-scoped only  
- Reuse reason codes  
- Human gate on Track B/C behavior changes  
- Monthly UI suggestions — not weekly layout churn  

---

## 8. Acceptance (Improve v1)

1. Dry-run on fixture workflow data produces markdown report.  
2. Followed-vs-ignored contrast table non-empty when ≥5 closed Rx.  
3. No automatic L4/L6 production config flip without `approval.status=approved`.
