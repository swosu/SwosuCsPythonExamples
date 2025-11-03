class RockPaperScissorsGame:
    def __init__(self):
        self.rules = self.create_rules()
        self.choice_map = {1: "rock", 2: "paper", 3: "scissors"}  # Map integers to choices

    @staticmethod
    def create_rules():
        """
        Creates named dictionaries for each of Player 1's choices and a main dictionary to hold them.
        """
        # Dictionary for when Player 1 chooses "rock"
        player_1_rock = {
            "rock": "Rock meets rock. It's a tie!",
            "paper": "Paper covers rock. Player 2 wins!",
            "scissors": "Rock smashes scissors. Player 1 wins!",
        }

        # Dictionary for when Player 1 chooses "paper"
        player_1_paper = {
            "rock": "Paper covers rock. Player 1 wins!",
            "paper": "Paper meets paper. It's a tie!",
            "scissors": "Scissors cut paper. Player 2 wins!",
        }

        # Dictionary for when Player 1 chooses "scissors"
        player_1_scissors = {
            "rock": "Rock smashes scissors. Player 2 wins!",
            "paper": "Scissors cut paper. Player 1 wins!",
            "scissors": "Scissors meet scissors. It's a tie!",
        }

        # Combine named dictionaries into the main choice dictionary
        player_1_choice_dictionary = {
            "rock": player_1_rock,
            "paper": player_1_paper,
            "scissors": player_1_scissors,
        }

        return player_1_choice_dictionary

    def determine_winner(self, player1_choice, player2_choice):
        """
        Determines the winner based on the choices of Player 1 and Player 2.

        Args:
            player1_choice (str): The choice of Player 1.
            player2_choice (str): The choice of Player 2.

        Returns:
            str: A verbose message describing the result of the round.
        """
        try:
            return self.rules[player1_choice][player2_choice]
        except KeyError:
            raise ValueError("Invalid choice. Please choose 1, 2, or 3.")

    def play_round(self, player1_choice, player2_choice):
        """
        Simulates a single round of Rock-Paper-Scissors.

        Args:
            player1_choice (int): The numeric choice of Player 1.
            player2_choice (int): The numeric choice of Player 2.

        Returns:
            str: A message describing the outcome of the round.
        """
        try:
            player1_choice_name = self.choice_map[player1_choice]
            player2_choice_name = self.choice_map[player2_choice]
        except KeyError:
            raise ValueError("Invalid input. Please enter 1 for rock, 2 for paper, or 3 for scissors.")

        result = self.determine_winner(player1_choice_name, player2_choice_name)
        return f"Player 1 picked {player1_choice_name}, Player 2 picked {player2_choice_name}. {result}"

# Main program
def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("Enter 1 for Rock, 2 for Paper, or 3 for Scissors.")
    game = RockPaperScissorsGame()

    while True:
        print("\nEnter your choices (or type 'quit' to exit):")
        
        player1_input = input("Player 1: ")
        if player1_input.lower() == "quit":
            print("Goodbye!")
            break

        player2_input = input("Player 2: ")
        if player2_input.lower() == "quit":
            print("Goodbye!")
            break

        try:
            player1_choice = int(player1_input)
            player2_choice = int(player2_input)
            outcome_message = game.play_round(player1_choice, player2_choice)
            print(outcome_message)
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
