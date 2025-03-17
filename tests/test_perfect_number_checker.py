import pytest
from src.perfect_number_checker import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) == True, f"{num} should be a perfect number"

def test_known_non_perfect_numbers():
    """Test known non-perfect numbers."""
    non_perfect_numbers = [10, 15, 21, 100, 1000]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) == False, f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases."""
    assert is_perfect_number(1) == False, "1 should not be a perfect number"
    assert is_perfect_number(0) == False, "0 should not be a perfect number"
    
def test_negative_numbers():
    """Test negative numbers."""
    assert is_perfect_number(-6) == False, "Negative numbers should not be perfect numbers"
    assert is_perfect_number(-28) == False, "Negative numbers should not be perfect numbers"

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    with pytest.raises(ValueError):
        is_perfect_number("6")
    with pytest.raises(ValueError):
        is_perfect_number(None)