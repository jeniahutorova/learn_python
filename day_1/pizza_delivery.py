print("Welcome to Python Pizza delivery!")
bill = 0
size = input("What size pizza do you want? S, M or L: ")
pepperoni =  input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == "S":
    bill = 10
elif size == "M": 
    bill = 15
elif size == "L":
    bill = 20
else:
    print("You've printed wrong inputs")

if pepperoni == "Y":
    if size == "S":
        bill+= 2
    else:
        bill+= 3
else:
    print("You've printed wrong inputs")


if extra_cheese == "Y":
    bill+= 1
print(f"Your bill is £{bill}")



