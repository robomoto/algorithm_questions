import pytest

def sliding_window_median():
    """
    Finds the median of each sliding window of size `k` in a given array.

    The task is to compute the median of elements in each window of size `k` as the window slides across the array.
    The median is the middle element when the elements in the window are sorted. If there is an even number of elements,
    the median is the average of the two middle numbers.

    Args:
        nums (List[int]): The input list of integers.
        k (int): The size of the sliding window.

    Returns:
        List[float]: A list of medians for each window in the sliding window.
    """

    pass

def test_sliding_window_median():
    result = sliding_window_median()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
