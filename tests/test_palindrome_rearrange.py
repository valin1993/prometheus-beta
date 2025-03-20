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
    assert can_form_palindrome("aabccc") == True

def test_rearrange_to_palindrome():
    """
    Test the rearrange_to_palindrome function with various input scenarios.
    """
    # Specific test cases
    test_cases = [
        ("racecar", "racecar"),  # Already a palindrome
        ("aab", ["aba", "baa"]),  # Multiple possible rearrangements 
        ("aabb", ["abba", "baab"]),  # Multiple possible rearrangements
        ("abc", ""),  # Impossible to form palindrome
        ("", ""),  # Empty string
        ("a", "a"),  # Single character
        ("aaaaaa", "aaaaaa"),  # All same characters
        ("aabccb", lambda x: len(x) == 6 and x != ""),  # Palindrome possible
        ("aabccc", lambda x: len(x) == 6 and x != "")   # Palindrome possible
    ]
    
    def is_palindrome(s):
        """Helper function to check if a string is a palindrome."""
        return s == s[::-1]
    
    def verify_rearrangement(original, result):
        """Verify that the rearrangement is valid."""
        # Check result type
        if callable(result):
            assert result(original), f"Invalid result for {original}"
        else:
            assert result == original or is_palindrome(result), \
                f"Invalid rearrangement for {original}"
        
        # Verify character counts
        if result:
            assert sorted(result) == sorted(original), \
                f"Character counts don't match for {original}"
    
    # Run through test cases
    for original, expected in test_cases:
        result = rearrange_to_palindrome(original)
        verify_rearrangement(original, expected)

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