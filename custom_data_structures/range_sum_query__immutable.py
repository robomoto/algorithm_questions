import pytest

def range_sum_query_immutable():
    """
    Implements a data structure that supports querying the sum of elements in a given range.

    The array is immutable, meaning values cannot be updated once initialized.
    The structure supports efficient sum range queries.

    Methods:
        sumRange(left: int, right: int) -> int:
            Returns the sum of elements between indices left and right (inclusive).

    Args:
        left (int): The starting index of the range.
        right (int): The ending index of the range.

    Returns:
        int: The sum of elements from index `left` to `right`, inclusive.
    """

    pass

def test_range_sum_query_immutable():
    result = range_sum_query_immutable()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
