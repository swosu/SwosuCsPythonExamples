import random
import time
import statistics
import math
import matplotlib.pyplot as plt


def build_game_rules():
    """
    Build and return the dictionary-of-dictionaries that stores
    the Rock, Paper, Scissors game logic.

    Outer dictionary behavior:
        key   -> user's choice ("R", "P", or "S")
        value -> inner dictionary for that choice

    Inner dictionary behavior:
        key   -> computer's choice ("R", "P", or "S")
        value -> outcome string ("Tie", "You win", or "You lose")

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
    into full words.
    """
    return {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors"
    }


def get_random_choice():
    """
    Randomly return one valid game choice.

    Returns:
        str: "R", "P", or "S"
    """
    return random.choice(["R", "P", "S"])


def look_up_game_result(user_choice, computer_choice, game_rules):
    """
    Use the dictionary-of-dictionaries to determine the round result.

    This is the key nested dictionary lookup:
        game_rules[user_choice][computer_choice]

    Returns:
        str: "Tie", "You win", or "You lose"
    """
    return game_rules[user_choice][computer_choice]


def create_empty_choice_counter():
    """
    Create and return a dictionary that counts Rock, Paper, and Scissors.
    """
    return {
        "R": 0,
        "P": 0,
        "S": 0
    }


def create_empty_result_counter():
    """
    Create and return a dictionary that counts game outcomes.
    """
    return {
        "Tie": 0,
        "You win": 0,
        "You lose": 0
    }


def create_empty_combination_counter():
    """
    Create and return a dictionary that counts all 9 possible
    (user_choice, computer_choice) combinations.

    The key is a tuple, which is another useful dictionary behavior.
    """
    combination_counter = {}

    for user_choice in ["R", "P", "S"]:
        for computer_choice in ["R", "P", "S"]:
            combination_counter[(user_choice, computer_choice)] = 0

    return combination_counter


def update_choice_counter(choice_counter, choice):
    """
    Increment the count for one choice in a choice counter dictionary.
    """
    choice_counter[choice] += 1


def update_result_counter(result_counter, result):
    """
    Increment the count for one result in a result counter dictionary.
    """
    result_counter[result] += 1


def update_combination_counter(combination_counter, user_choice, computer_choice):
    """
    Increment the count for one (user_choice, computer_choice) combination.
    """
    combination_counter[(user_choice, computer_choice)] += 1


def simulate_one_round(game_rules):
    """
    Simulate one automated round of Rock, Paper, Scissors.

    Returns:
        tuple: (user_choice, computer_choice, result)
    """
    user_choice = get_random_choice()
    computer_choice = get_random_choice()
    result = look_up_game_result(user_choice, computer_choice, game_rules)
    return user_choice, computer_choice, result


def run_one_batch(number_of_trials, game_rules):
    """
    Run one Monte Carlo batch containing a fixed number of trials.

    This function:
    - simulates all rounds in the batch
    - counts user choices
    - counts computer choices
    - counts outcomes
    - counts all 9 combinations
    - times how long the batch takes

    Returns:
        dict: all raw counts, proportions, and timing information for the batch
    """
    user_choice_counter = create_empty_choice_counter()
    computer_choice_counter = create_empty_choice_counter()
    result_counter = create_empty_result_counter()
    combination_counter = create_empty_combination_counter()

    start_time = time.perf_counter()

    for _ in range(number_of_trials):
        user_choice, computer_choice, result = simulate_one_round(game_rules)

        update_choice_counter(user_choice_counter, user_choice)
        update_choice_counter(computer_choice_counter, computer_choice)
        update_result_counter(result_counter, result)
        update_combination_counter(combination_counter, user_choice, computer_choice)

    end_time = time.perf_counter()
    elapsed_seconds = end_time - start_time
    elapsed_milliseconds = elapsed_seconds * 1000

    batch_summary = {
        "trials": number_of_trials,
        "user_choice_counter": user_choice_counter,
        "computer_choice_counter": computer_choice_counter,
        "result_counter": result_counter,
        "combination_counter": combination_counter,
        "elapsed_seconds": elapsed_seconds,
        "elapsed_milliseconds": elapsed_milliseconds,
        "result_proportions": calculate_result_proportions(result_counter, number_of_trials),
        "choice_proportions_user": calculate_choice_proportions(user_choice_counter, number_of_trials),
        "choice_proportions_computer": calculate_choice_proportions(computer_choice_counter, number_of_trials),
    }

    return batch_summary


