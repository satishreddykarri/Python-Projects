alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here is the message after encryption : {cipher_text}")
def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Here is the message after encryption : {plain_text}")
program_end = False
while not program_end:
    user_choice = input("Type 'encrypt' for encryption and 'decrypt' fot decryption : ")
    message = input("Enter your message : ").lower()
    shift = int(input("Enter the shift key : "))
    if user_choice == "encrypt":
        encryption(plain_text=message, shift_key=shift)
    elif user_choice == "decrypt":
        decryption(cipher_text = message,shift_key = shift)
    play_again = input("Type 'yes' to continue, type 'no' to exit : ")
    if play_again == 'no':
        program_end =True
        print("Enjoy your day!!")
