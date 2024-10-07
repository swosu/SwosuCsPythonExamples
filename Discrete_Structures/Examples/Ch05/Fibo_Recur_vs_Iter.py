import time
import csv

class DataTracker:
    def __init__(self):
        self.additions = 0
        self.function_calls = 0
        self.variable_assignments = 0
        self.list_writes = 0
        self.start_time = None
        self.end_time = None

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()

    def get_elapsed_time(self):
        return self.end_time - self.start_time

    def reset(self):
        self.additions = 0
        self.function_calls = 0
        self.variable_assignments = 0
        self.list_writes = 0
        self.start_time = None
        self.end_time = None


def Fibo_iterative(n, tracker):
    tracker.start_timer()
    fib_sequence = []
    a, b = 0, 1
    tracker.variable_assignments += 2  # for a, b initialization

    for i in range(n):
        fib_sequence.append(a)
        tracker.list_writes += 1  # Writing to the list
        tracker.variable_assignments += 2  # a, b reassignments
        tracker.additions += 1  # addition operation a + b
        a, b = b, a + b

    tracker.stop_timer()
    return fib_sequence


def Fibo_recursive(n, tracker):
    tracker.start_timer()

    def fib_rec(x):
        tracker.function_calls += 1  # Track recursive function calls
        if x <= 1:
            return x
        else:
            tracker.additions += 1  # addition operation
            return fib_rec(x - 1) + fib_rec(x - 2)

    result = [fib_rec(i) for i in range(n)]
    tracker.list_writes += n  # Each result is written to the list

    tracker.stop_timer()
    return result


def log_to_csv(iter_tracker, rec_tracker):
    # Log both methods' results on the same line
    with open('Fibo_Comparison_Notes.xls', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'Iterative vs Recursive',
            iter_tracker.additions, iter_tracker.function_calls, iter_tracker.variable_assignments, iter_tracker.list_writes, iter_tracker.get_elapsed_time(),
            rec_tracker.additions, rec_tracker.function_calls, rec_tracker.variable_assignments, rec_tracker.list_writes, rec_tracker.get_elapsed_time()
        ])


# Create two DataTracker instances
iter_tracker = DataTracker()
rec_tracker = DataTracker()

# Generate Fibonacci sequence iteratively and recursively
n = 10

# Run iterative method and collect metrics
Fibo_iterative(n, iter_tracker)

# Run recursive method and collect metrics
Fibo_recursive(n, rec_tracker)

# Log both method metrics on a single line in the CSV
log_to_csv(iter_tracker, rec_tracker)
