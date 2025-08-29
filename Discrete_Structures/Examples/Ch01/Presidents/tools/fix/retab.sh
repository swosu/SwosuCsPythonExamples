#!/usr/bin/env bash
set -euo pipefail

here="$(cd "$(dirname "$0")"/../.. && pwd)"
echo "Retabbing *.py under: $here (excluding .venv)"

# Use perl for a portable in-place tab->4 spaces
# Only affects *.py outside .venv
find "$here" -type f -name '*.py' -not -path '*/.venv/*' -print0 \
  | xargs -0 perl -0777 -pe 's/\t/    /g' -i

echo "Done. Tip: run tools/check/style_tabs.sh to verify."

