#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")"/../.. && pwd)"

echo "== LOC per .py (incl. blanks/comments) =="
find "$root" -type f -name '*.py' -not -path '*/.venv/*' -exec wc -l {} + | sort -n

echo
echo "== SLOC per .py (no blanks or # comments) =="
find "$root" -type f -name '*.py' -not -path '*/.venv/*' -print0 \
  | xargs -0 -I{} awk '
      BEGIN{c=0}
      /^[[:space:]]*($|#)/ {next}
      {c++}
      END{printf "%6d %s\n", c, FILENAME}
    ' {} | sort -n

echo
echo "== Totals =="
total_loc=$(find "$root" -type f -name '*.py' -not -path '*/.venv/*' -exec wc -l {} + | awk 'END{print $1}')
total_sloc=$(find "$root" -type f -name '*.py' -not -path '*/.venv/*' -print0 \
  | xargs -0 -I{} awk '
      BEGIN{c=0}
      /^[[:space:]]*($|#)/ {next}
      {c++}
      END{print c}
    ' {} | awk '{s+=$1} END{print s}')
printf "LOC : %d\nSLOC: %d\n" "$total_loc" "$total_sloc"

