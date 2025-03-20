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
    
    # Count character frequencies
    char_counts = Counter(s)
    
    # Separate characters with even and odd counts
    even_chars = []
    odd_chars = []
    
    for char, count in char_counts.items():
        if count % 2 == 0:
            # Add half of even-count characters to the sides
            even_chars.extend([char] * (count // 2))
        else:
            # Add half of the odd character count to sides
            even_chars.extend([char] * ((count - 1) // 2))
            odd_chars.append(char)
    
    # Construct palindrome
    # Left side of characters
    left = ''.join(even_chars)
    # Middle character (if exists) - use the first odd count character
    middle = odd_chars[0] if odd_chars else ''
    # Right side (reversed left side)
    right = left[::-1]
    
    return left + middle + right