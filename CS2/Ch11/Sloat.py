import time
import sys

def get_age():
    age = int(input("Enter your age: "))
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age

def fat_burning_heart_rate(age):
    return 0.7 * (220 - age)

def animated_output(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

if __name__ == "__main__":
    try:
        animated_output("Welcome to the Fat Burning Heart Rate Calculator!", 0.03)
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        animated_output(f"Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm", 0.02)
    except ValueError as e:
        animated_output(str(e), 0.02)
        animated_output("Could not calculate heart rate info.", 0.02)

