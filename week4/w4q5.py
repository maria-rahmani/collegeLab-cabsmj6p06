def digit_sum(n):
    updated_n = map(int, list(str(n)))
    sum_val = sum(updated_n)
    return sum_val

print(digit_sum(541))
