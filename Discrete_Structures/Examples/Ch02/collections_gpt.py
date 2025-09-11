from collections import Counter

# -------------------------------
# Classical Sets with Bit Strings
# -------------------------------
def bitstring_union(set_A_bits, set_B_bits):
    return [a | b for a, b in zip(set_A_bits, set_B_bits)]

def bitstring_intersection(set_A_bits, set_B_bits):
    return [a & b for a, b in zip(set_A_bits, set_B_bits)]

def bitstring_difference(set_A_bits, set_B_bits):
    return [a & ~b for a, b in zip(set_A_bits, set_B_bits)]

def bitstring_symmetric_diff(set_A_bits, set_B_bits):
    return [a ^ b for a, b in zip(set_A_bits, set_B_bits)]

# -------------------------------
# Multisets using Counter
# -------------------------------
def multiset_union(bag_A, bag_B):
    return bag_A | bag_B  # max of counts

def multiset_intersection(bag_A, bag_B):
    return bag_A & bag_B  # min of counts

def multiset_difference(bag_A, bag_B):
    return bag_A - bag_B  # subtract counts (no negatives)

def multiset_addition(bag_A, bag_B):
    return bag_A + bag_B  # add counts

# -------------------------------
# Fuzzy Sets (dict: element -> degree)
# -------------------------------
def fuzzy_union(fuzzy_A, fuzzy_B):
    return {x: max(fuzzy_A.get(x, 0), fuzzy_B.get(x, 0)) for x in set(fuzzy_A) | set(fuzzy_B)}

def fuzzy_intersection(fuzzy_A, fuzzy_B):
    return {x: min(fuzzy_A.get(x, 0), fuzzy_B.get(x, 0)) for x in set(fuzzy_A) | set(fuzzy_B)}

def fuzzy_complement(fuzzy_A):
    return {x: 1 - fuzzy_A[x] for x in fuzzy_A}

# -------------------------------
# Example Demo
# -------------------------------
if __name__ == "__main__":
    print("=== Classical Sets (bit strings) ===")
    evens_as_bits   = [1, 0, 1, 0, 1]  # {0, 2, 4}
    odds_as_bits    = [0, 1, 1, 0, 1]  # {1, 2, 4}
    print("Evens ∪ Odds =", bitstring_union(evens_as_bits, odds_as_bits))
    print("Evens ∩ Odds =", bitstring_intersection(evens_as_bits, odds_as_bits))
    print("Evens - Odds =", bitstring_difference(evens_as_bits, odds_as_bits))
    print("Evens ⊕ Odds =", bitstring_symmetric_diff(evens_as_bits, odds_as_bits))

    print("\n=== Multisets ===")
    bag_of_letters1 = Counter("aabc")   # {a:2, b:1, c:1}
    bag_of_letters2 = Counter("bccd")   # {b:1, c:2, d:1}
    print("Bag1 ∪ Bag2 =", multiset_union(bag_of_letters1, bag_of_letters2))
    print("Bag1 ∩ Bag2 =", multiset_intersection(bag_of_letters1, bag_of_letters2))
    print("Bag1 - Bag2 =", multiset_difference(bag_of_letters1, bag_of_letters2))
    print("Bag1 + Bag2 =", multiset_addition(bag_of_letters1, bag_of_letters2))

    print("\n=== Fuzzy Sets ===")
    fuzzy_weather_today   = {"sunny": 0.7, "cloudy": 0.2, "rainy": 0.9}
    fuzzy_weather_tomorrow = {"sunny": 0.5, "cloudy": 0.8, "rainy": 0.1}
    print("Today ∪ Tomorrow =", fuzzy_union(fuzzy_weather_today, fuzzy_weather_tomorrow))
    print("Today ∩ Tomorrow =", fuzzy_intersection(fuzzy_weather_today, fuzzy_weather_tomorrow))
    print("¬Today =", fuzzy_complement(fuzzy_weather_today))
