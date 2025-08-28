# cli_demo.py — improved CLI with lobby + strict option filtering
from engine import new_round, classify_play, is_legal_follow, Play
from cards import RANKS, RANK_TO_VALUE
import sys

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

def ranks_strictly_higher_than(rank: str):
    v = RANK_TO_VALUE[rank]
    return [r for r in RANKS if RANK_TO_VALUE[r] > v]

def generate_options(hand, current_play):





    """
    Return dict {size: [list_of_index_lists]} for LEGAL sizes only.
    Singles list includes ONLY true singletons (ranks with count==1),
    to avoid breaking pairs/trips/quads.
    """
    # Count indices by rank
    by_rank = {}
    for idx, c in enumerate(hand):
        by_rank.setdefault(c.rank, []).append(idx)

    # Which sizes are even legal this turn?
    if current_play is None:
        legal_sizes = {1, 2, 3, 4}
        higher_ranks = RANKS  # any rank allowed when leading
    else:
        legal_sizes = {current_play.size}
        higher_ranks = ranks_strictly_higher_than(current_play.rank)

    plays = {1: [], 2: [], 3: [], 4: []}
    for rank, indices in by_rank.items():
        # must be a rank that can follow (or any if leading)
        if current_play is not None and rank not in higher_ranks:
            continue

        count = len(indices)
        # Singles: only if this rank is a true singleton
        if 1 in legal_sizes and count == 1:
            plays[1].append([indices[0]])

        # Doubles/Triples/Quads: if we have enough copies
        for size in (2, 3, 4):
            if size in legal_sizes and count >= size:
                # For Presidents, any same-rank subset is equivalent—just expose the first N
                plays[size].append(indices[:size])

    # remove sizes with no options (so we don’t offer invalid menus)
    return {s: opts for s, opts in plays.items() if opts}

def format_minimum_needed(current_play):
    if current_play is None:
        return "You are leading; any legal size is allowed."
    need = ranks_strictly_higher_than(current_play.rank)
    if not need:
        return f"Nothing beats {current_play.rank}; passing is your only option."
    return f"Minimum to beat: {current_play.size} x higher than {current_play.rank} (i.e., {', '.join(need)})."

def break_tag(count: int) -> str:
    return {
        1: "",    # not breaking anything
        2: "[breaks pair]",
        3: "[breaks triple]",
        4: "[breaks quad]",
    }.get(count, "")

def best_move(hand, current_play, plays_by_size):
    """
    Return (size, index_list) or None for a 'best' safe move.
    Heuristics:
      - Lead: lowest singleton; else lowest pair; else lowest triple; else quad.
      - Follow single: lowest higher singleton; else take 1 from the largest group (3/4 then 2).
      - Follow multi: lowest higher set of required size.
    """
    if not plays_by_size:
        return None

    # Map hand rank -> indices to know multiplicities
    by_rank = {}
    for idx, c in enumerate(hand):
        by_rank.setdefault(c.rank, []).append(idx)

    def option_rank(opt):  # opt is list of indices for a single-rank play
        return hand[opt[0]].rank

    def opt_value(opt):
        # used to sort by ascending strength
        from cards import RANK_TO_VALUE
        return RANK_TO_VALUE[option_rank(opt)]

    if current_play is None:
        # Prefer singles then pairs, etc. by ascending rank
        for size in (1, 2, 3, 4):
            if size in plays_by_size:
                candidates = sorted(plays_by_size[size], key=opt_value)
                return (size, candidates[0])
        return None

    need_size = current_play.size
    if need_size == 1:
        # Prefer true singletons first
        singles = plays_by_size.get(1, [])
        if singles:
            # Rank singletons only: those whose rank count==1 in hand
            true_singletons = [opt for opt in singles if len(by_rank[option_rank(opt)]) == 1]
            if true_singletons:
                return (1, sorted(true_singletons, key=opt_value)[0])
            # Otherwise, pick from biggest group so we likely leave a pair/triple intact
            # Sort candidates by (-group_count, value)
            singles_sorted = sorted(
                singles,
                key=lambda opt: (-len(by_rank[option_rank(opt)]), opt_value(opt))
            )
            return (1, singles_sorted[0])
        return None
    else:
        # Need exact size; pick lowest that beats
        if need_size in plays_by_size:
            candidates = sorted(plays_by_size[need_size], key=opt_value)
            return (need_size, candidates[0])
        return None



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
            print(f"{name} (bot) is thinking... (stub) -> pass")
            try:
                rnd.pass_turn(pid)
            except Exception as e:
                print("Bot failed to pass:", e)
            continue

        # Human menu: only offer valid sizes
        menu_sizes = sorted(plays.keys())
        menu_map = {str(i+1): s for i, s in enumerate(menu_sizes)}
        labels = ", ".join(f"{k}={menu_map[k]}-kind" for k in menu_map)
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
        for i, opt in enumerate(opts, 1):
            cards_str = " ".join(str(hand[j]) for j in opt)
            print(f"{i}. {cards_str}")
        try:
            sel = int(input("Pick which option: ").strip()) - 1
            rnd.play_cards(pid, opts[sel])
            print("Played successfully.")
        except Exception as e:
            print("Invalid play:", e)

    # End of round
    print("\n=== Round finished! Order:", rnd.finished_order)

if __name__ == "__main__":
    try:
        run_cli_demo()
    except KeyboardInterrupt:
        sys.exit(0)

