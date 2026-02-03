num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))

if num2 == 0:
    print("Zero division error!")
    exit()
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")

