import random
from hangman_words import words_list
from hangman_art import stages

chosen_word = random.choice(words_list)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
incorrect_guess = 0
max_attempts = 6

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You've already guessed the letter {guess}. Try again.")
    
    display = "" 
    for letter in chosen_word:
        if letter == guess:
            display+= letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print(f"Congratulations! You made it! The word is {display}")
        game_over = True

    if guess not in chosen_word:
        incorrect_guess += 1
        print("Your guess is wrong!" + stages[incorrect_guess])
    if incorrect_guess == max_attempts:
        print("Sorry! You reached maximum amounts of attempts. Game over!")
        game_over = True