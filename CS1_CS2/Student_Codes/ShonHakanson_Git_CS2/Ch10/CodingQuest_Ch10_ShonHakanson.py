import time

def riddle_round(question, answer, penalty_wrong=5, penalty_error=10):
    """Handles one riddle round with both wrong and error penalties."""
    try:
        guess = input(f"\n{question}\nEnter your answer (digits only): ")
        num = int(guess)  # Raises ValueError if not a number

        if num == answer:
            print("✅ Correct! Wire snipped safely.")
            return 0
        else:
            print(f"❌ Wrong number! Time penalty: -{penalty_wrong}s")
            return penalty_wrong

    except ValueError:
        print(f"⚠️ Invalid input (not a number)! Time penalty: -{penalty_error}s")
        return penalty_error


def bomb_defusal():
    timer = 40  # total time allowed
    start = time.time()

    print("💣 You’ve found a ticking bomb with two wires!")
    print(f"You have {timer} seconds to solve both riddles.\n")

    # Riddle 1
    penalties = 0
    penalties += riddle_round(
        "Riddle 1: I am an odd number. Take away one letter and I become even. What number am I?",
        answer=7
    )

    # Riddle 2
    penalties += riddle_round(
        "Riddle 2: I am a three-digit number. My tens digit is five more than my ones digit. "
        "My hundreds digit is eight less than my tens digit. What number am I?",
        answer=194
    )

    elapsed = int(time.time() - start)
    remaining = timer - elapsed - penalties

    if remaining > 0:
        print(f"\n🎉 Bomb defused with {remaining} seconds left!")
    else:
        print("\n💀 BOOM! You ran out of time…")


if __name__ == "__main__":
    bomb_defusal()
