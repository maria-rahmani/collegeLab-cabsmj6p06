x = int(input("Enter a number: "))
x = str(x)

if x == x[::-1]:
    print(f"{x} is Palindrome")
else:
    print(f"{x} is not Palindrome")