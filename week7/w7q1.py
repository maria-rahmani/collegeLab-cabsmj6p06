num = int(input("Enter a numeric value: "))

def narcissistic(num):
    count = 0
    digitSum = 0
    originalNum = num
    temp = num
    while num > 0:
        num = num//10
        count += 1
    while temp > 0:
        digitSum += (int(temp % 10) ** count)
        temp /= 10
    
    if originalNum == digitSum:
        return 1
    else:
        return 0

if narcissistic(num) == 1:
    print("An Armstrong number!")
else:
    print("Not an armstrong number!")
    
