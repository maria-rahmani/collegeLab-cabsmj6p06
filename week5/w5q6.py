def remove_indentation(multiline_text):
    """
    Removes indentation from each line of multi-line text.
    """
    lines = multiline_text.split('\n')
    cleaned_lines = [line.lstrip() for line in lines]
    return '\n'.join(cleaned_lines)

# Test
text = """    First line
      Second line
        Third line"""
print(remove_indentation(text))