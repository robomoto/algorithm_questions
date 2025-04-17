import pytest

def next_greater_element_i():
    """
    Finds the next greater element for each element in a given list.

    Given two lists, `nums1` and `nums2`, the task is to find the next greater element for each element in `nums1` 
    based on their position in `nums2`. The next greater element for an element `x` in `nums1` is the first element 
    in `nums2` that is greater than `x`. If no such element exists, return -1.

    Args:
        nums1 (List[int]): A list of integers for which the next greater element is to be found.
        nums2 (List[int]): A list of integers where the next greater element is searched.

    Returns:
        List[int]: A list where each element is the next greater element from `nums2` for each element in `nums1`.
    """

    pass

def test_next_greater_element_i():
    result = next_greater_element_i()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
