import tkinter as tk
# imported tkinter to create the GUI
root = tk.Tk()
root.title("Cashier Tool")

root.geometry("800x400") 
root.configure(bg="#134074")

#Created labels and buttons for the GUI
labelOne = tk.Label(root,text= "Enter dollar amount due:", font = "Ariel, 11")
labelOne.pack(padx= 20,pady= 10, anchor= 'nw')
labelOne.configure(bg = "#8DA9C4")

inputTxtRec = tk.Text(root,height = 1, width = 11)
inputTxtRec.pack(padx=20,pady =20, anchor='w')
inputTxtRec.config(bg = "#EEF4ED")

labelTwo = tk.Label(root,text= "Enter dollar amount given:", font = "Ariel, 11")
labelTwo.pack(padx= 20,pady= 10, anchor= 'nw')
labelTwo.configure(bg = "#8DA9C4")

inputTxtDue = tk.Text(root,height = 1, width = 11)
inputTxtDue.pack(padx= 20,pady= 20, anchor= 'nw')
inputTxtDue.config(bg = "#EEF4ED")

#Deciding the amount of change due - main function
def change():
    # Denominations of coins and bills
    amountDue = float(inputTxtDue.get(1.0,"end-1c"))
    amountGiven = float(inputTxtRec.get(1.0,"end-1c"))
    cash = amountDue - amountGiven
    changeDue.config(text = (f'${cash:.2f}'))
    denominations = [
        ('Hundred(s)', 100),
        ('Fifty(s)', 50),
        ('Twenty(s)', 20),
        ('Ten(s)', 10),
        ('Five(s)', 5),
        ('One(s)', 1),
        ('Quarter(s)', 0.25),
        ('Dime(s)', 0.1),
        ('Nickel(s)', 0.05),
        ('Penny(s)', 0.01)
    ]
    change = {}

    for denom_name, denom_value in denominations:
        if cash >= denom_value:
            count = int(cash / denom_value)
            cash -= count * denom_value
            cash = round(cash, 2) # rounding to 2 decimal places
            change[denom_name] = count
    #Prompts if the amount given is not enough to cover the amount due     
    if change == {}:
      retLabel.config(text = (f"Not enough money was given to cover the amount due."))
    else:
      retLabel.config(text = (f"Give the customer: {change}"))

#button to calculate the change due
calcBtn = tk.Button(root, text = 'Calculate Change Due',command= change)
calcBtn.pack(padx = 30, pady = 1 , anchor = 'center')

changeDueDisplay = tk.Label(root, text = 'Change Due: ', font = "Ariel, 11", width= 15)
changeDueDisplay.pack(padx = 15 , pady = .4 , anchor = 'w')
changeDueDisplay.config(bg = "#EEF4ED")

changeDue = tk.Label(root, font = "Ariel, 11", height = 1, width = 15)
changeDue.pack(padx = 15 , pady = 0 , anchor = 'w')
changeDueDisplay.config(bg = "#8DA9C4")

#label to display the change due and denominations
retLabel = tk.Label(root, text = '', width = 110, height = 2)
retLabel.place(relx = 0.5 , rely = 0.8 , anchor ='s')
retLabel.config(bg = "#8DA9C4")

root.mainloop()


#Sources: https://www.toppr.com/guides/python-guide/examples/python-examples/functions/number-divisible/python-program-find-numbers-divisible-another-number/
#https://www.youtube.com/watch?v=9-Cpi3hGjrY
#https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/
#https://chat.openai.com/chat
#https://www.geeksforgeeks.org/python-place-method-in-tkinter/
#https://www.activestate.com/resources/quick-reads/how-to-use-pack-in-tkinter/
