import pytest

def find_subsequence_of_length_k_with_the_largest_sum():
    """
    Finds the subsequence of length k with the largest sum.

    Given an array of integers and an integer k, the task is to find the subsequence of length k that has the largest sum. 
    The subsequence must maintain the relative order of elements from the original array.

    Args:
        nums (List[int]): The list of integers.
        k (int): The length of the subsequence to find.

    Returns:
        List[int]: The subsequence of length k with the largest sum.
    """

    pass

def test_find_subsequence_of_length_k_with_the_largest_sum():
    result = find_subsequence_of_length_k_with_the_largest_sum()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
