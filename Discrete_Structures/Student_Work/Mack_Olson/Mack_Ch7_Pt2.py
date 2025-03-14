import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from math import comb

def expected_value(jackpot, num_tickets_sold):
    total_outcomes = comb(49, 6)
    
    # Probability of winning the jackpot
    p_win = 1 / total_outcomes
    
    # Expected winnings assuming a split pot
    expected_winnings = (jackpot / max(1, num_tickets_sold)) * p_win
    
    return expected_winnings

def calculate():
    try:
        jackpot = float(jackpot_entry.get())
        num_tickets_sold = int(ticket_entry.get())
        
        ev = expected_value(jackpot, num_tickets_sold)
        
        result_label.config(text=f"Expected Value: ${ev:.6f}")
        
        if ev > 1:
            messagebox.showinfo("Good Bet!", "The expected value is greater than $1. This may be a profitable bet!")
        else:
            messagebox.showinfo("Bad Bet!", "The expected value is less than $1. This is not a good bet.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

def plot_ev():
    jackpots = np.linspace(1e6, 200e6, 100)  # Simulate jackpot values from $1M to $200M
    num_tickets_sold = int(ticket_entry.get())
    ev_values = [expected_value(j, num_tickets_sold) for j in jackpots]
    
    plt.figure(figsize=(8, 5))
    plt.plot(jackpots, ev_values, label='Expected Value')
    plt.axhline(y=1, color='r', linestyle='--', label='$1 Threshold')
    plt.xlabel("Jackpot Size ($)")
    plt.ylabel("Expected Value ($)")
    plt.title("Expected Value vs Jackpot Size")
    plt.legend()
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("Lottery EV Calculator")

tk.Label(root, text="Jackpot Size ($):").grid(row=0, column=0)
jackpot_entry = tk.Entry(root)
jackpot_entry.grid(row=0, column=1)

tk.Label(root, text="Number of Tickets Sold:").grid(row=1, column=0)
ticket_entry = tk.Entry(root)
ticket_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate EV", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2)

plot_button = tk.Button(root, text="Plot Graph", command=plot_ev)
plot_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
