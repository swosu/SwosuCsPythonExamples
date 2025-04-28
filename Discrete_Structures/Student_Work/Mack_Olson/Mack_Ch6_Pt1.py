import tkinter as tk
from tkinter import messagebox
from math import comb

def count_cookie_combinations(total_cookies, cookie_types):
    """
    This function calculates the number of ways to choose total_cookies from cookie_types
    using the "stars and bars" combinatorial method.
    
    Parameters:
    total_cookies (int): Total number of cookies to be chosen.
    cookie_types (int): Number of different cookie types.
    
    Returns:
    int: The number of ways to distribute the cookies.
    """
    return comb(total_cookies + cookie_types - 1, cookie_types - 1)

def calculate():
    try:
        total_cookies = int(entry_cookies.get())
        cookie_types = int(entry_types.get())
        result = count_cookie_combinations(total_cookies, cookie_types)
        messagebox.showinfo("Result", f"The number of different ways to choose {total_cookies} cookies from {cookie_types} types is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers for both fields.")

# Create main window
root = tk.Tk()
root.title("Cookie Combinations Calculator")

# Center the window on the screen
window_width = 350
window_height = 75
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

tk.Label(root, text="Enter the total number of cookies:").grid(row=0, column=0)
entry_cookies = tk.Entry(root)
entry_cookies.grid(row=0, column=1)

tk.Label(root, text="Enter the number of different cookie types:").grid(row=1, column=0)
entry_types = tk.Entry(root)
entry_types.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=2, columnspan=2)

root.mainloop()
