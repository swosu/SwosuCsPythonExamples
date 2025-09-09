import random
from collections import Counter, deque

# ----------------------------
# Presidents & Associates (Asshole) — 4 players, multi-round
# Sets only (singles/doubles/triples), no runs. Any 2 (single/double/triple) wipes pile.
# Round 1 start: holder of 3♣ must open with single 3♣.
# Later starts: President leads anything.
# Between rounds: taxation (card exchange) by titles.
# ----------------------------

SUITS = ["♣", "♦", "♥", "♠"]
RANK_ORDER = ["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
RANK_VALUE = {r:i for i, r in enumerate(RANK_ORDER, start=3)}  # 3->3, ..., 2->15
TITLES = ["President", "Vice President", "Citizen", "Asshole"]

def make_deck():
    return [(rank, suit) for rank in RANK_ORDER for suit in SUITS]

def card_str(c): return f"{c[0]}{c[1]}"
def sort_hand(hand): return sorted(hand, key=lambda c: (RANK_VALUE[c[0]], SUITS.index(c[1])))
def has_three_clubs(hand): return ("3","♣") in hand

def all_opening_plays(hand):
    plays = []
    by_rank = {}
    for r,s in hand:
        by_rank.setdefault(r, []).append((r,s))
    for r,cards in by_rank.items():
        cards_sorted = cards[:]
        n = len(cards_sorted)
        plays.append([cards_sorted[0]])
        if n >= 2: plays.append(cards_sorted[:2])
        if n >= 3: plays.append(cards_sorted[:3])
    return plays

def valid_plays_from_hand(hand, needed_count, must_beat_value):
    plays, by_rank = [], {}
    for r,s in hand:
        by_rank.setdefault(r, []).append((r,s))
    for r,cards in by_rank.items():
        if len(cards) >= needed_count and RANK_VALUE[r] > must_beat_value:
            plays.append(cards[:needed_count])
    return plays

def is_two_play(play_cards):
    return all(c[0] == "2" for c in play_cards)

def remove_cards(hand, play):
    newhand = hand[:]
    for c in play: newhand.remove(c)
    return newhand

def display_state(pnum, hands, table):
    print("\n" + "="*70)
    print(f"Current player: P{pnum+1}")
    for i,h in enumerate(hands):
        if i == 0:
            print(f"Your hand ({len(h)}): {', '.join(card_str(c) for c in sort_hand(h))}")
        else:
            print(f"P{i+1} hand: {len(h)} cards")
    lp = table["last_play"]
    if lp is None:
        print("Pile: [empty]  (leader can play any single/double/triple of one rank)")
    else:
        print(f"On pile: {lp['count']}×{lp['rank']}  (must match count with higher rank or pass)")
    if table["passes_in_row"] > 0:
        print(f"Passes in a row: {table['passes_in_row']}")
    print("="*70)

def choose_human_play(hand, table):
    lp = table["last_play"]
    legal = all_opening_plays(hand) if lp is None else valid_plays_from_hand(hand, lp["count"], RANK_VALUE[lp["rank"]])

    # De-dup by (rank,count) for clear menu
    seen, uniq = set(), []
    for play in legal:
        key = (play[0][0], len(play))
        if key not in seen:
            seen.add(key)
            uniq.append(play)

    if not uniq:
        print("You have no legal play. Press Enter to pass.")
        input()
        return None

    print("\nYour legal plays:")
    uniq = sorted(uniq, key=lambda p: (RANK_VALUE[p[0][0]], len(p)))
    for i,play in enumerate(uniq):
        print(f"  [{i}] {len(play)}×{play[0][0]} -> " + " ".join(card_str(c) for c in play))
    print("  [p] Pass")

    while True:
        choice = input("Choose index (or 'p' to pass): ").strip().lower()
        if choice == 'p': return None
        if choice.isdigit():
            ii = int(choice)
            if 0 <= ii < len(uniq):
                # map to actual cards in hand
                desired_rank = uniq[ii][0][0]
                need = len(uniq[ii])
                res = [c for c in hand if c[0] == desired_rank][:need]
                if len(res) == need: return res
        print("Invalid selection.")

def choose_cpu_play(hand, table):
    lp = table["last_play"]
    if lp is None:
        options = all_opening_plays(hand)
        def score(p):
            r, cnt = p[0][0], len(p)
            two_penalty = 10 if r == "2" and len(hand) > cnt else 0
            return (cnt, RANK_VALUE[r], two_penalty)
        return min(options, key=score)
    else:
        needed = lp["count"]
        plays = valid_plays_from_hand(hand, needed, RANK_VALUE[lp["rank"]])
        if not plays: return None
        two_plays = [p for p in plays if is_two_play(p)]
        if two_plays:
            two_plays.sort(key=lambda p: len(p))
            if len(hand) == len(two_plays[0]) or needed >= 2 or len(hand) <= 3:
                return two_plays[0]
        return min(plays, key=lambda p: (RANK_VALUE[p[0][0]], len(p)))

def deal_four():
    deck = make_deck()
    random.shuffle(deck)
    return [sorted(deck[i::4], key=lambda c: (RANK_VALUE[c[0]], SUITS.index(c[1]))) for i in range(4)]

def round_play(hands, starting_rule, starting_player):
    """Play a single round.
       starting_rule: 'three_clubs_must_open' OR 'president_leads'
       starting_player: index 0..3 who leads for this round
       Returns finishing order list of player indices (length 4)."""
    table = {"last_play": None, "needed_count": None, "passes_in_row": 0}
    finished_order, out = [], [False]*4
    turn_order = deque([0,1,2,3])
    while turn_order[0] != starting_player: turn_order.rotate(-1)

    three_clubs_forced = (starting_rule == "three_clubs_must_open")
    first_turn_done = False

    while len(finished_order) < 3:
        current = turn_order[0]
        if out[current]:
            turn_order.rotate(-1)
            continue

        leader = (table["last_play"] is None)
        if leader: table["passes_in_row"] = 0

        display_state(current, hands, table)

        # Determine play
        if three_clubs_forced and leader and not first_turn_done:
            # Whoever is at 'starting_player' must open with single 3♣.
            if current == starting_player:
                if ("3","♣") in hands[current]:
                    play = [("3","♣")]
                    print(f"Opening rule: P{current+1} must start with single 3♣.")
                    first_turn_done = True
                else:
                    # Safety (shouldn't happen if we aligned starting_player to holder)
                    play = choose_human_play(hands[current], table) if current == 0 else choose_cpu_play(hands[current], table)
            else:
                play = choose_human_play(hands[current], table) if current == 0 else choose_cpu_play(hands[current], table)
        else:
            play = choose_human_play(hands[current], table) if current == 0 else choose_cpu_play(hands[current], table)

        # Handle pass or validate play
        if play is None:
            print(f"P{current+1} passes.")
            table["passes_in_row"] += 1
            active_players = sum(1 for i in range(4) if not out[i])
            if table["last_play"] is not None and table["passes_in_row"] >= (active_players - 1):
                print(f"All others passed. Pile clears. Leader is P{table['last_play']['who']+1}.")
                while turn_order[0] != table["last_play"]["who"]:
                    turn_order.rotate(-1)
                table["last_play"] = None
                table["needed_count"] = None
                table["passes_in_row"] = 0
            else:
                turn_order.rotate(-1)
            continue
        else:
            # Validate
            if three_clubs_forced and leader and not first_turn_done and current == starting_player:
                if not (len(play) == 1 and play[0] == ("3","♣")):
                    print("Invalid. Opening move must be the single 3♣. Forcing it.")
                    play = [("3","♣")]
                first_turn_done = True
            else:
                if table["last_play"] is None:
                    ranks = {c[0] for c in play}
                    if len(ranks) != 1 or len(play) not in (1,2,3):
                        print("Invalid lead (must be 1/2/3 of the same rank). Treated as pass.")
                        play = None
                else:
                    need = table["last_play"]["count"]
                    ranks = {c[0] for c in play}
                    if len(ranks) != 1 or len(play) != need:
                        print(f"Invalid play (must play {need} of the same rank). Treated as pass.")
                        play = None
                    else:
                        r = next(iter(ranks))
                        if RANK_VALUE[r] <= RANK_VALUE[table["last_play"]["rank"]]:
                            print("Invalid (rank not high enough). Treated as pass.")
                            play = None

            if play is None:
                print(f"P{current+1} passes.")
                table["passes_in_row"] += 1
                active_players = sum(1 for i in range(4) if not out[i])
                if table["last_play"] is not None and table["passes_in_row"] >= (active_players - 1):
                    print(f"All others passed. Pile clears. Leader is P{table['last_play']['who']+1}.")
                    while turn_order[0] != table["last_play"]["who"]:
                        turn_order.rotate(-1)
                    table["last_play"] = None
                    table["needed_count"] = None
                    table["passes_in_row"] = 0
                else:
                    turn_order.rotate(-1)
                continue

        # Execute play
        print(f"P{current+1} plays: " + " ".join(card_str(c) for c in play))
        hands[current] = remove_cards(hands[current], play)
        last_rank, last_count = play[0][0], len(play)
        table["last_play"] = {"rank": last_rank, "count": last_count, "who": current, "cards": play[:] }
        table["needed_count"] = last_count
        table["passes_in_row"] = 0

        # Wipe on 2
        if is_two_play(play):
            print(">>> 2 played! Pile WIPED. Same player leads again. <<<")
            table["last_play"] = None
            table["needed_count"] = None
            table["passes_in_row"] = 0

        # Out?
        if len(hands[current]) == 0 and not out[current]:
            out[current] = True
            print(f"*** P{current+1} is OUT! ***")
            finished_order.append(current)

        # Rotate (unless wiped -> same player continues; but if they are out, advance to next)
        if table["last_play"] is None:
            if out[current]:
                turn_order.rotate(-1)
                while out[turn_order[0]]: turn_order.rotate(-1)
        else:
            turn_order.rotate(-1)
            while out[turn_order[0]]: turn_order.rotate(-1)

    # Append last remaining
    last_player = next(i for i in range(4) if i not in finished_order)
    finished_order.append(last_player)
    return finished_order

def pick_lowest(hand, k):
    return sort_hand(hand)[:k]

def pick_highest(hand, k):
    return list(reversed(sort_hand(hand)))[0:k]

def exchange_between_rounds(hands, finishing_order):
    """Apply taxation per titles:
       1st(Pres) <-> 4th(Asshole): 2 cards (Asshole gives highest 2, Pres returns lowest 2)
       2nd(VP)   <-> 3rd(Citizen): 1 card (Citizen gives highest 1, VP returns lowest 1)"""
    # Map positions to players
    pres, vp, citizen, asshole = finishing_order[0], finishing_order[1], finishing_order[2], finishing_order[3]

    # Asshole -> President: 2 highest; President returns 2 lowest
    a_gives = pick_highest(hands[asshole], 2)
    p_gives = pick_lowest(hands[pres], 2)
    for c in a_gives: hands[asshole].remove(c)
    for c in p_gives: hands[pres].remove(c)
    hands[pres].extend(a_gives)
    hands[asshole].extend(p_gives)

    # Citizen -> Vice President: 1 highest; VP returns 1 lowest
    c_gives = pick_highest(hands[citizen], 1)
    v_gives = pick_lowest(hands[vp], 1)
    for c in c_gives: hands[citizen].remove(c)
    for c in v_gives: hands[vp].remove(c)
    hands[vp].extend(c_gives)
    hands[citizen].extend(v_gives)

def show_standings(order):
    print("\n" + "#"*70)
    print("Round Placings:")
    for place, pid in enumerate(order, start=1):
        label = TITLES[place-1]
        mark = "(You)" if pid == 0 else ""
        print(f"{place}. P{pid+1} {mark} — {label}")
    print("#"*70)

def main():
    print("\nWelcome to Presidents & Associates — Multi-Round (4 players).")
    print("Rules: sets only (single/double/triple), must beat rank to match count, any 2 wipes,")
    print("Round 1: holder of 3♣ opens with single 3♣. Later rounds: President leads anything.")
    print("Between rounds: Asshole gives top 2 to President (gets lowest 2 back); Citizen gives top 1 to VP (gets lowest 1 back).")
    print("You are Player 1; P2–P4 are CPU.\n")

    round_num = 1
    president_player = None  # set after first round

    while True:
        # Deal fresh hands
        hands = deal_four()

        # Figure starting player and rule
        if round_num == 1:
            # Holder of 3♣ must open
            starter = next(i for i in range(4) if has_three_clubs(hands[i]))
            starting_rule = "three_clubs_must_open"
        else:
            starter = president_player
            starting_rule = "president_leads"

        # If round_num > 1, perform taxation BEFORE play (after dealing)
        if round_num > 1:
            print(f"\n=== Round {round_num}: Card Exchange (Taxation) ===")
            # We need titles from the previous round to decide exchange.
            # 'president_player' is known; but we also need 2nd/3rd/4th from last round.
            # We'll store last finishing_order to use here. So, we keep it outside the loop too.
            # We'll have saved 'last_order' at the end of previous loop iteration.
            exchange_between_rounds(hands, last_order)
            print("Exchange completed.")

        # Play round
        print(f"\n=== Round {round_num} Begins ===")
        order = round_play(hands, starting_rule, starter)
        show_standings(order)

        # Save president & last_order for next loop
        president_player = order[0]
        last_order = order[:]

        # Ask to continue
        ans = input("Play another round? [Y/n]: ").strip().lower()
        if ans == 'n':
            print("Thanks for playing!")
            break
        round_num += 1

if __name__ == "__main__":
    main()
