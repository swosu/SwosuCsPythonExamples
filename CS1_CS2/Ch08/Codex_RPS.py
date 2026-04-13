"""
Rock, Paper, Scissors using a dictionary of dictionaries.

This module separates:
- game logic
- user interaction
- unit tests
- simulation and statistical analysis

Usage:
- `python Codex_RPS.py`
- `python Codex_RPS.py test`
- `python Codex_RPS.py stats`
"""

import math
import random
import sys


def build_valid_choices():
    """Return the legal moves for the game."""
    return ["rock", "paper", "scissors"]


def build_outcome_table():
    """Return the dictionary-of-dictionaries rule table."""
    return {
        "rock": {"rock": "tie", "paper": "lose", "scissors": "win"},
        "paper": {"rock": "win", "paper": "tie", "scissors": "lose"},
        "scissors": {"rock": "lose", "paper": "win", "scissors": "tie"},
    }


def normalize_player_choice(raw_text):
    """Return a cleaned version of user input."""
    return raw_text.strip().lower()


def is_valid_choice(choice, valid_choices):
    """Return True when the choice is legal."""
    return choice in valid_choices


def build_invalid_choice_message(valid_choices):
    """Return the invalid-input help message."""
    return (
        "Invalid choice. Please type one of these options: "
        + ", ".join(valid_choices)
        + "."
    )


def prompt_for_player_choice(valid_choices, input_func=input, print_func=print):
    """Prompt until the user enters a legal choice."""
    prompt = "Choose rock, paper, or scissors: "

    while True:
        raw_text = input_func(prompt)
        cleaned_choice = normalize_player_choice(raw_text)

        if is_valid_choice(cleaned_choice, valid_choices):
            return cleaned_choice

        print_func(build_invalid_choice_message(valid_choices))


def choose_computer_move(valid_choices, rng=None):
    """Return a random move for the computer."""
    if rng is None:
        rng = random
    return rng.choice(valid_choices)


def validate_lookup_choice(choice, valid_choices, label):
    """Raise ValueError when a lookup key is invalid."""
    if not is_valid_choice(choice, valid_choices):
        message = (
            f"Invalid {label} choice for lookup: {choice!r}. "
            f"Expected one of {valid_choices}."
        )
        raise ValueError(message)


def determine_round_result(player_choice, computer_choice, outcome_table):
    """Return win, lose, or tie using the dictionary-of-dictionaries."""
    valid_choices = list(outcome_table.keys())
    validate_lookup_choice(player_choice, valid_choices, "player")
    validate_lookup_choice(computer_choice, valid_choices, "computer")
    return outcome_table[player_choice][computer_choice]


def build_round_message(player_choice, computer_choice, result):
    """Return a friendly summary for one round."""
    result_map = {
        "win": "You win.",
        "lose": "You lose.",
        "tie": "It is a tie.",
    }
    return (
        f"You chose {player_choice}. "
        f"The computer chose {computer_choice}. "
        f"{result_map[result]}"
    )


def display_round_message(message, print_func=print):
    """Print the round message."""
    print_func(message)


def build_scoreboard():
    """Return a fresh scoreboard dictionary."""
    return {"win": 0, "lose": 0, "tie": 0, "rounds": 0}


def update_scoreboard(scoreboard, result):
    """Update the scoreboard for one result."""
    if result not in ("win", "lose", "tie"):
        raise ValueError(f"Invalid result for scoreboard update: {result!r}")

    scoreboard[result] += 1
    scoreboard["rounds"] += 1
    return scoreboard


def format_scoreboard(scoreboard):
    """Return a printable scoreboard string."""
    return (
        "Scoreboard\n"
        f"Rounds: {scoreboard['rounds']}\n"
        f"Wins:   {scoreboard['win']}\n"
        f"Losses: {scoreboard['lose']}\n"
        f"Ties:   {scoreboard['tie']}"
    )


