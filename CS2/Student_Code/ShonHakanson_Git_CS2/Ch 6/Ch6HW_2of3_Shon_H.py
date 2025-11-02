#Comp Sci 2 HW Problem 6.20 Shon H
#This program converts feet walked to steps taken
def feet_to_steps(user_feet):
    return int (user_feet/2.5)

if __name__ == '__main__':
    user_feet = float(input("Enter the number of feet walked: "))

    number_of_steps_walked = feet_to_steps(user_feet)
    print(f'{number_of_steps_walked}')
    