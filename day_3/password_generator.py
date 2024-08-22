import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("Welcome tp the PyPassword Generator!\nHow many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols?\n"))
nr_numbers = int(input("How many numbers?\n"))

password = ""

for letter in range(0, nr_letters + 1):
    password += random.choice(letters)

for symbol in range(0, nr_symbols + 1):
    password+= random.choice(symbols)

for number in range(0, nr_numbers + 1):
    password+= random.choice(numbers)

password_list = list(password)
random.shuffle(password_list)
random_password = ''.join(password_list)
print(random_password)

