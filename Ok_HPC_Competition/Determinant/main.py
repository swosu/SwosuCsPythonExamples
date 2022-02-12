print('hello.')

import binary_file_reader
import numpy as np

obj = binary_file_reader.binary_file_reader()
c = obj.get_sum(3,8)
print(c)

matrix_side_length = 16

matrix = obj.load_matrix(matrix_side_length)
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
print(matrix)
