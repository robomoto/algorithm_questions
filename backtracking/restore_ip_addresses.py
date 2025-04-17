import pytest

def restore_ip_addresses():
    """
    Given a string containing only digits, return all possible valid IP address combinations
    that can be formed by inserting dots into the string.

    A valid IP address consists of exactly four integers (each between 0 and 255) separated by dots,
    and cannot have leading zeros unless the segment is exactly '0'.

    Args:
        s (str): A string containing only digits.

    Returns:
        List[str]: A list of all possible valid IP address combinations.
    """

    pass

def test_restore_ip_addresses():
    result = restore_ip_addresses()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
