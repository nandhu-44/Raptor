number = int(input("Enter the number of terms: "))

sum = 0
sign = 1

for i in range(1, number+1):
    sum += sign*(i**2)
    sign *= -1

print(f"The sum of the series upto {number} terms is {sum}")
