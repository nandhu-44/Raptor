number = int(input("Enter a number: "))
original_number = number
reverse = 0
while number > 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number // 10

print(f"The reverse of {original_number} is {reverse}")