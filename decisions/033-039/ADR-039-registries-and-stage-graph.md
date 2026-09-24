# ADR-039: Registries and expandable stage graph

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-25 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-033](ADR-033-l4-decision-runtime.md) · [`technical/l4/21-registries-and-stage-graph.md`](../../technical/l4/21-registries-and-stage-graph.md) · [`technical/l4/17-change-guide.md`](../../technical/l4/17-change-guide.md) |

---

## Context

L4 will grow: new domains, families, workflows, pipeline stages, analyses, patterns, constraint kinds, tools, prompts, memory missions, model pins. Hard-coding domain names or stage order into the kernel makes every expansion a rewrite and breaks replay.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Registries | Domains, families, workflows, stages, analyses, patterns, constraint kinds, tools, prompts, memory missions, model pins, ranking policy, soft-gate thresholds — all versioned registry entries |
| 2 | Release lockfile | One lockfile pins the set of registry versions for a deploy; nothing promotes itself |
| 3 | Kernel | Refers to registries by id; never lists domains or stages by name |
| 4 | Default stage graph | candidates → constraint evaluator → portfolio → kernel re-check → terminal |
| 5 | Graph change | Stages can be added or reordered by registry; every graph must still pass kernel checkpoints; portfolio always after constraint evaluator |
| 6 | New domain | Registry entry + analysis plug-in + memory tag scope + seam option appearance — not a kernel change |
| 7 | Seam options | Drawn from registries so new domains/workflows appear without seam code changes |
| 8 | Exception exemption | Declared on the domain registry entry (attention-budget exempt), not hard-coded |

---

## Consequences

- Adding a sixth domain or a new pipeline stage is registration plus replay.
- Replay uses the lockfile that was live at run time.
- Kernel remains small and ADR-gated.

---

## Rejected alternatives

- Hard-coded five domains inside the kernel.
- Free agent that invents new stages at runtime.
- Per-plant silent registry edits without lockfile / release.
