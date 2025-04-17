import pytest

def zero_one_matrix():
    """
    Given a binary matrix, returns a matrix where each cell contains the distance to the nearest 0.

    The distance between two adjacent cells is 1. Each cell in the output matrix represents the
    minimum number of steps to reach the nearest 0 in the input matrix.

    Args:
        mat (List[List[int]]): A 2D list of binary values (0s and 1s).

    Returns:
        List[List[int]]: A 2D list where each cell contains the distance to the nearest 0.
    """

    pass

def test_zero_one_matrix():
    result = zero_one_matrix()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
