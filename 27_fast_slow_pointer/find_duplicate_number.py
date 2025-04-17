import pytest

def find_duplicate_number():
    """
    Finds the duplicate number in an array where each number appears once except for one number which appears twice.

    The array contains `n + 1` integers, where each integer is between 1 and `n` (inclusive). 
    The task is to identify the duplicate number in the array.

    Args:
        nums (List[int]): A list of integers where one number appears twice and all others appear once.

    Returns:
        int: The duplicate number in the array.
    """

    pass

def test_find_duplicate_number():
    result = find_duplicate_number()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
