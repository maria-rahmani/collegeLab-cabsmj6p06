a = int(input("Enter first value:"))
b = int(input("Enter second value:"))

# a^a = 0 (See table)
# a^0 = a (see tale)

print(f"Before swapping a = {a} and b = {b}")

a = a^b # a = 3^4
b = a^b # b = 3^4^4 = 3
a = a^b # a = 3^4^3 = 4

print(f"After swapping a = {a} and b = {b}")
