import random
from art import logo
from art import vs
print(logo)
game_over = False
contestants = {
    'Cristiano Ronaldo, a Footballer from Portugal': '628',
    'Lionel Messi, a Footballer from Argentina': '502',
    'Selena Gomez, a Musician and Actress from US': '429',
    'Kylie Jenner, an Entrepreneur and Media Personality from US': '400',
    'Dwayne "The Rock" Johnson, an Actor from US': '397',
    'Ariana Grande, a Musician from US': '379',
    'Kim Kardashian, a Media Personality from US': '363',
    'Beyoncé, a Musician from US': '319',
    'Justin Bieber, a Musician from Canada': '292',
    'Taylor Swift, a Musician from US': '283',
}
score = 0
while not game_over:
# Randomly select two contestants
    contestant_1 = random.choice(list(contestants.keys()))
    contestant_2 = random.choice(list(contestants.keys()))

    #Ensure two contestants are different
    while contestant_1 == contestant_2:
        contestant_2 = random.choice(list(contestants.keys()))

    #Print the contestants
    print(f"Compare A: {contestant_1}")
    print(vs)
    print(f"Against B: {contestant_2}")

    #Users guess
    guess = input("Who has more followers? Type 'A' or 'B': ")

    #Contestants followers
    followers_1 = int(contestants[contestant_1])
    followers_2 = int(contestants[contestant_2])
    
    #Mark the correct answer
    if followers_1 > followers_2:
            correct_answer =  'a'
    else:
            correct_answer = 'b'

    #  Check if the user's guess is correct 
    if guess == correct_answer:
        score += 1
        print(f"You're right! Your current score is {score}.")
    else:
        print(f"You're wrong! The correct answer was {'A' if correct_answer == 'a' else 'B'}. Your score is {score}.")
        game_over = True