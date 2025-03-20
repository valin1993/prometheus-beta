from collections import Counter

def can_form_palindrome(s: str) -> bool:
    """
    Determines if the characters in the given string can be rearranged to form a palindrome.

    A palindrome can be formed if at most one character has an odd count,
    and all other characters have even counts.

    Args:
        s (str): The input string to check for palindrome rearrangement possibility.

    Returns:
        bool: True if the string's characters can be rearranged to form a palindrome, False otherwise.

    Examples:
        >>> can_form_palindrome("racecar")
        True
        >>> can_form_palindrome("aab")
        True
        >>> can_form_palindrome("abc")
        False
    """
    # Count the frequency of each character
    char_counts = Counter(s)
    
    # Count characters with odd frequencies
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    
    # Palindrome is possible if at most one character has an odd count
    return odd_count <= 1

def rearrange_to_palindrome(s: str) -> str:
    """
    Rearranges the characters in the given string to form a palindrome.

    Args:
        s (str): The input string to rearrange.

    Returns:
        str: A palindrome formed by rearranging the characters, or an empty string if impossible.

    Examples:
        >>> rearrange_to_palindrome("aab")
        "aba"
        >>> rearrange_to_palindrome("racecar")
        "racecar"
        >>> rearrange_to_palindrome("abc")
        ""
    """
    # First, check if palindrome rearrangement is possible
    if not can_form_palindrome(s):
        return ""
    
    # Special cases for empty string or single character
    if len(s) <= 1:
        return s
    
    # Count character frequencies
    char_counts = Counter(s)
    
    # If the input is already a palindrome, return it
    if s == s[::-1]:
        return s
    
    # Get character frequencies sorted in lexicographic order
    freq_sorted_chars = sorted(char_counts.items(), key=lambda x: x[0])
    
    # Separate characters with even and odd counts
    left_half = []
    middle_char = None
    
    for char, count in freq_sorted_chars:
        # For even count, add half to left side
        if count % 2 == 0:
            left_half.extend([char] * (count // 2))
        else:
            # Add half to left side and set middle character
            left_half.extend([char] * ((count - 1) // 2))
            # If multiple odd count characters, choose lexicographically smallest
            if middle_char is None or char < middle_char:
                middle_char = char
    
    # Construct palindrome
    middle = middle_char if middle_char is not None else ''
    right_half = left_half[::-1]
    
    return ''.join(left_half) + middle + ''.join(right_half)