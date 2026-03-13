from src.craps_rules import play_pass_line_round

def simulate_games(num_games):

    results = []

    for game_id in range(num_games):

        outcome, rolls = play_pass_line_round()

        results.append({
            "game_id": game_id,
            "outcome": outcome,
            "num_rolls": len(rolls),
            "sequence": rolls
        })

    return results