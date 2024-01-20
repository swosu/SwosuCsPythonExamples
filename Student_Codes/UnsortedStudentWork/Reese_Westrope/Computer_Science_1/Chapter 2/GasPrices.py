mpg = float(input("Enter your vehicle's miles per gallon:"))
dpg = float(input("Enter the current gas price (dollars per gallon):"))
distance = int(input("Enter the first distance you would like to travel:"))
distance2 = int(input("Enter the second distance you would like to travel:"))
distance3 = int(input("Enter the third distance you would like to travel:"))
cost = dpg/mpg*distance
cost2 = dpg/mpg*distance2
cost3 = dpg/mpg*distance3

print("It will cost you $"'{:.2f}'.format(cost),"to travel",distance,"miles,")
print("$"'{:.2f}'.format(cost2),"to travel",distance2,"miles,")
print("and $"'{:.2f}'.format(cost3),"to travel",distance3, "miles.")