a = int(input("Enter first side of a triangle: "))
b = int(input("Enter second side of a triangle: "))
c = int(input("Enter third side of a triangle: "))

def triangle(a, b, c):
    if a == b and b == c:
        print("Equilateral triangle!")
    if a == b or b == c or c == a:
        print("Isosceles triangle!")
    if a != b and b != c and c != a:
        print("Scalene triangle!")

if a+b > c and b+c > a and c+a > b:
    triangle(a, b, c)
else:
    print("Triangle can't be formed")



     
