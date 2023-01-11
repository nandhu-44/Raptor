number = int(input("Enter the number of terms: "))

first = 0
second = 1
if number <=0:
    print("Need at least one term!")
elif number == 1:
    print(first)
elif number == 2:
    print(first, second, sep =", ")
else:
    print(first, second, sep =", ", end =", ")
    count = 2
    while count < number:
        next = first + second
        print(next, end =", ")
        first = second
        second = next
        count += 1
    print()