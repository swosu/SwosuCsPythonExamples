class find_diagonal:


    def __init__(self):
        self.sum_ = 0
        self.file_name = ''
        self.matrix = []

    def work_multiply_diagonal(self,upper_triangular_matrix):
        import math

        print('start of work multiply diagonal.')
        diagonal_multiply_value = 1
        diagonal_log_add_value = 0
        determinant_values = [1, 0]

        matrix_side_length = len(upper_triangular_matrix)
        print(f'inside function, matrix side length is: {matrix_side_length}.')

        for diagonal_index in range (0, matrix_side_length):
            diagonal_multiply_value = diagonal_multiply_value * \
            upper_triangular_matrix[diagonal_index][diagonal_index]

            diagonal_log_add_value = diagonal_log_add_value + \
            math.log10(abs(upper_triangular_matrix[diagonal_index][diagonal_index]))

        determinant_values[0] = diagonal_multiply_value
        determinant_values[1] = diagonal_log_add_value
        return determinant_values
