def perfect(n):
    divisor_sum = 0

    if n < 1:
        print("Invalid Input! Please enter a positive number.")
        return 0

    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i

    if divisor_sum == n:
        return 1

    return 0

print(perfect(10))
