def count_vowels_consonants(text):
    """
    Counts and displays vowels and consonants in the text.
    """
    vowels = set('aeiouAEIOU')
    vowel_list = []
    consonant_list = []
    
    for char in text:
        if char.isalpha():  # Check if it's a letter
            if char in vowels:
                vowel_list.append(char)
            else:
                consonant_list.append(char)
    
    print(f"Vowels: {', '.join(vowel_list)}")
    print(f"Number of vowels: {len(vowel_list)}")
    print(f"Consonants: {', '.join(consonant_list)}")
    print(f"Number of consonants: {len(consonant_list)}")
    
    return {
        'vowels': vowel_list,
        'vowel_count': len(vowel_list),
        'consonants': consonant_list,
        'consonant_count': len(consonant_list)
    }

# Test
text = "Hello World"
count_vowels_consonants(text)