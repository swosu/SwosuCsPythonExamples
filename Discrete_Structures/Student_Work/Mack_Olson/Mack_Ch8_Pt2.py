import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
import matplotlib.pyplot as plt

class FibonacciPrimeFinder:
    def __init__(self):
        self.fibonacci_numbers = [0, 1]
        self.prime_fibonacci_numbers = []
        self.is_running = True

    def generate_next_fibonacci(self):
        next_number = self.fibonacci_numbers[-1] + self.fibonacci_numbers[-2]
        self.fibonacci_numbers.append(next_number)
        return next_number

    @staticmethod
    def is_prime_number(number):
        if number < 2:
            return False
        if number in (2, 3):
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        divisor = 5
        while divisor * divisor <= number:
            if number % divisor == 0 or number % (divisor + 2) == 0:
                return False
            divisor += 6
        return True

    def find_prime_fibonacci_numbers(self, duration_seconds, update_callback):
        start_time = time.time()
        while self.is_running and (time.time() - start_time < duration_seconds):
            fibonacci_value = self.generate_next_fibonacci()
            if self.is_prime_number(fibonacci_value):
                self.prime_fibonacci_numbers.append(fibonacci_value)
            update_callback(len(self.prime_fibonacci_numbers))
        self.is_running = False


class FibonacciPrimeGUI:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("Prime Fibonacci Finder")

        self.finder = FibonacciPrimeFinder()

        self.label_timer = ttk.Label(root_window, text="Time Elapsed: 0s", font=("Arial", 12))
        self.label_timer.pack(pady=5)

        self.label_count = ttk.Label(root_window, text="Prime Fibonacci Numbers Found: 0", font=("Arial", 12))
        self.label_count.pack(pady=5)

        self.label_duration = ttk.Label(root_window, text="Enter Time (seconds):", font=("Arial", 12))
        self.label_duration.pack(pady=5)

        self.entry_duration = ttk.Entry(root_window, font=("Arial", 12))
        self.entry_duration.pack(pady=5)
        self.entry_duration.insert(0, "60")  # Default value

        self.start_button = ttk.Button(root_window, text="Start Search", command=self.start_search)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(root_window, text="Stop Search", command=self.stop_search, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.chart_button = ttk.Button(root_window, text="Show Chart", command=self.show_chart, state=tk.DISABLED)
        self.chart_button.pack(pady=5)

        self.is_running = False
        self.start_time = None
        self.duration_seconds = 60  # Default to 60 seconds

    def update_ui(self, prime_count):
        elapsed_time = int(time.time() - self.start_time)
        self.label_timer.config(text=f"Time Elapsed: {elapsed_time}s")
        self.label_count.config(text=f"Prime Fibonacci Numbers Found: {prime_count}")
        if elapsed_time >= self.duration_seconds:
            self.stop_search()

    def start_search(self):
        try:
            self.duration_seconds = int(self.entry_duration.get())
            if self.duration_seconds <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for time duration.")
            return

        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.chart_button.config(state=tk.DISABLED)

        self.start_time = time.time()
        self.finder.is_running = True

        search_thread = threading.Thread(target=self.finder.find_prime_fibonacci_numbers, args=(self.duration_seconds, self.update_ui))
        search_thread.daemon = True
        search_thread.start()

    def stop_search(self):
        self.finder.is_running = False
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.chart_button.config(state=tk.NORMAL)

    def show_chart(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.finder.prime_fibonacci_numbers, marker='o', linestyle='-', color='b')
        plt.xlabel("Index")
        plt.ylabel("Prime Fibonacci Number")
        plt.title("Prime Fibonacci Numbers Found")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    root_window = tk.Tk()
    app_instance = FibonacciPrimeGUI(root_window)
    root_window.mainloop()
