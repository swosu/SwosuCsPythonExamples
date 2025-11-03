import sys
import os

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} input_file")
    sys.exit(1)

file_name = sys.argv[1]
print(f"Opening file {file_name}...")

if not os.path.exists(file_name):
    print("File does not exist.")
    sys.exit(1)

with open(file_name, "r", encoding="utf-8") as f:
    print("Reading two integers.")
    num1 = int(f.readline())
    num2 = int(f.readline())

print(f"Closing file {file_name}.")
print(f"\nnum1: {num1}")
print(f"num2: {num2}")
print(f"num1 + num2 = {num1 + num2}")
