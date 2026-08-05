#!/usr/bin/env bash
# Legacy entrypoint — PATH_MAP: scripts/validate.sh → scripts/contracts/validate.sh
exec "$(cd "$(dirname "$0")" && pwd)/contracts/validate.sh" "$@"
