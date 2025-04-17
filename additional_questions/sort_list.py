import pytest

def sort_list():
    """
    Sorts a list of integers.

    Given a list of integers, the task is to sort the list in ascending order.

    Args:
        nums (List[int]): A list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers in ascending order.
    """

    pass

def test_sort_list():
    result = sort_list()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
