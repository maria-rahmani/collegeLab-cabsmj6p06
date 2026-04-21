# Get user input for the range
n = int(input("Enter the range (e.g., 15): "))

# Generate dictionary with keys 1 to n and their squares
squares = {i: i**2 for i in range(1, n + 1)}

# Output the dictionary
print(squares)   
