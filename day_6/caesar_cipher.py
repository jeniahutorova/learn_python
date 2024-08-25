alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
direction = input("Type 'encode' to encript and 'decode' to decrypt\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            original_index = alphabet.index(letter)
            new_index = (original_index + shift) % len(alphabet)
            encrypted_text+= alphabet[new_index]
        else:
            encrypted_text_text += letter
    return encrypted_text    

if direction == "encode":
        encripted_message = encrypt(text, shift)
        print(f"Encoded message is:\n{encripted_message}")

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
         if letter in alphabet:
            index = alphabet.index(letter)
            original_index = (index - shift) % len(alphabet)
            decrypted_text+= alphabet[original_index]
    return decrypted_text
if direction == "decode":
     decoded_message = decrypt(text, shift)
     print(f"Decoded message is:\n{decoded_message}")

def caesar(direction, text, shift):
     