def bitwise_operations(bit_string1, bit_string2):
    # Ensure both bit strings are of equal length
    assert len(bit_string1) == len(bit_string2), "Bit strings must be of equal length"

    # Calculate bitwise AND
    bitwise_and = ''.join(['1' if bit_string1[i] == '1' and bit_string2[i] == '1' else '0' for i in range(len(bit_string1))])

    # Calculate bitwise OR
    bitwise_or = ''.join(['1' if bit_string1[i] == '1' or bit_string2[i] == '1' else '0' for i in range(len(bit_string1))])

    # Calculate bitwise XOR
    bitwise_xor = ''.join(['1' if bit_string1[i] != bit_string2[i] else '0' for i in range(len(bit_string1))])

    return bitwise_and, bitwise_or, bitwise_xor

while True:
    # Example usage with user inputs
    while True:
        try:
            bit_string1 = format(int(input("Enter first integer: ")), 'b')
            bit_string2 = format(int(input("Enter second integer: ")), 'b')
            break
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    # Ensure both bit strings are of equal length by padding with leading zeros
    max_len = max(len(bit_string1), len(bit_string2))
    bit_string1 = bit_string1.zfill(max_len)
    bit_string2 = bit_string2.zfill(max_len)

    and_result, or_result, xor_result = bitwise_operations(bit_string1, bit_string2)
    print(f"Binary of {int(bit_string1, 2)}: {bit_string1}")
    print(f"Binary of {int(bit_string2, 2)}: {bit_string2}")
    print(f"Bitwise AND: {and_result}")
    print(f"Bitwise OR: {or_result}")
    print(f"Bitwise XOR: {xor_result}")
    

    # Ask if the user wants to continue
    continue_prompt = input("Do you want to enter new integers? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        break
