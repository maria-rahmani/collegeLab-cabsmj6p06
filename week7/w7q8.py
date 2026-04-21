def int_list_input(input_string: str):
    user_in = list(map(int, input(input_string).split()))
    return user_in

id_list_1 = int_list_input("Enter IDs for list 1: ")
id_list_2 = int_list_input("Enter IDs for list 2: ")

result = sorted(id_list_1 + id_list_2)

print("Merged list:", result)