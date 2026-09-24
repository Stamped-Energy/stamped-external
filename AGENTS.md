# Stamped Platform — Agent Mode

> **Repo role:** Shared platform pack (contracts, ADRs, handoff, technical specs) — **not application code**.  
> **Product:** Stamped — choose, assign, and verify the next operating action across five domains.  
> **Cursor config source:** [cursor-config-coding](https://github.com/Vinayak-RZ/cursor-config-coding) (vendored under `.cursor/`).

Engineering workflow: **ponytail → (spec-kit for features) → research → plan → approve → implement → validate → commit → learn**.

## Vision (read first — every product-shaped task)

1. [`research/plant-efficiency-exploration-2026-09/AGENT-START.md`](research/plant-efficiency-exploration-2026-09/AGENT-START.md)
2. [`research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md`](research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md) — **wins on conflict**
3. [`research/plant-efficiency-exploration-2026-09/10-stamped-vision-agent-alignment.md`](research/plant-efficiency-exploration-2026-09/10-stamped-vision-agent-alignment.md)
4. [ADR-030](decisions/028-032/ADR-030-five-domain-decision-loop.md)
5. [`technical/STAMPED_ARCHITECTURE.md`](technical/STAMPED_ARCHITECTURE.md)

**Never** append Energy to the product name. **Never** teach withdrawn dual-pillar framing, fixed savings-% as identity, or energy-only company. External marketing is under [`archive/external-marketing-2026-09/`](archive/external-marketing-2026-09/) — do not read it for identity; do not rewrite it unless the human asked for a marketing pass.

Rule: `stamped-vision.mdc`. Lint: `./scripts/vision-identity-lint.ps1`.

## Repo-specific guidance

| Area | Guidance |
|------|----------|
| **Contracts** (`contracts/`) | Schema changes require `contracts/CHANGELOG.md` semver bump + `scripts/contracts/contract-check.sh` pass |
| **ADRs** (`decisions/`) | New decisions as ADR-NNN under number buckets; update `decisions/README.md` index; framing = ADR-030 |
| **Handoff** (`handoff/`) | Cross-repo integration docs; start at `handoff/README.md` |
| **Archive** | Marketing / decks / old client narrative — out of agent identity path |
| **Consumer repos** | See [REPOS.md](REPOS.md) and [SUBMODULE.md](SUBMODULE.md) |
| **Release** | Tag as needed; bump [VERSION](VERSION) and [CHANGELOG.md](CHANGELOG.md) after intentional releases |

**Reading order for new agents:** [README.md](README.md) → vision pack above → [handoff/README.md](handoff/README.md) → [decisions/README.md](decisions/README.md).

## Ponytail — mandatory gate for all coding

**Before writing or modifying any code**, read and apply the `ponytail` skill (`.cursor/skills/ponytail/SKILL.md`). Always-on rule: `ponytail.mdc`.

## Spec Kit — Spec-Driven Development (features / greenfield)

From [github/spec-kit](https://github.com/github/spec-kit). Pre-installed skills: `speckit-*`. Rule: `speckit.mdc`.

Use for **new features / greenfield**, not one-line fixes or contract typo fixes.

## Before any task

1. Read this file and all `.cursor/rules/` (start with `rule-awareness`, `stamped-vision`, `ponytail`, `core-engineering`).
2. **Coding tasks:** read `ponytail` skill before proposing or writing code.
3. **Feature / greenfield:** follow `speckit.mdc` when the user wants specs-first or the change is multi-phase.
4. Follow `planning.mdc` — analyze, plan, **get user approval** before non-trivial coding.
5. Unfamiliar tech → research brief for the user before architectural choices.

## Architecture (when designing or refactoring)

| Domain | Skill | Rule |
|--------|-------|------|
| Frontend / UI / Next.js | `frontend-architecture` | `frontend-architecture.mdc` |
| Backend / API / data | `backend-architecture` | `backend-architecture.mdc` |
| AI agents / LLM / tools | `agentic-system-design` | `agentic-systems.mdc` |
| Any major trade-off | `system-design-tradeoffs` | `trade-offs.mdc` |

Do **not** invent a new company when designing. Product = five-domain closed decision loop ([ADR-030](decisions/028-032/ADR-030-five-domain-decision-loop.md)).

## Git commits and pushes

After each validated phase or meaningful feature:

- **Conventional commit** per `git-commit-discipline.mdc`
- **Push check** after every commit — auto-push when **≥ 10 unpushed** commits, or when user asks

## Before completion

1. Apply `quality-gates.mdc` — validate, report, update progress docs, **commit**.
2. Contract changes: run `./scripts/contracts/contract-check.sh` before marking done.
3. Identity-sensitive doc PRs: run `./scripts/vision-identity-lint.ps1`.

## Upstream config

To refresh from [cursor-config-coding](https://github.com/Vinayak-RZ/cursor-config-coding), follow that repo’s vendor instructions. Project overrides for Stamped vision stay in this repo’s `.cursor/rules/stamped-vision.mdc`.
