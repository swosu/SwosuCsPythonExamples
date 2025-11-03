import datetime
import time

def estimate_caffeine_level(initial_caffeine_level, half_life_hours, hours_elapsed):
    # Calculate the remaining caffeine level
    remaining_caffeine = initial_caffeine_level * (0.5 ** (hours_elapsed / half_life_hours))
    return remaining_caffeine

def main():
    # Input parameters
    print("Welcome to the Caffeine Tracker Game!")
    initial_caffeine_level = float(input("Enter your initial caffeine level (in mg): "))
    half_life_hours = 6.0  # Caffeine half-life is approximately 6 hours
    
    # Set the target caffeine level
    target_level = initial_caffeine_level / 4
    
    # Get the current time
    current_time = datetime.datetime.now()
    
    print("Let's see how long it takes for your caffeine level to drop to a safe level.")
    
    # Simulate the caffeine drop
    hours_elapsed = 0
    while initial_caffeine_level > target_level:
        # Calculate the estimated caffeine level
        estimated_caffeine_level = estimate_caffeine_level(initial_caffeine_level, half_life_hours, hours_elapsed)
        
        # Display the estimated caffeine level
        print(f"After {hours_elapsed} hours, your estimated caffeine level is {estimated_caffeine_level:.2f} mg")
        
        # Sleep for a moment to make it more interactive
        time.sleep(1)
        
        # Update the variables
        initial_caffeine_level = estimated_caffeine_level
        hours_elapsed += 1
    
    # Game over message
    print("\nCongratulations! Your caffeine level has dropped to a safe level.")
    print(f"It took you {hours_elapsed} hours to achieve this. ☕️🎉")

if __name__ == "__main__":
    main()
