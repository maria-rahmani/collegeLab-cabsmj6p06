def letters_count(s):
    new_s = list(s)
    count_upper = 0
    count_lower = 0
    for i in new_s:
        if i.isupper():
            count_upper += 1
        if i.islower():
            count_lower += 1

    print("Number of uppercase letters are : ", count_upper)
    print("Number of lowercase letters are : ", count_lower)
    
print(letters_count('Maria Rahmani'))
