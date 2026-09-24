#!/usr/bin/env python3
"""Hygiene checks for L1–L2 context-records branches (H1)."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VENV_RE = re.compile(r"(^|[\\/])\.venv([\\/]|$)")
SECRET_RE = re.compile(
    r"(?i)(password\s*[:=]\s*['\"]?\S+|api[_-]?key\s*[:=]\s*['\"]?\S+|secret\s*[:=]\s*['\"]?\S{8,})"
)


def scan_text(text: str) -> list[str]:
    findings: list[str] = []
    for i, line in enumerate(text.splitlines(), 1):
        if VENV_RE.search(line):
            findings.append(f"L{i}: .venv path in diff/tree")
        if SECRET_RE.search(line):
            findings.append(f"L{i}: possible secret literal")
    return findings


def self_test() -> int:
    fake = """
diff --git a/foo/.venv/lib/site.py b/foo/.venv/lib/site.py
+password = "hunter2-super-secret"
+print('ok')
"""
    findings = scan_text(fake)
    ok_venv = any(".venv" in f for f in findings)
    ok_pw = any("secret" in f.lower() or "password" in f.lower() for f in findings)
    if not ok_venv:
        print("SELF-TEST FAIL: .venv not caught")
        return 1
    if not ok_pw:
        print("SELF-TEST FAIL: password not caught")
        return 1
    print("SELF-TEST OK: .venv and password caught")
    return 0


def scan_workspace(workspace: Path) -> int:
    repos = [
        workspace / "stamped-external",
        workspace / "universal-repositary",
        workspace / "Connector - L1" / "connectors-cloud",
        workspace / "Connector - L1" / "connectors-edge",
        workspace / "Connector - L1" / "connectors-bill",
    ]
    failures = 0
    for repo in repos:
        if not repo.is_dir():
            continue
        # Untracked/modified names via git status --porcelain
        import subprocess

        r = subprocess.run(
            ["git", "status", "--porcelain", "-u"],
            cwd=str(repo),
            text=True,
            capture_output=True,
        )
        text = r.stdout or ""
        findings = scan_text(text)
        # also scan diff of tracked changes
        d = subprocess.run(
            ["git", "diff", "HEAD"],
            cwd=str(repo),
            text=True,
            capture_output=True,
        )
        findings.extend(scan_text(d.stdout or ""))
        if findings:
            print(f"FAIL {repo.name}:")
            for f in findings[:20]:
                print(" ", f)
            failures += 1
        else:
            print(f"OK {repo.name}")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.workspace:
        print("--workspace required unless --self-test", file=sys.stderr)
        return 2
    return scan_workspace(Path(args.workspace))


if __name__ == "__main__":
    sys.exit(main())
