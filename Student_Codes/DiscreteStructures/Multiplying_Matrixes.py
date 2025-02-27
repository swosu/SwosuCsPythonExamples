# MATRIX A
# m = 3 columns 
# k1 = 4 rows (k1 , k2 MUST be equal)
matrixA = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
# MATRIX B
# k2 = 4 columns (k1 , k2 MUST be equal)
# n = 3 rows
matrixB = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

def multiply_matrixes(matrixA, matrixB):
    # Get the dimensions of the matrixes
    m = len(matrixA[0]) # Number of columns in matrix A
    k1 = len(matrixA) # Number of rows in matrix A
    k2 = len(matrixB[0]) # Number of columns in matrix B
    n = len(matrixB) # Number of rows in matrix B

    # Check if the matrixes can be multiplied
    if k1 != k2:
        return "The matrixes can't be multiplied"

    # Create the result matrix
    result = [[0 for i in range(n)] for j in range(m)]

    # Multiply the matrixes
    for i in range(m):
        for j in range(n):
            for k in range(k1):
                result[i][j] += matrixA[k][i] * matrixB[j][k]

    return result

# Print the result
print("Matrix A:")
for row in matrixA:
    print(row)

print("Matrix B:")
for row in matrixB:
    print(row)

print("Result:")
for row in multiply_matrixes(matrixA, matrixB):
    print(row)
