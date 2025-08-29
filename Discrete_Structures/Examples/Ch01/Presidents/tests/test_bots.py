# tests/test_bots.py
import bots
from types import SimpleNamespace

def test_choose_bot_play_greedy(monkeypatch):
    hand = []
    cur = SimpleNamespace(size=1, rank="7")
    plays = {1: [[0], [1]], 2: [[2, 3]]}

    def fake_best_move(h, c, p):  # deterministic
        return (1, [1])

    monkeypatch.setattr(bots, "best_move", fake_best_move)
    assert bots.choose_bot_play(hand, cur, plays, "greedy") == (1, [1])

def test_choose_bot_play_random(monkeypatch):
    # Make random.choice deterministic (first element)
    calls = {"n": 0}
    def deterministic_choice(x):
        calls["n"] += 1
        # 1st call: x is sorted keys [1,2]; pick 1
        # 2nd call: x is plays[1] e.g. [[9], [10]]; pick first option
        return sorted(x)[0] if isinstance(x, set) or isinstance(x, list) else x[0]

    monkeypatch.setattr(bots.random, "choice", deterministic_choice)

    hand = []
    cur = None
    plays = {1: [[9], [10]], 2: [[20, 21]]}

    size, idxs = bots.choose_bot_play(hand, cur, plays, "random")
    assert size == 1
    assert idxs == [9]
    # sanity: we actually called random twice
    assert calls["n"] == 2


def test_choose_bot_play_none_when_no_options():
    assert bots.choose_bot_play([], None, {}, "random") is None