def play_one_round(valid_choices, outcome_table, scoreboard, rng=None,
                   input_func=input, print_func=print):
    """Run one full interactive round and return round data."""
    player_choice = prompt_for_player_choice(valid_choices, input_func, print_func)
    computer_choice = choose_computer_move(valid_choices, rng)
    result = determine_round_result(player_choice, computer_choice, outcome_table)
    update_scoreboard(scoreboard, result)
    message = build_round_message(player_choice, computer_choice, result)
    display_round_message(message, print_func)

    return {
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "result": result,
    }


def normalize_yes_no(raw_text):
    """Return a cleaned yes/no response."""
    return raw_text.strip().lower()


def ask_to_play_again(input_func=input, print_func=print):
    """Return True when the user wants another round."""
    while True:
        answer = normalize_yes_no(input_func("Play again? (y/n): "))
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print_func("Please answer with y, yes, n, or no.")


def display_final_scoreboard(scoreboard, print_func=print):
    """Print the final game summary."""
    print_func("")
    print_func("Final results")
    print_func(format_scoreboard(scoreboard))


def play_game(input_func=input, print_func=print, rng=None):
    """Run the full interactive game loop."""
    valid_choices = build_valid_choices()
    outcome_table = build_outcome_table()
    scoreboard = build_scoreboard()

    print_func("Rock, Paper, Scissors")
    print_func("---------------------")

    keep_playing = True
    while keep_playing:
        play_one_round(
            valid_choices,
            outcome_table,
            scoreboard,
            rng=rng,
            input_func=input_func,
            print_func=print_func,
        )
        keep_playing = ask_to_play_again(input_func, print_func)

    display_final_scoreboard(scoreboard, print_func)
    return scoreboard


def simulate_computer_choices(number_of_trials, valid_choices, rng=None):
    """Count how often the computer selects each move."""
    if rng is None:
        rng = random.Random()

    counts = {choice: 0 for choice in valid_choices}
    for _ in range(number_of_trials):
        choice = choose_computer_move(valid_choices, rng)
        counts[choice] += 1
    return counts


def calculate_choice_percentages(choice_counts):
    """Convert move counts into percentages."""
    total = sum(choice_counts.values())
    if total == 0:
        return {choice: 0.0 for choice in choice_counts}

    return {
        choice: (count / total) * 100.0
        for choice, count in choice_counts.items()
    }


def expected_probability(number_of_categories):
    """Return the expected probability for equally likely categories."""
    return 1.0 / number_of_categories


def calculate_variance_from_expected(counts, expected_probability_value):
    """Return the variance of observed proportions from the expected value."""
    total = sum(counts.values())
    if total == 0:
        return 0.0

    observed_proportions = [count / total for count in counts.values()]
    squared_differences = [
        (proportion - expected_probability_value) ** 2
        for proportion in observed_proportions
    ]
    return sum(squared_differences) / len(squared_differences)


def calculate_margin_of_error(expected_probability_value, number_of_trials,
                              confidence_z_score=1.96):
    """Return the 95% confidence margin of error for a proportion."""
    standard_error = math.sqrt(
        (expected_probability_value * (1 - expected_probability_value))
        / number_of_trials
    )
    return confidence_z_score * standard_error


def build_confidence_interval(expected_probability_value, number_of_trials,
                              confidence_z_score=1.96):
    """Return the lower and upper bounds of the confidence interval."""
    margin = calculate_margin_of_error(
        expected_probability_value,
        number_of_trials,
        confidence_z_score,
    )
    lower_bound = max(0.0, expected_probability_value - margin)
    upper_bound = min(1.0, expected_probability_value + margin)
    return (lower_bound, upper_bound)


def evaluate_acceptance(observed_proportion, confidence_interval):
    """Return True when the observation falls inside the interval."""
    lower_bound, upper_bound = confidence_interval
    return lower_bound <= observed_proportion <= upper_bound


