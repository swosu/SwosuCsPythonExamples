import itertools as it

def cookie_combos(pos_selec = 6):
    cookies = ["Peanut Butter", "Chocolate Chip", "Macadamia Nut","Brownie"]
    cookie_combos = list(it.combinations_with_replacement(cookies,pos_selec))
    return cookie_combos

def check_repeats(cookie_list):
    ans = ""
    for order in cookie_list:
        cookie_list.remove(order)
        if order in cookie_list:
            ans = "Yes"
    if ans == "Yes":
        print("There are repeats")
    else:
        print("There are no repeats")

if __name__ == "__main__":
    num_of_combos = 0
    for order in cookie_combos():
        num_of_combos += 1
        cookie_combos().append(order)    
    print(f"There are {num_of_combos} different cookie combinations for ")
    
    dis_combos_ans = input("Do you want to see the combinations? (y/n): ")
    if dis_combos_ans in ("y", "Y", "yes", "Yes", "YES"):
        for i in cookie_combos():
            print(i)
        
    check_repeats_ans = (input("Do you want to check for repeats? (y/n): "))
    if check_repeats_ans in ("y", "Y", "yes", "Yes", "YES"):
        check_repeats(cookie_combos())
