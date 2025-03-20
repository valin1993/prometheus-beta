import pytest
from src.palindrome_rearrange import can_form_palindrome, rearrange_to_palindrome

def test_can_form_palindrome():
    """
    Test the can_form_palindrome function with various input scenarios.
    """
    # Simple cases
    assert can_form_palindrome("racecar") == True
    assert can_form_palindrome("aab") == True
    assert can_form_palindrome("aabb") == True
    assert can_form_palindrome("abc") == False
    
    # Edge cases
    assert can_form_palindrome("") == True
    assert can_form_palindrome("a") == True
    assert can_form_palindrome("aaaaaa") == True
    
    # Complex cases
    assert can_form_palindrome("aabccb") == True
    
    # Special case with multiple odd-count characters
    assert can_form_palindrome("aabccc") == True

def test_rearrange_to_palindrome():
    """
    Test the rearrange_to_palindrome function with various input scenarios.
    """
    def is_palindrome(s):
        """Helper function to check if a string is a palindrome."""
        return s == s[::-1]
    
    def verify_palindrome(original, result):
        """Verify that the result is a valid palindrome rearrangement."""
        assert result != "", f"Could not form palindrome for {original}"
        assert len(result) == len(original), f"Length mismatch for {original}"
        assert sorted(result) == sorted(original), f"Character mismatch for {original}"
        assert is_palindrome(result), f"Result is not a palindrome for {original}"
    
    # Test cases with various scenarios
    test_cases = [
        "racecar",   # Already a palindrome
        "aab",       # Can be rearranged to palindrome
        "aabb",      # Can be rearranged to palindrome
        "a",         # Single character
        "aaaaaa",    # All same characters
        "aabccb",    # Multiple characters
        "aabccc"     # Multiple characters with differing odd/even counts
    ]
    
    # Negative test case
    assert rearrange_to_palindrome("abc") == ""
    assert rearrange_to_palindrome("") == ""
    
    # Test valid palindrome rearrangement
    for case in test_cases:
        result = rearrange_to_palindrome(case)
        verify_palindrome(case, result)

def test_edge_cases():
    """
    Test edge cases and boundary conditions.
    """
    # Empty and single character cases
    assert can_form_palindrome("") == True
    assert rearrange_to_palindrome("") == ""
    
    # Single character
    assert can_form_palindrome("a") == True
    assert rearrange_to_palindrome("a") == "a"
    
    # Multiple characters with odd count
    test_cases = ["aabccc"]
    for case in test_cases:
        assert can_form_palindrome(case) == True
        assert rearrange_to_palindrome(case) != ""