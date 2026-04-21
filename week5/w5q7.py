def reverse_string(s):
    """
    Reverses a string array in-place with O(1) extra memory.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Test
s = ['h', 'e', 'l', 'l', 'o']
reverse_string(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']