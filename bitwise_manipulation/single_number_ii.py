import pytest

def single_number_ii():
    """
    Finds the element that appears exactly once in an array where every other element appears three times.

    The algorithm should have linear runtime complexity and use only constant extra space.

    Args:
        nums (List[int]): A list of integers where every element appears three times except one.

    Returns:
        int: The element that appears only once.
    """

    pass

def test_single_number_ii():
    result = single_number_ii()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
