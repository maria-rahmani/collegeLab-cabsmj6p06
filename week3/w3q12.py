num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while num2!= 0:
    temp = num1 % num2
    num1 = num2
    num2 = temp

print(f"{num1} is the GCD.")
