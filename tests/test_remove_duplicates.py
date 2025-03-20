import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates."""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test with an empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test with a list that has no duplicates."""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test with a list of all duplicate elements."""
    input_list = [1, 1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_preserves_first_occurrence_order():
    """Ensure the first occurrence of each unique element is preserved."""
    input_list = [5, 2, 3, 2, 5, 1, 3]
    expected = [5, 2, 3, 1]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)

def test_remove_duplicates_invalid_element_type():
    """Test that a ValueError is raised for non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be integers"):
        remove_duplicates([1, 2, "3", 4])
    with pytest.raises(ValueError, match="All elements must be integers"):
        remove_duplicates([1, 2, 3.14, 4])