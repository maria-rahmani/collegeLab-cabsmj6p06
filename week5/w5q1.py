import math

def largest(n, m, p):
    return max(n, m, p)

def volume(shape):
    match shape:
        case ("cylinder", r, h):
            return math.pi*r**2*h
        case ("cube", a):
            return a**3
        case ("rect_box", l, w, h):
            return l*w*h
def rect_area(l,b):
    return l*b

def circle_circum(r):
    return 2*math.pi*r

def swap(a, b):
    a,b = b,a

def dist(a, b):
    return math.dist(a, b)

print("Enter your choice:")
print("1. Largest\n2. Volume\n3. Area_rectangle\n4. Circumference\n5. Swap\n6. Distance")
choice : int(input("Entered choice : "))

if choice < 1 or choice > 6:
    print("Invalid choice! Choose among the given options.")

match choice:
    case 1:
        x1 = int(input("Enter first number: "))
        x2 = int(input("Enter second number: "))
        x3 = int(input("Enter third number: "))

        print("Largest among the entered three number is ", largest(x1, x2, x3))
    case 2:
        shape = input("Enter a shape (cylinder, cube, rectangular box): ")
        if shape != "cylinder" or shape != "cube" or shape != "rect_box":
            print("Invalid shape input! Please enter among the options given.")
            exit()
        if shape == "cylinder":
            r = float(input("Enter radius of cylinder: "))
            h = float(input("Enter height of cylinder: "))
            print(volume(("cylinder", r, h)))
        elif shape == "cube":
            s = float(input("Enter side of cube: "))
            print(volume(("cube", s)))
        else:
            l = float(input("Enter length of rect_box: "))
            w = float(input("Enter width of rect_box: "))
            h = float(input("Enter height of rect_box: "))

            print(volume("rect_box", l, w, h))
            
            print("Volume of cylinder is ", volume("cylinder", r, h))
    case 3:
        l = float(input("Enter length of rectangle: "))
        b = float(input("Enter breadth of rectangle: "))

        print("Area of rectangle: ", rect_area(l, b))
    case 4:
        r = float(input("Enter radius of circle: "))

        print("Circumference of the given circle is ", circle_circum(r))
    case 5:
        x1 = int(input("Enter first number: "))
        x2 = int(input("Enter second number: "))

        print(f"Before swapping x = {x} and y = {y}")
        swap(x1, x2)
        print(f"After swapping x = {x} and y = {y}")
    case 6:
        p1 = list(input("Enter point 1: "))
        p2 = list(input("Enter point 2: "))

        print("Distance between the given two points are: ", dist(p1, p2))







