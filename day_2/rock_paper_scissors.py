import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

your_choice = int(input("What do you choose?\n Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
choices = [rock, paper, scissors]
if your_choice not in [0, 1, 2]:
    print("You've printed a wrong number. Please start again!")
else:
    print(choices[your_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(choices[computer_choice])

if your_choice == 0 and computer_choice == 2 or your_choice == 2 and computer_choice == 1 or your_choice == 1 and computer_choice == 0:
    print("You win!")
elif your_choice == computer_choice:
    print("It's a draw!")
else:
    print("You lose!")