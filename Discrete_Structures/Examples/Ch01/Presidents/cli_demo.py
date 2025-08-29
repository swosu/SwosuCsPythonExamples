# cli_demo.py — improved CLI with lobby + strict option filtering

import sys
import random


from engine import (
    new_round, classify_play, is_legal_follow, Play,
    singles_with_break_info, n_kind_with_break_info,
    best_non_breaking_single, best_non_breaking_n_kind,  # ADD THESE
)
from cards import RANKS, RANK_TO_VALUE
from strategy import (
    ranks_strictly_higher_than,
    generate_options,
    best_move,
)
from bots import choose_bot_play

BOT_TYPES = ["random", "greedy"]  # placeholder list; behavior TBA

def setup_lobby():
    print("=== Presidents CLI Setup ===")
    while True:
        try:
            humans = int(input("How many human players? (1-4): ").strip())
            if 1 <= humans <= 4:
                break
        except Exception:
            pass
        print("Please enter a number from 1 to 4.")
    while True:
        try:
            bots = int(input("How many bot players? (0-4): ").strip())
            if 0 <= bots <= 4 and humans + bots >= 2:
                break
        except Exception:
            pass
        print("Enter 0–4 (and total players must be at least 2).")

    names = []
    for i in range(humans):
        n = input(f"Name for Human #{i+1}: ").strip() or f"Human{i+1}"
        names.append(("human", n, None))

    for i in range(bots):
        n = input(f"Name for Bot #{i+1}: ").strip() or f"Bot{i+1}"
        print("Choose bot type:")
        for idx, t in enumerate(BOT_TYPES, 1):
            print(f" {idx}. {t}")
        while True:
            try:
                pick = int(input("Type number: ").strip())
                if 1 <= pick <= len(BOT_TYPES):
                    break
            except Exception:
                pass
            print("Pick a valid number.")
        names.append(("bot", n, BOT_TYPES[pick-1]))

    return names  # list of tuples (kind, name, bot_type|None)


def explain_follow(prev_play, candidate_size, candidate_rank):
    """
    Return a human-friendly explanation of whether (candidate_size of candidate_rank)
    is allowed on top of prev_play.
    """
    if prev_play is None:
        return "Legal: you’re leading—any size and rank may start the trick."
    if candidate_size != prev_play.size:
        return f"Illegal: must play {prev_play.size}-of-a-kind to follow, not {candidate_size}."
    if RANK_TO_VALUE[candidate_rank] <= RANK_TO_VALUE[prev_play.rank]:
        return (f"Illegal: rank must be strictly higher than {prev_play.rank}. "
                f"{candidate_rank} does not beat it.")
    return (f"Legal: {candidate_size}-of-a-kind {candidate_rank} beats "
            f"{prev_play.size}-of-a-kind {prev_play.rank}.")



def cards_str(cards):
    return " ".join(str(c) for c in cards)


def suggestion_line_for_lead(hand):
    """Return a pretty multi-category suggestion string for a fresh lead, or None."""
    parts = []
    # Best safe single (doesn't break sets)
    s = best_non_breaking_single(hand)
    if s:
        parts.append(f"1 card -> {s}")
    # Best safe pair/triple/quad
    for n in (2, 3, 4):
        grp = best_non_breaking_n_kind(hand, n)
        if grp:
            parts.append(f"{n} cards -> {cards_str(grp)}")
    if parts:
        return "Suggestion: " + " | ".join(parts)
    return None

def format_minimum_needed(current_play):
    if current_play is None:
        return "You are leading; any legal size is allowed."
    need = ranks_strictly_higher_than(current_play.rank)
    if not need:
        return f"Nothing beats {current_play.rank}; passing is your only option."
    return f"Minimum to beat: {current_play.size} x higher than {current_play.rank} (i.e., {', '.join(need)})."


def plural(n, word):
    return f"{n} {word}" + ("" if n == 1 else "s")


def break_tag(count: int) -> str:
    return {
        1: "",    # not breaking anything
        2: "[breaks pair]",
        3: "[breaks triple]",
        4: "[breaks quad]",
    }.get(count, "")


