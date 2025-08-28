# cli_demo.py — simple 2-human CLI demo of Presidents round
from engine import RoundEngine, classify_play, is_legal_follow, new_round
from cards import Card
import sys

def generate_options(hand, current_play):
    """Return dict of possible plays grouped by size."""
    by_rank = {}
    for idx, c in enumerate(hand):
        by_rank.setdefault(c.rank, []).append(idx)
    plays = {1: [], 2: [], 3: [], 4: []}
    for rank, indices in by_rank.items():
        for size in (1, 2, 3, 4):
            if len(indices) >= size:
                chosen = indices[:size]
                try:
                    play = classify_play([hand[i] for i in chosen])
                    if is_legal_follow(current_play, play):
                        plays[size].append(chosen)
                except Exception:
                    continue
    return plays

def print_options(plays):
    for size, options in plays.items():
        if options:
            print(f" {size}-of-a-kind options:")
            for i, choice in enumerate(options, start=1):
                cards_str = " ".join(str(hand[i]) for i in choice)
                print(f"   {i}. {cards_str}")

def run_cli_demo():
    rnd = new_round(2, seed=42)
    print("=== Presidents CLI Demo (2 Humans) ===")
    while not rnd.is_round_over():
        pid = rnd.current_player()
        hand = rnd.hands[pid]
        print(f"\nPlayer {pid+1}'s turn. Your hand: {' '.join(map(str, hand))}")
        if rnd.current_play:
            print(f"Current pile: {rnd.current_play.size} x {rnd.current_play.rank}+")
        else:
            print("No current pile. You lead!")
        plays = generate_options(hand, rnd.current_play)
        if not any(plays.values()):
            print("No legal plays. You must pass.")
            rnd.pass_turn(pid)
            continue
        print("Options:")
        print(" 1 = singles, 2 = doubles, 3 = triples, 4 = quads, 5 = all, p = pass")
        choice = input("Your choice: ").strip().lower()
        if choice == "p":
            try:
                rnd.pass_turn(pid)
                print("You passed.")
            except Exception as e:
                print("Invalid pass:", e)
            continue
        if choice in {"1", "2", "3", "4"}:
            size = int(choice)
            opts = plays[size]
            if not opts:
                print("No options of that size.")
                continue
            for i, opt in enumerate(opts, 1):
                cards_str = " ".join(str(hand[j]) for j in opt)
                print(f"{i}. {cards_str}")
            sel = int(input("Pick which option: ")) - 1
            try:
                rnd.play_cards(pid, opts[sel])
                print("Played successfully.")
            except Exception as e:
                print("Invalid play:", e)
        elif choice == "5":
            for size, opts in plays.items():
                for i, opt in enumerate(opts, 1):
                    cards_str = " ".join(str(hand[j]) for j in opt)
                    print(f"{size}-of-a-kind option {i}: {cards_str}")
            continue
    print("\n=== Round finished! Order:", rnd.finished_order)

if __name__ == "__main__":
    try:
        run_cli_demo()
    except KeyboardInterrupt:
        sys.exit(0)

