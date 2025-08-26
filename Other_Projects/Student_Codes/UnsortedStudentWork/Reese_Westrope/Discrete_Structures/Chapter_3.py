#cashiers algorithm

BeverageMenu = {
    "Water: $": "1.00",
    "Dr Pepper: $": "2.00",
    "Coca Cola: $": "2.00",
    }
BurgerMenu = {
    "Classic Burger: $": "7.00",
    "Organic Sirloin Burger: $": "9.00",
    "Greek Burger: $": "10.00",
    "Bacon Cheeseburger: $":"8.00", 
    "Quinoa and Black Bean Burger: $":"9.00"
    }
SideMenu = {
    "Onion Rings: $": "3.50",
    "Fries: $": "3.00", 
    "Sweet Potato Fries: $": "4.00", 
    "Mozzarella Sticks: $": "3.00"
    }
DessertMenu = {
    "Cookie: $": "2.50", 
    "Brownie: $": "2.50"
    }


def GetBeverages():
    global user_beverage
    print("Beverages:")
    for beverage, price in BeverageMenu.items():
        print(beverage, price)
    user_beverage = input("Choose a beverage\n:").title()
    return user_beverage
    
def GetBurgers():
    global user_burger
    print("\nBurgers")
    for burger, price in BurgerMenu.items():
        print(burger, price)
    user_burger = input("Choose a burger\n:").title()
    return user_burger
    
def GetSides():
    global user_side
    print("\nSides")
    for side, price in SideMenu.items():
        print(side, price)
    user_side = input("Choose a side\n:").title()
    return user_side
    
def GetDesserts():
    global user_dessert
    print("\nDesserts")
    for dessert, price in DessertMenu.items():
        print(dessert, price)
    user_dessert = input("Choose a dessert\n:").title()
    return user_dessert

def GetUserTotal():
    global user_dessert, user_beverage, user_burger, user_side, total_cost
    
    beverage_cost = 0
    burger_cost = 0
    side_cost = 0
    dessert_cost = 0
    for beverage, cost in BeverageMenu.items():
        if beverage.replace(": $", "") == user_beverage:
            print(f"The cost of your beverage is ${cost}")
            beverage_cost += float(cost)
    if beverage_cost == 0:
        print("You didn't choose a beverage from the menu.")
                
    for burger, cost in BurgerMenu.items():
        if burger.replace(": $", "") == user_burger:
            print(f"The cost of your burger is ${cost}")
            burger_cost += float(cost)      
    if burger_cost == 0:
        print("You didn't choose a burger from the menu.")
            
    for side, cost in SideMenu.items():
        if side.replace(": $", "") == user_side:
            print(f"The cost of your side is ${cost}")
            side_cost += float(cost)          
    if side_cost == 0:
        print("You didn't choose a side from the menu.")
                
    for dessert, cost in DessertMenu.items():
        if dessert.replace(": $", "") == user_dessert:
            print(f"The cost of your dessert is ${cost}")
            dessert_cost += float(cost)         
    if dessert_cost == 0:
        print("You didn't choose a dessert from the menu.")
                
    total_cost = beverage_cost + burger_cost + side_cost + dessert_cost
    print(f"Your total cost is ${total_cost:.2f}")
    
def GetUserPayment():
    global user_payment
    user_payment = float(input("What are you going to pay? (in cash)\n:"))
    return user_payment

def CashiersAlgorithm(cost, payment):
    change1 = payment - cost
    change = payment - cost
    ten_dollars = 0
    five_dollars = 0
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while change > 0:
        if change >= 10:
            ten_dollars += 1
            change -= 10
        elif change >= 5:
            five_dollars += 1
            change -= 5
        elif change >= 1:
            dollars += 1
            change -= 1
        elif change >= 0.25:
            quarters += 1
            change -= 0.25
        elif change >= 0.1:
            dimes += 1
            change -= 0.1
        elif change >= 0.05:
            nickels += 1
            change -= 0.05
        elif change >= 0.01:
            pennies += 1
            change -= 0.01
    print(f"Your change will be ${change1:.2f}.\n You will get {ten_dollars} ten dollar bill(s), {five_dollars} five dollar bill(s), {dollars} dollar bill(s), {quarters} quarter(s), {dimes} dime(s), {nickels} nickel(s), and {pennies} pennie(s).")



if __name__ == "__main__":
    
    GetBeverages()
    GetBurgers()
    GetSides()
    GetDesserts()
    GetUserTotal()
    GetUserPayment()
    CashiersAlgorithm(total_cost, user_payment)