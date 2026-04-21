num = int(input("Enter a number: "))

def calculate_routes(n):
    if n < 0:
        return "Invalid input! Please enter a positive number."
    if n == 0 or n == 1:
        return 1
    
    return n*calculate_routes(n-1)

print(f"Factorial of {num} is {calculate_routes(num)}")
