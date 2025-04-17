import pytest

def single_number():
    """
    Finds the element that appears exactly once in an array where every other element appears twice.

    The algorithm should have linear runtime complexity and use only constant extra space.

    Args:
        nums (List[int]): A list of integers where every element appears twice except one.

    Returns:
        int: The element that appears only once.
    """

    pass

def test_single_number():
    result = single_number()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
