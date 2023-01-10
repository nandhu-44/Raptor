a = int(input("Enter the value of coeff of x^2 (a) : "))
b = int(input("Enter the value of coeff of x (b) : "))
c = int(input("Enter the value of constant (c) : "))
d = b**2 - 4*a*c
if d > 0:
    print("Roots are real and unequal")
elif d == 0:
    print("Roots are real and equal")
else:
    print("Roots are imaginary")
