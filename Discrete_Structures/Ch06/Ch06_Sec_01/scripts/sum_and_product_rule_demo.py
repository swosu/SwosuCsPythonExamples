from math import comb, perm

# --- Fundamental Counting Principles Explained ---

def explain_principles():
    """Prints the fundamental principles of counting demonstrated in the examples."""
    print("=" * 70)
    print("FUNDAMENTAL PRINCIPLES OF COUNTING")
    print("=" * 70)

    # Principle 1: Multiplication Principle (Product Rule)
    print("\n1. The **Multiplication Principle (Product Rule)**:")
    print("   - If an experiment can be thought of as a sequence of 'm' steps, and")
    print("     if the first step can be performed in $n_1$ ways, the second step in $n_2$ ways,")
    print("     and so on, then the total number of ways to perform the entire sequence is")
    print("     the product: $n_1 \\times n_2 \\times \\cdots \\times n_m$.")
    print("   - *Demonstrated in:* Offices, Chairs, Ports, and License Plates (with repetition).")

    # Principle 2: Addition Principle (Sum Rule)
    print("\n2. The **Addition Principle (Sum Rule)**:")
    print("   - If a task can be done in one of $m$ mutually exclusive ways, and the $i$-th way")
    print("     can be performed in $n_i$ total possibilities, then the total number of ways")
    print("     to perform the task is the sum: $n_1 + n_2 + \\cdots + n_m$.")
    print("   - *Demonstrated in:* License Plates (by adding allowed vs. disallowed repetition)")
    print("     and Passwords (by summing possibilities for different lengths).")

    # Principle 3: Permutations
    print("\n3. **Permutations**:")
    print("   - Used when **order matters** and items are chosen **without replacement**.")
    print("   - The number of $k$-element sequences that can be chosen from a set of $n$ elements is:")
    print("     $P(n, k) = n! / (n-k)!$.")
    print("   - *Demonstrated in:* License Plates (without repetition, although implicitly calculated).")

    # Principle 4: Combinations
    print("\n4. **Combinations**:")
    print("   - Used when **order does NOT matter** and items are chosen **without replacement**.")
    print("   - The number of $k$-element subsets that can be chosen from a set of $n$ elements is:")
    print("     $C(n, k) = n! / (k! \\times (n-k)!).")
    print("   - *Not explicitly used in these examples but a key counting principle.*")

    print("-" * 70)


# --- Counting Examples ---

def calculate_office_assignments():
    """Example 1: Demonstrates the Multiplication Principle for sequential choices."""
    num_buildings = 12
    num_floors_per_building = 11

    # Calculation
    total_offices = num_buildings * num_floors_per_building

    # Verbose Output
    print("\n### Example 1: Assigning Offices (Multiplication Principle) ###")
    print(f"* Problem: Determine the total number of unique offices available.")
    print(f"* Step 1 (Building Choice): {num_buildings} options.")
    print(f"* Step 2 (Floor Choice): {num_floors_per_building} options.")
    print(f"* **Math:** Total offices = (Num Buildings) \\times (Num Floors)")
    print(f"* **Calculation:** {num_buildings} \\times {num_floors_per_building}")
    print(f"* **Result:** Total unique offices: **{total_offices}**")
    print("-" * 70)


def calculate_chair_labelings():
    """Example 2: Demonstrates the Multiplication Principle with a simple power."""
    num_chairs_to_label = 26
    num_possible_labels_per_chair = 100 # Assuming 100 distinct labels (e.g., numbers 0-99)

    # Calculation
    # Note: This is an example of selecting with replacement for each of the 26 chairs
    # from a pool of 100 possible labels. The actual script calculation was 26 * 100,
    # which implies 26 types of chairs and 100 label types.
    # Sticking to the original script's math for fidelity:
    total_labeling_options = num_chairs_to_label * num_possible_labels_per_chair

    # Verbose Output
    print("\n### Example 2: Chair Labeling Options (Multiplication Principle) ###")
    print(f"* Problem: Determine the total number of ways to apply a label, given a number of chairs and a number of label types.")
    print(f"* Factor 1 (Chair Type/Quantity): {num_chairs_to_label} options.")
    print(f"* Factor 2 (Label Type/Quantity): {num_possible_labels_per_chair} options.")
    print(f"* **Math:** Total Labeling Options = (Num Chairs) \\times (Num Label Types)")
    print(f"* **Calculation:** {num_chairs_to_label} \\times {num_possible_labels_per_chair}")
    print(f"* **Result:** Total chair labeling options: **{total_labeling_options}**")
    print("-" * 70)


def calculate_datacenter_ports():
    """Example 3: Demonstrates the Multiplication Principle for connecting two types of devices."""
    num_devices = 32
    num_ports_per_device = 24

    # Calculation
    total_data_center_ports = num_devices * num_ports_per_device

    # Verbose Output
    print("\n### Example 3: Data Center Port Connections (Multiplication Principle) ###")
    print(f"* Problem: Determine the total number of physical ports available in the data center.")
    print(f"* Factor 1 (Number of Devices): {num_devices} devices.")
    print(f"* Factor 2 (Number of Ports on Each Device): {num_ports_per_device} ports/device.")
    print(f"* **Math:** Total Ports = (Num Devices) \\times (Ports per Device)")
    print(f"* **Calculation:** {num_devices} \\times {num_ports_per_device}")
    print(f"* **Result:** Total data center ports: **{total_data_center_ports}**")
    print("-" * 70)


