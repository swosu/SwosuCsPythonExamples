# Get par and number of strokes as input
par = int(input("Enter par (3, 4, or 5): "))
strokes = int(input("Enter the number of strokes: "))

# Check if par is valid (3, 4, or 5)
if par not in [3, 4, 5]:
    print("Error")
else:
    # Calculate the difference between strokes and par
    score_difference = strokes - par

    # Determine the appropriate score name
    if score_difference == -2:
        print("Eagle")
    elif score_difference == -1:
        print("Birdie")
    elif score_difference == 0:
        print("Par")
    elif score_difference == 1:
        print("Bogey")
    elif score_difference == 2:
        print("Double Bogey")
    else:
        print("Error")
