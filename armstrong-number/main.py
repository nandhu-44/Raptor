number = int(input("Enter a number: "))
original_number = number
sum = 0
terms = len(str(number))

while number > 0:
    digit = number % 10
    sum += digit ** terms
    number = number // 10

if sum == original_number:
    print("The given number is an armstrong number.")
else:
    print("The given number is not an armstrong number.")