def analyze_choice_distribution(choice_counts):
    """Return counts, percentages, variance, and 95% interval checks."""
    total = sum(choice_counts.values())
    category_count = len(choice_counts)
    expected_p = expected_probability(category_count)
    confidence_interval = build_confidence_interval(expected_p, total)
    percentages = calculate_choice_percentages(choice_counts)

    analysis = {}
    for choice, count in choice_counts.items():
        observed_proportion = count / total if total else 0.0
        analysis[choice] = {
            "count": count,
            "percentage": percentages[choice],
            "proportion": observed_proportion,
            "inside_95_ci": evaluate_acceptance(
                observed_proportion,
                confidence_interval,
            ),
        }

    return {
        "trials": total,
        "expected_probability": expected_p,
        "confidence_interval": confidence_interval,
        "variance": calculate_variance_from_expected(choice_counts, expected_p),
        "choices": analysis,
    }


def display_choice_distribution(choice_counts, choice_percentages, print_func=print):
    """Print move counts and percentages."""
    print_func("Computer choice distribution")
    for choice in build_valid_choices():
        count = choice_counts[choice]
        percentage = choice_percentages[choice]
        print_func(f"{choice:9s}: {count:6d}  ({percentage:6.2f}%)")


def simulate_fixed_player_strategy(player_choice, number_of_trials, outcome_table,
                                   valid_choices, rng=None):
    """Simulate many rounds with one fixed player move."""
    validate_lookup_choice(player_choice, valid_choices, "player")
    if rng is None:
        rng = random.Random()

    scoreboard = build_scoreboard()
    for _ in range(number_of_trials):
        computer_choice = choose_computer_move(valid_choices, rng)
        result = determine_round_result(player_choice, computer_choice, outcome_table)
        update_scoreboard(scoreboard, result)
    return scoreboard


def compare_player_strategies(number_of_trials, outcome_table, valid_choices, rng=None):
    """Compare long-run outcomes for fixed player choices."""
    results = {}
    if rng is None:
        rng = random.Random()

    for player_choice in valid_choices:
        strategy_rng = random.Random(rng.randrange(1_000_000_000))
        results[player_choice] = simulate_fixed_player_strategy(
            player_choice,
            number_of_trials,
            outcome_table,
            valid_choices,
            rng=strategy_rng,
        )
    return results


def calculate_result_percentages(scoreboard):
    """Convert win/lose/tie totals into percentages."""
    total = scoreboard["rounds"]
    if total == 0:
        return {"win": 0.0, "lose": 0.0, "tie": 0.0}

    return {
        "win": (scoreboard["win"] / total) * 100.0,
        "lose": (scoreboard["lose"] / total) * 100.0,
        "tie": (scoreboard["tie"] / total) * 100.0,
    }


def analyze_strategy_fairness(strategy_results):
    """Analyze whether each fixed strategy is close to the expected 1/3 split."""
    expected_p = expected_probability(3)
    analyzed = {}

    for choice, scoreboard in strategy_results.items():
        confidence_interval = build_confidence_interval(expected_p, scoreboard["rounds"])
        percentages = calculate_result_percentages(scoreboard)

        analyzed[choice] = {
            "scoreboard": scoreboard,
            "percentages": percentages,
            "confidence_interval": confidence_interval,
            "checks": {
                result_name: evaluate_acceptance(
                    scoreboard[result_name] / scoreboard["rounds"],
                    confidence_interval,
                )
                for result_name in ("win", "lose", "tie")
            },
        }

    return analyzed


def display_strategy_comparison(strategy_results, print_func=print):
    """Print strategy comparison data."""
    print_func("Fixed-player strategy comparison")
    for choice in build_valid_choices():
        scoreboard = strategy_results[choice]
        percentages = calculate_result_percentages(scoreboard)
        print_func(
            f"{choice:9s}: "
            f"W {scoreboard['win']:5d} ({percentages['win']:6.2f}%), "
            f"L {scoreboard['lose']:5d} ({percentages['lose']:6.2f}%), "
            f"T {scoreboard['tie']:5d} ({percentages['tie']:6.2f}%)"
        )


