from datetime import datetime, timezone

def timestamp_to_human_readable(timestamp):
    """
    Convert a timestamp to a human-readable date string.

    Args:
        timestamp (int or float): A Unix timestamp (seconds since epoch).

    Returns:
        str: A human-readable date string in the format 'YYYY-MM-DD HH:MM:SS UTC'.

    Raises:
        TypeError: If the input is not an integer or float.
        ValueError: If the timestamp is negative or cannot be converted.
    """
    # Type checking
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be an integer or float")
    
    # Validate timestamp value
    if timestamp < 0:
        raise ValueError("Timestamp cannot be negative")
    
    try:
        # Use fromtimestamp with UTC timezone
        dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        
        # Format the date in a human-readable format
        return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    
    except (ValueError, OSError) as e:
        raise ValueError(f"Unable to convert timestamp: {e}")