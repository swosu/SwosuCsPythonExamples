#!/usr/bin/env bash
set -euo pipefail
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; cd "$PROJECT_DIR"

REQUIRED_MAJOR=3
REQUIRED_MINOR=11   # accept 3.11+
VENV_DIR=".venv"

say(){ echo -e "👉 $*"; }
die(){ echo -e "❌ $*" >&2; exit 1; }

find_python() {
  # Prefer newest if multiple are present
  for cmd in python3.13 python3.12 python3.11 python3 python; do
    if command -v "$cmd" >/dev/null 2>&1; then
      ver=$("$cmd" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' || true)
      maj=${ver%%.*}; min=${ver#*.}
      if [[ -n "${maj:-}" && -n "${min:-}" && $maj -ge $REQUIRED_MAJOR && $min -ge $REQUIRED_MINOR ]]; then
        echo "$cmd"; return 0
      fi
    fi
  done
  return 1
}

PYBIN="$(find_python || true)"
if [[ -z "${PYBIN:-}" ]]; then
  echo "❌ No Python ${REQUIRED_MAJOR}.${REQUIRED_MINOR}+ interpreter found."
  echo
  if command -v dnf >/dev/null 2>&1; then
    cat <<'ROCKY'
• Rocky/RHEL 9 (enable CRB and install Python 3.11):
    sudo dnf install -y dnf-plugins-core
    sudo dnf config-manager --set-enabled crb
    sudo dnf install -y python3.11 python3.11-devel
    # then re-run: ./setup.sh
ROCKY
  elif command -v apt >/dev/null 2>&1; then
    cat <<'APT'
• Ubuntu/Debian:
    sudo apt update
    sudo apt install -y python3.11 python3.11-venv
    # then re-run: ./setup.sh
APT
  elif [[ "$(uname -s)" == "Darwin" ]]; then
    cat <<'BREW'
• macOS (Homebrew):
    brew install python@3.12
    # then re-run: ./setup.sh
BREW
  else
    echo "• Or install via pyenv: https://github.com/pyenv/pyenv"
  fi
  exit 1
fi

say "Using interpreter: $PYBIN ($("$PYBIN" -V))"

if [[ ! -d "$VENV_DIR" ]]; then
  say "Creating virtual environment in $VENV_DIR"
  "$PYBIN" -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"
python -m pip install -U pip

if [[ -f requirements.txt ]]; then
  say "Installing requirements"
  pip install -r requirements.txt
else
  say "No requirements.txt found; installing pytest for dev"
  pip install -U pytest
fi

say "Running environment check"
python check_env.py || die "Environment check failed (see instructions above)."

say "Running tests"
if [[ -f pytest.ini ]]; then
  pytest -q
else
  pytest -q tests
fi

say "✅ Setup complete!"
say ""
say "To start working, run:"
say "   source $VENV_DIR/bin/activate"
say ""
say "When finished, deactivate with:"
say "   deactivate"

