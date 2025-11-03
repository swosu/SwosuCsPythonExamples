def get_age():
    try:
        age = int(input("Enter age: "))
    except ValueError as ve:
        raise ValueError("You must enter a valid integer for age. Please try again.") from ve
    if age < 18 or age > 75:
        raise ValueError("Invalid age. Age must be between 18 and 75.")
    return age

def fat_burning_heart_rate(age):
    return (220 - age) * 0.70

if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm")
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.")
    else:
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm")
    finally:
        print("Thank you for using the fat burning heart rate calculator.")
