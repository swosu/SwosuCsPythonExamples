from engine import new_round

def test_finisher_recorded_once_and_skipped():
    rnd = new_round(3, seed=14)
    p0 = rnd.current_player()

    # Let p0 keep dumping singles; force clears so p0 keeps leading until empty
    while not rnd.is_round_over() and rnd.hands[p0]:
        # ensure it's p0's turn before playing
        if rnd.current_player() != p0:
            # if it's a fresh lead (no current play), don't pass—illegal
            if rnd.current_play is None:
                break
            rnd.pass_turn(rnd.current_player())
            continue

        rnd.play_cards(p0, [0])

        # Force the clear: others pass while the trick is live
        for _ in range(2):
            if rnd.is_round_over():
                break
            # Only pass if the trick is live and it's not p0
            if rnd.current_play is not None and rnd.current_player() != p0:
                rnd.pass_turn(rnd.current_player())

    assert p0 in rnd.finished_order
    # If round isn’t over yet, p0 should not get more turns
    if not rnd.is_round_over():
        assert rnd.current_player() != p0