def build_convergence_report(trial_counts, valid_choices, outcome_table, base_seed=2026):
    """Return simulation snapshots that show how results change with trial count."""
    report_rows = []

    for index, trial_count in enumerate(trial_counts):
        choice_rng = random.Random(base_seed + index)
        strategy_rng = random.Random(base_seed + 1000 + index)

        choice_counts = simulate_computer_choices(trial_count, valid_choices, choice_rng)
        choice_analysis = analyze_choice_distribution(choice_counts)

        strategy_results = compare_player_strategies(
            trial_count,
            outcome_table,
            valid_choices,
            strategy_rng,
        )
        fairness_analysis = analyze_strategy_fairness(strategy_results)

        report_rows.append(
            {
                "trial_count": trial_count,
                "choice_analysis": choice_analysis,
                "fairness_analysis": fairness_analysis,
            }
        )

    return report_rows


def display_convergence_report(report_rows, print_func=print):
    """Print a table showing how the simulation settles down as trials grow."""
    print_func("Convergence report")
    print_func(
        "Trials | Rock % | Paper % | Scissors % | "
        "Rock win % | Paper win % | Scissors win %"
    )

    for row in report_rows:
        trial_count = row["trial_count"]
        choices = row["choice_analysis"]["choices"]
        fairness = row["fairness_analysis"]
        print_func(
            f"{trial_count:6d} | "
            f"{choices['rock']['percentage']:6.2f} | "
            f"{choices['paper']['percentage']:7.2f} | "
            f"{choices['scissors']['percentage']:10.2f} | "
            f"{fairness['rock']['percentages']['win']:10.2f} | "
            f"{fairness['paper']['percentages']['win']:11.2f} | "
            f"{fairness['scissors']['percentages']['win']:14.2f}"
        )


def explain_statistical_conclusion():
    """Return a plain-English explanation of the simulation results."""
    return (
        "The computer has 3 equally likely choices, so the expected probability "
        "for rock, paper, and scissors is 1/3 each. The player also sees 3 "
        "equally likely outcomes in the long run: win, lose, and tie. A 95% "
        "confidence interval gives an acceptance band around 1/3. For a sample "
        "size of n, the margin of error is 1.96 * sqrt((1/3)*(2/3)/n). As the "
        "trial count increases, the margin of error gets smaller, and the "
        "observed percentages should settle closer to 33.33%."
    )


def run_statistical_analysis(print_func=print):
    """Run the randomness and fairness analysis."""
    valid_choices = build_valid_choices()
    outcome_table = build_outcome_table()
    number_of_trials = 10_000

    choice_rng = random.Random(2026)
    strategy_rng = random.Random(4040)

    choice_counts = simulate_computer_choices(number_of_trials, valid_choices, choice_rng)
    choice_percentages = calculate_choice_percentages(choice_counts)
    choice_analysis = analyze_choice_distribution(choice_counts)

    strategy_results = compare_player_strategies(
        number_of_trials,
        outcome_table,
        valid_choices,
        strategy_rng,
    )
    fairness_analysis = analyze_strategy_fairness(strategy_results)

    display_choice_distribution(choice_counts, choice_percentages, print_func)
    print_func("")
    lower_bound, upper_bound = choice_analysis["confidence_interval"]
    print_func(
        "95% confidence interval for each computer choice proportion: "
        f"{lower_bound * 100:.2f}% to {upper_bound * 100:.2f}%"
    )
    print_func(f"Observed variance from the expected 1/3 split: {choice_analysis['variance']:.6f}")

    print_func("")
    display_strategy_comparison(strategy_results, print_func)
    print_func("")
    print_func("95% confidence interval for each outcome proportion in a fixed strategy:")
    for choice in valid_choices:
        interval = fairness_analysis[choice]["confidence_interval"]
        print_func(
            f"{choice:9s}: {interval[0] * 100:.2f}% to {interval[1] * 100:.2f}%"
        )

    print_func("")
    print_func(explain_statistical_conclusion())
    print_func("")

    report_rows = build_convergence_report(
        [30, 100, 300, 1_000, 3_000, 10_000],
        valid_choices,
        outcome_table,
    )
    display_convergence_report(report_rows, print_func)


