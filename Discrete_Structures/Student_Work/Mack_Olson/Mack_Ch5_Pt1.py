import time
import tkinter as tk
from tkinter import messagebox

def fibonacci_iterative(number):
    step_count = 0  # Count the number of steps
    if number <= 0:
        return 0, step_count
    elif number == 1:
        return 1, step_count
    
    previous_value, current_value = 0, 1
    for index in range(number - 1):
        step_count += 1
        previous_value, current_value = current_value, previous_value + current_value #this line as well
    return current_value, step_count #work on objectifying it

def fibonacci_recursive(number, step_count=0):
    if number <= 0:
        return 0, step_count + 1
    elif number == 1:
        return 1, step_count + 1
    
    fibonacci_value_one, step_count_one = fibonacci_recursive(number - 1, step_count)
    fibonacci_value_two, step_count_two = fibonacci_recursive(number - 2, step_count)
    return fibonacci_value_one + fibonacci_value_two, step_count_one + step_count_two + 1

def measure_time_and_steps():
    try:
        number = int(entry_number.get())
        
        # Measure iterative approach
        start_time = time.time()
        fibonacci_value_iterative, step_count_iterative = fibonacci_iterative(number)
        iterative_time = time.time() - start_time
        
        # Measure recursive approach
        start_time = time.time()
        fibonacci_value_recursive, step_count_recursive = fibonacci_recursive(number)
        recursive_time = time.time() - start_time
        
        result_text.set(f"Fibonacci({number}) = {fibonacci_value_iterative}\n"
                        f"Iterative: Steps = {step_count_iterative}, Time = {iterative_time:.6f} sec\n"
                        f"Recursive: Steps = {step_count_recursive}, Time = {recursive_time:.6f} sec")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer")

# GUI Setup
root = tk.Tk()
root.title("Fibonacci Calculator")

tk.Label(root, text="Enter a number:").pack()
entry_number = tk.Entry(root)
entry_number.pack()

tk.Button(root, text="Calculate", command=measure_time_and_steps).pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.pack()

root.mainloop()
