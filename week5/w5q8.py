def reverse_words(s):
    """
    Reverses characters in each word while preserving whitespace and word order.
    """
    words = s.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Test
print(reverse_words("Hello World Python"))  # Output: "olleH dlroW nohtyP"