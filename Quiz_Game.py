print("********************")
print("Welcome to My Quiz Game!!!")
def check_answer(user_guess, correct_ans):
    if(user_guess == correct_ans):
        return True
    else:
        return False

question_bank = [
    {"text": "The ability of one class to acquire menthos and attributes from another class is called _____.","answer":"A"},
    {"text": "Which of the following is a type of inheritance?","answer":"D"},
    {"text": "WHat type of inheritance has multiple subclasses to a single superclass?","answer":"C"},
    {"text": "What is the depth pf ulti level inhertance in Python?","answer":"C"},
    {"text": "What does MRO stands for? ","answer":"B"}
]
options = [
    ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D.Objects"],
    ["A.Single", "B.Double", "C. Multiple", "D. both A and C"],
    ["A. Mutliple Inheritance", "B. Multilevel Inheritance", "C. Hierarchial Inheritance", "D. None of these"],
    ["A. Two level", "B. Three level", "C. Any level","D. None of these"],
    ["A. Method Recursive Object", "B. Method Resolution Order", "C. Main REsolution Order", "D. Method Resolution Object"]
]
score = 0
for question_no in range(len(question_bank)):
    print("********************************")
    print(question_bank[question_no]["text"])
    for i in options[question_no]:
        print(i)
    guess = input("Enter your answer(A/B/C/D) : ").upper()
    is_correct = check_answer(guess,question_bank[question_no]["answer"])
    if is_correct:
        score += 1
    else:
        print("Incorrect answer")
        print(f"The correct answer is {question_bank[question_no]["answer"]}")
    print(f"Your score is {score}/{question_no+1}")
print(f"Your final score is {score}")
print(f"Your score percentage is {(score/len(question_bank)) * 100}%")