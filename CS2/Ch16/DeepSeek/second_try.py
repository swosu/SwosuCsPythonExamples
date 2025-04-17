import timeit
import random
import time
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict

class DataGenerator:
    """Generates random datasets for sorting tests"""
    def __init__(self, size: int = 2000, min_val: int = 1, max_val: int = 10000):
        self.size = size
        self.min_val = min_val
        self.max_val = max_val
    
    def generate(self) -> List[int]:
        """Generate a single dataset of random integers"""
        return [random.randint(self.min_val, self.max_val) for _ in range(self.size)]


class Sorter:
    """Handles sorting operations and timing"""
    @staticmethod
    def bubble_sort(data: List[int]) -> Tuple[List[int], float]:
        """Perform bubble sort and return sorted data with time taken"""
        arr = data.copy()
        start_time = time.time()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        end_time = time.time()
        return arr, end_time - start_time
    
    @staticmethod
    def python_sort(data: List[int]) -> Tuple[List[int], float]:
        """Perform Python's built-in sort and return sorted data with time taken"""
        arr = data.copy()
        start_time = time.time()
        arr.sort()
        end_time = time.time()
        return arr, end_time - start_time


class SortingExperiment:
    """Manages the entire sorting comparison experiment"""
    def __init__(self, runs: int = 10, data_size: int = 128000):
        self.runs = runs
        self.data_size = data_size
        self.data_generator = DataGenerator(size=data_size)
        self.results = {
            'bubble_sort': [],
            'python_sort': [],
            'dataset1_bubble': [],
            'dataset1_python': [],
            'dataset2_bubble': [],
            'dataset2_python': []
        }
    
    def run(self):
        """Execute the sorting experiment across multiple runs"""
        for run in range(self.runs):
            # Generate two different datasets
            dataset1 = self.data_generator.generate()
            dataset2 = self.data_generator.generate()
            
            # Sort dataset1 with both methods
            _, bubble_time1 = Sorter.bubble_sort(dataset1)
            _, python_time1 = Sorter.python_sort(dataset1)
            
            # Sort dataset2 with both methods
            _, bubble_time2 = Sorter.bubble_sort(dataset2)
            _, python_time2 = Sorter.python_sort(dataset2)
            
            # Store results
            self.results['bubble_sort'].append((bubble_time1 + bubble_time2) / 2)
            self.results['python_sort'].append((python_time1 + python_time2) / 2)
            self.results['dataset1_bubble'].append(bubble_time1)
            self.results['dataset1_python'].append(python_time1)
            self.results['dataset2_bubble'].append(bubble_time2)
            self.results['dataset2_python'].append(python_time2)
    
    def plot_results(self):
        """Generate and display plots of the timing results"""
        plt.figure(figsize=(12, 6))
        
        # Plot 1: Comparison of average sorting times
        plt.subplot(1, 2, 1)
        plt.plot(range(1, self.runs+1), self.results['bubble_sort'], label='Bubble Sort (Avg)')
        plt.plot(range(1, self.runs+1), self.results['python_sort'], label='Python Sort (Avg)')
        plt.xlabel('Run Number')
        plt.ylabel('Time (seconds)')
        plt.title('Average Sorting Times Across Both Datasets')
        plt.legend()
        plt.grid(True)
        
        # Plot 2: Individual dataset performance
        plt.subplot(1, 2, 2)
        plt.plot(range(1, self.runs+1), self.results['dataset1_bubble'], label='Dataset 1 Bubble')
        plt.plot(range(1, self.runs+1), self.results['dataset1_python'], label='Dataset 1 Python')
        plt.plot(range(1, self.runs+1), self.results['dataset2_bubble'], label='Dataset 2 Bubble')
        plt.plot(range(1, self.runs+1), self.results['dataset2_python'], label='Dataset 2 Python')
        plt.xlabel('Run Number')
        plt.ylabel('Time (seconds)')
        plt.title('Individual Dataset Sorting Times')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()
    
    def print_summary(self):
        """Print a summary of the timing results"""
        avg_bubble = sum(self.results['bubble_sort']) / self.runs
        avg_python = sum(self.results['python_sort']) / self.runs
        
        print(f"\nSorting Performance Summary ({self.runs} runs, {self.data_size} elements each)")
        print(f"Average Bubble Sort Time: {avg_bubble:.6f} seconds")
        print(f"Average Python Sort Time: {avg_python:.6f} seconds")
        print(f"Bubble Sort is {avg_bubble/avg_python:.1f}x slower than Python's built-in sort")


if __name__ == "__main__":
    # Create and run the experiment
    experiment = SortingExperiment(runs=5, data_size=16000)
    experiment.run()
    
    # Display results
    experiment.print_summary()
    experiment.plot_results()