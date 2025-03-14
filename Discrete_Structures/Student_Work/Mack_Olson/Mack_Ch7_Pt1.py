import tkinter as tk
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def birthday_probability(num_people):
    """Calculates the probability that at least two people in a group share a birthday."""
    probability = 1.0
    for person in range(num_people):
        probability *= (366 - person) / 366
    return 1 - probability

def find_minimum_people(target_probability):
    """Finds the minimum number of people needed to reach the target probability."""
    num_people = 1
    while birthday_probability(num_people) < target_probability:
        num_people += 1
    return num_people

def calculate_probability():
    """Handles the calculation and updates the UI with results."""
    try:
        target_percentage = float(entry_target_probability.get()) / 100  # Convert percentage to decimal
        if target_percentage <= 0 or target_percentage >= 1:
            label_result.config(text="Please enter a valid percentage between 1 and 99.")
            return
        
        minimum_people = find_minimum_people(target_percentage)
        label_result.config(text=f"Minimum number of people needed: {minimum_people}")
        
        # Generate and plot probability distribution
        people_range = np.arange(1, minimum_people + 10)
        probability_values = [birthday_probability(group_size) for group_size in people_range]
        
        plt.figure(figsize=(8, 4))
        ax = sns.lineplot(x=people_range, y=probability_values, color='red')
        ax.axhline(y=target_percentage, color='blue', linestyle='--', 
                   label=f'Target Probability: {target_percentage * 100:.1f}%')
        ax.axvline(x=minimum_people, color='green', linestyle='--', 
                   label=f'Minimum People: {minimum_people}')
        plt.xlabel('Number of People in Group')
        plt.ylabel('Probability of Shared Birthday')
        plt.title('Probability of at Least Two People Sharing a Birthday')
        plt.legend()
        plt.show()
    except ValueError:
        label_result.config(text="Invalid input. Please enter a valid number.")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Birthday Paradox Probability Calculator")

tk.Label(root, text="Enter target probability percentage:").pack()
entry_target_probability = tk.Entry(root)
entry_target_probability.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate_probability)
button_calculate.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
