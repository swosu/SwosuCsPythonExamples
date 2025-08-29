#!/usr/bin/env python3
import time, argparse, random
from engine import new_round
from strategy import generate_options, best_move
from bots import choose_bot_play

touch tools/__init__.py
touch tools/bench/__init__.py

def run_round(n_players, bot_type, seed):
    rnd = new_round(n_players, seed=seed)
    while not rnd.is_round_over():
        pid = rnd.current_player()
        hand = rnd.hands[pid]
        plays = generate_options(hand, rnd.current_play)
        mv = choose_bot_play(hand, rnd.current_play, plays, bot_type)
        if mv:
            _, idxs = mv
            rnd.play_cards(pid, idxs)
        else:
            rnd.pass_turn(pid)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rounds", type=int, default=2000)
    ap.add_argument("--players", type=int, default=4)
    ap.add_argument("--bot", default="greedy")
    args = ap.parse_args()
    t0 = time.perf_counter()
    rng = random.Random(1234)
    for _ in range(args.rounds):
        run_round(args.players, args.bot, rng.randrange(1<<30))
    dt = time.perf_counter() - t0
    rps = args.rounds/dt
    print(f"Rounds: {args.rounds} | Players: {args.players} | Bot: {args.bot}")
    print(f"Time: {dt:.3f}s | {rps:.1f} rounds/sec")

if __name__ == "__main__":
    main()

