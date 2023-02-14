import time

class Operation_Counter:
    def __init__(self, name):
        self.name = name
        self.function_call_count = 0
        self.comparison_call_count = 0
        self.addition_call_count = 0
        self.subtraction_call_count = 0
        self.multiplication_call_count = 0
        self.start_time = time.time()
        self.stop_time = time.time()
        self.time_difference = self.stop_time - self.start_time

    def set_start_time(self):
        self.start_time = time.time()

    def set_stop_time(self):
        self.stop_time = time.time()

    def get_time_difference(self):
        return self.stop_time - self.start_time

    def __call__(self, *args, **kwargs):
        self.count += 1
        print('Call {} to {}.'.format(self.count, self.name))

    def incrament_function_call(self):
        self.function_call_count += 1
    
    def incrament_comparison_call(self):
        self.comparison_call_count += 1

    def incrament_addition_call(self):
        self.addition_call_count += 1

    def incrament_subtraction_call(self):
        self.subtraction_call_count += 1

    def incrament_multiplication_call(self):
        self.multiplication_call_count += 1

    def get_function_call_count(self):
        return self.function_call_count

    def get_comparison_count(self):
        return self.comparison_call_count

def factorial(x, operation_counter):
    operation_counter.incrament_function_call()
    """This is a recursive function
    to find the factorial of an integer"""
    operation_counter.incrament_comparison_call()
    if x == 1:
        return 1
    else:
        operation_counter.incrament_multiplication_call()
        operation_counter.incrament_subtraction_call()
        return (x * factorial(x-1, operation_counter))


num = 3

recursive_operation_data = Operation_Counter('recursive factorial')
recursive_operation_data.set_start_time()
print("The factorial of", num, "is", factorial(num, recursive_operation_data))
recursive_operation_data.set_stop_time()

print('The factorial function was called {} times.'
.format(recursive_operation_data.get_function_call_count()))

print(f'the factorial function had {recursive_operation_data.get_comparison_count()} comparisons.')

print(f'the factorial function had {recursive_operation_data.addition_call_count} additions.')

print(f'the factorial function had {recursive_operation_data.subtraction_call_count} subtractions.')

print(f'the factorial function had {recursive_operation_data.multiplication_call_count} multiplications.')

print(f'the factorial function took {recursive_operation_data.get_time_difference()} seconds to run.')
