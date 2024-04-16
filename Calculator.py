import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    n1 = int(input("Enter first number: "))
    for symbol in operations_dict:
        print(symbol)

    continue_flag = True
    while continue_flag:
        op_symbol = input("Pick an operation : ")
        n2 = int(input("Enter next number: "))
        cal_function = operations_dict[op_symbol]
        output = cal_function(n1,n2)
        print(f"{n1} {op_symbol} {n2} = {output}")

        should_continue= input(f"Enter 'y' to calculate with previous number {output} and enter 'n' to start new calculation and 'x' to exit : ").lower()
        if should_continue == 'y':
            n1 = output
        elif should_continue == 'n':
            continue_flag = False
            os.system('cls')
            calculator()
        elif should_continue == 'x':
            continue_flag = False
            print("Thank you...")

calculator()