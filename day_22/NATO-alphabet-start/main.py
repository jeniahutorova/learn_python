student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

letters_dict = pandas.read_csv(r"C:\Users\jenia\Desktop\learn_python\day_22\NATO-alphabet-start\nato_phonetic_alphabet.csv")
new_dictionary = { row.letter : row.code  for (index, row) in letters_dict.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()

phonetic_code_words = [new_dictionary[letter] for letter in user_input if letter in new_dictionary]

print(phonetic_code_words)
print(f"Enjoy your {phonetic_code_words}!")