import random   
import os 


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes in a list of cards and calculates a score of the cards then returns this value."""
    if sum(cards) == 21 and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "you lose!"
    elif user_score == 0:
        print(f"You win with a score of {user_score}!")
    elif user_score > 21:
        print(f"Bust! You got {user_score}.")
    elif computer_score > 21:
        print(f"computer went over with {computer_score}, you win!")
    elif user_score > computer_score:
        print(f"you win! Your score is {user_score} and the computer got {computer_score}. ")
    else: return (f"you loose! Your score is {user_score} and the computer got {computer_score}. ")


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your Cards are  {user_cards} and your score is {user_score}.")
        print(f" Computers first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_should_deal = input("Would you like to draw another card? (y/n): ") 
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score  !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(compare(user_score, computer_score))

while input("do you want to play a game of black jack? (y/n): ") == "y":
    os.system('cls')
    play_game()

