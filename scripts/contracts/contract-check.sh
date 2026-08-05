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

schema_files = sorted(schemas.rglob("*.json"))
if not schema_files:
    print("contract-check: no schemas found", file=sys.stderr)
    sys.exit(1)

schema_by_name = {}
for sf in schema_files:
    with open(sf) as f:
        json.load(f)
    schema_by_name[sf.name] = sf

for ff in sorted(fixtures.rglob("*.json")):
    with open(ff) as f:
        json.load(f)

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
}
fixture_by_name = {ff.name: ff for ff in fixtures.rglob("*.json")}
for fixture, schema_name in pairs.items():
    fp, sp = fixture_by_name.get(fixture), schema_by_name.get(schema_name)
    if fp is not None and sp is not None:
        with open(sp) as f:
            schema = json.load(f)
        with open(fp) as f:
            data = json.load(f)
        jsonschema.validate(instance=data, schema=schema)

print(f"contract-check: OK ({len(schema_files)} schemas, {len(list(fixtures.rglob('*.json')))} fixtures)")
PY

test -f "${FIXTURES}/golden/dedupe_golden.json" || fail "missing golden/dedupe_golden.json"
echo "contract-check: dedupe golden present"
