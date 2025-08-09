import random

# Initial set up the constants for the game
# Suits and Ranks of the cards
SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Create a rank value for scoring
RANK_VALUE = {
    "Ace": 1,
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 0, "Jack": 0, "Queen": 0, "King": 0,
}

# Create a deck and random cards
def build_shuffled_deck():
    deck = [(s, r) for s in SUITS for r in RANKS]
    random.shuffle(deck)
    return deck

# Sum the values of the ranks in the hand and take modulo 10 (to get the last digit)
def score(hand):
    return sum(RANK_VALUE[r] for _, r in hand) % 10

# Format the hand for display
def card_format(hand):
    return ", ".join(f"{s}-{r}" for s, r in hand)

# Ask the user for a bet amount (should be a positive integer)
def ask_bet():
    while True:
        raw = input("> Please put your bet\n> ").strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("> Invalid bet. Enter a positive integer.")

# Ask the user if they want to play again
def ask_yes_no(prompt):
    while True:
        ans = input(f"> {prompt} (Yes/No)?\n> ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("> Please answer Yes or No.")

# Main function
def main():
    print("> npm start")  # To make it consistent with the given context, 
                          # actually it is not needed for python.
    chips = 0

    while True:
        bet = ask_bet()

        deck = build_shuffled_deck()
        player = [deck[0], deck[1]]               # player gets first two cards
        dealer = [deck[-2], deck[-1]]             # dealer gets last two cards

        ## For testing "Tie case", please uncomment the following lines
        # player = [("Clubs", "4"), ("Hearts", "3")]
        # dealer = [("Spades", "Ace"), ("Diamonds", "6")]

        print(f"> You got {card_format(player)}")
        print(f"> The dealer got {card_format(dealer)}")

        player_score, dealer_score = score(player), score(dealer)

        if player_score > dealer_score:
            chips += bet
            print(f"> You won!!!, received {bet} chips")
        elif player_score < dealer_score:
            chips -= bet
            print(f"> You lost..., paid {bet} chips")
        else:
            print("> Tie, no chips exchanged")

        if not ask_yes_no("Wanna play more"):
            break

    print(f"> You got total {chips} chips")

if __name__ == "__main__":
    main()
