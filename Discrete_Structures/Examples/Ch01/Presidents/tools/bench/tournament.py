#!/usr/bin/env python3
import os, sys, time, random, argparse, multiprocessing as mp
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ROOT)

from engine import new_round
from strategy import generate_options
from bots import choose_bot_play

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
    return rnd.finished_order[0]  # winner pid

def worker(args):
    n_players, bot, seeds = args
    wins = [0]*n_players
    for s in seeds:
        w = run_round(n_players, bot, s)
        wins[w] += 1
    return wins

def chunk(lst, k):
    n = len(lst); step = (n + k - 1)//k
    for i in range(0, n, step):
        yield lst[i:i+step]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rounds", type=int, default=20000)
    ap.add_argument("--players", type=int, default=4)
    ap.add_argument("--bot", default="greedy")
    ap.add_argument("--procs", type=int, default=mp.cpu_count())
    ap.add_argument("--csv", default="")
    args = ap.parse_args()

    seeds = [random.randrange(1<<30) for _ in range(args.rounds)]
    t0 = time.perf_counter()
    with mp.Pool(args.procs) as pool:
        parts = list(chunk(seeds, args.procs))
        outs = pool.map(worker, [(args.players, args.bot, p) for p in parts])

    total_wins = [0]*args.players
    for w in outs:
        for i,v in enumerate(w):
            total_wins[i] += v

    dt = time.perf_counter() - t0
    rps = args.rounds/dt
    print(f"Rounds: {args.rounds} | Players: {args.players} | Bot: {args.bot} | Procs: {args.procs}")
    print(f"Time: {dt:.2f}s | {rps:.1f} rounds/sec")
    print("Wins:", total_wins)

    if args.csv:
        with open(args.csv, "a") as f:
            f.write("rounds,players,bot,procs,time,rounds_per_sec," +
                    ",".join([f"wins_p{i}" for i in range(args.players)]) + "\n")
            f.write(",".join(map(str, [args.rounds, args.players, args.bot, args.procs,
                                       f"{dt:.3f}", f"{rps:.1f}", *total_wins])) + "\n")

if __name__ == "__main__":
    main()

