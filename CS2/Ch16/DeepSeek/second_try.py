import timeit
import random
import time
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict
from multiprocessing import Process, Queue, cpu_count

class DataGenerator:
    """Generates random datasets for sorting tests"""
    def __init__(self, size: int = 1000, min_val: int = 1, max_val: int = 10000):
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
        
        def worker(data: List[int], queue: Queue):
            """Worker function for parallel sorting"""
            queue.put(Sorter.merge_sort_serial(data))
        
        # Determine number of processes to use
        num_processes = min(cpu_count(), 4)  # Limit to 4 for practical purposes
        chunk_size = len(arr) // num_processes
        chunks = [arr[i*chunk_size:(i+1)*chunk_size] for i in range(num_processes)]
        
        # Handle remainder if array isn't perfectly divisible
        if len(arr) % num_processes != 0:
            chunks[-1].extend(arr[num_processes*chunk_size:])
        
        # Create and start processes
        queue = Queue()
        processes = []
        for chunk in chunks:
            p = Process(target=worker, args=(chunk, queue))
            processes.append(p)
            p.start()
        
        # Collect results
        sorted_chunks = []
        for _ in range(num_processes):
            sorted_chunks.append(queue.get())
        
        # Wait for all processes to finish
        for p in processes:
            p.join()
        
        # Merge the sorted chunks
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
    def __init__(self, runs: int = 10, data_size: int = 1000):
        self.runs = runs
        self.data_size = data_size
        self.data_generator = DataGenerator(size=data_size)
        self.results = {
            'bubble_sort': [],
            'python_sort': [],
            'parallel_merge': [],
            'dataset1_bubble': [],
            'dataset1_python': [],
            'dataset1_parallel': [],
            'dataset2_bubble': [],
            'dataset2_python': [],
            'dataset2_parallel': []
        }
    
    def run(self):
        """Execute the sorting experiment across multiple runs"""
        for run in range(self.runs):
            # Generate two different datasets
            dataset1 = self.data_generator.generate()
            dataset2 = self.data_generator.generate()
            
            # Sort dataset1 with all methods
            _, bubble_time1 = Sorter.bubble_sort(dataset1)
            _, python_time1 = Sorter.python_sort(dataset1)
            _, parallel_time1 = Sorter.parallel_merge_sort(dataset1)
            
            # Sort dataset2 with all methods
            _, bubble_time2 = Sorter.bubble_sort(dataset2)
            _, python_time2 = Sorter.python_sort(dataset2)
            _, parallel_time2 = Sorter.parallel_merge_sort(dataset2)
            
            # Store results
            self.results['bubble_sort'].append((bubble_time1 + bubble_time2) / 2)
            self.results['python_sort'].append((python_time1 + python_time2) / 2)
            self.results['parallel_merge'].append((parallel_time1 + parallel_time2) / 2)
            self.results['dataset1_bubble'].append(bubble_time1)
            self.results['dataset1_python'].append(python_time1)
            self.results['dataset1_parallel'].append(parallel_time1)
            self.results['dataset2_bubble'].append(bubble_time2)
            self.results['dataset2_python'].append(python_time2)
            self.results['dataset2_parallel'].append(parallel_time2)
    
    def plot_results(self):
        """Generate and display plots of the timing results"""
        plt.figure(figsize=(15, 6))
        
        # Plot 1: Comparison of average sorting times
        plt.subplot(1, 2, 1)
        plt.plot(range(1, self.runs+1), self.results['bubble_sort'], label='Bubble Sort (Avg)')
        plt.plot(range(1, self.runs+1), self.results['python_sort'], label='Python Sort (Avg)')
        plt.plot(range(1, self.runs+1), self.results['parallel_merge'], label='Parallel Merge (Avg)')
        plt.xlabel('Run Number')
        plt.ylabel('Time (seconds)')
        plt.title('Average Sorting Times Across Both Datasets')
        plt.legend()
        plt.grid(True)
        
        # Plot 2: Individual dataset performance
        plt.subplot(1, 2, 2)
        plt.plot(range(1, self.runs+1), self.results['dataset1_bubble'], 'C0--', label='Dataset 1 Bubble')
        plt.plot(range(1, self.runs+1), self.results['dataset1_python'], 'C1--', label='Dataset 1 Python')
        plt.plot(range(1, self.runs+1), self.results['dataset1_parallel'], 'C2--', label='Dataset 1 Parallel')
        plt.plot(range(1, self.runs+1), self.results['dataset2_bubble'], 'C0-', label='Dataset 2 Bubble')
        plt.plot(range(1, self.runs+1), self.results['dataset2_python'], 'C1-', label='Dataset 2 Python')
        plt.plot(range(1, self.runs+1), self.results['dataset2_parallel'], 'C2-', label='Dataset 2 Parallel')
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
        avg_parallel = sum(self.results['parallel_merge']) / self.runs
        
        print(f"\nSorting Performance Summary ({self.runs} runs, {self.data_size} elements each)")
        print(f"Average Bubble Sort Time: {avg_bubble:.6f} seconds")
        print(f"Average Python Sort Time: {avg_python:.6f} seconds")
        print(f"Average Parallel Merge Sort Time: {avg_parallel:.6f} seconds")
        print(f"\nSpeed Comparisons:")
        print(f"Bubble Sort is {avg_bubble/avg_python:.1f}x slower than Python's built-in sort")
        print(f"Parallel Merge is {avg_python/avg_parallel:.1f}x {'faster' if avg_parallel < avg_python else 'slower'} than Python's built-in sort")
        print(f"Parallel Merge is {avg_bubble/avg_parallel:.1f}x faster than Bubble Sort")


if __name__ == "__main__":
    # Create and run the experiment
    print(f"Available CPU cores: {cpu_count()}")
    experiment = SortingExperiment(runs=5, data_size=16000)
    experiment.run()
    
    # Display results
    experiment.print_summary()
    experiment.plot_results()