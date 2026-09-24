#!/usr/bin/env python3
"""Validate L1 context-record contracts (schemas, packs, tools, fixtures)."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

try:
    import jsonschema
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover
    print("jsonschema required: uv run --with jsonschema ...", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2]
CONTRACTS = ROOT / "contracts"
SCHEMAS = {
    "asset_state": CONTRACTS / "schemas" / "telemetry" / "asset-state.json",
    "process_batch": CONTRACTS / "schemas" / "plant" / "process-batch.json",
    "flow_position": CONTRACTS / "schemas" / "plant" / "flow-position.json",
    "maintenance_context": CONTRACTS / "schemas" / "plant" / "maintenance-context.json",
    "quality_status": CONTRACTS / "schemas" / "plant" / "quality-status.json",
    "material_availability": CONTRACTS / "schemas" / "plant" / "material-availability.json",
    "operating_rate": CONTRACTS / "schemas" / "commercial" / "operating-rate.json",
}
FIXTURES = {
    "asset_state": (
        CONTRACTS / "fixtures" / "telemetry" / "asset_state.valid.json",
        CONTRACTS / "fixtures" / "telemetry" / "asset_state.invalid.json",
    ),
    "process_batch": (
        CONTRACTS / "fixtures" / "plant" / "process_batch.valid.json",
        CONTRACTS / "fixtures" / "plant" / "process_batch.invalid.json",
    ),
    "flow_position": (
        CONTRACTS / "fixtures" / "plant" / "flow_position.valid.json",
        CONTRACTS / "fixtures" / "plant" / "flow_position.invalid.json",
    ),
    "maintenance_context": (
        CONTRACTS / "fixtures" / "plant" / "maintenance_context.valid.json",
        CONTRACTS / "fixtures" / "plant" / "maintenance_context.invalid.json",
    ),
    "quality_status": (
        CONTRACTS / "fixtures" / "plant" / "quality_status.valid.json",
        CONTRACTS / "fixtures" / "plant" / "quality_status.invalid.json",
    ),
    "material_availability": (
        CONTRACTS / "fixtures" / "plant" / "material_availability.valid.json",
        CONTRACTS / "fixtures" / "plant" / "material_availability.invalid.json",
    ),
    "operating_rate": (
        CONTRACTS / "fixtures" / "commercial" / "operating_rate.valid.json",
        CONTRACTS / "fixtures" / "commercial" / "operating_rate.invalid.json",
    ),
}
PACK_SCHEMA = CONTRACTS / "packs" / "pack.schema.json"
PACK_FIXTURE = CONTRACTS / "packs" / "fixtures" / "generic-csv-process-batch.json"
TOOLS = CONTRACTS / "tools" / "l2-query-tools.json"
ENVELOPE = CONTRACTS / "schemas" / "envelope" / "stamped-record-envelope.json"
TOPICS = CONTRACTS / "TOPICS.md"

REQUIRED_TOOLS = {
    "get_measurements",
    "get_asset_state",
    "get_events",
    "list_production_orders",
    "get_production_records",
    "get_process_batch",
    "get_flow_position",
    "get_maintenance_context",
    "get_quality_status",
    "get_material_availability",
    "get_shift_roster",
    "get_operating_rate",
    "get_bill_lines",
    "list_bills",
    "get_active_tariff",
    "list_constraints",
}

NEW_ENUM = {
    "asset_state",
    "process_batch",
    "flow_position",
    "maintenance_context",
    "quality_status",
    "material_availability",
    "shift_roster",
    "operating_rate",
    "plant_constraint",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def assert_additional_properties_false(schema: dict, path: str, errors: list[str]) -> None:
    # Object schemas must lock the shape: false, or a schema constraining extras (maps).
    if schema.get("type") == "object" or "properties" in schema:
        ap = schema.get("additionalProperties", None)
        if ap is True or ap is None:
            errors.append(f"{path}: additionalProperties must be false (or a schema for maps)")
    for key, sub in (schema.get("properties") or {}).items():
        if isinstance(sub, dict):
            assert_additional_properties_false(sub, f"{path}.{key}", errors)
    items = schema.get("items")
    if isinstance(items, dict):
        assert_additional_properties_false(items, f"{path}[]", errors)


def validate_fixtures(errors: list[str]) -> None:
    for name, schema_path in SCHEMAS.items():
        schema = load(schema_path)
        assert_additional_properties_false(schema, str(schema_path), errors)
        validator = Draft202012Validator(schema)
        valid_path, invalid_path = FIXTURES[name]
        valid = load(valid_path)
        inv = list(validator.iter_errors(valid))
        if inv:
            errors.append(f"{valid_path}: expected valid, got {inv[0].message}")
        invalid = load(invalid_path)
        if validator.is_valid(invalid):
            errors.append(f"{invalid_path}: expected invalid")


def validate_pack(errors: list[str]) -> None:
    schema = load(PACK_SCHEMA)
    assert_additional_properties_false(schema, str(PACK_SCHEMA), errors)
    fixture = load(PACK_FIXTURE)
    Draft202012Validator(schema).validate(fixture)


def validate_tools(errors: list[str]) -> None:
    doc = load(TOOLS)
    names = {t["name"] for t in doc.get("tools", [])}
    if names != REQUIRED_TOOLS:
        errors.append(f"tools mismatch: missing={REQUIRED_TOOLS - names} extra={names - REQUIRED_TOOLS}")
    for tool in doc.get("tools", []):
        props = (tool.get("arguments") or {}).get("properties") or {}
        if "org_id" in props:
            errors.append(f"tool {tool['name']} must not take org_id")
        if "org_id" in ((tool.get("arguments") or {}).get("required") or []):
            errors.append(f"tool {tool['name']} must not require org_id")


def validate_envelope(errors: list[str]) -> None:
    env = load(ENVELOPE)
    enum = set(env["properties"]["record_type"]["enum"])
    missing = NEW_ENUM - enum
    if missing:
        errors.append(f"envelope missing record_type values: {sorted(missing)}")


def validate_topics(errors: list[str]) -> None:
    text = TOPICS.read_text(encoding="utf-8")
    for token in ("orders", "context", "process_batch", "observed_at", "asset_state"):
        if token not in text:
            errors.append(f"TOPICS.md missing token {token!r}")


def run_self_test() -> int:
    """Mutate fixtures in memory and assert rejection."""
    failures = 0
    schema = load(SCHEMAS["process_batch"])
    valid = load(FIXTURES["process_batch"][0])
    v = Draft202012Validator(schema)

    extra = copy.deepcopy(valid)
    extra["junk"] = 1
    if v.is_valid(extra):
        print("SELF-TEST FAIL: extra field accepted")
        failures += 1
    else:
        print("SELF-TEST OK: extra field rejected")

    no_lineage = copy.deepcopy(valid)
    del no_lineage["lineage"]
    if v.is_valid(no_lineage):
        print("SELF-TEST FAIL: missing lineage accepted")
        failures += 1
    else:
        print("SELF-TEST OK: missing lineage rejected")

    tools = load(TOOLS)
    mutated = copy.deepcopy(tools)
    mutated["tools"][0]["arguments"]["properties"]["org_id"] = {"type": "string"}
    bad = []
    for tool in mutated["tools"]:
        props = (tool.get("arguments") or {}).get("properties") or {}
        if "org_id" in props:
            bad.append(tool["name"])
    if not bad:
        print("SELF-TEST FAIL: org_id inject not detected")
        failures += 1
    else:
        print("SELF-TEST OK: org_id in tool args detected")

    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()

    errors: list[str] = []
    validate_fixtures(errors)
    validate_pack(errors)
    validate_tools(errors)
    validate_envelope(errors)
    validate_topics(errors)
    if errors:
        for e in errors:
            print("FAIL:", e)
        return 1
    print("OK: context contracts valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
