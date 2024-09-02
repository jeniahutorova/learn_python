from art import logo
import random
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
game_over = False
your_cards = []
computer_cards = []
computer_current_score = -1
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

if start.lower() == 'y':
    print(logo)
    
    for _ in range(2):
        your_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not game_over:
        your_current_score = calculate_score(your_cards)
        computer_current_score = calculate_score(computer_cards)
        
        print(f"Your cards: {your_cards}, current score: {your_current_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if your_current_score == 0:
            print("Blackjack! You win!")
            game_over = True
        elif computer_current_score == 0:
            print(f"Computer has Blackjack with {computer_cards}! You lose!")
            game_over = True
        elif your_current_score > 21:
            print("You went over 21. You lose!")
            game_over = True
        else:
            go_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
            if go_or_pass.lower() == 'y':
                your_cards.append(deal_card())
            else:
                while computer_current_score < 17 and computer_current_score != 0:
                    computer_cards.append(deal_card())
                    computer_current_score = calculate_score(computer_cards)
                
                print(f"Your final hand: {your_cards}, final score: {your_current_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_current_score}")

                if computer_current_score > 21:
                    print("Computer went over 21. You win!")
                elif computer_current_score > your_current_score:
                    print("You lose!")
                elif computer_current_score == your_current_score:
                    print("It's a draw!")
                else:
                    print("You win!")
                
                game_over = True

elif start.lower() == 'n':
    print("Maybe next time!")
else:
    print("Sorry, you entered an invalid input. Please restart the game.")