# Blackjack
import random


def intro(play):
    while play is True:
        read_rules = input("Read the rules? ('y' or 'n') ")
        if read_rules == 'y' or read_rules == 'n':
            if read_rules == 'y':
                print("R U L E S")
                play = False
            else:
                play = False
        else:
            print("Sorry, that is not valid.")


# Starting funds for user and dealer.
def initial_fund():
    user_fund = 2000
    dealer_fund = 2000
    return user_fund, dealer_fund


# Get bet from user and dealer.
def get_bet(user_fund, dealer_fund):
    user_bet = 0
    dealer_bet = 0

    for i in range(0, 2):
        bet_check = False
        while bet_check is False:
            try:
                if i == 0:
                    print(f"\nYou currently have ${user_fund}.")
                    if user_fund < 50:
                        print("Unfortunately your funds are less than $50.")
                        quit()
                    elif 50 < user_fund < 400:
                        print(f"You can bet between $50 - ${user_fund}.")
                        user_bet = int(input(f"Bet $50 - ${user_fund}: "))
                        if user_bet > user_fund:
                            print(f"Sorry, your bet is ${user_bet - user_fund} short. Max bet is ${user_fund}.")
                        elif user_bet < 50:
                            print(f"Minimum bet is $50.")
                        else:
                            print(f"You bet ${user_bet}")
                            bet_check = True
                    else:
                        print(f"You can bet between $50 - $400.")
                        user_bet = input("Bet ($50 - $400): ")
                        if 50 > int(user_bet) or int(user_bet) > 400:
                            print("Sorry, this bet is not within the range of $50 - $400.")
                        else:
                            print(f"You bet ${user_bet}")
                            bet_check = True
                else:
                    print(f"\nThe dealer currently has ${dealer_fund}.")
                    print(f"Dealer bet ${dealer_bet}")
                    bet_check = True
            except ValueError:
                print("Sorry, you have entered an invalid key.")
    return user_bet, dealer_bet


# Create and shuffle cards, cut random amount ranging from 20 - 24 cards.
def shuffle_deck():
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
    random.shuffle(deck)

    print("\nThe dealer shuffles the deck, then lays the deck face-down in front of you.")
    input("Press enter to cut the deck...")
    cut_deck = deck[:(random.randrange(28, 32))]
    return cut_deck


# Deal phase, returns user and dealer hands
def initial_deal(cut_deck):
    user_hand = []
    dealer_hand = []

    print("\nThe dealer begins to hand out cards.")
    for i in range(0, 2):
        user_hand.append(cut_deck.pop())
        dealer_hand.append(cut_deck.pop())
    return user_hand, dealer_hand, cut_deck


# Assign card values.
def get_value(card, hand_value=[], turn=0):
    value = 0

    if turn == 0:
        if 11 <= card <= 13:
            value = 10
        if 1 < card <= 10:
            value = card
        if 1 == card:
            check = False
            while check is False:
                value = input("Please select a value for the Ace: ")
                if value == '1' or value == '10':
                    print(f"Ace is equal to {value}.")
                    check = True
                else:
                    print("Sorry, this value is not accepted.")
    if turn == 1:
        if 11 <= card <= 13:
            value = 10
        if 1 < card <= 10:
            value = card
        if 1 == card:
            if sum(hand_value) <= 11:
                value = 10
            else:
                value - 1
    return int(value)


# Dealer actions
# 1. Decide bet
# 2. Decide hit or stand
# 3.
def dealer(choice, dealer_value):
    if choice == 1:
        if sum(dealer_value) <= 16:
            print("The dealer will hit.")
        else:
            print("The dealer will stand.")


