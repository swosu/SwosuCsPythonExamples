import time
import csv
import tracemalloc
import matplotlib.pyplot as plt

class OperationTracker:
    def __init__(self):
        self.reset()

    def reset(self):
        self.adds = 0
        self.subs = 0
        self.func_calls = 0

    def log(self, adds=0, subs=0, func_calls=0):
        self.adds += adds
        self.subs += subs
        self.func_calls += func_calls

class FibonacciAnalyzer:
    def __init__(self):
        self.tracker = OperationTracker()

    def fibonacci_recursive(self, n):
        self.tracker.log(func_calls=1)
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        self.tracker.log(adds=1)
        return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    def fibonacci_iterative(self, n):
        self.tracker.log(func_calls=1)
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(2, n + 1):
            self.tracker.log(adds=1)
            a, b = b, a + b
        return b if n > 0 else a

    def analyze(self, method, n):
        self.tracker.reset()
        tracemalloc.start()
        start_time = time.perf_counter()
        result = method(n)
        elapsed_time = time.perf_counter() - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return {
            "result": result,
            "adds": self.tracker.adds,
            "subs": self.tracker.subs,
            "calls": self.tracker.func_calls,
            "time": elapsed_time,
            "memory": peak
        }

def write_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Fibo Num",
            "Recursive Adds", "Recursive Subtracts", "Recursive Func Calls", "Recursive Time", "Recursive Memory",
            "Iterative Adds", "Iterative Subtracts", "Iterative Func Calls", "Iterative Time", "Iterative Memory"
        ])
        for row in data:
            writer.writerow([
                row["n"],
                row["recursive"]["adds"], row["recursive"]["subs"], row["recursive"]["calls"], row["recursive"]["time"], row["recursive"]["memory"],
                row["iterative"]["adds"], row["iterative"]["subs"], row["iterative"]["calls"], row["iterative"]["time"], row["iterative"]["memory"]
            ])

def plot_graphs(data):
    ns = [row["n"] for row in data]
    recursive_mem = [row["recursive"]["memory"] / 1024 for row in data]  # KB
    iterative_mem = [row["iterative"]["memory"] / 1024 for row in data]

    plt.figure(figsize=(10, 6))
    plt.plot(ns, recursive_mem, label="Recursive Memory (KB)", marker='o')
    plt.plot(ns, iterative_mem, label="Iterative Memory (KB)", marker='o')
    plt.title("Memory Usage by Fibonacci Method")
    plt.xlabel("Fibonacci Number (n)")
    plt.ylabel("Memory Usage (KB)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    filename = r"C:\Users\evertj\git\SwosuCsPythonExamples\Discrete_Structures\Examples\Ch05\fibonacci_rec_vs_iter.csv"
    analyzer = FibonacciAnalyzer()
    data = []

    for n in range(0, 6):
        recursive = analyzer.analyze(analyzer.fibonacci_recursive, n)
        iterative = analyzer.analyze(analyzer.fibonacci_iterative, n)
        data.append({
            "n": n,
            "recursive": recursive,
            "iterative": iterative
        })

    write_csv(filename, data)
    plot_graphs(data)

if __name__ == "__main__":
    main()
