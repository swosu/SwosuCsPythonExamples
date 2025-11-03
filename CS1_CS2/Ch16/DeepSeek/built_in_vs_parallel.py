import random
import time
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict
from multiprocessing import Pool, cpu_count
import numpy as np

class DataGenerator:
    """Generates random datasets for sorting tests"""
    def __init__(self, min_val: int = 1, max_val: int = 10000):
        self.min_val = min_val
        self.max_val = max_val
    
    def generate(self, size: int) -> List[int]:
        """Generate a single dataset of random integers"""
        return [random.randint(self.min_val, self.max_val) for _ in range(size)]


class Sorter:
    """Handles sorting operations and timing"""
    @staticmethod
    def python_sort(data: List[int]) -> Tuple[List[int], float]:
        """Perform Python's built-in sort and return sorted data with time taken"""
        arr = data.copy()
        start_time = time.time()
        arr.sort()
        end_time = time.time()
        return arr, end_time - start_time
    
    @staticmethod
    def merge(left: List[int], right: List[int]) -> List[int]:
        """Merge two sorted lists"""
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    @staticmethod
    def merge_sort_serial(data: List[int]) -> List[int]:
        """Standard recursive merge sort (serial)"""
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = Sorter.merge_sort_serial(data[:mid])
        right = Sorter.merge_sort_serial(data[mid:])
        return Sorter.merge(left, right)
    
    @staticmethod
    def parallel_merge_sort(data: List[int]) -> Tuple[List[int], float]:
        """Parallel merge sort using multiprocessing"""
        arr = data.copy()
        start_time = time.time()
        
        # Use a Pool instead of individual Processes
        with Pool(processes=min(cpu_count(), 4)) as pool:
            size = len(arr)
            chunk_size = size // pool._processes
            chunks = [arr[i*chunk_size:(i+1)*chunk_size] for i in range(pool._processes)]
            
            # Handle remainder
            if size % pool._processes != 0:
                chunks[-1].extend(arr[pool._processes*chunk_size:])
            
            # Map chunks to workers
            sorted_chunks = pool.map(Sorter.merge_sort_serial, chunks)
            
            # Merge the results
            while len(sorted_chunks) > 1:
                new_chunks = []
                for i in range(0, len(sorted_chunks), 2):
                    if i+1 < len(sorted_chunks):
                        new_chunks.append(Sorter.merge(sorted_chunks[i], sorted_chunks[i+1]))
                    else:
                        new_chunks.append(sorted_chunks[i])
                sorted_chunks = new_chunks
        
        end_time = time.time()
        return sorted_chunks[0], end_time - start_time


class SortingExperiment:
    """Manages the entire sorting comparison experiment"""
    def __init__(self, runs: int = 5, dataset_sizes: List[int] = [1000, 5000, 10000, 50000, 100000]):
        self.runs = runs
        self.dataset_sizes = dataset_sizes
        self.data_generator = DataGenerator()
        self.results = {
            size: {
                'python_sort': [],
                'parallel_merge': [],
                'python_avg': 0,
                'parallel_avg': 0
            } for size in dataset_sizes
        }
    
    def run(self):
        """Execute the sorting experiment across multiple runs and dataset sizes"""
        for size in self.dataset_sizes:
            print(f"\nTesting with dataset size: {size}")
            
            python_times = []
            parallel_times = []
            
            for run in range(self.runs):
                dataset = self.data_generator.generate(size)
                
                # Sort with Python's built-in sort
                _, python_time = Sorter.python_sort(dataset)
                python_times.append(python_time)
                
                # Sort with parallel merge sort
                _, parallel_time = Sorter.parallel_merge_sort(dataset)
                parallel_times.append(parallel_time)
                
                print(f"Run {run+1}: Python={python_time:.6f}s, Parallel={parallel_time:.6f}s")
            
            # Store results for this dataset size
            self.results[size]['python_sort'] = python_times
            self.results[size]['parallel_merge'] = parallel_times
            self.results[size]['python_avg'] = sum(python_times) / self.runs
            self.results[size]['parallel_avg'] = sum(parallel_times) / self.runs
    
    def plot_results(self):
        """Generate and display plots of the timing results"""
        plt.figure(figsize=(12, 6))
        
        # Prepare data for plotting
        sizes = sorted(self.dataset_sizes)
        python_avgs = [self.results[size]['python_avg'] for size in sizes]
        parallel_avgs = [self.results[size]['parallel_avg'] for size in sizes]
        
        # Plot 1: Average times by dataset size
        plt.subplot(1, 2, 1)
        plt.plot(sizes, python_avgs, 'o-', label='Python Sort')
        plt.plot(sizes, parallel_avgs, 's-', label='Parallel Merge')
        plt.xlabel('Dataset Size')
        plt.ylabel('Average Time (seconds)')
        plt.title('Sorting Performance by Dataset Size')
        plt.legend()
        plt.grid(True)
        
        # Plot 2: Speedup ratio
        plt.subplot(1, 2, 2)
        speedup = [py/pl for py, pl in zip(python_avgs, parallel_avgs)]
        plt.plot(sizes, speedup, 'd-', label='Speedup (Python/Parallel)')
        plt.axhline(1, color='red', linestyle='--', label='Break-even')
        plt.xlabel('Dataset Size')
        plt.ylabel('Speedup Ratio')
        plt.title('Parallel Speedup Over Python Sort')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()
    
    def print_summary(self):
        """Print a summary of the timing results"""
        print("\nSorting Performance Summary")
        print(f"{'Dataset Size':>12} | {'Python Avg (s)':>14} | {'Parallel Avg (s)':>16} | {'Speedup':>8} |")
        print("-" * 65)
        
        for size in sorted(self.dataset_sizes):
            py_avg = self.results[size]['python_avg']
            pl_avg = self.results[size]['parallel_avg']
            speedup = py_avg / pl_avg
            print(f"{size:12,} | {py_avg:14.6f} | {pl_avg:16.6f} | {speedup:8.2f}x |")


if __name__ == "__main__":
    # Configuration - easily adjustable
    RUNS = 5
    DATASET_SIZES = [100000, 500000, 1000000, 5000000, 10000000]  # Can add more sizes here
    
    print(f"Available CPU cores: {cpu_count()}")
    print(f"Testing with dataset sizes: {DATASET_SIZES}")
    
    # Create and run the experiment
    experiment = SortingExperiment(runs=RUNS, dataset_sizes=DATASET_SIZES)
    experiment.run()
    
    # Display results
    experiment.print_summary()
    experiment.plot_results()