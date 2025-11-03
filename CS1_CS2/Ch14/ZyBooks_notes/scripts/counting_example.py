def count_down(count, depth=0):
    """Recursive countdown with detailed debugging output."""
    
    # Create indentation to visualize recursion depth
    indent = "  " * depth
    
    print(f"{indent}🔍 Entering count_down(count={count}) at depth {depth}")

    if count == 0:
        print(f"{indent}💥 Base case reached! count == 0")
        print(f"{indent}🎉 Go!")
    else:
        print(f"{indent}➡️ Not at base case yet. Printing {count} and recursing deeper...")
        print(f"{indent}🧩 Before recursive call: count = {count}")
        
        # Recursive call — here’s where we “go deeper into the tunnel”
        count_down(count - 1, depth + 1)
        
        # When recursion returns, we pop back up the call stack
        print(f"{indent}⬆️ Returning from depth {depth + 1} to depth {depth}")
        print(f"{indent}🧠 Post-recursion: count = {count}")

    print(f"{indent}✅ Exiting count_down(count={count})")

# Run the countdown
print("🚀 Starting recursive countdown...\n")
count_down(3)
print("\n🏁 Countdown complete!")
