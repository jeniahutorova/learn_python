from art import logo
import random
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
game_over = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []

if start.lower() == 'y':
    print(logo)
    while len(your_cards) < 2:
        your_cards.append(random.choice(cards))
    
    while len(computer_cards) < 2:
        computer_cards.append(random.choice(cards))
    
    while not game_over:
        
        your_current_score = sum(your_cards)
        computer_current_score = sum(computer_cards)

        print(f"Your cards: {your_cards}, current score: {your_current_score}")
        print(f"Computers's first card: {computer_cards[0]}")
        
        if your_current_score > 21:
            print("You went over 21. You lose!")
            game_over = True
        elif your_current_score == 21:
            print("You hit 21! You win!")
        else:
            go_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
            if go_or_pass.lower() == "y":
               your_cards.append(random.choice(cards))
            else:
                while computer_current_score < 17:
                    computer_cards.append(random.choice(cards))
                
                print(f"Your final hand: {your_cards}, final score: {your_current_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_current_score}")

                if computer_current_score > 21:
                    print("Computer went over 21. You win!")
                    game_over = True
                elif computer_current_score == 21:
                    print("Computer hit 21! You lose!")
                elif computer_current_score < your_current_score:
                    print("You win!")
                else:
                    print("It's a draw!")
                game_over = True
elif start.lower() == 'n':
    game_over = True
else:
    print("Sorry, you add an ivalid input. Try again!")
    game_over = True
