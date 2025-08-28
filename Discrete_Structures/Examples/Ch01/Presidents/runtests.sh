#!/usr/bin/env bash
set -euo pipefail
# Always use the project venv's Python so version matches (3.11+)
exec "$(dirname "$0")/.venv/bin/python" -m pytest "$@"

