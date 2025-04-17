import pytest

def cyclic_sort():
    """
    Sorts an array containing `n` distinct numbers taken from the range [0, n] or [1, n].

    The algorithm places each number at its correct index by swapping elements in-place,
    resulting in an O(n) time complexity and O(1) space complexity.

    Args:
        nums (List[int]): The unsorted list of integers.

    Returns:
        None: The input list is modified in-place to be sorted.
    """

    pass

def test_cyclic_sort():
    result = cyclic_sort()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
