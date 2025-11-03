import math

def quadratic_formula(a, b, c):
    # TODO: Compute the quadratic formula results in variables x1 and x2

    first_coefficient = a
    second_coefficient = b
    third_coefficient = c

    discriminant = (second_coefficient ** 2) - (4 * first_coefficient * third_coefficient)
    if discriminant < 0:
        raise ValueError("The equation has no real solutions.")
    
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (-second_coefficient + sqrt_discriminant) / (2 * first_coefficient)
    x2 = (-second_coefficient - sqrt_discriminant) / (2 * first_coefficient)
    
    return (x1, x2)
   

def print_number(number, prefix_str):
    if float(int(number)) == number:
        print(f'{prefix_str}{number:.0f}')
    else:
        print(f'{prefix_str}{number:.2f}')
   

if __name__ == "__main__":
    input_line = input()
    split_line = input_line.split(" ")
    a = float(split_line[0])
    b = float(split_line[1])
    c = float(split_line[2])
    solution = quadratic_formula(a, b, c)
    print(f'Solutions to {a:.0f}x^2 + {b:.0f}x + {c:.0f} = 0')
    print_number(solution[0], 'x1 = ')
    print_number(solution[1], 'x2 = ')