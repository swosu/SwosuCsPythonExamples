from cards import Card
from engine import Play
from cli_demo import generate_options, best_move

def mkhand(s: str):
    toks = s.split()
    return [Card(t[:-1], t[-1]) for t in toks]

def test_best_move_follow_single_prefers_singleton_over_breaking_pair():
    # Hand: singleton 8♦ and pair of 10s; need to beat 7
    hand = mkhand("8♦ 10♣ 10♦")
    plays = generate_options(hand, Play("7", 1))
    size, opt = best_move(hand, Play("7", 1), plays)
    # Should pick 8♦, not crack the 10s
    assert size == 1
    assert str(hand[opt[0]]) == "8♦"

def test_best_move_follow_single_breaks_bigger_group_first():
    # Hand: pair of 9s and triple of Qs; need to beat J
    hand = mkhand("9♣ 9♦ Q♣ Q♦ Q♥")
    plays = generate_options(hand, Play("J", 1))
    size, opt = best_move(hand, Play("J", 1), plays)
    # Should take one Q (leaving a pair) instead of breaking the 9s
    assert size == 1
    r = hand[opt[0]].rank
    assert r == "Q"

