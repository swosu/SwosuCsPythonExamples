def movies():
    # Get a valid age input


    while True:
        time = input("Day or Night:").lower()
        if time == "day" or time == "night":
            break  # Exit the loop if the input is valid
        else:
            print("Invalid input. Please enter 'Day' or 'Night'.")
            
    while True:
        try:
            age = int(input("How old are you:"))
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")
    
    # Keep asking for a valid time input
    

    # Now handle the conditions based on age and time
    if age < 4:
        print("free") 

    elif age >= 4 and time == "day":
        print("8")
    
    elif age >= 4 and age <= 16 and time == "night":
        print("Night")
        print("12")

    elif age >= 17 and age <= 54 and time == "night":
        print("Night")
        print("15")

    elif age >= 55 and time == "night":
        print("13")

movies()
