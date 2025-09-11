import random

class Card:
    suit_icons = {
        "Hearts": "♥",
        "Diamonds": "♦",
        "Clubs": "♣",
        "Spades": "♠"
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return f"{self.rank}{self.suit_icons[self.suit]}"

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["3", "4", "5", "6", "7", "8", "9", "10",
             "J", "Q", "K", "A", "2"]  # President ranks
    
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, num_players):
        """Deal cards fairly to all players"""
        hands = [[] for _ in range(num_players)]
        for i, card in enumerate(self.cards):
            hands[i % num_players].append(card)
        return hands


# --- Ask the user how many players ---
while True:
    try:
        num_players = int(input("How many players? "))
        if num_players < 2:
            print("You need at least 2 players.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Create and deal deck
deck = Deck()
deck.shuffle()
hands = deck.deal(num_players)

# Define rank order for sorting
rank_order = {rank: i for i, rank in enumerate(Deck.ranks)}

# Sort each player's hand
for hand in hands:
    hand.sort(key=lambda card: rank_order[card.rank])

# Print hands (for debugging)
for i, hand in enumerate(hands, start=1):
    print(f"\nPlayer {i}'s hand:")
    print(hand)

# Randomly choose starter (can be replaced with "3 of Clubs" rule)
current_player = random.randint(0, num_players - 1)
print(f"\nPlayer {current_player + 1} will go first!")


# --- Game State ---
pile = []               # cards on the table this trick
last_play = None        # rank of last play
passes = [False] * num_players
active_players = num_players


def all_passed_except_one():
    """Check if all but one player has passed."""
    return passes.count(False) == 1 and last_play is not None


# --- Main game loop ---
while active_players > 1:
    if not hands[current_player]:  # Skip if no cards left
        current_player = (current_player + 1) % num_players
        continue

    print(f"\n--- Player {current_player + 1}'s turn ---")
    print("Your hand:", hands[current_player])
    print("Current pile:", pile if pile else "empty")
    print("Last play:", last_play if last_play else "None")

    choice = input("Play cards (rank, e.g. '7') or 'pass': ").strip()

    if choice.lower() == "pass":
        passes[current_player] = True
        print(f"Player {current_player + 1} passes.")
    else:
        # Gather all cards of chosen rank
        chosen_cards = [c for c in hands[current_player] if c.rank == choice]

        if not chosen_cards:
            print("Invalid rank. You pass by default.")
            passes[current_player] = True
        else:
            # Validate play
            if last_play is None or rank_order[choice] >= rank_order[last_play]:
                # Play valid
                hands[current_player] = [c for c in hands[current_player] if c.rank != choice]
                pile = chosen_cards
                last_play = choice
                passes = [False] * num_players  # reset passes
                print(f"Player {current_player + 1} plays {pile}")
                if not hands[current_player]:
                    print(f"Player {current_player + 1} is OUT!")
                    active_players -= 1
            else:
                print("Play too low. You pass instead.")
                passes[current_player] = True

    # If all but one passed → trick ends
    if all_passed_except_one():
        winner = [i for i, p in enumerate(passes) if not p][0]
        print(f"\nTrick ends! Player {winner + 1} wins and starts next trick.")
        pile = []
        last_play = None
        passes = [False] * num_players
        current_player = winner
        continue

    # Next player's turn
    current_player = (current_player + 1) % num_players

print("\nGame over!")
for i, hand in enumerate(hands, start=1):
    if hand:
        print(f"Player {i} loses with remaining cards: {hand}")
    else:
        print(f"Player {i} is out!")
