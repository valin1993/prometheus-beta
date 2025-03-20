def fibonacci_reverse(n):
    """
    Generate a reverse Fibonacci sequence up to the Nth element.
    
    Args:
        n (int): The number of Fibonacci elements to generate.
    
    Returns:
        list: A list of Fibonacci numbers in reverse order.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    
    Examples:
        >>> fibonacci_reverse(0)
        []
        >>> fibonacci_reverse(1)
        [0]
        >>> fibonacci_reverse(5)
        [3, 2, 1, 1, 0]
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle edge cases
    if n == 0:
        return []
    
    # Generate Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Extend the sequence if needed
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Trim and reverse the sequence
    return list(reversed(fib_sequence[:n]))