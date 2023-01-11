import math
side1 = int(input("Enter the length of side1: "))
side2 = int(input("Enter the length of side2: "))
side3 = int(input("Enter the length of side3: "))

perimeter = side1 + side2 + side3
semiperimeter = perimeter / 2
area = math.sqrt(semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3))
print("Perimeter of the triangle is: ", perimeter)
print("Area of the triangle is: ", area)
