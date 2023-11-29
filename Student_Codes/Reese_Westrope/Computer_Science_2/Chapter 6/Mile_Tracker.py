
def SetRunDistance():
    print("How many miles would you like to run?")
    global run_distance
    run_distance = int(input(":"))
    print(f"You have chosen to run {run_distance} miles.")

def SetMilePace():
    print("How fast would you like to run each mile (in minutes)?")
    global mile_pace
    mile_pace = int(input(":"))
    print(f"You have chosen to run at a {mile_pace} minute mile pace.")

def SetTrackLength():
    print("How many miles long is the track you are running on?")
    global track_length
    track_length = float(input(":"))
    return track_length

def CalcLapsPerMile():
    global laps_per_mile
    laps_per_mile = 1/track_length
    print(f"You will run {laps_per_mile} laps per mile.")

def CalcLapPace():
    lap_pace = mile_pace/laps_per_mile
    print(f"You will need to run each lap in {lap_pace} minutes.")

def CalcRunTime():
    run_time = run_distance*mile_pace
    print(f"It will take you {run_time} minutes to complete your run. Have a great day!")

if __name__ == "__main__":

    decision = input("Would you like to go running today?")

    if decision in ("yes","Yes","Y","y","yeah","Yeah","yep","Yep","yup","Yup"):
        SetRunDistance()
        SetMilePace()
        SetTrackLength()
        CalcLapsPerMile()
        CalcLapPace()
        CalcRunTime()
    else:
        print("Alright, have fun being lazy today.")

