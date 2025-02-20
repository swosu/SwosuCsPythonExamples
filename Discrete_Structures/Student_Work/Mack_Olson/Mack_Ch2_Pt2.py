def matrix_multiply(A, B):
    """Multiply two matrices A and B."""
    if len(A[0]) != len(B):
        return "Invalid matrix dimensions for multiplication."
    
    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    return result

# Get user input for matrix dimensions
def get_matrix_input(rows, cols, name):
    print(f"Enter elements for matrix {name} row-wise:")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input().split()))
                if len(row) != cols:
                    raise ValueError
                matrix.append(row)
                break
            except ValueError:
                print(f"Invalid input! Please enter {cols} integers separated by spaces.")
    return matrix

m = int(input("Enter number of rows for matrix A: "))
k = int(input("Enter number of columns for matrix A (and rows for matrix B): "))
n = int(input("Enter number of columns for matrix B: "))

# Get matrices from user
A = get_matrix_input(m, k, 'A')
B = get_matrix_input(k, n, 'B')

# Perform multiplication
result = matrix_multiply(A, B)
if isinstance(result, str):
    print(result)
else:
    print("Resultant matrix:")
    for row in result:
        print(" ".join(map(str, row)))