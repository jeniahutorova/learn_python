print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to the treasure island.")
print("Your mission is to find the treasure.")
cross_road = input("You're at the cross road. Where do you want to go?\n Type 'left' or 'right': ")
if cross_road == "left":
    action = input("You come to a lake.\nDo you want to swim or wait for a boat? Type 'swim' or 'wait': ")
    if action =="wait":
        choice = input("You arrive at a house with three doors.\nOne red, one yellow, and one blue. Which door do you want to open? Type 'red', 'yellow', or 'blue': ")
        if choice == "yellow":
            print("Congratulations! You won the game!")
        elif choice == "red":
            print("You've burnt by fire. Game over!")
        elif choice == "blue":
            print("You've eaten by beasts. Game over!")
        else:
            print("Game over!")
    else:
        print("You've been attacked by trout. Game over!")
else:
    print("You fell into a hole. Game over!")
