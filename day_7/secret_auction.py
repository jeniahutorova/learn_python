
game_over = False
group_of_biddes = {}

while not game_over:
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))

    group_of_biddes[name] = bid

    other_bid = input("Is there anyone else who wants to bid? Type 'yes' or 'no': ")
    if other_bid == "yes":
        print("\n" * 100)
    elif other_bid == "no":
        largest_number = 0 
        winner = ""
        for key in group_of_biddes:
            if group_of_biddes[key] > largest_number: 
                largest_number = group_of_biddes[key]
                winner = key
        game_over = True
    else:
        print("Sorry, you typed something wrong. Try again!")

print(f"Largest bid was £{largest_number} by {winner}")