def calculate_choice_proportions(choice_counter, total_trials):
    """
    Convert raw Rock/Paper/Scissors counts into proportions.

    Returns:
        dict: proportion for each choice
    """
    return {
        "R": safe_divide(choice_counter["R"], total_trials),
        "P": safe_divide(choice_counter["P"], total_trials),
        "S": safe_divide(choice_counter["S"], total_trials),
    }


def calculate_result_proportions(result_counter, total_trials):
    """
    Convert raw outcome counts into proportions.

    Returns:
        dict: proportion for Tie, You win, and You lose
    """
    return {
        "Tie": safe_divide(result_counter["Tie"], total_trials),
        "You win": safe_divide(result_counter["You win"], total_trials),
        "You lose": safe_divide(result_counter["You lose"], total_trials),
    }


def safe_divide(numerator, denominator):
    """
    Safely divide two numbers.

    Returns:
        float: numerator / denominator, or 0.0 if denominator is 0
    """
    if denominator == 0:
        return 0.0
    return numerator / denominator


def run_repeated_batches(number_of_trials_per_batch, number_of_batches, game_rules):
    """
    Run many independent batches at the same sample size.

    This is the heart of the variance demonstration.

    Example:
        10 trials per batch, repeated 10 times

    Returns:
        list: list of batch summary dictionaries
    """
    batch_results = []

    for _ in range(number_of_batches):
        batch_summary = run_one_batch(number_of_trials_per_batch, game_rules)
        batch_results.append(batch_summary)

    return batch_results


def calculate_mean(values):
    """
    Return the arithmetic mean of a list of numbers.
    """
    if len(values) == 0:
        return 0.0
    return statistics.mean(values)


def calculate_standard_deviation(values):
    """
    Return the sample standard deviation of a list of numbers.

    If there is only one value, return 0.0 because standard deviation
    is not meaningful for a single observed value.
    """
    if len(values) < 2:
        return 0.0
    return statistics.stdev(values)


def summarize_batch_group(batch_results):
    """
    Summarize a group of repeated batches that all used the same sample size.

    We calculate:
    - mean outcome proportions
    - standard deviation of outcome proportions
    - mean timing
    - standard deviation of timing

    Returns:
        dict: summary statistics for the entire group
    """
    tie_rates = []
    win_rates = []
    lose_rates = []

    user_rock_rates = []
    user_paper_rates = []
    user_scissors_rates = []

    computer_rock_rates = []
    computer_paper_rates = []
    computer_scissors_rates = []

    elapsed_milliseconds_list = []

    for batch in batch_results:
        tie_rates.append(batch["result_proportions"]["Tie"])
        win_rates.append(batch["result_proportions"]["You win"])
        lose_rates.append(batch["result_proportions"]["You lose"])

        user_rock_rates.append(batch["choice_proportions_user"]["R"])
        user_paper_rates.append(batch["choice_proportions_user"]["P"])
        user_scissors_rates.append(batch["choice_proportions_user"]["S"])

        computer_rock_rates.append(batch["choice_proportions_computer"]["R"])
        computer_paper_rates.append(batch["choice_proportions_computer"]["P"])
        computer_scissors_rates.append(batch["choice_proportions_computer"]["S"])

        elapsed_milliseconds_list.append(batch["elapsed_milliseconds"])

    summary = {
        "trials_per_batch": batch_results[0]["trials"] if batch_results else 0,
        "number_of_batches": len(batch_results),
        "tie_mean": calculate_mean(tie_rates),
        "tie_std_dev": calculate_standard_deviation(tie_rates),
        "win_mean": calculate_mean(win_rates),
        "win_std_dev": calculate_standard_deviation(win_rates),
        "lose_mean": calculate_mean(lose_rates),
        "lose_std_dev": calculate_standard_deviation(lose_rates),
        "user_rock_mean": calculate_mean(user_rock_rates),
        "user_rock_std_dev": calculate_standard_deviation(user_rock_rates),
        "user_paper_mean": calculate_mean(user_paper_rates),
        "user_paper_std_dev": calculate_standard_deviation(user_paper_rates),
        "user_scissors_mean": calculate_mean(user_scissors_rates),
        "user_scissors_std_dev": calculate_standard_deviation(user_scissors_rates),
        "computer_rock_mean": calculate_mean(computer_rock_rates),
        "computer_rock_std_dev": calculate_standard_deviation(computer_rock_rates),
        "computer_paper_mean": calculate_mean(computer_paper_rates),
        "computer_paper_std_dev": calculate_standard_deviation(computer_paper_rates),
        "computer_scissors_mean": calculate_mean(computer_scissors_rates),
        "computer_scissors_std_dev": calculate_standard_deviation(computer_scissors_rates),
        "elapsed_ms_mean": calculate_mean(elapsed_milliseconds_list),
        "elapsed_ms_std_dev": calculate_standard_deviation(elapsed_milliseconds_list),
        "batch_results": batch_results,
    }

    return summary


