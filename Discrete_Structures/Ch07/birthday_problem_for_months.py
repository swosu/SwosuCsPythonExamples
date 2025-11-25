import random

def main():

    # set a random seed for reproducibility
    random.seed(42)

    max_number_of_people = 13

    number_of_trials_per_person_count = 10000

    for number_of_people in range(2, max_number_of_people + 1):
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

        probability = number_of_successful_trials / number_of_trials_per_person_count

        print(f"For {number_of_people} people, the probability of shared birthday month is approximately {probability * 100:.2f}%")




if __name__ == "__main__":
    print("Hello, World!")

    #lets start with an example looking at how many people have a birthday in the same month

    main()