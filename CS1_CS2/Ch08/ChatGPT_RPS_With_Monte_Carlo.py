import random


def build_game_rules():
    """
    Build and return the dictionary-of-dictionaries that stores
    all Rock, Paper, Scissors outcomes.

    Outer dictionary behavior:
        Key   -> user's choice
        Value -> another dictionary for that user's choice

    Inner dictionary behavior:
        Key   -> computer's choice
        Value -> result string ("You win", "You lose", or "Tie")

    Example:
        rules["R"]["S"] -> "You win"
    """
    rock_choice_dictionary = {
        "R": "Tie",
        "P": "You lose",
        "S": "You win"
    }

    paper_choice_dictionary = {
        "R": "You win",
        "P": "Tie",
        "S": "You lose"
    }

    scissors_choice_dictionary = {
        "R": "You lose",
        "P": "You win",
        "S": "Tie"
    }

    user_choice_dictionary = {
        "R": rock_choice_dictionary,
        "P": paper_choice_dictionary,
        "S": scissors_choice_dictionary
    }

    return user_choice_dictionary


def build_choice_name_dictionary():
    """
    Build and return a dictionary that translates the short codes
    R, P, and S into full words.
    """
    return {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors"
    }


def get_random_choice():
    """
    Randomly choose and return one valid game option.

    Returns:
        str: "R", "P", or "S"
    """
    valid_choices = ["R", "P", "S"]
    return random.choice(valid_choices)


def look_up_game_result(user_choice, computer_choice, game_rules):
    """
    Use the dictionary-of-dictionaries to determine the round result.

    Dictionary behavior:
    - First lookup gets the inner dictionary for the user's choice.
    - Second lookup gets the final game result based on the computer's choice.

    Example:
        game_rules["P"]["R"] -> "You win"

    Returns:
        str: "Tie", "You win", or "You lose"
    """
    return game_rules[user_choice][computer_choice]


def create_empty_choice_counter():
    """
    Create a dictionary used to count how many times each choice appears.

    Returns:
        dict: keys R, P, S all starting at 0
    """
    return {
        "R": 0,
        "P": 0,
        "S": 0
    }


def create_empty_result_counter():
    """
    Create a dictionary used to count game outcomes.

    Returns:
        dict: counts for Tie, You win, and You lose
    """
    return {
        "Tie": 0,
        "You win": 0,
        "You lose": 0
    }


def create_empty_combination_counter():
    """
    Create a dictionary to count all 9 user/computer combinations.

    Each key is a tuple:
        (user_choice, computer_choice)

    Example:
        ("R", "S") means user chose Rock and computer chose Scissors.

    Returns:
        dict: all 9 combinations initialized to 0
    """
    combination_counter = {}

    for user_choice in ["R", "P", "S"]:
        for computer_choice in ["R", "P", "S"]:
            combination_counter[(user_choice, computer_choice)] = 0

    return combination_counter


def simulate_one_round(game_rules):
    """
    Simulate one automated round of Rock, Paper, Scissors.

    Both the user's choice and the computer's choice are generated randomly.

    Returns:
        tuple: (user_choice, computer_choice, result)
    """
    user_choice = get_random_choice()
    computer_choice = get_random_choice()
    result = look_up_game_result(user_choice, computer_choice, game_rules)

    return user_choice, computer_choice, result


def update_choice_counter(choice_counter, choice):
    """
    Add one count to the selected choice in a choice counter dictionary.

    This demonstrates dictionary mutation by updating a value stored
    under a key.
    """
    choice_counter[choice] += 1


def update_result_counter(result_counter, result):
    """
    Add one count to the selected game result in a result counter dictionary.
    """
    result_counter[result] += 1


def update_combination_counter(combination_counter, user_choice, computer_choice):
    """
    Add one count to the specific (user_choice, computer_choice) combination.

    This uses a tuple as the dictionary key, which is another nice
    dictionary idea for students to see.
    """
    combination_counter[(user_choice, computer_choice)] += 1


