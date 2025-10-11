def next_permutation(a):

    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i == 0:
        return False

    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    a[i:] = reversed(a[i:])
    return True


def generate_lex_permutations(n):
    a = list(range(1, n + 1))
    yield a[:]
    while next_permutation(a):
        yield a[:]


def main():
    import sys
    try:
        n = int(input().strip())
        if n <= 0:
            raise ValueError
    except Exception:
        print("Please enter a positive integer n.")
        sys.exit(1)

    for p in generate_lex_permutations(n):
        print(" ".join(map(str, p)))


if __name__ == "__main__":
    main()
