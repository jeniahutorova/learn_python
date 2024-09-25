#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Read all the starting letters
with open(r"day_20\name-merge-project\Input\Letters\starting_letters.txt") as letter_file:
    letter_template = letter_file.read()

# Read all names
with open(r"day_20\name-merge-project\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines()

# For all names extract \n and change [name] in starting letters for new correct name
for name in names:
    new_name = name.strip("\n")
    personalized_letter = letter_template.replace("[name]", new_name)

    with open(rf"day_20\name-merge-project\Output\ReadyToSend\letter_for_{new_name}", mode="w") as completed_letters_file:
        completed_letters_file.write(personalized_letter)