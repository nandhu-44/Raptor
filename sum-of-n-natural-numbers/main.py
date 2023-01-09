num = int(input("Enter the number of terms: "))
sum = 0
for i in range(1, num+1):
    sum+=i
print(f"The sum of first {num} natural numbers is {sum}")