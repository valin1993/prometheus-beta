import pytest
from src.most_frequent_char import find_most_frequent_character

def test_basic_functionality():
    """Test finding the most frequent character in a simple string."""
    assert find_most_frequent_character("hello") == 'l'
    assert find_most_frequent_character("programming") == 'r'

def test_empty_string():
    """Test handling of an empty string."""
    assert find_most_frequent_character("") is None

def test_single_character():
    """Test a string with a single character."""
    assert find_most_frequent_character("a") == 'a'

def test_multiple_most_frequent_chars():
    """Test when multiple characters have the same highest frequency."""
    assert find_most_frequent_character("aabbc") == 'a'

def test_all_unique_characters():
    """Test a string where all characters appear once."""
    assert find_most_frequent_character("abcde") == 'a'

def test_spaces_and_mixed_characters():
    """Test a string with spaces and mixed characters."""
    assert find_most_frequent_character("hello world") == 'l'

def test_invalid_input():
    """Test handling of non-string inputs."""
    with pytest.raises(TypeError):
        find_most_frequent_character(12345)
    
    with pytest.raises(TypeError):
        find_most_frequent_character(None)

def test_case_sensitivity():
    """Test case sensitivity of the function."""
    assert find_most_frequent_character("Hello") == 'l'
    assert find_most_frequent_character("hello") == 'l'
    assert find_most_frequent_character("HELLO") == 'L'