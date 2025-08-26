import random

def generate_bit_string1(length):
    string1 = ''.join(random.choice('01') for _ in range(length))
    return string1
    
def generate_bit_string2(length):
    string2 = ''.join(random.choice('01') for _ in range(length))
    return string2

def bitwise_and(bit_string1, bit_string2):
    result = ''.join('1' if bit_string1[i] == '1' and bit_string2[i] == '1' else '0' for i in range(len(bit_string1)))
    return result

def bitwise_or(bit_string1, bit_string2):
    result = ''.join('1' if bit_string1[i] == '1' or bit_string2[i] == '1' else '0' for i in range(len(bit_string1)))
    return result

def bitwise_xor(bit_string1, bit_string2):
    result = ''.join('1' if bit_string1[i] != bit_string2[i] else '0' for i in range(len(bit_string1)))
    return result


bit_string1 = generate_bit_string1(5)
bit_string2 = generate_bit_string2(5)

print("Bit String 1:", bit_string1)
print("Bit String 2:", bit_string2)
print("Bitwise AND:", bitwise_and(bit_string1, bit_string2))
print("Bitwise OR:", bitwise_or(bit_string1, bit_string2))
print("Bitwise XOR:", bitwise_xor(bit_string1, bit_string2))
    
