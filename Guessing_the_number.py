import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
def check_answer(guessed_number, answer,attempts):
    if(guessed_number < answer):
        print("Your guess is too low")
        attempts = attempts - 1
        return attempts
    elif guessed_number > answer:
        print('Your guess is too high')
        attempts = attempts - 1
        return attempts
    else:
        print("Your guess is correct\nYOU WIN")
def game():
    print("let me think of a number between 1 to 50.")
    answer = random.randint(1,50)
    print(answer)
    level = input("Choose the level either 'hard' or 'easy' : ")
    attempts = set_difficulty(level)
    guessed_number = 0
    while guessed_number != answer:
        print(f"You have {attempts} remaining to guess the number.")
        guessed_number = int(input("Guess a number : "))
        attempts = check_answer(guessed_number,answer,attempts)
        if attempts == 0:
            print('You are out of guesses\nYou lose')
            return
        if guessed_number != answer:
            print('Guess Again')
game()