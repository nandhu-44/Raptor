number = int(input("Enter a decimal number: "))

binary = ""
while number > 0:
    remainder = number % 2
    number = number // 2
    binary += f"{remainder}"

binary = binary[::-1]

print(f"Binary representation is {binary}")
