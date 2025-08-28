# tests/test_engine.py — core round flow: play/pass/clear/finish
import pytest
from engine import new_round, classify_play, is_legal_follow, Play
from cards import Card

def test_classify_and_follow_rules():
    # classify
    p = classify_play([Card("7","♣"), Card("7","♦")])
    assert p.size == 2 and p.rank == "7"
    with pytest.raises(ValueError):
        classify_play([])
    with pytest.raises(ValueError):
        classify_play([Card("7","♣"), Card("8","♣")])

    # follow rules
    assert is_legal_follow(None, Play("5",1))     # any lead is fine
    assert not is_legal_follow(Play("7",2), Play("9",1))  # size mismatch
    assert is_legal_follow(Play("7",2), Play("8",2))      # strictly higher, same size
    assert not is_legal_follow(Play("Q",3), Play("Q",3))  # must be strictly higher

def test_simple_trick_and_clear():
    rnd = new_round(3, seed=7)
    # Player order = [0,1,2]
    # Lead: P0 plays a single (lowest in their hand)
    p0 = rnd.current_player()
    hand0 = rnd.hands[p0]
    # choose lowest single (index 0)
    rnd.play_cards(p0, [0])
    assert rnd.current_play is not None
    # P1 passes, P2 passes -> pile clears and leader becomes last player who played (P0)
    p1 = rnd.current_player()
    rnd.pass_turn(p1)
    p2 = rnd.current_player()
    rnd.pass_turn(p2)
    # After clear, P0 should lead again and current_play is None
    assert rnd.current_play is None
    assert rnd.current_player() == p0

def test_finish_order_records_and_round_ends():
    rnd = new_round(2, seed=1)
    # Brutalize: each player always plays the first card they can until hands empty
    while not rnd.is_round_over():
        pid = rnd.current_player()
        hand = rnd.hands[pid]
        # if leading, must play; if following and illegal, pass
        played = False
        for i in range(len(hand)):
            try:
                rnd.play_cards(pid, [i])
                played = True
                break
            except Exception:
                continue
        if not played:
            rnd.pass_turn(pid)
    # finished_order has both players, first is the winner (President), second is Scum
    assert len(rnd.finished_order) == 2
    assert rnd.finished_order[0] != rnd.finished_order[1]