def run_cli_demo():
    players = setup_lobby()
    num_players = len(players)
    rnd = new_round(num_players, seed=42)

    print("\n=== Presidents CLI Demo ===")
    print("Players:")
    for i, (_, name, kind) in enumerate(players):
        extra = f" [{kind}]" if kind else ""
        print(f" {i}: {name}{extra}")

    while not rnd.is_round_over():
        pid = rnd.current_player()
        kind, name, bot_type = players[pid]
        hand = rnd.hands[pid]
        print(f"\n{name}'s turn. Your hand: {' '.join(map(str, hand))}")
        if rnd.current_play:
            print(f"Top of pile: {rnd.current_play.size} x {rnd.current_play.rank}+")
        else:
            print("Top of pile: (none) — you lead")

        print(format_minimum_needed(rnd.current_play))

        plays = generate_options(hand, rnd.current_play)
        if not plays:
            print("No legal plays. You must pass.")
            rnd.pass_turn(pid)
            continue

        # Bots not yet implemented—stub: always pass (or we could add random soon)
        if kind == "bot":
            print(f"{name} (bot) is thinking...")
            try:
                move = choose_bot_play(hand, rnd.current_play, plays, bot_type or "greedy")
                if not move:
                    rnd.pass_turn(pid)
                    print(f"{name} passes.")
                else:
                    size, indices = move
                    cards_txt = " ".join(str(hand[j]) for j in indices)
                    rnd.play_cards(pid, indices)
                    print(f"{name} plays {cards_txt} ({size}-kind).")
            except Exception as e:
                print(f"{name} (bot) error:", e)
                # if something goes wrong, fail safe: pass
                rnd.pass_turn(pid)
            continue

        # Human menu: only offer valid sizes
        menu_sizes = sorted(plays.keys())
        menu_map = {str(i+1): s for i, s in enumerate(menu_sizes)}
        labels = ", ".join(f"{k}={menu_map[k]}-kind" for k in menu_map)
        if rnd.current_play is None:
            print(f"Options: {labels}")
        else:
            print(f"Options: {labels}, p=pass")
        choice = input("Your choice: ").strip().lower()

        if choice == "p":
            try:
                rnd.pass_turn(pid)
                print("You passed.")
            except Exception as e:
                print("Invalid pass:", e)
            continue





        if choice not in menu_map:
            print("Invalid selection.")
            continue

        size = menu_map[choice]
        opts = plays[size]

        # Map rank -> indices in hand to detect breaks
        by_rank = {}
        for idx, c in enumerate(hand):
            by_rank.setdefault(c.rank, []).append(idx)

        # Suggestions:
        if rnd.current_play is None:
            # On a fresh lead, show multiple categories (safe, non-breaking)
            multi = suggestion_line_for_lead(hand)
            if multi:
                print(multi)
        else:
            # When following, keep the existing best-move pointer
            suggestion = best_move(hand, rnd.current_play, plays)
            if suggestion:
                s_size, s_opt = suggestion
                s_cards = " ".join(str(hand[j]) for j in s_opt)
                print(f"Suggestion: {plural(s_size, 'card')} -> {s_cards}")

        # Show options with break warnings for ANY size if it consumes part of a larger group
        for i, opt in enumerate(opts, 1):
            rank = hand[opt[0]].rank
            group_size = len(by_rank[rank])
            tag = break_tag(group_size) if group_size > size else ""
            cards_text = " ".join(str(hand[j]) for j in opt)
            print(f"{i}. {cards_text} {tag}".rstrip())
        
        # --- Teaching hints (non-selectable info) when LEADING ---
        if rnd.current_play is None:
            # 1) If leading singles, show the breaking singles you could also lead
            if size == 1:
                breaking_singles = [c for (c, lbl) in singles_with_break_info(hand) if lbl]
                if breaking_singles:
                    print("Other lead singles (would break sets): " + " ".join(str(c) for c in breaking_singles))

            # 2) Preview other lead categories (pairs/triples/quads) with break labels
            for n in (2, 3, 4):
                groups = n_kind_with_break_info(hand, n)
                if groups:
                    # Show up to 3 examples to keep it tidy
                    examples = []
                    for cards_list, lbl in groups[:3]:
                        ex = cards_str(cards_list)
                        if lbl:
                            ex += f" [{lbl}]"
                        examples.append(ex)
                    print(f"Also possible lead: {n}-kind e.g.: " + " | ".join(examples))
        # --- End teaching hints ---




        raw = input("Pick which option (or p=pass): ").strip().lower()
        if raw == "p":
            try:
                rnd.pass_turn(pid)
                print("You passed.")
            except Exception as e:
                print("Invalid pass:", e)
            continue
        if raw == "":
            print("Tip: enter a number to play, or 'p' to pass.")
            continue
        try:
            sel = int(raw) - 1

            chosen = opts[sel]

            # If this play will break a larger set, confirm first (works for any size)
            chosen_rank = hand[chosen[0]].rank
            group_size = len(by_rank[chosen_rank])
            if group_size > size:
                # Correct mapping: 2->pair, 3->triple, 4->quad
                kind_map = {2: "pair", 3: "triple", 4: "quad"}
                kind = kind_map.get(group_size, "set")
                confirm = input(
                    f"This will break a {kind}. Proceed? [y/N]: "
                ).strip().lower()
                if confirm != "y":
                    print("Okay, not playing that. You may choose another option or pass.")
                    continue


            rnd.play_cards(pid, chosen)
            print("Played successfully.")
        except Exception as e:
            print("Invalid play:", e)



    # End of round
    print("\n=== Round finished! ===")
    order = rnd.finished_order
    if order:
        pres = players[order[0]][1]
        scum = players[order[-1]][1]
        names_line = " > ".join(players[i][1] for i in order)
        print(f"Finish order: {names_line}")
        print(f"President: {pres}")
        if len(order) >= 2:
            print(f"Scum: {scum}")


if __name__ == "__main__":
    try:
        run_cli_demo()
    except KeyboardInterrupt:
        sys.exit(0)

