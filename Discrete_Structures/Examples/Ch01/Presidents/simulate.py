from engine import new_round
from strategy import generate_options
from bots import choose_bot_play

def simulate(n_rounds=200, n_players=4, bot_type="greedy", seed=12345):
    import random
    rng = random.Random(seed)
    wins = [0]*n_players
    for _ in range(n_rounds):
        rnd = new_round(n_players, seed=rng.randrange(1<<30))
        while not rnd.is_round_over():
            pid = rnd.current_player()
            hand = rnd.hands[pid]
            plays = generate_options(hand, rnd.current_play)
            move = choose_bot_play(hand, rnd.current_play, plays, bot_type)
            if move:
                _, indices = move
                rnd.play_cards(pid, indices)
            else:
                rnd.pass_turn(pid)
        wins[rnd.finished_order[0]] += 1
    print("Wins:", wins)

if __name__ == "__main__":
    simulate()

