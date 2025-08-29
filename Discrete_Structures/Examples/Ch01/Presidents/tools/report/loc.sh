#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")"/../.. && pwd)"
THRESH=${1:-120}   # highlight files with SLOC > THRESH
TOP=${2:-10}       # show top N heavy files

echo "== SLOC per .py (no blanks or # comments), largest first =="
# build "SLOC  path" rows, sort DESC, show top N, mark big ones
find "$root" -type f -name '*.py' -not -path '*/.venv/*' -print0 \
  | xargs -0 -I{} awk '
      BEGIN{c=0}
      /^[[:space:]]*($|#)/ {next}
      {c++}
      END{printf "%6d %s\n", c, FILENAME}
    ' {} \
  | sort -nr \
  | awk -v T="$THRESH" '{flag = ($1 > T ? "  ‼" : ""); printf "%6d %s%s\n", $1, $2, flag }' \
  | sed -n "1,${TOP}p"

echo
echo "== LOC per .py (incl. blanks/comments), largest first =="
find "$root" -type f -name '*.py' -not -path '*/.venv/*' -exec wc -l {} + \
  | sort -nr \
  | sed -n "1,${TOP}p"

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

