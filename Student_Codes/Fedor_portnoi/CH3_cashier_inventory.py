import argparse
from decimal import Decimal, ROUND_HALF_UP

def parse_amount_to_cents(s: str) -> int:
    if s.isdigit():
        return int(s)
    amt = Decimal(s).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return int(amt * 100)

def parse_inventory(s: str) -> list[tuple[int,int]]:
    parts = [p.strip() for p in s.split(",") if p.strip()]
    inv = []
    for p in parts:
        if "x" in p:
            d, c = p.split("x", 1)
            inv.append((int(d), int(c)))
        else:
            inv.append((int(p), 10**9))
    inv.sort(reverse=True, key=lambda x: x[0])
    return inv

def greedy_with_inventory(cents: int, inventory: list[tuple[int,int]]):
    used = {}
    remaining = cents
    for denom, count in inventory:
        take = min(remaining // denom, count)
        used[denom] = take
        remaining -= take * denom
    return used, remaining

def format_output(used: dict[int,int], remaining: int) -> str:
    lines = []
    for d in sorted(used.keys(), reverse=True):
        lines.append(f"{d}: {used[d]}")
    lines.append(f"leftover_cents: {remaining}")
    return "\n".join(lines)

def main():
    p = argparse.ArgumentParser(description="Greedy cashier with limited inventory.")
    p.add_argument("amount", type=str, help="Amount in dollars (e.g., 12.34) or cents (e.g., 1234).")
    p.add_argument("--inventory", type=str, default="100x10,25x10,10x10,5x10,1x100", help="Comma list of <denom>x<count>. Omit 'x<count>' for unlimited.")
    args = p.parse_args()

    cents = parse_amount_to_cents(args.amount)
    inv = parse_inventory(args.inventory)
    used, leftover = greedy_with_inventory(cents, inv)
    print(format_output(used, leftover))

if __name__ == "__main__":
    main()
