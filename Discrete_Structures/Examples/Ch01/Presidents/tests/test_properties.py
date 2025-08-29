from hypothesis import given, strategies as st
from cards import RANKS, SUITS, Card
from engine import Play  # if Play is a dataclass; otherwise adapt
from strategy import generate_options, ranks_strictly_higher_than

all_cards = [Card(r, s) for r in RANKS for s in SUITS]

@given(
    hand=st.lists(st.sampled_from(all_cards), min_size=1, max_size=13, unique=True),
    # Either None (lead) or a legal Play size with some rank
    cur=st.one_of(
        st.just(None),
        st.builds(lambda sz, rk: Play(size=sz, rank=rk),
                  st.sampled_from([1,2,3,4]),
                  st.sampled_from(RANKS))
    )
)
def test_generate_options_only_offers_legal_moves(hand, cur):
    plays = generate_options(hand, cur)
    for size, opts in plays.items():
        for idxs in opts:
            # all cards in the option share a rank
            ranks = {hand[i].rank for i in idxs}
            assert len(ranks) == 1
            assert len(idxs) == size
            if cur is None:
                # leading: any size allowed
                assert size in {1,2,3,4}
            else:
                # must match size
                assert size == cur.size
                # and be strictly higher rank
                rank = next(iter(ranks))
                assert rank in ranks_strictly_higher_than(cur.rank)

