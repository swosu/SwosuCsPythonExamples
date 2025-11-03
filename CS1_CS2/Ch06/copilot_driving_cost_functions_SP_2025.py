
def greet_user(greeting_repeat_times):
    for repeat_index in range(greeting_repeat_times):
        print("Hi calculate the driving cost")

def ask_user_for_gas_tank_size():
    gas_tank_size = float(input("Enter the gas tank size: "))
    return gas_tank_size




if __name__ == "__main__":
    greet_user(6)

    gas_tank_size = ask_user_for_gas_tank_size()
    print("Gas tank size is: ", gas_tank_size)
