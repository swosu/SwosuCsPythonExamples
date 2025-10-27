import math

P = 1 / math.comb(49, 6)

def prob_at_least_one(T):
    if T <= 0:
        return 0.0
    return 1.0 - math.exp(T * math.log1p(-P))

def ev_jackpot(J, T, small_prize_ev=0.0):
    if T <= 0:
        return 0.0
    return J * prob_at_least_one(T) / T + small_prize_ev

def min_jackpot_for_t(T, target_ev=1.0, small_prize_ev=0.0):
    q = prob_at_least_one(T)
    if q <= 0:
        return float("inf")
    return max(0.0, (target_ev - small_prize_ev) * T / q)

def min_tickets_for_j(J, target_ev=1.0, small_prize_ev=0.0, max_T=50_000_000):
    if ev_jackpot(J, 1, small_prize_ev) >= target_ev:
        return 1
    low, high = 1, 2
    while high <= max_T and ev_jackpot(J, high, small_prize_ev) < target_ev:
        high *= 2
    if high > max_T:
        return None
    while low < high:
        mid = (low + high) // 2
        if ev_jackpot(J, mid, small_prize_ev) >= target_ev:
            high = mid
        else:
            low = mid + 1
    return low

if __name__ == "__main__":
    example_T = [1_000, 10_000, 100_000, 1_000_000]
    print("p (single-ticket jackpot probability) =", P)
    print()
    for T in example_T:
        required_J = min_jackpot_for_t(T)
        print(f"Tickets sold T={T:,}: min jackpot J to make EV >= $1 ≈ ${required_J:,.0f}")
    print()
    examples_J = [1_000_000, 10_000_000, 50_000_000]
    for J in examples_J:
        needed_T = min_tickets_for_j(J)
        if needed_T is None:
            print(f"Jackpot J=${J:,}: need more than search limit tickets to reach EV >= $1")
        else:
            print(f"Jackpot J=${J:,}: minimum tickets T so EV >= $1 ≈ {needed_T:,}")
    print()
    print("Sample EV calculations (jackpot only) for J=50,000,000:")
    for T in [1000, 10000, 100000, 1000000]:
        print(f" T={T:,} -> EV = ${ev_jackpot(50_000_000, T):.4f}")
