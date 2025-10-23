# Example 3: Reading a file line by line — the right way

from pathlib import Path

print("📖 Let's open 'readme.txt' and read it line by line!")

# Step 1: Always use a context manager (`with open`) so the file closes automatically
file_path = Path("readme.txt")

if not file_path.exists():
    print("🚨 Oops! 'readme.txt' not found. Please create it and try again.")
else:
    # Open safely with UTF-8 decoding for portability
    with open(file_path, "r", encoding="utf-8", errors="replace") as my_file:
        print("✅ File opened successfully!\n")

        # Step 2: Read all lines into a list
        lines = my_file.readlines()

        # Step 3: Process the lines
        print(f"🧮 Found {len(lines)} lines in 'readme.txt'\n")

        # Print each line with its line number
        for index, line in enumerate(lines, start=1):
            clean_line = line.strip()  # Removes \n and whitespace
            print(f"Line {index:>2}: {clean_line}")

        # Step 4: Show something interesting from the content
        print("\n✨ Text Magic ✨")
        # Combine all words and find the longest one
        all_words = " ".join(lines).split()
        longest_word = max(all_words, key=len)
        print(f"🪄 Longest word in the file: '{longest_word}'")

        # Reverse the lines to see the story backwards
        print("\n🌀 Reading the file in reverse order:\n")
        for rev_index, line in enumerate(reversed(lines), start=1):
            print(f"Reverse {rev_index:>2}: {line.strip()}")

print("\n📚 End of file processing.\n")

# 🧠 Why this is good practice:
# • Using 'with open(...)' ensures the file closes automatically, even if errors occur.
# • Using 'encoding=\"utf-8\"' avoids weird Windows decoding errors.
# • Using Path() makes file handling cross-platform and readable.
# • Looping line-by-line is memory-efficient for big files.
# • Stripping lines and enumerating helps visualize line positions clearly.
