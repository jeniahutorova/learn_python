print("Welcome to the rollecoster!")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("You can ride a rollercoster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Your ticket will be £5")
        bill = 5
    elif age <= 18:
        print("Your ticket will be £7")
        bill = 7
    elif 45 <= age <= 55:
        print("Your ticket will be free!")
    else:
        print("Your ticket will be £12")
        bill = 12
    photo = input("Do you want to add a printed photo? Y/N ")
    if photo == "Y" :
        bill+= 3
        print(f"Your final bill is {bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")