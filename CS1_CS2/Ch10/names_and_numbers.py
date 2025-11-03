if __name__ == "__main__":
    names_and_ages = []
    
    while True:
        user_input = input()
        if user_input == "-1":
            break
        
        parts = user_input.split()
        name = parts[0]
        
        try:
            age = int(parts[1])
        except ValueError:
            age = 0
        
        names_and_ages.append((name, age + 1))
    
    for name, age in names_and_ages:
        print(f"{name} {age}")
