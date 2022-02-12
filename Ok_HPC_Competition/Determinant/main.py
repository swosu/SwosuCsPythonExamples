print('hello.')

import binary_file_reader

obj = binary_file_reader.binary_file_reader()
c = obj.get_sum(3,8)
print(c)

matrix_side_length = 16

matrix = obj.load_matrix(matrix_side_length)