def run_monte_carlo_simulation(number_of_trials, game_rules):
    """
    Run the full Monte Carlo simulation for a specified number of trials.

    For each trial:
    - randomly generate the user choice
    - randomly generate the computer choice
    - determine the result
    - update all counters

    Returns:
        dict: a bundle of all simulation results
    """
    user_choice_counter = create_empty_choice_counter()
    computer_choice_counter = create_empty_choice_counter()
    result_counter = create_empty_result_counter()
    combination_counter = create_empty_combination_counter()

    for _ in range(number_of_trials):
        user_choice, computer_choice, result = simulate_one_round(game_rules)

        update_choice_counter(user_choice_counter, user_choice)
        update_choice_counter(computer_choice_counter, computer_choice)
        update_result_counter(result_counter, result)
        update_combination_counter(combination_counter, user_choice, computer_choice)

    return {
        "trials": number_of_trials,
        "user_choice_counter": user_choice_counter,
        "computer_choice_counter": computer_choice_counter,
        "result_counter": result_counter,
        "combination_counter": combination_counter
    }


def calculate_proportion(count, total):
    """
    Calculate and return a proportion.

    Returns:
        float: count / total
    """
    if total == 0:
        return 0.0
    return count / total


def calculate_margin_of_error(probability, sample_size, z_score=1.96):
    """
    Calculate the approximate margin of error for a sample proportion.

    Formula:
        MOE = z * sqrt( p * (1 - p) / n )

    Parameters:
        probability (float): expected probability for the category
        sample_size (int): number of trials
        z_score (float): 1.96 gives an approximate 95% confidence level

    Returns:
        float: margin of error
    """
    if sample_size <= 0:
        return 0.0

    return z_score * ((probability * (1 - probability) / sample_size) ** 0.5)


def calculate_required_sample_size(probability, desired_margin_of_error, z_score=1.96):
    """
    Calculate the approximate sample size needed for a desired margin of error.

    Rearranged formula:
        n = z^2 * p * (1 - p) / ME^2

    Parameters:
        probability (float): expected probability of the category
        desired_margin_of_error (float): desired half-width of the interval
        z_score (float): 1.96 for about 95% confidence

    Returns:
        int: recommended sample size rounded up
    """
    numerator = (z_score ** 2) * probability * (1 - probability)
    denominator = desired_margin_of_error ** 2

    return int(numerator / denominator) + 1


def display_choice_distribution(title, counter_dictionary, total_trials, choice_names):
    """
    Display counts and proportions for Rock, Paper, and Scissors.

    This function is generic enough to work for either the user's choices
    or the computer's choices.
    """
    print(title)
    print("-" * len(title))

    expected_probability = 1 / 3
    margin_of_error = calculate_margin_of_error(expected_probability, total_trials)

    for short_choice in ["R", "P", "S"]:
        count = counter_dictionary[short_choice]
        proportion = calculate_proportion(count, total_trials)

        print(
            f"{choice_names[short_choice]:<10} "
            f"Count = {count:>6}   "
            f"Observed = {proportion:>7.4f}   "
            f"Expected = {expected_probability:>7.4f}"
        )

    print(f"Approximate 95% margin of error for p = 1/3: ±{margin_of_error:.4f}")
    print()


def display_result_distribution(result_counter, total_trials):
    """
    Display counts and proportions for Tie, You win, and You lose.
    """
    title = "Outcome Distribution"
    print(title)
    print("-" * len(title))

    expected_probability = 1 / 3
    margin_of_error = calculate_margin_of_error(expected_probability, total_trials)

    for result_name in ["Tie", "You win", "You lose"]:
        count = result_counter[result_name]
        proportion = calculate_proportion(count, total_trials)

        print(
            f"{result_name:<10} "
            f"Count = {count:>6}   "
            f"Observed = {proportion:>7.4f}   "
            f"Expected = {expected_probability:>7.4f}"
        )

    print(f"Approximate 95% margin of error for p = 1/3: ±{margin_of_error:.4f}")
    print()


def display_combination_distribution(combination_counter, total_trials, choice_names):
    """
    Display the frequency of all 9 user/computer combinations.

    Each of the 9 combinations should appear about 1/9 of the time
    in a fair and properly randomized simulation.
    """
    title = "User Choice x Computer Choice Combination Distribution"
    print(title)
    print("-" * len(title))

    expected_probability = 1 / 9
    margin_of_error = calculate_margin_of_error(expected_probability, total_trials)

    for user_choice in ["R", "P", "S"]:
        for computer_choice in ["R", "P", "S"]:
            count = combination_counter[(user_choice, computer_choice)]
            proportion = calculate_proportion(count, total_trials)

            label = f"{choice_names[user_choice]} vs {choice_names[computer_choice]}"

            print(
                f"{label:<24} "
                f"Count = {count:>6}   "
                f"Observed = {proportion:>7.4f}   "
                f"Expected = {expected_probability:>7.4f}"
            )

    print(f"Approximate 95% margin of error for p = 1/9: ±{margin_of_error:.4f}")
    print()


