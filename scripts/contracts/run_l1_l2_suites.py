#!/usr/bin/env python3
"""Run L1–L2 suites in order; one line per suite; non-zero if any fail."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> int:
    print("+", " ".join(cmd), f"(cwd={cwd})")
    p = subprocess.run(cmd, cwd=str(cwd))
    return p.returncode


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", required=True)
    args = ap.parse_args()
    ws = Path(args.workspace)
    results: list[tuple[str, int]] = []

    stamped = ws / "stamped-external"
    code = run(
        [
            "uv",
            "run",
            "--python",
            "3.12",
            "--with",
            "jsonschema",
            "--with",
            "pyyaml",
            "python",
            "scripts/contracts/validate_l1_context.py",
        ],
        stamped,
    )
    results.append(("B1_contracts", code))

    l2 = ws / "universal-repositary"
    py = l2 / ".venv" / "Scripts" / "python.exe"
    if not py.exists():
        py = l2 / ".venv" / "bin" / "python"
    code = run(
        [str(py), "-m", "pytest", "packages/ingest/tests", "packages/query-api/tests", "-q"],
        l2,
    ) if py.exists() else 1
    if not (l2 / ".venv").exists():
        print("L2 .venv missing")
    results.append(("B2_l2", code))

    cloud = ws / "Connector - L1" / "connectors-cloud"
    py = cloud / ".venv" / "Scripts" / "python.exe"
    if not py.exists():
        py = cloud / ".venv" / "bin" / "python"
    code = run([str(py), "-m", "pytest", "-q"], cloud) if py.exists() else 1
    results.append(("B3_cloud", code))

    edge = ws / "Connector-L1" / "connectors-edge" / "packages" / "edge-agent"
    code = run(["go", "test", "./...", "-count=1"], edge) if edge.is_dir() else 1
    results.append(("B4_edge", code))

    bill = ws / "Connector-L1" / "connectors-doc"
    py = bill / ".venv" / "Scripts" / "python.exe"
    if not py.exists():
        py = bill / ".venv" / "bin" / "python"
    code = run([str(py), "-m", "pytest", "packages", "-q"], bill) if py.exists() else 1
    results.append(("B5_bill", code))

    failed = 0
    for name, code in results:
        status = "PASS" if code == 0 else "FAIL"
        print(f"{status} {name} exit={code}")
        if code != 0:
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
