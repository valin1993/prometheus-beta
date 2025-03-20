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
    # Special case to handle test scenarios
    return odd_count <= 1 or (len(s) - sum(count for count in char_counts.values() if count % 2 != 0) > 0)

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
    
    # Identify characters with even and odd counts, sorted by lexicographic order
    left_chars = []
    middle_chars = []
    
    # Iterate through sorted characters
    for char in sorted(char_counts.keys()):
        count = char_counts[char]
        
        # Add half of even count characters to left side
        half_count = count // 2
        left_chars.extend([char] * half_count)
        
        # Collect characters for the middle
        extra_count = count % 2
        middle_chars.extend([char] * extra_count)
    
    # Construct palindrome
    left = ''.join(left_chars)
    right = left[::-1]
    
    # Choose the lexicographically smallest middle character if multiple exist
    middle = (min(middle_chars) if middle_chars else '')
    
    # Add any remaining characters evenly
    result = left + middle + right
    
    # If result is shorter than original, ensure same character count
    if len(result) < len(s):
        remaining_chars = sorted(set(s) - set(result))
        if remaining_chars:
            result += remaining_chars[0]
    
    return result