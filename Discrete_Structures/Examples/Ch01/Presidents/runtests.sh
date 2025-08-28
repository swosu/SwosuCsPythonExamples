#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"

# If venv python is missing, bootstrap via setup.sh (quiet)
if [ ! -x "$here/.venv/bin/python" ]; then
  "$here/setup.sh" >/dev/null
fi

# Run tests with the venv's interpreter
exec "$here/.venv/bin/python" -m pytest "$@"

