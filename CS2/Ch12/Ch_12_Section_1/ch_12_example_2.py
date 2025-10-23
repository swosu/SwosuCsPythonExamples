# Example 2 (refined): Reading a text file safely with UTF-8 encoding and commentary

from pathlib import Path
import traceback

# Step 1: Announce the mission
print("🗃️ Attempting to open 'myfile.txt' with universal UTF-8 decoder...")

# Step 2: Check for file existence before opening
# (This provides a cleaner control flow than handling FileNotFoundError later)
file_path = Path("myfile.txt")
if not file_path.exists():
    print("🚨 File not found! Make sure 'myfile.txt' exists in this directory.")
    contents = ""
else:
    try:
        # Step 3: Use a context manager (with-statement) for automatic closing
        # encoding='utf-8' ensures proper handling of Unicode; errors='replace' avoids crash
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            print("✅ File opened successfully — exotic characters will be handled gracefully.")
            contents = f.read()
            print("✨ Reading complete!")

    except FileNotFoundError:
        # This branch is mostly redundant due to the pre-check, but it's good pedagogy to include
        print("🚨 FileNotFoundError caught — file may have been deleted mid-run.")
        contents = ""

    except Exception as e:
        # ⚠️ Catching Exception is a double-edged sword:
        # - ✅ Pros: prevents crashes and gives friendly messages for beginners
        # - ❌ Cons: can silently hide real bugs or IO errors that need attention
        # Here we’ll print AND log the full traceback for clarity during development
        print(f"💥 Unexpected error while reading file: {e}")
        traceback.print_exc()  # Developers see what went wrong
        contents = ""
        # Optional: re-raise to crash intentionally if stability is important
        # raise

# Step 4: Display what was read
print("\n--- Contents of myfile.txt ---")
print(contents if contents else "(No readable content found)")
print("--- End of file ---\n")

# Step 5: Perform simple text analysis
if contents:
    print("🔍 Performing advanced text analysis...\n")

    word_count = len(contents.split())
    line_count = len(contents.splitlines())
    char_count = len(contents)

    print(f"📏 Number of lines: {line_count}")
    print(f"🧮 Number of words: {word_count}")
    print(f"🔡 Number of characters: {char_count}\n")

    # Step 6: Find the most common word
    words = [w.strip(".,!?").lower() for w in contents.split()]
    most_common = max(set(words), key=words.count)
    print(f"👑 Most common word: '{most_common}'")

    # Step 7: Add a dramatic flourish
    print("\n🌀 Reading the file backwards (for dramatic effect):\n")
    print(contents[::-1])
    print("\n✨ End of reverse reading ✨")

else:
    print("⚠️ Nothing to analyze — file was empty, missing, or unreadable.")

# Notes for the adventurous coder:
# --------------------------------
# • pathlib.Path gives clearer and more cross-platform path handling.
# • In production, avoid swallowing Exception silently — log it or re-raise it.
# • For exact byte preservation (e.g., binary or unknown encodings), use:
#     open(file_path, "rb")   # read bytes directly
# • For best practice in production, detect encoding via 'chardet' or 'charset_normalizer'.
# • Always validate and sanitize file contents before processing in security-sensitive applications.
# • Consider using 'with' for all file operations to ensure proper resource management.