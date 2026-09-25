# TRACE_NOTES — stamped-external @ a4c91bc286099e0cb0d3db124932994df045ac94

This repository is the **platform SSOT pack** (contracts, ADRs, handoff, technical architecture). There is **no long-running application** on main—only documentation, JSON schemas, fixtures, and CI scripts that consumer repos invoke via the `external/` git submodule ([ADR-011](decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md)).

## Entry points (what humans/CI run)

| Entry | Trigger | Stages | Output | Evidence |
| --- | --- | --- | --- | --- |
| `scripts/contracts/contract-check.sh` | Consumer PR or local dev | Load schemas → validate fixtures → jsonschema pairs | Exit 0 or fail CI | `scripts/contracts/contract-check.sh:1-80` |
| `scripts/vision-identity-lint.ps1` | Platform PR (identity-sensitive docs) | Scan `*.md` / `*.mdc` for withdrawn framing | Exit 0 or fail | `scripts/vision-identity-lint.ps1:10-16` |
| `scripts/contracts/validate.sh` | Optional wrapper | Delegates to contract-check | Same as contract-check | `scripts/contracts/validate.sh:1` |
| Python contract suites | Layer CI when present | Adversarial / L1-L2 pins / e2e scripts under `scripts/contracts/` | Test reports | e.g. `scripts/contracts/e2e_finding_to_ledger.py:74` |

No `pyproject.toml` / `package.json` application entry on main at this SHA—the repo is consumed as read-only content plus the scripts above.

## Contract change runtime path (organizational)

1. Author PR in **stamped-external** with schema + fixture + `contracts/CHANGELOG.md` (+ ADR when normative).
2. `contract-check.sh` on merge (see diagram EXT-02).
3. Tag / semver noted in `VERSION` + root `CHANGELOG.md` (platform release discipline).
4. Consumer repos bump `external/` submodule pin (ADR-011 matrix).
5. Dual-read window documented in `contracts/CHANGELOG.md` (e.g. Finding 2.0.0, deprecated `prescription.json`).

## Authority order (when docs disagree)

Documented chain: `research/.../AGENT-START.md` → `09` → `10` → ADR-030 → `technical/STAMPED_ARCHITECTURE.md` → `technical/l4/` → `handoff/` → `contracts/schemas` (diagram EXT-04). Vision `09` wins on product meaning; contracts win on wire bytes.

## Env flags

None on this repo at runtime. Consumer repos inherit their own env; submodule pin is git metadata, not an env flag.

## Doc ↔ code gaps

| ID | Docs say | Code / tree on main | Evidence | Shown in |
| --- | --- | --- | --- | --- |
| G9 | Some archived / legacy layer write-ups still describe L4 as a prescription **compiler** only | `technical/STAMPED_ARCHITECTURE.md` and `technical/l4/` describe the agentic L4 kernel; `technical/layers/README.md` points to `l4/` as normative | `technical/STAMPED_ARCHITECTURE.md:9` vs `archive/cleanup-2026-09/technical/layers/l4-l6/L4-knowledge-and-reasoning.md` (archived) | EXT-04 |
| new | Contract **removed** state as an automated enum | Policy prose in `contracts/CHANGELOG.md` only; no schema enum for “removed” | `contracts/CHANGELOG.md:14-17` | EXT-05 card |

Honesty: no integration is live at any customer plant. Verified savings to date: ₹0.
