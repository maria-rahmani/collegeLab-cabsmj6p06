n = int(input("Enter an integer value: "))
s1 = "Fizz"
s2 = "Buzz"

if n % 3 == 0 and n % 5 == 0:
    print(s1 + s2)
elif n % 3 == 0:
    print(s1)
elif n % 5 == 0:
    print(s2)
