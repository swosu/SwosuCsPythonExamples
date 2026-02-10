def caesar_cipher(text, shift):
    """
    Encrypts or decrypts a text using the Caesar cipher.

    :param text: The input string to be encrypted/decrypted
    :param shift: The number of positions each character in the text is shifted
    :return: Encrypted/Decrypted text
    """
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            # Shift within lowercase letters
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            # Shift within uppercase letters
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)

    return ''.join(result)


# call the function with 'see you in the park' and a shift of 6
if __name__ == "__main__":
    original_text = "see you in the park"
    shift_value = -5

    encrypted_text = caesar_cipher(original_text, shift_value)
    print(f"Encrypted Text: {encrypted_text}")

    decrypted_text = caesar_cipher(encrypted_text, -shift_value)
    print(f"Decrypted Text: {decrypted_text}")