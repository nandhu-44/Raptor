number = int(input("Enter a number: "))
digit1 = number // 10
digit2 = number % 10

if digit1 < digit2:
    print(f"{digit1} is the smallest digit in {number}")
elif digit1 > digit2:
    print(f"{digit2} is the smallest digit in {number}")
else:
    print(f"Both digits are equal")