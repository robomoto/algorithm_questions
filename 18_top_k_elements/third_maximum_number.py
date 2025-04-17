import pytest

def third_maximum_number():
    """
    Finds the third maximum number in a list of integers.

    Given a list of integers, the task is to find the third largest number in the list. If the list contains less than 
    three distinct numbers, return the maximum number instead.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        int: The third maximum number in the list, or the maximum number if there are less than three distinct numbers.
    """

    pass

def test_third_maximum_number():
    result = third_maximum_number()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
