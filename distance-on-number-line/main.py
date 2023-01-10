num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

if num1 > 0 and num2 > 0:
    print(f"The distance between {num1} and {num2} is {abs(num2 - num1)} units")
elif num1 < 0 and num2 < 0:
    print(f"The distance between {num1} and {num2} is {abs(num2 - num1)} units")
else:
    print(f"The distance between {num1} and {num2} is {abs(num2) + abs(num1)} units")