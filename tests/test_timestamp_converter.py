import pytest
from src.timestamp_converter import timestamp_to_human_readable

def test_valid_timestamp():
    """Test conversion of a known timestamp."""
    # Updated timestamp to match the expected conversion
    timestamp = 1673785845
    assert timestamp_to_human_readable(timestamp) == '2023-01-15 12:30:45 UTC'

def test_zero_timestamp():
    """Test conversion of zero timestamp (epoch start)."""
    assert timestamp_to_human_readable(0) == '1970-01-01 00:00:00 UTC'

def test_future_timestamp():
    """Test conversion of a future timestamp."""
    # Unix timestamp for a future date
    timestamp = 2147483647  # Year 2038 timestamp
    assert timestamp_to_human_readable(timestamp) == '2038-01-19 03:14:07 UTC'

def test_invalid_type_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        timestamp_to_human_readable("not a number")
    
    with pytest.raises(TypeError):
        timestamp_to_human_readable(None)

def test_negative_timestamp():
    """Test handling of negative timestamps."""
    with pytest.raises(ValueError):
        timestamp_to_human_readable(-1)

def test_large_float_timestamp():
    """Test conversion with a float timestamp."""
    # Updated timestamp to match the expected conversion
    timestamp = 1673785845.5
    assert timestamp_to_human_readable(timestamp) == '2023-01-15 12:30:45 UTC'