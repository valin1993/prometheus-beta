import pytest
from src.palindrome_rearrange import can_form_palindrome, rearrange_to_palindrome

def test_can_form_palindrome():
    # Test cases for can_form_palindrome
    assert can_form_palindrome("racecar") == True
    assert can_form_palindrome("aab") == True
    assert can_form_palindrome("aabb") == True
    assert can_form_palindrome("abc") == False
    assert can_form_palindrome("") == True
    assert can_form_palindrome("a") == True
    assert can_form_palindrome("aaaaaa") == True
    assert can_form_palindrome("aabccb") == True
    assert can_form_palindrome("aabccc") == True

def test_rearrange_to_palindrome():
    # Test various scenarios for rearrange_to_palindrome
    assert rearrange_to_palindrome("racecar") == "racecar"
    assert rearrange_to_palindrome("aab") in ["aba", "baa"]
    assert rearrange_to_palindrome("aabb") in ["abba", "baab"]
    assert rearrange_to_palindrome("abc") == ""
    assert rearrange_to_palindrome("") == ""
    assert rearrange_to_palindrome("a") == "a"
    assert rearrange_to_palindrome("aaaaaa") == "aaaaaa"
    
    # Verify that the result is indeed a palindrome
    def is_palindrome(s):
        return s == s[::-1]
    
    # Additional palindrome check for rearrangeable strings
    test_cases = ["aabccb", "aabccc"]
    for case in test_cases:
        result = rearrange_to_palindrome(case)
        assert result != "", f"Could not form palindrome for {case}"
        assert is_palindrome(result), f"Result {result} is not a palindrome"
        # Verify same character counts
        assert sorted(result) == sorted(case)

def test_edge_cases():
    # Empty string
    assert can_form_palindrome("") == True
    assert rearrange_to_palindrome("") == ""
    
    # Single character
    assert can_form_palindrome("a") == True
    assert rearrange_to_palindrome("a") == "a"
    
    # Multiple characters with odd count
    assert can_form_palindrome("aabccc") == True
    assert rearrange_to_palindrome("aabccc") != ""