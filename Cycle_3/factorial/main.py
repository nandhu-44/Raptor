number = int(input("Enter a number: "))
original_number = number
factorial = number
while number > 1:
    number -= 1
    factorial *= number
print(f"The factorial of {original_number} is {factorial}")