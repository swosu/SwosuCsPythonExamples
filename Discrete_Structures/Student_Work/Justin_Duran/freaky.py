import tkinter as tk
from tkinter import messagebox
import time
import random

# Create main window
root = tk.Tk()
root.title("Tower of Hanoi Visualization")

# Create canvas for visualization
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Input field and button
frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Enter number of disks: ").pack(side=tk.LEFT)
entry_disks = tk.Entry(frame)
entry_disks.pack(side=tk.LEFT)

tk.Label(frame, text="Set Timeout (seconds): ").pack(side=tk.LEFT)
timeout_entry = tk.Entry(frame)
timeout_entry.pack(side=tk.LEFT)

solve_button = tk.Button(frame, text="Solve", command=lambda: solve_hanoi())
solve_button.pack(side=tk.LEFT)

# Timer label
timer_label = tk.Label(root, text="Elapsed Time: 0.00s")
timer_label.pack()

# Dropdown menu for theme selection
theme_var = tk.StringVar(value="Light Mode")  # Default theme is light
theme_dropdown = tk.OptionMenu(root, theme_var, "Light Mode", "Dark Mode", "Random Color Mode", "Green Mode", "Blue Mode", command=lambda value: change_theme(value))
theme_dropdown.pack()

# Global Variables
rods = {}
start_time = None
max_time = None
stop_flag = False

snarky_responses = [
    "Negative disks? Did you think the laws of physics were optional?",
    "Oh sure, let's stack negative disks. Brilliant idea!",
    "Negative disks? Why not divide by zero while you're at it?"
]
snarky_responses_timeout = [
    "A negative timeout? What are you trying to do, break the space-time continuum?",
    "Negative timeout? Time-traveling puzzles aren't supported. Yet.",
    "Why not enter a black hole if you're so keen on reversing time?"
]

# Funny messages to pop up when the puzzle is solved
funny_messages = [
    "You did it! Now go outside. The world is not made of disks.",
    "Congrats! You solved it. Are you a wizard or just lucky?",
    "Well done! You can now officially call yourself a diskologist.",
    "Puzzle solved! You deserve a medal... or at least a cookie.",
    "Bravo! You solved it... now, what about that other puzzle? The meaning of life?",
    "Amazing! You're a Tower of Hanoi genius. Don't let it get to your head.",
    "You did it! Now, celebrate like it's your birthday, because you deserve it."
]

# Randomly select a funny message to display
def show_funny_message():
    random_message = random.choice(funny_messages)
    messagebox.showinfo("Success", random_message)

# Functions to change the theme
def change_theme(theme_choice):
    if theme_choice == "Dark Mode":
        root.config(bg="black")
        canvas.config(bg="black")
        timer_label.config(bg="black", fg="white")
        for widget in frame.winfo_children():
            widget.config(bg="black", fg="white")
    elif theme_choice == "Random Color Mode":
        random_color()
    elif theme_choice == "Green Mode":
        # Change to #DFFF00 (Ugly Green)
        root.config(bg="#DFFF00")
        canvas.config(bg="#DFFF00")
        timer_label.config(bg="#DFFF00", fg="black")
        for widget in frame.winfo_children():
            widget.config(bg="#DFFF00", fg="black")
    elif theme_choice == "Light Mode":
        # Light mode with white background
        root.config(bg="white")
        canvas.config(bg="white")
        timer_label.config(bg="white", fg="black")
        for widget in frame.winfo_children():
            widget.config(bg="white", fg="black")
    elif theme_choice == "Blue Mode":
        # Change to red color scheme
        root.config(bg="red")
        canvas.config(bg="red")
        timer_label.config(bg="red", fg="white")
        for widget in frame.winfo_children():
            widget.config(bg="red", fg="white")

def random_color():
    """ Randomly change the background and text color """
    hex_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    root.config(bg=hex_color)
    canvas.config(bg=hex_color)
    timer_label.config(bg=hex_color, fg=random_color_fg())
    for widget in frame.winfo_children():
        widget.config(bg=hex_color, fg=random_color_fg())

def random_color_fg():
    """ Return a random contrasting color for text """
    return "#ffffff" if random.random() > 0.5 else "#000000"

def tower_of_hanoi_visual(number_of_disks, source_rod, target_rod, auxiliary_rod):
    global stop_flag
    if stop_flag:
        return
    if time.time() - start_time > max_time:
        stop_flag = True
        messagebox.showwarning("Timeout", "Womp Womp. Too slow!")
        return

    if number_of_disks == 1:
        move_disk(source_rod, target_rod)
        return
    tower_of_hanoi_visual(number_of_disks - 1, source_rod, auxiliary_rod, target_rod)
    move_disk(source_rod, target_rod)
    tower_of_hanoi_visual(number_of_disks - 1, auxiliary_rod, target_rod, source_rod)

def move_disk(source_rod, target_rod):
    disk = rods[source_rod].pop()
    rods[target_rod].append(disk)
    canvas.after(500)
    draw_rods()
    canvas.update()

    if len(rods["Target"]) == int(entry_disks.get()):
        stop_timer()
        show_funny_message()  # Show one of the funny messages after solving the puzzle

def solve_hanoi():
    global rods, start_time, max_time, stop_flag
    try:
        number_of_disks = int(entry_disks.get())
        if number_of_disks <= 0:
            raise ValueError(random.choice(snarky_responses))

        max_time = float(timeout_entry.get())
        if max_time <= 0:
            raise ValueError(random.choice(snarky_responses_timeout))
    except ValueError as error:
        messagebox.showerror("Invalid Input", str(error))
        return

    rods = {
        "Source": list(range(number_of_disks, 0, -1)),
        "Auxiliary": [],
        "Target": []
    }
    stop_flag = False
    draw_rods()

    start_time = time.time()
    update_timer()

    tower_of_hanoi_visual(number_of_disks, "Source", "Target", "Auxiliary")

def draw_rods():
    canvas.delete("all")
    rod_width = 10
    rod_height = 200
    base_y = 300
    rod_positions = {"Source": 100, "Auxiliary": 300, "Target": 500}

    for rod, x_position in rod_positions.items():
        canvas.create_rectangle(
            x_position - rod_width // 2, base_y - rod_height,
            x_position + rod_width // 2, base_y, fill="black"
        )

    for rod, x_position in rod_positions.items():
        stack = rods[rod]
        for index, disk in enumerate(stack):
            disk_width = disk * 20
            disk_height = 20
            y_position = base_y - (index + 1) * disk_height
            canvas.create_rectangle(
                x_position - disk_width // 2, y_position,
                x_position + disk_width // 2, y_position + disk_height, fill="blue"
            )

def update_timer():
    if stop_flag or not start_time:
        return
    elapsed_time = time.time() - start_time
    timer_label.config(text=f"Elapsed Time: {elapsed_time:.2f}s")
    canvas.after(100, update_timer)

def stop_timer():
    global stop_flag
    stop_flag = True
    elapsed_time = time.time() - start_time
    timer_label.config(text=f"Elapsed Time: {elapsed_time:.2f}s (Completed)")

# Start the Tkinter main loop
root.mainloop()