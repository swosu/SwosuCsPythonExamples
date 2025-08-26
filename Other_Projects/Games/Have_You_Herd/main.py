# import statements
from tkinter import *
import tkinter as tk
# run
# python -m tkinter
# this verifies that everything is running correctly.


if __name__ == '__main__':
    print('Welcome to have you herd, a game.')
    root=Tk()

    # from: https://www.geeksforgeeks.org/python-tkinter-text-widget/
    # specify size of window.
    root.geometry("250x170")


    a = Label(root, text="Hello, world!")
    a.pack()

    # Create text widget and specify size.
    T = Text(root, height = 5, width = 52)

    Fact = """It takes a big dog to
    weigh a ton."""

    # Create button for next text.
    b1 = Button(root, text = "Next", )

    # Create an Exit button.
    b2 = Button(root, text = "Exit",
            command = root.destroy)

    T.pack()
    b1.pack()
    b2.pack()

    # Insert The Fact.
    T.insert(tk.END, Fact)

    root.mainloop()
