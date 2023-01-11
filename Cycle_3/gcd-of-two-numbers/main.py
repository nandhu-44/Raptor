num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = 1

smallest = min(num1, num2)

for i in range(1, smallest + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print(f"The greatest common divisor of {num1} and {num2} is {gcd}.")