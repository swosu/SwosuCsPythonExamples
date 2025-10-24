<<<<<<< HEAD
import math, random

def min_n_for_p(p, days=365):
    prob_unique = 1.0
    n = 0
    while True:
        n += 1
        if n > days + 1:
            return n
        if n > 1:
            prob_unique *= (days - (n - 1)) / days
        if 1 - prob_unique >= p:
            return n

targets = [0.70, 0.80, 0.90, 0.95, 0.99]
thresholds = {p: min_n_for_p(p) for p in targets}
print("Exact thresholds:", thresholds)

def simulate(n, trials=50000, days=365):
    hits = 0
    for _ in range(trials):
        seen = set()
        dup = False
        for _ in range(n):
            b = random.randrange(days)
            if b in seen:
                dup = True
                break
            seen.add(b)
        hits += dup
    return hits / trials

for n in [30, 35, 41, 47, 57]:
    print(n, simulate(n))
=======
import math, random

def min_n_for_p(p, days=365):
    prob_unique = 1.0
    n = 0
    while True:
        n += 1
        if n > days + 1:
            return n
        if n > 1:
            prob_unique *= (days - (n - 1)) / days
        if 1 - prob_unique >= p:
            return n

targets = [0.70, 0.80, 0.90, 0.95, 0.99]
thresholds = {p: min_n_for_p(p) for p in targets}
print("Exact thresholds:", thresholds)

def simulate(n, trials=50000, days=365):
    hits = 0
    for _ in range(trials):
        seen = set()
        dup = False
        for _ in range(n):
            b = random.randrange(days)
            if b in seen:
                dup = True
                break
            seen.add(b)
        hits += dup
    return hits / trials

for n in [30, 35, 41, 47, 57]:
    print(n, simulate(n))
>>>>>>> cb2846c (Add lottery_ticket.py under Student_Codes/Fedor_portnoi)
