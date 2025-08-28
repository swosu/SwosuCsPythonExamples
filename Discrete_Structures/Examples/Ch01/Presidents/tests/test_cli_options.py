# tests/test_cli_options.py — verify option filtering & singles logic
from cards import Card
from engine import Play
from cli_demo import generate_options

def mkhand(cards: str):
    # cards like "4♣ 4♦ 7♣ 8♦ 8♥ 9♣"
    toks = cards.split()
    out = []
    for t in toks:
        rank = t[:-1]
        suit = t[-1]
        out.append(Card(rank, suit))
    return out

def test_only_true_singles_listed_when_leading():
    # Hand has 4♣ 4♦ (pair of 4s) and single 7♣
    hand = mkhand("4♣ 4♦ 7♣ 8♦ 8♥")
    opts = generate_options(hand, current_play=None)
    # singles should list ONLY ranks with exactly one copy => 7♣
    singles = opts.get(1, [])
    shown = [[str(hand[i]) for i in idxs] for idxs in singles]
    assert ["7♣"] in shown
    # And should NOT include 4 or 8 singles
    flat = [c for group in shown for c in group]
    assert "4♣" not in flat and "8♦" not in flat and "8♥" not in flat

def test_size_filtered_when_following_single():
    # If pile is single 9+, only size=1 options appear
    hand = mkhand("4♣ 4♦ 7♣ 8♦ 8♥ 10♣ 10♦")
    opts = generate_options(hand, current_play=Play("9", 1))
    assert set(opts.keys()) == {1}  # doubles/triples not offered
    # and singles must be >9
    singles = opts[1]
    shown_ranks = {hand[idxs[0]].rank for idxs in singles}
    assert shown_ranks == {"10"}

def test_size_filtered_when_following_pair():
    # If pile is pair 6+, only pairs higher than 6 appear
    hand = mkhand("4♣ 4♦ 7♣ 7♦ 7♥ 8♦ 8♥ 9♣")
    opts = generate_options(hand, current_play=Play("6", 2))
    assert set(opts.keys()) == {2}
    pairs = opts[2]
    # pairs of 7, 8 are valid; 9 has only one copy here
    pair_ranks = []
    for idxs in pairs:
        r = {hand[i].rank for i in idxs}
        assert len(r) == 1
        pair_ranks.append(next(iter(r)))
    assert set(pair_ranks) == {"7", "8"}

