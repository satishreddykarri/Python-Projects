import random
letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
numbers = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
symbols = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
        ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
    ]
print("Welcome to password Generator!!!")
n_letters = int(input("How many letters do you want in your password : "))
n_numbers = int(input("How many numbers do you want in your password : "))
n_symbols = int(input("How many symbols do you want in your password : "))
password = []
for i in range(1, n_letters+1):
    letter = random.choice(letters)
    password += letter
for i in range(1, n_numbers+1):
    number = random.choice(numbers)
    password += number
for i in range(1, n_symbols+1):
    symbol = random.choice(symbols)
    password += symbol
random.shuffle(password)
password_list = ""
for i in password:
    password_list += i
print(password_list)