import random
rock = "🪨"
paper = "📄"
scissors = "✂️"
game_images = [rock,paper,scissors]
user_choice= int(input("Enter your choice\nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors :  "))
if(user_choice>=3 or user_choice<0):
    print("You entered invalid input, Please check")
else:
    print(f"User choice is : {game_images[user_choice]}")
    computer_choice = random.randint(0, 2)
    print(f"Computer choice is : {game_images[computer_choice]}")
    if (computer_choice == user_choice):
        print("It's a draw")
    elif (computer_choice == 2 and user_choice == 0):
        print("You win")
    elif (computer_choice == 0 and user_choice == 2):
        print("You lose")
    elif (computer_choice > user_choice):
        print("You lose")
    elif (user_choice > computer_choice):
        print("You win")
