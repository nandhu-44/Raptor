number = int(input("Enter a number: "))
original_number = number
reverse = 0
while number > 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number // 10
if original_number == reverse:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")

