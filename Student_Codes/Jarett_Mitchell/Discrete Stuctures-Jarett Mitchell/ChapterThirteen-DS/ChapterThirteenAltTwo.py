import tkinter as tk

window = tk.Tk()
window.title("Vending Machine")
window.geometry("400x400")

moneyRecieved = int(0)



# Create a frame to hold buttons with the denomination of the coins in usd
frame = tk.Frame(window)
frame.pack()

# Create a button for each denomination of coin
button1 = tk.Button(frame, text="1 Cent", fg="black")
button1.pack(side=tk.LEFT)
button1.pack(side=tk.LEFT)
button5 = tk.Button(frame, text="5 Cent", fg="black")
button5.pack(side=tk.LEFT)
button10 = tk.Button(frame, text="10 Cent", fg="black")
button10.pack(side=tk.LEFT)
button25 = tk.Button(frame, text="25 Cent", fg="black")
button25.pack(side=tk.LEFT)
button50 = tk.Button(frame, text="50 Cent", fg="black")
button50.pack(side=tk.LEFT)
button100 = tk.Button(frame, text="1 Dollar", fg="black")
button100.pack(side=tk.LEFT)
button200 = tk.Button(frame, text="2 Dollar", fg="black")
button200.pack(side=tk.LEFT)
button500 = tk.Button(frame, text="5 Dollar", fg="black")
button500.pack(side=tk.LEFT)

# Create a sperated frame to hold buttons with the items in the vending machine
frame2 = tk.Frame(window)
frame2.pack()


window.mainloop()

