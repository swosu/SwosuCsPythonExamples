print('hello')

"""
Compare the number of operations and the time needed
to compute Fibonacci numbers recursively versus that
needed to compute them iteratively
"""

class Data_tracker:
    def __init__(self):
        self.data = []
        self.number_of_times_function_called = 0
        self.if_count = 0
        self.add_count = 0
        self.subtract_count = 0
        self.start_time = 0
        self.stop_time = 0
        self.assignment_count = 0

    def increment_assignment_count(self):
        self.assignment_count += 1

    def increment_function_call_count(self):
        self.number_of_times_function_called += 1

    def increment_if_count(self):
        self.if_count += 1

    def increment_add_count(self):
        self.add_count += 1

    def increment_subtract_count(self):
        self.subtract_count += 1

    def print_function_data(self):
        print(f'we called this function {self.number_of_times_function_called} times.')
        print(f'we added {self.add_count} times.')
        print(f'we subtracted {self.subtract_count} times.')
        print(f'we did a if statement {self.if_count} times.')
        print(f'we did an assignment operation {self.assignment_count} times.')
        print("--- %s seconds ---" % (self.stop_time - self.start_time))


# recursive work
# Python program to display the Fibonacci sequence

def recur_fibo(n, recursive_data):
    recursive_data.increment_function_call_count()
    recursive_data.increment_if_count()
    if n <= 1:
        return n
    else:
        recursive_data.increment_add_count()
        recursive_data.increment_subtract_count()
        recursive_data.increment_subtract_count()
        return(recur_fibo(n-1, recursive_data) + recur_fibo(n-2, recursive_data))

import time

recursive_data = Data_tracker()

number_of_terms = 40

recursive_data.start_time = time.time()

# check if the number of terms is valid
if number_of_terms <= 0:
   print("Plese enter a positive integer")
else:
   print(f"Fibonacci number for {number_of_terms} terms:")
   print(recur_fibo((number_of_terms - 1), recursive_data))

recursive_data.stop_time = time.time()

print('\n\nRECUSIVE DATA')
recursive_data.print_function_data()

# iterative work


# https://www.programiz.com/python-programming/examples/fibonacci-sequence

# Program to display the Fibonacci sequence up to n-th term

iterative_data = Data_tracker()

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if number_of_terms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif number_of_terms == 1:
   print("Fibonacci sequence upto",number_of_terms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   iterative_data.start_time = time.time()
   while count < number_of_terms:
       iterative_data.increment_if_count()
       #print(n1)
       iterative_data.increment_add_count()
       nth = n1 + n2
       # update values
       iterative_data.increment_assignment_count()
       n1 = n2
       iterative_data.increment_assignment_count()
       n2 = nth
       iterative_data.increment_assignment_count()
       count += 1

iterative_data.stop_time = time.time()
print('\n\nITERATIVE DATA')
iterative_data.print_function_data()
