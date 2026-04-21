def remove_even_index_chars(text):
    """
    Removes characters at even index positions (0, 2, 4, etc.)
    """
    result = ''
    for i in range(len(text)):
        if i % 2 != 0:  # Keep characters at odd indices
            result += text[i]
    return result

# Test cases
print(remove_even_index_chars("H@e#l$l"))  # Output: "el"
print(remove_even_index_chars(""))  # Output: ""