import random
import time
import tracemalloc
import matplotlib.pyplot as plt


class SortingAlgorithmComparison:
    """
    A class to compare the performance of Quicksort and Selection Sort
    with varying input sizes in terms of time taken and memory usage.
    """
    def __init__(self):
        """
        Initializes data structures for storing performance results.
        """
        self.input_sizes = []
        self.quicksort_times = []
        self.selection_sort_times = []
        self.quicksort_memory = []
        self.selection_sort_memory = []

    def quicksort(self, array):
        """
        Sorts an array using the Quicksort algorithm.
        """
        if len(array) <= 1:
            return array

        pivot = array[-1]
        left = [x for x in array[:-1] if x <= pivot]
        right = [x for x in array[:-1] if x > pivot]
        return self.quicksort(left) + [pivot] + self.quicksort(right)

    def selection_sort(self, array):
        """
        Sorts an array using the Selection Sort algorithm.
        """
        for i in range(len(array)):
            min_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
        return array

    def measure_sorting_performance(self, array, sort_function):
        """
        Measures the time and memory usage for a given sorting function and array.
        """
        # Measure memory usage
        tracemalloc.start()
        start_time = time.perf_counter()
        sort_function(array.copy())  # Sort a copy to avoid modifying the original
        end_time = time.perf_counter()
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Return time and memory usage
        return end_time - start_time, peak_memory

    def run_comparison(self, start_size=10, max_size=1_000_000, step_multiplier=10):
        """
        Runs the comparison for input sizes ranging from start_size to max_size.
        """
        current_size = start_size
        while current_size <= max_size:
            # Generate a random array of the current size
            array = [random.randint(1, 1000) for _ in range(current_size)]

            # Measure Quicksort performance
            quicksort_time, quicksort_memory = self.measure_sorting_performance(array, self.quicksort)

            # Measure Selection Sort performance
            selection_sort_time, selection_sort_memory = self.measure_sorting_performance(array, self.selection_sort)

            # Store the results
            self.input_sizes.append(current_size)
            self.quicksort_times.append(quicksort_time)
            self.selection_sort_times.append(selection_sort_time)
            self.quicksort_memory.append(quicksort_memory)
            self.selection_sort_memory.append(selection_sort_memory)

            print(f"Size: {current_size}, Quicksort Time: {quicksort_time:.4f}s, "
                  f"Selection Sort Time: {selection_sort_time:.4f}s")

            # Increase the size for the next iteration
            current_size *= step_multiplier

    def plot_results(self):
        """
        Plots the results of the performance comparison.
        """
        # Plot time comparisons
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.plot(self.input_sizes, self.quicksort_times, label="Quicksort", marker='o')
        plt.plot(self.input_sizes, self.selection_sort_times, label="Selection Sort", marker='x')
        plt.xscale("log")
        plt.yscale("log")
        plt.xlabel("Input Size")
        plt.ylabel("Time (seconds)")
        plt.title("Sorting Time vs Input Size")
        plt.legend()
        plt.grid(True)

        # Plot memory comparisons
        plt.subplot(1, 2, 2)
        plt.plot(self.input_sizes, self.quicksort_memory, label="Quicksort", marker='o')
        plt.plot(self.input_sizes, self.selection_sort_memory, label="Selection Sort", marker='x')
        plt.xscale("log")
        plt.xlabel("Input Size")
        plt.ylabel("Memory (bytes)")
        plt.title("Memory Usage vs Input Size")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    comparison = SortingAlgorithmComparison()
    comparison.run_comparison()
    comparison.plot_results()
