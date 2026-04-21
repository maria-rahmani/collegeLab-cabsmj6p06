s1 = int(input("Enter first signal: "))
s2 = int(input("Enter second signal: "))

def find_signal_sync(a, b):
    if a < 0 or b < 0:
        return -1
    
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    return gcd(a,b)

result = find_signal_sync(s1, s2)

if result == -1:
    print("Numbers must be non-negative!")
else:
    print("Result: ", result)
