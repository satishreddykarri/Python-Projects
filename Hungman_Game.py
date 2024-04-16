import random
import Hungman_stages
word_list = ['apple','banana','potato']
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for letter in chosen_word:
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter : ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"you have only {lives} chances left")
        if lives == 0:
            game_over = True
            print("You Lose!!!")
    if '_' not in display:
        game_over = True
        print("You winn!!!")
    print(Hungman_stages.stages[lives])
