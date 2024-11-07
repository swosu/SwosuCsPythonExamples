import time

start_time = time.time()

class OperationCounter:
    def __init__(self):
        self.function_call_count = 0
        self.subtract_1_count = 0
        self.subtract_2_count = 0

    def GetFunctionCount(self):
        return self.function_call_count

    def GetSubtract1Count(self):
        return self.subtract_1_count

    def GetSubtract2Count(self):
        return self.subtract_2_count



operation_counter = OperationCounter()


def fibonacci_iterative(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        # Initialize variables to store the first two numbers in the sequence
        a, b = 0, 1
        # Loop through the sequence up to n, updating a and b at each step
        for index in range(2, num+1):
            operation_counter.function_call_count += 1
            c = a + b
            a = b
            b = c
        return b


if __name__ == '__main__':

    print(fibonacci_iterative(100000))

    end_time = time.time()
    total_time = end_time - start_time

    print(f"You looped through the for loop {operation_counter.GetFunctionCount()} times")
    print(f"The total time this took was {total_time}")