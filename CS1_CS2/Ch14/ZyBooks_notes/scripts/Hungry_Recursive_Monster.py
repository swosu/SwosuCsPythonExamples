import sys
import tracemalloc
import random
import string

def hungry_count_down(count, depth=0, payload=None):
    """
    Recursive countdown that *intentionally* consumes a lot of memory per call.
    Each call creates a large list and string, simulating a memory-hungry operation.
    """
    indent = "  " * depth
    frame = sys._getframe()

    if depth == 0:
        print(f"🧭 Recursion limit: {sys.getrecursionlimit()}")
        print("   (We'll stop before hitting it — if we’re lucky.)")

    # build a large payload (each call stores ~1 MB of junk)
    junk = ["".join(random.choices(string.ascii_letters, k=1024)) for _ in range(1024)]
    big_string = "".join(random.choices(string.ascii_letters, k=512*1024))  # 0.5 MB string
    payload = (junk, big_string, payload)  # chain to previous, keeping references alive

    if tracemalloc.is_tracing():
        current, peak = tracemalloc.get_traced_memory()
        print(f"{indent}📦 heap: current={current/1024/1024:.2f} MiB, peak={peak/1024/1024:.2f} MiB")

    print(f"{indent}→ depth={depth}, count={count}, frame_id={id(frame)}")

    if count == 0:
        print(f"{indent}BASE CASE — 💥 Go!")
        return "Go!"
    else:
        result = hungry_count_down(count - 1, depth + 1, payload)
        print(f"{indent}⬆️  returning from depth {depth+1}")
        return result


def demo(n=10):
    """Run the hungry recursion and report heap use."""
    tracemalloc.start()
    try:
        hungry_count_down(n)
    except RecursionError as e:
        print("❌ RecursionError:", e)
    except MemoryError as e:
        print("💣 MemoryError! The monster ran out of snacks:", e)
    finally:
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"\n📈 Peak heap use: {peak/1024/1024:.2f} MiB")
        print("🏁 Done.")


if __name__ == "__main__":
    # lower the count if your machine starts to gasp!
    demo(n=100)
