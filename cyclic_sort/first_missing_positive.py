import pytest

def first_missing_positive():
    """
    Finds the smallest missing positive integer from an unsorted list.

    The algorithm should run in O(n) time and use constant extra space.

    Args:
        nums (List[int]): The input list of integers.

    Returns:
        int: The smallest positive integer that is missing from the list.
    """
    pass

def test_first_missing_positive():
    result = first_missing_positive()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
