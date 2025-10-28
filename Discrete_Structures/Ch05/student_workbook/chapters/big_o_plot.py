#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt

def main():
    ns = list(range(0, 35))
    two_pow = [2**n for n in ns]
    linear = ns

    fig = plt.figure(figsize=(8, 5))
    ax = plt.gca()
    ax.plot(ns, two_pow, label="2^n")
    ax.plot(ns, linear, label="n")
    ax.set_xlabel("n")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(True)
    # If you want a log y-axis to show both on-screen:
    # ax.set_yscale("log")
    plt.tight_layout()
    plt.savefig("chapters/big_o_curves.pdf")

if __name__ == "__main__":
    main()

