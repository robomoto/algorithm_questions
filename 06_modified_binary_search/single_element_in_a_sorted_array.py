import pytest

def single_element_in_a_sorted_array():
    """
    Finds the single element in a sorted array that appears only once.

    Given a sorted array where every element appears twice except for one element, the task is to find the single
    element that appears only once. The array is sorted, and the solution should be efficient.

    Args:
        nums (List[int]): A sorted list where each element appears twice except for one element.

    Returns:
        int: The single element that appears only once in the array.
    """

    pass

def test_single_element_in_a_sorted_array():
    result = single_element_in_a_sorted_array()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
