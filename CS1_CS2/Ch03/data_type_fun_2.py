# Alphabet Data Structure Explorer
import string

def show_table(letters):
    print(f"{'Char':^6} | {'Dec':^6} | {'Hex':^6} | {'Oct':^6} | {'Bin':^10}")
    print("-" * 44)
    for ch in letters:
        u = ord(ch)
        print(f"{ch:^6} | {u:^6} | {hex(u):^6} | {oct(u):^6} | {bin(u):^10}")

print("Lowercase Alphabet\n")
show_table(string.ascii_lowercase)

print("\nUppercase Alphabet\n")
show_table(string.ascii_uppercase)
