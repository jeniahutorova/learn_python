import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty.\nType 'easy' or 'hard': ")
number = random.randint(1, 100)
game_over = False

if difficulty.lower() == 'easy':
    number_of_guesses = 10
else:
    number_of_guesses = 5

print(f"You have {number_of_guesses} attempts to guess a number.")
    
while not game_over:
    guess = int(input("Make a guess: "))

    if guess < number :
        print("Too low.\nGuess again.")
    elif guess > number:
        print("Too high.\nGuess again.")
    else:
        print("You win! Congratulations!!!")
        game_over = True

    number_of_guesses -= 1

    if number_of_guesses == 0 and not game_over:
        print("Sorry you are out of attempts. Try again!")
        game_over = True
    elif not game_over:
        print(f"You have {number_of_guesses} attempts remaining to guess the number.")
        