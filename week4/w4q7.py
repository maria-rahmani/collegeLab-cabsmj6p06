def prime(n):
    if n <= 1:
        return "Invalid input! Please enter a number greater than 1."
    for i in range(2, n):
        if n % i == 0:
            return f"{n} is not prime"
    return f"{n} is Prime"

print(prime(6))
