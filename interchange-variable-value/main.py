num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

print(f"The values of number1 and number 2 are {num1} and {num2} respectively")

num1,num2 = num2,num1

print(f"After swapping the values of number1 and number 2 are {num1} and {num2} respectively")