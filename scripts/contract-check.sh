#!/usr/bin/env bash
# Compatibility shim — CI and consumer wrappers call scripts/contract-check.sh
exec bash "$(cd "$(dirname "$0")" && pwd)/contracts/contract-check.sh" "$@"
