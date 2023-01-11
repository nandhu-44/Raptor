number = int(input("Enter a number: "))
f = 2

while f < number // 2:
    if number % f == 0:
        print(f"{number} is a composite number")
        break
    f += 1
else:
    print(f"{number} is a prime number")