import random

def main():

    # set a random seed for reproducibility
    random.seed(40)

    max_number_of_people = 13

    number_of_trials_per_person_count = 10000

    for number_of_people in range(2, max_number_of_people + 1):
        # how many people are we keeping in each room?
        print(f"Calculating for {number_of_people} people...")
        number_of_successful_trials = 0

        for trial_number in range(number_of_trials_per_person_count):
            # Generate random birthdays for the given number of people
            birthdays = []
            for _ in range(number_of_people):
                random_month = random.randint(1, 12)  # Generate a random month (1 to 12)
                birthdays.append(random_month)       # Add the random month to the list

            # Check if there is at least one shared birthday month
            unique_months = len(set(birthdays))
            total_birthdays = len(birthdays)
            if total_birthdays != unique_months:
                number_of_successful_trials += 1
                #print(f"  Trial {trial_number + 1}: Birthdays = {birthdays} -> Shared month found!")
                # update for where we are in the run, how many trials complete, how many matches, and what our current percentage is
                #print(f"    Trials complete: {trial_number + 1}, Successful trials: {number_of_successful_trials}, Current probability: {(number_of_successful_trials / (trial_number + 1)) * 100:.2f}%")
            #else:
                #print(f"  Trial {trial_number + 1}: Birthdays = {birthdays} -> No shared month.")
                # update for where we are in the run, how many trials complete, how many matches, and what our current percentage is
                #print(f"    Trials complete: {trial_number + 1}, Successful trials: {number_of_successful_trials}, Current probability: {(number_of_successful_trials / (trial_number + 1)) * 100:.2f}%")

        probability = number_of_successful_trials / number_of_trials_per_person_count

        # out of how many trial did we have, how many were a match, and what's the probability
        print(f"Out of {number_of_trials_per_person_count} trials, there were {number_of_successful_trials} successful trials.")

        print(f"For {number_of_people} people, the probability of shared birthday month is approximately {probability * 100:.2f}%")




if __name__ == "__main__":
    print("Hello, World!")

    #lets start with an example looking at how many people have a birthday in the same month

    main()