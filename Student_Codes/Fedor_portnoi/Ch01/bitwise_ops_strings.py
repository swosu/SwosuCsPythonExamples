def normalize_bits(s: str) -> str:
    return "".join(ch for ch in s.strip() if ch in "01")

def is_bitstring(s: str) -> bool:
    return all(ch in "01" for ch in s)

def bitwise_and(a: str, b: str) -> str:
    return "".join("1" if (x == "1" and y == "1") else "0" for x, y in zip(a, b))

def bitwise_or(a: str, b: str) -> str:
    return "".join("1" if (x == "1" or y == "1") else "0" for x, y in zip(a, b))

def bitwise_xor(a: str, b: str) -> str:
    return "".join("1" if (x != y) else "0" for x, y in zip(a, b))

def main():
    s1 = input("Enter first bit string (e.g., 10110011): ")
    s2 = input("Enter second bit string (same length): ")

    a = normalize_bits(s1)
    b = normalize_bits(s2)

    if not (is_bitstring(a) and is_bitstring(b)):
        raise ValueError("Inputs must be bit strings containing only 0 and 1.")
    if len(a) != len(b):
        raise ValueError(f"Lengths must match. Got {len(a)} and {len(b)}.")

    print("A:", a)
    print("B:", b)
    print("AND:", bitwise_and(a, b))
    print("OR: ", bitwise_or(a, b))
    print("XOR:", bitwise_xor(a, b))

if __name__ == "__main__":
    main()
