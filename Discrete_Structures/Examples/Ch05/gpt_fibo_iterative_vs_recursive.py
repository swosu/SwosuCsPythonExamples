import time
import csv

class OperationTracker:
    def __init__(self):
        self.reset()

    def reset(self):
        self.function_calls = 0
        self.additions = 0
        self.subtractions = 0
        self.memory_assignments = 0

    def log_operation(self, function_calls=0, additions=0, subtractions=0, memory_assignments=0):
        self.function_calls += function_calls
        self.additions += additions
        self.subtractions += subtractions
        self.memory_assignments += memory_assignments

class FibonacciResult:
    def __init__(self, n, time_iterative, tracker_iterative, time_recursive, tracker_recursive):
        self.fibo_number = n
        self.time_iterative = time_iterative
        self.tracker_iterative = tracker_iterative
        self.time_recursive = time_recursive
        self.tracker_recursive = tracker_recursive

class FibonacciCalculator:
    def __init__(self):
        self.tracker = OperationTracker()

    def fibonacci_recursive(self, fibo_number):
        self.tracker.log_operation(function_calls=1)
        if fibo_number <= 0:
            return 0
        elif fibo_number == 1:
            return 1
        self.tracker.log_operation(additions=1)
        return self.fibonacci_recursive(fibo_number - 1) + self.fibonacci_recursive(fibo_number - 2)

    def fibonacci_iterative(self, fibo_number):
        self.tracker.log_operation(memory_assignments=2)
        previous = 0
        current = 1
        for current_index in range(fibo_number):
            self.tracker.log_operation(additions=1, memory_assignments=2)
            next_value = previous + current
            previous = current
            current = next_value
        return previous

    def measure_time_and_operations(self, fibo_number):
        # Measure iterative method
        self.tracker.reset()
        start_time = time.time()
        self.fibonacci_iterative(fibo_number)
        elapsed_time_iterative = time.time() - start_time
        tracker_iterative = self.tracker.__dict__.copy()
        
        # Measure recursive method
        self.tracker.reset()
        start_time = time.time()
        self.fibonacci_recursive(fibo_number)
        elapsed_time_recursive = time.time() - start_time
        tracker_recursive = self.tracker.__dict__.copy()
        
        return FibonacciResult(fibo_number, elapsed_time_iterative, tracker_iterative, elapsed_time_recursive, tracker_recursive)

def main():
    filename = r"C:\Users\evertj\git\SwosuCsPythonExamples\Discrete_Structures\Examples\Ch05\fibonacci_comparison.csv"
    calculator = FibonacciCalculator()
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Fibo Num", "Iterative Time (s)", "Iterative Function Calls", "Iterative Additions", "Iterative Subtractions", "Iterative Memory Assignments", "Recursive Time (s)", "Recursive Function Calls", "Recursive Additions", "Recursive Subtractions", "Recursive Memory Assignments"])
        
        for fibo_number in range(1, 5):
            print(f"Calculating for n = {fibo_number}")
            result = calculator.measure_time_and_operations(fibo_number)
            writer.writerow([
                result.fibo_number,
                result.time_iterative, result.tracker_iterative['function_calls'], result.tracker_iterative['additions'], result.tracker_iterative['subtractions'], result.tracker_iterative['memory_assignments'],
                result.time_recursive, result.tracker_recursive['function_calls'], result.tracker_recursive['additions'], result.tracker_recursive['subtractions'], result.tracker_recursive['memory_assignments']
            ])

if __name__ == "__main__":
    print("Hello World!")
    main()
