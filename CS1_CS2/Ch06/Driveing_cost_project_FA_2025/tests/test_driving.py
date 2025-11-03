import driving

def test_simple_driving_cost():
    # From the prompt: driving_cost(20.0, 3.1599, 50.0) == 7.89975
    result = driving.driving_cost(20.0, 3.1599, 50.0)
    assert abs(result - 7.89975) < 1e-6
