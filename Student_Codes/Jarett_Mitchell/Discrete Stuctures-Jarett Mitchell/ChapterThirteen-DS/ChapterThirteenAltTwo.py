import tkinter as tk
import time

class Inventory:
    def __init__(self,moneyReceived=0):
        self.state = 'idle'
        self.moneyReceived = moneyReceived
        self.items = {'Candy Bar': 1.00, 'Soda': 1.50, 'Chips': 2.00}
        
    def receivingMoney(self, amount):
        print(self.state)
        if self.state == 'idle':
            self.state = 'receiving money'
        elif self.state == 'receiving money':
            self.moneyReceived += amount
            print(f"{self.moneyReceived:.2f}")
        else:
            print("state change error")
   #what is the difference between the two functions below?      
    def selection(self):
        if self.state == "recieving money":
            self.state = "dispensing"
        elif self.state == "dispensing":
            self.moneyReceived = 0
        else:
            print("state change error")
            
    def dispensor(self):
        if self.state == "item selected":
            self.state = "dispensing"
        else:
            print("state change error")
    
    def changeDispensor(self):
        if self.state == "dispensing":
            self.state = "change dispening"
            self.moneyRecieved = 0 
        else:
            print("state change error")

root = tk.Tk()
root.title("Vending Machine")
root.geometry("600x400")

# Create a frame to hold buttons with the denomination of the coins in usd
frame = tk.Frame(root)
frame.pack()

operation =Inventory()

# Create a button for each denomination of coin
buttonPennies = tk.Button(frame, text="1¢", fg="black", command=lambda: operation.receivingMoney(0.01))
buttonPennies.pack(side=tk.LEFT)

buttonNickels = tk.Button(frame, text="5¢", fg="black", command=lambda: operation.receivingMoney(0.05))
buttonNickels.pack(side=tk.LEFT)

buttonDimes = tk.Button(frame, text="10¢", fg="black", command=lambda: operation.receivingMoney(0.10))
buttonDimes.pack(side=tk.LEFT)

buttonQuarters = tk.Button(frame, text="25¢", fg="black", command=lambda: operation.receivingMoney(0.25))
buttonQuarters.pack(side=tk.LEFT)

buttonHalfdollars = tk.Button(frame, text="50¢", fg="black", command=lambda: operation.receivingMoney(0.50))
buttonHalfdollars.pack(side=tk.LEFT)

buttonDollars = tk.Button(frame, text="$1", fg="black", command=lambda: operation.receivingMoney(1.00))
buttonDollars.pack(side=tk.LEFT)

buttonTwodollars = tk.Button(frame, text="$2", fg="black", command=lambda: operation.receivingMoney(2.00))
buttonTwodollars.pack(side=tk.LEFT)

buttonFivedollars = tk.Button(frame, text="$5", fg="black", command=lambda: operation.receivingMoney(5.00))
buttonFivedollars.pack(side=tk.LEFT)

#on button click, selection takes amount of item clicked and subtracts it from moneyRecieved then returns the change
buttonCandybar = tk.Button(frame, text = "Candy Bar", command=lambda: operation.selection(operation.items.get("Candy Bar")))
buttonCandybar.pack(side='left', padx=20, pady=10)

buttonSoda = tk.Button(frame, text = "Soda")
buttonSoda.pack(side='left', padx=3, pady=10)

#label to display the amount of money received, updates when a button is clicked
textMoneyReceived = tk.Label(root, textvariable=moneyReceivedVar, height=1, width=10)
textMoneyRecieved.pack()
textMoneyRecieved.configure(bg = "#8DA9C4")





root.mainloop()

