def string_to_bitstring(s):
    """Convert a string to its binary representation as a bit string."""
    bitstring = ''.join(format(ord(char), '08b') for char in s)
    return bitstring

def pad_bitstrings(bitstring1, bitstring2):
    """Pad the shorter bit string with leading zeros to make both strings the same length."""
    max_len = max(len(bitstring1), len(bitstring2))
    bitstring1 = bitstring1.zfill(max_len)
    bitstring2 = bitstring2.zfill(max_len)
    return bitstring1, bitstring2

def bitwise_and(bitstring1, bitstring2):
    """Perform a bitwise AND operation on two bit strings."""
    bitstring1, bitstring2 = pad_bitstrings(bitstring1, bitstring2)
    return ''.join('1' if b1 == '1' and b2 == '1' else '0' for b1, b2 in zip(bitstring1, bitstring2))

def bitwise_or(bitstring1, bitstring2):
    """Perform a bitwise OR operation on two bit strings."""
    bitstring1, bitstring2 = pad_bitstrings(bitstring1, bitstring2)
    return ''.join('1' if b1 == '1' or b2 == '1' else '0' for b1, b2 in zip(bitstring1, bitstring2))

def bitwise_xor(bitstring1, bitstring2):
    """Perform a bitwise XOR operation on two bit strings."""
    bitstring1, bitstring2 = pad_bitstrings(bitstring1, bitstring2)
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bitstring1, bitstring2))

def print_results(and_result, or_result, xor_result):
    """Print the results of the bitwise operations."""
    print("Bitwise AND Result: ", and_result)
    print("Bitwise OR Result:  ", or_result)
    print("Bitwise XOR Result: ", xor_result)

def main():
    # Ask the user for two phrases
    phrase1 = input("Enter the first phrase: ")
    phrase2 = input("Enter the second phrase: ")

    # Convert the phrases to bit strings
    bitstring1 = string_to_bitstring(phrase1)
    bitstring2 = string_to_bitstring(phrase2)

    # Perform bitwise operations
    and_result = bitwise_and(bitstring1, bitstring2)
    or_result = bitwise_or(bitstring1, bitstring2)
    xor_result = bitwise_xor(bitstring1, bitstring2)

    # Print the results
    print_results(and_result, or_result, xor_result)

if __name__ == "__main__":
    main()
