#!/usr/bin/env python3
import json
from pathlib import Path

def derivation():
    # From the chapter:
    # Amina fixed left: 4 (LZ block placements) * 2 (LZ|ZL) * 2 (nonadj bot pairs) * 2! (bot identities) * 1 (Jake) = 32
    # Double by symmetry (Amina right end) => 64
    return {
        "N_all": 720,
        "N_A": 240,
        "N_B": 240,
        "N_C": 480,
        "N_ABC": 64
    }

def main():
    files = Path("../files"); files.mkdir(parents=True, exist_ok=True)
    counts = derivation()

    with open(files/"ch01_counts.json","w") as f:
        json.dump(counts, f, indent=2)

    with open(files/"ch01_summary.txt","w") as f:
        f.write("Nebula Diner combinatorics summary\n")
        f.write("----------------------------------\n")
        for k,v in counts.items():
            f.write(f"{k}: {v}\n")

    print("OK ch01 formulas written")

if __name__ == "__main__":
    main()

