def matmul(A, B):
    m, k = len(A), len(A[0])
    k2, n = len(B), len(B[0])
    if k != k2:
        raise ValueError(f"Inner dimensions must match: A is {m}x{k}, B is {k2}x{n}.")
    C = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for t in range(k):
                C[i][j] += A[i][t] * B[t][j]
    return C

def pretty_print(M, name="Matrix"):
    print(f"{name} ({len(M)}x{len(M[0]) if M else 0}):")
    for row in M:
        print(" ".join(f"{x:g}" for x in row))
    print()

def main():
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    C = matmul(A, B)

    pretty_print(A, "A")
    pretty_print(B, "B")
    pretty_print(C, "A * B")

if __name__ == "__main__":
    main()
