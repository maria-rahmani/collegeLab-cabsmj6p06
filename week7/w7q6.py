def ID_filter(id_list: list):
    low_priority = []
    high_priority = []

    for id in id_list:
        if id % 2 == 0:
            low_priority.append(id)
        else:
            high_priority.append(id)

    return low_priority, high_priority

packet_id = list(map(int, input("Enter IDs: ").split()))
low, high = ID_filter(packet_id)

print("Low priority IDs: ", low)
print("High priority IDs: ", high)