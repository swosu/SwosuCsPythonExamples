import sys
import math

def factorial(n):
    """Recursive factorial to show recursion nesting."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def scramble_collect(remaining, built_word="", results=None):
    """
    Fast version of the recursive scrambler:
    Collects permutations in a list instead of printing them.
    """
    if results is None:
        results = []

    # Base case
    if not remaining:
        results.append(built_word)
        return results

    # Recursive case
    for i, letter in enumerate(remaining):
        next_remaining = remaining[:i] + remaining[i+1:]
        scramble_collect(next_remaining, built_word + letter, results)
    
    return results

def scramble_driver():
    """Run a fast scramble, factorial check, and uniqueness analysis."""
    word = input("Enter a word to scramble: ").strip()

    print(f"\n🎬 Starting fast scramble for '{word}'...\n")

    # Step 1: factorial check
    n = len(word)
    theoretical_total = factorial(n)
    print(f"🧮 Letters: {n}")
    print(f"📈 Theoretical permutations (n!): {theoretical_total:,}")

    # Step 2: scramble and measure results
    print("⚡️ Generating permutations (this may take a moment)...")
    all_perms = scramble_collect(word)

    actual_total = len(all_perms)
    unique_total = len(set(all_perms))

    print(f"\n🗂️ Total permutations generated: {actual_total:,}")
    print(f"🎯 Unique permutations (via set): {unique_total:,}")

    # Step 3: comparison
    print("\n🔍 Analysis:")
    if unique_total < actual_total:
        print("   → There are duplicates! That means your word has repeated letters.")
        print("   → The set removes duplicates — giving only unique word forms.")
    else:
        print("   → Every permutation was unique. No duplicate letters in this word!")

    print(f"\nExample permutations: {all_perms[:10]} ...")

if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    scramble_driver()
