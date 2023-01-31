
miles_per_lap = 0.25

def laps_to_miles(laps):
    miles = laps * miles_per_lap
    return miles

user_laps = float(input("Please enter number of laps: "))
miles_walked = laps_to_miles(user_laps)



print(miles_walked)