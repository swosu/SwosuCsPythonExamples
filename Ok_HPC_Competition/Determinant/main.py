import numpy as np

import binary_file_reader
import upper_triangular

np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})

matrix_side_length = 16

reader = binary_file_reader.binary_file_reader()
matrix = reader.load_matrix(matrix_side_length)
print(matrix)

upper_triangular_handler = upper_triangular.upper_triangular()
upper_triangular_matrix = upper_triangular_handler.make_upper_triangular(matrix)
print(upper_triangular_matrix)

diagonal_multiply_value = 1
diagonal_log_add_value = 0

for diagonal_index in range (0, matrix_side_length):
    diagonal_multiply_value = diagonal_multiply_value * \
    upper_triangular_matrix[diagonal_index][diagonal_index]

print(f'our determinant is {diagonal_multiply_value}.')