def build_experiment_plan():
    """
    Build and return the experiment plan.

    Each tuple contains:
        (label, trials_per_batch, number_of_batches)

    The idea is to show:
    - tiny sample size
    - small sample size
    - medium sample size
    - sufficient sample size
    - excessive sample size
    """
    return [
        ("Tiny", 1, 100),
        ("Small", 10, 10),
        ("Medium", 100, 10),
        ("Sufficient", 3000, 10),
        ("Excessive", 10000, 10),
    ]


def run_full_variance_experiment(game_rules):
    """
    Run the full multi-stage Monte Carlo variance demonstration.

    Returns:
        list: one summary dictionary per experiment stage
    """
    experiment_summaries = []
    experiment_plan = build_experiment_plan()

    for label, trials_per_batch, number_of_batches in experiment_plan:
        batch_results = run_repeated_batches(trials_per_batch, number_of_batches, game_rules)
        summary = summarize_batch_group(batch_results)
        summary["label"] = label
        experiment_summaries.append(summary)

    return experiment_summaries


def print_experiment_summary(experiment_summaries):
    """
    Print a readable summary of all experiment stages.

    This gives students a table-like report that compares:
    - the mean outcome rates
    - the standard deviations
    - the average time per batch
    """
    print()
    print("Rock, Paper, Scissors with Monte Carlo Analysis and Statistical Variance Demonstration")
    print("=" * 86)

    for summary in experiment_summaries:
        print()
        print(f"Experiment Stage: {summary['label']}")
        print("-" * 50)
        print(f"Trials per batch: {summary['trials_per_batch']}")
        print(f"Number of batches: {summary['number_of_batches']}")
        print()

        print("Outcome proportions across repeated batches")
        print("Expected long-run value for each outcome: 0.3333")
        print(f"  Tie      mean = {summary['tie_mean']:.4f}   std dev = {summary['tie_std_dev']:.4f}")
        print(f"  You win  mean = {summary['win_mean']:.4f}   std dev = {summary['win_std_dev']:.4f}")
        print(f"  You lose mean = {summary['lose_mean']:.4f}   std dev = {summary['lose_std_dev']:.4f}")
        print()

        print("User choice proportions across repeated batches")
        print("Expected long-run value for each choice: 0.3333")
        print(f"  Rock     mean = {summary['user_rock_mean']:.4f}   std dev = {summary['user_rock_std_dev']:.4f}")
        print(f"  Paper    mean = {summary['user_paper_mean']:.4f}   std dev = {summary['user_paper_std_dev']:.4f}")
        print(f"  Scissors mean = {summary['user_scissors_mean']:.4f}   std dev = {summary['user_scissors_std_dev']:.4f}")
        print()

        print("Computer choice proportions across repeated batches")
        print("Expected long-run value for each choice: 0.3333")
        print(f"  Rock     mean = {summary['computer_rock_mean']:.4f}   std dev = {summary['computer_rock_std_dev']:.4f}")
        print(f"  Paper    mean = {summary['computer_paper_mean']:.4f}   std dev = {summary['computer_paper_std_dev']:.4f}")
        print(f"  Scissors mean = {summary['computer_scissors_mean']:.4f}   std dev = {summary['computer_scissors_std_dev']:.4f}")
        print()

        print("Timing")
        print(f"  Mean batch time     = {summary['elapsed_ms_mean']:.3f} ms")
        print(f"  Std dev batch time  = {summary['elapsed_ms_std_dev']:.3f} ms")


