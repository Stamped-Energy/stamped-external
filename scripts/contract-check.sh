#!/usr/bin/env bash
# Legacy entrypoint — PATH_MAP: scripts/contract-check.sh → scripts/contracts/contract-check.sh
exec "$(cd "$(dirname "$0")" && pwd)/contracts/contract-check.sh" "$@"
