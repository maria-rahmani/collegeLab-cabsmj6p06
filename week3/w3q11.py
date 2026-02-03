num = int(input("Enter a number: "))
if num <= 1:
    print("Invalid input! Please enter a valid number.")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Number is not prime.")
            print("It's first factor is: ", i)
            break
    else:
        print("Number is prime.")
