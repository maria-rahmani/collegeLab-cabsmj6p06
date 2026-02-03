num = int(input("Enter a number:"))

def fib(n):
    current = 0
    next = 1
    while current <= n:
        if n == current:
            return print(f"{n} is a fibonnaci number")
        
        temp = current + next
        current = next
        next = temp
        
    return print(f"{n} is not a fibonnaci number")

fib(num)
    
