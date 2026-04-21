n = int(input("Enter the number of terms for fibonacci series: "))

def fib(n):
    if n < 0:
        return "Invalid input! Please enter a number greater than 0."
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("Fibonacci series: ")
for i in range(n):
    print(fib(i), end=" ")
