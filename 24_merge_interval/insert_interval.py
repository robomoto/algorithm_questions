import pytest

def insert_interval():
    """
    Inserts a new interval into a list of non-overlapping intervals and merges any overlapping intervals.

    Given a list of non-overlapping intervals and a new interval, the task is to insert the new interval into the list,
    merging any overlapping intervals if necessary. The list of intervals is sorted by the starting time.

    Args:
        intervals (List[Tuple[int, int]]): A list of non-overlapping intervals, each represented by a tuple of start and end times.
        newInterval (Tuple[int, int]): The new interval to insert, represented as a tuple of start and end times.

    Returns:
        List[Tuple[int, int]]: A list of merged intervals after inserting the new interval.
    """

    pass

def test_insert_interval():
    result = insert_interval()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
