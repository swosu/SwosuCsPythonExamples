import itertools
import tkinter as tk
from tkinter import ttk, messagebox

class PermutationGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lexicographic Permutations Generator")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")
        
        self.create_widgets()
    
    def create_widgets(self):
        title_label = ttk.Label(self.root, text="Lexicographic Permutations", font=("Arial", 14, "bold"), background="#f0f0f0")
        title_label.pack(pady=10)

        entry_label = ttk.Label(self.root, text="Enter a positive integer (n):", background="#f0f0f0")
        entry_label.pack()

        self.entry = ttk.Entry(self.root, width=10)
        self.entry.pack()

        generate_button = ttk.Button(self.root, text="Generate", command=self.generate_permutations)
        generate_button.pack(pady=10)

        self.steps_label = ttk.Label(self.root, text="", font=("Arial", 10, "bold"), background="#f0f0f0")
        self.steps_label.pack()
        
        # Frame for scrolling text
        frame = tk.Frame(self.root)
        frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.text_widget = tk.Text(frame, wrap="none", height=15, width=50)
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget.config(yscrollcommand=scrollbar.set)
    
    def generate_permutations(self):
        try:
            n = int(self.entry.get())
            if n <= 0:
                messagebox.showerror("Error", "Please enter a positive integer")
                return
            
            numbers = list(range(1, n + 1))
            permutations = list(itertools.permutations(numbers))
            self.text_widget.delete("1.0", tk.END)  # Clear previous content
            for i, perm in enumerate(permutations):
                self.text_widget.insert(tk.END, f"Step {i+1}: {perm}\n")
            self.steps_label.config(text=f"Total Steps: {len(permutations)}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PermutationGeneratorApp(root)
    root.mainloop()
