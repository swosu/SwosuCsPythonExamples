from hypothesis import given, strategies as st
from cards import Card, RANKS, SUITS, RANK_TO_VALUE
from engine import Play, is_legal_follow

all_cards = [Card(r, s) for r in RANKS for s in SUITS]

@given(
    prev_size=st.sampled_from([1,2,3,4]),
    prev_rank=st.sampled_from(RANKS),
    next_size=st.sampled_from([1,2,3,4]),
    next_rank=st.sampled_from(RANKS),
)
def test_is_legal_follow_matches_rule(prev_size, prev_rank, next_size, next_rank):
    prev = Play(size=prev_size, rank=prev_rank)
    nxt  = Play(size=next_size, rank=next_rank)
    ok = is_legal_follow(prev, nxt)
    expected = (next_size == prev_size) and (RANK_TO_VALUE[next_rank] > RANK_TO_VALUE[prev_rank])
    assert ok == expected

