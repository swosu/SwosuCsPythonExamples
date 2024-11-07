import time
import math
import csv

# create a class to keep track of the number of times the function is called
# and the number of multiplications performed
# and the number of subtractions performed
# and the number of comparisons performed

class Factorial_Data_Counter:
    def __init__(self):
        self.function_call_count = 0
        self.multiplication_count = 0
        self.subtraction_count = 0
        self.comparison_count = 0
    
    def increment_function_call_count(self):
        self.function_call_count += 1

    def increment_multiplication_count(self):
        self.multiplication_count += 1

    def increment_subtraction_count(self):
        self.subtraction_count += 1

    def increment_comparison_count(self):
        self.comparison_count += 1




def factorial_loop(number, loop_data):
    print('the number is', number)
    output = 1
    for index in range(1, number + 1):
        loop_data.increment_comparison_count()
        #print('the index is', index, 'the output is', output)
        output *= index
        loop_data.increment_multiplication_count()
    loop_data.increment_comparison_count()
    return output

def factorial_recursive(number, recursive_data):
    #print('the number is', number)
    if number == 1:
        recursive_data.increment_comparison_count()
        return 1
    else:
        recursive_data.increment_comparison_count()
        recursive_data.increment_multiplication_count()
        recursive_data.increment_subtraction_count()
        return number * factorial_recursive(number - 1, recursive_data)
        print('I LIKE FISH!!!'  )
    

if __name__ == '__main__':

    # open the csv file factorial_recursive_data.csv
    csv_file_path = 'factorial_recursive_data.csv'

    # open the csv file in append mode
    with open(csv_file_path, 'a') as csv_file:

        csv_writer = csv.writer(csv_file)

        # write the data header to the csv file
        csv_writer.writerow(['number', 'loop multiplications', 'loop comparisons', 'recursive function calls', 'recursive multiplications', 'recursive comparisons', 'recursive subtractions', 'loop time', 'math time', 'recursive time'])
        for number in range(1, 1201):

            loop_data = Factorial_Data_Counter()
            recursive_data = Factorial_Data_Counter()

            loop_time_start = time.time()
            print('loop result: ', factorial_loop(number, loop_data))
            loop_time_end = time.time()
            print('the loop time is', loop_time_end - loop_time_start)
            print('the loop multiplications are', loop_data.multiplication_count)
            print('the loop comparisons are', loop_data.comparison_count)

            math_factorial_start = time.time()
            print('math result: ', math.factorial(number))
            math_factorial_end = time.time()
            print('the math time is', math_factorial_end - math_factorial_start)

            recursive_factorial_start = time.time()
            print('recursive result: ', factorial_recursive(number, recursive_data))
            recursive_factorial_end = time.time()
            print('the recursive time is', recursive_factorial_end - recursive_factorial_start)
            print('the recursive multiplications are', recursive_data.multiplication_count)
            print('the recursive comparisons are', recursive_data.comparison_count)
            print('the recursive subtractions are', recursive_data.subtraction_count)
            print('the recursive function calls are', recursive_data.function_call_count)


            # write the data to the csv file
            csv_writer.writerow([number, loop_data.multiplication_count, loop_data.comparison_count, recursive_data.comparison_count, recursive_data.multiplication_count, recursive_data.comparison_count, recursive_data.subtraction_count, loop_time_end - loop_time_start, math_factorial_end - math_factorial_start, recursive_factorial_end - recursive_factorial_start])