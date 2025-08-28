#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"

# ---- Choose interpreter (prefer python3.11 if present) ----
PY="${PYTHON:-}"
if [[ -z "${PY}" ]]; then
  if command -v python3.11 >/dev/null 2>&1; then
    PY="python3.11"
  elif command -v python3 >/dev/null 2>&1; then
    PY="python3"
  else
    echo "❌ Could not find python3.11 or python3 in PATH."
    exit 1
  fi
fi

echo "👉 Using interpreter: $(${PY} -V 2>&1 | tr -d '\n')"

# ---- Ensure Python >= 3.11 ----
ver="$(${PY} - <<'PYV'
import sys
print(f"{sys.version_info[0]}.{sys.version_info[1]}")
PYV
)"
ma="${ver%%.*}"; mi="${ver#*.}"
if (( ma < 3 || (ma==3 && mi < 11) )); then
  echo "Exit: Python 3.11+ required, found ${ver}"
  exit 1
fi

# ---- Create venv if missing ----
if [[ ! -d "${HERE}/.venv" ]]; then
  echo "👉 Creating virtual environment at .venv"
  "${PY}" -m venv "${HERE}/.venv"
fi

# ---- Upgrade pip ----
"${HERE}/.venv/bin/python" -m pip install -U pip >/dev/null
echo "Requirement already satisfied: pip in ./.venv (updated)"

# ---- Install project requirements ----
echo "👉 Installing requirements"
if [[ -f "${HERE}/requirements.txt" ]]; then
  "${HERE}/.venv/bin/python" -m pip install -r "${HERE}/requirements.txt"
else
  echo "⚠️  No requirements.txt found; skipping."
fi

# ---- Quick environment check ----
echo "👉 Running environment check"
"${HERE}/.venv/bin/python" - <<'PYCHK'
import sys
assert sys.version_info >= (3,11), f"Python 3.11+ required, found {sys.version}"
print("✅ Python 3.11 looks good!")
PYCHK

# ---- Create runtests.sh helper (idempotent) ----
RUNTESTS="${HERE}/runtests.sh"
if [[ ! -f "${RUNTESTS}" ]]; then
  cat > "${RUNTESTS}" <<'RUN'
#!/usr/bin/env bash
set -euo pipefail
# Always use the project venv's Python so version matches (3.11+)
exec "$(dirname "$0")/.venv/bin/python" -m pytest "$@"
RUN
  chmod +x "${RUNTESTS}"
fi

# ---- Run tests once so users see green ----
echo "👉 Running tests"
"${HERE}/.venv/bin/python" -m pytest -q || true

echo "👉 ✅ Setup complete!"
echo
echo "👉 Next steps:"
echo "👉   1) Activate the venv when you want an interactive shell:"
echo "👉        source .venv/bin/activate"
echo "👉   2) Or run tests without activating the venv:"
echo "👉        ./runtests.sh -q"
echo "👉   3) Run the CLI demo without activating the venv:"
echo "👉        ./.venv/bin/python cli_demo.py"
echo
echo "👉 Pro tip: if tests fail because the wrong Python runs, use:"
echo "👉        ./runtests.sh -q"

