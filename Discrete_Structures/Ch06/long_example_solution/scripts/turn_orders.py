#!/usr/bin/env python3
"""
turn_orders.py - enumerate / count initiative orders (permutations) for a team.

Console output: a single summary line.
Files:
  data/turn_orders_T{T}.csv              (only when enumerating)
  files/turn_orders_summary.txt          (always)
  figures/turn_orders_lead_freq_T{T}.png (if matplotlib present and enumerating)

Examples:
  python scripts/turn_orders.py -T 3 --list-small
  python scripts/turn_orders.py -T 4 --names A,B,C,D --must-before A>B,B>D --together C+D --list-small
  python scripts/turn_orders.py -T 8   # count only (no full enumeration)
"""

import argparse
import csv
import itertools
import math
import os
import sys
from collections import Counter

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def ensure_dirs():
    for d in ("data", "files", "figures"):
        os.makedirs(d, exist_ok=True)

def default_names(T: int):
    # A, B, C, ... then A1, B1... if we run out
    base = [chr(ord('A') + i) for i in range(min(T, 26))]
    if T <= 26:
        return base
    names = base[:]
    i = 1
    while len(names) < T:
        for ch in base:
            names.append(f"{ch}{i}")
            if len(names) >= T:
                break
        i += 1
    return names

def parse_pairs(s: str):
    # "A>B,B>C" -> [("A","B"),("B","C")]
    if not s:
        return []
    parts = [p.strip() for p in s.split(",") if p.strip()]
    pairs = []
    for p in parts:
        if ">" not in p:
            raise ValueError(f"must-before pair '{p}' must look like X>Y")
        a, b = [x.strip() for x in p.split(">")]
        if not a or not b:
            raise ValueError(f"Bad must-before pair '{p}'")
        pairs.append((a, b))
    return pairs

def parse_groups(s: str):
    # "A+B, C+D+E" -> [["A","B"], ["C","D","E"]]
    if not s:
        return []
    groups = []
    for g in s.split(","):
        g = g.strip()
        if g:
            groups.append([x.strip() for x in g.split("+") if x.strip()])
    return groups

def is_contiguous_block(order, group):
    # group appears as a consecutive block in 'order' (any internal order allowed)
    idxs = sorted(order.index(x) for x in group)
    return all(idxs[i] + 1 == idxs[i+1] for i in range(len(idxs)-1))

def is_any_adjacent_pair(order, group):
    # does ANY adjacent pair from group occur? (used for "apart" = forbid adjacency)
    pos = {name: i for i, name in enumerate(order)}
    group_set = set(group)
    for a in group:
        i = pos[a]
        if i > 0 and order[i-1] in group_set:
            return True
        if i < len(order)-1 and order[i+1] in group_set:
            return True
    return False

def check_constraints(order, must_before, together_groups, apart_groups):
    ok_mb = True
    for a, b in must_before:
        if order.index(a) >= order.index(b):
            ok_mb = False
            break

    ok_tog = True
    for g in together_groups:
        if not is_contiguous_block(order, g):
            ok_tog = False
            break

    ok_apart = True
    for g in apart_groups:
        if is_any_adjacent_pair(order, g):
            ok_apart = False
            break

    ok_all = ok_mb and ok_tog and ok_apart
    return ok_mb, ok_tog, ok_apart, ok_all

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Turn order (permutation) counter/enumerator.")
    ap.add_argument("-T", "--team-size", type=int, required=True, help="Number of heroes on the team")
    ap.add_argument("--names", type=str, default="", help="Comma-separated hero names (length must equal T)")
    ap.add_argument("--list-small", action="store_true",
                    help="Enumerate and write CSV only for small T (<=8). Otherwise just print formula count.")
    ap.add_argument("--must-before", type=str, default="", help="Constraints like 'A>B,B>C'")
    ap.add_argument("--together", type=str, default="", help="Groups that must be contiguous like 'A+B, C+D+E'")
    ap.add_argument("--apart", type=str, default="", help="Groups that must NOT be adjacent like 'A+B, C+D'")
    args = ap.parse_args()

    T = args.team_size
    if T < 1:
        print("Team size T must be >= 1", file=sys.stderr)
        sys.exit(2)

    names = [n.strip() for n in args.names.split(",") if n.strip()] if args.names else default_names(T)
    if len(names) != T:
        print(f"Provided {len(names)} names but T={T}.", file=sys.stderr)
        sys.exit(2)

    must_before = parse_pairs(args.must_before)
    together_groups = parse_groups(args.together)
    apart_groups = parse_groups(args.apart)

    ensure_dirs()

    # Always compute the total unconstrained count.
    total_unconstrained = math.factorial(T)

    enumerating = args.list_small and T <= 8
    csv_path = f"data/turn_orders_T{T}.csv"
    summary_path = "files/turn_orders_summary.txt"
    fig_path = f"figures/turn_orders_lead_freq_T{T}.png"

    valid_count = None
    lead_counter = Counter()

    if enumerating:
        order_id = 0
        with open(csv_path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["order_id", "order", "valid_must_before", "valid_together", "valid_apart", "valid_all"])
            for perm in itertools.permutations(names, T):
                perm_list = list(perm)
                ok_mb, ok_tog, ok_ap, ok_all = check_constraints(perm_list, must_before, together_groups, apart_groups)
                if ok_all:
                    lead_counter[perm_list[0]] += 1
                w.writerow([order_id, "-".join(perm_list), int(ok_mb), int(ok_tog), int(ok_ap), int(ok_all)])
                order_id += 1

        # Count how many were valid overall
        with open(csv_path, newline="") as f:
            r = csv.DictReader(f)
            valid_count = sum(1 for row in r if row["valid_all"] == "1")

        # Try to plot if matplotlib is available
        try:
            import matplotlib.pyplot as plt
            if lead_counter:
                heroes, counts = zip(*sorted(lead_counter.items()))
                plt.figure()
                plt.bar(heroes, counts)
                plt.title(f"Lead-slot frequency among valid orders (T={T})")
                plt.xlabel("Leading hero")
                plt.ylabel("Count")
                plt.tight_layout()
                plt.savefig(fig_path, dpi=150)
                plt.close()
        except Exception:
            # Soft fail: no figure if matplotlib missing
            fig_path = None

    # Write summary
    with open(summary_path, "w") as s:
        s.write("=== Turn Orders Summary ===\n")
        s.write(f"T = {T}\n")
        s.write(f"Names = {names}\n")
        s.write(f"Unconstrained count = {total_unconstrained}\n")
        s.write(f"must_before = {must_before}\n")
        s.write(f"together    = {together_groups}\n")
        s.write(f"apart       = {apart_groups}\n")
        if enumerating:
            s.write(f"Enumerated all orders and wrote {csv_path}\n")
            s.write(f"Valid (all constraints) = {valid_count}\n")
            if fig_path:
                s.write(f"Figure (lead frequency) saved to {fig_path}\n")
        else:
            s.write("Large T or no --list-small: skipped full enumeration.\n")
            s.write("Reported only the unconstrained factorial count above.\n")

    # Console: one clean line
    if enumerating:
        print(f"Turn order count (valid/all) = {valid_count}/{total_unconstrained} | CSV: {csv_path} | Summary: {summary_path}")
    else:
        print(f"Turn order count (unconstrained) = {total_unconstrained} | Summary: {summary_path}")


if __name__ == "__main__":
    main()