def extract_batch_outcome_series(summary, outcome_name):
    """
    Extract the list of outcome proportions for a single outcome
    across all repeated batches in one experiment stage.

    Parameters:
        summary (dict): one experiment stage summary
        outcome_name (str): "Tie", "You win", or "You lose"

    Returns:
        list: list of proportions
    """
    series = []

    for batch in summary["batch_results"]:
        series.append(batch["result_proportions"][outcome_name])

    return series


def extract_batch_timing_series(summary):
    """
    Extract the list of elapsed milliseconds across repeated batches
    for one experiment stage.
    """
    timing_series = []

    for batch in summary["batch_results"]:
        timing_series.append(batch["elapsed_milliseconds"])

    return timing_series


def plot_outcome_bounce(experiment_summaries, outcome_name):
    """
    Plot how one outcome proportion bounces around from batch to batch
    for each sample-size stage.

    This graph helps students see that:
    - tiny sample sizes swing wildly
    - sufficient sample sizes cluster tightly
    """
    plt.figure(figsize=(10, 6))

    for summary in experiment_summaries:
        y_values = extract_batch_outcome_series(summary, outcome_name)
        x_values = list(range(1, len(y_values) + 1))
        label = f"{summary['label']} (n={summary['trials_per_batch']})"
        plt.plot(x_values, y_values, marker="o", linestyle="-", label=label)

    plt.axhline(1 / 3, linestyle="--", label="Expected = 1/3")
    plt.title(f"Batch-to-Batch Variance for Outcome: {outcome_name}")
    plt.xlabel("Batch Number")
    plt.ylabel("Observed Proportion")
    plt.ylim(0, 1)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_outcome_standard_deviation(experiment_summaries):
    """
    Plot the standard deviation of the outcome proportions by sample size.

    This is one of the clearest graphs in the whole story because it
    directly shows variance shrinking as sample size increases.
    """
    labels = []
    sample_sizes = []
    tie_std_devs = []
    win_std_devs = []
    lose_std_devs = []

    for summary in experiment_summaries:
        labels.append(summary["label"])
        sample_sizes.append(summary["trials_per_batch"])
        tie_std_devs.append(summary["tie_std_dev"])
        win_std_devs.append(summary["win_std_dev"])
        lose_std_devs.append(summary["lose_std_dev"])

    plt.figure(figsize=(10, 6))
    plt.plot(sample_sizes, tie_std_devs, marker="o", linestyle="-", label="Tie std dev")
    plt.plot(sample_sizes, win_std_devs, marker="o", linestyle="-", label="You win std dev")
    plt.plot(sample_sizes, lose_std_devs, marker="o", linestyle="-", label="You lose std dev")
    plt.xscale("log")
    plt.title("Standard Deviation of Outcome Proportions by Sample Size")
    plt.xlabel("Trials Per Batch (log scale)")
    plt.ylabel("Standard Deviation")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_mean_outcomes_with_error_bars(experiment_summaries):
    """
    Plot the mean outcome proportions with error bars equal to one
    standard deviation for each experiment stage.

    This graph shows:
    - the means stay near fairness
    - the error bars shrink as sample size grows
    """
    sample_sizes = []
    tie_means = []
    tie_stds = []
    win_means = []
    win_stds = []
    lose_means = []
    lose_stds = []

    for summary in experiment_summaries:
        sample_sizes.append(summary["trials_per_batch"])
        tie_means.append(summary["tie_mean"])
        tie_stds.append(summary["tie_std_dev"])
        win_means.append(summary["win_mean"])
        win_stds.append(summary["win_std_dev"])
        lose_means.append(summary["lose_mean"])
        lose_stds.append(summary["lose_std_dev"])

    plt.figure(figsize=(10, 6))
    plt.errorbar(sample_sizes, tie_means, yerr=tie_stds, fmt="o-", capsize=5, label="Tie")
    plt.errorbar(sample_sizes, win_means, yerr=win_stds, fmt="o-", capsize=5, label="You win")
    plt.errorbar(sample_sizes, lose_means, yerr=lose_stds, fmt="o-", capsize=5, label="You lose")
    plt.axhline(1 / 3, linestyle="--", label="Expected = 1/3")
    plt.xscale("log")
    plt.title("Mean Outcome Proportions with Standard Deviation Error Bars")
    plt.xlabel("Trials Per Batch (log scale)")
    plt.ylabel("Observed Proportion")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_timing_by_sample_size(experiment_summaries):
    """
    Plot the average timing per batch as sample size increases.

    This shows the tradeoff:
    - larger sample sizes reduce variance
    - but they cost more time
    """
    sample_sizes = []
    mean_times = []
    std_times = []

    for summary in experiment_summaries:
        sample_sizes.append(summary["trials_per_batch"])
        mean_times.append(summary["elapsed_ms_mean"])
        std_times.append(summary["elapsed_ms_std_dev"])

    plt.figure(figsize=(10, 6))
    plt.errorbar(sample_sizes, mean_times, yerr=std_times, fmt="o-", capsize=5)
    plt.xscale("log")
    plt.title("Average Batch Runtime by Sample Size")
    plt.xlabel("Trials Per Batch (log scale)")
    plt.ylabel("Elapsed Time (milliseconds)")
    plt.tight_layout()
    plt.show()


