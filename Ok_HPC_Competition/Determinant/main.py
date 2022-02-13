import numpy as np

import binary_file_reader
import upper_triangular

matrix_side_length = 16

reader = binary_file_reader.binary_file_reader()

matrix = reader.load_matrix(matrix_side_length)
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
print(matrix)
