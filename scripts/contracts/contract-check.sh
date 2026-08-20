#!/usr/bin/env bash
# contract-check.sh — validate JSON schemas and fixtures (stamped-platform)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SCHEMAS="${ROOT}/contracts/schemas"
FIXTURES="${ROOT}/contracts/fixtures"

fail() { echo "contract-check: $*" >&2; exit 1; }

test -d "${SCHEMAS}" || fail "missing ${SCHEMAS} — initialize external/ submodule first"

python3 - "${ROOT}" <<'PY'
import json, sys
from pathlib import Path

root = Path(sys.argv[1])
schemas = root / "contracts" / "schemas"
fixtures = root / "contracts" / "fixtures"

try:
    import jsonschema
except ImportError:
    print("contract-check: pip install jsonschema", file=sys.stderr)
    sys.exit(1)

def _prefer_nested(paths):
    """Dedupe by basename; prefer nested paths over flat legacy aliases."""
    by_name = {}
    for path in paths:
        cur = by_name.get(path.name)
        # nested = more parents under schemas/fixtures → higher depth wins
        if cur is None or len(path.parts) > len(cur.parts):
            by_name[path.name] = path
    return by_name

def _is_git_symlink_stub(path: Path) -> bool:
    """Windows checkouts of git symlinks are one-line relative targets, not JSON."""
    text = path.read_text(encoding="utf-8").strip()
    if not text or text[:1] in "{[":
        return False
    return "/" in text and "\n" not in text and not text.startswith("{")

def _load_json_files(paths):
    real = []
    for path in paths:
        if _is_git_symlink_stub(path):
            continue
        with open(path, encoding="utf-8") as f:
            json.load(f)
        real.append(path)
    return real

schema_files = _load_json_files(sorted(schemas.rglob("*.json")))
if not schema_files:
    print("contract-check: no schemas found", file=sys.stderr)
    sys.exit(1)

schema_by_name = _prefer_nested(schema_files)

fixture_files = _load_json_files(sorted(fixtures.rglob("*.json")))
fixture_by_name = _prefer_nested(fixture_files)

pairs = {
    "bill_line.valid.json": "bill-line.json",
    "finding.valid.json": "finding.json",
    "prescription.valid.json": "prescription.json",
    "ledger_entry.valid.json": "ledger-entry.json",
    "ledger_entry_opportunity_cost.valid.json": "ledger-entry.json",
    "workflow_event.valid.json": "workflow-event.json",
    "workflow_event_ops_verified.valid.json": "workflow-event.json",
    "plant_intelligence_score.valid.json": "plant-intelligence-score.json",
    "production_order.valid.json": "production-order.json",
    "production_record.valid.json": "production-record.json",
    "prescription_revision.valid.json": "prescription-revision.json",
    "improvement_signal.valid.json": "improvement-signal.json",
    "plant_preference_profile.valid.json": "plant-preference-profile.json",
    "plant_department_graph.valid.json": "plant-department-graph.json",
    "improve_cycle.valid.json": "improve-cycle.json",
    "calibration_patch.valid.json": "calibration-patch.json",
    "model_run.valid.json": "model-run.json",
    "plant_admin_settings.valid.json": "plant-admin-settings.json",
    "plant_knowledge_graph.valid.json": "plant-knowledge-graph.json",
    "plant_live_index.valid.json": "plant-live-index.json",
    "shift_roster.valid.json": "shift-roster.json",
    "l4_compile_trace.valid.json": "l4-compile-trace.json",
    "l4_compile_trace.withhold.json": "l4-compile-trace.json",
    "l4_compile_trace.abstain.json": "l4-compile-trace.json",
    "pipeline_run.valid.json": "pipeline-run.json",
}
for fixture, schema_name in pairs.items():
    fp, sp = fixture_by_name.get(fixture), schema_by_name.get(schema_name)
    if fp is not None and sp is not None:
        with open(sp) as f:
            schema = json.load(f)
        with open(fp) as f:
            data = json.load(f)
        jsonschema.validate(instance=data, schema=schema)

print(f"contract-check: OK ({len(schema_by_name)} schemas, {len(fixture_by_name)} fixtures)")
PY

test -f "${FIXTURES}/golden/dedupe_golden.json" || fail "missing golden/dedupe_golden.json"
echo "contract-check: dedupe golden present"
