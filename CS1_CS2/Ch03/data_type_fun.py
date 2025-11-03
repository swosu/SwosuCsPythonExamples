import time

# Step 1: Start with the string
sentence = "the quick brown dog jumped over the lazy Fox"

# Step 2: Convert string -> list of characters
char_list = list(sentence)

# Step 3: Convert list of characters -> Unicode (ord)
unicode_list = [ord(ch) for ch in char_list]

# Step 4: Print Unicode values in a straight line
print("Unicode values (decimal):")
print(" ".join(str(u) for u in unicode_list))

# Step 5: Rebuild characters in a loop, showing progress
rebuilt_chars = []
print("\nBuilding back character by character:\n")

print(f"{'Char':^10} | {'Unicode':^10} | {'Hex':^10}")
print("-" * 34)

for ch, u in zip(char_list, unicode_list):
    rebuilt_chars.append(chr(u))  # convert number back to char
    # Print side by side: char, Unicode decimal, and hex
    print(f"{ch:^10} | {u:^10} | {hex(u):^10}")
    time.sleep(0.25)  # pause for dramatic effect
