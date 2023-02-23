############### Blackjack Project #####################
from art import logo
import random
import os

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The computer is the dealer.
##################### Hints #####################

# function to draw a card and add it to the passed list
user_cards = []
house_cards = []


def deal_card(list_name):
    """Function takes a list and append a random card to it from the deck"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    list_name.append(random.choice(deck))


# function to get the score for players
def get_score(list_name):
    """Function takes a list and returns the sum of the list items"""
    score = sum(list_name)
    # check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score.
    if score == 21 and len(list_name) == 2:
        return 0
    # check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1
    elif score > 21 and 11 in list_name:
        list_name.remove(11)
        list_name.append(1)
        return sum(list_name)
    else:
        return sum(list_name)


# lists for holding players cards and game over flag

# Function to display players hands/cards
def present_cards():
    print(f"Your cards: {user_cards}, current score: {get_score(user_cards)}")
    print(f"Computer's first card: {house_cards[0]}")


# Function to compare the scores and return the winner
def compare():
    """Function to compare players scores"""
    user_score = get_score(user_cards)
    house_score = get_score(house_cards)
    if user_score == house_score:
        print("it's a draw!")
    elif house_score == 0:
        print("house wins! with Black Jack!")
    elif user_score == 0:
        print("You wins!")
    elif user_score > 21:
        print("You went over, House Win!")
    elif house_score > 21:
        print("House went over, You Win!")
    elif user_score > house_score:
        print("You Win!")
    else:
        print("house wins! You lose!")


# main function to play the game
def play_game():
    is_game_over = False

    # deal cards
    for _ in range(2):
        deal_card(user_cards)
        deal_card(house_cards)

    # present them
    present_cards()

    while not is_game_over:
        # check current score for game over
        if get_score(user_cards) == 0 or get_score(house_cards) == 0 or get_score(user_cards) > 21:
            is_game_over = True
        else:
            # ask user if they want to get another card
            get_another_card = input("Do you want another card, type Y or N: ").lower()

            # while get_another_card == "y":
            if get_another_card == "y":
                deal_card(user_cards)
                present_cards()
            else:
                is_game_over = True

        # house turn to finish hand and draw all cards
        while get_score(house_cards) < 17 and get_score(house_cards) != 0:
            deal_card(house_cards)

        # print(f"Your final hand: {user_cards}, your final score: {get_score(user_cards)}")
        # print(f"House final hand: {house_cards}, house final score: {get_score(house_cards)}")
        if is_game_over == True:
          compare()


# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Black Jack? Y or N: ").lower() == "y":
    os.system('clear')
    print(logo)
    user_cards = []
    house_cards = []
    play_game()

