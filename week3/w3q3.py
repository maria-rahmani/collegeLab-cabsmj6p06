l = float(input("Enter length of the cuboid:"))
b = float(input("Enter breadth of the cuboid:"))
h = float(input("Enter height of the cuboid:"))

SA = 2*(l*b + b*h + h*l)
Vol = l * b * h

print(f"Surface area = {SA} and Volume = {Vol}")
