import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Cashier's Algorithm")

# Function to calculate change denominations
def calculate_change():
    try:
        # Get the total and payment values from the input fields
        total = float(total_entry.get())
        payment = float(payment_entry.get())
        
        # Calculate the change amount
        change = payment - total
        
        # Check if payment is sufficient
        if change >= 0:
            # Define the available denominations
            denominations = [50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
            change_dict = {}
            
            # Calculate the number of each denomination
            for denom in denominations:
                num_denom = int(change / denom)
                if num_denom > 0:
                    change_dict[denom] = num_denom
                    change -= num_denom * denom
            
            # Display the change denominations
            change_text.delete(1.0, tk.END)  # Clear previous text
            for denom, count in change_dict.items():
                change_text.insert(tk.END, f"${denom}: {count}\n")
        else:
            change_text.delete(1.0, tk.END)
            change_text.insert(tk.END, "Insufficient payment!")

    except ValueError:
        change_text.delete(1.0, tk.END)
        change_text.insert(tk.END, "Invalid input!")

# Generate random total and payment values
total_value = round(random.uniform(0.01, 100), 2)
payment_value = round(random.uniform(total_value + 0.01, total_value + 100), 2)

# Create and configure GUI elements
total_label = tk.Label(root, text="Total Amount:")
total_label.pack()
total_entry = tk.Entry(root)
total_entry.insert(0, total_value)
total_entry.pack()

payment_label = tk.Label(root, text="Payment Amount:")
payment_label.pack()
payment_entry = tk.Entry(root)
payment_entry.insert(0, payment_value)
payment_entry.pack()

calculate_button = tk.Button(root, text="Calculate Change", command=calculate_change)
calculate_button.pack()

change_label = tk.Label(root, text="Change Denominations:")
change_label.pack()
change_text = tk.Text(root, height=10, width=30)
change_text.pack()

# Start the GUI main loop
root.mainloop()
