score1 = int(input("Enter first score: "))
score2 = int(input("Enter second score: "))
score3 = int(input("Enter third score: "))

def highest_score(a, b, c):
    highest = a
    if b > a:
        highest = b
    if c > a:
        highest = c

    return highest

print(f"Highest among the three scores is {highest_score(score1, score2, score3)}")
