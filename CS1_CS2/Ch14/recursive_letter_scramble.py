import sys

def show_recursion_limit():
    """Display the current recursion limit."""
    #print(f"🐍 Python recursion limit: {sys.getrecursionlimit()} frames\n")

def scramble_word(remaining, built_word, depth=0):
    """
    Recursively build and print all permutations of a word.
    
    Each call:
    - Chooses one letter from 'remaining'
    - Adds it to 'built_word'
    - Calls itself with the smaller 'remaining' set
    """
    indent = "│  " * depth  # Visually show depth in output

    # Base case: no letters left
    if not remaining:
        #print(f"{indent}✅ Complete word: {built_word}")
        return

    # Recursive case: choose each letter in turn
    #print(f"{indent}→ Depth {depth}: remaining='{remaining}', built='{built_word}'")

    for i, letter in enumerate(remaining):
        # Choose this letter
        next_remaining = remaining[:i] + remaining[i+1:]
        next_built = built_word + letter

        #print(f"{indent}  Picking '{letter}' → next_remaining='{next_remaining}'")

        # Recursive descent
        scramble_word(next_remaining, next_built, depth + 1)

        # After returning, this frame resumes here
        #print(f"{indent}  ↩️ Returning to depth {depth} after exploring '{letter}'")

def scramble_driver():
    """Run a demonstration with user input and stack awareness."""
    show_recursion_limit()
    word = input("Enter a word to scramble: ").strip()
    print(f"\n🎬 Starting recursion for '{word}'...\n")
    scramble_word(word, "")

if __name__ == "__main__":
    scramble_driver()
