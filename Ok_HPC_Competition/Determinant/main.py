import numpy as np
import math
import time

import binary_file_reader
import upper_triangular
import find_diagonal

np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})

matrix_side_length = 512

# Read in the data
reader = binary_file_reader.binary_file_reader()
matrix = reader.load_matrix(matrix_side_length)
#print(matrix)

start_time = time.perf_counter()

# find the upper triangular matrix
upper_triangular_handler = upper_triangular.upper_triangular()
upper_triangular_matrix = upper_triangular_handler.make_upper_triangular(matrix)
#print(upper_triangular_matrix)

# work the diagonal to find the determinant
mather = find_diagonal.find_diagonal()
determinant_values = mather.work_multiply_diagonal(upper_triangular_matrix)

# calculate time to complete process.
end_time = time.perf_counter()
elapsed_time = end_time - start_time

# print results
#print(f'\n\nProcess completed in {elapsed_time:0.2e} seconds')
#print(f'matrix side length: {matrix_side_length}.')
#print(f'our determinant is {determinant_values[0]:.6e}.')
#print(f'The log of the absolute value determinant is {determinant_values[1]:.6e}.')

print(elapsed_time)
print(matrix_side_length)
print(determinant_values[0])
print(determinant_values[1])

print(f'\n\nmatrix side length')
print(f'seconds')
print(f'determinant')
print(f'log abs')

print(f'\n\n{matrix_side_length}')
print(f'{elapsed_time:0.2e}')
print(f'{determinant_values[0]:.6e}')
print(f'{determinant_values[1]:.6e}')
