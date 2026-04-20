from src.fibonacci_metrics import fib_iterative, fib_recursive


def test_fib_iterative_base_cases():
    assert fib_iterative(0) == 0
    assert fib_iterative(1) == 1


def test_fib_iterative_known_values():
    known = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for n, expected in enumerate(known):
        assert fib_iterative(n) == expected


def test_fib_recursive_matches_iterative():
    for n in range(0, 20):
        assert fib_recursive(n) == fib_iterative(n), f"Mismatch at n={n}"


def test_fib_recursive_call_counter():
    counter = [0]
    fib_recursive(10, counter=counter)
    assert counter[0] > 1
