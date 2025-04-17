import pytest

def merge_intervals():
    """
    Merges overlapping intervals into one.

    Given a list of intervals, where each interval is represented by a pair of start and end times, 
    the task is to merge all overlapping intervals into a single interval. The intervals are initially 
    sorted by their start times.

    Args:
        intervals (List[List[int]]): A list of intervals, where each interval is represented by a pair [start, end].

    Returns:
        List[List[int]]: A list of merged intervals.
    """

    pass

def test_merge_intervals():
    result = merge_intervals()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