def test_build_valid_choices():
    """Test the legal-choice list."""
    choices = build_valid_choices()
    assert choices == ["rock", "paper", "scissors"]


def test_build_outcome_table_structure():
    """Test the rule-table shape and legal values."""
    table = build_outcome_table()
    choices = build_valid_choices()

    assert set(table.keys()) == set(choices)
    for outer_key in choices:
        assert isinstance(table[outer_key], dict)
        assert set(table[outer_key].keys()) == set(choices)
        for inner_key in choices:
            assert table[outer_key][inner_key] in ("win", "lose", "tie")


def test_all_rule_outcomes():
    """Test all 9 Rock-Paper-Scissors outcomes."""
    table = build_outcome_table()

    assert determine_round_result("rock", "rock", table) == "tie"
    assert determine_round_result("rock", "paper", table) == "lose"
    assert determine_round_result("rock", "scissors", table) == "win"

    assert determine_round_result("paper", "rock", table) == "win"
    assert determine_round_result("paper", "paper", table) == "tie"
    assert determine_round_result("paper", "scissors", table) == "lose"

    assert determine_round_result("scissors", "rock", table) == "lose"
    assert determine_round_result("scissors", "paper", table) == "win"
    assert determine_round_result("scissors", "scissors", table) == "tie"


def test_normalize_player_choice():
    """Test user-input cleanup."""
    assert normalize_player_choice(" Rock ") == "rock"
    assert normalize_player_choice("PAPER") == "paper"
    assert normalize_player_choice("scissors") == "scissors"


def test_is_valid_choice():
    """Test move validation."""
    choices = build_valid_choices()
    assert is_valid_choice("rock", choices) is True
    assert is_valid_choice("paper", choices) is True
    assert is_valid_choice("scissors", choices) is True
    assert is_valid_choice("lizard", choices) is False
    assert is_valid_choice("", choices) is False


def test_build_invalid_choice_message():
    """Test the invalid-input help message."""
    message = build_invalid_choice_message(build_valid_choices())
    assert "Invalid choice." in message
    assert "rock" in message
    assert "paper" in message
    assert "scissors" in message


def test_determine_round_result():
    """Test direct lookup behavior."""
    table = build_outcome_table()
    assert determine_round_result("rock", "scissors", table) == "win"
    assert determine_round_result("paper", "scissors", table) == "lose"
    assert determine_round_result("scissors", "scissors", table) == "tie"


def test_determine_round_result_invalid_key():
    """Test defensive handling of invalid lookup keys."""
    table = build_outcome_table()

    try:
        determine_round_result("lizard", "rock", table)
        assert False, "Expected ValueError for invalid player lookup key."
    except ValueError as error:
        assert "Invalid player choice for lookup" in str(error)

    try:
        determine_round_result("rock", "spock", table)
        assert False, "Expected ValueError for invalid computer lookup key."
    except ValueError as error:
        assert "Invalid computer choice for lookup" in str(error)


def test_build_scoreboard():
    """Test the initial scoreboard values."""
    scoreboard = build_scoreboard()
    assert scoreboard == {"win": 0, "lose": 0, "tie": 0, "rounds": 0}


def test_update_scoreboard():
    """Test scoreboard updates."""
    scoreboard = build_scoreboard()

    update_scoreboard(scoreboard, "win")
    assert scoreboard["win"] == 1
    assert scoreboard["rounds"] == 1

    update_scoreboard(scoreboard, "lose")
    assert scoreboard["lose"] == 1
    assert scoreboard["rounds"] == 2

    update_scoreboard(scoreboard, "tie")
    assert scoreboard["tie"] == 1
    assert scoreboard["rounds"] == 3


