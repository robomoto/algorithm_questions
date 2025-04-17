import pytest

def find_all_duplicates_in_an_array():
    """
    Finds all duplicate elements in an array.

    Given an array of integers, the task is to find all the elements that appear more than once in the array. 
    The solution should return all duplicates without any duplicates in the output list.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        List[int]: A list containing all the elements that appear more than once in the array.
    """

    pass

def test_find_all_duplicates_in_an_array():
    result = find_all_duplicates_in_an_array()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
