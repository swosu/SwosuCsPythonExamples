import numpy as np
import math
import time

import binary_file_reader
import upper_triangular
import find_diagonal

np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})

matrix_side_length = 16

reader = binary_file_reader.binary_file_reader()
matrix = reader.load_matrix(matrix_side_length)
#print(matrix)

start_time = time.perf_counter()

upper_triangular_handler = upper_triangular.upper_triangular()
upper_triangular_matrix = upper_triangular_handler.make_upper_triangular(matrix)
#print(upper_triangular_matrix)

mather = find_diagonal.find_diagonal()
determinant_values = mather.work_multiply_diagonal(upper_triangular_matrix)






end_time = time.perf_counter()
print(f'matrix side length: {matrix_side_length}.')
print(f'our determinant is {determinant_values[0]:.6e}.')
print(f'The log of the absolute value determinant is {determinant_values[1]:.6e}.')
elapsed_time = end_time - start_time
print(f"Process completed in {elapsed_time:0.2e} seconds")
