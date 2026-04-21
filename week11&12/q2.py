def create_histogram(text):
    histogram = {}
    for char in text:
        histogram[char] = histogram.get(char, 0) + 1
    return histogram

# Example 1
input_str1 = "mississippi"
output1 = create_histogram(input_str1)
print(f"Input: '{input_str1}' → Output: {output1}")

# Example 2
input_str2 = "hello world"
output2 = create_histogram(input_str2)
print(f"Input: '{input_str2}' → Output: {output2}")   
