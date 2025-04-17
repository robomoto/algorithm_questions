import pytest

def sort_colors():
    """
    Sorts an array of colors.

    Given an array of integers representing colors (0, 1, and 2), the task is to sort the array in-place such that 
    all the 0s come first, followed by the 1s, and then the 2s. The solution should not use the built-in sort function.

    Args:
        nums (List[int]): A list of integers where each integer is 0, 1, or 2, representing the colors.

    Returns:
        None: The list is sorted in place.
    """

    pass

def test_sort_colors():
    result = sort_colors()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
