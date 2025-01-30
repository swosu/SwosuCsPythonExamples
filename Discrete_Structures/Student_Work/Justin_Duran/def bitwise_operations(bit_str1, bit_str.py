def bitwise_operations(bit_str1, bit_str2):
    # Ensure both strings are of the same length
    if len(bit_str1) != len(bit_str2):
        raise ValueError("Bit strings must have the same length")
    
    # Convert the bit strings to integers
    num1 = int(bit_str1, 2)
    num2 = int(bit_str2, 2)
    
    # Perform bitwise AND, OR, and XOR
    and_result = num1 & num2
    or_result = num1 | num2
    xor_result = num1 ^ num2
    
    # Convert the results back to binary strings
    and_result_bin = bin(and_result)[2:].zfill(len(bit_str1))
    or_result_bin = bin(or_result)[2:].zfill(len(bit_str1))
    xor_result_bin = bin(xor_result)[2:].zfill(len(bit_str1))
    
    return and_result_bin, or_result_bin, xor_result_bin

# Example usage
bit_str1 = '1101'
bit_str2 = '1011'

and_result, or_result, xor_result = bitwise_operations(bit_str1, bit_str2)

print(f"AND: {and_result}")
print(f"OR: {or_result}")
print(f"XOR: {xor_result}")

