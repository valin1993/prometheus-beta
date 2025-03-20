import pytest
from src.string_capitalizer import capitalize_strings

def test_capitalize_strings_basic():
    """Test basic string capitalization."""
    input_array = ["hello", "world", "python"]
    expected = ["Hello", "World", "Python"]
    assert capitalize_strings(input_array) == expected

def test_capitalize_strings_empty_list():
    """Test capitalization of an empty list."""
    assert capitalize_strings([]) == []

def test_capitalize_strings_already_capitalized():
    """Test strings that are already capitalized."""
    input_array = ["Hello", "World"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_array) == expected

def test_capitalize_strings_mixed_case():
    """Test strings with mixed case."""
    input_array = ["hELLo", "wORLd", "pYTHOn"]
    expected = ["Hello", "World", "Python"]
    assert capitalize_strings(input_array) == expected

def test_capitalize_strings_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        capitalize_strings("not a list")

def test_capitalize_strings_non_string_elements():
    """Test that a TypeError is raised for non-string list elements."""
    with pytest.raises(TypeError, match="All elements in the list must be strings"):
        capitalize_strings(["hello", 42, "world"])

def test_capitalize_strings_single_element():
    """Test capitalization with a single element list."""
    assert capitalize_strings(["single"]) == ["Single"]