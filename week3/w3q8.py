a = int(input("Enter first value:"))
b = int(input("Enter second value:"))

print(f"Before swapping a = {a} and b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swapping a = {a} and b = {b}")
a = a + b
b = a - b
a = a - b

