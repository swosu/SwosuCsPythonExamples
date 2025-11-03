#CH6 HW Problem 6.22: Swapping Variables
def swap_values(user_val1, user_val2, user_val3, user_val4):
    # Swap val1 and val2
    temp = user_val1
    user_val1 = user_val2
    user_val2 = temp
    # Swap val3 and val4
    temp = user_val3
    user_val3 = user_val4
    user_val4 = temp
    return user_val1, user_val2, user_val3, user_val4


if __name__ == "__main__":
    val1 = input("Enter value 1: ")
    val2 = input("Enter value 2: ")
    val3 = input("Enter value 3: ")
    val4 = input("Enter value 4: ")

    print(f"Before swapping: val1={val1}, val2={val2}, val3={val3}, val4={val4}")
    val1, val2, val3, val4 = swap_values(val1, val2, val3, val4)
    print(f"After swapping: val1={val1}, val2={val2}, val3={val3}, val4={val4}")