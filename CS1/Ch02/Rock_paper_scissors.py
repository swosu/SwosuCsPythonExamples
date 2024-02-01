import tkinter as tk
import random

class NotRockPaperScissorsGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("not rock paper scissors")
        self.round_num = 1
        self.user_score = 0
        self.opponent_score = 0

        # Title Screen
        tk.Label(self.window, text="not rock paper scissors").pack()
        start_button = tk.Button(self.window, text="trats", command=self.show_second_screen)
        start_button.pack()

    def show_second_screen(self):
        self.clear_screen()
        tk.Label(self.window, text="Enter your name:").pack()
        self.user_name_entry = tk.Entry(self.window)
        self.user_name_entry.pack()
        tk.Button(self.window, text="Submit", command=self.show_third_screen).pack()

    def show_third_screen(self):
        user_name = self.user_name_entry.get()
        self.clear_screen()
        tk.Label(self.window, text=f"Round {self.round_num}").pack()

        attacks = ["Spitball", "Glare", "Kick", "Finger Gun", "Flashlight"]
        user_attack = self.get_user_attack(attacks)
        opponent_attack = random.choice(attacks)

        result = self.determine_winner(user_attack, opponent_attack)
        tk.Label(self.window, text=f"{user_name} chose {user_attack}").pack()
        tk.Label(self.window, text=f"Opponent chose {opponent_attack}").pack()
        tk.Label(self.window, text=result).pack()

        if result != "It's a tie!":
            if result == f"{user_name} wins!":
                self.user_score += 1
            else:
                self.opponent_score += 1

        if self.round_num < 5:
            self.round_num += 1
            tk.Button(self.window, text="Continue", command=self.show_third_screen).pack()
        else:
            self.show_last_screen()

    def determine_winner(self, user_attack, opponent_attack):
        interactions = {
            "Spitball": ["Glare", "Flashlight"],
            "Kick": ["Spitball", "Flashlight"],
            "Glare": ["Kick", "Finger Gun"],
            "Finger Gun": ["Spitball", "Glare"],
            "Flashlight": ["Finger Gun", "Glare"]
        }

        if user_attack == opponent_attack:
            return "It's a tie!"

        if opponent_attack in interactions[user_attack]:
            return f"{self.user_name_entry.get()} wins!"
        else:
            return "Opponent wins!"

    def show_last_screen(self):
        self.clear_screen()
        tk.Label(self.window, text="Game Over!").pack()
        tk.Label(self.window, text=f"{self.user_name_entry.get()}: {self.user_score}").pack()
        tk.Label(self.window, text=f"Opponent: {self.opponent_score}").pack()
        tk.Label(self.window, text="Thanks for playing!").pack()

    def get_user_attack(self, attacks):
        attack_window = tk.Toplevel(self.window)
        attack_window.title("Choose Your Attack")

        user_attack = tk.StringVar()
        user_attack.set(attacks[0])

        for attack in attacks:
            tk.Radiobutton(attack_window, text=attack, variable=user_attack, value=attack).pack()

        tk.Button(attack_window, text="Submit", command=attack_window.destroy).pack()
        attack_window.wait_window()

        return user_attack.get()

    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    game = NotRockPaperScissorsGame()
    game.window.mainloop()
