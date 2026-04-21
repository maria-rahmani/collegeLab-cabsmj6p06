files = []
name = None

print("Write 0 to end input...\n")

while name != "0":
    name = input("Enter a filename: ")
    
    if name != "0": files.append(name)

print(files)

# Using Bubble Sort
n = len(files)
for i in range(n):
    for j in range(0, n - i - 1):
        if len(files[j]) > len(files[j + 1]):
            files[j], files[j + 1] = files[j + 1], files[j]
            
print("Sorted Files:")
print(files)
