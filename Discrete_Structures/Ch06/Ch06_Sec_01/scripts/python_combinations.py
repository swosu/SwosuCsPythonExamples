from math import comb
from itertools import combinations

# Count how many k-subsets of an n-set:
n, k = 6, 3
print(comb(n, k))  # 10

# List them explicitly for the set {a,b,c,d,e}:
S = ['a','b','c','d','e', 'f']
teams = list(combinations(S, k))
for t in teams:
    print(t)
