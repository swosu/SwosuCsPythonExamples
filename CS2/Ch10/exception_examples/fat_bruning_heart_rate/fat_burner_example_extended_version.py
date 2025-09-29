class AgeError(Exception):
    """Custom exception for invalid ages."""
    pass


def get_age():
    """Prompt user for age and validate range."""
    try:
        age = int(input("Enter age: "))
    except ValueError:
        # This happens if user types 'dog'
        raise AgeError("Age must be a number.")

    if age < 18 or age > 75:
        raise AgeError("Invalid age.")

    return age


def fat_burning_heart_rate(age):
    """Calculate fat-burning heart rate."""
    return (220 - age) * 0.70


if __name__ == "__main__":
    try:
        age = get_age()
    except AgeError as e:
        print(e)
        print("Could not calculate heart rate info.")
    else:
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm")
    finally:
        print("Program finished. Thank you for using the heart rate calculator.")
