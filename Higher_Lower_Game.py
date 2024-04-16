import random
import os
import HigherLowerGame_logoart
import HigherLowerGame_database
print(HigherLowerGame_logoart.game_logo)

def display_accountinfo(account_1):
    name = account_1["name"]
    description = account_1["description"]
    country = account_1["country"]
    return f"{name} a {description}, from {country}"
def check_answer(guess,follower_count1,follower_count2):
    if(follower_count1<follower_count2):
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False
score = 0
continue_flag = True
account_2 = random.choice(HigherLowerGame_database.people_data)
while continue_flag:
    account_1 = account_2
    account_2 = random.choice(HigherLowerGame_database.people_data)
    while account_1 == account_2:
        account_2 = random.choice(HigherLowerGame_database.people_data)
    print(f"Compare1 1 : {display_accountinfo(account_1)}")
    print(HigherLowerGame_logoart.vs)
    print(f"Compare 2 : {display_accountinfo(account_2)}")
    guess = int(input("Who has more followers? Type 1 or 2 : "))
    follower_count_1 = account_1["follower_count"]
    follower_count_2 = account_2["follower_count"]
    print(follower_count_1)
    print(follower_count_2)
    is_correct = check_answer(guess,follower_count_1,follower_count_2)
    os.system('cls')
    if is_correct == True:
        score+=1
        print(f"You are right...\nYour score is {score}")

    else:
        print(f"You ffare wrong..\nYour final score is {score}")
        continue_flag = False