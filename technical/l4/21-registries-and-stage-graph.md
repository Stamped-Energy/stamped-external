# Registries and stage graph

**Status:** Architecture. Normative kernel checkpoints: [`00-kernel.md`](00-kernel.md) §12.  
**ADR:** [039](../../decisions/033-039/ADR-039-registries-and-stage-graph.md)

---

## Why registries

The kernel must stay small. Domains, workflows, soft thresholds, and model pins will change weekly in v1. Hard-coding them into the runtime turns every plant request into a rewrite and breaks replay. Everything replaceable is a **versioned registry entry** pinned by one **release lockfile**.

The kernel and runtime refer to registries by id. They never list the five seed domains by name.

---

## Registry catalog

| Registry | What an entry defines | Used by |
| --- | --- | --- |
| Domains | id, label, attention-budget exempt flag, default owner roles | Card primary domain; memory tags; seam options |
| Families | Finding family → domain, proof obligations, workflow default | Finding intake |
| Workflows | Stage sequence id, applicability predicate, escape to investigative | Workflow-route seam |
| Stages | Stage id, port, allowed tools, token budget | Stage graph |
| Analyses | Plug-in id, domain binding, claim kinds, forbidden claims | Domain analyses |
| Patterns | Scanner predicate, footprint template, domain, condition-key recipe, verification recipe, owner, precision thresholds | Discovery emit |
| Constraint kinds | Predicate vocabulary + evaluator binding | Constraint evaluator |
| Tools | Allowlisted read tools / builder reads | Analyses, zoom |
| Prompts | Versioned prompt ids per seam / analysis | Model calls |
| Memory missions | Hindsight mission ids and retention | Plant bank |
| Model pins | Family A/B ids, offline council ids, hosting mode | Runtime |
| Ranking policy | Lexicographic order for discovery/portfolio ranking | Discovery, portfolio |
| Soft-gate thresholds | Numeric / enum thresholds per soft gate id | Soft gates |
| Roles | Owner role set | One-owner rule |

---

## Release lockfile

One lockfile per deploy pins:

- every registry entry version in use
- `l4-kernel` version
- model pins
- Hindsight / case-library schema versions

Replay of a past DecisionCase uses the lockfile that was live at run time. Nothing in a registry promotes itself into the lockfile.

---

## Default stage graph

```mermaid
flowchart LR
  C[Candidates] --> CE[Constraint evaluator]
  CE --> PF[Portfolio]
  PF --> MIN[Card minimizer]
  MIN --> KR[Kernel re-check]
  KR --> T[Terminal]
```

Rules that every custom graph must still obey — see [`00-kernel.md`](00-kernel.md) §12 (do not restate the checkpoint list here).

Stages may be added (e.g. an optional analysis stage) or reordered **within** those checkpoints by registry change + replay.

---

## How a new domain appears

1. Domain registry entry (id, exempt flag, roles).
2. Analysis plug-in bound to that id ([`10-domain-analyses.md`](10-domain-analyses.md)).
3. Memory tag scope uses the same id.
4. Seam option sets pull domains from the registry — no seam code change.
5. Lockfile pin + replay on holdouts + shadow before plant default.

No kernel edit. No ADR unless the domain needs a new hard gate (unusual).

---

## How a new pipeline stage appears

1. Stage registry entry (port, tools, budget, typed in/out).
2. Insert into workflows **without skipping** kernel checkpoints. If the stage changes candidates or footprints **after** the constraint evaluator, it must trigger constraint re-evaluation before portfolio.
3. Lockfile + replay.

If the stage would change a kernel checkpoint, that is an ADR + kernel bump — not a registry-only change.

**Domain registry entry (canonical fields for v1):** id, label, `attention_budget_exempt`, default owner roles, analysis plug-in id. Richer fields (claim kinds, effect units, calculator methods, rendering) live on the **analysis plug-in** and family entries — see [`17-change-guide.md`](17-change-guide.md) for the full add-domain recipe including L5/L6 section ids on the wire.

---

## Exception-response attention exemption

Declared on the **domain registry entry** (`attention_budget_exempt: true`), not hard-coded in portfolio logic. Portfolio reads the flag ([`09-portfolio.md`](09-portfolio.md)).

---

## Seam options from registries

Workflow route, secondary domain, owner role, pattern id, and similar closed option sets are populated from registries at runtime. Adding a domain or workflow automatically extends the option set for the next lockfile that includes it.

---

## Change control summary

| Change | Path |
| --- | --- |
| Registry content | Entry version + lockfile + replay |
| Soft-gate threshold | Soft-gate registry + owner accept after evidence ([`22-missed-opportunities.md`](22-missed-opportunities.md)) |
| Stage graph shape | Stage + workflow registries + replay; must keep kernel checkpoints |
| Kernel checkpoints / hard gates | ADR + kernel version bump + full replay |

See also [`17-change-guide.md`](17-change-guide.md).

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Seed registries for five product domains + Pilot families/workflows/patterns | Sixth+ domains, more stages, more soft gates — still registry-only |
| Default stage graph | Custom graphs that keep kernel checkpoints |
| Soft-gate thresholds in registry | Same; calibrated via opportunity ledger |
| Shared pack target: `stamped-external/registries/` (schemas + seed; implementation after this docs set) | Same location |
