def count_word_frequency(sentence):
    """
    Counts occurrences of each word in a sentence.
    """
    # Remove punctuation and convert to lowercase
    import string
    # Remove punctuation from sentence
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Split into words and convert to lowercase
    words = sentence.lower().split()
    
    # Count frequencies
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

# Test cases
print(count_word_frequency("Hello hello world"))  # Output: {'hello': 2, 'world': 1}
print(count_word_frequency("Hi, Hi!"))  # Output: {'hi': 2}