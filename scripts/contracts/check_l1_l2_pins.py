#!/usr/bin/env python3
"""Fail unless all L1–L2 consumer repos pin the same contracts/ tree as stamped-external HEAD."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

CONSUMERS = [
    "universal-repositary",
    "Connector - L1/connectors-cloud",
    "Connector - L1/connectors-edge",
    "Connector - L1/connectors-bill",
]


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        text=True,
        capture_output=True,
    )


def submodule_sha(repo: Path) -> str:
    ext = repo / "external"
    if not ext.exists():
        raise SystemExit(f"missing external: {ext}")
    r = run(["git", "rev-parse", "HEAD"], cwd=ext)
    if r.returncode != 0:
        raise SystemExit(f"rev-parse failed in {ext}: {r.stderr}")
    return r.stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", required=True)
    args = ap.parse_args()
    ws = Path(args.workspace)
    stamped = ws / "stamped-external"
    if not stamped.is_dir():
        print("FAIL: stamped-external missing", file=sys.stderr)
        return 1

    head = run(["git", "rev-parse", "HEAD"], cwd=stamped)
    if head.returncode != 0:
        print(head.stderr, file=sys.stderr)
        return 1
    stamped_head = head.stdout.strip()
    print(f"stamped-external HEAD {stamped_head[:12]}")

    failures = 0
    for rel in CONSUMERS:
        repo = ws / rel
        if not repo.is_dir():
            print(f"FAIL: missing repo {rel}")
            failures += 1
            continue
        try:
            sha = submodule_sha(repo)
        except SystemExit as e:
            print(f"FAIL: {rel}: {e}")
            failures += 1
            continue
        # contracts/ tree must match stamped HEAD
        diff = run(
            ["git", "diff", "--quiet", sha, stamped_head, "--", "contracts"],
            cwd=stamped,
        )
        if diff.returncode != 0:
            print(f"FAIL: {rel} pin {sha[:12]} contracts/ differs from stamped HEAD")
            failures += 1
        else:
            print(f"OK: {rel} pin {sha[:12]} contracts/ matches")

    # edge go build
    edge = ws / "Connector - L1" / "connectors-edge" / "packages" / "edge-agent"
    if edge.is_dir():
        gb = run(["go", "build", "./..."], cwd=edge)
        if gb.returncode != 0:
            print("FAIL: go build ./... in edge-agent")
            print(gb.stderr)
            failures += 1
        else:
            print("OK: go build ./... edge-agent")

    # compose configs
    for compose in [
        ws / "universal-repositary" / "deploy" / "docker-compose.l2.yml",
        ws / "Connector - L1" / "connectors-cloud" / "deploy" / "profiles" / "l1-l6-real-l2.yml",
    ]:
        if not compose.exists():
            print(f"WARN: compose not found {compose} (checked later in R1)")
            continue
        dc = run(["docker", "compose", "-f", str(compose), "config", "-q"])
        if dc.returncode != 0:
            print(f"FAIL: docker compose config -q {compose.name}: {dc.stderr.strip()}")
            failures += 1
        else:
            print(f"OK: docker compose config {compose.name}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