def test_choose_computer_move_with_seed():
    """Test seeded random move selection."""
    rng = random.Random(7)
    choices = build_valid_choices()
    observed = [choose_computer_move(choices, rng) for _ in range(5)]
    assert observed == ["paper", "rock", "paper", "scissors", "rock"]


def test_simulate_computer_choices_total():
    """Test that simulated computer moves add up correctly."""
    rng = random.Random(10)
    choices = build_valid_choices()
    counts = simulate_computer_choices(200, choices, rng)
    assert sum(counts.values()) == 200
    assert set(counts.keys()) == set(choices)


def test_simulate_fixed_player_strategy_total():
    """Test that a fixed-player strategy simulation tracks all rounds."""
    rng = random.Random(50)
    choices = build_valid_choices()
    table = build_outcome_table()
    scoreboard = simulate_fixed_player_strategy("rock", 120, table, choices, rng)
    assert scoreboard["rounds"] == 120
    assert scoreboard["win"] + scoreboard["lose"] + scoreboard["tie"] == 120


def test_calculate_margin_of_error():
    """Test the 95% confidence interval math."""
    margin = calculate_margin_of_error(1 / 3, 300)
    assert round(margin, 4) == 0.0533


def test_build_confidence_interval():
    """Test confidence interval construction."""
    interval = build_confidence_interval(1 / 3, 300)
    assert math.isclose(interval[0], 0.2799888900460552, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(interval[1], 0.3866777766206114, rel_tol=0.0, abs_tol=1e-12)


def test_evaluate_acceptance():
    """Test acceptance checking against the confidence interval."""
    interval = (0.28, 0.39)
    assert evaluate_acceptance(0.33, interval) is True
    assert evaluate_acceptance(0.41, interval) is False


def collect_test_functions():
    """Return the list of test functions in execution order."""
    return [
        test_build_valid_choices,
        test_build_outcome_table_structure,
        test_all_rule_outcomes,
        test_normalize_player_choice,
        test_is_valid_choice,
        test_build_invalid_choice_message,
        test_determine_round_result,
        test_determine_round_result_invalid_key,
        test_build_scoreboard,
        test_update_scoreboard,
        test_choose_computer_move_with_seed,
        test_simulate_computer_choices_total,
        test_simulate_fixed_player_strategy_total,
        test_calculate_margin_of_error,
        test_build_confidence_interval,
        test_evaluate_acceptance,
    ]


def run_all_tests(print_func=print):
    """Run every test and report pass/fail results."""
    test_functions = collect_test_functions()
    passed = 0
    failed = 0

    print_func("Running tests")
    print_func("-------------")

    for test_function in test_functions:
        try:
            test_function()
            print_func(f"PASS: {test_function.__name__}")
            passed += 1
        except AssertionError as error:
            print_func(f"FAIL: {test_function.__name__} -> {error}")
            failed += 1
        except Exception as error:  # Defensive runner behavior for unexpected errors.
            print_func(f"ERROR: {test_function.__name__} -> {error}")
            failed += 1

    print_func("")
    print_func(f"Passed: {passed}")
    print_func(f"Failed: {failed}")
    return failed == 0


def print_usage(print_func=print):
    """Print command-line usage help."""
    print_func("Usage:")
    print_func("python Codex_RPS.py        # play the game")
    print_func("python Codex_RPS.py test   # run unit tests")
    print_func("python Codex_RPS.py stats  # run simulations and statistics")


def main():
    """Dispatch to game mode, test mode, or statistics mode."""
    if len(sys.argv) == 1:
        play_game()
        return 0

    command = sys.argv[1].strip().lower()

    if command == "test":
        success = run_all_tests()
        return 0 if success else 1

    if command == "stats":
        run_statistical_analysis()
        return 0

    print_usage()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
