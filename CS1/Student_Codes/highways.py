
def interstate_def():
    while True:
        interstate = int(input("Enter Highway number: "))
        if interstate > 0 and interstate % 100 != 0 and interstate < 1000:
            direction = interstate_direction(interstate)
            auxilary = define_auxilary(interstate)
            print(f"{interstate} is {auxilary}, {direction}")
        else: 
            print(f"{interstate} is not  valid interstate number!")
            interstate_def

def interstate_direction(interstate):
    if interstate % 2 == 0:
        return "going east/west!"
    else:
        return "going north/south!"
    
def define_auxilary(interstate):
    branch = define_branch(interstate)
    if interstate < 100:
        return "is a primary"
    else:
        return f"is an auxilary, serving I-{branch}"
    
def define_branch(interstate):
    if 100 <= interstate <= 999:
        return interstate % 100  
    else:
        return None  
    

    
interstate_def()