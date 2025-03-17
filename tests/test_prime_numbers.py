import pytest
from src.prime_numbers import find_primes_to_n

def test_primes_to_100():
    """Test finding primes from 1 to 100."""
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    assert find_primes_to_n(100) == expected_primes

def test_small_primes():
    """Test finding primes for small ranges."""
    assert find_primes_to_n(10) == [2, 3, 5, 7]
    assert find_primes_to_n(2) == [2]

def test_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        find_primes_to_n(1)
    
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        find_primes_to_n(0)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_primes_to_n("not an int")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_primes_to_n(3.14)

def test_large_input():
    """Test handling of a larger input."""
    primes = find_primes_to_n(1000)
    assert len(primes) > 0
    assert primes[-1] <= 1000
    assert all(is_prime(p) for p in primes)

def is_prime(n):
    """Helper function to verify primality."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True