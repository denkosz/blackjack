import logo
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(a):
    if 11 in a and 10 in a and len(a) == 2:
        return 0
    if 11 in a and sum(a) > 21:
        a.remove(11)
        a.append(1)
    return sum(a)

def compare(a, b):
    if a == b:
        return "Its a draw! "
    elif b == 0:
        return "Computer won, User  lost"
    elif a == 0:
        return "User won, Computer  lost"
    elif a > 21:
        return "You went over. User lost"
    elif b > 21:
        return "Computer lost"
    elif a > b:
        return "You win"
    else:
        return "You lose"

def game_start():
    print(logo.logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer card: {computer_cards[0]}, current score: {computer_score}")

        if 0 == user_score or 0 == computer_score or user_score > 21:
            print("Game over")
            game_over = True
        else:
            x = input("Type 'y' if you want another card, type 'n' to pass:")
            if x == "y":
             user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}  ")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}  ")
    print(compare(user_score, computer_score))

game_start()

while input("Do you want to play again? type 'y' or 'n' for pass ! ") == "y":
    game_start()

