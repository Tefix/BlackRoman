import random

def draw_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

def calculate_total(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def display_hand(hand, name):
    """Displays the cards in the player's or dealer's hand."""
    print(f"{name}'s hand: {hand} (Total: {calculate_total(hand)})")

def blackjack_game():
    balance = 100  # Starting balance
    while balance > 0:
        print(f"\nYour current balance is: ${balance}")
        while True:
            try:
                bet = int(input("Enter your bet: "))
                if bet > balance:
                    print("You cannot bet more than your current balance.")
                elif bet <= 0:
                    print("Bet must be a positive amount.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        # Initial deal
        player_hand = [draw_card(), draw_card()]
        dealer_hand = [draw_card(), draw_card()]

        # Show hands
        display_hand(player_hand, "Player")
        print(f"Dealer's hand: [{dealer_hand[0]}, '?']")

        # Player's turn
        while True:
            if calculate_total(player_hand) > 21:
                print("Player busts! Dealer wins.")
                balance -= bet
                break
            move = input("Do you want to hit or stand? (h/s): ")
            if move.lower() == 'h':
                player_hand.append(draw_card())
                display_hand(player_hand, "Player")
            elif move.lower() == 's':
                break
            else:
                print("Invalid input. Please enter 'h' to hit or 's' to stand.")

        # Dealer's turn
        if calculate_total(player_hand) <= 21:
            display_hand(dealer_hand, "Dealer")
            while calculate_total(dealer_hand) < 17:
                dealer_hand.append(draw_card())
                display_hand(dealer_hand, "Dealer")
            dealer_total = calculate_total(dealer_hand)
            player_total = calculate_total(player_hand)
            if dealer_total > 21:
                print("Dealer busts! Player wins.")
                balance += bet
            elif dealer_total > player_total:
                print("Dealer wins.")
                balance -= bet
            elif dealer_total < player_total:
                print("Player wins.")
                balance += bet
            else:
                print("It's a tie!")

        if balance <= 0:
            print("You are out of money. Game over!")
            break

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print(f"You leave the game with a balance of ${balance}.")
            break

blackjack_game()
