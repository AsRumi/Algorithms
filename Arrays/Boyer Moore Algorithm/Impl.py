def build_bad_character_table(pattern):
    """
    Builds the bad character table for Boyer-Moore.
    Returns a dictionary mapping each character to its rightmost position in pattern.
    """
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table

def boyer_moore_search(text, pattern):
    """
    Boyer-Moore string search algorithm using bad character rule.
    Returns a list of all starting positions where pattern is found in text.
    """
    if not pattern or not text:
        return []
    
    n = len(text)
    m = len(pattern)
    
    if m > n:
        return []
    
    # Build the bad character table
    bad_char = build_bad_character_table(pattern)
    matches = []
    
    # Start with pattern aligned at the beginning of text
    s = 0  # shift of the pattern relative to text
    
    while s <= n - m:
        j = m - 1  # Start comparing from the end of pattern
        
        # Keep matching characters from right to left
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        if j < 0:
            # Pattern found! All characters matched
            matches.append(s)
            # Shift pattern to align with next possible position
            s += 1
        else:
            # Mismatch occurred at position j
            # Get the mismatched character from text
            bad_char_in_text = text[s + j]
            
            # Calculate shift using bad character rule
            if bad_char_in_text in bad_char:
                # Character exists in pattern
                # Shift pattern to align this character with its rightmost occurrence
                shift = max(1, j - bad_char[bad_char_in_text])
            else:
                # Character doesn't exist in pattern
                # Shift pattern completely past this character
                shift = j + 1
            
            s += shift
    
    return matches

# Example usage and demonstration
def demonstrate_boyer_moore():
    text = "ABAAABCDABCDABAAABCD"
    pattern = "ABCD"
    
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    print(f"Pattern length: {len(pattern)}\n")
    
    # Build bad character table
    bad_char = build_bad_character_table(pattern)
    print("Bad Character Table:")
    for char, pos in sorted(bad_char.items()):
        print(f"  '{char}' -> position {pos}")
    print()
    
    # Find all matches
    matches = boyer_moore_search(text, pattern)
    
    print(f"Pattern found at positions: {matches}\n")
    
    # Visualize matches
    for pos in matches:
        print(" " * pos + pattern + f"  <- Match at position {pos}")
        print(text)
        print()

# Run demonstration
demonstrate_boyer_moore()

# Additional test cases
print("\n" + "="*50)
print("Additional Test Cases")
print("="*50 + "\n")

test_cases = [
    ("AAAAAAA", "AAA"),
    ("ABCDEFGHIJKLMNOP", "MNOP"),
    ("ABABABABAB", "ABAB"),
    ("The quick brown fox jumps over the lazy dog", "fox")
]

for text, pattern in test_cases:
    matches = boyer_moore_search(text, pattern)
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")
    print(f"Matches at: {matches if matches else 'No matches found'}")
    print()