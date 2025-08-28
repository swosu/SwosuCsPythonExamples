from cards import Card
from engine import Play
from cli_demo import generate_options

def mkhand(s: str):
    toks = s.split()
    return [Card(t[:-1], t[-1]) for t in toks]

def test_generate_options_exposes_single_from_pair_when_following():
    # Following single 8, pair 9s are legal as a single (breaks pair)
    hand = mkhand("9♣ 9♦")
    opts = generate_options(hand, Play("8", 1))
    # Expect some single available
    assert 1 in opts and len(opts[1]) >= 1

