num = int(input("Enter a number:"))

def factorial(num):
    fact = 1
    if num < 0:
        return print("Invalid input! Please enter a positive number.")
    if num == 0:
        return 1
    if num == 1:
        return 1
    while num > 0:
        fact = fact * num
        num = num - 1
    return fact

print(f"Factorial of {num} = {factorial(num)}")
