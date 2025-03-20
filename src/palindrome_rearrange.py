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
    
    # Identify the order of characters
    chars_sorted = sorted(char_counts.keys())
    
    # Prepare components of palindrome
    left_chars = []
    middle_char = ""
    
    # Arrange characters 
    for char in chars_sorted:
        count = char_counts[char]
        
        # Add half of even count characters to left side
        if count % 2 == 0:
            left_chars.extend([char] * (count // 2))
        else:
            # Add part of odd count chars to left
            left_chars.extend([char] * ((count - 1) // 2))
            # Use the first odd count char as middle
            if not middle_char:
                middle_char = char
    
    # Create palindrome
    left = ''.join(left_chars)
    right = left[::-1]
    
    return left + middle_char + right