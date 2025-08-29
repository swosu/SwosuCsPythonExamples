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

# 4) Run tests (no exec); capture status
echo "-> Running pytest..."
"$PY" -m pytest "$@"
status=$?

# 5) LOC summary (largest files first)
echo
echo "-> LOC summary (top heavy files):"
"$here/tools/report/loc.sh" | sed -n '1,100p'  # script will already sort DESC

# 6) Optional quick smoke sim only if tests passed
if [ $status -eq 0 ] && [ -x "$here/tools/sim/simulate.py" ]; then
  echo
  echo "-> Quick bot-only simulation:"
  "$here/tools/sim/simulate.py" || true
fi

exit $status

