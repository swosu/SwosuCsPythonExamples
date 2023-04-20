import tkinter as tk
import time

class Inventory:
    def __init__(self,moneyReceived=0):
        self.state = 'idle'
        self.moneyReceived = moneyReceived
        self.change = 0
        self.selection = ''
        self.items = {'Candy Bar': 1.00, 'Soda': 1.50, 'Chips': 2.00}
        
    #take money recieved and add it to the total amount of money recieved 
    def receivingMoney(self, amount):
        print(self.state)
        if self.state == 'idle':
            self.state = 'receiving money'
        elif self.state == 'receiving money':
            self.moneyReceived += amount
            print(f"{self.moneyReceived:.2f}")
        else:
            raise Exception('Invalid state')
        return self.moneyReceived
    
    #take money recieved and subtract it from the price of the item selected   
    def selectItem(self, item):
        if self.state == "receiving money":
            self.state = "selection made"
            if self.moneyReceived >= self.items[item]:
                self.change = self.moneyReceived - self.items[item]
            else:
                raise Exception('Not enough money received')
        else:
            raise Exception('Invalid state')
      
    #dispense item      
    def dispensor(self):
        if self.state == "selection made":
            self.state = "dispensing"
        else:
            raise Exception('Invalid state')
    
    #dispense change
    def changeDispensor(self):
        if self.state == "dispensing":
            self.state = "change dispening"
            print(f"{self.moneyReceived:.2f}")
            self.moneyRecieved = 0 
        else:
            raise Exception('Invalid state')

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
buttonCandybar = tk.Button(frame, text = "Candy Bar", command=lambda: operation.selectItem('Candy Bar'))
buttonCandybar.pack(side='left', padx=10, pady=10)

buttonSoda = tk.Button(frame, text = "Soda", command=lambda: operation.selectItem('Soda'))
buttonSoda.pack(side='left', padx=10, pady=10)

buttonChips = tk.Button(frame, text = "Chips", command=lambda: operation.selectItem('Chips'))
buttonChips.pack(side='left', padx=10, pady=10)

#write a label to display the amount of money received that updates when a button is clicked
labelMoneyReceived = tk.Label(root, text= operation.moneyReceived)
labelMoneyReceived.pack()

labelChange = tk.Label(root, text= operation.change)
labelChange.pack()

# Define a function that updates the label text
def updateLabel():
    labelMoneyReceived.config(text=f"Money received: ${operation.moneyReceived:.2f}")
    labelChange.config(text=f"Change: ${operation.change:.2f}")
    root.after(1, updateLabel)  # Schedule this function to run again in 1 second 

# Schedule the first update of the label text
root.after(1, updateLabel)

root.mainloop() 

