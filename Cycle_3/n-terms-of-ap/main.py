first_term = int(input("Enter the value of first term (a) : "))
diff = int(input("Enter the value of common difference (d) : "))
num = int(input("Enter the number of terms (n) : "))

i = 1
while i <= num:
    print(first_term)
    first_term += diff
    i += 1
