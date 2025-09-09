#!/usr/bin/env python3
"""
bitwiseoperations.py

Author: Justin Wiederkehr
Description: This script demonstrates bitwise operations in Python.
"""

def main():
    # Example bitwise operations
    a = 5  # 0b0101
    b = 3  # 0b0011

    print(f"a = {a} ({bin(a)})")
    print(f"b = {b} ({bin(b)})")
    print(f"a & b = {a & b} ({bin(a & b)})")   # Bitwise AND
    print(f"a | b = {a | b} ({bin(a | b)})")   # Bitwise OR
    print(f"a ^ b = {a ^ b} ({bin(a ^ b)})")   # Bitwise XOR
    print(f"~a = {~a} ({bin(~a)})")            # Bitwise NOT
    print(f"a << 1 = {a << 1} ({bin(a << 1)})") # Left shift
    print(f"a >> 1 = {a >> 1} ({bin(a >> 1)})") # Right shift

if __name__ == "__main__":
    main()