# Main game loop.
def game():
    print("\n****** B L A C K J A C K ******\n")
    play = True
    intro(play)
    user_fund, dealer_fund = initial_fund()

    while play is True:
        user_stand = 0
        dealer_stand = 0
        user_bet, dealer_bet = get_bet(user_fund, dealer_fund)
        user_hand, dealer_hand, deck = initial_deal(shuffle_deck())
        user_bet = int(user_bet)
        dealer_bet = int(dealer_bet)

        misc = ['first', 'second', 'third', 'fourth', 'fifth']
        face_cards = ['Ace', 'Jack', 'Queen', 'King']
        user_value = []
        dealer_value = []

        bust = False
        reveal = False

        # Initial deal to user and dealer.
        for i in range(0, 2):
            if user_hand[i] == 1:
                input(f"\nThe {misc[i]} card is dealt. It is a {face_cards[0]}. Press enter to continue...")
                user_value.append(get_value(user_hand[i]))
            elif user_hand[i] == 11:
                user_value.append(get_value(user_hand[i]))
                input(f"\nThe {misc[i]} card is dealt. It is a {face_cards[1]}. Press enter to continue...")
            elif user_hand[i] == 12:
                user_value.append(get_value(user_hand[i]))
                input(f"\nThe {misc[i]} card is dealt. It is a {face_cards[2]}. Press enter to continue...")
            elif user_hand[i] == 13:
                user_value.append(get_value(user_hand[i]))
                input(f"\nThe {misc[i]} card is dealt. It is a {face_cards[3]}. Press enter to continue...")
            else:
                user_value.append(get_value(user_hand[i]))
                input(f"\nThe {misc[i]} card is dealt. It is a {user_hand[i]}. Press enter to continue...")
            dealer_value.append(get_value(dealer_hand[i], dealer_hand, 1))

        print(f"\nThe dealer has one card face-up, with a value of {dealer_value[0]}.")
        print("The dealer's face-down card is an unknown value.")
        print(f"\nYour current card value is: {sum(user_value[0:2])}")

# Phase two, hit or stand.
        while bust is False:
            while sum(user_value) < 21:
                while (user_stand < 2) and (dealer_stand < 2):
                    print("Now, will you hit or stand?")
                    hit_response = input("('h' or 's'):")

                    if hit_response == 'h':
                        user_hand.append(deck.pop())
                        if user_hand[-1] == 1:
                            print(f"\nYou drew an {face_cards[0]}")
                            user_value.append(get_value(user_hand[-1]))
                        elif user_hand[-1] == 11:
                            print(f"\nYou drew a {face_cards[1]}")
                            user_value.append(get_value(user_hand[-1]))
                        elif user_hand[-1] == 12:
                            print(f"\nYou drew a {face_cards[2]}")
                            user_value.append(get_value(user_hand[-1]))
                        elif user_hand[-1] == 13:
                            print(f"\nYou drew a {face_cards[3]}")
                            user_value.append(get_value(user_hand[-1]))
                        else:
                            print(f"You drew a {user_hand[-1]}")
                            user_value.append(get_value(user_hand[-1]))
                        if sum(user_value) > 21:
                            bust = True
                            break
                        print(f"Your new card value is {sum(user_value)}.\n")
                        if len(user_hand) == 3:
                            if reveal is False:
                                print(f"The dealer reveals their face-down card, value of {dealer_value[-1]}")
                                reveal = True
                    elif hit_response == 's':
                        print("You chose to stand.")
                        user_stand = user_stand + 1
                        if reveal is False:
                            print(f"The dealer reveals their face-down card, value of {dealer_value[-1]}")
                            reveal = True
                    else:
                        print("\nSorry, this response in invalid.\n")
                    if sum(dealer_value) < 17:
                        dealer_hand.append(deck.pop())
                        dealer_value.append(get_value(dealer_hand[-1], dealer_value, 1))
                        if dealer_hand[-1] == 1:
                            print(f"The dealer will hit. They draw a {face_cards[0]}")
                        elif dealer_hand[-1] == 11:
                            print(f"The dealer will hit. They draw a {face_cards[1]}")
                        elif dealer_hand[-1] == 12:
                            print(f"The dealer will hit. They draw a {face_cards[2]}")
                        elif dealer_hand[-1] == 13:
                            print(f"The dealer will hit. They draw a {face_cards[3]}")
                        else:
                            print(f"The dealer will hit. They draw a {dealer_hand[-1]}")
                    else:
                        print("The dealer will stand.")
                        dealer_stand = dealer_stand + 1
                    if sum(dealer_value) > 21:
                        bust = True
                        break

        if sum(user_value) > 21:
            print("You bust! Dealer wins...")
            user_fund -= user_bet
            print(f"You lost ${user_bet}. New balance is ${user_fund}.")
        if sum(dealer_value) > 21:
            print("Dealer busts! You win!!!")
            dealer_fund += dealer_bet
            print(f"You won ${dealer_bet}! New balance is ${user_fund}.")

        print(user_hand, user_value, dealer_hand, dealer_value)

        play_again = input("Would you like to play again? ('y' or 'n')")
        if play_again == 'n':
            play = False
        else:
            print("You chose to play again.")


# Game
game()

