# Caesar Cipher Implementation 
# Shift each letter by a user chosen amount in the alphabet
# Programmer: Shon Hakanson
# Mentor: Anton Kusik

alphabet_list = alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                            " ", ".", ",", "?"]

encrypt_input_word = input("Enter a word or phrase: ")
encrypt_input_word = encrypt_input_word.lower()
encrypt_input_list = list(encrypt_input_word)

print("1. Encrypt Word")
print("2. Decrypt Word")
choice = input("Choose an option (1 or 2): ")

# ---- NEW: Require Shift Amount ----
shift = int(input("Enter a shift amount (e.g., 1-26): "))

# ---------- ENCRYPTION ----------
if choice == "1":
    for index in range(len(encrypt_input_list)):
        character = encrypt_input_list[index]
        if character in alphabet_list:
            position = alphabet_list.index(character)
            new_position = (position + shift) % len(alphabet_list)  # Uses user shift
            encrypt_input_list[index] = alphabet_list[new_position]
        else:
            print(f"Character {character} not in alphabet list.")

    print("".join(encrypt_input_list))

# ---------- DECRYPTION ----------
elif choice == "2":
    for index in range(len(encrypt_input_list)):
        character = encrypt_input_list[index]
        if character in alphabet_list:
            original_position = alphabet_list.index(character)
            shifted_position = (original_position - shift) % len(alphabet_list)  # Uses user shift
            encrypt_input_list[index] = alphabet_list[shifted_position]
        else:
            print(f"Character {character} not in alphabet list.")

    print("".join(encrypt_input_list))
