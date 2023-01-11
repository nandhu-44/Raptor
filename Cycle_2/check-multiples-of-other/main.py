num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

if num1 % num2 == 0:
    print(f"{num1} is a multiple of {num2}")
elif num2 % num1 == 0:
    print(f"{num2} is a multiple of {num1}")
else:
    print(f"{num1} and {num2} are not multiples of each other")
