num = int(input("Enter a number: "))
f = 1
sum = 0

while f <= num:
    if num % f == 0:
       sum+=f
    f += 1
print(f"The sum of factors of {num} is {sum}")
