num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

if num1 < num2 and num1 < num3 :
    print(f"{num1} is the smallest number")
elif num2 < num3 :
    print(f"{num2} is the smallest number")
else:
    print(f"{num3} is the smallest number")