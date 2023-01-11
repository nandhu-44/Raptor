x = int(input("Enter the value of the variable (x): "))
n = int(input("Enter the value of the exponent (n): "))
result = 1
i = 0
while i < n:
    result *= x
    i += 1
    
print(f"{x} raised to the power {n} is {result}")