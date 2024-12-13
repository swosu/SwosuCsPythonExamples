def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def convert_to_binary(numbers):
    return [bin(num)[2:] for num in numbers]

n = 10
print(fibonacci(n))
print(convert_to_binary(fibonacci(n)))
