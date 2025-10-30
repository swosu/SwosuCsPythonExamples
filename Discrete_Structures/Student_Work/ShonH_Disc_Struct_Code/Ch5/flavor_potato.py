import sys
import time

# Let’s give the potato a bigger frying pan
sys.setrecursionlimit(3000)

def spicy_potato(depth=1):
    """A dramatic recursive dive for htop enthusiasts."""
    print(f"🌶️ Depth {depth} — Potato still sizzling...")
    time.sleep(0.01)  # Slow it down for dramatic flair

    # Base case: when to stop before meltdown
    if depth >= 2500:
        print(f"🔥 SPICY LIMIT REACHED at depth {depth}! Potato is fully cooked!")
        return depth

    # Keep digging deeper
    return spicy_potato(depth + 1)

if __name__ == "__main__":
    print("🥔 Launching spicy potato recursion demo...")
    spicy_potato()
    print("✅ Program exited gracefully — no stack overflow today!")

