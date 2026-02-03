from math import pi
def area(R, r):
    if R > r:
        return pi*(R-r)**2
    return "R should be greater than r"

print(area(1,2))
