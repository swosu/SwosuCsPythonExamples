def matrix_multiply(A, B):
    # Get the dimensions of the matrices
    m = len(A)      # number of rows in A
    k = len(A[0])   # number of columns in A (also rows in B)
    n = len(B[0])   # number of columns in B

    # Initialize the result matrix with zero values
    C = [[0 for _ in range(n)] for _ in range(m)]
    
    # Perform matrix multiplication
    for i in range(m):
        for j in range(n):
            for l in range(k):
                C[i][j] += A[i][l] * B[l][j]
    
    return C

# Example matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Matrix multiplication result
result = matrix_multiply(A, B)
print("Matrix AB:")
for row in result:
    print(row)
