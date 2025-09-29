#!/usr/bin/env python3
import os
import subprocess
import time

# List of demos to run
DEMOS = [
    ("CPU-Bound Pi Approximation", "cpu_bound_find_pi.py"),
    ("Memory-Bound Matrix Multiply", "memory_bound_matrix_multiply.py"),
    ("GPU Matrix Multiply", "cuda_matrix_multiply.py"),
]

def countdown(seconds=5):
    for i in range(seconds, 0, -1):
        print(f"  Starting in {i}...", flush=True)
        time.sleep(1)
    print(">>> GO!\n")

def run_demo(name, script):
    print("="*60)
    print(f"🔥 Demo: {name}")
    print("="*60)
    countdown(5)
    try:
        subprocess.run(["python3", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {script}: {e}")
    print("\n")

if __name__ == "__main__":
    for demo_name, demo_script in DEMOS:
        run_demo(demo_name, demo_script)

    print("="*60)
    print("✅ All demos complete! Show this machine some respect 😎")
    print("="*60)

