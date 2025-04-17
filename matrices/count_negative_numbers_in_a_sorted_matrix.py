import pytest

def count_negative_numbers_in_a_sorted_matrix():
    """
    Counts the number of negative numbers in a sorted matrix.

    Given an m x n matrix where each row is sorted in non-decreasing order and the last element of each row is negative,
    the task is to find the number of negative numbers in the matrix.

    Args:
        matrix (List[List[int]]): A 2D list representing the matrix, where each row is sorted in non-decreasing order.

    Returns:
        int: The number of negative numbers in the matrix.
    """

    pass

def test_count_negative_numbers_in_a_sorted_matrix():
    result = count_negative_numbers_in_a_sorted_matrix()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
