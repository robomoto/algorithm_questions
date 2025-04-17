import pytest

def longest_increasing_subsequence():
    """
    Finds the length of the longest increasing subsequence in an array.

    Given an unsorted array of integers, the task is to find the length of the longest subsequence that is strictly 
    increasing. A subsequence is a sequence derived from the array by deleting some or no elements without changing 
    the order of the remaining elements.

    Args:
        nums (List[int]): A list of integers representing the input array.

    Returns:
        int: The length of the longest increasing subsequence.
    """

    pass

def test_longest_increasing_subsequence():
    result = longest_increasing_subsequence()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
