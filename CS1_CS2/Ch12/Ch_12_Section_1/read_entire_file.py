# Example 1: Reading the entire contents of a file
from pathlib import Path
file_path = Path("journal.txt")
if file_path.exists():
with open(file_path, "r", encoding="utf-8") as journal:
contents = journal.read()
print("[Info] Successfully opened journal.txt!\n")
print(contents)
else:
print("[Warning] File 'journal.txt' not found.")

