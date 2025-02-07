import unittest
import numpy as np

# Matrix Multiplication Function
def matrix_multiply(A, B):
    """Multiplies two matrices A and B using numpy."""
    # Get the dimensions of the matrices
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Check if multiplication is possible
    if cols_A != rows_B:
        raise ValueError("Cannot multiply matrices: incompatible dimensions.")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Unit Test Class
class TestMatrixMultiplication(unittest.TestCase):

    def test_1x3_times_3x1(self):
        A = np.array([[2, 5, 6]])
        B = np.array([[3],
                      [4],
                      [-5]])
        expected = np.array([[-4]])
        np.testing.assert_array_equal(matrix_multiply(A, B), expected)

    def test_3x1_times_1x3(self):
        A = np.array([[2],
                      [5],
                      [6]])
        B = np.array([[3, 4, -5]])
        expected = np.array([[6, 8, -10],
                             [15, 20, -25],
                             [18, 24, -30]])
        np.testing.assert_array_equal(matrix_multiply(A, B), expected)

    def test_3x1_times_1x3_v2(self):
        A = np.array([[2, 5, 6]])
        B = np.array([[3],
                      [4],
                      [-5]])
        expected = np.array([[6, 15, 18],
                             [8, 20, 24],
                             [-10, -25, -30]])
        np.testing.assert_array_equal(matrix_multiply(B, A), expected)

    def test_2x3_times_3x4(self):
        A = np.array([[1, 4, -2],
                      [3, 5, -6]])
        B = np.array([[5, 2, 8, -1],
                      [3, 6, 4, 5],
                      [-2, 9, 7, -3]])
        expected = np.array([[21, 8, 10, 25],
                             [42, -18, 2, 40]])
        np.testing.assert_array_equal(matrix_multiply(A, B), expected)
    def test_4x4_multiplication(self):
        A = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])
        B = np.array([[17, 18, 19, 20],
                      [21, 22, 23, 24],
                      [25, 26, 27, 28],
                      [29, 30, 31, 32]])
        expected = np.array([[250, 260, 270, 280],
                             [618, 644, 670, 696],
                             [986, 1028, 1070, 1112],
                             [1354, 1412, 1470, 1528]])
        np.testing.assert_array_equal(matrix_multiply(A, B), expected)

    def test_2x4_times_4x2(self):
        A = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8]])
        B = np.array([[9, 10],
                      [11, 12],
                      [13, 14],
                      [15, 16]])
        expected = np.array([[130, 140],
                             [322, 348]])
        np.testing.assert_array_equal(matrix_multiply(A, B), expected)

if __name__ == '__main__':
    unittest.main()
