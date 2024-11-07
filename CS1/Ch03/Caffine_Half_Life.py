import datetime

def estimate_caffeine_level(initial_caffeine_level, half_life_hours, hours_elapsed):
    # Calculate the remaining caffeine level
    remaining_caffeine = initial_caffeine_level * (0.5 ** (hours_elapsed / half_life_hours))
    return remaining_caffeine

def main():
    # Input parameters
    initial_caffeine_level = float(input("Enter the initial caffeine level (in mg): "))
    half_life_hours = 6.0  # Caffeine half-life is approximately 6 hours
    
    # Get the current time
    current_time = datetime.datetime.now()
    
    # Ask the user for the number of hours elapsed since caffeine intake
    hours_elapsed = float(input("Enter the number of hours elapsed: "))
    
    # Calculate the estimated caffeine level
    estimated_caffeine_level = estimate_caffeine_level(initial_caffeine_level, half_life_hours, hours_elapsed)
    
    # Display the estimated caffeine level
    print(f"Estimated caffeine level after {hours_elapsed} hours: {estimated_caffeine_level:.2f} mg")

if __name__ == "__main__":
    main()