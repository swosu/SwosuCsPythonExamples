import tkinter as tk
from scipy.stats import binom
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def birthday_probability(n):
    prob = 1.0
    for i in range(n):
        prob *= (365 - i) / 365
    return 1 - prob

def find_min_people(target_prob):
    n = 1
    while birthday_probability(n) < target_prob:
        n += 1
    return n

def calculate():
    try:
        target = float(entry.get()) / 100  # Convert percentage to decimal
        if target <= 0 or target >= 1:
            result_label.config(text="Please enter a valid percentage between 1 and 99.")
            return
        
        num_people = find_min_people(target)
        result_label.config(text=f"Minimum people needed: {num_people}")
        
        # Generate and plot probability distribution
        x = np.arange(1, num_people + 10)
        y = [birthday_probability(i) for i in x]
        
        plt.figure(figsize=(8, 4))
        ax = sns.lineplot(x=x, y=y, color='red')
        ax.axhline(y=target, color='blue', linestyle='--', label=f'Target: {target*100:.1f}%')
        ax.axvline(x=num_people, color='green', linestyle='--', label=f'Minimum: {num_people}')
        plt.xlabel('Number of People')
        plt.ylabel('Probability of Shared Birthday')
        plt.title('Birthday Paradox Probability')
        plt.legend()
        plt.show()
    except ValueError:
        result_label.config(text="Invalid input. Enter a valid number.")

# Tkinter GUI
root = tk.Tk()
root.title("Birthday Probability Calculator")

tk.Label(root, text="Enter probability percentage:").pack()
entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
