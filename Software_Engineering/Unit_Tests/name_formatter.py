def print_name(first_name, last_name, middle_name=None):
    # Capitalize the first letter of the first name, middle name (if provided), and last name
    first_name = first_name.capitalize()
    if middle_name:
        middle_name = middle_name.capitalize()
    last_name = last_name.capitalize()

    # Combine the first name, middle name (if provided), and last name with a space
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    # Return the full name
    return full_name