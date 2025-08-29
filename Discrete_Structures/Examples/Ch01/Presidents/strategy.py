# strategy.py — pure rules/choice helpers (no prints/UI)
from typing import Dict, List, Optional, Tuple
from cards import RANKS, RANK_TO_VALUE

def ranks_strictly_higher_than(rank: str) -> List[str]:
    v = RANK_TO_VALUE[rank]
    return [r for r in RANKS if RANK_TO_VALUE[r] > v]

def generate_options(hand, current_play) -> Dict[int, List[List[int]]]:
    """
    Return {size: [index_lists]} of LEGAL options for the current player.

    Policy:
      - Leading:
          singles include ONLY true singletons (avoid breaking sets by default);
          pairs/triples/quads also listed if available.
      - Following a single:
          list ALL higher singles (even if it breaks a set).
      - Following multi (pair/triple/quad):
          list only higher sets of that exact size.
    """
    # Count indices by rank
    by_rank = {}
    for idx, c in enumerate(hand):
        by_rank.setdefault(c.rank, []).append(idx)

    if current_play is None:
        legal_sizes = {1, 2, 3, 4}
        higher_ranks = RANKS
    else:
        legal_sizes = {current_play.size}
        higher_ranks = ranks_strictly_higher_than(current_play.rank)

    plays: Dict[int, List[List[int]]] = {1: [], 2: [], 3: [], 4: []}

    for rank, indices in by_rank.items():
        if current_play is not None and rank not in higher_ranks:
            continue

        count = len(indices)

        # Singles
        if 1 in legal_sizes:
            if current_play is None:
                if count == 1:           # only true singleton when leading
                    plays[1].append([indices[0]])
            else:
                if count >= 1:           # any higher single when following
                    plays[1].append([indices[0]])

        # Multi-sets
        for size in (2, 3, 4):
            if size in legal_sizes and count >= size:
                plays[size].append(indices[:size])

    return {s: opts for s, opts in plays.items() if opts}

def best_move(hand, current_play, plays_by_size) -> Optional[Tuple[int, List[int]]]:
    """
    Heuristics:
      - Lead: lowest singleton; else lowest pair; else lowest triple; else quad.
      - Follow single: lowest higher singleton; else take 1 from the largest group (3/4 then 2).
      - Follow multi: lowest higher set of required size.
    """
    if not plays_by_size:
        return None

    # multiplicities by rank
    by_rank = {}
    for idx, c in enumerate(hand):
        by_rank.setdefault(c.rank, []).append(idx)

    def option_rank(opt):          # opt is list of idx for one rank
        return hand[opt[0]].rank

    def opt_value(opt):            # for ascending strength
        return RANK_TO_VALUE[option_rank(opt)]

    if current_play is None:
        for size in (1, 2, 3, 4):
            if size in plays_by_size:
                return (size, sorted(plays_by_size[size], key=opt_value)[0])
        return None

    need_size = current_play.size
    if need_size == 1:
        singles = plays_by_size.get(1, [])
        if singles:
            # true singletons first
            true = [opt for opt in singles if len(by_rank[option_rank(opt)]) == 1]
            if true:
                return (1, sorted(true, key=opt_value)[0])
            # else take from largest group (prefer not to destroy pairs)
            singles_sorted = sorted(
                singles,
                key=lambda opt: (-len(by_rank[option_rank(opt)]), opt_value(opt))
            )
            return (1, singles_sorted[0])
        return None
    else:
        if need_size in plays_by_size:
            return (need_size, sorted(plays_by_size[need_size], key=opt_value)[0])
        return None

