# bots.py — simple bot policies
import random
from typing import Optional, Tuple, List
from strategy import best_move

def choose_bot_play(hand, current_play, plays_by_size, bot_type: str) -> Optional[Tuple[int, List[int]]]:
    if not plays_by_size:
        return None
    if bot_type == "greedy":
        return best_move(hand, current_play, plays_by_size)
    # default 'random'
    size = random.choice(sorted(plays_by_size.keys()))
    opt = random.choice(plays_by_size[size])
    return (size, opt)

