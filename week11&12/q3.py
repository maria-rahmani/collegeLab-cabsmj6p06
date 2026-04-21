def reverse_lookup(employee_data, badge_id):
    for name, bid in employee_data.items():
        if bid == badge_id:
            return name
    return "ID not found"

# Example usage
employee_data = {'Alice': 5001, 'Bob': 5002, 'Charlie': 5003}

print(reverse_lookup(employee_data, 5002))  # Output: Bob
print(reverse_lookup(employee_data, 9999))  # Output: ID not found   
