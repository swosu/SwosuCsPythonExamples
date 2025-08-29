#!/usr/bin/env bash
set -euo pipefail

# current project directory
here="$(cd "$(dirname "$0")"/../.. && pwd)"

# only check Python files in THIS repo, skip .venv
matches="$(grep -R -n $'\t' --include='*.py' \
  --exclude-dir=.venv \
  "$here" || true)"

if [ -n "$matches" ]; then
  echo "$matches"
  echo "❌ Tabs found in YOUR code. In vim: :set expandtab ts=4 sw=4  then  :retab"
  exit 1
else
  echo "✅ No tabs found in your code. Third-party sins ignored."
fi

