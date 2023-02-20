import time

start_time = time.time()

#breaks at 998
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

def fibonacci_recursive(num):
    operation_counter.function_call_count += 1
    if num <= 1:
        return num
    else:
        operation_counter.subtract_1_count += 1
        operation_counter.subtract_2_count += 1
        return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)


if __name__ == '__main__':
    print(fibonacci_recursive(25))

    end_time = time.time()
    total_time = end_time - start_time

    print(f"It took {total_time} seconds to run the program")
    print(f"you called fibonacci {operation_counter.GetFunctionCount()} times")
    print(f"you subtracted 1 {operation_counter.GetSubtract1Count()} times")
    print(f"you subtracted 2 {operation_counter.GetSubtract2Count()} times")

