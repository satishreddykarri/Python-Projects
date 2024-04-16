size = input("Enter the size of pizza you want(S/M/L)?")
bill = 0
if(size == 'S' or size == 's'):
    bill += 100
    print("Small size pizza price is 100Rs...")
elif (size == 'M' or size == 'm'):
    bill += 200
    print("Medium size pizza price is 200rs...")
else:
    bill += 300
    print("Large size pizza price is 300Rs...")
add_pepper = input("Do you want pepper with the pack(Y/N)? ")
if add_pepper == "y" or add_pepper == 'Y':
    if size == "s" or size == "S":
        bill += 30
    else:
        bill += 50
extra_cheese = input("Do you want some extra cheese also(Y/N)? ")
if extra_cheese == "y" or extra_cheese == "Y":
    bill += 20
print(f"Your total bill prize is {bill}")