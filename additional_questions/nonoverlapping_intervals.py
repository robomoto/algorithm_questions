import pytest

def nonoverlapping_intervals():
    """
    Finds the minimum number of intervals to remove to make the remaining intervals non-overlapping.

    Given a list of intervals, where each interval is represented by a pair [start, end], the task is to determine 
    the minimum number of intervals to remove so that the remaining intervals do not overlap.

    Args:
        intervals (List[List[int]]): A list of intervals, each represented by [start, end].

    Returns:
        int: The minimum number of intervals that need to be removed to make the remaining intervals non-overlapping.
    """

    pass

def test_nonoverlapping_intervals():
    result = nonoverlapping_intervals()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
