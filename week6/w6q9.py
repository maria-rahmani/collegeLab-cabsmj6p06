num_list = list(input("Enter a list of numbers: "))
new_list = list(map(int, num_list))

def check(l):
    temp_index = 0
    
    for i in range(1, len(l)):
        if l[i] - l[temp_index] != 1:
            return "Not consecutive list"
        temp_index = i

    return "List is consecutive"

print(new_list)
print(check(new_list))

    
