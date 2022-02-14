class upper_triangular:


    def __init__(self):
        self.sum_ = 0
        self.file_name = ''
        self.matrix = []

    def get_sum(self,num1,num2):
        self.sum_ = num1+num2
        return self.sum_

    def make_upper_triangular(self, matrix):
        import numpy as np
        row_count = len(matrix)
        print(f'row count is: {row_count}')
        column_count = len(matrix[0])
        print(f'column count is: {column_count}')

        upper_triangular_matrix = matrix.copy()

        #for column_to_zero_index in range(0, 3):
        for column_to_zero_index in range(0, column_count - 1):

            print(f'\n\n\ncolumn to work to 0s is: {column_to_zero_index}.')

            squishing_factor_denominator = \
            upper_triangular_matrix[column_to_zero_index][column_to_zero_index]
            print(f'squishing_factor_denominator is: {squishing_factor_denominator}.')

            #for row_to_work_index in range(column_to_zero_index + 1, 4):
            for row_to_work_index in range(column_to_zero_index + 1, row_count):

                print(f'\n\nwe want to work on row: {row_to_work_index}.')
                squishing_factor_numerator = \
                upper_triangular_matrix[row_to_work_index][column_to_zero_index]
                print(f'squishing_factor_numerator is: {squishing_factor_numerator}.')
                squishing_factor = \
                squishing_factor_numerator / squishing_factor_denominator

                #for column_inside_index in range(column_to_zero_index, 5):
                for column_inside_index in range(column_to_zero_index, column_count):

                    print(f'\ncolumn_inside_index is: {column_inside_index}.')

                    upper_triangular_matrix[row_to_work_index][column_inside_index] = \
                    upper_triangular_matrix[row_to_work_index][column_inside_index] - \
                    squishing_factor * \
                    upper_triangular_matrix[column_to_zero_index][column_inside_index]

                    if(column_inside_index == column_to_zero_index):
                        print(f'after squishing, the leading number is: {upper_triangular_matrix[row_to_work_index][column_inside_index]}.')

                #print('finished the row')
                #print(upper_triangular_matrix)

        return upper_triangular_matrix
