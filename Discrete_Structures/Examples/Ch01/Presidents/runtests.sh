#!/usr/bin/env bash
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
PY="$here/.venv/bin/python"

echo "=== Presidents test runner ==="

# 1) Ensure venv exists (quiet bootstrap)
if [ ! -x "$PY" ]; then
  echo "-> No venv python found; bootstrapping via setup.sh..."
  "$here/setup.sh" >/dev/null
fi

# 2) Style preflight: tabs check (skips .venv inside the script)
if [ -x "$here/tools/check/style_tabs.sh" ]; then
  echo "-> Running style check (tabs -> spaces)..."
  "$here/tools/check/style_tabs.sh"
else
  echo "-> style_tabs.sh not found; skipping tab check."
fi

# 3) Interpreter banner
echo "-> Using interpreter: $("$PY" -c 'import sys; print(sys.executable)')"
echo "-> Python version:    $("$PY" -V)"

# 4) Run tests
echo "-> Running pytest..."
exec "$PY" -m pytest "$@"

