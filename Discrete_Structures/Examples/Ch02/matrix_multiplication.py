import unittest
import numpy as np

# Matrix Multiplication Function
def matrix_multiply(A, B):
    """Multiplies two matrices A and B using numpy."""
    return np.dot(A, B)

# Unit Test Class
class TestMatrixMultiplication(unittest.TestCase):
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
