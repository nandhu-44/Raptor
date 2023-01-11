number = int(input("Enter a number: "))
square = number ** 2

f = 1
while f <= number:
    f *= 10

if (square % f) == number:
    print(f"{number} is an automorphic number")
else:
    print(f"{number} is not an automorphic number")