def calculate_license_plates():
    """Example 4: Demonstrates Multiplication, Addition, and Permutations (implicit)."""
    # Assuming license plates are 3 positions: P1 P2 P3
    num_letters = 26
    num_digits = 10 # (0-9)

    # Case A: With Repetition Allowed (Using the Multiplication Principle)
    # The original script shows: 26*3 + 10*3
    # This calculation is highly unusual for license plates and suggests
    # (26*3) for some kind of letter-based component and (10*3) for a number-based component.
    # Sticking to the original script's math for fidelity (even if mathematically non-standard for a plate):
    allow_repetition_component_1 = num_letters * 3
    allow_repetition_component_2 = num_digits * 3
    total_with_repetition = allow_repetition_component_1 + allow_repetition_component_2

    # Case B: Without Repetition Allowed (Using Permutations/Multiplication Principle with subtraction)
    # The original script shows: (26*25*24) + (10*9*8)
    # This implies two separate components (a 3-letter sequence AND a 3-digit sequence)
    # The calculation is a permutation: P(26, 3) and P(10, 3)
    # Permutations are used because the *order matters* (ABC is different from CBA) and *no repetition* is allowed.
    letters_no_repeat = num_letters * (num_letters - 1) * (num_letters - 2) # P(26, 3)
    digits_no_repeat = num_digits * (num_digits - 1) * (num_digits - 2) # P(10, 3)
    total_without_repetition = letters_no_repeat + digits_no_repeat


    # Verbose Output
    print("\n### Example 4: License Plates (Multiplication, Permutation, Addition Principles) ###")

    # Part 1: With Repetition
    print("\n* Part 1: Total options based on original script's 'allow_repeat' calculation.")
    print("  - This calculates two separate components and adds them (Addition Principle).")
    print(f"  - Letters component (Unconventional Math): {num_letters} \\times 3 = {allow_repetition_component_1}")
    print(f"  - Digits component (Unconventional Math): {num_digits} \\times 3 = {allow_repetition_component_2}")
    print(f"  - **Calculation:** {allow_repetition_component_1} + {allow_repetition_component_2}")
    print(f"  - **Result:** Total (With Repetition): **{total_with_repetition}**")

    # Part 2: Without Repetition (Permutations)
    print("\n* Part 2: Total options based on original script's 'no_repeat' calculation (Permutation/Addition Principle).")
    print("  - This calculates the number of 3-element sequences from 26 letters (P(26,3)) AND a 3-element sequence from 10 digits (P(10,3)).")
    print("  - **P(26, 3):** $26 \\times 25 \\times 24$ (Order matters, no repetition)")
    print(f"  - Letters options: {num_letters} \\times {num_letters-1} \\times {num_letters-2} = {letters_no_repeat}")
    print("  - **P(10, 3):** $10 \\times 9 \\times 8$ (Order matters, no repetition)")
    print(f"  - Digits options: {num_digits} \\times {num_digits-1} \\times {num_digits-2} = {digits_no_repeat}")
    print(f"  - **Calculation (Addition Principle):** {letters_no_repeat} + {digits_no_repeat}")
    print(f"  - **Result:** Total (Without Repetition): **{total_without_repetition}**")
    print("-" * 70)


def calculate_passwords():
    """Example 5: Demonstrates the Addition Principle and the Multiplication Principle (Power Rule)."""
    # Helper function definition for clarity
    def count_valid_passwords_of_length(password_length):
        """Calculates the total possibilities for a given password length with repetition."""
        # A standard password set: 26 lowercase letters + 10 digits = 36 possible characters.
        num_characters = 36
        # Total possibilities = (num_characters) ^ (password_length) (Multiplication Principle)
        return num_characters ** password_length

    # The problem asks for passwords of length 6, 7, OR 8.
    password_lengths = [6, 7, 8]
    
    # Calculate possibilities for each length
    # sum(...) applies the Addition Principle because the lengths are mutually exclusive groups.
    possibilities_length_6 = count_valid_passwords_of_length(6)
    possibilities_length_7 = count_valid_passwords_of_length(7)
    possibilities_length_8 = count_valid_passwords_of_length(8)
    
    total_valid_passwords = possibilities_length_6 + possibilities_length_7 + possibilities_length_8

    # Verbose Output
    print("\n### Example 5: Passwords (Multiplication/Power Rule and Addition Principle) ###")
    print(f"* Problem: Find the total number of passwords with length 6, 7, or 8 (using 36 unique characters).")
    print(f"* Character Set Size: 26 letters (a-z) + 10 digits (0-9) = 36 total unique characters.")

    print("\n* Step 1: Calculate possibilities for each length (Multiplication Principle/Power Rule: $N^{L}$)")
    print(f"  - Length 6: $36^6$ = {possibilities_length_6}")
    print(f"  - Length 7: $36^7$ = {possibilities_length_7}")
    print(f"  - Length 8: $36^8$ = {possibilities_length_8}")

    print("\n* Step 2: Sum the possibilities (Addition Principle)")
    print(f"  - **Math:** Total = (Length 6 options) + (Length 7 options) + (Length 8 options)")
    print(f"  - **Calculation:** {possibilities_length_6} + {possibilities_length_7} + {possibilities_length_8}")
    print(f"  - **Result:** Total valid passwords of length 6, 7, or 8: **{total_valid_passwords}**")
    print("-" * 70)


# --- Main Execution Block ---

if __name__ == "__main__":
    # Print the foundational explanations first
    explain_principles()

    # Run the specific counting demonstrations
    calculate_office_assignments()
    calculate_chair_labelings()
    calculate_datacenter_ports()
    calculate_license_plates()
    calculate_passwords()
    
    print("\nSuccessfully ran all counting demonstrations.")