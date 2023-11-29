def print_name(*names):
    # Capitalize the first letter of each name
    capitalized_names = [name.capitalize() for name in names]

    # Combine the names with spaces
    full_name = " ".join(capitalized_names)

    # Return the full name
    return full_name