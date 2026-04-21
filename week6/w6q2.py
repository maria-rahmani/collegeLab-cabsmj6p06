reading1 = float(input("Enter first reading: "))
reading2 = float(input("Enter second reading: "))
reading3 = float(input("Enter third third: "))

def lowest_reading(a, b, c):
    lowest = a
    if b < a:
        lowest = b
    if c < a:
        lowest = c

    return lowest

print(f"Lowest among the three readings is {lowest_reading(reading1, reading2, reading3)}")
