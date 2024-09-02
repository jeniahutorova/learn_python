alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *=-1
            
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            original_index = (index + shift_amount) % len(alphabet)
            output_text += alphabet[original_index]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result:\n{output_text}")

game_over = False

while not game_over:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)
    
    continue_game = input("Would you like to go again? Type 'yes' or 'no'\n").lower()
    if continue_game == "no":
        game_over = True
        print("Game is over!")