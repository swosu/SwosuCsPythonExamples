import sys
import tracemalloc

def count_down(count, depth=0):
    """
    Recursive countdown with detailed 'what gets saved where' narration.
    Each call:
      - Uses one C stack frame (return address, registers, etc.).
      - Allocates a Python frame object on the heap:
          * locals: count, depth, indent
          * links: f_back (caller), code object, globals, etc.
    When we return, that Python frame becomes collectible and the C stack
    frame is popped.
    """
    # --- Visual aid for nesting ---
    indent = "  " * depth

    # --- Introspect the current Python frame (on the heap) ---
    frame = sys._getframe()  # current frame object (heap-allocated in CPython)

    if depth == 0:
        print(f"🧭 Recursion limit (guardrail): {sys.getrecursionlimit()}")
        print("   (Largest safe n ≈ recursion_limit - 1; keep a little buffer.)")

    # --- Trace memory, if tracemalloc is running ---
    if tracemalloc.is_tracing():
        current, peak = tracemalloc.get_traced_memory()
        print(f"{indent}📦 heap: current={current/1024:.1f} KiB, peak={peak/1024:.1f} KiB")

    # --- Narrate what we're pushing onto the stack/heap this call ---
    print(f"{indent}→ call depth={depth}, count={count}, frame_id={id(frame)}")

    if count == 0:
        print(f"{indent}BASE CASE: count == 0 → print('Go!') and return")
        print(f"{indent}Go!")
        print(f"{indent}← pop frame depth={depth} (C stack shrinks; Python frame collectible)")
        return "Go!"
    else:
        print(f"{indent}Saving locals in frame: count={count}, depth={depth}")
        print(f"{indent}We will recurse with count-1 → {count-1}")
        result = count_down(count - 1, depth + 1)
        print(f"{indent}Returned from depth={depth+1} with {result!r}")
        print(f"{indent}← pop frame depth={depth} (unwinding the call stack)")
        return result


def demo(n=5, trace_memory=True):
    """
    Runs the countdown with optional heap tracing and shows safe depth guidance.
    """
    if trace_memory and not tracemalloc.is_tracing():
        tracemalloc.start()

    try:
        print("\n🚀 Starting recursive countdown demo")
        count_down(n)
    except RecursionError as e:
        print("❌ RecursionError:", e)
    finally:
        if tracemalloc.is_tracing():
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(f"\n📈 Peak Python heap traced during recursion: {peak/1024:.1f} KiB")
        print("🏁 Done.\n")


if __name__ == "__main__":
    # Pro tip: check first; don't blindly crank this up.
    # sys.setrecursionlimit(2000)  # ⚠️ Dangerous if set too high—can segfault.
    print(f"Python says recursion limit is: {sys.getrecursionlimit()}")
    # Choose a conservative n well under the limit (limit-50 is a nice classroom rule of thumb).
    demo(n=min(sys.getrecursionlimit() - 50, 20))