def display_sample_size_guidance():
    """
    Display sample-size guidance for the simulation.

    We compute two example recommendations:
    1. For the three main outcomes with p = 1/3 and margin of error = 0.02
    2. For the nine exact combinations with p = 1/9 and margin of error = 0.015
    """
    title = "Sample Size Guidance"
    print(title)
    print("-" * len(title))

    outcome_probability = 1 / 3
    outcome_margin_of_error = 0.02
    outcome_sample_size = calculate_required_sample_size(
        outcome_probability,
        outcome_margin_of_error
    )

    combination_probability = 1 / 9
    combination_margin_of_error = 0.015
    combination_sample_size = calculate_required_sample_size(
        combination_probability,
        combination_margin_of_error
    )

    print("For the three overall outcomes (Tie / You win / You lose):")
    print(f"  Expected probability for each outcome = 1/3")
    print(f"  Desired margin of error             = ±{outcome_margin_of_error:.3f}")
    print(f"  Recommended sample size             = {outcome_sample_size}")
    print()

    print("For the 9 exact user/computer combinations:")
    print(f"  Expected probability for each combination = 1/9")
    print(f"  Desired margin of error                  = ±{combination_margin_of_error:.3f}")
    print(f"  Recommended sample size                  = {combination_sample_size}")
    print()

    print("Practical classroom advice:")
    print("  100 trials   -> enough to see the basic idea")
    print("  1,000 trials -> pretty stable for wins / losses / ties")
    print("  3,000 trials -> a strong middle ground for the full 9-cell table")
    print("  10,000 trials -> very stable and still runs quickly")
    print()


def display_interpretation(simulation_results):
    """
    Display a plain-English interpretation of what the simulation means.

    This helps students connect the numbers to the idea of fairness.
    """
    total_trials = simulation_results["trials"]
    result_counter = simulation_results["result_counter"]

    ties = calculate_proportion(result_counter["Tie"], total_trials)
    wins = calculate_proportion(result_counter["You win"], total_trials)
    losses = calculate_proportion(result_counter["You lose"], total_trials)

    print("Interpretation")
    print("--------------")
    print("If the game is fair, the long-run proportions for Tie, You win, and You lose")
    print("should all be close to 1/3.")
    print()
    print(f"Observed tie rate   = {ties:.4f}")
    print(f"Observed win rate   = {wins:.4f}")
    print(f"Observed lose rate  = {losses:.4f}")
    print()

    print("Small differences are normal because randomness wiggles.")
    print("Large sample sizes reduce that wiggle.")
    print("If the observed values stay close to 1/3 as the sample size increases,")
    print("that is strong evidence that the game mechanics are fair.")
    print()


def run_rock_paper_scissors_monte_carlo_analysis():
    """
    Run the full Rock, Paper, Scissors Monte Carlo analysis program.

    Program flow:
    1. Build the game rules and choice-name dictionary
    2. Display sample-size guidance
    3. Ask the user for the number of trials
    4. Run the simulation
    5. Display all distributions and interpretation
    """
    game_rules = build_game_rules()
    choice_names = build_choice_name_dictionary()

    print("Rock, Paper, Scissors with Monte Carlo Analysis")
    print("=" * 48)
    print()

    display_sample_size_guidance()

    number_of_trials = int(input("Enter the number of automated trials to run: "))

    simulation_results = run_monte_carlo_simulation(number_of_trials, game_rules)

    print()
    print(f"Simulation complete. Total trials = {simulation_results['trials']}")
    print()

    display_choice_distribution(
        "User Choice Distribution",
        simulation_results["user_choice_counter"],
        simulation_results["trials"],
        choice_names
    )

    display_choice_distribution(
        "Computer Choice Distribution",
        simulation_results["computer_choice_counter"],
        simulation_results["trials"],
        choice_names
    )

    display_result_distribution(
        simulation_results["result_counter"],
        simulation_results["trials"]
    )

    display_combination_distribution(
        simulation_results["combination_counter"],
        simulation_results["trials"],
        choice_names
    )

    display_interpretation(simulation_results)


run_rock_paper_scissors_monte_carlo_analysis()