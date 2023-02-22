import itertools as it

Cookie_Types = it.product(["Peanut Butter", "Chocolate Chip", "Macadamia Nut","Brownie"], repeat=6)
Cookie_Combos = []

def Check_Repeats(Cookie_List):
    ans = ""
    for order in Cookie_List:
        Cookie_List.remove(order)
        if order in Cookie_List:
            ans = "Yes"
    if ans == "Yes":
        print("There are repeats")
    else:
        print("There are no repeats")

if __name__ == "__main__":
    Num_Of_Combos = 0
    for order in Cookie_Types:
        Num_Of_Combos += 1
        Cookie_Combos.append(order)    
        print(order)    
    print(f"There are {Num_Of_Combos} different cookie combos")
    
    Check_Repeats_Ans = (input("Do you want to check for repeats? (y/n): "))
    if Check_Repeats_Ans in ("y", "Y", "yes", "Yes", "YES"):
        Check_Repeats(Cookie_Combos)
        
