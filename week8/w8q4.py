n = int(input("Enter value of n: "))

data = []
for i in range(n + 1):
    item = (i, 5 * i**3)
    data.append(item)

print("Result:", data)