def print_interpretation(experiment_summaries):
    """
    Print a plain-English interpretation of the variance experiment.

    This is the teaching bridge between the math and the observed results.
    """
    print()
    print("Interpretation")
    print("=" * 40)
    print("1. Tiny sample sizes produce noisy, jumpy proportions.")
    print("   A single round can only produce 0%, 100%, or nothing in between for an outcome.")
    print()
    print("2. As the sample size increases, the batch results cluster more tightly around 1/3.")
    print("   That means the standard deviation gets smaller.")
    print()
    print("3. The mean outcome rates stay close to 1/3 across all reasonable large sample sizes.")
    print("   That is what we expect from a fair Rock, Paper, Scissors system.")
    print()
    print("4. Around 3000 trials per batch, the system should already look very stable.")
    print("   Running 10000 trials usually does not change the story very much.")
    print("   It mainly reduces the wiggle a little more while costing extra time.")
    print()
    print("5. So 3000 is a strong practical choice:")
    print("   large enough to be convincing, small enough to be efficient.")


def run_variance_demonstration_program():
    """
    Run the full stand-alone program.

    Program flow:
    1. Build the game rules
    2. Run repeated batches at different sample sizes
    3. Print summary statistics
    4. Print interpretation
    5. Show graphs
    """
    game_rules = build_game_rules()

    experiment_summaries = run_full_variance_experiment(game_rules)

    print_experiment_summary(experiment_summaries)
    print_interpretation(experiment_summaries)

    plot_outcome_bounce(experiment_summaries, "Tie")
    plot_outcome_bounce(experiment_summaries, "You win")
    plot_outcome_bounce(experiment_summaries, "You lose")

    plot_outcome_standard_deviation(experiment_summaries)
    plot_mean_outcomes_with_error_bars(experiment_summaries)
    plot_timing_by_sample_size(experiment_summaries)


run_variance_demonstration_program()