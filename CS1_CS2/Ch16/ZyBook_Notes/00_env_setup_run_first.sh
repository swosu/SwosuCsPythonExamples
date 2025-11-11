#!/usr/bin/env bash
#
# 00_env_setup_run_first.sh
#
# One-time (or once-per-machine) setup script for this project.
# It creates a Python virtual environment in .venv/ and installs
# the packages we need (numpy, matplotlib).
#

set -euo pipefail

# Go to the directory where this script lives (project root)
PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$PROJECT_ROOT"

echo "Project root: $PROJECT_ROOT"

# 1. Create virtual environment if it does not exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment in .venv ..."
    python3 -m venv .venv
else
    echo "Virtual environment .venv already exists."
fi

# 2. Activate the venv
echo "Activating virtual environment ..."
# shellcheck source=/dev/null
source .venv/bin/activate

# 3. Upgrade pip and install required packages
echo "Upgrading pip and installing packages ..."
python -m pip install --upgrade pip
pip install numpy matplotlib

echo
echo "✅ Environment setup complete."
echo "To work in this project in a new shell, run:"
echo "    cd \"$PROJECT_ROOT\""
echo "    source .venv/bin/activate"
echo
echo "Then you can run:"
echo "    python scripts/bubble_sort_analyze.py"
echo "    python scripts/bubble_sort_timing.py"

